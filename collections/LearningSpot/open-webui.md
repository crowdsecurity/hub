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

## Reverse proxy

If Open WebUI sits behind a reverse proxy, make sure the real client IP is forwarded (`X-Forwarded-For`), otherwise the proxy's IP gets banned. Also set `FORWARDED_ALLOW_IPS` to your proxy's address: by default Open WebUI trusts this header from anyone. See the `LearningSpot/open-webui-logs` parser documentation for details.
