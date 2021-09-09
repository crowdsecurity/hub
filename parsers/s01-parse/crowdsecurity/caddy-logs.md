Parser for caddy logs.
It expects the default key values for caddy logs.

You need to specify caddy config to enable logging in a file:

```bash
:80 {
        # Set this path to your site's directory.
        root * /usr/share/caddy

        # Enable the static file server.
        file_server

        # Another common task is to set up a reverse proxy:
        # reverse_proxy localhost:8080

        # Or serve a PHP site through php-fpm:
        # php_fastcgi localhost:9000
        log {
                output file /var/log/caddy/access.log
        }
}

```

And then add in acquisition this :

```yaml
---
filenames:
 - /var/log/caddy/access.log
labels:
  type: caddy
```