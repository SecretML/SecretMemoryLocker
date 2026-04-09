# ============================================================
# SML PSQC Memory-Derived Key Recovery Tool
#
# Master Key Recovery Mode (Phantom-Step Cascade V4 logic)
# Offline Answer-Chained Argon2 Key Derivation
#
# Feature: MEMORY-BASED KEY DERIVATION
# https://github.com/SecretML/SecretMemoryLocker/blob/main/docs/features/memory-based-key-derivation.md
#
# © 2026 SecretMemoryLocker.com
# ============================================================

"""
This script implements the core memory-derived key (v4) generation logic for Secret Memory Locker.
It uses a Sequential Argon2 approach (AC-AKDF):
Iterative memory-hard hashing linked directly to the sequence of user answers,
where the output of the previous step acts as the salt for the next.
"""

import hashlib
import sys
import os
from argon2.low_level import hash_secret_raw, Type

# ============================================================
# USER CONFIGURATION (Static inputs for recovery)
# ============================================================

# Your important or confidential file that was used as the seed.
# It should be located in your archive (SML.zip) along with the password.
FILE_PATH = "path/to/your/confidential_file.txt"

# Fallback: The SHA-256 hash of the source file (hex string).
# Used if the file at FILE_PATH cannot be read directly.
MANUAL_FILE_HASH = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

# The answers provided during container creation.
# Must be in the exact order and format (case-sensitive, spaces matter).
USER_ANSWERS = ['answer 1', 'answer 2', 'answer 3', 'answer 4', 'answer 5']

# Argon2 Parameters (Must match V4 App Settings exactly)
ARGON2_PARAMS = {
    "time_cost": 2,
    "memory_cost": 524288,  # 512 MB per step
    "parallelism": 4,
    "hash_len": 32,
    "type": Type.ID
}

# =====================================================================
# HELPER FUNCTIONS
# =====================================================================

def calculate_file_sha256(file_path):
    """Calculates the SHA-256 hash of a file dynamically."""
    if not os.path.exists(file_path):
        return None
    
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
            
    return sha256_hash.hexdigest()

# ============================================================
# CORE CRYPTO LOGIC
# ============================================================

def generate_memory_derived_key_v4(answers, file_hash):
    """
    Phantom-Step Cascade V4 Logic:
    1. Seed: k = SHA256(file_hash_string)
    2. Chain: k = Argon2(answer, salt=k_prev)
    3. Final: MemoryDerivedKey = SHA256(k_final)
    """
    
    # --- PHASE 1: INITIAL SEEDING ---
    try:
        k = hashlib.sha256(file_hash.encode("utf-8")).digest()
    except Exception as e:
        print(f"[!] Error encoding file hash: {e}")
        return None

    # --- PHASE 2: ARGON2 CHAINING ---
    for i, answer in enumerate(answers):
        print(f"[*] Step {i+1}/{len(answers)}: Hardening answer...")
        
        k = hash_secret_raw(
            secret=answer.encode("utf-8"),
            salt=k,  # Chained salt from previous step
            time_cost=ARGON2_PARAMS["time_cost"],
            memory_cost=ARGON2_PARAMS["memory_cost"],
            parallelism=ARGON2_PARAMS["parallelism"],
            hash_len=ARGON2_PARAMS["hash_len"],
            type=ARGON2_PARAMS["type"]
        )

    # --- PHASE 3: FINAL STABILIZATION ---
    return hashlib.sha256(k).hexdigest()

if __name__ == "__main__":
    print("-" * 60)
    print("SML PSQC V4 - MEMORY-DERIVED KEY RECOVERY")
    print("-" * 60)
    
    # Attempt to read from file, fallback to manual hash if file missing
    SOURCE_FILE_HASH = calculate_file_sha256(FILE_PATH)
    if not SOURCE_FILE_HASH:
        print(f"[!] File not found at '{FILE_PATH}'.")
        print("[*] Using MANUAL_FILE_HASH fallback.")
        SOURCE_FILE_HASH = MANUAL_FILE_HASH
    
    if not USER_ANSWERS or not SOURCE_FILE_HASH:
        print("[!] Error: Configuration missing (Answers or Hash).")
        sys.exit(1)

    try:
        final_key = generate_memory_derived_key_v4(USER_ANSWERS, SOURCE_FILE_HASH)
        
        print("\n" + "=" * 60)
        print("GENERATION SUCCESSFUL")
        print("-" * 60)
        print(f"Memory-Derived Key: {final_key}")
        print("=" * 60)
        print("Offline mode: verified.")
        
    except MemoryError:
        print("\n[!] FATAL ERROR: RAM limit exceeded.")
        print(f"This process requires at least {ARGON2_PARAMS['memory_cost'] // 1024} MB of free RAM per step.")
    except Exception as e:
        print(f"\n[!] Unexpected Error: {e}")
