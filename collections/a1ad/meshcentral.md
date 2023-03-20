
A collection to defend [Meshcentral](https://www.meshcommander.com/meshcentral2) instance against common attacks :
 - Meshcentral parser
 - Meshcentral bruteforce detection

## Acquisition template

Example acquisition for this collection :

You need to add the following in the Meshcentral config file before Meshcentral starts logging:
"authLog": "/opt/meshcentral/meshcentral-data/auth.log"

```yaml
---
filenames:
 - /opt/meshcentral/meshcentral-data/auth.log
labels:
  type: meshcentral
```

For Docker directly
```yaml
---
source: docker
container_name:
 - meshcentral
#container_id:
# - 843ee92d231b
labels:
  type: meshcentral
```
