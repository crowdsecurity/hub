A collection to defend Baserow docker instance against common attacks :
 - Baserow parser
 - Baserow bruteforce detection

## Acquisition template

Example acquisition for this collection :

If using baserow docker instance:
```yaml
---
source: docker
container_name:
 - baserow
labels:
  type: baserow
```
