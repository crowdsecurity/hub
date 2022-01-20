## Apache2 collection

A collection for apache2 :
 - apache2 parser
 - base http scenarios for crawl, scan etc.

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/apache2/*.log
  - /var/log/*httpd*.log
  - /var/log/httpd/*log
labels:
  type: apache2
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
