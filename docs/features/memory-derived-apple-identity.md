<img src="https://github.com/user-attachments/assets/655a0ba9-f1a6-4b44-a815-fa381a20cf62" width="60">

# 🍎 Memory-Derived Apple Identity (MDAI)

Deterministic Apple credential recovery from human memory.

---

## 🧠 Overview

Memory-Derived Apple Identity (MDAI) is a stateless system that allows users to regenerate Apple-related credentials (Apple ID passwords, iOS passcodes, FileVault keys) without storing them anywhere.

Instead of relying on saved passwords or external backups, MDAI derives all credentials from a single master key reconstructed from user memory via the PSQC (Phantom-Step Q&A Cascade) process.

---

## ⚙️ How It Works

1. User reconstructs a master key using memory-based Q&A (PSQC)
2. The master key is used as a root entropy source
3. Deterministic derivation generates service-specific credentials:
   - iPhone passcode
   - Screen Time PIN
   - Apple ID password
   - macOS FileVault recovery key

Each credential is derived using HMAC-based domain separation, ensuring cryptographic independence between services.

---

## 🔐 Key Properties

- **No storage required** — nothing to save, nothing to leak  
- **Deterministic recovery** — same memory → same credentials  
- **Service isolation** — each credential is cryptographically independent  
- **Offline operation** — works without internet access  
- **Human-optimized output** — designed for real-world usability on Apple devices  

---

## 📱 Why This Matters

Modern ecosystems like Apple tightly bind user identity to device access and account credentials. Losing access can result in permanent data loss.

MDAI introduces an alternative model:

> Your memory becomes the root of your digital identity.

No backups. No password managers. No recovery emails.

---

## ⚠️ Security Notes

- Security depends entirely on the entropy of user memory and PSQC reconstruction
- Weak or predictable answers will compromise the system
- This feature assumes a strong upstream AC-AKDF (Argon2-based) process

---

## 🚀 Status

Experimental feature — part of the SML identity research direction.

---
