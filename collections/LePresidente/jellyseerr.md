A collection to defend [JellySeerr](https://github.com/Fallenbagel/jellyseerr) instance against common attacks:
 - JellySeerr parser
 - JellySeerr bruteforce detection

## Acquisition template

Example acquisition for this collection :

```yaml
---
source: docker
container_name:
 - jellyseerr
#container_id:
# - 843ee92d231b
labels:
  type: docker
  program: jellyseerr
```