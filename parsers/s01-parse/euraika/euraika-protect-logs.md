Parse the access and error logs of [Euraika Protect](https://docs.protect.euraika.dev), an nginx-based web application firewall.

Access lines carry the target host and a request identifier:

```
www.example.com 203.0.113.7 - d5b21bae5740ca98e1189502159dc01a - [21/Nov/2026:17:21:06 +0000] "GET /login HTTP/1.1" 200 82704 "-" "curl/8.7.1"
```

Error lines (authentication failures, rate limiting) are parsed as well.

Acquisition example (`/etc/crowdsec/acquis.d/euraika-protect.yaml`):

```yaml
filenames:
  - /var/log/euraika-protect/access.log
  - /var/log/euraika-protect/error.log
labels:
  type: euraika-protect
```
