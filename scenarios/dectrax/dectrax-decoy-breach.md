# DECTRAX Decoy Engagement & Interdiction Trigger

## Description

Triggers an immediate high-confidence remediation decision (`remediation: true`, `confidence: 3`) whenever an IP interacts with any DECTRAX decoy sensor or honeytoken.

Because deception sensors have zero legitimate business utility, any connection attempt constitutes malicious intent (scans, brute force, lateral movement).

## Remediation

Immediately bans the offender IP address via configured CrowdSec bouncers (iptables, nftables, Cloudflare, AWS WAF, etc.).

## MITRE ATT&CK Mappings

- `T1021.001`: Remote Services: Remote Desktop Protocol
- `T1078`: Valid Accounts
- `T1046`: Network Service Discovery
- `T1110`: Brute Force

## Documentation & Project Links

- Official Website: [https://dectrax.com](https://dectrax.com)
- Platform Documentation: [https://dectrax.com/docs](https://dectrax.com/docs)
