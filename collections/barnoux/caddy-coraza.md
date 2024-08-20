This collections includes a parser and scenario to parse Caddy coraza logs from [coraza-caddy](https://github.com/corazawaf/coraza-caddy) runtime error logs.

## Parser

The parser is based on the error logs format from Coraza plugin

## Scenario

The included scenarios is directly tied to using CRS (Core rule set) with Coraza WAF which is based on the inbound anomaly score that is triggered by the inbound request and can be tuned by the user from [CRS](https://coreruleset.org/docs/concepts/anomaly_scoring/#anomaly-score-thresholds) config files:

- Inbound anomaly score detection

Please note if you _dont_ use the Core Rule Set with Coraza WAF, you will need to create your own scenario and may have trouble with the current parser implementation (as this test case is based on CRS rules).
