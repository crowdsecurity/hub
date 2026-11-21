## Axigen slow user enumeration

Detects slow attempts to authenticate as many distinct Axigen users. The
bucket holds five different usernames and leaks one every five minutes.
Repeated failures for one username are ignored by this scenario.

Requires the `Railline/axigen-logs` parser.
