## Axigen WebMail login brute force

Detects rapid failed login attempts against the native Axigen WebMail API. It
uses the `401` status written by Axigen and correlates the request with the
public source address stored for the same Axigen session.

The bucket holds five failures and leaks one every minute. Successful logins
with status `200` are ignored. Requires the `Railline/axigen-logs` parser.
