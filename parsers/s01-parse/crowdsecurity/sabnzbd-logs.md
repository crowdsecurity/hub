A parser for sabnzbd authentication failures. This parser will attempt to override the `source_ip` with `X-Forwarded-For` common separated values provided by the sabnzbd logs. If the `X-Forwarded-For` is not present, the `source_ip` will be set to the first IP address.

