# 成本归因

## 定义

成本归因把 token、模型调用、工具调用、重试、缓存、失败和多智能体依赖链连接起来，使团队能把费用分摊到任务、用户、功能或失败模式。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 成本应该按请求、任务、工具链还是智能体分摊？
- 失败重试和长上下文膨胀如何暴露？
- 成本信号如何与 trace join？

## 证据入口

- [AI Cost Visibility: How to Track and Optimize Token Spend Before the Invoice Arrives](summaries/s3-012-AI-Cost-Visibility-Before-the-Invoice-Ho.md) — 这篇技术文章的实践价值极高，因为它揭示了一个被学术界和工业界同时忽视的问题：agent 系统的真实运行成本与其设计时的成本预估之间存在数量级的差距。
- [Token Economics for LLM Agents: A Dual-View Study from Computing and Economics](summaries/s3-011-Token-Economics-for-LLM-Agents-A-Dual-Vi.md) — 在 agentic trace 分析的研究中，我们通常关注功能正确性和执行效率，但往往忽视了经济维度。
- [A Guide to AI Agent Cost Optimization With Observability](summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi.md) — 这篇指南的最大价值在于它将「可观测性」从「事后排查工具」重新定位为「成本工程的基础设施」。
- [LLM Agent Cost Attribution: Complete Production 2026 Guide](summaries/s3-014-LLM-Agent-Cost-Attribution-Complete-Prod.md) — 这篇指南的价值在于它将成本归因从一个财务部门的报表需求，重新定义为工程团队的基础设施责任。
- [What Is AI Agent Observability? Why Cost Is What You're Missing](summaries/s3-015-What-Is-AI-Agent-Observability-Why-Cost.md) — 这篇文章的价值在于它把「成本」从可观测性的附属指标提升为核心信号。
- [GenAIOps on AWS: 端到端可观测性栈](summaries/s1-010-GenAIOps-on-AWS-End-to-End-Observability.md) — 这篇文章是少数能将 GenAI 可观测性的 "为什么" 和 "怎么做" 同时讲透的工业博客。
- [OpenTelemetry for AI Agents: Implementing Observability in MCP Workflows](summaries/s3-004-OpenTelemetry-for-AI-Agents-Implementing.md) — 这篇博客的价值在于它将 OpenTelemetry 的通用可观测性框架与 MCP 这一特定协议场景进行了深度对接，提供了一套从概念到实践的完整实施路径。与许多停留在理念层面的可观测性文章不同，本文给出了具体的集成模式、采样策略配置建议和敏感数据处理方案，具有较强的工程参考价值。
- [Elastic LLM与Agentic AI可观测性技术文档](summaries/s2-010-LLM-and-agentic-AI-observability-Elasti.md) — Elastic的LLM可观测性文档虽然篇幅精炼，但战略意图清晰。
- [AgentOps AI Infrastructure Platform Market Research Report 2034](summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark.md) — 这是一份典型的付费行业研究报告，其价值不在于方法论创新，而在于提供了经过多源交叉验证的市场规模、增长率和竞争格局数据。对于构建 Agent 可观测性综述而言，这类产业报告的最大用途是弥补学术文献在"市场采纳度"和"企业真实痛点"方面的信息缺口。学术文献通常从故障检测、追踪语义、评估基准等技术角度出发，而行业报告则揭示了这些技术问题背后的商业紧迫性——当一家金融或医疗企业决定采购 AgentOps 平台时，其决策往往不是由某个追踪算法的创新驱动的，而是由合规截止日期、Token 成本失控或生产事故触发的。
- [AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices](summaries/c-018-AI-Agents-in-Production-Monitoring-Guard.md) — 这篇博客的最大价值在于其极强的可操作性。与多数学术论文聚焦评估指标与算法改进不同，本文给出了大量可直接运行或稍加修改即可部署的 Python 代码片段，从 Streamlit UI 到 FastAPI 端点，从 Langfuse CallbackHandler 到熔断器类实现，工程师可以按图索骥在数小时内搭建最小可行生产系统。这种「从零到一」的指导意义，使其在综述的工程实践章节中占据了独特位置。

## 相关词条

- [Token 经济学](terms/token-economics.md)
- [Token 预算](terms/token-budget.md)
- [上下文膨胀](terms/context-bloat.md)
- [成本可见性](terms/cost-visibility.md)
