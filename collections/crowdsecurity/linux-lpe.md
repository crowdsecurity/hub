## Local Privilege Escalation Detection

This collection aims at detecting (when possible) local privilege escalation attacks.

 - CVE-2021-4034 : Detect exploitation of pkexec vulnerability

:warning: Please note those scenarios are detection only, and are very likely to be bypassed by smart attackers, do not rely solely on them :warning:

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/auth.log
labels:
  type: syslog
```

notes :
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection

