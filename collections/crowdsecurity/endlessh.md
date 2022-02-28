## Endlessh collection

A collection for [Endlessh](https://github.com/skeeto/endlessh)
 * log parser
 * brute-force scenario

> Contribution by https://github.com/bamx23

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /var/log/endlessh.log
labels:
  type: endlessh
```

You need to configure Endlessh to write logs to this path.
I.e. by having this line in `/usr/lib/systemd/system/endlessh.service`:

```
StandardOutput=file:/var/log/endlessh.log
```
