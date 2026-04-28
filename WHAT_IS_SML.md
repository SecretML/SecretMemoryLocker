<img src="https://github.com/user-attachments/assets/655a0ba9-f1a6-4b44-a815-fa381a20cf62" width="60">


# SecretMemoryLocker (SML)
> **A zero-storage, deterministic cryptographic system that transforms human memory into a high-entropy security foundation.**

SecretMemoryLocker (SML) allows you to derive cryptographic keys and secrets from your memory and external factors without storing a single byte of sensitive data. It eliminates the need for master passwords, cloud databases, and local vaults.

---
SML v5+ introduces a simple, memory-based interface for creating and opening encrypted capsules.  
It focuses on minimal design, deterministic key generation, and local-only operation.

Below is a preview of the main application window.

<img width="850" alt="SecretMemoryLocker 2026 v5" src="https://github.com/user-attachments/assets/3fc0279f-73b5-4d19-b5d6-9db425816c82" />


---

## 🔑 The Dual-Key Model

SML splits security into two distinct layers, separating **Identity** from **Secure Access**.

### 1. Memory Key (The Identity Layer)

* **Source:** Derived purely from user-provided answers.
* **Logic:** `MemoryKey = Argon2id(answers)`
* **Representation:** Exposed as a concealed 256-bit hash (no raw key material is directly displayed).
* **Use Case:** A deterministic, recoverable entropy source for offline password generation, key derivation, and cryptographic recovery workflows.
  

### 2. PSQ Key (The 2FA Layer)

* **Source:** Derived from user answers combined with an external entropy source (e.g. file, hardware token, or other user-controlled secret).
* **Logic:** `PSQKey = KDF(answers || external_entropy)`
* **Representation:** Exposed as a concealed 256-bit hash (no raw key material is directly displayed).
* **Use Case:** A high-entropy deterministic key for secure encryption, capable of protecting high-value data where knowledge alone is insufficient.

### 📦 PSQ Container Modes

SML supports two operational modes for the PSQ Key, both based on a layered `.psq` container:

#### Mode 1 — Self-Contained Recovery Capsule
- Generates a standalone encrypted `.psq` file (typically a few kilobytes).
- The container stores a cascade of encrypted questions and hints.
- Each layer corresponds to one answer step.
- Total layers = number of questions + 1 (core payload).
- The container enables deterministic recovery without storing any answers.

#### Mode 2 — Bound Secure Archive
- Generates the same `.psq` recovery capsule.
- Additionally creates an encrypted archive (e.g. ZIP), protected by the PSQ Key.
- The archive contains a secret file whose hash is required to unlock the first layer of the `.psq` container.
- This creates a strict dependency between:
  - the user’s memory (answers)
  - and the external secret (file-based entropy)
  
---

## 🌀 Technical Architecture: Phantom-Step Cascade

The core of SML is the **Phantom-Step** mechanism, implemented through a **"Reverse Matryoshka"** encryption structure.

### 1. Cryptographic Stack
* **Data Encryption:** `ChaCha20Poly1305 (AEAD)` — Provides high-speed encryption with built-in ciphertext authentication.
* **Key Derivation (KDF):** `Argon2id` — The industry standard for memory-hard hashing, resistant to GPU/ASIC cracking.
* **Dynamic Salting:** Every derivation step uses a dynamic salt generated via `SHA-256` of the previous answer or the source file's hash.

### 2. The "Reverse Matryoshka" Structure
The `.psq` file is built from the inside out, creating a multi-layered cascade:

* **Core Payload:** Contains the actual keys/secrets alongside **Decoy Data** (honey-data).
* **Encapsulated Layers:** Each user answer acts as a "key" to peel off one layer. Each layer contains:
    1.  The encrypted payload of the next level.
    2.  The text/metadata of the next question.
    3.  **Cryptographic Noise (Padding):** Random data that obfuscates the real size of the payload, making it impossible for an attacker to guess how many layers exist.



---

## 🛡️ Security Model & Principles

* **Zero Storage:** No keys, plain-text answers, or master passwords ever touch the disk.
* **Stateless Operation:** The system computes the state on the fly. No database = no database leaks.
* **Anti-Brute Force:** By using `Argon2id` for *every* step in the cascade, the time required to brute-force a multi-question container grows exponentially.
* **Plausible Deniability:** Thanks to noise padding and decoy data, an attacker cannot prove if they have reached the "real" core or just a trap layer.

---

## 🛠️ Use Cases

* **Stateless Passwords:** Generate unique, high-entropy passwords for any service without storing credentials, using memory as the single source of truth.

* **Secure Recovery:** Use a `.psq` container as a recovery factor that remains cryptographically useless without the exact sequence of user answers.

* **Time-Locked Access (Nonce as Time Source):** Support delayed or conditional access using time-derived hints (e.g. partial nonce disclosure), enabling controlled unlocking scenarios without revealing the full key.

* **Split Secret Architecture:** Separate critical secrets across multiple components (e.g. `.psq` container + encrypted archive), where neither part alone is sufficient for recovery.

* **Controlled Inheritance:** Enable secure transfer of access by distributing different factors (memory + container + external file) across parties or time, supporting verifiable and controlled secret inheritance.

* **Seed Generation:** Create deterministic seeds for cryptocurrency wallets and other cryptographic systems, reproducible solely from memory-derived entropy.

---

## ⚠️ Important

The security of the **Phantom-Step Cascade** relies on:

1. **Entropy:** Security depends on the total entropy of user answers. This can be achieved through different strategies:
   - a small number of long, complex, and highly unique answers  
   - or a larger set of moderately complex answers, where the total number and sequence remain unknown to an attacker  

2. **Factor Integrity:** If an external entropy source (e.g. file, hardware token, or other secret) is used, its loss makes the corresponding **PSQ Key** unrecoverable.

3. **Sequence Sensitivity:** The exact order and structure of answers are part of the key derivation process. Any deviation (reordering, formatting differences, or missing elements) results in a completely different key.

---

© 2026 SecretMemoryLocker. 

All rights reserved.  

Website: https://secretmemorylocker.com  

Contact: secretmemorylocker@gmail.com

