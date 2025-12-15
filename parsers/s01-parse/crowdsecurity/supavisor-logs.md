# Supavisor Logs Parser

Parses [Supavisor](https://github.com/supabase/supavisor) connection pooler logs to detect authentication failures.

## Log Format

```
18:38:17.778 project=dev_tenant user=postgres region=local mode=transaction type=single app_name=psql peer_ip=123.123.123.123 [error] ClientHandler: Exchange error: "Wrong password" when method :auth_query
```

## Parsed Fields
    
| Field | Description |
|-------|-------------|
| `source_ip` | Client IP address |
| `project` | Tenant/project identifier |
| `db_user` | Database user |
| `log_type` | Event classification |

## Acquisition

```yaml
source: docker
container_name:
  - supabase-supavisor
labels:
  type: supavisor
```
