# Multi-Agent Portfolio Collaboration with OpenAI Agents SDK

## Source

- Raw note: `raw/notes/a-020_Multi-Agent_Portfolio_Collaboration_with.md`
- 作者: OpenAI Developers / OpenAI Cookbook Team
- 来源: OpenAI Cookbook 官方示例教程
- 证据质量: high
- PDF: [a-020]-multi-agent-portfolio-collaboration-with-openai-agents-sdk.pdf

## Compiled Summary

这是目前最为完整、可直接复现的工业级多智能体协作示例之一。其最大价值在于展示了"agents as a tool"不仅是一种设计模式，更是一种可观测性和可调试性的架构选择——当每个专家智能体都被封装为显式工具时，失败定位、性能归因和结果审计都变得更加直接和系统化。从可观测性研究的角度看，这是一个重要的架构级发现：observability 不应只是事后附加的监控层，而应该在架构设计阶段就被纳入考量。

## Evidence Notes

- 从可观测性技术角度看，本示例对综述的一个重要启示是：tracing 必须覆盖三个层级——orchestration 层（PM 的决策过程、任务分解逻辑）、tool 层（每次工具调用的输入输出、延迟和错误）和 model 层（每次 LLM 调用的推理轨迹、token 消耗和输出质量）。OpenAI Agents SDK 的 `trace()` 机制恰好提供了这种分层能力，但如何将其与外部可观测性平台（如基于 OpenTelemetry 的生态系统、Langfuse、Phoenix 等）进行标准化对接，仍是一个亟待解决的开放工程问题。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/audit-trails-security-and-governance]], [[concepts/production-operations-and-cloud-platforms]], [[concepts/observability-products-and-market-map]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: None identified
