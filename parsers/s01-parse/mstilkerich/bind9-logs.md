This bind9 parser supports logs in separate bind9 log files as well as syslog
entries. When logging to separate bind9 log files directly with bind9, the
`print-time` setting should be enabled, otherwise no timestamp will be
available.

This parser currently detects the following security events of bind9:
 - Zone transfer request denied by security policy
 - Queries denied by security policy

To configure data acquisition from a bind9 log file, set the `type` to `named`:
```yaml
---
filenames:
  - /var/log/named/security.log
labels:
  type: named
```

Inspired by fail2ban named-refused.
