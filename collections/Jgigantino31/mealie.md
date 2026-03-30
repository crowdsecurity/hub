A collection to defend [Mealie](https://mealie.io/) instance against common attacks :
 - Mealie parser
 - Mealie bruteforce detection

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /var/log/mealie.log
labels:
  type: mealie
```

For Docker directly
```yaml
---
source: docker
container_name:
 - mealie
#container_id:
# - 843ee92d231b
labels:
  type: mealie
