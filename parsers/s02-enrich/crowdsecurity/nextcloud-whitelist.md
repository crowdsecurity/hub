## Nextcloud whitelist

### Contacts app
Contacts has an issue with excessive 404 response codes when a user image is missing
[Upstream issue](https://github.com/nextcloud/contacts/issues/3021)

---
### Photos app
On first load the photos app calls a preview endpoint, however, if it fails to load it will trigger http-probing

When opening the photos app, multiple requests are made very quickly for images, since they are not marked as images (ending in png,jpg etc) it can trigger HTTP crawl non statics.

---
### Backup app
When loading backups for a file if those backups have been modified or deleted by (OS/USER) it can easily trigger http-probing

---
### Files app
The `/core/preview` endpoint returns 404 if a file has no thumbnail (including files which aren't meant to, like XMLs).
This can trigger http-probing when using the file search bar.

When previews are missing for files in the trash bin, a 404 error is returned which triggers http probing.

In rare cases HTTP Probing will be triggered when opening multiple folders quickly, Nextcloud checks for a ``readme.md`` file and if it doesn't exist a 404 error is thrown.

---
### Creating files via WebDAV
When uploading files via WebDAV, a PROPFIND request is sent to the server, which returns 404 if the file does not
exist. Then the file is created. Uploading more than 10 files at a time will trigger http-probing.

When syncing large amount of files via WebDAV, it could trigger http-probing so the expression also whitelists 200 response codes.

---
### Reshares via federation
When shared files via federation are reshared, the federated instance can scan each directory to find `readme.md` file with a `PROPFIND`, even if it doesn't exist.

---
### Trashbin
Whilst browsing deleted files in the trashbin, a 404 error is thrown when a file has no preview thumbnail. This can trigger http-probing.

---
### Bookmarks
Whilst browsing bookmarks a 404 response could be sent if the bookmarked page had no favicon or image attached.

Whilst browsing private folder on the bookmark app a 404 response could be sent if the bookmarked page had no publictoken generated.

