author: xulianh
classification:

AppSec
Proxy
tags:
xray
brute-force

🛡️ X-ray Brute-Force Detection
📝 Description
This scenario is designed to detect brute-force authentication attempts or port scanning targeting an X-ray proxy service. It actively monitors connection events that the X-ray parser explicitly classifies with a rejected action type.

⚙️ Detection Logic
The scenario implements a leaky bucket algorithm to control the frequency of failed access attempts per source IP address, handled in an isolated and concurrent manner:

Capacity: 5 events (the 6th event within the time window triggers the bucket overflow).

Leak Speed: 20 seconds.

Trigger: If a single source IP address accumulates more than 5 rejected connection attempts within a 20-second sliding window, the bucket overflows, triggering a security alert and requesting a remediation decision (blocking).

Resilience to Mixed Traffic: In accordance with best practices for signature design, the correlation logic discriminates concurrent malicious bursts without being affected by the presence of interleaved legitimate traffic (accepted). Successful connections from an IP do not clear or reset the failure counter for that same IP, neutralizing common signature evasion techniques via legitimate noise injection.

📊 Architecture Flow
[Incoming Connection] --> [X-ray Service] --> [Log Entry (rejected)]
|
v
[Alert / Decision] <--- [Bucket Overflowed] <--- [Scenario Engine]

🧪 Validation and Testing
To ensure the scenario operates correctly before distribution, the pipeline behavior must be validated using the integrated hubtest development framework on a controlled injection vector, isolating tests from the global server installation.

The execution of the standard simulation is performed via the local test suite using the following command:
cscli hubtest run xray-brute-force

To interactively inspect the complete state transition tree and the line-by-line evaluation of syntactic expressions (equivalent to the explain command in a production environment), the detailed diagnostic directive is invoked:
cscli hubtest explain xray-brute-force --verbose

🔍 Verification and Best Practices
The framework confirms simulation success when processing the lines generates the corresponding overflow alerts for the evaluated IP addresses, matching the signatures saved in local assertion files (parser.assert and scenario.assert).

Security Standards for Test Vector Generation:

When building or updating the xray_sample.log simulation file located in the .tests/xray-brute-force/ path, it is strictly forbidden to include operational or private IP addresses extracted directly from production infrastructure. If real logs are captured from the service using filtering tools such as tail, a mandatory anonymization process must be performed before delivery.

It is recommended to replace nodes with address blocks reserved exclusively for documentation in accordance with RFC 5737 (such as the 192.0.2.0/24 or 198.51.100.0/24 networks). This ensures code portability in continuous integration (CI) environments and prevents unwanted leakage of server network topology into public community repositories.
