## Kubernetes Audit collection

A collection for Kubernetes audit logs :
 - Kubernetes audit logs parser
 - Scenarios to detect security related events (privileged pod creation, exec into a pod, mounting a sensitive host folder, ...)

Most scenarios in this collection will *not* lead to a decision, they are mostly intented for notification purpose.

## Notifications

As this collection is mostly intended for notifications, you will need to update your `/etc/crowdsec/profiles.yaml` to add support for alerts without remediation.

For example, if you want slack notifications, add the following at the top of the file:
```yaml
name: k8s_audit_notification
filters:
 - Alert.Remediation == false && Alert.GetScenario() startsWith "crowdsecurity/k8s-audit"
notifications:
  - slack_k8s_audit
on_success: break
---
```

Next, edit `/etc/crowdsec/notifications/slack.yaml` as follow:
```yaml
type: slack
name: slack_k8s_audit

log_level: info

format: |
  Kubernetes Security Alert: 
  {{range . -}}
  {{$alert := . -}}
  {{- $resource_name := GetMeta $alert "resource_name" -}}
  {{- $resource_kind := GetMeta $alert "kind" -}}
   - Scenario: {{$alert.Scenario}}
   - Source IP: {{GetMeta $alert "source_ip"}}
   - User: {{GetMeta $alert "user"}}
   - Namespace: {{GetMeta $alert "namespace"}}
   {{- if $resource_name }}
   - Resource Name: {{GetMeta $alert "resource_name"}}
   {{- end -}}
   {{- if $resource_name }}
   - Resource Kind: {{GetMeta $alert "kind"}}
   {{- end }}
  ----
  {{end -}}


webhook: <WEBHOOK_URL>
```

More informations about the notification system can be found in [our documentation](https://docs.crowdsec.net/docs/next/notification_plugins/intro)

## Acquisition template

Example acquisition for this collection if you log to a file:

```yaml
filenames:
  - /var/log/k8s/audit.log
labels:
 type: k8s-audit
```

Example acquisition for this collection if you use the `k8s_audit` datasource:
```yaml
source: k8s_audit
listen_addr: 0.0.0.0
listen_port: 4242
webhook_path: /audit/webhook/event
labels:
 type: k8s-audit
```
