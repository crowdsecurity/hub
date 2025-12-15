# Supabase Supavisor Collection

Detect brute force attacks against self-hosted [Supabase](https://supabase.com/) deployments using the [Supavisor](https://github.com/supabase/supavisor) connection pooler.

## Acquisition

```yaml
source: docker
container_name:
  - supabase-supavisor
labels:
  type: supavisor
```

For dynamic container names (Coolify, etc.):

```yaml
source: docker
container_name_regexp:
  - "supabase-supavisor-.*"
labels:
  type: supavisor
```

## Included Components

| Type | Name | Description |
|------|------|-------------|
| Parser | `crowdsecurity/supavisor-docker-logs` | Parses Supavisor logs from Docker containers |
| Parser | `crowdsecurity/supavisor-logs` | Parses Supavisor logs |
| Scenario | `crowdsecurity/supavisor-bf` | Brute force detection |
