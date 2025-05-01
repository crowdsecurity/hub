A collection to defend Dockge docker instance against common attacks :
 - Dockge parser
 - Dockge bruteforce detection

## Acquisition template

Example acquisition for this collection :

If using dockge docker instance:
```yaml
---
source: docker
container_name:
 - dockge
labels:
  type: dockge
```
