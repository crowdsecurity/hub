## Matrix/Synapse whitelist

### Federation and Client-Server API
Matrix homeservers constantly communicate with each other via the `/_matrix/` endpoint for federation (server-to-server) and client-to-server traffic. These requests can produce a high volume of 4xx responses during normal operation — for example when querying unknown rooms, resolving user profiles across federated servers, or during key exchange. Without this whitelist, scenarios such as `http-probing` or `http-crawl-non_statics` can be triggered, potentially causing legitimate Matrix federation partners or your own clients to get banned.

### Synapse Admin and internal endpoints
The `/_synapse/` path is used by Synapse-specific administration and internal endpoints (e.g. the admin API or media worker communication). Automated health checks, admin dashboards, and internal service calls to these endpoints may generate responses that look suspicious to CrowdSec. This whitelist prevents those requests from being counted toward attack scenarios.

### Server Discovery (`.well-known`)
Matrix relies on `/.well-known/matrix/` for server discovery, where clients and remote servers look up the homeserver and identity server configuration. These lightweight requests are a fundamental part of the Matrix protocol and should never be treated as malicious. Without whitelisting, repeated discovery lookups — especially from multiple federated servers — could falsely trigger rate-based or probing-based scenarios.
