# RFC: should AutoGen support tamper-evident audit trails for multi-agent conversations in regulated industries?

## Source

- Raw note: `raw/notes/s3-008_RFC_should_AutoGen_support_tamper-eviden.md`
- 证据质量: 中（基于社区实践反馈与跨框架趋势观察）

## Compiled Summary

这篇 RFC 的价值不仅在于提出了 AutoGen 的合规增强方案，更在于它揭示了多智能体系统从"功能可用"走向"生产可信"时必须跨越的治理鸿沟。当前大多数可观测性方案（包括 OpenTelemetry、LangSmith、Datadog LLM Observability 等）擅长回答系统行为的"是什么"和"什么时候"，但在"是否被允许"这一策略维度上缺乏密码学级别的证明能力。日志可以告诉你某条 API 请求在 14:32 被发出，却无法证明该请求在发出前已经通过了有效的策略审查；传统数据库的写入权限可以被拥有管理员凭证的人员事后修改，而 tamper-evident 的哈希链结构则从数学上排除了这种可能性。

## Evidence Notes

- 提案中的 behavioral covenant 概念非常贴近操作系统中的 capability-based security 和网络安全中的零信任架构（Zero Trust）思想，将其迁移到智能体编排层是一个自然的延伸。每个智能体不再被默认信任，而是携带一份明确的权限清单，所有越界请求在执行前即被拦截。这种"最小权限 + 默认拒绝"的原则，对于由大语言模型驱动的自主智能体尤为重要，因为 LLM 的不可预测性意味着即使 prompt 工程再完善，也无法 100% 保证智能体不会生成危险的操作指令。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: [OpenInference](entities/OpenInference.md), [AgentTrace](entities/AgentTrace.md)
