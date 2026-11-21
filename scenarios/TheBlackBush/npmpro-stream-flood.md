Detects clients that open too many connections to an [NPMpro](https://github.com/TheBlackBush/NPMpro) stream (a TCP or UDP proxy).

It counts the lines of the stream log written by `TheBlackBush/npmpro-logs`, grouped by source IP and stream (the stream id, or the port when the line has no stream id). A client that makes more than 40 connections per second to one stream triggers it, with a leakspeed of 1s and a blackhole of 1m.

 - the threshold is for a plain connection flood. Some stream protocols open many short connections on purpose (for example a database pool behind NPMpro), so check the log of your own streams before you rely on it, and use a local copy with a higher capacity if needed
 - the stream log is only written when Write log files is on, and has to be added to the acquisition (`stream.log`, `type: npmpro`), see the `TheBlackBush/npmpro` collection
