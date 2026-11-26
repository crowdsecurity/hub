Parser for [Owncloud](https://owncloud.com/) logs

If you have the default settings of logging to file, you need to add in acquisition (change filename to your log file location):

```yaml
---
filenames:
 - /var/www/owncloud/data/owncloud.log
labels:
  type: Owncloud
```

This parser requires ownCloud's default file logging (`log_type` set to `owncloud`), which writes JSON lines.
ownCloud's syslog output (`log_type` set to `syslog`) uses a different, non-JSON format and is not supported.

## Official Docker image: restrict X-Forwarded-For to your reverse proxy

The official `owncloud/server` Docker image enables Apache's `mod_remoteip` with
`RemoteIPHeader X-Forwarded-For` and no trusted proxy. Any client can then pick the IP
that ownCloud logs (and that CrowdSec bans) by sending an `X-Forwarded-For` header,
even through a reverse proxy that appends to that header.

Only trust the header from your reverse proxy, by replacing
`/etc/apache2/conf-enabled/remoteip.conf` in the container (for instance with a volume)
with:

```
RemoteIPHeader X-Forwarded-For
RemoteIPInternalProxy 172.18.0.2
```

where `172.18.0.2` is the address (or subnet) of your reverse proxy.
