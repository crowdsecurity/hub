# Description
A parser that will search for unauthorized (401) status code in a log file that gotify is outputting its stdout to. 
From testing it seems gotify returns a 401 for unknown user, bad password, and incorrect tokens. There is no way to 
determine which is which so this parser will only search for 401 status code.

# HOW TO INSTALL PROPERLY
- REQUIRED - example `acquis.yaml` entry - The `type` **MUST** be exactly as shown here or the parser will never be successful.

```yaml
filenames:
  - /path/to/gotify.log
labels:
  type: gotify
```
:exclamation: The `type` **MUST** be `gotify` :exclamation:

# Statics
- The IP is the only data grabbed from the log and is stored in `evt.Parsed.source_ip` and `evt.Meta.source_ip`

# How to - Have Gotify (Docker) log to a file
- You must create your own `Dockerfile` and then build it. Example Dockerfile as follows.
```Dockerfile
FROM gotify/server
ENTRYPOINT /bin/bash -c '/app/gotify-app | tee /app/data/gotify.log'
```
- Build the image `sudo docker build -t <TAG NAME>`
- Example `<TAG NAME>` - server/gotify:logger
- Now make a docker-compose file to use the image, the log file will end up in the `gotify_data` directory
```docker
  gotify:
    image: gotify/server:logger
    container_name: gotify
    restart: always
    ports:
      - 8080:80
    volumes:
      - "./gotify_data:/app/data"

```
