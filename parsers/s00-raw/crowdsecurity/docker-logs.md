# Docker parser

This is the default docker json logs format parser.
It works on kubernetes using docker.

## requirements

When using this parser, you need to specify in your `acquis.yaml` type and program. So your log will be extracted and then sent to the proper next parser using the program key.

example: 

```yaml
labels:
 type: docker
 program: nginx
```
