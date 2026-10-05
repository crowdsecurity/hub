## Cowrie JSON log parser

Parses the JSON event log of the [Cowrie](https://github.com/cowrie/cowrie) SSH and telnet honeypot (`cowrie.json`, one JSON object per line). Each line is decoded once into `evt.Unmarshaled.cowrie`, so every Cowrie field (for example `input`, `url`, `shasum`, `hassh`) is available to scenarios and alert contexts.

Lines that are not a JSON object with a `cowrie.*` `eventid` and a `src_ip` are ignored, so the parser can share `type: cowrie` with `crowdsecurity/cowrie-logs`, which parses Cowrie's text log.

### Fields set

| Meta | Source |
|---|---|
| `source_ip` | `src_ip` |
| `dest_ip`, `dest_port` | `dst_ip`, `dst_port` |
| `target_user` | `username` (login events) |
| `service` | `protocol` (`ssh` or `telnet`), `cowrie` when absent |
| `log_type` | see below |

The event time is taken from `timestamp` (UTC `...Z` or local `...+hhmm` format).

### Log types

| Cowrie event | `log_type` |
|---|---|
| `cowrie.session.connect` over telnet | `telnet_new_session` (as `crowdsecurity/cowrie-logs`, used by `crowdsecurity/telnet-bf`) |
| `cowrie.login.failed` over SSH | `ssh_failed-auth` (as `crowdsecurity/sshd-logs`, used by `crowdsecurity/ssh-bf` and `crowdsecurity/ssh-slow-bf`) |
| `cowrie.session.file_download` without a `url` (file written by shell redirection) | `cowrie_session_file_redirect` |
| any other `cowrie.<a>.<b>` event | `cowrie_<a>_<b>`, e.g. `cowrie_login_success`, `cowrie_login_failed`, `cowrie_command_input`, `cowrie_session_file_download`, `cowrie_session_file_download_failed`, `cowrie_session_file_upload` |

Cowrie 2.9.0 and later record `protocol` on every event. With older releases only `cowrie.session.connect` carries it, and other events get `service: cowrie`.

### Acquisition template

```yaml
filenames:
  - /home/cowrie/cowrie/var/log/cowrie/cowrie.json
labels:
  type: cowrie
```
