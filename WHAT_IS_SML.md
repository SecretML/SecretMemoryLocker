<img src="https://github.com/user-attachments/assets/655a0ba9-f1a6-4b44-a815-fa381a20cf62" width="60">


# SecretMemoryLocker (SML)
> **A zero-storage, deterministic cryptographic system that transforms human memory into a high-entropy security foundation.**

SecretMemoryLocker (SML) allows you to derive cryptographic keys and secrets from your memory and external factors without storing a single byte of sensitive data. It eliminates the need for master passwords, cloud databases, and local vaults.

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

* **Seed Generation:** Create deterministic seeds for BIP39/cryptocurrency wallets.
* **Stateless Passwords:** Generate unique, complex passwords for any service using your memory as the only source of truth.
* **Secure Recovery:** Use a `.psq` file as a recovery factor that is useless without the specific sequence of memories.

---

## ⚠️ Important

The security of the **Phantom-Step Cascade** relies on:
1.  **Entropy:** Your answers should be long and non-obvious.
2.  **Factor Integrity:** If you use a physical file as an entropy source, losing that file renders the **PSQ Key** unrecoverable.

---

