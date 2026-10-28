# PostgreSQL and PgBouncer Logs Parser

PostgreSQL and PgBouncer failed authentication parser.

Supports PostgreSQL (v12+, AWS Aurora) as well as PgBouncer authentication failure formats (IPv4 and IPv6).

**Warning**: By default (at least on Debian with PostgreSQL 12), PostgreSQL logs do not contain the source IP, and `log_line_prefix` needs to be edited to contain `%h` (the remote host). This parser assumes the `log_line_prefix` is `%m [%p] %h%q %u@%d ` (instead of the default `%m [%p] %q%u@%d `).

Please note that the parser ignores the timezone written by postgres.

## Acquisition Configuration

### PostgreSQL

Example configuration for PostgreSQL log file in `/etc/crowdsec/acquis.yaml`:

```yaml
filenames:
  - /var/log/postgresql/postgresql-*.log
labels:
  type: postgres
```

### PgBouncer

Example configuration for PgBouncer log file in `/etc/crowdsec/acquis.yaml`:

```yaml
filenames:
  - /var/log/postgresql/pgbouncer.log
labels:
  type: pgbouncer
```

If PgBouncer logs to systemd journal or syslog:

```yaml
journalctl_filter:
  - _SYSTEMD_UNIT=pgbouncer.service
labels:
  type: syslog
```

*Note: Both `type: pgbouncer` and `type: postgres` are supported by this parser.*

## Parsed Fields

| Field | Description |
|-------|-------------|
| `source_ip` | Remote client IP address (IPv4 or IPv6) |
| `user` | Database user being authenticated |
| `db` | Target database name |
| `auth_method` | Authentication method used |
| `log_type` | Set to `pgsql_failed_auth` |
