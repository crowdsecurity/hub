Parse [Flowtriq](https://flowtriq.com) DDoS detection alerts in CEF (Common Event Format) over syslog.

Flowtriq is a network DDoS detection platform. When the FTAgent detects an attack, it can output structured alerts in Syslog CEF format. This parser extracts attack metadata including destination IP (the node under attack), attack type, severity, packets per second, and bits per second.

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

- `destination_ip` - Target IP address (the node being attacked)
- `attack_type` - Attack family (e.g., udp_flood, syn_flood, tcp_flood)
- `pps` - Peak packets per second during the attack
- `bps` - Peak bits per second during the attack
- `severity` - Attack severity level (low, medium, high, critical)
- `source_count` - Number of unique source IPs observed
- `incident_id` - Flowtriq incident ID
- `event_severity` - CEF severity level
- `event_name` - Name of the detected event (e.g., DDoS Attack Detected, DDoS Attack Resolved)
