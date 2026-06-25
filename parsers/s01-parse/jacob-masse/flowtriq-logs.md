Parse [Flowtriq](https://flowtriq.com) DDoS detection alerts in CEF (Common Event Format) over syslog.

Flowtriq is a network DDoS detection platform. When the FTAgent detects an attack, it can output structured alerts in Syslog CEF format. This parser extracts attack metadata including source IP, destination IP, attack type, severity, packets per second, bits per second, and confidence level.

## Prerequisites

This parser requires the `crowdsecurity/cef-logs` raw parser (s00-raw stage) to be installed, which handles the initial CEF header parsing.

## Acquisition template

Example acquisition for Flowtriq CEF syslog output:

```yaml
---
source: syslog
listen_addr: 0.0.0.0
listen_port: 514
labels:
  type: cef
```

Or if writing to a log file:

```yaml
---
filenames:
  - /var/log/flowtriq.log
labels:
  type: cef
```

## Extracted metadata

- `source_ip` - Attacker source IP address
- `destination_ip` - Target destination IP address
- `attack_type` - Type of DDoS attack detected (e.g., SYN Flood, UDP Flood)
- `pps` - Packets per second during the attack
- `bps` - Bits per second during the attack
- `confidence` - Detection confidence level (low, medium, high, critical)
- `protocol` - Network protocol
- `event_severity` - CEF severity level
- `event_name` - Name of the detected event
