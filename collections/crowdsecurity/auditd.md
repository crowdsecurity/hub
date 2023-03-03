## Auditd collection

A collection for auditd:
 - auditd log parser

Various associated scenarios :
 - post-exploitation typical behavior detection


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/auditd/*.log
labels:
  type: auditd
```

## Warning

The scenario's effectiveness will depend on your `auditd` configuration.
Please refer to individual scenarios, or see [Florian Roth's example auditd config](https://github.com/Neo23x0/auditd/blob/master/audit.rules).


## Notification template

To have nice-looking notifications on auditd alerts, you can use the following format template:

```yaml
format: |
  {{ range . -}}
  {{$alert := . }}
  *{{$alert.Scenario}}*
  {{ range .Events }}
  `{{.GetMeta "exe"}}` invoked by parent process `{{.GetMeta "parent_progname"}}` (uid={{.GetMeta "uid"}})
  {{ end -}}
  {{- end }}
```
