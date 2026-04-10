## Overview

Detects IPs performing OpenVPN TLS bruteforce or probing attacks.
Bans IPs that trigger 3 or more TLS errors within 15 minutes.

## Configuration

Requires the proonoob/openvpn parser.

## Behavior

- Trigger: 3 TLS errors
- Time window: 15 minutes
- Remediation: ban
