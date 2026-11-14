Detects bruteforce on the [NPMpro](https://github.com/TheBlackBush/NPMpro) web UI login.

It counts failed logins: `POST /api/tokens` (password) and `POST /api/tokens/totp` (2FA code) answered with 401, 403 (wrong credentials or code) or 429 (the NPMpro login rate limit of 5 failed attempts per 5 minutes), received on the NPMpro admin port.

 - leakspeed of 2m, capacity of 5, grouped by source IP: the first attempt after the login rate limit kicks in (the 6th failed login in a row) triggers it, as do slower attempts of about one per minute (after about 10 of them)
 - the admin port is matched as `81`, the default of `NPM_PORT`. It is the port nginx listens on inside the container, so a remapped Docker port (for example `8181:81`) still matches. If you changed `NPM_PORT`, this scenario does not match and you need a local copy with your port
 - requires the access log parsed by `TheBlackBush/npmpro-logs` from a version of NPMpro that logs the receiving port (`$server_port`) as the last field
