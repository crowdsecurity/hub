## RocketChat whitelist

### Avatar

RocketChat loads avatars as `/avatar/<username>` or `/avatar/room/<room_uuid>`, since the URL's does not end in a static extension such as `.jpg` it can trigger `http-crawl-non_statics`
