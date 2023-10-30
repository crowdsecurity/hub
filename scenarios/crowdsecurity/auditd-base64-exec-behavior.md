## Auditd : base64 exec detection

Attempt to detect a process that is invoking both `base64` and an interpreter such as `sh`, `bash`, `perl`, `dash`, `zsh` or `python`.

This pattern is usually seen in post-exploitation behaviors to have "file less" backdoors :

```bash
echo ZWNobyAnbWFsaWNpb3VzIHBheWxvYWQnCg== | base64 -d | bash
```
