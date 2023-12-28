## Local Privilege Escalation Detection

This collection aims at detecting (when possible) local privilege escalation attacks.

 - CVE-2021-4034 : Detect exploitation of pkexec vulnerability

:warning: Please note those scenarios are detection only, and are very likely to be bypassed by smart attackers, do not rely solely on them :warning:

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/auth.log
  - /var/log/kern.log
labels:
  type: syslog
```

If you want to get kernel log through journalctl
```
source: journalctl
journalctl_filter:
  - "-k"
labels:
  type: syslog
```

notes :
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
 -  CVE-2023-4911 needs kernel log detection, either kern.log or through journalctl filtering

