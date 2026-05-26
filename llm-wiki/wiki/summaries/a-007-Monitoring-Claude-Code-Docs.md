# Monitoring - Claude Code Docs

## Source

- Raw note: `raw/notes/a-007_Monitoring__Claude_Code_Docs.md`
- 作者: Anthropic（Claude Code 官方文档）
- 来源: Claude Code 官方文档
- 证据质量: high
- PDF: [a-007]-monitoring--claude-code-docs.pdf

## Compiled Summary

Claude Code 的监控文档是目前公开资料中最完整、最系统化的企业级 agent 遥测实现方案。与社区驱动的实验性项目（如 Codex CLI 的 rollout trace 或各类开源 agent 框架的日志系统）不同，Anthropic 的设计体现了生产环境所需的完整性、安全性、可管理性和可扩展性。

## Evidence Notes

- 几个特别值得深入分析的设计选择：
第一，内容控制的四级开关（user prompts → tool details → tool content → raw API bodies）体现了“渐进式透明度”（progressive transparency）的隐私设计理念。这种分层设计让组织可以根据合规要求（GDPR、HIPAA、SOX 等）灵活配置，而不是简单的全有或全无。更精妙的是，文档明确指出了各层之间的依赖关系和 consent 隐含关系——启用 raw API bodies 意味着同意泄露其他所有内容，因为这些请求体包含完整的对话历史。这种 explicit consent modeling 在企业软件中并不常见，但在 age

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/audit-trails-security-and-governance]], [[concepts/production-operations-and-cloud-platforms]], [[concepts/cost-token-and-resource-attribution]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]], [[entities/Claude-Code|Claude Code]]
