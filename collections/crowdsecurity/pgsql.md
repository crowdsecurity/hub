## PostgreSQL collection

A collection for postgresql services :
 - pgsql logs parser
 - bruteforce detection

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - <TBD>
labels:
  type: postgres
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
