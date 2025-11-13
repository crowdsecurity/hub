## VsFTPD collection

A collection to defend VSFTPD against common attacks:
 - vsftpd failed authentication parser
 - vsftpd successful authentication parser
 - detect bruteforce (fast attacks: 5 failures in ~50s)
 - detect slow bruteforce (slower attacks: 10 failures in ~10min)
 - detect time-based bruteforce (time-spaced attacks: 3 failures with >2min median interval, includes false positive reduction)

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/vsftpd/*.log
labels:
  type: vsftpd
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
