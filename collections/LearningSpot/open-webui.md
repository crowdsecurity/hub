A collection to defend Open WebUI Docker instance against common attacks :
 - Open WebUI parser
 - Open WebUI bruteforce detection

## Acquisition template

Example acquisition for this collection :

If Open WebUI container name is open-webui or change the container name accordingly :
```yaml
---
source: docker
container_name:
 - open-webui
labels:
  type: open-webui
```