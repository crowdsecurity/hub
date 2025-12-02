A collection to defend [Sympa - Mailing List Management Software](https://www.sympa.community/) instance against common attacks:
 - Sympa web service (wwsympa) parser
 - Sympa http scan detection

This collection protects against HTTP scanning attempts that try to discover non-existing actions or lists. Since Sympa returns HTTP 200 responses even for non-existent resources with user-facing error messages, standard web server log analysis cannot detect these scans. This collection uses Sympa's own logs to detect and block such attempts.

## Acquisition template

Example acquisition for this collection :

```yaml
---
filenames:
 - /var/log/sympa.log
labels:
  type: syslog
```

Or using journalctl:

```yaml
---
source: journalctl
journalctl_filter:
  - "_SYSTEMD_UNIT=wwsympa.service"
labels:
  type: syslog
```

