## Overview

Parser for OpenVPN server logs. Supports both legacy syslog and modern ISO8601 timestamp formats.

## Configuration

Add to /etc/crowdsec/acquis.d/openvpn.yaml

## Detected Events

- auth_failed: TLS tls-crypt unwrapping failed (scanner/probe without valid key)
- auth_failed: AUTH_FAILED (failed authentication)
- auth_failed: TLS handshake failed
- auth_failed: Certificate VERIFY ERROR

## Log formats supported

Legacy syslog:
Apr  5 11:26:07 vpn ovpn-server[380]: TLS Error: tls-crypt unwrapping failed from [AF_INET]182.200.116.38:38382

Modern ISO8601:
2026-04-10T12:17:48.771346+02:00 vpn ovpn-server[448]: TLS Error: tls-crypt unwrapping failed from [AF_INET]182.200.116.38:38382
