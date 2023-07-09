Parser for [Baikal](https://github.com/sabre-io/Baikal) logs. Baikal does not produce dedicated logs but rather sends PHP errors into apache/nginx logs. Currently only apache error logs are supported by this parser.

```yaml
---
filenames:
    - /var/log/httpd/error.log
labels:
    type: Baikal
```
