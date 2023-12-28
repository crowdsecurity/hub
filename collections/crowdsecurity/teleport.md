Teleport collection includes:
- JSON Parser
- Authentication bruteforce scenarios for webui and tsh
- Impossible travel detection

Teleport supports multiple storage backends for storing audit events. The `dir` backend uses the local filesystem of an Auth Service host. When this backend is used, events are written to the filesystem in JSON format. The dir backend rotates the event file approximately once every 24 hours, but never deletes captured events.

Example acquisition:

```yaml
filenames:
  - /var/lib/teleport/log/*.log
labels:
  type: teleport
```

### Impossible travel remediation

The reason why we have set remediation to false by default is we don't want to lock out legitimate users and want you to fully understand how the collection works before you jump in feet first.

You can enable remediation by setting remediation label within crowdsecurity/impossible-travel.yaml to true within the scenarios folder.

You can enable user remediation by setting remediation label within crowdsecurity/impossible-travel-user.yaml to true within the scenarios folder and you must add a profiles to handle this scope example:

```yaml
#/etc/crowdsec/profiles.yaml.local
name: username_temp_ban
filters:
 - 'Alert.Remediation == true && Alert.GetScope() == "username"'
decisions:
  - type: tempban
    scope: "username"
    duration: 12h
on_success: break
```

#### However, most bouncers dont know how to handle user remediation I will append a blog post on how to handle this in the future.