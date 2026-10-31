A parser for [NPMpro](https://github.com/TheBlackBush/NPMpro), supports both access and error logs.

It reads the NPMpro access log format (`alog` in [nginx.conf](https://github.com/TheBlackBush/NPMpro/blob/develop/rootfs/usr/local/nginx/conf/nginx.conf)), including lines written before the receiving port (`$server_port`) was added as the last field, and the nginx error log (basic auth failures and `limit_req` lines).

The receiving port is available as `evt.Parsed.server_port` and `evt.Meta.target_port`. It is set by nginx (the port of the listening socket inside the container), not by the client, and is empty for requests received over a unix socket.

Use `type: npmpro` in the acquisition, see the `TheBlackBush/npmpro` collection.
