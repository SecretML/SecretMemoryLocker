<img src="https://github.com/user-attachments/assets/655a0ba9-f1a6-4b44-a815-fa381a20cf62" width="60">

# Invisible Key Technology™

### Memory-Based Cryptography

The core cryptographic technology behind **Secret Memory Locker (SML)**.

This directory contains the standalone reference implementation of the **Secret Memory Locker (SML)** file encryption engine, built around the concept of **Invisible Key Technology™**.

Unlike conventional encryption software, this engine does **not** generate, store, display, or manage cryptographic keys.

The cryptographic key is reconstructed separately by the main Secret Memory Locker application through memory-based authentication, encrypted hint capsules, multi-stage (nested) recovery, and Argon2 key derivation. Until this reconstruction is successfully completed, **the encryption key effectively does not exist**.

The user never has to memorize, write down, copy, or manually handle the cryptographic key itself. Instead, the application deterministically reconstructs a 256-bit **Memory-Derived Key** (represented internally as a 64-character hexadecimal value) only when it is required for cryptographic operations.

This reference engine accepts that reconstructed key and performs authenticated file encryption and decryption using **ChaCha20-Poly1305** together with the SML container format.

The purpose of this code is to provide a minimal, transparent, and independently verifiable implementation of the SML file format, allowing encrypted files to be recovered without requiring the complete Secret Memory Locker application, **provided the same memory-derived key can be reconstructed again**.

---

### **Secret Memory Locker™**

**Your key doesn't exist... until you need it.**
