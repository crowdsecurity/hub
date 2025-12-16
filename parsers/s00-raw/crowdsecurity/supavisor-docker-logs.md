# Supavisor Docker Logs Parser

Prepares Supavisor logs for parsing by setting the program and message fields.

## Acquisition

```yaml
source: docker
container_name:
  - supabase-supavisor
labels:
  type: supavisor
```
