## Litespeed collection

A collection to defend litespeed against common attacks :
 - litespeed parser
 - base http scenarios (crawl, 404 scan, bf)
 - Bruteforce against litespeed admin UI

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /usr/local/lsws/YOURVHOST/logs/*.log
  - /usr/local/lsws/admin/logs/*.log
  - /usr/local/lsws/logs/*.log
labels:
  type: litespeed
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
