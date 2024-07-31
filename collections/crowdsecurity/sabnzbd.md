## Sabnzbd collection

A collection to defend sshd against common attacks :
 - sabnzbd parser
 - sabnzbd bruteforce
 - sabnzbd 'slow' bruteforce

## Acquisition template

The log directory is purely configurable please checkout the [official sabnzbd documentation](https://sabnzbd.org/wiki/advanced/directory-setup) for more information.

Example acquisition for this collection :

```yaml
filenames:
  - /path/to/log/file
labels:
  type: sabnzbd
```
