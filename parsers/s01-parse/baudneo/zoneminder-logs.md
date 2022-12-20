# Description
A parser that searches for unknown user and incorrect password logins to ZoneMinder by using `web_php.log` as a data source.
Now supports new PHP date format; DEFAULT US/CAN format.

# HOW TO INSTALL PROPERLY
- REQUIRED - example `acquis.yaml` entry - the `type` must be exactly as shown here or the parser will never be successful.
***The log path is the default path on a debian based distro, change to point towards where your ZoneMinder `web_php.log` is***
```yaml
filenames:
  - /var/log/zm/web_php.log
labels:
  type: zoneminder
```
:exclamation: The `type` **MUST** be `zoneminder` :exclamation:

# Statics
- IP is logged as `evt.Parsed.source_ip` and `evt.Meta.source_ip`
- Username is logged as `evt.Parsed.username` and `evt.Meta.username`
