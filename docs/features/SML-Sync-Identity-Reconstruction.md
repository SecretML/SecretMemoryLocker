<img src="https://github.com/user-attachments/assets/655a0ba9-f1a6-4b44-a815-fa381a20cf62" width="60">

# SML-Sync

SML-Sync is an experimental identity-centric synchronization layer for SecretMemoryLocker that does not store passwords and does not rely on cloud vault services.

Instead of synchronizing secrets, SML-Sync collects lightweight browser identity anchors and uses them as deterministic entropy sources for secret reconstruction.

The feature analyzes local browser profiles and builds identity anchors in the following format:

```text
domain<_>username
```

Examples:

```text
facebook.com<_>user@gmail.com
github.com<_>dev@example.com
```

These values are not passwords. They represent resource identities and are used only as entropy anchors during deterministic secret generation.

---

## How It Works

SML-Sync reads local browser identity traces such as:

* saved login resources
* usernames / emails
* browser profile mappings
* optional semantic resource hints

Important: SML-Sync does not extract, decrypt, store, or use browser passwords. The system operates exclusively on browser identity metadata.

After collection, SecretMemoryLocker combines:

```text
Memory-Derived Key
+
identity anchor
+
generation mode
```

to reconstruct passwords or secrets on demand without storing them.

---

## Stateless Password Reconstruction

Passwords are not synchronized and are not stored in a vault database.

Instead, they are reconstructed deterministically:

```text
password = Generator(
    Memory-Derived Key,
    domain<_>username,
    mode
)
```

This allows complete password reconstruction even after:

* file loss
* cache cleanup
* operating system reinstallation
* device replacement
* missing backups

as long as the correct Memory-Derived Key can be reconstructed.

---

## Supported Modes

SML-Sync supports multiple deterministic output modes:

* MAX
* DEC
* WEB
* B58
* PHR
* TOK
* REC

These modes allow generation of:

* web passwords
* recovery tokens
* phrases
* compact secrets
* deterministic identifiers

---

## Structured Resource Parsing

Identity anchors can also act as lightweight metadata containers.

For example:

```text
facebook.com<_>user@gmail.com
```

contains both:

```text
Resource = facebook.com
Login    = user@gmail.com
```

When secrets are transferred through SML-TL and reconstructed on a target device, SecretMemoryLocker automatically parses the resource string and separates the information into dedicated fields.

This allows the interface to display:

```text
Resource
Login
Password
```

instead of presenting a single combined string.

The separator exists only to improve resource organization and usability. It does not affect password storage because no password is stored.

---

## Browser-Assisted Identity Layer

SML-Sync operates on top of the existing browser ecosystem without modifying the browser or interfering with its password manager.

The feature uses only:

* domain names
* usernames
* browser identity mappings
* resource references

This allows existing browser login workflows to be transformed into deterministic reconstruction flows without storing the secrets themselves.

---

## Local-Only Architecture

SML-Sync works locally and does not alter the existing browser ecosystem.

The system:

* does not store passwords
* does not upload secrets
* does not use remote vaults
* does not require online accounts
* does not depend on centralized synchronization servers

Identity anchors remain local and may optionally be protected by SecretMemoryLocker encryption layers only when a resource is actively used.

---

## SML-TL Integration

SML-Sync integrates with SML-TL (Stateless Optical Transport), an experimental protocol for transferring secrets between devices without using:

* clipboard sharing
* cloud storage
* persistent network connections

The transfer process uses:

* local secret generation
* time-aligned reconstruction
* volatile browser memory
* stateless QR transport

After reconstruction on the target device, the user receives:

```text
Resource
Login
Password
```

without exposing the Memory-Derived Key or permanently storing the generated secret.

---

## Experimental Status

SML-Sync is an experimental feature exploring:

```text
identity-based deterministic secret reconstruction
```

instead of traditional password storage.

The project investigates how existing browser identity systems can be reused to build stateless cryptographic workflows with minimal secret persistence, local-only operation, and deterministic recovery.

