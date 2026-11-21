Detect a client sending unauthenticated requests to many distinct [Plex Media Server](https://www.plex.tv) endpoints.

Plex answers `401` to requests without a valid token. Scanners enumerating the Plex API therefore produce `401` responses, which `crowdsecurity/http-probing` does not count (it only counts `400`, `403` and `404`).

The scenario triggers when one IP receives `401` on more than 20 distinct paths, with a leak speed of 10 seconds. A client repeating the same request with an expired token does not trigger it.

A Plex app whose token was revoked (for example, after its user lost access to a shared library) can also receive `401` on many endpoints when it starts, and be banned.

Requires the `andrebrait/plex-logs` parser.
