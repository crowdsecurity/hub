## Axigen SMTP probe

Detects repeated SMTP sessions that use common scanner EHLO values (`User` or
`localhost`) and produce a non-passing SPF result. The bucket holds eight
events and leaks one every 30 seconds.

Requires the `Railline/axigen-logs` parser.
