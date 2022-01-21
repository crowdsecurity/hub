## MySQL Collection

A collection for mysql services :
 - mysql logs parser
 - bruteforce detection
 
 ## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/mysql/error.log
labels:
  type: mysql
```

notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
