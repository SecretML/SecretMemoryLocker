<img src="https://github.com/user-attachments/assets/655a0ba9-f1a6-4b44-a815-fa381a20cf62" width="60">


# Nonce as a Time Source
### A Time-Lock Concept for PSQC Containers (SecretMemoryLocker)

## Overview

Traditional “digital time capsule” services rely on a trusted server that stores encrypted data and releases it after a specific date. This approach has several weaknesses:

- the server stores sensitive data
- long-term availability of the service is uncertain
- users must trust the provider not to access the data

The **PSQC container model** used in SecretMemoryLocker explores a different architecture:

**the server does not store encrypted data or keys — only a nonce (or information derived from it).**

The delay before decryption is enforced by **computational difficulty**, not by server policy.

In this design, a **nonce effectively becomes a source of time**.

---

# PSQC Container Structure

A PSQC file contains a small JSON structure prefixed with `PSQC:`.

Example:

```text
PSQC:{
  "nonce_hint": "LEdWTvvka9******",
  "nonce_hash_V1": "48d49beb8cbb82c65d1009fbcbc22c70c1a3dad87a7558b932dfb97ec4f3b928",
  "ciphertext": "..."
}
```
## PSQC Container Fields

| Field | Description |
|------|-------------|
| `nonce_hint` | Optional partial hint of the nonce (can reduce search space or assist recovery) |
| `nonce_hash_V1` | Target hash of the real nonce |
| `ciphertext` | Encrypted payload |

The real nonce satisfies:
hash(nonce) == nonce_hash_V1

To unlock the container the system must **discover the nonce**.

---

## Nonce Discovery

The nonce is generated randomly:
nonce = random_bytes()
nonce_hash = SHA256(nonce)

Only `nonce_hash` is stored in the PSQC container.

Unlocking requires searching for the nonce that produces the stored hash:
hash(candidate_nonce) == nonce_hash

The size of the nonce search space defines the computational delay:
time ≈ search_space / attempts_per_second

Thus the nonce effectively becomes a **computational time source**.

---

## Key Derivation

Once the correct nonce is found, it becomes the secret input for a memory-hard key derivation function:
key = Argon2id(
secret = nonce,
salt = file_hash
)

The derived key decrypts the PSQC container.

Algorithms used:

- **KDF:** Argon2id  
- **AEAD:** ChaCha20-Poly1305  
- **Hash:** SHA-256  

---

## Memory-Hard Verification

Every nonce candidate must pass through Argon2id.

Example parameters:
memory_cost = 512 MB – 1 GB
time_cost = 2
parallelism = 4

This makes each verification expensive and significantly reduces the efficiency of large-scale GPU brute-force attacks.

---

## Layered Decryption

PSQC containers may contain multiple sequential layers.

Layer0 → Argon2 → decrypt
↓
Layer1 → Argon2 → decrypt
↓
Layer2 → final payload

Each layer depends on the previous one, partially limiting parallelization and increasing total computational cost.

---

## Dynamic Salt

To prevent precomputation attacks, salts can depend on ciphertext:
salt = hash(ciphertext_chunk)

This binds the key derivation process to the specific encrypted container.

---

## Optional Server Role

A server may optionally store the real nonce and release it later.

Two modes are possible:

### 1. Server-assisted unlock

The server releases the nonce after a time condition.

### 2. Offline unlock

The nonce is discovered by brute-force search.

In both cases the server never stores:

- ciphertext  
- encryption keys  
- plaintext data  

Only nonce information may exist server-side.

---

## Security Properties

This architecture provides:

- no server-side storage of encrypted data  
- no server access to encryption keys  
- computational time-delay  
- memory-hard verification  
- fully offline operation  

The encrypted payload can be stored anywhere:

- locally  
- cloud storage  
- email  
- decentralized storage  

The PSQC container itself is sufficient for unlocking.

---

## Potential Use Cases

- cryptographic time capsules  
- delayed-release secrets  
- privacy-focused digital vaults  
- secure archival storage  
- experimental time-lock encryption systems  

---

## Status

This mechanism is experimental and requires further study regarding:

- brute-force parallelization  
- optimal Argon2 parameters  
- time calibration across hardware  
- practical nonce search spaces
