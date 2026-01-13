## Synology DSM web authentication parser

A parser for Synology DSM web authentication (failed) logs.
Those logs are usually present in `/var/log/auth.log`.

Example acquisition:

```yaml
filenames:
  - /var/log/auth.log
labels:
  type: syslog
```
