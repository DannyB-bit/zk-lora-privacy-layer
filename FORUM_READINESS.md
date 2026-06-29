# Forum Readiness Notes

Status: prototype-ready for community review, not production-ready.

Verified locally:
- Python reference proof runner passes.
- Full `python verify_all_proofs.py` suite passes 20/20 runtimes.
- C++ verifier source builds and runs with Clang on Windows amd64.
- Rust WASM verifier builds for `wasm32-unknown-unknown`; artifact captured in `artifacts/milestone1/`.
- `benchmark_milestone1.py` records separate reference proof generation and verification timings.
- Rust operator builds.
- TypeScript operator builds and runs `npm test`.
- Go operator builds and runs `go test` plus `go run . --test`.
- Payment matching logic verifies a decrypted payment event fixture containing `ref:demo_packet_hash_hello_zcash_mesh`.
- The developer treasury split is checked as 2% using integer zatoshi math.
- RAK operator TX/RX logs are summarized in `artifacts/milestone1/rak_operator_log_summary.md`.

Do not overclaim:
- The current scanner does not decrypt shielded memos from the public chain by itself.
- A real Zcash wallet/light-client adapter must supply decrypted payment events.
- Public explorers cannot decrypt shielded Zcash memos.
- RF transmission logs in this repo are demo/operator logs unless backed by Semtech HAL, packet-forwarder, ChirpStack, TTN, Helium, or SDR captures.
- The proof code is a reference/structural prototype, not a production Groth16/halo2/arkworks verifier.

Forum checklist:
- Link to the four repos and this readiness note.
- Link `artifacts/milestone1/README.md` and `docs/milestone1_hardware_layout.md`.
- Say the current milestone proves deterministic packet-reference and 2% fee validation from decrypted events.
- Say the next grant-funded integration is real Zcash testnet/regtest wallet scanning plus hardware RF capture.
- Avoid "fully private", "production", "on-chain verified split", or "live mempool decrypted" language until those pieces are demonstrated.
