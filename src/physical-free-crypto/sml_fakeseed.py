# ============================================================
# SecretML: FakeSeed (Blind Shuffle Mapping)
#
# FEATURE: Experimental Zero-Knowledge Paper Backup
# VERSION: 1.0.0 (Experimental)
#
# SECURITY MODEL:
# - This is NOT encryption.
# - This is an obfuscation layer.
# - Use only with 24-word seeds.
# - Not a standalone security solution.
#
# THREAT MODEL:
# - Protects against: accidental exposure of paper backup
# - Does NOT protect against: targeted brute-force or cryptographic attacks
#
# IMPORTANT NOTES:
# - BIP39 seeds have structure and checksum,
# reducing the effective brute-force space.
#
# SECRET REQUIREMENTS:
# - Must be high-entropy (NOT a simple phrase)
# - Recommended: use SML Final Key (256-bit)
#
# DESCRIPTION:
# This tool creates a deterministic "scrambling map" for your
# physical seed phrase. You never enter your words here.
# You only provide a secret (or a key from SML), and the app
# tells you how to rearrange your words on paper.
#
# Even if someone finds your paper backup, they won't know
# the correct order of words without your Secret/Final Key.
#
# © 2026 SecretMemoryLocker.com
# ============================================================


import hashlib
import hmac
import sys

# ==========================================
# CONFIGURATION (Simulation)
# ==========================================

# Option A: Simple manual secret
USER_SECRET = "CHANGE_ME_USE_HIGH_ENTROPY_SECRET"

# Option B: Dynamic key from SML (derived from *.PSQ + Q&A)
# If using SML, the final_key is already a high-entropy hex string.
SML_FINAL_KEY = "3b7ca58e35427da7ce5e927252e65c745ede2ee5d38253e1c66ad31392b02574"

# Logic to choose the source:
# We hash the USER_SECRET to get a 256-bit key, or use SML_FINAL_KEY directly.
#USE_SML_KEY = True 
USE_SML_KEY = False

if USE_SML_KEY:
    final_key = SML_FINAL_KEY
else:
    final_key = hashlib.sha256(USER_SECRET.encode('utf-8')).hexdigest()

MODE_WORDS = 24  # Supports 12 or 24


# ==========================================
# CORE LOGIC: DETERMINISTIC SHUFFLING
# ==========================================

def generate_blind_shuffle_map(key_hex: str, word_count: int = 24) -> list:
    """
    Creates a unique, reproducible map based on the provided key.
    Uses HMAC-SHA256 to ensure the sequence never changes across systems.
    """
    key_bytes = key_hex.encode('utf-8')
    original_positions = list(range(1, word_count + 1))
    
    def secure_sort_key(pos):
        # HMAC creates a unique hash for each index based on your secret key
        return hmac.new(key_bytes, str(pos).encode('utf-8'), hashlib.sha256).digest()
    
    # Sort the list of numbers [1..24] using the crypto-hashes as sort keys
    shuffled = sorted(original_positions, key=secure_sort_key)
    return shuffled


# ==========================================
# PRESENTATION / CLI OUTPUT
# ==========================================

def run_presentation():
    shuffle_map = generate_blind_shuffle_map(final_key, MODE_WORDS)
    
    print("\n" + "="*55)
    print("      SECRET MEMORY LOCKER — FAKESEED MODULE")
    print("="*55)
    print(f"[*] Mode:         {MODE_WORDS} Words Mapping")
    print(f"[*] Source:       {'SML Final Key' if USE_SML_KEY else 'User Secret'}")
    print(f"[*] Key Identity: {final_key[:8]}...{final_key[-8:]}")
    print("-"*55)
    print("[!] SECURITY NOTICE:")
    print("    This mapping is unique to your secret.")
    print("    Your actual seed words NEVER touch this device.")
    print("="*55)

    # --- ENCRYPTION STEP ---
    print("\nSTEP 1: CREATING YOUR SHUFFLED BACKUP")
    print("Take your PHYSICAL paper and write words in this order:\n")
    
    for i, orig_num in enumerate(shuffle_map):
        slot = i + 1
        print(f"  Slot {slot:02d}  <--  Write your ORIGINAL Word #{orig_num:02d}")

    # --- DECRYPTION STEP ---
    print("\n" + "-"*55)
    print("STEP 2: RECOVERING THE REAL SEED")
    print("To reconstruct the BIP39 phrase for your wallet:\n")
    
    # Calculate recovery map
    recovery_map = [0] * MODE_WORDS
    for i, orig_num in enumerate(shuffle_map):
        recovery_map[orig_num - 1] = i + 1

    for i, fake_slot in enumerate(recovery_map):
        real_pos = i + 1
        print(f"  Real Word #{real_pos:02d}  is found in  Slot {fake_slot:02d} on your paper")

    print("="*55)
    print("      ZERO-KNOWLEDGE BACKUP COMPLETE")
    print("="*55 + "\n")

if __name__ == "__main__":
    try:
        run_presentation()
    except KeyboardInterrupt:
        sys.exit(0)
