## Modsecurity collection

A collection for modsecurity (tested only with Apache):
 - modsecurity parser: `crowdsecurity/modsecurity`
 - modsecurity scenario: `crowdsecurity/modsecurity


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/apache2/*.log
  - <TBD>
labels:
  type: modsecurity
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
