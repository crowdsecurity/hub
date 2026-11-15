## Music Assistant Allowlist

### Album artwork
When a Music Assistant client loads a library view, album artwork is fetched from `/imageproxy/<sha256>` endpoints. The path contains no file extension, so `crowdsecurity/http-logs` classifies it as a non-static resource. Loading a large library therefore produces many distinct URLs in a short time, which can trigger `crowdsecurity/http-crawl-non_statics`. Clients can also cancel artwork requests while scrolling, producing `499` responses that are counted by the same scenario.

This allowlist matches `GET` requests for `/imageproxy/` followed by a 64-character hexadecimal content hash, with a `200`, `304`, `404` or `499` status. Music Assistant answers `404` when an artwork id is no longer known or the upstream provider cannot serve the image, so those requests are legitimate too.

A `403` is deliberately not allowlisted. It is returned by the reverse proxy or by an existing CrowdSec ban, not by Music Assistant, and it is the evidence that a client is already blocked. Allowlisting it would hide that signal, so those requests keep being parsed.

Other paths, verbs, statuses and malformed ids are still parsed normally, so probing unrelated URLs remains detectable.
