# ============================================================
# SecretMemoryLocker PSQC Tool (nonce_hash_V1 recovery)
# © 2026 SecretMemoryLocker.com
# ============================================================

"""
USAGE:

1. Place your *.PSQ file in the same folder as this script
2. Run:
       python brute_force.py

The tool will automatically detect the first .PSQ file
and start nonce recovery process.
"""

import os
import json
import time
import base64
import hashlib
import itertools
import multiprocessing as mp
from datetime import datetime

# =========================
# CONFIG
# =========================

CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/"
LOG_FILE = "nonce_bruteforce.log"

SAVE_INTERVAL_SEC = 600  # 10 m
PROCESSES = max(2, mp.cpu_count() - 1)

# =========================
# HASH (PSQC RULE)
# =========================

def hash_nonce(candidate: str):
    try:
        raw = base64.b64decode(candidate)
        return hashlib.sha256(raw).hexdigest()
    except Exception:
        return None


# =========================
# LOAD FILE
# =========================

def load_psq():
    for f in os.listdir("."):
        if f.endswith(".psq"):
            with open(f, "r", encoding="utf-8") as file:
                data = file.read()
            if data.startswith("PSQC:"):
                return f, json.loads(data[5:])
    return None, None


# =========================
# LOG
# =========================

def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {msg}\n")


# =========================
# ETA ESTIMATION
# =========================

def estimate_space(n):
    return len(CHARSET) ** n


def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.1f}s"
    if seconds < 3600:
        return f"{seconds/60:.1f}m"
    return f"{seconds/3600:.2f}h"


# =========================
# WORKER
# =========================

def worker(prefix, suffix_len, target_hash, start_idx, step, result_queue):
    total = len(CHARSET)

    for idx in range(start_idx, total ** suffix_len, step):
        combo = []

        x = idx
        for _ in range(suffix_len):
            combo.append(CHARSET[x % total])
            x //= total

        suffix = "".join(reversed(combo))
        candidate = prefix + suffix

        h = hash_nonce(candidate)

        if h == target_hash:
            result_queue.put(candidate)
            return


# =========================
# FIND NONCE
# =========================

def find_nonce(nonce_hint, target_hash):
    unknown = nonce_hint.count("*")
    prefix = nonce_hint.split("*")[0]

    print(f"[i] Prefix: {prefix}")
    print(f"[i] Unknown chars: {unknown}")
    print(f"[i] Charset size: {len(CHARSET)}")
    print(f"[i] Processes: {PROCESSES}")

    space = estimate_space(unknown)

    print("\n==============================")
    print("[ESTIMATE]")
    print(f"Search space: {space:,}")

    # rough estimate (very conservative CPU speed)
    speed_per_sec = 150000  # single-thread baseline guess
    total_speed = speed_per_sec * PROCESSES

    eta_sec = space / total_speed

    print(f"Estimated time: {format_time(eta_sec)}")
    print("==============================\n")

    ctx = mp.get_context("spawn")
    result_queue = ctx.Queue()

    start = time.time()
    last_log = start

    processes = []

    for i in range(PROCESSES):
        p = ctx.Process(
            target=worker,
            args=(prefix, unknown, target_hash, i, PROCESSES, result_queue),
        )
        p.start()
        processes.append(p)

    checked = 0

    while True:
        if not result_queue.empty():
            nonce = result_queue.get()

            for p in processes:
                p.terminate()

            print(f"\n[✓] FOUND NONCE: {nonce}")
            log(f"FOUND: {nonce}")
            return nonce

        now = time.time()

        if now - last_log > SAVE_INTERVAL_SEC:
            speed = checked / (now - start + 1e-9)

            msg = f"Running... Speed ~{int(speed)} ops/sec"
            print(msg)
            log(msg)

            last_log = now

        time.sleep(0.2)


# =========================
# REWRITE FILE
# =========================

def rewrite(file_path, data, nonce):
    new = dict(data)

    new.pop("nonce_hint", None)
    new.pop("nonce_hash_V1", None)

    new["nonce"] = nonce

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("PSQC:" + json.dumps(new))


# =========================
# MAIN
# =========================

def main():
    file_path, data = load_psq()

    if not data:
        print("[!] No PSQC file found")
        return

    nonce_hint = data.get("nonce_hint")
    target_hash = data.get("nonce_hash_V1")

    print("[i] PSQC Brute-force Engine Started")
    print(f"[i] File: {file_path}")

    nonce = find_nonce(nonce_hint, target_hash)

    if nonce:
        rewrite(file_path, data, nonce)
        print("[✓] PSQC updated successfully")
    else:
        print("[!] Not found")


if __name__ == "__main__":
    main()
