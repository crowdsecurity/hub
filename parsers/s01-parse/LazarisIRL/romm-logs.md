Parser for [RomM](https://github.com/rommapp/romm) logs.

To use the docker socket directly, ensure CrowdSec has access to the Docker socket (`/var/run/docker.sock`)

```yaml
source: docker
container_name:
  - romm
labels:
  type: romm
```

If you are using file based acquisition, add the following to your RomM `docker-compose.yaml`:

```yaml
command: sh -c "/init 2>&1 | tee /path/to/romm.log"
```

Then add:

```yaml
filenames:
  - /path/to/romm.log
labels:
  type: romm
```
