# SecretMemoryLocker (SecretML v2.14)

**Your personal digital vault – protected by your memories.**

---
## 🆕 What's New in v2.14

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
## 🚀 Download

🧷 Download from:  
✅ GitHub Release (v2.14)  

[SecretML v2.14.zip](https://github.com/user-attachments/files/21482280/SecretML.v2.14.zip)

📄 **SHA256:** `1b0c713ecd17109bd43360312b9ab954827a7d6b96fae73d5e71f1373b1ccd6b`


## 📸 Interface Preview
<img width="400" height="350" alt="v2 14" src="https://github.com/user-attachments/assets/6d939f62-c799-461e-b29e-dd8d23d40102" />

---
## 📜 Previous Versions

SecretMemoryLocker v2.12 

🧷 Download from:  
✅ GitHub Release (v2.12)  

[SecretML v2.14.zip](https://github.com/user-attachments/files/21482280/SecretML.v2.14.zip)

📄 **SHA256:** `1b0c713ecd17109bd43360312b9ab954827a7d6b96fae73d5e71f1373b1ccd6b`

🛠 Changelog – v2.12 (2025-07-28)
Fixes & Improvements:

🧩 Fixed UTF-8 filename issue when extracting files with non-Latin characters (e.g., Cyrillic).

📐 Fixed window sizing bug for smaller screen resolutions and DPI settings.

## 🚀 Download

🧷 Download from:  
✅ GitHub Release (v2.12)  

[SecretML v2.12.zip](https://github.com/user-attachments/files/21474295/SecretML.v2.12.zip)

📄 **SHA256:** `a5ad090870661094046fe8cf54cc502a1cab64e22ba1e338311968680194286f`

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

## 🚀 Download

🧷 Download from:  
✅ GitHub Release (v2.11)  

[**SecretML v2.11.zip**](https://github.com/user-attachments/files/21412514/SecretML.v2.11.zip)

📄 **SHA256:** `00ac67d44d2542fa4b9b9b211e26ce5bf21b0f23c7db0e4625b7a760f5e11e58`

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

## 🚀 Download
🧷 Download from:  
✅ GitHub Release (v2.03)  

[**SecretML v2.03.zip**](https://github.com/user-attachments/files/21366510/SecretML.v2.03.zip)

📄 **SHA256:** `e3cd00891acb3f7a25d112acc48bcdc4460aac019a37b8f62a00904f4a05998e`

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

## 🚀 Download

🧷 Download from:  
- [✅ GitHub Release (v1.05)](https://github.com/SecretML/SecretMemoryLocker/releases/tag/v1.05)  
📄 **SHA256:** `2b9379a32d16f55480ae82aac5fd0d05ccd11937486ddf1c24f0da712b310b57`

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







