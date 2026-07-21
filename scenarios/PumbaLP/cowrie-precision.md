# Cowrie Precision Detection

Aggressive detection scenario and parser collection for the Cowrie Honeypot (SSH/Telnet).

## Description
This collection provides a robust detection framework specifically tailored for Cowrie Honeypots. Unlike standard brute-force scenarios that primarily target failed login attempts, this detection suite focuses on environment discovery and post-exploitation activities. It triggers immediately on both connection attempts (`cowrie-login`) and emulated command executions (`cowrie-command`), routing offending IPs to local remediation profiles.

## Usage
To install both the required parser and the aggressive detection scenario, run the following command:

`cscli collections install PumbaLP/cowrie`

## Configuration
Ensure your CrowdSec `acquis.d/cowrie.yaml` is configured to ingest Cowrie JSON logs:

```yaml
filenames:
  - /opt/cowrie/var/log/cowrie/cowrie.json
labels:
  type: cowrie
