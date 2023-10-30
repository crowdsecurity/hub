## Bookstack collection

A collection to defend Bookstack against common attacks :
 - bookstack failed login


## Acquisition template

Example acquisition for this collection :

```yaml
---
filenames:
 - /var/log/bookstack.log
labels:
  type: bookstack
---
```

notes :
 - You will need to enable [Failed Access Logging](https://www.bookstackapp.com/docs/admin/security/#failed-access-logging) (off by default) 
