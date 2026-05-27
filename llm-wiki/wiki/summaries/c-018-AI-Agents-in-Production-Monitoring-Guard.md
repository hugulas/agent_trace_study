# AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices

## Source

- Raw note: `raw/notes/c-018_AI_Agents_in_Production_Monitoring_Guard.md`
- Metadata: not available in note

## Compiled Summary

这篇博客的最大价值在于其极强的可操作性。与多数学术论文聚焦评估指标与算法改进不同，本文给出了大量可直接运行或稍加修改即可部署的 Python 代码片段，从 Streamlit UI
到 FastAPI 端点，从 Langfuse CallbackHandler
到熔断器类实现，工程师可以按图索骥在数小时内搭建最小可行生产系统。这种「从零到一」的指导意义，使其在综述的工程实践章节中占据了独特位置。

## Evidence Notes

- 其中关于「模型路由」的讨论启发较大。作者建议以 token 数量和关键词简单路由到不同模型（token_count < 50 走 gpt-4o-mini，包含
"analyze"/"compare"/"explain why" 走 gpt-4o），这在生产初期足够实用且实现成本极低。但在复杂场景下，关键词匹配容易误判，可能需要更精细的
classifier-based 路由策略。未来可探索基于轻量级分类器（如 DistilBERT 或更小尺寸的
encoder）的自动路由，以在延迟、成本与质量之间取得动态最优平衡。若综述涉及「自适应模型选择」或「cascading inference」，这一方向值得深入。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [Langfuse](entities/Langfuse.md), [Claude Code](entities/Claude-Code.md)
