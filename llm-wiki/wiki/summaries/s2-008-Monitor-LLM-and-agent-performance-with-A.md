# Splunk 推出 AI Agent Monitoring，为企业级 Agent 应用提供全栈可观测性

## Source

- Raw note: `raw/notes/s2-008_Monitor_LLM_and_agent_performance_with_A.md`
- 作者: Splunk 官方博客
- 证据质量: medium（基于官方产品发布声明，包含具体功能描述和技术架构信息）

## Compiled Summary

Splunk 推出 AI Agent Monitoring 是一个具有行业风向标意义的事件。作为传统可观测性领域的领军企业，Splunk 的进入意味着 Agent 监控已经从初创公司的创新探索阶段，进入了主流企业软件厂商的战略布局阶段。这对于整个赛道的成熟度和客户教育都是重大利好。回顾历史，当一个新兴市场出现足够多的独立初创公司后，传统巨头的进入往往是市场即将进入高速增长期的信号。Splunk 的决策可能基于其企业客户群中 AI 项目部署数量的显著增长，以及这些客户对统一监控平台的明确需求。

## Evidence Notes

- 从技术架构角度，Splunk 选择基于 OpenTelemetry 构建是一个明智的决定。OpenTelemetry 已经成为云原生可观测性的事实标准，而 Cisco AGNTCY 则为 Agent 特有的遥测数据（如 Agent 意图、工具调用计划、记忆状态）提供了语义规范。这种双标准策略既保证了与现有基础设施的兼容性，又为 Agent 特有的监控需求预留了扩展空间。值得注意的是，AGNTCY 标准由 Cisco 主导，而 Cisco 于 2023 年收购了 Splunk，因此 Splunk 对 AGNTCY 的采用也可能带有推动 Cisco 自有标准成为行业规范的意图。这种标准之争可能会影响未来 Agent 生态的互操作性格局，

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/audit-trails-security-and-governance]], [[concepts/production-operations-and-cloud-platforms]], [[concepts/observability-products-and-market-map]], [[concepts/cost-token-and-resource-attribution]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]], [[entities/Braintrust|Braintrust]]
