A collection to defend a [Webmin](https://github.com/webmin/webmin) instance against common attacks:

-   Webmin parser
-   Webmin bruteforce & enumeration detection

## Acquisition template

Example acquisition for this collection:

```yaml
---
filenames:
    - /var/webmin/webmin.log
labels:
    type: Webmin
```
