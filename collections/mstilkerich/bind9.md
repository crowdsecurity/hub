## Bind9 collection

A collection for bind9
 * Log parser for supporting both logs in syslog and separate bind9 logfile
 * Scenario that detects bind9 security policy violations

This collection should address the same events as the fail2ban named-refused
jail.


## Acquisition template

Acquisition configuration depends on whether bind9 is configured to log to
syslog, separate log files, or both.

For a separate log file, set the log type to `named`:

```yaml
filenames:
  - /var/log/named/security.log
labels:
  type: named
```

If you are using syslog, set type to `syslog` instead.
