## Asterisk collection

A collection for asterisk :
 - asterisk log parser
 - asterisk user enumeration scenario
 - asterisk bruteforce scenario


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/asterisk/*.log
  type: asterisk
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection

