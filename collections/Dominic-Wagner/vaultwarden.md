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

## Timestamp issues

In the default configuration of `vaultwarden` logs, the timestamp uses system local time. This means that detection may not work as expected as CrowdSec uses UTC time. To fix this, you can configure `vaultwarden` to log the offset from UTC time. To do this, head over to `Vaultwarden Admin Panel -> Advanced Settings -> Log timestamp format` and change format to `%Y-%m-%d %H:%M:%S.%3f%z`.
