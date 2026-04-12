# ============================================================
# Secret Memory Locker (SML)
# ------------------------------------------------------------
# Target Use Case (Apple Ecosystem)
# ------------------------------------------------------------
#
# This module is designed for deterministic recovery of
# Apple ecosystem credentials, including:
# - iPhone passcodes
# - Apple ID passwords
# - macOS FileVault recovery keys
#
# It enables offline identity reconstruction for Apple devices
# without relying on iCloud, backups, or password storage.
#
# Core Concept Flow:
# Human Memory
#     ↓
# PSQC Reconstruction
#     ↓
# Master Key (256-bit)
#     ↓
# HMAC-based Deterministic Identity Derivation
#
# NOTE:
# This is an experimental cryptographic identity model and is
# NOT affiliated with Apple Inc.
# ------------------------------------------------------------
#
# © 2026 SecretMemoryLocker.com
# ============================================================

"""
SML (Secret Memory Locker) - Operating Instructions:

1. MASTER SOURCE: 
   - Set 'USE_SML_KEY = True' to use the 256-bit PSQC key (reconstructed from memory).
   - Set 'USE_SML_KEY = False' to use 'USER_SECRET' (manual high-entropy string).

2. CUSTOM OVERRIDES & ENTROPY BRANCHING:
   - 'CUSTOM_IPHONE_PASS' & 'CUSTOM_SCREENTIME_PIN': 
     If left empty (""), the system generates these codes deterministically.
     If you enter a value (e.g., "9999"), the system:
        a) Returns this value as-is for that specific field.
        b) Uses this value as 'salt' to mathematically branch the Final Key.
     WARNING: Changing a custom PIN will change ALL derived complex passwords.

3. SECURITY:
   - This script is stateless. It does not store your secrets. 
   - All operations are local and offline.
"""

import hashlib
import hmac
import sys


# ============================================================
# CONFIGURATION
# ============================================================

# Toggle between PSQC Key or Manual Secret
USE_SML_KEY = False

# Sources
SML_FINAL_KEY = "16ef72c7c5759f257b8fc17d32baffea8540d43d31c93f853aa01bf888239ec8"
USER_SECRET   = "CHANGE_ME_USE_HIGH_ENTROPY_SECRET"

# Custom Overrides
# Entering a value here replaces the generated PIN and modifies global entropy.
CUSTOM_IPHONE_PASS    = ""    # e.g., "123456"
CUSTOM_SCREENTIME_PIN = ""    # e.g., "9999"


# ============================================================
# MASTER KEY RESOLUTION
# ============================================================

def get_master_key() -> str:
    """
    Resolves base master key from either PSQC output or local user secret.
    """
    if USE_SML_KEY:
        return SML_FINAL_KEY

    return hashlib.sha256(
        USER_SECRET.encode("utf-8")
    ).hexdigest()


# ============================================================
# ENTROPY MODIFIER LAYER
# ============================================================

def apply_modifier(master_key_hex: str, modifier: str = "") -> str:
    """
    Applies user-controlled modifier using HMAC-SHA256.
    This creates a unique 'branch' of entropy for all derived credentials.
    """
    if not modifier:
        return master_key_hex

    # Convert hex to bytes to utilize full 256-bit entropy
    key_bytes = bytes.fromhex(master_key_hex)
    
    return hmac.new(
        key_bytes,
        modifier.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()


def build_modifier() -> str:
    """
    Combines custom user inputs into a single salt string.
    """
    parts = [m for m in [CUSTOM_IPHONE_PASS, CUSTOM_SCREENTIME_PIN] if m]
    return "::".join(parts)


# ============================================================
# CORE DERIVATION
# ============================================================

def derive_seed(master_key_hex: str, label: str) -> bytes:
    """
    Derives service-specific seed using HMAC-SHA256 with domain separation.
    """
    key_bytes = bytes.fromhex(master_key_hex)
    return hmac.new(
        key_bytes,
        label.encode("utf-8"),
        hashlib.sha256
    ).digest()


# ============================================================
# CREDENTIAL GENERATORS
# ============================================================

def generate_numeric_code(master_key_hex: str, label: str, length: int = 6, override: str = "") -> str:
    """
    Generates a deterministic numeric code. Returns override if provided.
    """
    if override:
        return override

    seed = derive_seed(master_key_hex, label)
    value = int.from_bytes(seed, "big")

    return str(value % (10 ** length)).zfill(length)


def generate_apple_password(master_key_hex: str, label: str, length: int = 16) -> str:
    """
    Generates an ergonomic Apple-style password.
    Includes at least: 1 Upper, 1 Lower, 1 Digit, 1 Symbol (-).
    Ambiguous characters (0, O, I, l) are excluded.
    """
    seed = derive_seed(master_key_hex, label)
    value = int.from_bytes(seed, "big")

    # Ergonomic pools
    uppers   = "ABCDEFGHJKLMNPQRSTUVWXYZ"
    lowers   = "abcdefghijkmnopqrstuvwxyz"
    digits   = "123456789"
    specials = "-"
    pool     = uppers + lowers + digits + specials
    
    chars = []

    # Ensure requirements are met
    chars.append(uppers[value % len(uppers)]);   value //= len(uppers)
    chars.append(lowers[value % len(lowers)]);   value //= len(lowers)
    chars.append(digits[value % len(digits)]);   value //= len(digits)
    chars.append(specials[value % len(specials)]); value //= len(specials)

    # Fill remaining length
    for _ in range(length - 4):
        chars.append(pool[value % len(pool)])
        value //= len(pool)

    # Deterministic Shuffle (Fisher-Yates)
    result = []
    while chars:
        idx = value % len(chars)
        result.append(chars.pop(idx))
        value //= (len(chars) or 1)

    return "".join(result)


# ============================================================
# TEST SUITE
# ============================================================

def run_test():
    base_key = get_master_key()
    modifier = build_modifier()
    
    # Calculate Final Key based on custom modifications
    final_key = apply_modifier(base_key, modifier)

    print("\n" + "="*50)
    print(" SML MEMORY-DERIVED IDENTITY SYSTEM")
    print("="*50)
    
    print(f"Base Source  : {'PSQC (SML_FINAL_KEY)' if USE_SML_KEY else 'Manual (USER_SECRET)'}")
    print(f"Base Key     : {base_key[:12]}...{base_key[-8:]}")

    if modifier:
        print(f"Modifier Active: '{modifier}'")
        print(f"Branch Key   : {final_key[:12]}...{final_key[-8:]}")
    else:
        print("Modifier     : None (Using default entropy)")

    print("\nDERIVED CREDENTIALS:")
    print(f"1. iPhone Passcode    : {generate_numeric_code(final_key, 'ios_pass_v1', 6, CUSTOM_IPHONE_PASS)}")
    print(f"2. Screen Time PIN    : {generate_numeric_code(final_key, 'ios_st_v1', 4, CUSTOM_SCREENTIME_PIN)}")
    print(f"3. Apple ID Password  : {generate_apple_password(final_key, 'apple_id_v1', 16)}")
    print(f"4. Mac FileVault Key  : {generate_apple_password(final_key, 'mac_fv_v1', 24)}")
    print("="*50 + "\n")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    run_test()
