## Supabase Docker Compose collection

A collection for [self hosted Supabase via docker compose](https://github.com/supabase/supabase/blob/master/docker/docker-compose.yml)
 * Parser for Kong and postgresql
 * base http scenarios (crawl, 404 scan, bf)
 * bruteforce scenarios for postgresql

## Acquisition template

Example acquisition for this collection :

```yaml
source: docker
container_name:
 - supabase-db
labels:
  type: postgres
---
source: docker
container_name:
 - supabase-kong
labels:
  type: nginx
```
