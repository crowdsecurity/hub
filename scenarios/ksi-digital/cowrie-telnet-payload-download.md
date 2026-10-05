Detects a source that downloads, or attempts to download, a file onto a [Cowrie](https://github.com/cowrie/cowrie) honeypot over telnet after logging in (`cowrie.session.file_download` with a `url`, or `cowrie.session.file_download.failed`). This is the usual next step of IoT botnets after a telnet login: fetching their binary or loader script.

Files that Cowrie saves from shell redirection are not counted here; they are covered by `ksi-digital/cowrie-telnet-post-auth-commands`.

The scenario triggers on the first transfer; further transfers from the same source are ignored for one hour. Requires the `ksi-digital/cowrie-json-logs` parser and Cowrie 2.9.0 or later.
