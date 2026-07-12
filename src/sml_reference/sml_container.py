# AI-SML © 2026
# ==========================================================
# SML Engine
# SML Container v1
# ==========================================================

import struct


class SMLContainer:
    """
    SecretML Container

    Header (28 bytes):

        MAGIC           4
        VERSION         1
        ALGORITHM       1
        FLAGS           1
        RESERVED        1
        ORIGINAL_SIZE   8
        NONCE           12

    followed by ciphertext.
    """

    MAGIC = b"SML1"

    VERSION = 1

    ALGORITHM_CHACHA20 = 0

    HEADER_FORMAT = "<4sBBBBQ12s"

    HEADER_SIZE = struct.calcsize(
        HEADER_FORMAT
    )

    # ======================================================
    # PACK
    # ======================================================

    @classmethod
    def pack(
        cls,
        nonce: bytes,
        ciphertext: bytes,
        original_size: int,
        algorithm: int = ALGORITHM_CHACHA20,
        flags: int = 0,
    ) -> bytes:

        if len(nonce) != 12:
            raise ValueError(
                "Nonce must be 12 bytes."
            )

        header = struct.pack(
            cls.HEADER_FORMAT,
            cls.MAGIC,
            cls.VERSION,
            algorithm,
            flags,
            0,
            original_size,
            nonce,
        )

        return header + ciphertext

    # ======================================================
    # UNPACK
    # ======================================================

    @classmethod
    def unpack(cls, container: bytes):

        if len(container) < cls.HEADER_SIZE:
            raise ValueError(
                "Invalid container."
            )

        (
            magic,
            version,
            algorithm,
            flags,
            reserved,
            original_size,
            nonce,
        ) = struct.unpack(
            cls.HEADER_FORMAT,
            container[:cls.HEADER_SIZE]
        )

        if magic != cls.MAGIC:
            raise ValueError(
                "Invalid SML signature."
            )

        ciphertext = container[
            cls.HEADER_SIZE:
        ]

        return {
            "version": version,
            "algorithm": algorithm,
            "flags": flags,
            "original_size": original_size,
            "nonce": nonce,
            "ciphertext": ciphertext,
        }
		
		
		
		
