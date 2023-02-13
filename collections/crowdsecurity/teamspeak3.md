## Teamspeak3 collection

A collection for the [TeamSpeak](https://teamspeak.com/en/) server.
This collection contains :
 - Parsers for TeamSpeak logs
 - Scenario to detect brute force attacks

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /usr/local/teamspeak/logs/ts3server_*.log
  - /home/teamspeak/log/server/ts3server_*.log
labels:
  type: ts3
```

notes :
 - Teamspeak doesn't provide a standard installer, so the log path is relative to your setup
