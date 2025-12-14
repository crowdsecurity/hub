# Supabase Supavisor Collection

Detect and block attacks against self-hosted [Supabase](https://supabase.com/) deployments using the [Supavisor](https://github.com/supabase/supavisor) connection pooler.

## Why This Collection?

Modern Supabase deployments use Supavisor (an Elixir-based connection pooler) instead of PgBouncer. This changes where you need to monitor for attacks:

```
┌─────────────────────────────────────────────────────────────┐
│                    Attack Flow                               │
├─────────────────────────────────────────────────────────────┤
│  Attacker ──→ Supavisor ──→ PostgreSQL                      │
│     │            │               │                          │
│  Real IP     Sees real IP    Only sees Supavisor's IP       │
│              ✅ Monitor here  ❌ Useless for blocking        │
└─────────────────────────────────────────────────────────────┘
```

**PostgreSQL logs are useless** in this architecture - they only show Supavisor's internal container IP, not the attacker's IP. This collection monitors Supavisor directly where the real client IPs are visible.

## Installation

```bash
cscli collections install crowdsecurity/supabase-supavisor
```

## Acquisition Configuration

Create `/etc/crowdsec/acquis.d/supavisor.yaml`:

### Standard Supabase docker-compose

```yaml
source: docker
container_name:
  - supabase-supavisor
labels:
  type: supavisor
```

### Coolify / Dynamic Container Names

Coolify and similar platforms add random suffixes to container names. Use regex matching:

```yaml
source: docker
container_name_regexp:
  - "supabase-supavisor-.*"
labels:
  type: supavisor
```

### Multiple Patterns (Recommended)

For maximum compatibility:

```yaml
source: docker
container_name_regexp:
  - "supabase-supavisor-.*"
  - ".*supavisor.*"
labels:
  type: supavisor
```

## Requirements

### Docker Socket Access

CrowdSec needs access to the Docker socket to read container logs:

```yaml
# In your CrowdSec docker-compose.yml
volumes:
  - /var/run/docker.sock:/var/run/docker.sock:ro
```

### Network Access

CrowdSec must be able to reach the Supavisor container. If using Docker networks:

```yaml
networks:
  - your-supabase-network
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
| Parser | `crowdsecurity/supavisor-logs` | Extracts fields from Supavisor logs |
| Scenario | `crowdsecurity/supavisor-bf` | Brute force detection (5 failures/30s) |

## Testing

### Generate Test Alerts

```bash
# Run 6+ failed login attempts (exceeds threshold of 5)
for i in {1..7}; do
  psql 'postgresql://postgres.your_tenant:wrongpassword@your-host:5432/postgres' -c '\q' 2>/dev/null
  echo "Attempt $i"
  sleep 2
done
```

### Verify Detection

```bash
# Check alerts
cscli alerts list

# Check decisions (bans)
cscli decisions list

# View metrics
cscli metrics
```

### Unban Yourself (or add your IP to the whitelist)

If you accidentally ban your own IP during testing:

```bash
cscli decisions delete --ip YOUR_IP
```

whitelist config for your IP:

```yaml
# /opt/crowdsec/config/parsers/s02-enrich/my-whitelist.yaml
name: custom/my-whitelist
description: "Whitelist my IPs"
whitelist:
  reason: "My personal/office IPs"
  ip:
    - "123.123.123.123"
```

## Remediation

After detection, you need a bouncer to actually block the IPs:

### Firewall Bouncer (iptables/nftables)

```bash
apt install crowdsec-firewall-bouncer-iptables
# or
apt install crowdsec-firewall-bouncer-nftables
```

### Traefik Bouncer

If using Traefik as reverse proxy:

```bash
# See: https://github.com/fbonalair/traefik-crowdsec-bouncer
```

## Troubleshooting

### No Logs Being Read

```bash
# Check if CrowdSec sees the container
docker exec crowdsec cscli metrics | grep docker

# Check acquisition config
docker exec crowdsec cat /etc/crowdsec/acquis.yaml

# Verify container name matches regex
docker ps --format '{{.Names}}' | grep -i supavisor
```

### Parser Not Matching

```bash
# Enable debug mode in parser
# Edit: /etc/crowdsec/parsers/s01-parse/crowdsecurity/supavisor-logs.yaml
# Set: debug: true

# Restart and check logs
docker restart crowdsec
docker logs crowdsec 2>&1 | grep -i supavisor
```

### Scenario Not Triggering

```bash
# Check if parser is setting log_type
docker logs crowdsec 2>&1 | grep "log_type"

# Check scenario is loaded
cscli scenarios list | grep supavisor
```

## Related

- [Supabase Self-Hosting Guide](https://supabase.com/docs/guides/self-hosting/docker)
- [Supavisor Repository](https://github.com/supabase/supavisor)
- [CrowdSec Documentation](https://docs.crowdsec.net/)
