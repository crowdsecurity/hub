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

---
### Files app
The `/core/preview` endpoint returns 404 if a file has no thumbnail (including files which aren't meant to, like XMLs).
This can trigger http-probing when using the file search bar.

---
### Creating files via WebDAV
When uploading files via WebDAV, a PROPFIND request is sent to the server, which returns 404 if the file does not
exist. Then the file is created. Uploading more than 10 files at a time will trigger http-probing.