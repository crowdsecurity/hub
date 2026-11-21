Detects clients that send many bad requests to [NPMpro](https://github.com/TheBlackBush/NPMpro): scanners, bots that speak the wrong protocol on the HTTP port, and requests for names that no host serves.

It counts two kinds of access log lines, grouped by source IP:
 - answered with 400 by nginx itself: nginx refused a malformed request (bad request line, wrong protocol, invalid header), so the request reached no upstream and the upstream status is empty (`-` in the classic format, `""` in JSON)
 - answered with 444 by the NPMpro default site (`host_id` `default`): the request names a host that NPMpro does not serve, or has no `Host` at all, and the default site closes the connection

A 400 that an upstream answered is not counted: a proxied application may answer 400 to bad form input or a bad API call, and such a client did not send a malformed request. NPMpro lines from before the upstream status was logged have no upstream status, so every 400 in them counts.

A 444 answered by a proxy host is not counted. A proxy host answers 444 to an IP that CrowdSec banned (the NPMpro bouncer), so counting it would make a ban feed its own scenario.

 - leakspeed of 10s, capacity of 10, blackhole of 5m: more than 10 such requests in a short time trigger it, slow or occasional bad requests do not
 - requires the access log parsed by `TheBlackBush/npmpro-logs` from a version of NPMpro that logs the host id (`$npmpro_host_id`)
