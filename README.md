# 💾 SecretMemoryLocker (SecretML v4.02)

> **Your personal digital vault – protected by your memories.**
---
✅ Download SecretML [![Version](https://img.shields.io/badge/version-4.02-blue.svg)](https://github.com/SecretML/SecretMemoryLocker/releases)

[SecretML v4.02.zip](https://github.com/user-attachments/files/25515889/SecretML.v4.02.zip)

>### 🎭 New Feature: The Vault Quest
We’ve included a pre-configured challenge to demonstrate our **Tri-State Security Logic**. Can you distinguish the truth from the mirage?

**How to test:**
1. **Download** the release and locate the `/Vault` folder.
2. **Launch** the app and click the **"Decrypt"** button.
3. **Select** `quest_protocol.json` and then select `SecretML_Vault.zip`.
4. **Navigate** the three-step cognitive filter:
    - **Truth Path:** Enter 100% accurate data to access the authentic `license.txt`.
    - **Decoy Path:** Enter "plausible" decoy answers to trigger a **Plausible Deniability** event. You'll unlock a **Honey-pot** file, designed to mislead intruders.
    - **MirageLoop:** Any other input leads to an infinite processing loop — wasting an attacker's time without giving away a single bit of error data.

💡 *SecretMemoryLocker — Where memory becomes a labyrinth and security is absolute.*




>## 📜 Previous Versions:
>
# 🚀 SecretMemoryLocker v4.01 Release Notes

### 🛡 Phantom-Step Cascade — Argon2id + ChaCha20-Poly1305
A new multi-layer encryption model delivering the highest level of cryptographic resilience.

**Highlights:**
- **Multi-layer encryption:** Powered by Argon2id (KDF) and ChaCha20-Poly1305 (AEAD).
- **Advanced Logic:** Improved final key derivation and cascade execution.
- **Deterministic Security:** Version-locked crypto parameters for auditable and consistent recovery.

---

### 🎭 Decoy Trigger & Plausible Deniability (PRO)
Build recovery workflows that protect both your data and your narrative.

**Capabilities:**
- **Decoy Activation:** Specific password triggers to reveal "dummy" secret data.
- **Dual-Layer Recovery:** Create files containing both legitimate and decoy layers.
- **Anti-Coercion:** Designed for high-risk environments and real-world threat scenarios.

---

### 📦 Secure `.psq` Recovery Container
A robust container format with embedded vault capabilities.

**Features:**
- **Encrypted Payload:** Secure PSQ container using authenticated encryption.
- **Protected Data Vault:** Embedded architecture for metadata and secret isolation.
- **Deterministic Structure:** Ensures reliable recovery across different environments.

**Example structure:**
``` *.psq
{
  "PSQC": {
    "nonce": "Obbe/L24JZ2VS0RZ",
    "ciphertext": "nUhxVfOiwESyCvKeCWor7Xva7kLpuYWFT/T7kBqeeueWlW4Qauv/eV3hD9rTNainjwa6Cx/215L7LmEI+TPaeLPW9tO3wglYzh605s2P9lHVBlrBTakK9/HZSobMxZCCDlN38Q6cOfDXFVjm6tWQCOfdRCcFdsmIPEhC4kwYQgrqiZPB3rmiZcSEUUx"
  }
}

```
### ⚙️ Security & Engine Improvements
- Enhanced Reliability: Refined cascade processing for fail-safe execution.
- Hardened Workflow: Optimized cryptographic pipelines to prevent side-channel leaks.

💡 Generate robust recovery files with active decoy layers and a protected vault — engineered for elite security requirements.

> SecretMemoryLocker v4.01 — Where memory becomes a labyrinth and security is absolute.
---

## 🎥 Demo Video  
**Your Mind is the Password | How to Encrypt Files Without Storing a Key (SML Demo)**  

[![Watch the demo](https://img.youtube.com/vi/phjM9mlnKF8/0.jpg)](https://www.youtube.com/watch?v=phjM9mlnKF8)

---
## 🚀 What's New in v3.15 — Memory-Sync & Chained Recovery

### 🧠 Memory-Sync (Derived Access Key)
SecretML can now **derive and securely store a session master key** based on your answers — without ever saving the answers themselves.

- One **non-reversible 256-bit Master-Hash**
- Stored securely in the system keyring
- Enables instant access to multiple archives without re-entering answers

---

### 🔐 Per-Archive Unique Encryption
Every encrypted file receives its **own unique password**, even within the same session.

- Archive key = `SHA256(MasterHash + FileHash)`
- File hash is stored in archive metadata (comment)
- No two archives ever share the same encryption key

---

### ⛓ Chained Recovery (Memory Path Protection)
Access to the Master-Key is protected by a **recursive question–answer chain**.

- Each answer decrypts the next step
- No visible structure or plaintext questions
- Partial knowledge is useless

You don’t enter a password —  
**you unlock your own memory.**

---

### 🛡 Zero-Knowledge Security Model
- Answers are **never stored**
- Only derived hashes exist
- Keyring data can be wiped instantly via UI

---

### 🧨 Instant Access Revocation
Removing archive metadata immediately breaks access —  
even if the Master-Key still exists.

A true **cryptographic kill-switch**.

---

## 🧪 Status
- Stable Windows build
- No KDF (test version)
- Ready for real-world usage & testing

---

## 📦 Download
**SecretML v3.15.exe**
>
[SML v3.15.zip](https://github.com/user-attachments/files/25216234/SML.v3.15.zip)
> Memory-based encryption.  
> No passwords. No files. No traces.

---

# 🚀 What's New in v3.10 — Enhanced SML-Seed & AI Security Core

### 🌱 Improved SML-Seed 24 Generation
Your 24-word seed phrases are now stronger and more reliable.

**Enhancements:**
- Increased entropy when generating SML-Seed 24 from archive data.
- More chaotic internal parameters for higher resistance to pattern analysis.
- Fixed multiple bugs related to edge-case seed reconstruction.

---

### 🤖 Expanded AI Question Engine
Security questions now provide deeper variability and stronger protection.

**Upgrades:**
- Larger internal AI dataset for question generation.
- More unique and less predictable question patterns.
- Better personalization without reducing security.

---

### 🛡 PRO Mode — Update Availability Checker
PRO users now see **in-app version availability** and get notified when a new SML release is published.

---
✅ Download SecretML v3.10 

[SML v3.10.zip](https://github.com/user-attachments/files/23565795/SML.v3.10.zip)


<sub>📄 SHA256: eb1b3d7f30a77dcf38057ff9e68b2eb5ed196ba3f7fff4523d73cc0c4a9b2166</sub>

---

# 🚀 What's New in v3.09 — Memory Echo Password Generator (PRO)

### 🧠 Memory Echo Password Generator (PRO)
Generate infinite passwords dynamically — without ever storing them.  

**How it works**:  
- Combines your secret answers + the encrypted file hash (as salt).  
- Produces unique, instantly reproducible passwords for any resource.  

**Steps to use**:  
1. Activate PRO mode.  
2. Select your `*_SMLkey.json` key-file.  
3. Answer your secret questions.  
4. Enter the resource name (e.g. `GMAIL.COM`, `FACEBOOK.COM`).  
5. Get your password instantly.  

---

### 🔐 Password Formats
- **SHA-256 (64 chars)** — maximum entropy, hexadecimal string.  
- **SML-Echo (32 chars)** — mix of uppercase, lowercase, numbers.  

---

### 📌 Key Rules for Resource Names
- **Exact input matters** — same name = same password, even small changes break consistency.  
- **Case insensitive** — `facebook.com` = `FACEBOOK.COM`.  
- **Keep it simple** — e.g. use just `GMAIL.COM`.  

---

### 🛡 Why Memory Echo?
- **On-the-fly** — passwords never stored, exist only during generation.  
- **Offline mode** — once activated, no internet is needed.  
- **Total control** — only you, with answers + key-file, can restore passwords.  

💡 **Pro Tip**: Use Memory Echo to create your **master password** (e.g. for Google Account).  
This ensures **guaranteed recovery** and **unbreakable security** for your entire digital life.

---

## 📸 Interface Preview

<img width="600" height="500" alt="v3 09" src="https://github.com/user-attachments/assets/6deb758c-538c-4f2a-9fcb-be515802d4ba" />

---


# 🚀 What's New in v3.07 — SML-AutoPIN

**Secret Memory Locker v3.07** introduces the groundbreaking **SML-AutoPIN** feature:  

### 🔐 SML-AutoPIN
- **Unlimited passwords** — no need to memorize or manage them manually.  
- Simply **choose a file** — the app will securely archive it with a unique, automatically generated password.  
- To decrypt, just **select the archive** and instantly recover your file.  

This marks a new step towards effortless, memory-powered encryption.

---

# 🚀 What's New in v3.05 — Keyring & Upcoming AutoPIN

**Secret Memory Locker v3.05** introduces important updates and upcoming features:

### 🔑 Keyring Support
- **Purchased key management** — activate or remove your PRO keys directly in the app.  
- Full deletion of key data when removing a key.  
- Improved stability and reliability for key handling.

### 🛠 Improvements
- Several minor bug fixes to enhance overall performance and user experience.

### ⚡ Upcoming Feature: SML-AutoPIN
- **Auto-generated archive passwords** — create encrypted archives without entering a password.  
- Every archive gets a **unique, automatically generated password**.  
- Functionality under internal testing, coming soon.

✅ Try the new **SecretML-Seed** and experience memory-based security!


---

# 🚀 What's New in v3.03 — PRO Mode Upgrades

**Secret Memory Locker v3.03** expands the **PRO mode** with groundbreaking features:

### 🌱 SecretML-Seed
- **SecretML-Seed (12)** — A **12-word seed phrase** generated entirely from your memories. No physical storage required — your mind becomes the secure vault.  
- **SecretML-Seed (24)** — Maximum entropy with a **24-word seed phrase**. Full control, maximum security, and no need to ever write anything down.  

### 🔑 Core Idea
Your **memories + your archive** generate the **final entropy**.  
This means your security lives only in your head — not on paper, not on devices.  

## 📸 Interface Preview
<img width="600" height="500" alt="v3 02" src="https://github.com/user-attachments/assets/601166e3-fc0e-409a-b280-20a8f22a411b" />

---

# 🚀 What's New in v3.02

### 🔑 PRO Mode
- Added **PRO mode**, activated with a license key.  
- A **test key** is included in the package (`license_key.txt`).  
- Upcoming PRO-exclusive innovative features (see below).

⚠️ **Coming very soon**:  
The buttons for the new features are already available in the interface, but the functions are still under internal testing. Stay tuned for activation in the next updates!  

### 🌱 SecretML-Seed
- **Seed phrase generation from memory**:  
  - 12 words (**SecretML-Seed 12**)  
  - 24 words (**SecretML-Seed 24**)  
- A simple and secure way to create recovery phrases without storing them in plain text.

### 🔒 SML-PIN
- New mode that adds a **salt** to the archive password, derived from your license key.  
- Ensures each archive is unique and personalized.

### 🌀 Memory Echo (concept, coming soon)
- **Password generator from memory**.  
- Your memory itself becomes the seed for password generation.  
- Simple logic → endless stream of strong, unique passwords.

---


## 📸 Interface Preview
<img width="600" height="500" alt="v3 02" src="https://github.com/user-attachments/assets/b76f36c4-25b4-48e1-8007-9c968d35c281" />

---


**💡 Upcoming Feature:**  
**SecretML-Seed (SML-Seed)** — your personal recovery key, coming soon and fully functional!

**Secret Memory Locker v2.28** introduces several key updates:

### ✨ New Features
- **Offline question editing** — now you can edit AI-generated questions locally.
- **Pro version development started** — innovative features in progress.  
- **Free basic version** — core functionality remains freely available.  

### 🛠 Improvements
- **Bug fixes** — several minor issues resolved, improving overall performance.  

---

# 🚀 What's New in v2.26 — MirageLoop (SML-ML)

**Secret Memory Locker v2.26** brings important improvements to **MirageLoop (SML-ML)**:

### 🧠 Improvements
- **Smarter MirageLoop** — now monitors decryption attempts more intelligently.  
- **Expanded offline question pool** — more AI-generated questions available locally.  
- **Bug fixes** — several minor issues resolved for smoother operation.  

👉 Experience the enhanced **SML MirageLoop** and stronger protection!
---

# 🚀 What's New in v2.23 — MirageLoop (SML-ML)

**Secret Memory Locker v2.23** introduces the unique **MirageLoop (SML-ML)** feature.  
This is not just an update — it’s a **new reality of protection**.  

### 🔐 How it works
- When a **wrong answer** to a security question is entered — **MirageLoop** activates.  
- Instead of attempting to decrypt real data, the system launches an **infinite loop of AI-generated questions** from a secure local database.  
- To the attacker, it looks like they are making progress by answering question after question.  
- In reality, they are trapped in a **digital maze**, wasting time and resources while your true data remains **untouched and secure**.  

### 🛡 Key Advantage
MirageLoop creates an **illusion of progress** while ensuring that **no real data is ever exposed to risk**.  

---
👉 Try it yourself: enter a wrong answer and watch **SML MirageLoop** in action.

## 🚀 v2.22 – Offline AI Generation Mode  

### ✨ Added
- **New AI-powered mode:** `generate_offline`  
  - Create security questions **locally** using world-class templates.  
  - Pick from an **infinite pool** of questions to build a unique, strongly encrypted archive.  

### 🔧 Improved
- **100% local processing** — no data ever leaves your device.  
- **Flexible question selection** with fully customizable templates.  
- **Backward compatibility** with all previous SecretML archives.  

---

## 📸 Interface Preview

<p float="left">
  <img width="400" height="350" alt="v2.22(1)" src="https://github.com/user-attachments/assets/f1ffc556-19bb-485e-9355-62da48619fa3" />
  <img width="400" height="350" alt="v2.22(2)" src="https://github.com/user-attachments/assets/494b2d1d-fd90-471e-a2e0-60ece07ea9a4" />
</p>

<img width="600" height="500" alt="v2.22(3)" src="https://github.com/user-attachments/assets/0f9cfe36-8303-4306-bf17-1d5591e3772d" />

---
# 🚧 Coming Soon  

## ✨ New Features in SecretMemoryLocker

---

### 🌀 **SML MirageLoop (SML-ML)**  
*Extended security mode – AI-powered illusion defense.*  

🔐 **How it works**  
When an incorrect answer is entered, instead of decrypting anything,  
the system launches an **infinite loop of AI-generated questions** from a secure local base,  
creating the **illusion of progress without touching real data**.  

🤖 **AI-controlled functions**:  
- Checks the **length** of the user's response.  
- **Syllable-level analysis** for realistic reaction.  
- Endless flow of **dynamic, template-based questions**.  

💡 **Advantages**:  
- Confuses and delays potential attackers.  
- 100% local execution — no external data transfer.  
- Highly **realistic illusion of progress** under AI control.  

---

### 🛡 **SML ChainSignal📡**  
*Blockchain-integrated alert system.*  

📩 **Notification channel** (e.g., email, push, or other) is **securely stored inside the encrypted archive**.  
It is **decrypted only during BlockchainMode activation** using a blockchain-derived key, ensuring **privacy and security**.  

✅ **Benefits**:  
- Early warning of archive access or decryption attempts.  
- Fully flexible notification methods — email is just one option.  
- Adds an additional **layer of trust and surveillance** without exposing contact info.  

---
- 🆕 [What's New in v2.14](#)  

SecretMemoryLocker v2.14 introduces the first stage of integration with **AI-powered question generation** to protect your encrypted content even more securely and conveniently.

### ✨ New Features:
- 🧠 **Generate with AI (GPT)** — experimental feature to automatically create security questions using AI (coming soon).
- 📝 **Question generation modes**:
  - `( ) Manual Questions` — enter your own questions and answers.
  - `( ) Generate Offline` — generate questions locally using offline templates.
  - `(•) Generate with AI (GPT)` — let AI generate personalized memory-based questions (future integration).
- 🌐 **Multilingual Support**: English, Español, Українська.
- 🖼 Enhanced UI positioning — main window now opens centered without flickering.
- 🧪 Infrastructure ready for connecting GPT (OpenAI API or local models).

---

## 🔧 Roadmap for AI Integration

- [ ] Connect OpenAI GPT-4 or open-source local LLM.
- [ ] Add fine-tuned prompts based on user language and selected theme (e.g., childhood, preferences, habits).
- [ ] Enable export and preview of AI-generated questions.
- [ ] Add fallback for offline or manual-only mode if no internet.
---


## 📸 Interface Preview
<img width="400" height="350" alt="v2 14" src="https://github.com/user-attachments/assets/6d939f62-c799-461e-b29e-dd8d23d40102" />

---

SecretMemoryLocker v2.12 

🛠 Changelog – v2.12 (2025-07-28)
Fixes & Improvements:

🧩 Fixed UTF-8 filename issue when extracting files with non-Latin characters (e.g., Cyrillic).

📐 Fixed window sizing bug for smaller screen resolutions and DPI settings.

---

## 🆕 What's New in v2.11

🦾 🔒 Version 2.11 introduces a new encryption method **SHA256 Secure Mode-SML**, a patented encryption system that does not require memorizing a password phrase.

### Key features:
- The encryption process uses both the hash of the file (`file_hash`) and your answers.
- Security is independent of the question length — without the core (`file_hash`), brute-force is impossible.
- `file_hash` is stored in the ZIP archive comment as a separate key in the format **SHA256:<hash>**.
- Think of the JSON file as the key and the archive comment as the lock's core — without the core, the lock cannot be opened.
- All data is securely locked: having the JSON and archive without the core is useless.
- You can split the key and the core between different people for extra security.
- Plausible deniability: just remove the archive comment, and the core is irreversibly lost.
- The key and archive can be stored together without risk, as long as the `file_hash` is missing.

The final key for the archive is generated as:  
`final_key = SHA256(SHA256(answer1 + file_hash) + SHA256(answer2 + file_hash) + SHA256(answer3 + file_hash) + ...)`.

---

### 🔍 SHA256 Secure Mode Security Assessment
The SHA256 Secure Mode method combines AES-256-CBC and SHA-256, providing multi-layer protection. The final key is derived from the file hash (`file_hash`) and the user's answers, making brute-forcing the key virtually impossible without both components.

Thanks to its unique structure (combining answer1 + file_hash and an additional "payload"), this method resembles split-knowledge schemes but has no direct analogs among common solutions.

With properly chosen answers (strong passwords), the method offers a high level of cryptographic security and additional features, such as plausible deniability by removing the archive's comment.

---

## 📸 Interface Preview
<img width="350" height="300" alt="v2 11" src="https://github.com/user-attachments/assets/16023cf3-392c-49f9-ab2f-aa91ad54b3ec" />


---

## 🔧 System Requirements

- **OS**: Windows 10/11  
- **Disk Space**: 20 MB  
- **Other**: No installation or internet connection required.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Feedback & Contact

- **Email**: `secretmemorylocker@gmail.com`  
- **Website**: [secretmemorylocker.com](https://secretmemorylocker.com)

---


# SecretMemoryLocker (SecretML v2.03)

**Your personal digital vault – protected by your memories.**

## 🆕 What's New in v2.03

Version 2.03 introduces a new `_info` field in `secret_data.json`, which contains metadata about the file format:  
`"_info": "SecretMemoryLocker v2.03 / Lite-SML"`.

All encrypted content is now stored under a unified `payload` field for better structure and future compatibility.

### New encryption methods:
- ✅ **Lite-SML** — a patented encryption method that does not require memorizing a password phrase.
- 🔧 **SHA256** — in development.
- 🔧 **BlockchainMode** — in development.
- 🔧 **TimeLock** — in development.

---

## 📸 Interface Preview
<img width="400" height="400" alt="v2 03" src="https://github.com/user-attachments/assets/64b5715b-6300-487d-a6fc-8ffe8dd709af" />

---

# SecretMemoryLocker (SecretML v1.05)

**Your personal digital vault – protected by your memories.**

🌐 Read this in: [Українська](README.uk.md)

---

## 📖 About the Project

**SecretMemoryLocker** is a unique offline tool that transforms your personal memories into an unbreakable encryption key. It's designed to securely archive sensitive data and ensure recovery in critical situations.

This guarantees that you — or trusted people like heirs — can access crucial information even if all other passwords are lost.

---

## 🎯 Perfect For

- **Creating a "Digital Will"**: Store instructions or recovery hints for loved ones in case of unexpected events.
- **Protecting Seed Phrases**: Securely store clues to a modified seed phrase (based on the **FakeSeed** concept) instead of saving the phrase itself in plain form.
- **Password Archiving**: Keep important but rarely used passwords safely encrypted.
- **Protecting Any Files**: Encrypt personal documents, images, or any digital data for long-term offline storage.

---

## 🤔 How It Works

1. **Create your questions** — Choose personal questions only you or your trusted ones would know (e.g. "Where did we first meet?", "What was the name of my first pet?").
2. **Enter your answers** — Provide the exact answers to those questions.
3. **Attach your files** — Upload any files you want to encrypt.
4. **Get your archive** — The app generates a unique key from your answers, encrypts everything using AES-256, and produces a protected `.zip` archive.

To decrypt, simply run the program again and enter the exact same answers.

---

## ✨ Key Features

- ✅ **Strong Encryption**: Uses the battle-tested AES-256 algorithm to protect your data.
- ✅ **Memory-Based Key**: The encryption key is generated from a combination of your answers — impossible to guess or brute-force without exact input.
- ✅ **Fully Offline**: No internet connection is required. Everything runs locally on your computer.
- ✅ **No Cloud, No Servers**: Your data stays 100% with you. Nothing is uploaded anywhere.
- ✅ **Simple Interface**: User-friendly window built with Python/Tkinter.
- ✅ **Two-Layer Data Separation**: The app creates two separate files — an encrypted `.zip` archive and a `.json` file with encrypted questions. You can store them in different places (e.g., give the `.json` to a trusted person and keep the `.zip` with the app in a bank vault). Without both files **and** the correct answers, access is impossible.
- 🎯 **Most important:** No keys are ever saved. The key is computed in real-time only when the correct answers are provided.

---

> ❗ **Note:** Windows Defender may show a warning about an "unknown publisher" — this is expected for unsigned apps. The file is safe.

---

## 📸 Interface Preview

<img src="https://github.com/user-attachments/assets/93bf6c1d-1170-42ac-a97e-2ce9e2f08df2" alt="SecretMemoryLocker UI (English)" width="300"/>

---

## 🔧 System Requirements

- **OS**: Windows 10/11  
- **Disk Space**: 20 MB  
- **Other**: No installation or internet connection required.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Feedback & Contact

- **Email**: `secretmemorylocker@gmail.com`  
- **Website**: [secretmemorylocker.com](https://secretmemorylocker.com)







