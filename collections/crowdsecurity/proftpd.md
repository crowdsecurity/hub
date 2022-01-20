## ProFTPD collection

A collection to defend proftpd against common attacks:
 - proftpd parser
 - detect bruteforce
 - detect user enumeration


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - <TBD>
labels:
  type: proftpd
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
