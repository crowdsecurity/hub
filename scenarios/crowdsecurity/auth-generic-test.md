# auth generic test

This scenario is meant to check if CrowdSec is correctly configured for authentication services (excluding SSH, which has its own test scenario). This will trigger an alert, but no decision.

## How to trigger

Attempt a failed login with a username that starts with `crowdsec-test-NtktlJHV4TfBSK3wvlhiOBnl`. The scenario uses `startsWith` matching, so you can use either:

- Plain username: `crowdsec-test-NtktlJHV4TfBSK3wvlhiOBnl`
- Email format: `crowdsec-test-NtktlJHV4TfBSK3wvlhiOBnl@example.com`

### Examples for different services

**Authentik / Authelia:**
- Try logging in with username: `crowdsec-test-NtktlJHV4TfBSK3wvlhiOBnl` or `crowdsec-test-NtktlJHV4TfBSK3wvlhiOBnl@example.com`
- Use any password (it should fail)

**Gitea / Jellyfin / Jellyseerr / Grafana / Harbor:**
- Try logging in with username: `crowdsec-test-NtktlJHV4TfBSK3wvlhiOBnl` or `crowdsec-test-NtktlJHV4TfBSK3wvlhiOBnl@example.com`
- Use any password (it should fail)

**Web-based authentication services:**
- Navigate to the login page of your service
- Enter username: `crowdsec-test-NtktlJHV4TfBSK3wvlhiOBnl` (or with `@domain.com` suffix)
- Enter any password
- Submit the login form (it should fail)

**Note:** This scenario only works for authentication services other than SSH. For SSH testing, use the `crowdsecurity/ssh-generic-test` scenario instead.

## Expected results

You will see in your CrowdSec logs:

```
time="2025-06-12T16:59:45+02:00" level=info msg="Ip <your-ip> performed 'crowdsecurity/auth-generic-test' (1 events over 0s) at 2025-06-12 14:59:45.636887959 +0000 UTC"
time="2025-06-12T16:59:46+02:00" level=info msg="(<local API login>) alert : crowdsecurity/auth-generic-test by ip <your-ip> xxxxxx"
time="2025-06-12T16:59:47+02:00" level=info msg="Signal push: 1 signals to push"
```

`cscli alert list` will present you this alert as well. Please note that this scenario won't trigger any decision, and result in any remediation.

If you don't see anything in logs nor in the alerts list, then you can assume an issue in your setup.

## Requirements

This scenario requires your parser to set the following meta fields:
- `auth_status`: set to `'failed'` for failed authentication attempts
- `target_user`: the username that attempted to log in (can be plain username or email format)
- `service`: the service name (e.g., `authentik`, `gitea`, `jellyfin`, `grafana`, `harbor`, etc.)
- `source_ip`: the IP address of the client

Beware this WON'T work with local IPs (see [whitelists](https://github.com/crowdsecurity/hub/blob/master/parsers/s02-enrich/crowdsecurity/whitelists.md) that are installed by default).

