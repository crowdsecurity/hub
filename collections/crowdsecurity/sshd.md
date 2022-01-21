## SSHD collection

A collection to defend sshd against common attacks :
 - ssh parser
 - ssh bruteforce & enumeration detection
 - ssh 'slow' bruteforce & enumeration detection

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/auth.log
labels:
  type: syslog
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection

