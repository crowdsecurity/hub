## Actual Budget Whitelist

### Loading Database Migrations
When loading the homepage of an Actual Budget instance, even before logging in, requests for database migrations are made (``/data/migrations/<migration-name>.sql``). Files ending in .sql are non static files which will trigger http-crawl-non_statics and are also sensitive files which will trigger http-sensitive-files if this whitelist is not used.
