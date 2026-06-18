## Stalwart Mail collection

A collection for the Stalwart mail server
 - Stalwart log parser
 - Scenarios for relay denies, internal IP blocking

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /opt/stalwart-mail/logs/stalwart-mail.log
labels:
  type: stalwart
```

If you are running Stalwart [in a container](https://stalw.art/docs/install/docker/).

```yaml
---
source: docker
container_name: 
 -  stalwart-mail
labels:
  type: stalwart
```

notes :
 -  If you are using `journal`/`syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS/install method, paths to log files might change
 -  Only relevant if you are manually installing collection
