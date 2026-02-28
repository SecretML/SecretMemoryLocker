# 🛡️ Phantom-Step Cascade (`.psq`)
**When your memory becomes a labyrinth, and security is an illusion.**

**Phantom-Step Cascade** is a proprietary cascade encryption method developed by the **SecretMemoryLocker** team. This unique technology turns your personal memories into a dynamic security architecture, transforming an ordinary file into a recursive cryptographic labyrinth.

Most digital vaults simply lock the door. Phantom-Step Cascade ensures that **the next door doesn't even exist** until you unlock the first one. 

To the rest of the world, your `.psq` vault is a monolithic block of unreadable digital noise. To you, it’s an elegant sequence of steps where each "phantom" layer materializes only at the moment you provide the correct answer.

---

## ✨ Key Features: Security Through Illusion

* **🛑 100% Offline & Zero-Knowledge:** Everything happens strictly on your local device. No data is ever transmitted over the network. Your answers and generated keys exist only "on the fly" in your device's RAM during the creation or decryption process and are instantly wiped afterward.
* **👻 Zero Metadata (Stealth Shell):** The `.psq` file contains no plaintext data—no app version, no first question. The outer shell is encrypted with a master key generated from the unique SHA-256 hash of the target file. Without the original archive, the key file is just a random sequence of bytes.
* **🪆 The Recursive Matryoshka (The Cascade):** The next layer (question and payload) physically does not exist in memory until the previous one is successfully decrypted.
* **🍯 Honey Trap (Plausible Deniability):** If a special "panic" answer is entered, or during a brute-force attempt, the system doesn't throw an error. It simulates success and opens a "basement" with pre-prepared fake data (**Decoy Data**).
* **🌀 MirageLoop:** A hacker trying to brute-force answers falls into an infinite cascade of algorithmically generated fake layers, wasting years of computational power on a journey to nowhere.

---

## ⚙️ Technical Architecture

The process of building a `.psq` file consists of three fundamental stages:

### 1. Cryptographic Stack
* **Data Encryption:** `ChaCha20Poly1305` (AEAD) ensures high-speed encryption and built-in ciphertext authentication.
* **Key Derivation (KDF):** `Argon2id` (the global KDF standard resistant to GPU/ASIC cracking). 
* **Dynamic Salting:** The salt for each Argon2id step is generated dynamically (SHA-256 of the previous answer or the source file hash).



### 2. Internal Structure (The Cascade)
The file is built from the inside out (**Reverse Matryoshka**):
1.  **Core Payload:** Contains the real keys (`real`) and the trap data (`decoy`).
2.  **Inner Layers:** Each user answer is passed through `Argon2id` to derive a key. This key encrypts a packet containing:
    * The encrypted payload of the next level.
    * The text of the next question.
    * Random cryptographic noise (`noise_padding`) to obfuscate the real data size.

### 3. Stealth Shell
After the cascade is assembled, the entire JSON object is encrypted with a final **Outer Key**.
* **Secret:** `source_file_hash` (SHA-256 of the target file/archive).
* **Salt:** Static prefix + `source_file_hash`.
* **Result:** The file receives the `PSQC:` signature marker and is saved with the `.psq` extension.

---

## 🔐 Master Key Generation & Application

After successfully navigating the cascade, the system generates a final key to unlock the main archive or to be used as a master key that works as a deterministic generator for passwords, private cryptocurrency keys, etc. 

SecretML v4 utilizes a multi-stage pipeline to forge a 256-bit Master Key. The system supports two primary derivation modes to adapt to different threat levels:

### 1. Linear Entropy Fusion (Standard)
The baseline protocol optimized for speed. It layers cognitive responses with a physical file hash into a single, memory-hard derivation cycle.

**Final_Key** = `SHA256(`
&nbsp;&nbsp;&nbsp;&nbsp;`SHA256(Answer_1 + File_Hash) +`
&nbsp;&nbsp;&nbsp;&nbsp;`SHA256(Answer_2) + ... +`
&nbsp;&nbsp;&nbsp;&nbsp;`SHA256(Answer_N)`
`)`

---

### 2. Phantom-Step Cascade (High-Assurance)
An advanced engine based on **Sequential Dependency**. In this mode, the system realizes a step-wise decryption cascade: data for Step N does not exist in a readable state until Step N-1 is successfully unlocked.

#### 🛠 Final Key Derivation Logic
The derivation follows a recursive chain where each answer's entropy is fused with the output of the previous cryptographic transformation:

- **Seed₀** = `SHA256(source_file_hash)`
- **K₀** = `Seed₀`
- **K₁** = `Argon2(Answer₁, salt = K₀)`
- **K₂** = `Argon2(Answer₂, salt = K₁)`
- **K₃** = `Argon2(Answer₃, salt = K₂)`
- ...
- **Kₙ** = `Argon2(Answerₙ, salt = Kₙ₋₁)`
- **Final_Key** = `Kₙ`

#### 🛡 Core Properties
- **Sequential Dependency**: Each step strictly depends on the previous Argon2 output, preventing bypass attempts.
- **Memory-Hard Enforcement**: Every layer uses Argon2id to resist GPU/ASIC acceleration.
- **Non-Parallelizable Brute Force**: Steps must be executed strictly in order; the workload cannot be distributed.
- **Deterministic Output**: Identical answers and source file always yield the same Final_Key.
- **Layer-Count Sensitive**: Security complexity scales linearly with the number of answers provided.

#### 📂 Versioning Example
- **Output Container:** `V4.psq` (Phantom Secure Quantum-ready container)
- **Engine Version:** `SecretML v4.03`

💡 *By binding human memory (cognitive entropy) to a physical anchor (file hash) through a recursive cascade, SecretML ensures that the key exists only at the moment of correct recollection.*
---
© 2026 [SecretMemoryLocker.com](https://secretmemorylocker.com) | Phantom-Step Cascade Encryption
