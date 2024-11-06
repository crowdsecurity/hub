## Jellyfin Whitelist

### Playing videos
When playing videos a POST request is made to ``/Sessions/Playing/Progress``, Jellyfin will return a 403.

### Browsing Jellyfin (Swiftfin and Roku)
When browsing Jellyfin on Roku and Swiftfin, a GET request is made for non-existent images and Jellyfin will return a 404.
