<img src="https://github.com/user-attachments/assets/655a0ba9-f1a6-4b44-a815-fa381a20cf62" width="60">


# SecretMemoryLocker (SML)
> **A zero-storage cryptographic system that turns your memory into a secure foundation for keys.**

SecretMemoryLocker is a deterministic system that derives keys and secrets directly from your answers and external entropy. The core principle: **nothing is stored**. Your keys exist only when you compute them.

---

## 🔑 The Dual-Key Concept

SML utilizes a multi-layered access model, separating "what you know" from "what you have."

### 1. Memory Key (Identity Key)
A base key generated **exclusively** from your memory.
* **Source:** User-provided answers only.
* **Purpose:** Identity verification, deterministic password generation, and basic recovery.
* **Security:** Protected by an **Argon2** chain (memory-hard), making brute-force attacks computationally expensive.
* **UI Safety:** In the interface, the key value is always **masked (***)** to prevent visual interception (shoulder surfing).

### 2. PSQ Key (Secure Access Key / 2FA)
A high-entropy cryptographic key built on a two-factor authentication model.
* **Formula:** $PSQ\_Key = KDF(Answers + Container\_Nonce + External\_Entropy)$
* **External Entropy:** Can include biometric data (Face ID / Touch ID), hardware tokens, license keys, or any user-provided binary file.
* **Purpose:** Encrypting highly sensitive data. Without the second factor (the container or biometrics), the key cannot be reconstructed even if the answers are known.

---

## 🌀 Phantom-Step Cascade Method

At the heart of SML lies a unique architecture for cascading computation.



The **PSQ Container** is not just storage; it is a structured object that:
1.  **Stores an encrypted question cascade.**
2.  **Contains a Cryptographic Nonce** (a unique salt) to harden the PSQ Key.
3.  **Implements the Phantom-Step algorithm:** Each computation step is "phantom"—it leaves no digital footprint on the disk and exists only in RAM at the moment of derivation.

```text
[Answers] + [Nonce] + [Biometrics] 
      ↓ 
[Phantom-Step Cascade (Argon2)] 
      ↓ 
[Final PSQ Key]
```

---

## 🛠 Technical Advantages

* **Stateless:** The application has no password database. If you delete the app, not a single bit of information regarding your keys remains on the device.
* **Air-Gap Ready:** Designed for fully offline operation.
* **Entropy Matrices:** Generates character grids that allow you to derive complex passwords for various services deterministically without needing to memorize them.

---

## ⚙️ Design Principles

* **No Keys Stored:** Everything is computed on demand.
* **Memory-Hard:** High-iteration KDF prevents GPU/ASIC acceleration for cracking.
* **Flexible 2FA:** Supports multiple external entropy strategies (Files, Hardware, Biometrics).

---

## ⚠️ Security Notice

The strength of the system depends entirely on the quality of your input:
* **Answer Quality:** Use long, unique phrases. Avoid public or easily guessable information.
* **The 2FA Reality:** Losing your PSQ container or changing your biometric profile will render the PSQ Key unrecoverable. This is a deliberate security feature of a true 2FA system.

---

## 🧩 Summary

**SecretMemoryLocker** is more than a manager; it is a philosophy of **deterministic cryptography**. By combining human memory with external entropy through the **Phantom-Step Cascade**, it provides a secure way to manage secrets without relying on cloud providers or vulnerable local databases.

---
