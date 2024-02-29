# This collection covers sshd and will **NOT** take remediation actions by default.

Detect successful login from a country to another country in a short period of time. This is a strong indicator of a compromised account.

The reason why we have set remediation to false by default is we don't want to lock out legitimate users and want you to fully understand how the collection works before you jump in feet first.

You can enable remediation by setting remediation label within `crowdsecurity/impossible-travel.yaml` to `true` within the `scenarios` folder.

You can enable user remediation by setting remediation label within `crowdsecurity/impossible-travel-user.yaml` to `true` within the `scenarios` folder and you must add a profiles to handle this scope example:

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