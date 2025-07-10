# SecretMemoryLocker (SecretML v1.05)

**Your personal digital vault – protected by your memories.**

🌐 Read this in: [Українська](README.uk.md)

---

## 📖 About the Project

**SecretMemoryLocker** is a unique offline tool that transforms your personal memories into an unbreakable encryption key. It's designed to securely archive sensitive data and ensure recovery in critical situations.

This guarantees that you — or trusted people like heirs — can access crucial information even if all other passwords are lost.

---

## 🎯 Perfect For:

- **Creating a "Digital Will"**: Store instructions or recovery hints for loved ones in case of unexpected events.
- **Protecting Seed Phrases**: Securely store clues to a modified seed phrase (based on the **FakeSeed** concept) instead of saving the phrase itself in plain form.
- **Password Archiving**: Keep important but rarely used passwords safely encrypted.
- **Protecting Any Files**: Encrypt personal documents, images, or any digital data for long-term offline storage.

---

## 🤔 How It Works

The process is simple and secure:

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

> ❗️ **Note:** Windows Defender may show a warning about an "unknown publisher" — this is expected for unsigned apps. The file is safe.

---

## 📸 Interface Preview

<img src="https://github.com/user-attachments/assets/93bf6c1d-1170-42ac-a97e-2ce9e2f08df2" alt="SecretMemoryLocker UI (English)" width="300"/>

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
