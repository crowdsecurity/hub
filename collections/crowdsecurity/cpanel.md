A collection for cpanel. Contains:
 * cpanel log parser
 * cpanel scenario to detect bruteforce

The relevant `acquis.yaml` should be:

```yaml
filenames:
  - /home/<username>/logs/cpanel/login_log
labels:
  type: cpanel
```
