A collection to defend a [Baikal](https://github.com/sabre-io/Baikal) CalDAV/CardDAV instance against common attacks:

-   Baikal parser
-   Baikal bruteforce & enumeration detection

## Acquisition template

Example acquisition for this collection:

```yaml
---
filenames:
    - /var/log/httpd/error.log
labels:
    type: Baikal
```
