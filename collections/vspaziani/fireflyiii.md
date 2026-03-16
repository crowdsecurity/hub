A collection to defend [Fireflyiii](https://www.firefly-iii.org) instance against common attacks :
 - Fireflyiii parser
 - Fireflyiii bruteforce detection
 - Fireflyiii MFA detection

## Acquisition template

Example acquisition for this collection :

For Docker directly
```yaml
---
source: docker
container_name:
 - fireflyiii
#container_id:
# - 843ee92d231b
labels:
  type: fireflyiii
```
