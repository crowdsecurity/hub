Detects a source that transfers a file to a [Cowrie](https://github.com/cowrie/cowrie) honeypot over SSH after logging in:

- `cowrie.session.file_download`: a file fetched from a URL (for example with `wget` or `curl`)
- `cowrie.session.file_download.failed`: an attempted fetch that did not complete
- `cowrie.session.file_upload`: a file uploaded over SFTP or SCP

Files that Cowrie saves from shell redirection (`echo ... > file`, logged as `file_download` without a `url`) are not counted here; they are covered by `ksi-digital/cowrie-ssh-post-auth-commands`.

The scenario triggers on the first transfer; further transfers from the same source are ignored for one hour. Requires the `ksi-digital/cowrie-json-logs` parser and Cowrie 2.9.0 or later.
