## Pterodactyl collection

A collection to defend pterodactyl against common attacks:
 - Bruteforce against sftp

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /var/log/pterodactyl/wings.log
labels:
  type: pterodactyl
```

You can also use journalctl:
```yaml
source: journalctl
journalctl_filter:
 - "_SYSTEMD_UNIT=wings.service"
labels:
  type: "pterodactyl"
```