# adguardhome-dot-errors

Parser for AdGuard Home DoT (DNS-over-TLS, port 853) connection reset errors.

## Description

AdGuard Home logs connection reset errors when a client connects to port 853 (DoT) but does not complete a proper TLS handshake. This is a common indicator of port scanners and probers.

This parser extracts the remote IP address and sets the `dot_connection_reset` log type for use by the `PumbaLP/adguardhome-dot-scan` scenario.

## Matched log example
2026/04/04 20:41:41.673779 [error] dnsproxy: reading msg proto=tcp err="reading len: read tcp 172.20.2.2:853->85.217.140.42:59208: read: connection reset by peer"
## Limitations

- Only `connection reset by peer` errors contain a remote IP and are actionable.
- Other DoT errors (TLS version mismatch, cipher suite errors, unexpected EOF) do not contain a remote IP.
- DoQ (port 8853/udp) and direct DoH (port 443) errors also do not contain remote IPs.
- DoH via a reverse proxy (e.g. Nginx) is covered by `crowdsecurity/nginx-logs`.

## Acquisition

```yaml
source: docker
container_name:
  - adguardhome
labels:
  type: adguardhome
Or with log file:
filenames:
  - /var/log/AdGuardHome.log
labels:
  type: adguardhome
