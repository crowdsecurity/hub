A collection to defend [RomM](https://github.com/rommapp/romm) instance against common attacks :
 - RomM parser
 - RomM bruteforce detection

## Acquisition template

Example acquisition for this collection :

For Docker directly:
```yaml
---
source: docker
container_name:
 - romm
labels:
  type: romm
```

If using file-based acquisition:
```yaml
---
filenames:
 - /path/to/romm.log
labels:
  type: romm
```

**Note:** If you are using file based acquisition, you will need to add the following to your RomM `docker-compose.yaml` in order to write logs to a file:
```yaml
command: sh -c "/init 2>&1 | tee /path/to/romm.log"
```
