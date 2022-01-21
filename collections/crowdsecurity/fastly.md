## Fastly collection

A collection to defend fastly against common http attacks :
 - fastly default log format parser
 - base http scenarios (crawl, 404 scan, bf etc.)

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/fastly/*.log
labels:
  type: syslog
  external_format: fastly
```

notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
