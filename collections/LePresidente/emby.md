A collection to defend [Emby](https://emby.media) instance against common attacks :
 - Emby parser
 - Emby bruteforce detection

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /var/log/embyserver.txt
labels:
  type: Emby
```