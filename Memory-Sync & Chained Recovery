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

