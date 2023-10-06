## Auditd : suspicious executions

Attempt to detect a binary that is executed from unusual / suspicious locations, such as `/tmp/` or hidden directories startimg with a `.`.

This pattern is usually seen in post-exploitation when attackers are attempting to hide backdoors and other tools.
