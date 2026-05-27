# 成本可见性

## 定义

成本可见性是在账单到来之前，把 token、模型价格、工具调用、重试、缓存命中和用户/功能维度实时呈现出来，使团队能在运行期发现成本异常。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 成本异常应按什么粒度告警？
- 账单维度如何回连到 trace、用户和功能？
- 成本可见性如何转化为具体优化动作？

## 证据入口

- [AI Cost Visibility: How to Track and Optimize Token Spend Before the Invoice Arrives](summaries/s3-012-AI-Cost-Visibility-Before-the-Invoice-Ho.md) — 这篇技术文章的实践价值极高，因为它揭示了一个被学术界和工业界同时忽视的问题：agent 系统的真实运行成本与其设计时的成本预估之间存在数量级的差距。
- [LLM Agent Cost Attribution: Complete Production 2026 Guide](summaries/s3-014-LLM-Agent-Cost-Attribution-Complete-Prod.md) — 这篇指南的价值在于它将成本归因从一个财务部门的报表需求，重新定义为工程团队的基础设施责任。
- [A Guide to AI Agent Cost Optimization With Observability](summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi.md) — 这篇指南的最大价值在于它将「可观测性」从「事后排查工具」重新定位为「成本工程的基础设施」。
- [Splunk AI Agent Monitoring：企业级 AI 代理可观测性官方文档](summaries/s2-009-Introduction-to-Splunk-AI-Agent-Monitori.md) — Splunk 官方文档对 AI Agent Monitoring 的介绍虽然篇幅精炼， 但透露出的战略信息却相当丰富。
- [What Is AI Agent Observability? Why Cost Is What You're Missing](summaries/s3-015-What-Is-AI-Agent-Observability-Why-Cost.md) — 这篇文章的价值在于它把「成本」从可观测性的附属指标提升为核心信号。
- [Token Economics for LLM Agents: A Dual-View Study from Computing and Economics](summaries/s3-011-Token-Economics-for-LLM-Agents-A-Dual-Vi.md) — 在 agentic trace 分析的研究中，我们通常关注功能正确性和执行效率，但往往忽视了经济维度。
- [Monitoring - Claude Code Docs](summaries/a-007-Monitoring-Claude-Code-Docs.md) — Claude Code 的监控文档是目前公开资料中最完整、最系统化的企业级 agent 遥测实现方案。与社区驱动的实验性项目（如 Codex CLI 的 rollout trace 或各类开源 agent 框架的日志系统）不同，Anthropic 的设计体现了生产环境所需的完整性、安全性、可管理性和可扩展性。
- [OpenTelemetry for AI Agents: Implementing Observability in MCP Workflows](summaries/s3-004-OpenTelemetry-for-AI-Agents-Implementing.md) — 这篇博客的价值在于它将 OpenTelemetry 的通用可观测性框架与 MCP 这一特定协议场景进行了深度对接，提供了一套从概念到实践的完整实施路径。与许多停留在理念层面的可观测性文章不同，本文给出了具体的集成模式、采样策略配置建议和敏感数据处理方案，具有较强的工程参考价值。
- [What Is Braintrust? Is It the Best for AI Observability?](summaries/s2-018-What-Is-Braintrust-Is-It-the-Best-for-AI.md) — 这篇文章的阅读价值在于它提供了一个被投公司（Voiceflow）视角下的竞品分析样本， 兼具信息密度和立场偏差的双重特征。
- [AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices](summaries/c-018-AI-Agents-in-Production-Monitoring-Guard.md) — 这篇博客的最大价值在于其极强的可操作性。与多数学术论文聚焦评估指标与算法改进不同，本文给出了大量可直接运行或稍加修改即可部署的 Python 代码片段，从 Streamlit UI 到 FastAPI 端点，从 Langfuse CallbackHandler 到熔断器类实现，工程师可以按图索骥在数小时内搭建最小可行生产系统。这种「从零到一」的指导意义，使其在综述的工程实践章节中占据了独特位置。

## 相关词条

- [成本归因](terms/cost-attribution.md)
- [Token 经济学](terms/token-economics.md)
