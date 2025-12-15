# Supavisor Docker Logs Parser

Extracts Supavisor log messages from Docker JSON log format.

## Log Format

```json
{"log":"18:38:17.778 project=dev_tenant user=postgres ...","stream":"stderr","time":"2024-01-15T18:38:17.778Z"}
```

## Acquisition

```yaml
source: docker
container_name:
  - supabase-supavisor
labels:
  type: supavisor
```
