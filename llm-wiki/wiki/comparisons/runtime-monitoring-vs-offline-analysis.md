# 运行时监控与离线分析对比

## 对比表

| 维度 | 对象 1 | 对象 2 |
| --- | --- | --- |
| 目标 | 及时发现异常、告警、限流或阻断 | 解释失败、比较模型、生成证据和改进系统 |
| 延迟要求 | 低延迟、低开销、可在线执行 | 可接受批处理和较高 judge 成本 |
| 数据粒度 | 核心 span、指标、错误和抽样日志 | 完整轨迹、原始上下文、人工/自动标注和实验结果 |
| 常见方法 | OpenTelemetry、eBPF、SDK 插桩、产品 dashboard | AgentRx、AgentPex、AHE、benchmark 分析 |
| 设计取舍 | 实时性优先，解释可能较浅 | 解释性优先，成本和隐私压力更高 |

## 读法

这个对比页用于帮助选择分析层，而不是给工具或论文排名。若要解释单条失败轨迹，优先看诊断与归因；若要比较模型和领域，优先看过程评测；若要做生产接入，先保证结构化采集和 schema 稳定。

## 证据入口

- [Monitoring Monitorability](summaries/p-006-Monitoring-Monitorability.md) — 本文系统定义了思维链可监控性的评估框架与指标，通过大规模实验发现思维链长度与可监控性正相关，并揭示了模型能力、监控能力与可监控性之间的扩展权衡关系。
- [Auditing Agent Harness Safety](summaries/p-017-Auditing-Agent-Harness-Safety.md) — HarnessAudit 首次将智能体安全评估的单元从最终输出转移到完整执行轨迹，提出三层审计框架和大规模真实基准，系统揭示了当前执行框架在边界合规、执行保真与扰动稳定方面的严重缺陷。
- [Splunk 推出 AI Agent Monitoring，为企业级 Agent 应用提供全栈可观测性](summaries/s2-008-Monitor-LLM-and-agent-performance-with-A.md) — Splunk 推出 AI Agent Monitoring 是一个具有行业风向标意义的事件。作为传统可观测性领域的领军企业，Splunk 的进入意味着 Agent 监控已经从初创公司的创新探索阶段，进入了主流企业软件厂商的战略布局阶段。这对于整个赛道的成熟度和客户教育都是重大利好。回顾历史，当一个新兴市场出现足够多的独立初创公司后，传统巨头的进入往往是市场即将进入高速增长期的信号。Splunk 的决策可能基于其企业客户群中 AI 项目部署数量的显著增长，以及这些客户对统一监控平台的明确需求。
- [GitHub - Arize-ai/openinference: OpenTelemetry Instrumentation for AI Observability](summaries/c-004-OpenInference-OpenTelemetry-Instrumentat.md) — OpenInference 的价值不仅在于提供了多少 instrumentation 包，更在于它成功地将 AI 领域的大量专有概念（如 retrieval、tool call、prompt template）映射到了 OpenTelemetry 的通用追踪模型上。
- [Introduction to AI monitoring - New Relic Documentation](summaries/s2-013-Introduction-to-AI-monitoring-New-Relic.md) — 作为官方产品文档， 本文的信息密度和可信度较高， 但深度上自然受限于入门指南的定位—— 它告诉你 "有什么" 和 "怎么用"， 但不会深入讨论 "为什么这样设计" 或 "与其他方案相比优劣如何"。
- [Amazon Bedrock AgentCore Runtime - Part 3 AgentCore Runtime Observability](summaries/s1-008-Part-3-AgentCore-Runtime-Observability.md) — 这篇教程的价值在于它提供了一个从"零配置"到"全链路可观测"的完整闭环实践。与大多数停留在概念层面的文档不同，作者每一步都配有控制台截图与具体配置参数，这使得该文章具有极高的复现价值。从工程实践角度，我认为以下几点值得在综述中深入展开： 第一，ADOT 自动埋点与 Starter Toolkit 的协同设计体现了 AWS 在开发者体验上的深度思考。传统上，为 Python Agent 应用添加 OpenTelemetry 埋点需要开发者手动修改依赖、配置 exporter、初始化 tracer provider，步骤繁琐且容易出错。而 AgentCore
- [Getting Started with AI Agent Observability using Vertex AI Agent Engine and Cloud Trace](summaries/s1-005-Getting-Started-with-AI-Agent-Observabil.md) — 该实验的价值不仅在于教授了 Vertex AI Agent Engine 的可观测性工具操作，更在于它展示了一种"教育即实践"的设计理念——学习者在真实环境中操作真实的 Agent，每一步都有即时反馈。从工程与综述写作角度，我认为以下几点值得深入展开： 第一，Google Cloud 三套工具（Logs Explorer、Cloud Trace、Cloud Monitoring）的原生集成度是其差异化优势。与 AWS 需要额外配置 ADOT SDK 才能将 trace 送入 CloudWatch 不同，Vertex AI Agent Engine 作为托
- [Splunk AI Agent Monitoring：企业级 AI 代理可观测性官方文档](summaries/s2-009-Introduction-to-Splunk-AI-Agent-Monitori.md) — Splunk 官方文档对 AI Agent Monitoring 的介绍虽然篇幅精炼， 但透露出的战略信息却相当丰富。

## 相关页面

- [智能体轨迹](terms/agent-trace.md)
- [智能体可观测性不是日志收集](viewpoints/observability-is-not-logging.md)
- [最终奖励不足以评估智能体](viewpoints/final-reward-is-insufficient.md)
