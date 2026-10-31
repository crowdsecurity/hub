## Axigen TLS probing

Detects TLS scanners that cycle through at least three distinct handshake
failure types against Axigen within the bucket window.

The use of distinct errors is intentional: legitimate but misconfigured mail
clients often repeat one failure such as `handshake failure`. Repetition of one
error does not trigger this scenario. `certificate unknown` is also ignored
because it commonly reflects a client trust problem rather than scanning.

Requires the `Railline/axigen-logs` parser.
