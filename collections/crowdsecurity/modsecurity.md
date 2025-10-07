## Modsecurity collection

A collection for modsecurity (tested only with Apache):
 - modsecurity parser: `crowdsecurity/modsecurity`
 - modsecurity scenario:
  - `crowdsecurity/modsecurity`
  - `crowdsecurity/modsecurity-blocking-evaluation-response`
  - `crowdsecurity/modsecurity-blocking-evaluation`
  - `crowdsecurity/modsecurity-data-leakages-sql`
  - `crowdsecurity/modsecurity-data-leakages`
  - `crowdsecurity/modsecurity-generic`
  - `crowdsecurity/modsecurity-injection-nodejs`
  - `crowdsecurity/modsecurity-injection-php`
  - `crowdsecurity/modsecurity-java`
  - `crowdsecurity/modsecurity-lfi`
  - `crowdsecurity/modsecurity-multipart-header`
  - `crowdsecurity/modsecurity-nextcloud`
  - `crowdsecurity/modsecurity-protocol-enforcement`
  - `crowdsecurity/modsecurity-rce`
  - `crowdsecurity/modsecurity-reputation-scanner`
  - `crowdsecurity/modsecurity-rfi`
  - `crowdsecurity/modsecurity-session-fixation`
  - `crowdsecurity/modsecurity-sqli`
  - `crowdsecurity/modsecurity-ssrf`
  - `crowdsecurity/modsecurity-web-shells`
  - `crowdsecurity/modsecurity-wordpress`
  - `crowdsecurity/modsecurity-xss`

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/apache2/*.log
  - /var/log/nginx/*.log
labels:
  type: modsecurity
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
