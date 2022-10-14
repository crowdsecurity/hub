## Exchange collection

A collection for Microsoft Exchange:
 - Detect bruteforce on an OWA instance
 - Detect bruteforce on the SMTP service of Exchange

Note:
 - This collection will read the exchange transport logs, which are not written to disk in real time. In order to avoid false positive in low traffic environment, set the `use_time_machine` parameter to `true`.

## Acquisition template

Example acquisition for this collection:

```yaml
use_time_machine: true #Process logs as if we were replaying them to get the timestamp from the 
filenames:
  - C:\Program Files\Microsoft\Exchange Server\V15\TransportRoles\Logs\FrontEnd\ProtocolLog\SmtpReceive\*.LOG
labels:
  type: exchange-smtp
---
use_time_machine: true #Process logs as if we were replaying them to get the timestamp from the 
filenames:
  - C:\Program Files\Microsoft\Exchange Server\V15\Logging\Imap4\*.LOG
labels:
  type: exchange-imap
---
use_time_machine: true #Process logs as if we were replaying them to get the timestamp from the 
filenames:
  - C:\Program Files\Microsoft\Exchange Server\V15\Logging\Pop3\*.LOG
labels:
  type: exchange-pop
---
#OWA failed attempts are logged in the same way as RDP failed auth 
source: wineventlog
event_channel: Security
event_ids:
 - 4625
event_level: information
labels:
 type: eventlog
```