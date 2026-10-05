Detects a source that runs shell commands on a [Cowrie](https://github.com/cowrie/cowrie) honeypot after logging in over telnet. This is typical of IoT botnets that log in with factory-default credentials and then probe the device shell.

Cowrie only records `cowrie.command.input` once a login has succeeded. The scenario triggers on the first command; further commands from the same source are ignored for one hour.

Requires the `ksi-digital/cowrie-json-logs` parser and Cowrie 2.9.0 or later (`protocol` on every event).
