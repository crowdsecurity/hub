Parser for parsing coraza logs from Caddy [coraza-caddy](https://github.com/corazawaf/coraza-caddy) runtime error logs.

You need to specify caddy config to enable logging in a file and configure the coraza module:
```bash
{
	# coraza_waf first must be always included in your Caddyfile for Coraza module to work.
	order coraza_waf first

	# The log global option is for Caddy’s runtime logs, i.e. all the logs, and not only "access.log".
	log {
		level INFO
		output file /var/log/caddy/caddy-runtime.log
	}
}

:80 {
	log

	# Defining the directives for coraza.
	coraza_waf {
		directives `
		Include /ruleset/coraza.conf
		Include /ruleset/theappyouwanttoprotect/crs-setup.conf
		Include /ruleset/coreruleset/rules/*.conf
		`
	}

        # Set this path to your site's directory.
        root * /usr/share/caddy

        # Enable the static file server.
        file_server

        # Another common task is to set up a reverse proxy:
        # reverse_proxy localhost:8080

        # Or serve a PHP site through php-fpm:
        # php_fastcgi localhost:9000
}
```

be carefull to check the acquisition file of caddy to match with the output file defined in the Caddyfile like :

```yaml
---
filenames:
 - /var/log/caddy/caddy-runtime.log
labels:
  type: caddy
