## Jellyfin Whitelist

### Playing videos
When playing videos a POST request is made to ``/Sessions/Playing/Progress``, Jellyfin will return a 403.

### Browsing Jellyfin (Swiftfin, Roku and Infuse)
When browsing Jellyfin on Roku, Swiftfin and Infuse, a GET request is made for non-existent images and Jellyfin will return a 404.
