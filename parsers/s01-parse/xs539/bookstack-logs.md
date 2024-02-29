Parser for [Bookstack](https://www.bookstackapp.com/) logs

You will need to enable [Failed Access Logging](https://www.bookstackapp.com/docs/admin/security/#failed-access-logging) (off by default) 

```
LOG_FAILED_LOGIN_MESSAGE="Failed login for %u"
```

Example acquisition config:
```yaml
---
filenames:
 - /var/log/bookstack.log
labels:
  type: bookstack
---
```
