# Technitium DNS Server Collection

This collection provides support for monitoring Technitium DNS server authentication failures and detecting brute force attacks.

## Components

- **Parser**: `PintjesB/technitium-logs` - Parses Technitium DNS server authentication failure logs
- **Scenario**: `PintjesB/technitium-bf` - Detects brute force attacks against Technitium DNS server web interface

## Configuration

The Technitium integration requires the following log acquisition configuration:

```yaml
filenames:
  - /syslog-server/technitium.log
labels:
  type: technitium
```

## Features

- Parses Technitium authentication failure logs
- Detects brute force attacks with configurable thresholds
- Extracts source IP, username, and timestamp information
- Supports syslog-based log collection

## Installation

```bash
cscli collections install PintjesB/technitium
```
