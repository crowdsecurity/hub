## Odoo collection

A collection to defend Odoo against common attacks:
 - Odoo authentication failures parser
 - detect bruteforce
 - detect user enumeration


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/odoo/*.log
labels:
  type: odoo
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
