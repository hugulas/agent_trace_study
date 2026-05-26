# AI agent observability: tracing, debugging, and monitoring multi-agent systems

## Source

- Raw note: `raw/notes/a-021_AI_agent_observability_tracing_debugging.md`
- 作者: Coverge

## Compiled Summary

这篇文章的价值在于它清晰地界定了"agent 可观测性"的问题边界，避免了业界将 LLM 可观测性工具简单套用到多智能体系统的常见误区。作者用"研究-写作-审阅"三 agent 流水线的具象案例，展示了传统工具在跨 agent 归因上的结构性失明，这种叙事方式对于向技术团队传达 agent 可观测性的必要性非常有效。相比学术论文的抽象定义，这种来自产业界一线的技术指南更容易被工程团队理解和接受。

## Evidence Notes

- 从技术深度来看，OpenTelemetry 的 agent span 约定仍处于早期阶段（early 2026 仍为 experimental），但已成为事实标准（de facto standard）。这意味着当前的多智能体 tracing 互操作性本质上是"事实上的"而非"标准驱动的"，综述中关于标准化缺口的判断与此一致。文章提到的七步 instrument 清单（7-step instrumentation checklist）是一个可直接落地的实践框架，值得在后续综述的"实施建议"章节中引用。对于正在构建生产级多智能体系统的团队而言，这一 checklist 可以作为 instrumentation 的入门路线图，帮助他们在不

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/evaluation-and-benchmarking]], [[concepts/observability-products-and-market-map]], [[concepts/cost-token-and-resource-attribution]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]], [[entities/Langfuse|Langfuse]], [[entities/Arize-Phoenix|Arize Phoenix]], [[entities/Braintrust|Braintrust]], [[entities/Helicone|Helicone]], [[entities/Claude-Code|Claude Code]]
