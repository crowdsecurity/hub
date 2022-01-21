## Postfix collection

A collection for postfix
 * postfix log parsers
 * postscreen log parser
 * postfix scenario bruteforce spam attempt
 * postscreen rb attempt blacklist

This collection mostly aims at getting a similar spam protection as
the normal fail2ban postfix configuration although postcreen log
management isn't included by default by fail2ban.


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/mail.log
labels:
  type: syslog
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
