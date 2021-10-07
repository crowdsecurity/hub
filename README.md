
<p align="center">
<img src="https://raw.githubusercontent.com/crowdsecurity/hub/update_readme/assets/crowdsec_hub.svg" alt="CrowdSec" title="CrowdSec" width="400" height="260"/>
</p>
</br>
<p align="center">
<img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/AlteredCoder/ed74e50c43e3b17bdfc4d93149f23d37/raw/a473458a57da096789e79c4538b432ceeac2d853/hub_parsers_badge.json">
<img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/AlteredCoder/ed74e50c43e3b17bdfc4d93149f23d37/raw/a473458a57da096789e79c4538b432ceeac2d853/hub_scenarios_badge.json">
</p>

<p align="center">
:books: <a href="https://doc.crowdsec.net">Documentation</a>
:diamond_shape_with_a_dot_inside: <a href="https://hub.crowdsec.net">Configuration Hub</a>
:speech_balloon: <a href="https://discourse.crowdsec.net">Discourse (Forum)</a>
:speech_balloon: <a href="https://gitter.im/crowdsec-project/community?utm_source=share-link&utm_medium=link&utm_campaign=share-link">Gitter (Live chat)</a>
</p>


> CrowdSec Hub for parsers, enrichers and scenarios.

# Foreword

This repository stores most of the official parsers/scenarios/collections for crowdsec.

The repository is not intended for use as-is, but rather as source of truth for the [CrowdSec Hub](https://hub.crowdsec.net/) and `cscli`.

Feel free to use the parsers/scenarios here as a source of inspiration.

# Testing & Continuous integration

`cscli` provides a `hubtest` sub-command to help contributors to create tests for parsers and scenarios.


## View & use existing tests

:warning: most of `cscli hubtest` commands are expected to be run from the root directory of the hub. A git clone of this repository is the easier way to work :warning:

> list existing tests

`cscli hubtest list` 


> run a specific test

`cscli hubtest run [test-name]` 


> show current tests coverage

`cscli hubtest coverage`

## Create your own (parser) test

We're going to create the CI tests for the dovecot-parser. Before you start :
 - you will need some *actual* logs
 - you'd better know if the service logs on its own or via syslog (we're in the later case here)

1. Create a new test

```bash
▶ cscli hubtest create dovecot-logs --type syslog

  Test name                   :  dovecot-logs
  Test path                   :  .../github/hub/.tests/dovecot-logs
  Log file                    :  .../github/hub/.tests/dovecot-logs/dovecot-logs.log (please fill it with logs)
  Parser assertion file       :  .../github/hub/.tests/dovecot-logs/parser.assert (please fill it with assertion)
  Scenario assertion file     :  .../github/hub/.tests/dovecot-logs/parser.assert (please fill it with assertion)
  Configuration File          :  .../github/hub/.tests/dovecot-logs/config.yaml (please fill it with parsers, scenarios...)

```

What is relevant here is that every test is composed of :

 - A log file and it's associated type (same `type` as seen in acquis `labels:type`)
 - A configuration specifying which parsers and/or scenarios must be enabled for the test
 - A *ultimately* list of assertions that must be run against the parsers and/or scenarios output

Note: You can provide the parsers and scenarios you want in your test with `--parsers` and `--scenarios` (you can provide multiple parsers and scenarios)

If you want to test only a scenario, you can specify (`--ignore-parsers`) or set the `ignore_parsers` to `true` in the config.yaml

2. Configure your test


We need to edit the test configuration to use the relevant parsers :

```bash
▶ cat .../github/hub/.tests/dovecot-logs/config.yaml
parsers:
- crowdsecurity/syslog-logs
- crowdsecurity/dovecot-logs
scenarios:
postoverflows:
- ""
log_file: dovecot-logs.log
log_type: syslog

```

_note: the order doesn't matter. If the parser name is in the form `author/parser` it's from the hub, but relative paths are allowed for non-versioned parsers_

Now we need to dump some actual logs into the test's log file :

