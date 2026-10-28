## Mailcow netfilter-mailcow ban-line parser

Parses ban lines emitted by Mailcow's internal `netfilter-mailcow` component
(Mailcow's own F2B-equivalent that lives inside the Mailcow Docker network).

Two log patterns are recognized:

| Source | Sample line | Trigger |
|---|---|---|
| Auto-ban from F2B regex | `CRIT: Banning 198.51.100.42/32 for 60 minutes` | regex match against Mailcow internal failure counters |
| Manual perm-ban from `F2B_BLACKLIST` | `CRIT: Added host/network 198.51.100.42 to denylist` | static blacklist via Mailcow admin UI |

Extracted fields:

- `source_ip` -- the banned IP
- `ban_duration_min` -- duration in minutes (only set on auto-bans)
- `log_type` -- set to `mailcow_f2b_ban` for the downstream scenario
- `service` -- set to `mailcow-f2b`

### Acquisition example

The `netfilter-mailcow` container logs to stdout in a plain-text format
(no syslog, no JSON), so the docker acquisition tags it via `labels.type`:

```yaml
source: docker
container_name:
  - mailcowdockerized-netfilter-mailcow-1
labels:
  type: mailcow-f2b
```

The parser filter then keys off `evt.Parsed.program == 'mailcow-f2b'`,
which `crowdsecurity/non-syslog` populates automatically from the
acquisition `labels.type`.

### Companion scenario

This parser is meant to be paired with `Guezli/mailcow-f2b-feed`, which
turns each parsed ban event into a Crowdsec LAPI decision so the
host-side nftables-bouncer can act on Mailcow-internal bans.
