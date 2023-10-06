## Auditd : Crash of suid binary

Attempt to detect a SUID binary that crashes with `SIGILL`, `SIGTRAP`, `SIGABRT`, `SIGBUS`, `SIGSEGV`.

It might be related to someone trying to exploit local privilege escalation such as [CVE-2023-4911](https://nvd.nist.gov/vuln/detail/CVE-2023-4911).
