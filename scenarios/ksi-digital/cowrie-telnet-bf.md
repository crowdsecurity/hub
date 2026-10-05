Detects telnet brute force against a [Cowrie](https://github.com/cowrie/cowrie) honeypot: more than 5 failed telnet logins from the same source, leaking one every 10 seconds.

`crowdsecurity/telnet-bf` counts telnet connections. This scenario counts failed logins, which also catches clients that try many credentials over a single connection.

Requires the `ksi-digital/cowrie-json-logs` parser and Cowrie 2.9.0 or later (`protocol` on every event).
