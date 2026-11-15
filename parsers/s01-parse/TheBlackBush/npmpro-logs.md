A parser for [NPMpro](https://github.com/TheBlackBush/NPMpro), supports both access and error logs.

It reads the NPMpro access log format (`alog` in [nginx.conf](https://github.com/TheBlackBush/NPMpro/blob/develop/rootfs/usr/local/nginx/conf/nginx.conf)), including lines written before the receiving port (`$server_port`) and the fields after it were added, and the nginx error log (basic auth failures and `limit_req` lines).

The receiving port is available as `evt.Parsed.server_port` and `evt.Meta.target_port`. It is set by nginx (the port of the listening socket inside the container), not by the client, and is empty for requests received over a unix socket.

Use `type: npmpro` in the acquisition, see the `TheBlackBush/npmpro` collection.

The server name (`$server_name`), the host id (`$npmpro_host_id`: `proxy-<id>`, `redirection-<id>`, `dead-<id>`, `default` or `npmpro`), the request id (`$request_id`) and the connection number are available as `evt.Parsed.server_name`, `host_id`, `request_id` and `connection`, and `evt.Meta.host_id`, `request_id` and `connection`. The request id is also the id of the AppSec request of the same request in the NPMpro bouncer.

`evt.Parsed.target_fqdn` (and so `evt.Meta.target_fqdn`) is the first configured server name of the host (`$server_name`, the first domain name of the host) when the line has one, otherwise the `Host` of the request, so scenarios that group by it (such as `crowdsecurity/http-probing`) do not depend on the name a client sends. It is not the requested name: for a host with several domain names every request reports the first one, and a wildcard or regular expression name is reported as written (`*.example.com`, `~^...`). For the default server it is `_`. The host the client requested stays in `evt.Parsed.host`.
