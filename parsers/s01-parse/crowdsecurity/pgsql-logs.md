PostgreSQL and PgBouncer failed authentication parser.

Supports PostgreSQL (v12+, AWS Aurora) as well as PgBouncer authentication failure formats (password authentication failed and SASL authentication failed).

**warning** : By default (at least on debian with pgsql 12), postgreSQL logs do not contain the source IP, and `log_line_prefix` needs to be edited to contain `%h` (the remote host). This parser assumes the `log_line_prefix` is  `%m [%p] %h%q %u@%d ` (instead of the default `%m [%p] %q%u@%d `)

Please note that the parser ignores the timezone written by postgres.
