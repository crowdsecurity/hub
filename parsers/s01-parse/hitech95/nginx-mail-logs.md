## Nginx Email Proxy parser
A generic parser for `ngx_mail_core` module:
 - Detect new session
 - Detect auth failures when using `ngx_mail_auth_http_module`

## Acquisition template

```yaml
filenames:
  - /var/log/nginx/*.log
labels:
  type: nginx
```