Defend [Radicale](https://radicale.org/) CalDAV/CardDAV instances against brute-force and credential stuffing attacks.

Includes:
- Radicale access log parser
- Brute-force / credential stuffing scenario

## Acquisition template

### File

```yaml
---
source: file
filenames:
  - /var/log/radicale/radicale.log
labels:
  type: radicale
```

### Journald

```yaml
---
source: journalctl
journalctl_filter:
  - "_SYSTEMD_UNIT=radicale.service"
labels:
  type: radicale
```
