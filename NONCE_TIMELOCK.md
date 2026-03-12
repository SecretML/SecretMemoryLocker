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

