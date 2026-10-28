Detect failed Navidrome authentication attempts:

- leakspeed of 20s, capacity of 5 per unique IP address[^1]

[^1]: Note that this matches the default configuration of the
[Navidrome configuration](https://www.navidrome.org/docs/usage/configuration-options/#advanced-configuration)
for `AuthRequestLimit` and `AuthRequestLength`.
