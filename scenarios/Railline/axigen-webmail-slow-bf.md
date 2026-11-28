## Axigen WebMail slow login brute force

Detects failed Axigen WebMail logins spread over a longer period. It uses the
native `401` response and the public source address correlated through the
Axigen session identifier.

The bucket holds eight failures and leaks one every five minutes. Successful
logins with status `200` are ignored. Requires the `Railline/axigen-logs`
parser.
