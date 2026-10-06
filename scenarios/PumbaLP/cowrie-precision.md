# Cowrie Precision Detection

Detects a source that logs in to, or runs shell commands on, a [Cowrie](https://github.com/cowrie/cowrie) SSH/telnet honeypot.

## Description

Cowrie is a honeypot: no legitimate user has a reason to connect to it. Instead of waiting for a long brute-force run, this scenario counts login attempts (successful or failed) and shell commands (`cowrie.login.*`, `cowrie.command.*`) per source IP. The bucket has a capacity of 2 and leaks one event every 5 minutes, so the scenario triggers on the third such event from the same IP within that window.

It relies on the `PumbaLP/cowrie-json-logs` parser.

## Usage

To install the parser, this scenario and the related hub brute-force scenarios:

```
cscli collections install PumbaLP/cowrie
```

## Configuration

Point CrowdSec at Cowrie's JSON log in `acquis.d/cowrie.yaml`:

```yaml
filenames:
  - /opt/cowrie/var/log/cowrie/cowrie.json
labels:
  type: cowrie
```
