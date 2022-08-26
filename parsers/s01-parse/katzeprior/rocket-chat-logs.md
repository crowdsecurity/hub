Parser for [Rocket.Chat](https://www.rocket.chat/) Logs.

Example acquisition for Journalctl:
```yaml
---
journalctl_filter:
 - SYSLOG_IDENTIFER=rocketchat
labels:
  type: rocketchat
```