Detect failed [Bifrost](https://github.com/maximhq/bifrost) authentication attempts:

- leakspeed of 20s, capacity of 5 per unique IP address

Bifrost only logs the client address it sees. Behind a reverse proxy or tunnel
the parser uses the first entry of `X-Forwarded-For`, so the proxy must
overwrite that header with the real client address. Otherwise every event carries
the proxy address, or whatever address the client claims.
