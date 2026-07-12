# SML Reference Engine

This directory contains the standalone reference implementation of the **Secret Memory Locker (SML) file encryption engine**.

It is **not** responsible for reconstructing the cryptographic key from memory. The key reconstruction process—including memory-based authentication, encrypted hint capsules, multi-stage (nested) recovery, and Argon2 key derivation—is implemented separately by the main Secret Memory Locker application.

Once the user's memory reconstruction is successfully completed, the application produces a deterministic 256-bit key (`Memory-Derived Key`). This reference engine accepts that existing key and performs authenticated file encryption and decryption using **ChaCha20-Poly1305** together with the SML container format.

The purpose of this code is to provide a minimal, transparent, and independently verifiable implementation of the SML file format, allowing encrypted files to be recovered without requiring the complete Secret Memory Locker application, as long as the correct reconstructed key is available.
