Parser for [Jellyfin](https://jellyfin.org)  Logs.

```yaml
---
filenames:
 - /var/log/jellyfin/log_*.log
labels:
  type: jellyfin
```

**Note:** If you are using Docker logs (directly or sending them to a syslog server), the output format is incorrect and will not match.  
Create a copy of `logging.default.json` to `logging.json` in Jellyfin config directory (it will override the logging.default.json) and change the console output template like the following :  
```
...
        "WriteTo": [
            {
                "Name": "Console",
                "Args": {
                    "outputTemplate": "[{Timestamp:yyyy-MM-dd HH:mm:ss.fff zzz}] [{Level:u3}] [{ThreadId}] {SourceContext}: {Message:lj}{NewLine}{Exception}"
                }
            },
...
```
