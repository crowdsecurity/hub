## Exim collection

A collection for Exim mail server
 * exim log parser
 * exim scenario for bruteforce and spam attempt


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/exim_mainlog
labels:
  type: exim
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
