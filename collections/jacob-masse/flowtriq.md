A collection to integrate [Flowtriq](https://flowtriq.com) DDoS detection with CrowdSec:
 - Flowtriq CEF log parser
 - DDoS attack ban scenario (high/critical confidence)
 - Repeated attacker detection scenario

## Acquisition template

Configure CrowdSec to receive Flowtriq CEF syslog alerts:

```yaml
---
source: syslog
listen_addr: 0.0.0.0
listen_port: 514
labels:
  type: cef
```

Or if the FTAgent writes CEF logs to a file:

```yaml
---
filenames:
  - /var/log/flowtriq.log
labels:
  type: cef
```

## How it works

When Flowtriq's FTAgent detects a DDoS attack, it outputs a CEF-formatted syslog message containing the attack details. CrowdSec parses these alerts and creates ban decisions against the attacker source IPs, propagating protection across all connected bouncers.
