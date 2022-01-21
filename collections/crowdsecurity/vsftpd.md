## VsFTPD collection

A collection to defend VSFTPD against common attacks :
- VSFTPD parser: `crowdsecurity/vsftpd-logs`
- bruteforce scenario : `crowdsecurity/vsftpd-bf`

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
