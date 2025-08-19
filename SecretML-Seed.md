# SecretML-Seed (SML-Seed)

**Seed without physical storage. Memory becomes the key.**

SecretML-Seed is an innovative method for securing cryptocurrency wallets, where the seed phrase does **not require physical or digital storage**.  
Instead:

✅ **SecretML.json** — a set of encrypted security questions.  

✅ **SecretML.zip** — an encrypted archive containing any files you want to protect (documents, notes, videos, or other data) secured with a password.


✅ **Answers exist only in the user’s memory.**  

Thus, even if the files fall into the wrong hands, they remain completely useless without the correct answers.  

## How the Seed is Generated

The seed is deterministically derived from the user’s answers and a selected file:

$$
\mathrm{Seed} = \mathrm{SHA256}\Big(
    \mathrm{SHA256}(\mathrm{question\_1} + \mathrm{answer\_1} + \mathrm{file\_hash}) +
    \mathrm{SHA256}(\mathrm{answer\_2} + \mathrm{file\_hash}) +
    \mathrm{SHA256}(\mathrm{answer\_3} + \mathrm{file\_hash}) + \dots
\Big)
$$

Where:

$$
\mathrm{file\_hash} = \mathrm{SHA256}(\mathrm{YourFile_archive})
$$


## Key Features

📂 **No physical seed** — no need to store paper or USB drives.  

🧠 **Mental key** — the user keeps only their answers in memory.  

🔑 **Dual protection** — JSON with questions + ZIP archive as an additional barrier.  

🔒 **AES-256 + SHA256** — modern cryptography for strong security.  

🌐 **Offline mode** — zero risk of leaks via network.  

## Use Cases

- Cryptocurrency wallet owners who do not want to rely on seed paper.  
- Services offering psychologically-secured recovery access.  
- Educational platforms teaching crypto literacy.
