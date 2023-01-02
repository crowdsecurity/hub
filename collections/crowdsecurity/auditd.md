## Auditd collection

A collection for auditd:
 - auditd log parser

Various associated scenarios :
 - post-exploitation typical behavior detection


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/auditd/*.log
labels:
  type: auditd
```

## Warning

The scenario's effectiveness will depend on your `auditd` configuration.
Please refer to individual scenarios, or see [Florian Roth's example auditd config](https://github.com/Neo23x0/auditd/blob/master/audit.rules).


