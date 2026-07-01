~---
author: xulianh
classification:
  - AppSec
  - Proxy
tags:
  - xray
  - brute-force
---

# X-ray Brute-Force Detection

## Description
This scenario is designed to detect brute-force authentication attempts or network scanning directed at an X-ray proxy service. It actively monitors connection attempts that the X-ray parser explicitly flags as `rejected`.

## Detection Logic
The scenario implements a leaky bucket algorithm to monitor the frequency of failed connection attempts per source IP address:

* **Capacity:** 5 events.
* **Leak Speed:** 20 seconds.
* **Trigger:** If a single source IP address accumulates more than 5 rejected connection attempts within a 20-second rolling window, the bucket overflows, triggering a security alert.

### Architecture Flow

```text
[Incoming Connection] --> [X-ray Service] --> [Log Entry (rejected)]
                                                    |
                                                    v
[Alert Generated] <--- [Threshold Exceeded] <--- [CrowdSec Parser]
```

## Validation and Testing
To ensure the scenario operates correctly before deploying to production, it can be tested using a sample log file containing simulated rejected connections.

Run the following command using the CrowdSec CLI tool:

```bash
cscli explain --scenario ./scenarios/xulianh/xray-brute-force.yaml --log ./tests/xray_sample.log
```
### Verify that the output indicates the bucket successfully parsed the events and triggered an overflow after the 5th rejected attempt.

You could generate your xray_sample.log directly from real events as follows:
sudo tail -n 2 /var/log/xray/access.log > ./tests/xray_sample.log
