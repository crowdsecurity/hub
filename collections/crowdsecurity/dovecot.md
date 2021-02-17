A collection for dovecot
 * dovecot log parsers
 * dovecot scenario bruteforce spam attempt

This collection mostly aims at getting similar spam protection as
the normal fail2ban dovecot configuration.

The relevant `acquis.yaml` should be:

```yaml
filenames:
  - /var/log/mail.log
labels:
  type: syslog
```


> Contribution by https://github.com/LtSich
