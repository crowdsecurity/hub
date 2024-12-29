## Synapse Matrix Servers: Known/Server Requests

Prohibit Matrix servers from sending requests to the current server endpoints, even if the server no longer exists (decommissioned) or never existed (inherited/re-registered domain).

More details at

- https://github.com/element-hq/synapse/issues/3765
- https://github.com/element-hq/synapse/issues/5442
- https://github.com/element-hq/synapse/issues/17739

There does not seem to be a viable way to tell matrix network servers to stop sending these queries, hence this scenario to ban IP sources making these endless queries. Depending on the number of channels/servers the old server was connected to, this can be a significant number of requests per day.

There does not seem to be a viable way to tell matrix network servers to stop sending these queries, hence this scenario to ban IP sources making these endless queries.
