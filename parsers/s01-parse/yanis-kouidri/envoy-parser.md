# Envoy JSON logs parser (CRI)

## Description

This parser decodes [Envoy Gateway](https://gateway.envoyproxy.io/) logs formatted as JSON and encapsulated in CRI (standard for Kubernetes/containerd). It extracts HTTP metadata and forwards the event to crowdsecurity/http-logs and other enrichment parsers.

Then it can proceed by http scenarios like the ones in `base-http-scenarios` collection.

Example Log (CRI/JSON)

```log
2023-10-27T10:00:00.000000Z stdout F {"start_time":"2023-10-27T10:00:00.000Z","method":"GET","x-envoy-origin-path":"/admin","response_code":404,"user-agent":"Mozilla/5.0...","downstream_remote_address":"1.2.3.4:5678",":authority":"example.com"}
```

### Extracted Fields

- `source_ip`: Client IP address.
- `http_path`: Requested URL path.
- `http_verb`: HTTP method (GET, POST, etc.).
- `http_status`: Response code.
- `target_fqdn`: Target domain.
- `user_agent`: Client identifier.

### Dependencies

The following components must be installed for this parser to work correctly:

- crowdsecurity/cri-logs.

## Usage

Example of agent part of a `values.yaml` to use with crowdsec helm installation on Kubernetes

```yaml
container_runtime: containerd
agent:
  acquisition:
    - namespace: envoy-gateway-system
      podName: envoy-envoy-gateway-system-envoy-gateway-*
      program: envoy
      poll_without_inotify: true

  env:
    - name: COLLECTIONS
      value: "crowdsecurity/base-http-scenarios"
    - name: PARSERS
      value: "crowdsecurity/cri-logs yanis-kouidri/envoy-parser"
```