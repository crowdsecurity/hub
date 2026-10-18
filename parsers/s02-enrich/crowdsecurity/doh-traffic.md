## DoH (DNS over HTTPS) traffic

When a browser or the OS resolver is configured to use a self-hosted
DNS-over-HTTPS endpoint (for example `https://dns.example.com/dns-query`), it
sends `GET`/`POST` requests to `/dns-query`
([RFC 8484](https://www.rfc-editor.org/rfc/rfc8484)).

Two things make that traffic look suspicious:

- The endpoint path has no file extension, so the requests look like dynamic
  assets to `http-crawl-non_statics`.
- When discovering or validating the endpoint, some clients (Chrome on Android)
  probe **every prefix of the path**: `/d`, `/dn`, `/dns`, `/dns-qu`,
  `/dns-que`, ... until `/dns-query`. The incomplete ones are not valid DoH
  endpoints, so they are answered with **401**. That looks like a login
  brute-force to the generic 401 scenario (`http-generic-401-bf`), which can ban
  the legitimate client.

Only the DoH endpoint path and its discovery prefixes are whitelisted. Every
other path of the same host is still inspected.
