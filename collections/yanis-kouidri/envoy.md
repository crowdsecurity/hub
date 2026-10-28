## Envoy collection

A collection to defend Envoy Gateway against common attacks:
 - Envoy default access log format and JSON parser (CRI/containerd)
 - base http scenarios (crawl, 404 scan, bf)

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /path/to/file
labels:
  type: envoy
```

Example acquisition for Kubernetes (containerd/CRI):

```yaml
container_runtime: containerd
agent:
  acquisition:
    - namespace: envoy-gateway-system
      podName: envoy-envoy-gateway-system-envoy-gateway-*
      program: envoy
      poll_without_inotify: true
```
