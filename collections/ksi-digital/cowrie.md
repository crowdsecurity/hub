## Cowrie honeypot (JSON logs)

Support for the JSON event log of the [Cowrie](https://github.com/cowrie/cowrie) SSH and telnet honeypot (`cowrie.json`, one JSON object per line, written by Cowrie's `output_jsonlog` module, which is enabled by default).

Cowrie is a honeypot: no legitimate user has a reason to connect to it. Any source that logs in, runs commands or transfers files on it is acting with hostile intent, so all scenarios in this collection use `confidence: 3`.

The collection contains:

| Item | Detects |
|---|---|
| `ksi-digital/cowrie-json-logs` | Parser for `cowrie.json` events |
| `ksi-digital/cowrie-ssh-post-auth-commands` | Shell commands run after an SSH login |
| `ksi-digital/cowrie-telnet-post-auth-commands` | Shell commands run after a telnet login |
| `ksi-digital/cowrie-ssh-payload-download` | File downloads, download attempts and SFTP/SCP uploads over SSH |
| `ksi-digital/cowrie-telnet-payload-download` | File downloads and download attempts over telnet |
| `ksi-digital/cowrie-telnet-bf` | Repeated failed telnet logins |
| `crowdsecurity/ssh-bf`, `crowdsecurity/ssh-slow-bf` | Repeated failed SSH logins and user enumeration |
| `crowdsecurity/telnet-bf` | Repeated telnet connections |

The parser gives failed SSH logins the `ssh_failed-auth` log type and telnet connections the `telnet_new_session` log type, so the existing hub brute-force scenarios apply to Cowrie without changes.

## Acquisition template

```yaml
filenames:
  - /home/cowrie/cowrie/var/log/cowrie/cowrie.json
labels:
  type: cowrie
```

Adjust the path to your installation. When Cowrie runs in a container, mount its `var/log/cowrie` directory on the host and point `filenames` at `cowrie.json` there.

## Notes

- Cowrie's text log (`cowrie.log` or syslog output) is handled by `crowdsecurity/cowrie-logs`. Both parsers use `type: cowrie` and can be installed together: each one only accepts its own format.
- Cowrie 2.9.0 and later record `protocol` on every event. Older releases only record it on `cowrie.session.connect`; with those, `crowdsecurity/telnet-bf` still works, but the protocol-specific scenarios do not trigger.
- A bouncer on the honeypot host itself blocks attackers from reaching Cowrie and reduces what the honeypot records. Many operators run the honeypot in detection-only mode and use the resulting signals and decisions elsewhere.
- Logins you make to your own honeypot also raise alerts. Add your own addresses to a whitelist (for example an `s02-enrich` whitelist parser).

Maintained by [KSI Digital](https://www.ksi-digital.com/en) (PT Karunia Solusi Informatika).
