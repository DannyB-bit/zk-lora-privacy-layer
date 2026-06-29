# Raspberry Pi / RAK Setup Report

Status: application-level RAK operator logs present; hardware photo and packet-forwarder capture pending.

Milestone 1 now includes a 3-node hardware layout in `docs/milestone1_hardware_layout.md`. This local Windows environment cannot truthfully generate Raspberry Pi photos, Semtech HAL logs, packet-forwarder `rxpk` JSON, or Helium/TTN/ChirpStack gateway captures.

The main repo contains supporting application logs:

- `RAK_MINER_A_REAL_RUN.log`: synchronized TX operator session, one packet transmitted at 903.9 MHz, SF9.
- `RAK_MINER_B_REAL_RUN.log`: synchronized RX operator session, three received packets with RSSI/SNR values.

Those logs support the application workflow, but they do not replace packet-forwarder, Semtech HAL, gateway, or SDR capture evidence.

## Required evidence before claiming physical validation

- Photo-backed Node A, Node B, and Node C setup.
- Raspberry Pi/RAK OS and hardware inventory commands.
- Packet-forwarder, Semtech HAL, Helium, TTN, ChirpStack, or SDR logs showing the RF packet path.
- ZK-LoRa application logs with matching packet reference and timestamp.
- `python verify_all_proofs.py` and `python benchmark_milestone1.py --iterations 250` run on the Pi or RAK host.
