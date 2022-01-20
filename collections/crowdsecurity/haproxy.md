## Haproxy collection

A collection to defend haproxy http against common attacks :
 - haproxy http parser
 - base http scenarios (crawl, 404 scan, bf etc.)


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/haproxy/*.log
labels:
  type: haproxy
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
