# AI-SML © 2026
# ==========================================================
# SML Engine
# ChaCha20-Poly1305 Cipher
# ==========================================================

import os

from cryptography.hazmat.primitives.ciphers.aead import (
    ChaCha20Poly1305,
)


class SMLCipher:
    """
    ChaCha20-Poly1305 helper.

    Encrypts and decrypts raw bytes.

    Output format:

        nonce (12 bytes)
        +
        ciphertext
    """

    NONCE_SIZE = 12
    KEY_SIZE = 32

    # ======================================================
    # VALIDATE KEY
    # ======================================================

    @classmethod
    def validate_key(cls, key):

        if isinstance(key, str):

            key = bytes.fromhex(key)

        if not isinstance(key, bytes):
            raise TypeError(
                "Key must be bytes or hex string."
            )

        if len(key) != cls.KEY_SIZE:

            raise ValueError(
                f"Invalid key length ({len(key)}). "
                f"Expected {cls.KEY_SIZE} bytes."
            )

        return key

    # ======================================================
    # ENCRYPT BYTES
    # ======================================================

    @classmethod
    def encrypt_bytes(
        cls,
        data: bytes,
        key,
        aad: bytes | None = None,
        nonce: bytes | None = None,
    ) -> bytes:

        key = cls.validate_key(key)

        if nonce is None:
            nonce = os.urandom(cls.NONCE_SIZE)

        cipher = ChaCha20Poly1305(key)

        encrypted = cipher.encrypt(
            nonce,
            data,
            aad,
        )

        return nonce + encrypted

    # ======================================================
    # DECRYPT BYTES
    # ======================================================

    @classmethod
    def decrypt_bytes(
        cls,
        encrypted: bytes,
        key,
        aad: bytes | None = None,
    ) -> bytes:

        key = cls.validate_key(key)

        nonce = encrypted[:cls.NONCE_SIZE]

        ciphertext = encrypted[cls.NONCE_SIZE:]

        cipher = ChaCha20Poly1305(key)

        return cipher.decrypt(
            nonce,
            ciphertext,
            aad,
        )
		
		
		
