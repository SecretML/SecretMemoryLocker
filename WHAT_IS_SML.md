<img src="https://github.com/user-attachments/assets/655a0ba9-f1a6-4b44-a815-fa381a20cf62" width="60">

##  SecretMemoryLocker — Memory-Derived Cryptography

**SecretMemoryLocker (SML)** is a cryptographic system that uses **human memory as a source of entropy**.

Instead of storing secrets, SML allows you to **reconstruct them deterministically from your answers** — with no cloud, no saved keys, and no traditional master password.

---

# 🔑 Core Concepts

## 🧠 Memory-Derived Key (Brain Key)

**Memory Key** is a key that:

* is generated **purely from user answers**
* is always identical for the same inputs
* is **independent of files, containers, or external storage**
* is fully deterministic

```text
Memory Key = Argon2_chain(answers)
```

---

### ✔ Properties

* 🔁 **Deterministic** — can be reconstructed anytime
* ☁️ **Stateless** — nothing is stored
* 🧩 **Universal** — can act as a seed for any feature
* 🔐 **Memory-hard** — protected against brute-force via Argon2

---

### 🚀 Use Cases

Memory Key can be used as:

* a seed for password generation
* a root key for cryptographic systems
* an entropy source for offline secret generation
* a recovery mechanism

---

## 📦 PSQ Key (Phantom-Step Key)

**PSQ Key** is derived from:

* user answers
* **and an additional entropy source**

---

```text
Final Key = KDF(answers + external_entropy)
```

---

### ✔ External Entropy Sources

Instead of relying solely on a container, SML allows flexible second-factor inputs:

* `.psq` container (with encrypted question cascade)
* user-provided file (any binary data)
* license key (`key_pro`)
* biometric-derived input (e.g. Face ID abstraction)
* hardware token / electronic key
* any secret known or owned by the user

---

### ✔ Properties

* 🔐 **2FA model**:

  * something you know → answers
  * something you have → external entropy

* ❌ **Cannot be reconstructed without the second factor**

* 🔄 Supports multiple entropy strategies

* 🧱 Uses Phantom-Step Cascade structure

---

### 🧠 Concept

Even if an attacker knows the answers:

```text
without external entropy → final key cannot be derived
```

---

# 🧩 Memory Echo — System Core

**Memory Echo** is the central interface for working with keys.

---

### 🔍 Features

* 🔒 Hidden display of:

  * Memory Key
  * PSQ Key

* 🔄 Real-time key updates when answers change

* 🧠 Generates **entropy matrices** for:

  * offline password generation
  * deterministic secret derivation
  * recovery workflows

---

### ⚙️ Design Principles

* no keys are stored
* everything is computed on demand
* fully offline-capable

---

# 🔐 Security Model

SML uses a layered approach:

---

### 🧠 Memory Layer

* based on user answers
* deterministic
* recoverable

---

### 📦 Entropy Layer

* adds a second factor
* binds key derivation to external input
* prevents compromise from answers alone

---

```text
Memory Key → identity / entropy source  
PSQ Key    → secure access key (2FA)
```

---

# 💡 What This Enables

* ❌ No password storage
* ❌ No cloud dependency
* ❌ No traditional master password

---

* ✔ Memory-based recovery
* ✔ Deterministic key generation
* ✔ Strong protection via Argon2 + cascade
* ✔ Fully offline operation

---

# 🚀 Philosophy

> Human memory is a high-entropy source that cannot be extracted like a file.

SML turns that idea into a practical cryptographic system.

---

# ⚠️ Important

Security depends on answer quality:

* use long and unique answers
* avoid public or easily guessable information

---

# 🧩 Summary

**SecretMemoryLocker** is:

* deterministic cryptography without storage
* memory + external entropy combined
* a new approach to secret management

---

