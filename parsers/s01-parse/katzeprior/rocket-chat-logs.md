Parser for [Rocket.Chat](https://www.rocket.chat/) Logs.

Make sure to enable the following settings under settings->account->Login Logs

1. Log (on console) failed login attempts
2. Show Client IP on failed login attempts logs

If rocket.chat is behind more than 1 proxy, make sure to configure `HTTP_FORWARDED_COUNT` correctly accourding to the [docs](https://docs.rocket.chat/quick-start/environment-configuration/configuring-ssl-reverse-proxy).

Also so the right [timezone](https://docs.rocket.chat/guides/administration/admin-panel/settings/general#timezone) for rocket.chat.

Example acquisition for Journalctl and Docker:
```yaml
---
journalctl_filter:
 - SYSLOG_IDENTIFER=rocketchat
labels:
  type: rocketchat
---
source: docker
container_name:
 - my_container_name
labels:
  type: rocketchat
```