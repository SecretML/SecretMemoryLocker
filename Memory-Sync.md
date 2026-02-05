# 🔐 Secret Memory Locker — Memory-Sync & Chained Recovery

**Secret Memory Locker** introduces **Memory-Sync**, a cryptographically secure mechanism that allows users to create and manage an unlimited number of encrypted archives **without re-entering personal answers**.

Each archive is protected by a **unique, non-reusable encryption key**, derived from your memories — never stored, never exposed.

---

## 🚀 Feature: Memory-Sync & Chained Recovery

**Memory-Sync** is a seamless encryption system that combines human memory with modern cryptography.  
It ensures that each encrypted file has its own unique key while preserving strong privacy guarantees.

---

## 🛡 Security Benefits

### 🔐 Entropy Boosting
Even short, simple answers are transformed into a **cryptographically strong 256-bit key** using recursive SHA256 hashing.

### 🧠 Zero-Knowledge on Disk
Your answers are **never stored locally**.  
Only a **non-reversible Master-Hash** is kept in the system keyring (e.g., Windows Credential Manager).

### 👤 User-Controlled Privacy
Full control via the **“Delete Session Data”** action instantly wipes all derived keys from the system keyring.

### 🗂 Flexible Recovery Model
- Recovery JSON can be stored anywhere
- Archives remain independent, even within the same session
- Access control is enforced through archive metadata

---

## 🛠 Technical Flow

### 1️⃣ Master-Key Generation (from Recovery JSON)

When recovering access using the encrypted JSON file containing your question–answer chain:

#### 🔹 Entropy Concentration

Each answer is hashed individually:
Hᵢ = SHA256(answerᵢ)
All hashes are concatenated as raw bytes and hashed again:
MasterHash = SHA256(H₁ || H₂ || ... || Hₙ)

➡ Result: **64-character (256-bit) Master-Hash**

#### 🔹 Secure Storage

The `MasterHash` is stored in the system keyring using the `keyring` library.

#### 🔹 Contextual Masking

To identify the correct recovery context without revealing sensitive filenames, the application generates a masked identifier from the source JSON:

secretmemory.json → s_r_m_r_._o_

---

## 🔐 Per-Archive Salting (Unique Keys)

Even if you encrypt **100 files in a single session**, each archive receives a **completely unique password**.

### Encryption Process

1. Before archiving, the file hash is calculated:
H_file = SHA256(file)

2. This hash is written into the **archive comment (metadata)**
3. The final archive key is derived as:

FinalKey = SHA256(MasterHash + H_file)


---

### Decryption Process

1. The application reads `H_file` from the archive metadata
2. Combines it with the active `MasterHash` from the keyring
3. Automatically derives the correct decryption key

---

## 🧨 Access Revocation (Kill-Switch)

Deleting or modifying the archive metadata:

- Instantly breaks access
- Works **even if the Master-Key still exists**
- Requires no re-encryption

This enables fast, metadata-level access revocation.

---

## ⛓ Chained Recovery — The Chain of Knowledge

Access to the Master-Key is protected by a **recursive decryption chain**:

- Each correct answer decrypts the next block
- The previous answer becomes the key for the next stage
- The first answer decrypts the file hash bound to the archive

### 🔒 Security Impact

- Question structure is invisible in advance
- Partial knowledge is useless
- Brute-force attacks are impractical

You don’t simply enter a password —  
**you follow the path of your own memories**.

---

## 🧠 Design Philosophy
---
> Memory-Sync does not store secrets.  
> It remembers *how to remember*.
---
Only derived knowledge exists —  
**never the answers themselves**.



