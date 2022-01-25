## Nginx Proxy Manager collection

A collection to defend nginx against common attacks :
 - [Nginx Proxy Manager](https://github.com/NginxProxyManager/nginx-proxy-manager) parser
 - base http scenarios (crawl, 404 scan, bf)

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - ~/data/logs/*.log
labels:
  type: nginx-proxy-manager
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your configuration, paths to log files might change
 -  Only relevant if you are manually installing collection