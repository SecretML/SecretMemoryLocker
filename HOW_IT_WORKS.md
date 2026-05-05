
<img src="logo-SecretMemoryLocker.png" width="80" />

# SML: How It Works (The Memory Echo Example)

**Memory Echo** is a stateless, zero-storage password generation engine. It enables users to generate high-entropy, deterministic passwords of any format for any service without storing a single byte of sensitive data on disk or in the cloud.

## 1. Dual-Key Architecture (Identity & Access)
SML separates security into two independent layers. Users run the offline desktop application and regain access to their "Digital Identity" by answering their own stored and encrypted memory prompts.

### A. Memory Key (Identity Layer)
*   **Source:** Derived exclusively from the user’s memory (answers to personal prompts).
*   **Logic:** $$MemoryKey = Argon2id(answers)$$
*   **Essence:** A deterministic entropy source. If you remember the answers, you hold the key. It is never stored; it is recalculated from scratch every time.

<img width="400"  alt="Memory Key (Identity Layer)" src="https://github.com/user-attachments/assets/f64de187-9c17-44c6-9988-ad46bfc06052" />


### B. PSQ Key (2FA / Secure Access Layer)
*   **Source:** Memory answers combined with an external factor (file-key, hardware token, or secondary secret).
*   **Logic:** $$PSQKey = KDF(answers \parallel external\_entropy)$$
*   **Essence:** A high-entropy key designed to protect high-value data. Knowledge of the answers alone is insufficient without the physical or external factor.

<img width="400" alt="PSQ Key (2FA  Secure Access Layer)" src="https://github.com/user-attachments/assets/41cd2548-3960-400a-a390-afa50a5d31de" />


---

## 2. Memory Echo: The Matrix Engine ("Meat Grinder")
Once the key (Memory or PSQ) is restored, the Memory Echo mechanism is activated. The user enters the resource name (e.g., `google.com` or `work_vpn`).

*   **Input:** Chosen Key + Resource Name.
*   **Matrix Processing:** Data passes through a cascade of cryptographic transformations (KDF), which we refer to as the "Matrix Meat Grinder."
*   **Output:** A unique, cryptographically strong password that exists only in the application's volatile memory (RAM).

This process is **fully deterministic**: the same key combined with the same resource name will always produce the same password. However, without the key, it is computationally impossible to reconstruct the password.

<img width="550" alt="Feature-Memory-Echo" src="https://github.com/user-attachments/assets/864f1fea-1eb1-4b9b-b24c-afb76d4441a9" />


---

## 3. Secure Transport Layer (SML-TL)
Once a password is generated, it must be moved to the target device (e.g., a smartphone) with maximum security. This is handled by the **SML-TL (Time-Lock)** protocol.

<img width="300"  alt="SML-TL" src="https://github.com/user-attachments/assets/23a2456a-4113-46a3-a4f3-e4e75c235ab1" />


### How the Handoff Works:
1.  **Encryption (AES-GCM):** The desktop app encrypts the generated password and resource name.
2.  **Hybrid Key Derivation:** To encrypt the data, the app uses a combination of internal entropy and a dynamic key $k1$, synchronized with the current time bucket:
    $$k1 = SHA256(domain\hash \parallel bucket)$$
3.  **QR Handoff (Air-Gapped):** The encrypted payload (ciphertext + Nonce) is encoded into a single QR code. **No data is transmitted via Wi-Fi, Bluetooth, or cables.** The transfer occurs over an optical channel (phone camera reading the PC screen).
4.  **Decryption & Time-Lock:** The mobile browser scans the QR code. It fetches only the public part of the $k1$ key from a Cloudflare Worker (relevant to the current time bucket). If the link hasn't expired (the bucket is still active), the browser decrypts the data locally.

<img width="300" alt="SML-Time-Lock" src="https://github.com/user-attachments/assets/3510cca9-d35d-494d-b6df-fad626b08288" />


---

## 4. Key Security Advantages

| Advantage | Description |
| :--- | :--- |
| **Stateless** | Nothing is stored. Deleting the app does not result in the loss of passwords. |
| **Zero-Storage** | No password database (Vault) exists to be hacked or stolen. |
| **Air-Gapped** | Passwords move from PC to mobile without using Wi-Fi or cloud buffers. |
| **Time-Limited** | The QR code "self-destructs" after 2 minutes. Even a photo of the screen is useless to an attacker later. |
| **Identity-Driven** | Only the individual who knows the answers to their Memory Prompts can initiate the generation or recovery process. |

**SML Memory Echo** transforms your memory into the world’s most secure and infinite password vault—where the "vault" is the algorithm itself, not a physical medium.
