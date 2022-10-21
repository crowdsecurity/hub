# sshesame collection

A collection to parse sshesame honeypot logs.

* sshesame log parser
* sshesame login and command scenarios

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /var/log/sshesame.log
labels:
  type: sshesame
```

## Notes

* The parser expects sshesame log timestamps to be enabled
* The command scenario will immediately overflow on any command received from a remote client
