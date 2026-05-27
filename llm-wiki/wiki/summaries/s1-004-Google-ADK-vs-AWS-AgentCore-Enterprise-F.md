# Google ADK vs AWS AgentCore: Enterprise Framework Selection Guide

## Source

- Raw note: `raw/notes/s1-004_Google_ADK_vs_AWS_AgentCore_Enterprise_F.md`
- 作者: 未标注（cognilium.ai 平台发布）

## Compiled Summary

首先需要诚实记录：该来源的原始网页在资料抓取阶段已无法访问，本地存档的 PDF 仅包含浏览器错误页面（ERR_CONNECTION_CLOSED），web-archive 目录亦无有效内容。这意味着本笔记的内容摘要部分并非直接来自原文阅读，而是基于该来源的标题、存档信息、综述报告对该来源的多处引用，以及同一主题相关来源（s1-001、s1-002、s1-003、s1-009）的交叉推断整理而成。这种"间接阅读"方式在文献综述工作中不可避免，但需要在笔记中明确标注，以避免将推断性内容误作原文表述。同时，这也提醒我们：对于第三方博客、独立分析站点等非持久化来源，应在抓取时完成全文提取与本地存档，而非仅依赖后续按需访问。

## Evidence Notes

- 从内容价值角度，该来源的核心贡献在于提供了一个结构化的中立对比框架。在智能体框架选型这一高度分散且快速演进的市场中，大多数技术文档都来自厂商自身（如 Google 官方 ADK 文档、AWS AgentCore 白皮书、厂商技术博客），不可避免地带有生态推广色彩。第三方平台的对比分析能够帮助决策者跳出单一厂商视角，从可观测性架构、供应商锁定、多云适配、长期总拥有成本（TCO）等维度进行结构性评估。尽管原始内容无法获取，但从综述的引用密度和引用深度来看，该来源在 ADK 与 AgentCore 的对比分析中提供了其他来源未能充分覆盖的独到见解，尤其是对"专有日志格式导致多云转换成本"这一隐性成本的揭示。许多企业在评估框架时只关注功能清

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md), [AWS AgentCore](entities/AWS-AgentCore.md), [Google ADK and Vertex AI](entities/Google-ADK-and-Vertex-AI.md), [Claude Code](entities/Claude-Code.md)
