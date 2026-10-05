Detects a source that runs shell commands on a [Cowrie](https://github.com/cowrie/cowrie) honeypot after logging in over SSH.

Cowrie only records `cowrie.command.input` once a login has succeeded, so a command means the source guessed or reused credentials and then acted on the system. The scenario triggers on the first command; further commands from the same source are ignored for one hour.

Requires the `ksi-digital/cowrie-json-logs` parser and Cowrie 2.9.0 or later (`protocol` on every event).
