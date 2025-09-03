Parser for [Postal](https://github.com/postalserver) logs.

This parser detects authentication errors on the SMTP server. 

If you are using the docker-compose deployment of [Postal](https://docs.postalserver.io/)

```yaml
---
source: docker
container_name:
  - postal-smtp-1
labels:
  type: postal
  program: postal
```