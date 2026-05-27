# 可观测产品和开源工具对比地图

## 对比表

| 维度 | 结论 |
|---|---|
| LangSmith / Langfuse | 面向 LLM 应用开发、trace、prompt、eval 和数据集闭环 |
| Arize Phoenix / OpenInference | 强调 open instrumentation、eval 和 OpenTelemetry 语义连接 |
| Braintrust / Helicone | 强调 eval、gateway、请求记录、成本和开发工作流 |
| Datadog / Splunk / Elastic / New Relic | 把 LLM/agent telemetry 接入既有 APM 和企业运维栈 |
| AgentOps | 更明确面向 agent session、工具调用和 agent 运行监控 |

## 读法

这个对比页用于帮助选择分析层，而不是给工具或论文排名。若要解释单条失败轨迹，优先看诊断与归因；若要比较模型和领域，优先看过程评测；若要做生产接入，先保证结构化采集和 schema 稳定。

## 证据入口

- [Elastic LLM与Agentic AI可观测性技术文档](summaries/s2-010-LLM-and-agentic-AI-observability-Elasti.md) — Elastic的LLM可观测性文档虽然篇幅精炼，但战略意图清晰。
- [Arize-ai/phoenix: AI Observability & Evaluation](summaries/s2-016-Arize-aiphoenix-GitHub.md) — Phoenix 给我最深刻的印象是它的「整合性」设计哲学。
- [Elastic Brings Observability to AI Agents with Amazon Bedrock AgentCore](summaries/s2-011-Elastic-Brings-Observability-to-AI-Agent.md) — 这则新闻稿虽然内容不可访问，但其标题本身包含了丰富的信息密度。
- [AgentOps - AI Agent Monitoring and Observability 评测深度解读](summaries/s2-020-AgentOps-AI-Agent-Monitoring-and-Obser.md) — AgentOps 的产品形态揭示了一个重要的市场信号：Agent 可观测性正在从"可选项"变为"必需品"，而竞争的关键在于谁能以最低的集成成本提供最深的 Agent 语义洞察。AgentOps 选择的轻量级 SDK 路径与 Langfuse 的开源自托管路径、Datadog 的平台整合路径形成了三种差异化的市场切入策略。对于综述而言，这三种路径的并存说明当前市场尚未收敛到单一最优解，不同规模、不同技术成熟度和不同已有基础设施投资水平的团队，会有截然不同的工具选择逻辑。初创团队可能偏好 AgentOps 的低门槛或 Langfuse 的低成本自托管，而大型
- [Langfuse: 开源 LLM 工程平台](summaries/s2-014-langfuselangfuse-GitHub.md) — Langfuse 是我观察到的开源 LLM 可观测性领域社区增长最为迅猛的项目之一。
- [What Is Braintrust? Is It the Best for AI Observability?](summaries/s2-018-What-Is-Braintrust-Is-It-the-Best-for-AI.md) — 这篇文章的阅读价值在于它提供了一个被投公司（Voiceflow）视角下的竞品分析样本， 兼具信息密度和立场偏差的双重特征。
- [Splunk 推出 AI Agent Monitoring，为企业级 Agent 应用提供全栈可观测性](summaries/s2-008-Monitor-LLM-and-agent-performance-with-A.md) — Splunk 推出 AI Agent Monitoring 是一个具有行业风向标意义的事件。作为传统可观测性领域的领军企业，Splunk 的进入意味着 Agent 监控已经从初创公司的创新探索阶段，进入了主流企业软件厂商的战略布局阶段。这对于整个赛道的成熟度和客户教育都是重大利好。回顾历史，当一个新兴市场出现足够多的独立初创公司后，传统巨头的进入往往是市场即将进入高速增长期的信号。Splunk 的决策可能基于其企业客户群中 AI 项目部署数量的显著增长，以及这些客户对统一监控平台的明确需求。
- [Arize AI Review 2026: AI Observability & LLM Evaluation](summaries/s2-017-Arize-AI-Review-2026-AI-Observability-L.md) — Arize 的产品策略展现了 LLM 可观测性领域一个非常有代表性的演进路径： 以开源核心建立开发者社区和技术影响力， 以企业级产品实现商业化变现。

## 相关页面

- [智能体轨迹](terms/agent-trace.md)
- [智能体可观测性不是日志收集](viewpoints/observability-is-not-logging.md)
- [最终奖励不足以评估智能体](viewpoints/final-reward-is-insufficient.md)
