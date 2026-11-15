A parser for [NPMpro](https://github.com/TheBlackBush/NPMpro), supports the access log, the stream log and the `limit_req` lines of the error log.

It reads:
 - the NPMpro access log in the classic format (`alog` in [nginx.conf](https://github.com/TheBlackBush/NPMpro/blob/develop/rootfs/usr/local/nginx/conf/nginx.conf)), including lines written before the receiving port (`$server_port`) and the fields after it were added
 - the access log in the JSON format (Log format setting of NPMpro, one object per line). It gives the same `evt.Meta` as the classic line of the same request. A request line that does not parse (for example `GARBAGE`) is kept whole in `http_path`, in both formats
 - the stream log, in the classic and the JSON format (`log_type` `npmpro_stream-log`, `service` `tcp`, `target_port` and `stream_id`). Lines from before the stream id was added still parse
 - the `limiting requests, excess` lines of the nginx error log (`sub_type` `req_limit_exceeded`)

A file may hold classic and JSON lines one after the other (after a change of the Log format setting): each line is read by its own format.

Failed basic auth is read from the access log only: a `401` line with a user name gives `sub_type` `auth_fail` and `evt.Meta.username`. The error log lines `user "x": password mismatch` and `user "x" was not found in ...` of the same request are not parsed on purpose. They give no event: the access log has the 401 line of the same request, and parsing both would count every failed login twice in `crowdsecurity/http-generic-bf`. The other error log lines (upstream errors, warnings) give no event either.

A line from a unix socket client (`remote_addr` `unix:`) has no client address and gives no event.

The receiving port is available as `evt.Parsed.server_port` and `evt.Meta.target_port`. It is set by nginx (the port of the listening socket inside the container), not by the client.

Use `type: npmpro` in the acquisition, see the `TheBlackBush/npmpro` collection.

The server name (`$server_name`), the host id (`$npmpro_host_id`: `proxy-<id>`, `redirection-<id>`, `dead-<id>`, `default` or `npmpro`), the request id (`$request_id`) and the connection number are available as `evt.Parsed.server_name`, `host_id`, `request_id` and `connection`, and `evt.Meta.host_id`, `request_id` and `connection`. The request id is also the id of the AppSec request of the same request in the NPMpro bouncer.

`evt.Parsed.target_fqdn` (and so `evt.Meta.target_fqdn`) is the first configured server name of the host (`$server_name`, the first domain name of the host) when the line has one, otherwise the `Host` of the request, so scenarios that group by it (such as `crowdsecurity/http-probing`) do not depend on the name a client sends. It is not the requested name: for a host with several domain names every request reports the first one, and a wildcard or regular expression name is reported as written (`*.example.com`, `~^...`). For the default server it is `_`. The host the client requested stays in `evt.Parsed.host`.
