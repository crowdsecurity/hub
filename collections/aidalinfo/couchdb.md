# CouchDB

A collection to defend [CouchDB](https://couchdb.apache.org/).

## Features :

    - Crawl DB
    - Bruteforce
    - Bruteforce on specific DB

# CouchDB Configuration

Enable logging

```
[log]
writer = file
file = /opt/couchdb/var/log/couch.log
```
## Acquis template

Example acquisition for this collection :

```yaml
---
filenames:
  - /path/to/couch.log
labels:
  type: couchdb
```
