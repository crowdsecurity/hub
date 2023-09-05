Teleport collection includes:
- JSON Parser
- Authentication bruteforce scenarios for webui and tsh

Teleport supports multiple storage backends for storing audit events. The `dir` backend uses the local filesystem of an Auth Service host. When this backend is used, events are written to the filesystem in JSON format. The dir backend rotates the event file approximately once every 24 hours, but never deletes captured events.

Example acquisition:

```yaml
filenames:
  - /var/lib/teleport/log/*.log
labels:
  type: teleport
```