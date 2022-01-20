## Dovecot collection

A collection for dovecot
 * dovecot log parsers
 * dovecot scenario bruteforce spam attempt

This collection mostly aims at getting similar spam protection as
the normal fail2ban dovecot configuration.

> Contribution by https://github.com/LtSich

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/mail.log
labels:
  type: syslog
```


notes :
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
