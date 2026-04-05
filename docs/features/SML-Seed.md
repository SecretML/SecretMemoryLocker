<img src="https://github.com/user-attachments/assets/655a0ba9-f1a6-4b44-a815-fa381a20cf62" width="60">

## 🌱 SecretMemoryLocker-Seed (SML-Seed)

> **Seed without physical storage. Memory becomes the key.**

**SML-Seed** is a memory-bound cryptographic seed generation model where the seed phrase is **not stored anywhere physically or digitally**, but reconstructed deterministically from user memory and system-bound cryptographic context.

-----

## 🧠 Core Idea (Updated Architecture)

Unlike the original version (simple SHA256 aggregation), **SML-Seed now uses Phantom-Step V4/V5 key derivation as its entropy backbone**.

The seed is no longer directly derived from raw Q/A pairs — instead, it is generated from:

  - 🧩 **Phantom-Step Master Key (V4/V5)**
  - 🔐 **File-bound cryptographic context** (`file_hash`)
  - 🧠 **Ordered user answers** (memory sequence)
  - ⚙️ **Internal KDF cascade** (Argon2id-based)

> Memory is no longer just input — it is a structured entropy layer.

-----

## 🔐 System Components

### 📂 `SML.psq`

  - Encrypted question set.
  - Defines deterministic memory structure.
  - Does **NOT** contain answers or secrets.

### 📦 `SML.zip`

  - Encrypted archive of user data.
  - Protected via Memory-Derived Key (SML-Seed output).
  - Can include:
      - documents
      - notes
      - wallet backups
      - media files

### 🧠 Memory Layer

  - User answers exist **only in human memory**.
  - Can optionally be distributed among trusted parties (logical recovery model).
  - No persistent storage required.

-----

## ⚙️ Updated Seed Derivation Model (V4/V5-based)

SML-Seed is now derived through a **Phantom-Step Cascade dependency graph**:

### V4 Derivation

```text
k0 = file_hash_seed

for each answer_i:
    k_i = Argon2(answer_i, salt = k_{i-1})

final_seed = SHA256(k_N)
```

### V5 Derivation

```text
k0 = HMAC(user_salt, "init")

for each answer_i:
    input_i = HMAC(k_{i-1}, STEP || index || answer_i)
    salt_i  = SHA256(k_{i-1} || index || total_steps)
    k_i     = Argon2(input_i, salt_i)

final_key = SHA256(HMAC(k_N, file_hash))
```

**Where:**

  - `file_hash_seed` = `SHA256(SML.zip)`
  - Each step strengthens entropy via stateful chaining.
  - Final output is deterministic and reproducible.

-----

## 🧬 Evolution from Legacy Model

### ❌ Old Model (V3)

```text
Seed = SHA256(SHA256(Q1 + A1 + file_hash) + SHA256(Q2 + A2 + file_hash) + ...)
```

### ✅ New Model (Current)

  - Stateful cascade instead of parallel hashing.
  - Argon2-based memory hardness.
  - Strong inter-step dependency.
  - File-bound entropy initialization.
  - Output Container: `V4/V5.psq` (Phantom-Step Cascade container).

-----

## ⏳ Time-Lock Concept (PSQC Containers)

> **A nonce effectively becomes a source of time.**

Traditional “digital time capsule” services rely on a trusted server that stores encrypted data and releases it after a specific date. This approach has critical weaknesses:

  - The server stores sensitive data.
  - Long-term availability of the service is uncertain.
  - Users must trust the provider not to access the data.

### The SML Approach (Computational Time-Lock)

The **PSQC container model** used in SecretMemoryLocker explores a trustless architecture:

  - **No stored secrets:** The server does **not** store encrypted data or keys — only a nonce (or information derived from it).
  - **Computational delay:** The delay before decryption is enforced by **computational difficulty**, not by server policy.

### PSQC Container Structure

A PSQC file contains a small JSON structure prefixed with `PSQC:`.

```text
PSQC:{
  "nonce_hint": "LEdWTvvka9******",
  "nonce_hash_V1": "48d49beb8cbb82c65d1009fbcbc22c70c1a3dad87a7558b932dfb97ec4f3b928",
  "ciphertext": "..."
}
```

-----

## 🔑 Key Features

### 🧠 Memory-Only Security

> No seed phrase storage anywhere — recovery exists only through structured memory.

### 🔐 Phantom-Step Entropy Binding

Seed depends on:

  - Answer order.
  - Internal state transitions.
  - File hash binding.

### ⏳ Trustless Time-Lock

  - Nonce-based computational delay allows locking the crypto seed by time without physical access to the seed itself or reliance on trusted third parties.

### 📦 Dual-Layer Protection

  - `SML.psq` (structure).
  - `SML.zip` (data vault).

> *Both are useless without memory-based reconstruction.*

### 🌐 Offline-First Design

  - No network dependency.
  - No external key servers.
  - Fully deterministic local computation.

-----

## 🧪 Security Properties

  - **Memory-hard derivation** (Argon2id).
  - **Sequential dependency** (no parallel shortcut attacks).
  - **File-bound entropy isolation**.
  - **No stored seed or master key**.

-----

## 📌 Threat Model

**Assumes attacker has:**

  - Full access to `SML.zip` and `SML.psq` (or PSQC container).
  - Full knowledge of the algorithm.
  - No access to the correct memory answers.

**Security depends on:**

  - Entropy of user memory.
  - Strength of answer unpredictability.
  - Computational cost of the Argon2 cascade.

-----

## ⚠️ Important Notes

  - Weak or predictable answers reduce security significantly.
  - SML-Seed is **not** a replacement for hardware wallets in high-risk custody scenarios.

**Best used as:**

  - Recovery system.
  - Backup entropy layer.
  - Human-centric key reconstruction model.

-----

## 🧩 Use Cases

  - 🪙 **Cryptocurrency wallet recovery** without seed paper.
  - ⏳ **Trustless digital time capsules** for crypto assets (via PSQC computational delay).
  - 🧠 **Human-memory-based authentication** systems.
  - 📦 **Secure offline encrypted archives**.
  - 🎓 **Educational cryptography systems**.

-----

## 🌀 Design Philosophy

> “A seed is not written. A seed is reconstructed.”

SML-Seed transforms cryptographic ownership into a memory-bound deterministic system, eliminating dependency on physical seed storage entirely.
