# Description
A parser that will search for failed authentication attempts. 

# Configuration
- Modify the `acquis.yaml` configuraiton file. The `type` **MUST** be exactly as shown here or the parser will never be successful.

```yaml
filenames:
  - /path/to/apache-guacamole.log
labels:
  type: apache-guacamole
```
:exclamation: The `type` **MUST** be `apache-guacamole` :exclamation: