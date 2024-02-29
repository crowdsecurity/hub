A collection to defend [Overseerr](https://overseerr.dev) instance against common attacks:
 - Overseerr parser
 - Overseerr bruteforce detection

## Acquisition template

Example acquisition for this collection :

```yaml
---
source: docker
container_name:
 - overseerr
#container_id:
# - 843ee92d231b
labels:
  type: overseerr
```