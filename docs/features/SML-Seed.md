<img src="https://github.com/user-attachments/assets/655a0ba9-f1a6-4b44-a815-fa381a20cf62" width="60">

## 🌱 SecretMemoryLocker-Seed (SML-Seed)
## Seed without physical storage. Memory becomes the key.

**SML-Seed** is a memory-bound cryptographic seed generation model where the seed phrase is **not stored anywhere physically or digitally**, but reconstructed deterministically from user memory and system-bound cryptographic context.

---

## 🧠 Core Idea (Updated Architecture)

Unlike the original version (simple SHA256 aggregation), **SML-Seed now uses Phantom-Step V4/V5 key derivation as its entropy backbone**.

The seed is no longer directly derived from raw Q/A pairs — instead it is generated from:

- 🧩 Phantom-Step Master Key (V4/V5)
- 🔐 file-bound cryptographic context (`file_hash`)
- 🧠 ordered user answers (memory sequence)
- ⚙️ internal KDF cascade (Argon2id-based)

> Memory is no longer just input — it is a structured entropy layer.

---

## 🔐 System Components

### 📂 SecretML.json
- Encrypted question set  
- Defines deterministic memory structure  
- Does NOT contain answers or secrets  

---

### 📦 SecretML.zip
- Encrypted archive of user data  
- Protected via Memory-Derived Key (SML-Seed output)  
- Can include:
  - documents  
  - notes  
  - wallet backups  
  - media files  

---

### 🧠 Memory Layer
- User answers exist **only in human memory**
- Can optionally be distributed among trusted parties (logical recovery model)
- No persistent storage required

---

## ⚙️ Updated Seed Derivation Model (V5-based)

SML-Seed is now derived through a **Phantom-Step Cascade dependency graph**:

```text
k0 = file_hash_seed

for each answer_i:
    k_i = Argon2(answer_i, salt = k_{i-1})

final_seed = SHA256(k_n)
```
Where:

- file_hash_seed = SHA256(SecretML.zip)
- each step strengthens entropy via stateful chaining
- final output is deterministic and reproducible

---
  
🧬 Evolution from Legacy Model

❌ Old Model (Deprecated)
```text
Seed = SHA256(SHA256(Q1 + A1 + file_hash) + SHA256(Q2 + A2 + file_hash) + ...)
```

✅ New Model (Current)
- Stateful cascade instead of parallel hashing
- Argon2-based memory hardness
- Strong inter-step dependency
- File-bound entropy initialization
- Output Container:`V4.psq` (Phantom-Step Cascade container)
  
🔑 Key Features

🧠 Memory-Only Security

No seed phrase storage anywhere — recovery exists only through structured memory.
---

🔐 Phantom-Step Entropy Binding

Seed depends on:

- answer order
- internal state transitions
- file hash binding
  
📦 Dual-Layer Protection
- SML.psq (structure)
- SML.zip (data vault)

Both are useless without memory-based reconstruction.
---
🌐 Offline-First Design
- No network dependency
- No external key servers
- Fully deterministic local computation
---
🧪 Security Properties
- Memory-hard derivation (Argon2id)
- Sequential dependency (no parallel shortcut attacks)
- File-bound entropy isolation
- No stored seed or master key
---
📌 Threat Model
Assumes attacker has:

- full access to .zip and .json
- full knowledge of algorithm
- no access to correct memory answers

Security depends on:

- entropy of user memory
- strength of answer unpredictability
- computational cost of Argon2 cascade
---

⚠️ Important Notes
- Weak or predictable answers reduce security significantly
- SML-Seed is not a replacement for hardware wallets in high-risk custody scenarios
Best used as:
- recovery system
- backup entropy layer
- human-centric key reconstruction model
---

🧩 Use Cases

Cryptocurrency wallet recovery without seed paper


🧠 Human-memory-based authentication systems

📦 Secure offline encrypted archives

🎓 Educational cryptography systems

---

🌀 Design Philosophy

>“A seed is not written. A seed is reconstructed.”

SML-Seed transforms cryptographic ownership into a memory-bound deterministic system, eliminating dependency on physical seed storage entirely.
