# ============================================================
# SecretMemoryLocker PSQC Tool (nonce_hash_V1 recovery)
#
# Offline TimeLock recovery mode (manual / brute-force method)
# Alternative to server-based unlocking
#
# Feature: NONCE TIMELOCK
# https://github.com/SecretML/SecretMemoryLocker/blob/main/docs/features/NONCE_TIMELOCK.md
#
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
CHECKPOINT_FILE = "checkpoint.json"

SAVE_INTERVAL_SEC = 600 # 10 m
PROCESSES = max(2, mp.cpu_count() - 1)

# =========================
# HASH
# =========================

def hash_nonce(candidate: str):
    try:
        raw = base64.b64decode(candidate)
        return hashlib.sha256(raw).hexdigest()
    except:
        return None

# =========================
# LOAD FILE
# =========================

def load_psq():
    for f in os.listdir("."):
        if f.endswith(".psq"):
            with open(f, "r", encoding="utf-8") as file:
                content = file.read().strip()

            if not content.startswith("PSQC:"):
                continue

            try:
                data = json.loads(content.split("PSQC:", 1)[1])
                return f, data
            except:
                return None, None

    return None, None

# =========================
# CHECKPOINT
# =========================

def load_checkpoint(file_name, prefix, unknown):
    if not os.path.exists(CHECKPOINT_FILE):
        return {}

    try:
        with open(CHECKPOINT_FILE, "r") as f:
            data = json.load(f)

        if (
            data.get("file") == file_name
            and data.get("prefix") == prefix
            and data.get("unknown") == unknown
        ):
            return data.get("workers", {})
    except:
        pass

    return {}

def save_checkpoint(file_name, prefix, unknown, workers_progress):
    data = {
        "file": file_name,
        "prefix": prefix,
        "unknown": unknown,
        "workers": workers_progress
    }

    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(data, f)

# =========================
# LOG
# =========================

def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {msg}\n")

# =========================
# UTILS
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

def worker(prefix, suffix_len, target_hash, start_idx, step, result_queue, progress, worker_id):
    total = len(CHARSET)

    try:
        idx = progress.get(str(worker_id), start_idx)

        while idx < total ** suffix_len:

            x = idx
            combo = []

            for _ in range(suffix_len):
                combo.append(CHARSET[x % total])
                x //= total

            suffix = "".join(reversed(combo))
            candidate = prefix + suffix

            h = hash_nonce(candidate)

            if h == target_hash:
                result_queue.put(candidate)
                return

            idx += step

            if idx % 5000 == 0:
                try:
                    progress[str(worker_id)] = idx
                except:
                    return

    except KeyboardInterrupt:
        return

# =========================
# FIND NONCE
# =========================

def find_nonce(file_path, nonce_hint, target_hash):
    unknown = nonce_hint.count("*")
    prefix = nonce_hint.split("*")[0]
    file_name = os.path.basename(file_path)

    print(f"[i] Prefix: {prefix}")
    print(f"[i] Unknown chars: {unknown}")
    print(f"[i] Charset size: {len(CHARSET)}")
    print(f"[i] Processes: {PROCESSES}")

    space = estimate_space(unknown)

    print("\n==============================")
    print("[ESTIMATE]")
    print(f"Search space: {space:,}")

    speed_per_sec = 150000
    total_speed = speed_per_sec * PROCESSES
    eta_sec = space / total_speed

    print(f"Estimated time: {format_time(eta_sec)}")
    print("==============================\n")

    # checkpoint load
    progress_data = load_checkpoint(file_name, prefix, unknown)

    ctx = mp.get_context("spawn")
    manager = ctx.Manager()
    shared_progress = manager.dict(progress_data)

    result_queue = ctx.Queue()

    start = time.time()
    last_save = time.time()

    processes = []

    for i in range(PROCESSES):
        p = ctx.Process(
            target=worker,
            args=(prefix, unknown, target_hash, i, PROCESSES, result_queue, shared_progress, i),
        )
        p.start()
        processes.append(p)

    while True:
        if not result_queue.empty():
            nonce = result_queue.get()

            for p in processes:
                p.terminate()

            # cleanup checkpoint
            if os.path.exists(CHECKPOINT_FILE):
                os.remove(CHECKPOINT_FILE)

            elapsed = time.time() - start

            print("\n==============================")
            print("[RESULT]")
            print(f"Nonce: {nonce}")
            print(f"Time: {elapsed:.2f}s")
            print("Status: SUCCESS")
            print("==============================\n")

            log(f"FOUND: {nonce} | Time: {elapsed:.2f}s")

            return nonce

        now = time.time()

        if now - last_save > SAVE_INTERVAL_SEC:
            save_checkpoint(file_name, prefix, unknown, dict(shared_progress))
            last_save = now

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

    if not nonce_hint or not target_hash:
        print("[!] Invalid PSQC structure")
        return

    print("[i] PSQC Brute-force Engine Started")
    print(f"[i] File: {file_path}")

    try:
        nonce = find_nonce(file_path, nonce_hint, target_hash)
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
        return

    if nonce:
        rewrite(file_path, data, nonce)
        print("[✓] PSQC updated successfully")
    else:
        print("[!] Not found")

if __name__ == "__main__":
    main()
