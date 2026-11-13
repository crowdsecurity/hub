Detect failed [Bifrost](https://github.com/maximhq/bifrost) authentication attempts:

- leakspeed of 20s, capacity of 5 per unique IP address

Only 401 responses that Bifrost returns within 10ms count, which excludes 401s
passed through from an upstream provider. The parser documentation explains how
the source IP is chosen when a reverse proxy sits in front of Bifrost.
