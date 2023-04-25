## Zammad whitelist

### Attachments
When downloading attachments (or the zammad-SPA fetches attachment previews), `crowdsecurity/http-crawl-non_statics` may trigger HTTP crawl non statics,
since the Attachment-/Preview-URLs are not marked as images (ending in png,jpg etc) or PDF.

When fetching attachments with argument `view=inline`, zammad may return http-status 403 (not sure why, maybe short-living session ended?): this can trigger `crowdsecurity/http-probing`.
