# adguardhome-dot-scan

Detect DoT (DNS-over-TLS, port 853) scanners and probers targeting AdGuard Home.

## Description

A legitimate DNS-over-TLS client connects cleanly with a proper TLS handshake. Repeated connection resets from the same IP indicate a scanner or prober testing port 853 without proper TLS support.

Triggers a ban after **5 connection resets within 10 minutes** from the same IP.

## Requirements

Requires the `PumbaLP/adguardhome-dot-errors` parser.

## Tested against

- AdGuard Home v0.107.x
- Confirmed working in production (blocked real scanners)

## MITRE ATT&CK

- T1046 – Network Service Discovery
