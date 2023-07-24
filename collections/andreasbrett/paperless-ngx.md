A collection to defend a [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) instance against common attacks:

-   Paperless-ngx parser
-   Paperless-ngx bruteforce & enumeration detection

## Acquisition template

Example acquisition for this collection:

```yaml
---
filenames:
    - /var/log/paperless.log
labels:
    type: Paperless-ngx
```
