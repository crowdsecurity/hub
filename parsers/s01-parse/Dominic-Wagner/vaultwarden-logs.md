Parser for [Vaultwarden](https://github.com/dani-garcia/vaultwarden) Logs.

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