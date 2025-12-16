# Supavisor Brute Force Detection

Detects brute force attacks against PostgreSQL databases through the Supavisor connection pooler.

## Description

This scenario triggers when multiple authentication failures are detected from the same IP address. It detects wrong password attempts via Supavisor's `auth_query` authentication method.

## Behavior

| Parameter | Value | Description |
|-----------|-------|-------------|
| `capacity` | 5 | Failed attempts before triggering |
| `leakspeed` | 30s | Time window for counting |
| `blackhole` | 5m | Cooldown after trigger |

## Labels

| Label | Value |
|-------|-------|
| `confidence` | 3 |
| `spoofable` | 0 |
| `classification` | attack.T1110 |
| `remediation` | true |

## Acquisition

```yaml
source: docker
container_name_regexp:
  - "supabase-supavisor"
  - "supabase-supavisor-.*"
labels:
  type: supavisor
```
