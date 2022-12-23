## Nextcloud whitelist

### Contacts app
Contacts has an issue with excessive 404 response codes when a user image is missing
[Upstream issue](https://github.com/nextcloud/contacts/issues/3021)
---
### Photos app
On first load the photos app calls a preview endpoint, however, if it fails to load it will trigger http-probing
---
### Backup app
When loading backups for a file if those backups have been modified or deleted by (OS/USER) it can easily trigger http-probing