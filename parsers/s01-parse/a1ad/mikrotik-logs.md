Parser for [Mikrotik](https://mikrotik.com/) Logs.

You need to set up a remote syslog server. There is no crowdsec client on the Mikrotik, so log parsing needs to be done on the rsyslog server.
Do not forget to set "Firewall" flag in the remote log settings and create a drop rule with logging active.
For user authentication you need to set the "error" flag.

```yaml
---
filenames:
 - /var/log/rsyslog/10.10.10.1/syslog.log
labels:
  type: mikrotik
```
