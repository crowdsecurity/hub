## Overseerr Whitelist

### Browsing Movies, Series or Requests
When scrolling fast while using Overseerr on the Movies, Series or Requests pages, many GET requests are made to ``/api/v1/(movie|tv|request)``. The http-crawl-non_statics scenario will be triggered if too many requests to the API are made too quickly unless this whitelist is used.
