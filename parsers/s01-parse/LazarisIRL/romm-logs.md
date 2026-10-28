Parser for [RomM](https://github.com/rommapp/romm) logs.

To use the docker socket directly, ensure CrowdSec has access to the Docker socket (`/var/run/docker.sock`)

```yaml
source: docker
container_name:
  - romm
labels:
  type: romm
```

If you are using file-based acquisition, you will need to add the following to your RomM `docker-compose.yaml` in order to write the logs to a file:

```yaml
command: sh -c "/init 2>&1 | tee /path/to/romm.log"
```

Then add:

```yaml
filenames:
  - /path/to/romm.log
labels:
  type: romm
```

## Client IP and reverse proxies

RomM logs both the peer address and the raw `X-Forwarded-For` header. If the peer is a private address, the parser assumes it is a reverse proxy and uses the rightmost public IP from `X-Forwarded-For`. Otherwise it uses the peer address.

This only works if the proxy in front of RomM appends the real client IP to `X-Forwarded-For` (nginx `$proxy_add_x_forwarded_for`, Traefik and Caddy do this by default). The header can be spoofed, or the wrong IP banned, when:

- RomM is reached from a private address without such a proxy (rootless Docker/Podman, IPv6 through `docker-proxy`, LAN/VPN/Tailscale clients)
- the proxy does TCP/TLS passthrough
- a CDN (e.g. Cloudflare) sits in front: restore the real client IP on your proxy first

This should ideally be fixed on the RomM side: its bundled nginx should resolve the client IP itself (`real_ip` module with a configurable list of trusted proxies) and log only that address.