```bash
▶ cat > .tests/dovecot-logs/dovecot-logs.log 
Jan 28 10:16:13 dovecot-box dovecot[7508]: imap-login: Disconnected (auth failed, 1 attempts in 6 secs): user=<toto@toto.com>, method=PLAIN, rip=4.4.4.4, lip=7.7.7.7, TLS, session=<3650VvK5bdIaW-iK>
Sep 8 07:16:29 canyon dovecot: auth-worker(24058): pam(toto,1.1.1.1,<youpi>): pam_authenticate() failed: Authentication failure (password mismatch?)
Sep 8 07:46:51 canyon dovecot: auth-worker(24544): pam(toto,1.1.1.1): unknown user

```


3. Run the test for the first time

Now that we have config & logs, let's run it for the first time :

```bash
▶ cscli hubtest run dovecot-logs
INFO[27-09-2021 06:13:59 PM] Running test 'dovecot-logs'                  
INFO[27-09-2021 06:13:59 PM] parser 'crowdsecurity/dovecot-logs' installed succesfully in runtime environment 
INFO[27-09-2021 06:13:59 PM] parser 'crowdsecurity/syslog-logs' installed succesfully in runtime environment 
WARN[27-09-2021 06:14:02 PM] Assert file '/home/bui/github/hub/.tests/dovecot-logs/parser.assert' is empty, generating assertion: 

results["s00-raw"]["crowdsecurity/syslog-logs"][0].Success == true
...
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Success == true
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["pid"] == "7508"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["timestamp"] == "Jan 28 10:16:13"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["dovecot_login_result"] == "Disconnected (auth failed, 1 attempts in 6 secs)"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["message"] == "imap-login: Disconnected (auth failed, 1 attempts in 6 secs): user=<toto@toto.com>, method=PLAIN, rip=4.4.4.4, lip=7.7.7.7, TLS, session=<3650VvK5bdIaW-iK>"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["logsource"] == "syslog"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["program"] == "dovecot"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["protocol"] == "imap"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["dovecot_local_ip"] == "7.7.7.7"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["dovecot_remote_ip"] == "4.4.4.4"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["dovecot_user"] == "toto@toto.com"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Meta["datasource_path"] == "dovecot-logs.log"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Meta["datasource_type"] == "file"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Meta["log_type"] == "dovecot_logs"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Meta["source_ip"] == "4.4.4.4"
...
```

As our `parser.assert` is empty, the tool is generating some "suggested" asserts for us.
Your careful eye will keep only the ones relevant to the parser you're testing :


