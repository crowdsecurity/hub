A collection to defend Dockge instance against common attacks :
 - Dockge parser
 - Dockge bruteforce & enumeration detection

## Acquisition template

Example acquisition for this collection :

If dockge container name is dockge or change the container name accordingly :
```yaml
---
source: docker
container_name:
 - dockge
labels:
  type: dockge
```
