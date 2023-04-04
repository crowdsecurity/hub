Detects anonymous access to the K8S API, using the cluster audit logs.

Only attempts done on resources that are logged at least at the `Metadata` level will be recorded.

Access to `healthz`, `livez` and `readyz` are ignored.

No decision will be taken based on this scenario, it is only intended for notification purposes.
