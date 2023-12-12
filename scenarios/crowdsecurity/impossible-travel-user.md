Generic implementation of impossible travel to detect users logging in from two different locations in a short period of time. If you wish write a parser to fall into this generic bucket you must set the following attributes on the `meta` object:

- `log_type`: `auth_success`
- `source_ip`: the IP address
- `user`: the user that logged in
- `service`: the service the user logged in to EG `ssh`

It is important to set the `service` attribute as this is how the buckets are separated. If you do not set the `service` attribute, all the events for the same user will fall into the same bucket not matter if it was a different service which could lead to false positives.