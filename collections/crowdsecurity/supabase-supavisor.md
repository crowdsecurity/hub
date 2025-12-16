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

## What Gets Detected

### ✅ Detectable (has peer_ip)
| Attack Type | Log Pattern | Action |
|-------------|-------------|--------|
| Wrong password | `Exchange error: "Wrong password"` | Block after 5 attempts |
| SSL required bypass | `Tenant is not allowed to connect without SSL` | Block after 5 attempts |

### ❌ Not Detectable (no peer_ip in logs)

| Log Type | Reason |
|----------|--------|
| Bad startup payload | Supavisor doesn't log client IP |
| User not found | Supavisor doesn't log client IP |

This is a Supavisor logging limitation, not a CrowdSec limitation.

## Included Components

| Type | Name | Description |
|------|------|-------------|
| Parser | `crowdsecurity/supavisor-logs` | Parses Supavisor logs |
| Scenario | `crowdsecurity/supavisor-bf` | Brute force detection |

## Related

- [Supabase Self-Hosting Guide](https://supabase.com/docs/guides/self-hosting/docker)
- [Supavisor Repository](https://github.com/supabase/supavisor)
- [CrowdSec Documentation](https://docs.crowdsec.net/)
