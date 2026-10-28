A collection to defend [Litellm](https://github.com/BerriAI/litellm) docker instance against common attacks :
 - Litellm parser
 - Litellm bruteforce detection

## Acquisition template

Example acquisition for this collection :

If using Litellm docker instance:
```yaml
---
source: docker
container_name:
 - litellm_container_name
labels:
  type: litellm
```
