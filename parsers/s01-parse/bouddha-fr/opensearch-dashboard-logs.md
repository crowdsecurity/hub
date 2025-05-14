Parser for Opensearch Dashboard.

Typically you may find other software using this such as Wazuh.

Example acquistion:

```yaml
filenames:
 - /path/to/log.txt
labels:
  type: opensearch-dashboards
```

```yaml
filenames:
 - /var/log/syslog
labels:
  type: syslog
```

```yaml
source: journalctl
journalctl_filter:
 - "_SYSTEMD_UNIT=opensearch-dashboards.service"
labels:
  type: syslog
```

