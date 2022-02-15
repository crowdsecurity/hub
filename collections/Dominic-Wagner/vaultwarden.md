A collection to defend [Vaultwarden](https://github.com/dani-garcia/vaultwarden) instance against common attacks :
 - Vaultwarden parser
 - Vaultwarden bruteforce & enumeration detection

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /var/log/vaultwarden.log
labels:
  type: Vaultwarden
```
If running via systemd:
```yaml
---
source: journalctl
journalctl_filter:
  - "SYSLOG_IDENTIFER=Vaultwarden"
labels:
  type: Vaultwarden
```
