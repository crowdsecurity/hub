## Cpanel collection

A collection for cpanel. Contains:
 * cpanel log parser
 * cpanel scenario to detect bruteforce

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /home/<username>/logs/cpanel/login_log
labels:
  type: cpanel
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
