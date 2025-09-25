Parser for [Ntfy](https://ntfy.sh) Logs.

```yaml
---
filenames:
 - /var/log/ntfy.log
labels:
  type: ntfy
```

```yaml
---
source: docker
container_name:
 - ntfy
#container_id:
# - 843ee92d231b
labels:
  type: ntfy
```

**Note:** If you want to use a log file, set the log-file option to the file you want to log to and adjust the filename above to match. If you want to use Docker logs, the log-file option must not be set.
You must set the log-level to debug (or trace but trace has more information than is needed) and the log-format to json in order for the parser to be able to detect brute force attempts:
```
log-level: debug
log-format: json
```
For where to set these options when configuring Ntfy, see [Configuring the ntfy server](https://docs.ntfy.sh/config).
