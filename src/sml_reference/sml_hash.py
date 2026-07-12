#АІ-SML © 2026 All rights reserved.

# AI-SML © 2026
# ==========================================================
# SML Engine
# Hash Module
# ==========================================================

from pathlib import Path
import hashlib


class SMLHash:
    """
    SHA-256 helper for the SML Engine.

    Supports hashing:
        • text (UTF-8)
        • bytes
        • files (streaming)

    The file hashing method reads data in chunks,
    allowing very large files to be processed without
    loading them entirely into memory.
    """

    CHUNK_SIZE = 1024 * 1024      # 1 MB

    # ======================================================
    # SHA256 TEXT
    # ======================================================

    @staticmethod
    def sha256_text(text: str) -> str:
        """
        Returns SHA256 of UTF-8 text.
        """

        return hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

    # ======================================================
    # SHA256 BYTES
    # ======================================================

    @staticmethod
    def sha256_bytes(data: bytes) -> str:
        """
        Returns SHA256 of bytes.
        """

        return hashlib.sha256(
            data
        ).hexdigest()

    # ======================================================
    # SHA256 FILE
    # ======================================================

    @classmethod
    def sha256_file(cls, file_path) -> str:
        """
        Calculates SHA256 of a file.

        The file is read in streaming mode.

        Parameters
        ----------
        file_path : str | Path

        Returns
        -------
        str
            SHA256 hex digest.
        """

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(file_path)

        sha = hashlib.sha256()

        with file_path.open("rb") as file:

            while True:

                chunk = file.read(
                    cls.CHUNK_SIZE
                )

                if not chunk:
                    break

                sha.update(chunk)

        return sha.hexdigest()
		
		
		
		
		
