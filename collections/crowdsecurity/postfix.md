A collection for postfix
 * postfix log parsers
 * postscreen log parser
 * postfix scenario bruteforce spam attempt
 * postscreen rb attempt blacklist

This collection mostly aims at getting a similar spam protection than
the normal fail2ban postfix configuration although postcreen log
management isn't included by default by fail2ban.

The relevant `acquis.yaml` should be:
```
filenames:
  - /var/log/mail.log
labels:
  type: syslog
```
