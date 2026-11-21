A collection to defend [Foundry VTT](https://foundryvtt.com/) server instances against brute force attacks:

- Foundry VTT parser
- Foundry VTT brute force detection

## Whitelist

You may also want to use a whitelist to prevent Foundry triggering http-crawl-non_statics. Mine looks like this and prevents the issue for my foundry subdomain.

```yaml
name: eastcw/foundryvtt-whitelist
description: "Whitelist events from Foundry VTT"
filter: "evt.Meta.log_type in ['http_access-log', 'http_error-log']"
whitelist:
  reason: "Foundryvtt Whitelist"
  expression:
    - evt.Meta.http_verb in ['GET', 'HEAD'] && evt.Meta.target_fqdn == 'foundry.example.com' && evt.Parsed.static_ressource == 'false'
```

## Acquisition Templates

See example acquisitions for this collection below. Foundry V12 changed the way logs are generated and now creates a new file daily.

### For Foundry V11 and lower

If using LOG_FILE environment variable:

```yaml
---
filenames:
  - /PATH_TO_YOUR_FOUNDRY_DATA/Logs/debug.log
labels:
  type: foundryvtt
```

If running via systemd:

```yaml
---
filenames:
  - /PATH_TO_YOUR_FOUNDRY_DATA/Logs/debug.log
  type: foundryvtt
```

### For Foundry V12 and up

If using LOG_FILE environment variable:

```yaml
---
filenames:
  - /PATH_TO_YOUR_FOUNDRY_DATA/Logs/debug.*.log
labels:
  type: foundryvtt
```

If running via systemd:

```yaml
---
filenames:
  - /PATH_TO_YOUR_FOUNDRY_DATA/Logs/debug.*.log
  type: foundryvtt
```
