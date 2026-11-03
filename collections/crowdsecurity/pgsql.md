## PostgreSQL collection

A collection for postgresql services :
 - pgsql logs parser
 - bruteforce detection

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/postgresql/*.log
labels:
  type: postgres
```


For PgBouncer logs read directly from a file, use the same collection with `type: pgbouncer`:

```yaml
filenames:
  - /path/to/pgbouncer.log
labels:
  type: pgbouncer
```

notes :
 -  If PostgreSQL or PgBouncer logs are received through `syslog`, set type to `syslog` instead; the syslog parser must preserve the emitting program name
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
