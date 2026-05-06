# Copilot Review Instructions

Use these instructions when reviewing pull requests in this repository. They are based on the last 100 human PR review comments checked on 2026-05-05.

## Review priorities

Focus on correctness, test coverage, and Hub conventions. Prefer actionable review comments over broad style feedback.

## What to check first

- New parsers and scenarios should come with tests.
- Parser changes should usually update `.tests/.../parser.assert`.
- Scenario changes should usually update `.tests/.../scenario.assert`.
- If `.tests/.../config.yaml` sets `ignore_parsers: true`, a `parser.assert` file can be empty or omitted.
- If `.tests/.../config.yaml` does not include a scenario, a `scenario.assert` file can be omitted.
- Assert files should contain generated hubtest output only. Do not suggest comments or hand-written explanations inside assert files.
- Test logs should use private/example IPs, not WAN/public addresses.

## Parser-specific checks

- Validate that `name:` exists and matches the file/component being added.
- Watch for copy/paste mistakes in parser names, paths, labels, and metadata.
- Check that required base parsers and enrichers are present in test configs, especially `crowdsecurity/syslog-logs` and `crowdsecurity/dateparse-enrich` when relevant.
- For `s01` parsers, verify whether `apply_on: message` is required so `s00` parsers can strip syslog/docker/cri prefixes first.
- Prefer using fields prepared by `s00` parsers instead of reparsing raw input when possible.
- For JSON logs, prefer one structured unmarshal over repeated `JsonExtract` calls when it simplifies parsing and avoids repeated reflection.
- Custom grok pattern names must be namespaced to the parser or product to avoid collisions across the Hub.
- Regex feedback should be semantic, not cosmetic:
  - reject overly permissive patterns such as `%{DATA}` when the field is bounded
  - reject character classes that accidentally match the wrong things
  - ask for exact token/range matching when the log format is known
- If a parser invents a timezone for a timestamp that has none in the source log, flag it unless it follows an established Hub convention. Deployment-specific offsets are especially suspicious.

## Scenario checks

- Review threshold semantics carefully: `capacity`, `leakspeed`, `blackhole`, and similar fields are often misunderstood.
- Check that labels, classifications, and descriptions match the actual behavior and do not collapse distinct detections into the wrong bucket.

## Appsec checks

- For appsec rules, verify that rule identifiers, CVE references, source URLs, destination paths, and product names all match the file being introduced.
- For appsec rule changes, check that `.appsec-tests/` coverage was added or updated when behavior changed.
- For appsec configs, verify that referenced rule sets exist and that config fields such as `default_remediation` and `on_match` are coherent with the intended in-band or out-of-band behavior.
- For virtual patching or CVE-linked appsec rules, make sure the rule scope matches the vulnerable product and does not overmatch unrelated traffic.
- If an appsec PR changes matching logic, paranoia level, transforms, or exclusions, look for a regression test that proves the intended allow/block behavior.
- Flag appsec documentation or metadata that claims protection for products, versions, or exploit paths not supported by the actual rule logic.

## Documentation checks

- Keep `.md` files scoped to useful Hub documentation: short description, acquisition example, and behavior notes that help users operate the item.
- Ask to remove `TODO`, placeholder text, hallucinated claims, or long off-topic guidance.
- If YAML comments are really documentation, prefer moving them into the same-name `.md` file.
- Prefer consistent naming and wording with existing Hub items when the new text introduces a near-duplicate label or description.

## How to comment

- Leave comments only when you can point to a concrete bug, missing dependency, missing test, invalid convention, misleading documentation, or likely regression.
- Explain why the current change is wrong in Hub terms, not just that it differs from personal preference.
- When possible, suggest the exact fix: the missing parser, the expected `name:`, the stricter regex, the needed test regeneration, or the file that can be removed.
