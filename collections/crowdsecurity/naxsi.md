## Naxsi collection

A collection to detect virtual patch violations :
 - naxsi logs parser
 - vpatch high id (>9999) trigger rule

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
