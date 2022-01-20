## Caddy collection

A collection to defend caddy against common http attacks :
 - caddy parser
 - base-http-scenarios collection to detect http bad behaviors

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/caddy/*.log
  type: caddy
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
