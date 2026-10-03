## Axigen slow authentication brute force

Detects authentication brute force that is spread out to evade a short
rate-limit window. The bucket holds five events and leaks one every three
minutes.

Requires the `Railline/axigen-logs` parser.
