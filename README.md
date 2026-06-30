---
title: "ZK-LoRa Privacy Layer"
language:
- en
tags:
- zero-knowledge
- zk-snark
- lora
- privacy
- depin
license: mit
---

# ZK-LoRa Privacy Layer

*Zero-Knowledge Proofs for Private AI-to-AI Mesh Networks*

![ZK-LoRa Privacy Layer Logo](./logo.png)

### 📖 Download [ZK_LoRa_Whitepaper.pdf](./ZK_LoRa_Whitepaper.pdf) (18-Page PDF)

> *"The impossible is just code waiting to be written, physics waiting to be rewritten, math a work in progress, and truth waiting to be discovered."*

---

## Overview

The ZK-LoRa Privacy Layer adds **zero-knowledge proof authentication** to the Language-U mesh network. Agents prove they are legitimate network participants **without revealing their hardware identity, private keys, or message contents** to eavesdroppers.

This component combines:
1. **Bitcoin-Style Identity** — ECDSA keypairs (secp256k1) → HASH160 → LoRa phone numbers
2. **Groth16-style ZK-SNARKs** — Prove private key knowledge without revealing it
3. **Proof-of-Useful-Work** — Each packet includes computational proof of agent validity
4. **Unlinkable Transmissions** — Fresh ZK proofs per packet prevent traffic analysis

## Files

| File | Purpose |
| :--- | :--- |
| [WHITEPAPER.md](./WHITEPAPER.md) | Full ZK-LoRa Zcash specification with threat model & security analysis |
| [verify_all_proofs.py](./verify_all_proofs.py) | Master orchestrator verifying ZK proofs across 20 programming languages |
| [run_proof.py](./run_proof.py) | ZK-SNARK prover/verifier implementation + CI proof runner |

## Quick Start

```bash
# Run the proof verification (CI mode)
python run_proof.py --test

# Run the full multi-language verifier
python verify_all_proofs.py

# Run the Milestone 1 benchmark
python benchmark_milestone1.py --iterations 250
```

## Milestone 1 Artifact Pack

Reviewer evidence is collected in [artifacts/milestone1](./artifacts/milestone1/README.md):

| Artifact | Status |
| :--- | :--- |
| `verify_all_proofs.py` report | 20/20 runtimes passing |
| C++ native verifier build/run report | Complete |
| WASM verifier artifact and SHA-256 | Complete |
| Proof generation and verification benchmark | Complete for local reference host |
| 3-node RAK/Raspberry Pi hardware layout | Documented in [docs/milestone1_hardware_layout.md](./docs/milestone1_hardware_layout.md) |
| RAK operator logs | Summarized in [artifacts/milestone1/rak_operator_log_summary.md](./artifacts/milestone1/rak_operator_log_summary.md) |
| End-to-end raw LoRa RF proof | Verified in [zk-lora-milestone-1](https://github.com/DannyB-bit/zk-lora-milestone-1/tree/main/artifacts/milestone1/hardware_capture/end_to_end_rf_success) |

Scope note: this repo proves the Milestone 1 reference prototype and verifier portability. The dedicated Milestone 1 workspace now also contains reviewer-grade raw LoRa RF evidence: RakMiner-A transmitted a deterministic 240-byte payload, RakMiner-B decoded CRC OK packets during the matching TX window, and the received payload SHA-256 matched the transmitted SHA-256. Production gnark/arkworks/halo2 proof integration remains future work.

## Security Properties

| Property | Status |
| :--- | :---: |
| Unlinkable transmissions | ✅ |
| Selective disclosure | ✅ |
| Forward secrecy | ✅ |
| Replay protection | ✅ |
| Hardware fingerprint resistance | ✅ |

## AI-to-AI Mesh Autopilot

A verified autonomous execution log demonstrating mesh communication between RAK-Miner-A and RAK-Miner-B mediated by AI agents is documented in [AI_TO_AI_DEMO.md](./AI_TO_AI_DEMO.md).

## Milestone Workspaces

For structured tracking and evaluation by Zcash Community Grants reviewers, dedicated workspaces are maintained:
- **Milestone 1**: [zk-lora-milestone-1](https://github.com/DannyB-bit/zk-lora-milestone-1) - Prototype, verifier artifacts, and end-to-end RF evidence completed
- **Milestone 2**: [zk-lora-milestone-2](https://github.com/DannyB-bit/zk-lora-milestone-2) - Zcash integration workspace
- **Milestone 3**: [zk-lora-milestone-3](https://github.com/DannyB-bit/zk-lora-milestone-3) - Hardware mesh / field SDK workspace

## License

MIT License — see [LICENSE](./LICENSE)
