### myLifeEcho  
*Encrypted map of your digital life.*

> *“myLifeEcho is not a vault of files — it is a map to where your life exists.”*

---

## The Mission

Traditional password managers help transfer access to online accounts — but they fail when it comes to **real data stored on physical devices**.

Modern digital life is fragmented:
- files on local drives  
- backups across folders  
- critical data hidden in unknown locations  

**myLifeEcho** solves a different problem:

> It does not store your data.  
> It ensures someone can **find and access it when it matters**.

It acts as a **digital legacy navigator**, guiding a trusted person directly to important assets — such as crypto backups, personal archives, or documents — without relying on cloud services.

---

## How It Works

Instead of copying or encrypting large amounts of data, **myLifeEcho** creates a lightweight, encrypted structure describing *where* your important data lives.

### 1. Collect (Builder phase)
You select:
- local files or folders  
- cloud links (optional)  
- notes or instructions  

These are stored temporarily in a secure staging environment for review and editing.

---

### 2. Structure (Map creation)
The system builds a structured “map”:

- file paths  
- references  
- contextual notes  

No actual file content is copied or duplicated.

---

### 3. Secure (PSQ container)
The map is sealed into a **`.psq` container** using SecretMemoryLocker.

Access is protected by **Phantom-Step Cascade**:

- multiple memory-based answers  
- progressive key derivation  
- no stored master password  

At its core is **Argon2id**, ensuring strong resistance against brute-force attacks.

---

### 4. Recover (Unlock phase)
When access is needed:

- the user answers memory-based questions  
- the key is reconstructed step-by-step  
- the container is decrypted  

The result is a **guided map** showing:
- where files are located  
- what to open  
- what actions to take  

---

## Key Principles

### 🧭 Map, not storage
myLifeEcho does not store files — only references and instructions.

---

### 🔐 Access through memory
Security is based on **knowledge that cannot be stored or stolen**:
shared experiences, personal context, human memory.

---

### ☁️ No cloud dependency
All data remains local.  
Nothing is uploaded or synchronized externally.

---

### ⚡ Lightweight by design
A `.psq` file can represent access to terabytes of data while remaining only kilobytes in size.

---

## Optional Features

### Smart Suggestions (Local Analysis)
myLifeEcho can optionally scan common user directories and suggest potentially important files.

- Fully local analysis  
- No data leaves the device  
- User must explicitly confirm selections  

---

## What myLifeEcho is NOT

- ❌ Not a cloud storage system  
- ❌ Not a file encryption tool (by default)  
- ❌ Not a password manager  

---

## What it IS

> A secure, portable, and human-centered way to **preserve access to your digital life**.

---

## Summary

**SecretMemoryLocker** protects data.  
**myLifeEcho** ensures it can be found.

Together, they solve both sides of the same problem:
- security  
- recoverability  
