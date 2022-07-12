## ApisCP collection

A collection for ApisCP :
 - Apache log parser for apisCP and httpd access_log
 - Scenario to detect bruteforce on ApisCP admin page
 - Collections for supported services:
    - crowdsecurity/apache2
    - crowdsecurity/dovecot
    - crowdsecurity/haproxy
    - crowdsecurity/mysql
    - crowdsecurity/postfix
    - crowdsecurity/pgsql
    - crowdsecurity/vsftpd


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /usr/local/apnscp/storage/logs/access_log
  - /usr/local/apnscp/storage/logs/error_log
labels:
  type: apache2
---
filenames:
  - /var/log/pgsql/*.log
labels:
  type: postgres
---
filenames:
  - /var/log/maillog
labels:
  type: syslog
---
filenames:
  - /var/log/mysqld.log
labels:
  type: mysql
---
filenames:
  - /var/log/vsftpd.log
labels:
  type: vsftpd
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection

