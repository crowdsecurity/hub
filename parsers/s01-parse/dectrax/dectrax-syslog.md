# DECTRAX Syslog Parser

A parser for [DECTRAX](https://dectrax.com) autonomous cyber deception and honeypot decoy telemetry syslog streams.

DECTRAX documentation: https://docs.dectrax.com

## Acquisition template

Example acquisition configuration for syslog ingestion:

```yaml
filenames:
  - /var/log/dectrax.log
labels:
  type: syslog
```
