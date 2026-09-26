## Axigen user enumeration

Detects one source attempting to authenticate as many distinct Axigen users.
The bucket holds five different usernames and leaks one every minute. Repeated
failures for the same username do not fill this bucket.

Requires the `Railline/axigen-logs` parser.
