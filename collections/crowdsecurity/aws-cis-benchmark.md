:warning: This version requires crowdsec version 1.5 :warning:

## AWS CIS Benchmark collection

This collections provides scenario to comply with the various alarms requirements specified in the CIS AWS Foundation Benchmark (https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-cis.html)

## Notifications

This collection is mostly intended for notification purposes, you'll need to update your `/etc/crowdsec/profiles.yaml` to add support for alerts without remediation.

For example, to send a slack notification, add this to the top of the profile configuration file:
```yaml
name: aws_cloudtrail_notif
filters:
 - Alert.GetScenario() startsWith "crowdsecurity/aws-cis-benchmark-"
notifications:
  - http_cloudtrail_notif
on_success: break
---
```

Next, edit `/etc/crowdsec/notifications/http.yaml` (we are using the raw HTTP notification plugin here because the slack notification plugin only support plain text without any formatting):
```yaml
type: http
name: http_cloudtrail_notif
log_level: info
format: |
 {{- $alerts_count := len . -}}
 {
 "attachments": [{
 "color": "#E01E5A",
 "blocks": [
   {{- range $index, $elem := . -}}
   {{- $region := GetMeta . "region" -}}
   {{- $event_uuid := GetMeta . "event_id" -}}
   {{- $account_id := GetMeta . "account_id" -}}
   {{- $event_name := GetMeta . "event_name" -}}
   {{- $user := GetMeta . "user_arn" -}}
   {
     "type": "header",
     "text": {
       "type": "plain_text",
       "emoji": true,
       "text": ":rotating_light: Cloudtrail Alarm :rotating_light:"
     }
   },
   {
     "type": "section",
     "text": {
       "type": "mrkdwn",
       "text": "<https://{{index $region 0}}.console.aws.amazon.com/cloudtrail/home?region={{index $region 0}}#/events/{{index $event_uuid 0}}|View the cloudtrail event in the AWS console>"
     }
   },
   {
     "type": "header",
      "text": {
        "type": "plain_text",
        "text": "Alert Details"
      }
   },
   {
     "type": "section",
     "text": {
       "type": "mrkdwn",
       "text": "*Scenario Name*: {{$elem.Scenario}}\n *Source IP*: {{$elem.Source.Value}}\n *Account ID*: {{index $account_id 0}}\n *Event Name*: {{index $event_name 0}}\n *User*: {{index $user 0}}"
     }
   },
   {
     "type": "header",
     "text": {
       "type": "plain_text",
       "text": "Events details"
     }
   },
   {
     "type": "section",
     "text": {
       "type": "mrkdwn",
       "text": "{{- range $elem.Events -}} {{- range .Meta -}}* *{{.Key}}*: {{.Value}} \n {{end}} {{end}}"
     }
   },
   {
     "type": "divider"
   }
   {{- if lt $index (sub $alerts_count 1) -}}
   ,
   {{- end -}}
   {{ end }}
 ]
 }
 ]
 }
url: <SLACK_WEBHOOK_URL>
method: POST
---
```

More informations about the notification system can be found in [our documentation](https://docs.crowdsec.net/docs/next/notification_plugins/intro)

## Acquisition template

Example acquisition for this collection :

```yaml
source: kinesis
stream_name: cloudtrail-stream
from_subscription: true
labels:
 type: aws-cloudtrail
```