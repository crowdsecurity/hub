A collection to defend [Calibre-Web](https://github.com/janeczku/calibre-web) instance against common attacks :
 - Calibre-Web parser
 - Calibre-Web bruteforce detection

This collection also works when using the extension of Calibre-Web known as [Calibre-Web-Automated](https://github.com/crocodilestick/Calibre-Web-Automated).

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /var/log/calibre-web/calibre-web.log
labels:
  type: calibre-web
```
