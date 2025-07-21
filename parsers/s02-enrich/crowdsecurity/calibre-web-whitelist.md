## Calibre-Web Whitelist

### Loading Book Covers
When loading the homepage of an Calibre-Web instance, requests for all book covers shown on the homepage are made (``/cover/<book number>/md?c=<numbers>``). Since the book covers have no extension, they are not considered static files and will trigger http-crawl-non_statics if this whitelist is not used once there are more than ~40 books shown on the homepage.
