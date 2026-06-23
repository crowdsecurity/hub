# Cowrie Precision Detection

Aggressive detection scenario designed for the Cowrie Honeypot (SSH/Telnet).

## Description
Unlike standard SSH brute-force scenarios that only look for failed logins, this scenario targets automated environment discovery and post-exploitation attempts inside the honeypot. It triggers immediately on both connection attempts (`cowrie-login`) and emulated command executions (`cowrie-command`), routing the attacker to local remediation profiles.
