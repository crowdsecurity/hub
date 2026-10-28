# Syslog parser

This is a generic linux syslog parser with time-support.
It also supports BusyBox syslogd's `facility.severity` field after the hostname,
as used by Alpine Linux. Use a file acquisition with the `type: syslog` label
(e.g. `/var/log/messages`) for these logs.

Add `datasource_type` and `datasource_path` source and datasource type in the `Meta` object.