```bash
▶ cat > .tests/dovecot-logs/parser.assert 
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Success == true
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["pid"] == "7508"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["timestamp"] == "Jan 28 10:16:13"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["dovecot_login_result"] == "Disconnected (auth failed, 1 attempts in 6 secs)"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["message"] == "imap-login: Disconnected (auth failed, 1 attempts in 6 secs): user=<toto@toto.com>, method=PLAIN, rip=4.4.4.4, lip=7.7.7.7, TLS, session=<3650VvK5bdIaW-iK>"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["logsource"] == "syslog"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["program"] == "dovecot"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["protocol"] == "imap"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["dovecot_local_ip"] == "7.7.7.7"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["dovecot_remote_ip"] == "4.4.4.4"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Parsed["dovecot_user"] == "toto@toto.com"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Meta["datasource_path"] == "dovecot-logs.log"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Meta["datasource_type"] == "file"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Meta["log_type"] == "dovecot_logs"
results["s01-parse"]["crowdsecurity/dovecot-logs"][0].Evt.Meta["source_ip"] == "4.4.4.4"
results["s01-parse"]["crowdsecurity/dovecot-logs"][1].Success == true
results["s01-parse"]["crowdsecurity/dovecot-logs"][1].Evt.Parsed["dovecot_login_result"] == "Authentication failure (password mismatch?)"
results["s01-parse"]["crowdsecurity/dovecot-logs"][1].Evt.Parsed["logsource"] == "syslog"
results["s01-parse"]["crowdsecurity/dovecot-logs"][1].Evt.Parsed["message"] == "auth-worker(24058): pam(toto,1.1.1.1,<youpi>): pam_authenticate() failed: Authentication failure (password mismatch?)"
results["s01-parse"]["crowdsecurity/dovecot-logs"][1].Evt.Parsed["program"] == "dovecot"
results["s01-parse"]["crowdsecurity/dovecot-logs"][1].Evt.Parsed["timestamp"] == "Sep 8 07:16:29"
results["s01-parse"]["crowdsecurity/dovecot-logs"][1].Evt.Parsed["dovecot_remote_ip"] == "1.1.1.1"
results["s01-parse"]["crowdsecurity/dovecot-logs"][1].Evt.Parsed["dovecot_user"] == "toto"
results["s01-parse"]["crowdsecurity/dovecot-logs"][1].Evt.Meta["datasource_path"] == "dovecot-logs.log"
results["s01-parse"]["crowdsecurity/dovecot-logs"][1].Evt.Meta["datasource_type"] == "file"
results["s01-parse"]["crowdsecurity/dovecot-logs"][1].Evt.Meta["log_type"] == "dovecot_logs"
results["s01-parse"]["crowdsecurity/dovecot-logs"][1].Evt.Meta["source_ip"] == "1.1.1.1"
results["s01-parse"]["crowdsecurity/dovecot-logs"][2].Success == true
results["s01-parse"]["crowdsecurity/dovecot-logs"][2].Evt.Parsed["dovecot_login_result"] == "unknown user"
results["s01-parse"]["crowdsecurity/dovecot-logs"][2].Evt.Parsed["program"] == "dovecot"
results["s01-parse"]["crowdsecurity/dovecot-logs"][2].Evt.Parsed["dovecot_remote_ip"] == "1.1.1.1"
results["s01-parse"]["crowdsecurity/dovecot-logs"][2].Evt.Parsed["dovecot_user"] == "toto"
results["s01-parse"]["crowdsecurity/dovecot-logs"][2].Evt.Parsed["logsource"] == "syslog"
results["s01-parse"]["crowdsecurity/dovecot-logs"][2].Evt.Parsed["message"] == "auth-worker(24544): pam(toto,1.1.1.1): unknown user"
results["s01-parse"]["crowdsecurity/dovecot-logs"][2].Evt.Parsed["timestamp"] == "Sep 8 07:46:51"
results["s01-parse"]["crowdsecurity/dovecot-logs"][2].Evt.Meta["log_type"] == "dovecot_logs"
results["s01-parse"]["crowdsecurity/dovecot-logs"][2].Evt.Meta["source_ip"] == "1.1.1.1"
results["s01-parse"]["crowdsecurity/dovecot-logs"][2].Evt.Meta["datasource_path"] == "dovecot-logs.log"
results["s01-parse"]["crowdsecurity/dovecot-logs"][2].Evt.Meta["datasource_type"] == "file"
```



4. Test your newly crafted test


```bash
▶ cscli hubtest run dovecot-logs                                
INFO[27-09-2021 06:19:33 PM] Running test 'dovecot-logs'                  
INFO[27-09-2021 06:19:33 PM] parser 'crowdsecurity/syslog-logs' installed succesfully in runtime environment 
INFO[27-09-2021 06:19:33 PM] parser 'crowdsecurity/dovecot-logs' installed succesfully in runtime environment 
Test 'dovecot-logs' passed successfully (39 assertions) 🟩
```

And be amazed.



## Debug your own (parser) test

Things went wrong ? Don't panic

When working on a test, you can as well pass expressions directly to `hubtest` command and see the results :


```bash
▶ cscli hubtest  eval dovecot-logs -e 'results["s01-parse"]["crowdsecurity/dovecot-logs"][2].Evt.Parsed'             
dovecot_login_result: unknown user
dovecot_remote_ip: 1.1.1.1
dovecot_user: toto
facility: ""
logsource: syslog
message: 'auth-worker(24544): pam(toto,1.1.1.1): unknown user'
pid: ""
priority: ""
program: dovecot
timestamp: Sep 8 07:46:51
timestamp8601: ""
```

## Open your PR

yes.




