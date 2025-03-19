Parser for Opensearch Dashboard.

Typically you may find other software using this such as Wazuh.

Example acquistion:

```yaml
filenames:
 - /path/to/log.txt
labels:
  type: opensearch-dashboard
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
 - "_SYSTEMD_UNIT=opensearch-dashboard.service"
labels:
  type: syslog
```

