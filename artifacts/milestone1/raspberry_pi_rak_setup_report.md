# Raspberry Pi / RAK Setup Report

Status: application-level RAK operator logs present in this repo; reviewer-grade raw LoRa RF evidence is now committed in the dedicated Milestone 1 repo.

Milestone 1 now includes a 3-node hardware layout in `docs/milestone1_hardware_layout.md`. The dedicated Milestone 1 repo contains the strongest physical-layer evidence: RakMiner-A transmitted a deterministic 240-byte raw LoRa payload, RakMiner-B decoded CRC OK packets during the matching TX window, and the received payload SHA-256 matched the transmitted payload SHA-256.

The main repo contains supporting application logs:

- `RAK_MINER_A_REAL_RUN.log`: synchronized TX operator session, one packet transmitted at 903.9 MHz, SF9.
- `RAK_MINER_B_REAL_RUN.log`: synchronized RX operator session, three received packets with RSSI/SNR values.
- `artifacts/milestone1/rak_hardware_bench_photo_20260629.jpg`: owner-supplied bench photo of the RAK/miner hardware setup.
- `artifacts/milestone1/lab_staging_setup_photo_20260629.jpg`: owner-supplied staging/lab setup photo.

Those main-repo logs support the application workflow. The RF success claim should cite the Milestone 1 artifacts under `artifacts/milestone1/hardware_capture/end_to_end_rf_success/`.

## Remaining evidence for later production integrations

- Photo-backed Node A, Node B, and Node C setup.
- Production LoRaWAN packet-forwarder, ChirpStack, TTN, Helium, or SDR captures if the project claims those integrations.
- Real Zcash testnet/regtest wallet scanning that supplies decrypted shielded payment events.
- Production proof integration using gnark, arkworks, halo2, or Zcash circuit code.
