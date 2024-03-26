## Amavis collection

A collection for [Amavis](https://amavis.org/) :
 - amavis parser
 - base scenario to ban IPs sending infected emails

## Acquisition template

Example acquisition for this collection :

> File based
```yaml
filenames:
  - /var/log/amavis.log
  - /var/log/maillog
labels:
  type: syslog
```

> Journalctl based
```yaml
---
source: journalctl
journalctl_filter:
  - "SYSLOG_IDENTIFIER=amavis"
labels:
  type: syslog
```
