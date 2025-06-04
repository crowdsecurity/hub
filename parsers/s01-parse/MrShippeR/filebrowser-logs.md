Parser for [FileBrowser vanilla app](https://filebrowser.org/) logs.

```yaml
---
filenames:
  - /home/shipper/docker/filebrowser/config/filebrowser.log 
labels:
  type: filebrowser
```


Parser for [FileBrowser Docker container](https://hub.docker.com/r/filebrowser/filebrowser) logs.
```yaml
---
source: docker
container_name:
 - filebrowser_container_name
labels:
  type: filebrowser
```
