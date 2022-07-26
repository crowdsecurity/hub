## Nginx Mail collection

A collection for Nginx mail proxy
 * Nginx Mail core module log parsers
 * Nginx Mail auth module scenario bruteforce spam attempt

It is recommended having the `crowdsecurity/nginx` collection installed!

> Contribution by https://github.com/hitech95

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/nginx/*.log
  - ./tests/nginx/nginx.log
#this is not a syslog log, indicate which kind of logs it is
labels:
  type: nginx
```

If you are running Nginx inside docker, like [mailu](https://mailu.io/):

```yaml
---
source: docker
container_name: 
 -  mailu-front
labels:
  type: nginx
```

notes :
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
