## Axigen authentication brute force

Detects rapid authentication failures from one source across Axigen services.
The bucket holds six events and leaks one event every 30 seconds.

This scenario requires the `Railline/axigen-logs` parser. A companion slow
scenario covers attacks deliberately spread over a longer period.
