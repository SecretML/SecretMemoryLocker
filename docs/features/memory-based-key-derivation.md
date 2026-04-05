 <img src="https://github.com/user-attachments/assets/655a0ba9-f1a6-4b44-a815-fa381a20cf62" width="60">
 
## Memory-Based Key Derivation Architecture (PSQ)

## Overview

SecretMemoryLocker uses a **memory-based key derivation model**, where the final encryption key is **not stored anywhere**, but instead deterministically reconstructed from user knowledge.

The system derives the encryption key from:

* a sequence of user answers
* structured and ordered prompts (stored encrypted)
* a file-bound context

This approach eliminates the need for:

* stored master passwords
* seed phrases
* external key storage

---

## Core Concept

The key idea is:

> The encryption key is a deterministic function of user memory.

Users provide answers to a predefined sequence of questions. These answers are:

* processed in order
* never stored in plaintext
* used as entropy inputs into a memory-hard derivation process

The system ensures:

* **order sensitivity** (sequence matters)
* **full dependency between steps**
* **no independent evaluation of answers**

---

## Input Model

The derivation process operates on:

* `answers[]` — ordered sequence of user responses
* `file_hash` — unique identifier of the protected data
* `encrypted_questions` — stored separately inside the container

### Important properties

* The **order of answers is fixed and preserved**
* Answers are treated as **raw byte inputs**
* No transformations (case normalization, trimming, etc.) are applied automatically

This guarantees:

* deterministic reconstruction
* no ambiguity during key recovery

---

## Versioned Key Derivation Models

### 🔹 V4 — Sequential Argon2 Chain (AC-AKDF)

**Model:**

```
k0 = SHA256(file_hash)
kN = Argon2(answerN, salt = kN-1)
final_key = SHA256(kN)
```

**Characteristics:**

* Simple sequential chaining
* Each answer processed independently with previous state as salt
* File-bound initialization

**Properties:**

* Deterministic
* Memory-hard (Argon2)
* Low implementation complexity
* Easier to audit

**Limitations:**

* Weaker inter-step dependency
* Lower resistance to partial knowledge attacks

---

### 🔹 V5 — Stateful Memory-Hard Cascade (Hardened)

**Model:**

```
k0 = HMAC(user_salt, "init")

for each answer_i:
    input_i = HMAC(k_{i-1}, STEP || index || answer_i)
    salt_i  = SHA256(k_{i-1} || index || total_steps)
    k_i     = Argon2(input_i, salt_i)

final_key = SHA256(HMAC(k_N, file_hash))
```

**Enhancements over V4:**

* Stateful chaining (each step depends on full prior state)
* Domain separation (STEP + index binding)
* Deterministic salt derivation
* Final file binding using HMAC
* Minimum derivation depth enforced

---

## Minimum Depth Guarantee

To avoid weak configurations:

> The system enforces a minimum of 2 derivation steps.

If only one answer is provided:

* an internal deterministic domain step is added

This ensures:

* consistent computational cost
* uniform resistance to brute-force attacks

---

## Security Properties

### 🔐 Memory-Hardness

All derivation steps use Argon2, making attacks:

* memory-expensive
* difficult to parallelize efficiently

---

### 🔗 Sequential Dependency

Each step depends on:

* previous internal state
* step index
* total sequence length

This prevents:

* independent evaluation of answers
* reordering attacks
* partial reconstruction

---

### 🧠 User-Knowledge Binding

The final key depends entirely on:

* correct answers
* correct order
* correct structure

No single answer is sufficient.

---

### 📁 Context Binding

The key is bound to:

* the specific file/container (`file_hash`)

This prevents:

* key reuse across different containers
* cross-target attacks

---

## Threat Model

Assumed attacker capabilities:

* full access to encrypted container
* knowledge of algorithm
* no access to correct answers

Security relies on:

* entropy of user answers
* computational cost of Argon2
* sequential dependency of the cascade

---

## Trade-offs

| Aspect                          | V4     | V5     |
| ------------------------------- | ------ | ------ |
| Simplicity                      | High   | Medium |
| Auditability                    | High   | Medium |
| Resistance to brute-force       | Medium | High   |
| Resistance to partial knowledge | Low    | High   |
| Structural security             | Medium | High   |

---

## Design Philosophy

This system is **not a new cryptographic primitive**.

Instead, it is:

> A structured key derivation pipeline built from standard primitives:

* Argon2
* HMAC-SHA256
* SHA256

The goal is to:

* eliminate stored secrets
* bind encryption to human memory
* enforce computational cost on attackers

---

## Important Notes

* Security depends on the quality of user answers
* Weak or predictable answers reduce protection
* This system complements, but does not replace:

  * strong passwords
  * operational security practices

---

## Summary

SecretMemoryLocker implements a:

> **Stateful, memory-hard, answer-driven key derivation system**

that transforms user knowledge into a deterministic encryption key without ever storing that key.

---
