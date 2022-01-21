## Nginx collection

A collection to defend nginx against common attacks :
 - nginx parser (support also ingress nginx controller default [log_format](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/log-format/))
 - base http scenarios (crawl, 404 scan, bf)

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/nginx/*.log
labels:
  type: nginx
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
