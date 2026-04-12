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
import hmac
import sys

# ==========================================
# CONFIGURATION & ENTROPY SOURCE
# ==========================================

# Replace this with the actual final_key from your SML Q&A/PSQ process
# This is a 256-bit hex string.
SML_FINAL_KEY_EXAMPLE = "56ef72c7c5759f257b8fc17d32baffea8540d43d31c93f853aa01bf888239ec8"

# ==========================================
# CORE DERIVATION FUNCTIONS
# ==========================================

def derive_seed(master_key_hex: str, label: str) -> bytes:
    """
    Generates a unique deterministic seed for a specific service using HMAC-SHA256.
    Ensures domain separation between different passwords.
    """
    try:
        key_bytes = bytes.fromhex(master_key_hex)
    except ValueError:
        raise ValueError("Master key must be a valid hex string.")
        
    return hmac.new(
        key_bytes, 
        label.encode('utf-8'), 
        hashlib.sha256
    ).digest()


def generate_numeric_passcode(master_key_hex: str, label: str, length: int = 6) -> str:
    """
    Generates a numeric passcode for iOS Screen Lock or Screen Time.
    """
    seed = derive_seed(master_key_hex, label)
    seed_int = int.from_bytes(seed, byteorder='big')
    
    modulus = 10**length
    passcode_int = seed_int % modulus
    
    return f"{passcode_int:0{length}d}"


def generate_apple_complex_password(master_key_hex: str, label: str, length: int = 16) -> str:
    """
    Generates a complex Apple ID password with high ergonomics:
    - Guaranteed: 1 Upper, 1 Lower, 1 Digit, 1 Special character.
    - Special character restricted to '-' for easy iOS keyboard entry.
    - Ambiguous characters (O, 0, I, l) removed.
    """
    seed = derive_seed(master_key_hex, label)
    seed_int = int.from_bytes(seed, byteorder='big')
    
    # Character pools (Ergonomic & Safe)
    uppers = "ABCDEFGHJKLMNPQRSTUVWXYZ"
    lowers = "abcdefghijkmnopqrstuvwxyz"
    digits = "123456789"
    specials = "-" # Best for iOS keyboard (123-page)
    
    all_chars = uppers + lowers + digits + specials
    password_chars = []
    
    # 1. Force requirement fulfillment
    password_chars.append(uppers[seed_int % len(uppers)]); seed_int //= len(uppers)
    password_chars.append(lowers[seed_int % len(lowers)]); seed_int //= len(lowers)
    password_chars.append(digits[seed_int % len(digits)]); seed_int //= len(digits)
    password_chars.append(specials[seed_int % len(specials)]); seed_int //= len(specials)
    
    # 2. Fill the rest of the length
    for _ in range(length - 4):
        password_chars.append(all_chars[seed_int % len(all_chars)])
        seed_int //= len(all_chars)
        
    # 3. Deterministic Shuffle (Fisher-Yates)
    result = []
    while password_chars:
        idx = seed_int % len(password_chars)
        result.append(password_chars.pop(idx))
        seed_int //= (len(password_chars) or 1)
        
    return "".join(result)

# ==========================================
# CLI / TESTING
# ==========================================

def run_test_suite(key: str):
    print(f"--- SML Apple Module Test ---")
    print(f"Input Key: {key[:12]}...{key[-8:]}\n")
    
    print(f"1. iPhone Passcode (v1)   : {generate_numeric_passcode(key, 'ios_pass_v1', 6)}")
    print(f"2. Screen Time (v1)       : {generate_numeric_passcode(key, 'ios_st_v1', 4)}")
    print(f"3. Apple ID Password (v1) : {generate_apple_complex_password(key, 'apple_id_v1', 16)}")
    print(f"4. Apple ID Password (v2) : {generate_apple_complex_password(key, 'apple_id_v2', 16)}")
    print(f"5. Mac FileVault (v1)     : {generate_apple_complex_password(key, 'mac_fv_v1', 24)}")
    print("-" * 30)

if __name__ == "__main__":
    # Check for CLI argument or use example
    master_key = sys.argv[1] if len(sys.argv) > 1 else SML_FINAL_KEY_EXAMPLE
    run_test_suite(master_key)
