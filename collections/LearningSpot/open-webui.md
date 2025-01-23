A collection to defend Open WebUI docker instance against common attacks :
 - Open WebUI parser
 - Open WebUI bruteforce detection

## Acquisition template

Example acquisition for this collection :

If using open-webui docker instance:
```yaml
---
source: docker
container_name:
 - open-webui
labels:
  type: open-webui
```
