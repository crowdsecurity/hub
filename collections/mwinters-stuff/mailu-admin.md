Collection for the mailu admin container parser and secenario.

Mailu is a simple yet full-featured mail server as a set of Docker images. 

This collection identifies the mailu-admin container logs that show
when login attempts (brute force) are rate limited.
Website: https://mailu.io


```yaml
---
source: docker
container_name:
 - mailu/admin
labels:
  type: mailu-admin
```
