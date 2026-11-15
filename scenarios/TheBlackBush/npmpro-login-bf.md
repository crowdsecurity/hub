Detects bruteforce on the [NPMpro](https://github.com/TheBlackBush/NPMpro) web UI login.

It counts failed logins: `POST /api/tokens` (password) and `POST /api/tokens/totp` (2FA code) answered with 401, 403 (wrong credentials or code) or 429 (the NPMpro login rate limit of 5 failed attempts per 5 minutes), received by the NPMpro admin UI.

 - leakspeed of 2m, capacity of 5, grouped by source IP: the first attempt after the login rate limit kicks in (the 6th failed login in a row) triggers it, as do slower attempts of about one per minute (after about 10 of them)
 - the admin UI is matched by its host id: NPMpro writes the host id `npmpro` for every request to it, on any `NPM_PORT`, so a changed admin port or a remapped Docker port is covered, and a proxy host that listens on the same port (host id `proxy-<id>`) is not counted. Older NPMpro versions write no host id: for those lines the scenario falls back to the receiving port `81` (the default `NPM_PORT`); if you changed `NPM_PORT` on such a version, you need a local copy with your port
 - requires the access log (classic or JSON) parsed by `TheBlackBush/npmpro-logs`, from a version of NPMpro that logs the receiving port (`$server_port`); the host id needs a newer version, see above
