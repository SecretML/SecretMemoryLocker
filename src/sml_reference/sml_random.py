# AI-SML © 2026
# ==========================================================
# SML Engine
# Random Module
# ==========================================================

import secrets


class SMLRandom:
    """
    Cryptographically secure random generator
    for the SML Engine.

    Used for:
        • AES-GCM nonce
        • IV
        • Random bytes
        • Future SML features
    """

    NONCE_SIZE = 12      # AES-GCM standard
    IV_SIZE = 16

    # ======================================================
    # RANDOM BYTES
    # ======================================================

    @staticmethod
    def random_bytes(length: int) -> bytes:
        """
        Returns cryptographically secure random bytes.
        """

        if length <= 0:
            raise ValueError(
                "Length must be greater than zero."
            )

        return secrets.token_bytes(length)

    # ======================================================
    # NONCE
    # ======================================================

    @classmethod
    def nonce(cls) -> bytes:
        """
        Returns a 12-byte AES-GCM nonce.
        """

        return cls.random_bytes(
            cls.NONCE_SIZE
        )

    # ======================================================
    # IV
    # ======================================================

    @classmethod
    def iv(cls) -> bytes:
        """
        Returns a 16-byte IV.
        """

        return cls.random_bytes(
            cls.IV_SIZE
        )

    # ======================================================
    # HEX STRING
    # ======================================================

    @staticmethod
    def random_hex(length: int) -> str:
        """
        Returns a random hexadecimal string.

        Example:
            length=16 -> 32 hex chars
        """

        return secrets.token_hex(length)
		
		
		

		
