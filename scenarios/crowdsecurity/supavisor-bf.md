# Supavisor Brute Force Detection

Detects brute force attacks against PostgreSQL databases through the Supavisor connection pooler.

## Description

This scenario triggers when multiple authentication failures are detected from the same IP address within a short time period. It detects wrong password attempts via Supavisor's `auth_query` authentication method.

## Why Monitor Supavisor Instead of PostgreSQL?

In modern Supabase deployments using Supavisor:

```
Client (attacker) → Supavisor → PostgreSQL
       ↑                              ↑
  Real IP visible              Only sees Supavisor's IP
```

PostgreSQL logs would only show connections from Supavisor's internal container IP, making it impossible to identify and block attackers. Supavisor logs contain the actual client IP (`peer_ip`).

## Real Log Example

```
18:38:17.778 project=dev_tenant user=postgres region=local mode=transaction type=single app_name=psql peer_ip=123.123.123.123 [error] ClientHandler: Exchange error: "Wrong password" when method :auth_query
```

## Behavior

| Parameter | Value | Description |
|-----------|-------|-------------|
| `capacity` | 5 | Failed attempts before triggering |
| `leakspeed` | 30s | Time window for counting |
| `blackhole` | 5m | Cooldown after trigger |

## Labels

| Label | Value | Description |
|-------|-------|-------------|
| `confidence` | 3 | High - very unlikely false positive |
| `spoofable` | 0 | Cannot be spoofed (TCP required) |
| `classification` | attack.T1110 | MITRE ATT&CK: Brute Force |
| `remediation` | true | Triggers blocking action |

## Acquisition

```yaml
source: docker
container_name_regexp:
  - "supabase-supavisor-.*"
  - ".*supavisor.*"
labels:
  type: supavisor
```

## Testing

```bash
# Generate 6+ failed auth attempts
for i in {1..7}; do
  psql 'postgresql://postgres.your_tenant:wrongpassword@your-host:5432/postgres' -c '\q' 2>/dev/null
  sleep 2
done

# Check for alerts
cscli alerts list
cscli decisions list
```

## Related

- Parser: `crowdsecurity/supavisor-logs`
- Collection: `crowdsecurity/supabase-supavisor`
