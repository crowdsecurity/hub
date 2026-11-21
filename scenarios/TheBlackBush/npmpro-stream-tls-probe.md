Detects clients whose connections to an [NPMpro](https://github.com/TheBlackBush/NPMpro) TLS stream keep failing before the TLS handshake ends.

A stream with a certificate writes status 500 to the stream log when the handshake fails or the client leaves before it ends; failures of the upstream are 502 and are not counted. It counts these lines per source IP and stream: more than 15 trigger it, with a leakspeed of 5s and a blackhole of 5m.

 - a TCP health check of a TLS stream also ends with status 500: one check every 5 seconds or less often from one IP never triggers it, a monitor that checks faster than that needs a whitelist
 - on a stream without a certificate, status 500 is a rare internal error
 - the scenario sets no ban length. CrowdSec's default profile bans for 4 hours; see the NPMpro wiki (CrowdSec page) for a profile with 5 minute bans
 - the stream log is only written when Write log files is on, and has to be added to the acquisition (`stream.log`, `type: npmpro`), see the `TheBlackBush/npmpro` collection
