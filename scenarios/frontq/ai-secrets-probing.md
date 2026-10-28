# AI secrets probing

Detects scanners looking for the configuration and key files of AI coding assistants and AI providers, which no website serves:

- AI assistant folders and files: `/.claude/`, `/.cursor/`, `/.codex/`, `/.gemini/`, `/.aider*`
- MCP and desktop client config: `/.mcp.json`, `/claude_desktop_config.json`
- Cloudflare Workers local secrets: `/.dev.vars`
- AI provider key files such as `/openai-api-key.json`, `/anthropic_credentials.yaml`, `/aws-bedrock-api-key.txt`

A single request is enough: these paths only exist on a developer's machine, so any client asking a web server for them is hunting for leaked AI keys.

We have seen these requests since autumn 2026 from cloud-hosted scanners that also probe for `.env` and `.git`. Like `crowdsecurity/http-sensitive-files`, the scenario only looks at the request path, so it applies to any web stack.
