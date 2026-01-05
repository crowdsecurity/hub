Generic implementation of impossible travel to detect users logging in from two different locations in a short period of time. If you wish to write a parser to fall into this generic bucket you must set the following attributes on the `meta` object:

- `auth_status`: set to `'success'` for successful authentications
- `source_ip`: the IP address of the client (required for geoip enrichment)
- `target_user`: the username that logged in
- `service`: the service the user logged in to (e.g., `ssh`, `teleport`)

It is important to set the `service` attribute as this is how the buckets are separated. If you do not set the `service` attribute, all the events for the same user will fall into the same bucket no matter if it was a different service which could lead to false positives.

The scenario detects impossible travel when:
- At least 2 successful authentications are recorded
- The distance between consecutive login locations is greater than 1000 km
- All within a 3 hour window (leakspeed)

Note: This scenario requires geoip enrichment to be enabled (via the `geoip-enrich` parser) to calculate the distance between login locations.