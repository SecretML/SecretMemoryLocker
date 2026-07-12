# AI-SML © 2026
# ==========================================================
# test_engine.py
# End-to-End test
# ==========================================================

from pathlib import Path

from sml_hash import SMLHash
from sml_cipher import SMLCipher
from sml_container import SMLContainer


# ==========================================================
# CONFIG
# ==========================================================

# Memory-derived key depends ONLY on your answers. (64 HEX symbols)
# Test key
KEY = (
    "9e8883faaf29efc285626e6596b316e0cc480334ea359efad2d6b499567f3102"
)

BASE_DIR = Path(__file__).parent

SOURCE_FILE = Path("test.jpg")
CONTAINER_FILE = Path("test.sml")
RESTORED_FILE = Path("test_restored.jpg")


# ==========================================================
# ORIGINAL
# ==========================================================

print("=" * 70)
print("SML ENGINE TEST")
print("=" * 70)

original = SOURCE_FILE.read_bytes()

print("\nORIGINAL")

print("File :", SOURCE_FILE.name)
print("Size :", len(original))
print("SHA  :", SMLHash.sha256_bytes(original))


# ==========================================================
# ENCRYPT
# ==========================================================

encrypted = SMLCipher.encrypt_bytes(
    original,
    KEY
)

nonce = encrypted[:12]

ciphertext = encrypted[12:]

print("\nENCRYPT")

print("Nonce :", nonce.hex())
print("Cipher :", len(ciphertext))


# ==========================================================
# CONTAINER
# ==========================================================

container = SMLContainer.pack(
    nonce=nonce,
    ciphertext=ciphertext,
    original_size=len(original),
)

CONTAINER_FILE.write_bytes(container)

print("\nCONTAINER")

print("Saved :", CONTAINER_FILE)
print("Size  :", len(container))


# ==========================================================
# LOAD CONTAINER
# ==========================================================

loaded = CONTAINER_FILE.read_bytes()

info = SMLContainer.unpack(loaded)

print("\nUNPACK")

print("Version :", info["version"])
print("Algorithm :", info["algorithm"])
print("Flags :", info["flags"])
print("Original Size :", info["original_size"])


# ==========================================================
# DECRYPT
# ==========================================================

encrypted_again = (
    info["nonce"] +
    info["ciphertext"]
)

restored = SMLCipher.decrypt_bytes(
    encrypted_again,
    KEY
)

RESTORED_FILE.write_bytes(restored)

print("\nRESTORED")

print("File :", RESTORED_FILE.name)
print("Size :", len(restored))
print("SHA  :", SMLHash.sha256_bytes(restored))


# ==========================================================
# VERIFY
# ==========================================================

print("\nVERIFY")

same_size = len(original) == len(restored)

same_hash = (
    SMLHash.sha256_bytes(original)
    ==
    SMLHash.sha256_bytes(restored)
)

print("Size OK :", same_size)
print("Hash OK :", same_hash)

if same_size and same_hash:

    print("\n✅ ENGINE PASSED")

else:

    print("\n❌ ENGINE FAILED")

print("=" * 70)