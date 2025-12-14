# Supavisor Logs Parser

Parses [Supavisor](https://github.com/supabase/supavisor) connection pooler logs to detect authentication failures.

## Overview

Supavisor is Supabase's cloud-native, multi-tenant PostgreSQL connection pooler written in Elixir. It replaced PgBouncer in the Supabase stack and is now the default connection pooler.

**Important**: In modern Supabase deployments using Supavisor, the PostgreSQL container only sees connections from Supavisor's internal IP - not the real client IPs. This makes monitoring at the Supavisor level essential for detecting and blocking attacks.

## Supported Log Formats

### Authentication Failures (with peer_ip - can be blocked)

```
18:38:17.778 project=dev_tenant user=postgres region=local mode=transaction type=single app_name=psql peer_ip=123.123.123.123 [error] ClientHandler: Exchange error: "Wrong password" when method :auth_query
```

### SSL Required Errors (with peer_ip)

```
05:44:32.395 project=dev_tenant user=postgres region=local mode=transaction type=single app_name=psql peer_ip=123.123.123.123 [error] ClientHandler: Tenant is not allowed to connect without SSL, user postgres
```

### Bad Startup Payload (NO peer_ip - monitoring only)

```
08:31:53.782 region=local [error] ClientHandler: Client startup message error: :bad_startup_payload
```

### User Not Found (NO peer_ip - monitoring only)

```
06:06:31.740 region=local [error] ClientHandler: User not found: "Either external_id or sni_hostname must be provided" {:single, "postgres", nil}
```

## Limitation

Some Supavisor error types do NOT include `peer_ip`, making blocking impossible:

| Log Type | Has peer_ip | Can Block |
|----------|-------------|-----------|
| Wrong password | ✅ Yes | ✅ Yes |
| SSL required | ✅ Yes | ✅ Yes |
| Bad startup payload | ❌ No | ❌ No |
| User not found | ❌ No | ❌ No |

## Parsed Fields

| Field | Description |
|-------|-------------|
| `source_ip` | Client IP address (when `peer_ip` present) |
| `project` | Supavisor tenant/project identifier |
| `db_user` | Database user attempting connection |
| `pool_mode` | Connection pool mode (transaction/session) |
| `pool_type` | Pool type (single/pooled) |
| `app_name` | Client application name |
| `log_type` | Event classification |

## Acquisition

This parser requires Docker socket acquisition:

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
  - ".*supavisor.*"
labels:
  type: supavisor
```

## Related

- Scenario: `crowdsecurity/supavisor-bf`
- Collection: `crowdsecurity/supabase-supavisor`
