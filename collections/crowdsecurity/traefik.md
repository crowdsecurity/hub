## Traefik collection

> Co-authored with (https://github.com/gmelodie)

A collection to defend traefik against common attacks:
 - traefik parser (supports CLF and JSON)
 - base http scenarios (crawl, 404 scan, bf)


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/traefik/*.log
labels:
  type: traefik
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
