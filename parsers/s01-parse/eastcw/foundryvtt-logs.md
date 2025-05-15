Parser for [Foundry VTT](https://foundryvtt.com/) server logs.

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
