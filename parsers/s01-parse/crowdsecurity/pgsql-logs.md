PostgreSQL fail authentication parser.


**warning** : By default (at least on debian with pgsql 12), postgreSQL logs do not contain the source IP, and `log_line_prefix` needs to be edited to contain `%h` (the remote host). This parser assumes the `log_line_prefix` is  `%m [%p] %h%q %u@%d ` (instead of the default `%m [%p] %q%u@%d `)

Please note that the parser ignores the timezone written by postgres.

## PgBouncer

PgBouncer authentication failures are also supported. For direct file acquisition, label the source with `type: pgbouncer`. If PgBouncer logs are received through syslog, keep the acquisition type as `syslog`; the syslog parser must preserve `program: pgbouncer` for this parser to select the event.
