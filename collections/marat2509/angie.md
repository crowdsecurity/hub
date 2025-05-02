## Angie collection

A collection to defend angie against common attacks :
 - angie parser
 - base http scenarios (crawl, 404 scan, bf)

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/angie/*.log
labels:
  type: angie
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
