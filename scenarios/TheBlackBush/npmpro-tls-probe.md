Detects clients that probe [NPMpro](https://github.com/TheBlackBush/NPMpro) at the TLS layer, such as nmap and testssl.

It counts the lines of the TLS handshake log (`tls.log`, the NPMpro setting TLS handshake log) that `TheBlackBush/npmpro-logs` parses as rejected handshakes (no or an unknown host name, with the default site set to No Response (444)), old TLS versions, no shared cipher or signature algorithm, an ALPN protocol NPMpro does not offer, and data that is not TLS (including plain HTTP on the HTTPS port). Connections closed during the handshake are never counted. Lines over QUIC (HTTP/3) are counted in their own bucket. More than 10 from one IP trigger it, with a leakspeed of 30s and a blackhole of 5m.

 - the log only holds handshakes that end in the default site or the admin UI: a failed handshake that names one of the hosts is not logged
 - shared IPs (mobile networks, company NAT), old devices that retry TLS 1.0, TLS inspection proxies and uptime monitors that connect by IP without a host name can trigger it: whitelist them
 - the scenario sets no ban length. CrowdSec's default profile bans for 4 hours, which is long for a signal that shared IPs can trigger; see the NPMpro wiki (CrowdSec page) for a profile with 5 minute bans
 - the TLS handshake log is only written when the NPMpro setting TLS handshake log is on (it needs Write log files), and has to be added to the acquisition (`tls.log`, `type: npmpro`), see the `TheBlackBush/npmpro` collection
