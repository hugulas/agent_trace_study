# Token 经济学

## 定义

Token 经济学把智能体系统中的 token 视为可计量、可归因、可预算和可优化的计算资源，关注 token 投入如何转化为任务质量、延迟、可靠性和业务价值。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- token 增加带来的质量收益是否递减？
- 多智能体性能提升是协作收益还是 token 预算扩张？
- 哪些 token 消耗属于必要推理，哪些属于浪费？

## 证据入口

- [[summaries/s3-011-Token-Economics-for-LLM-Agents-A-Dual-Vi|Token Economics for LLM Agents: A Dual-View Study from Computing and Economics]] — 在 agentic trace 分析的研究中，我们通常关注功能正确性和执行效率，但往往忽视了经济维度。
- [[summaries/s3-012-AI-Cost-Visibility-Before-the-Invoice-Ho|AI Cost Visibility: How to Track and Optimize Token Spend Before the Invoice Arrives]] — 这篇技术文章的实践价值极高，因为它揭示了一个被学术界和工业界同时忽视的问题：agent 系统的真实运行成本与其设计时的成本预估之间存在数量级的差距。
- [[summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi|A Guide to AI Agent Cost Optimization With Observability]] — 这篇指南的最大价值在于它将「可观测性」从「事后排查工具」重新定位为「成本工程的基础设施」。
- [[summaries/s3-014-LLM-Agent-Cost-Attribution-Complete-Prod|LLM Agent Cost Attribution: Complete Production 2026 Guide]] — 这篇指南的价值在于它将成本归因从一个财务部门的报表需求，重新定义为工程团队的基础设施责任。
- [[summaries/s3-015-What-Is-AI-Agent-Observability-Why-Cost|What Is AI Agent Observability? Why Cost Is What You're Missing]] — 这篇文章的价值在于它把「成本」从可观测性的附属指标提升为核心信号。
- [[summaries/s2-010-LLM-and-agentic-AI-observability-Elasti|Elastic LLM与Agentic AI可观测性技术文档]] — Elastic的LLM可观测性文档虽然篇幅精炼，但战略意图清晰。
- [[summaries/s1-010-GenAIOps-on-AWS-End-to-End-Observability|GenAIOps on AWS: 端到端可观测性栈]] — 这篇文章是少数能将 GenAI 可观测性的 "为什么" 和 "怎么做" 同时讲透的工业博客。
- [[summaries/s3-004-OpenTelemetry-for-AI-Agents-Implementing|OpenTelemetry for AI Agents: Implementing Observability in MCP Workflows]] — 这篇博客的价值在于它将 OpenTelemetry 的通用可观测性框架与 MCP 这一特定协议场景进行了深度对接，提供了一套从概念到实践的完整实施路径。与许多停留在理念层面的可观测性文章不同，本文给出了具体的集成模式、采样策略配置建议和敏感数据处理方案，具有较强的工程参考价值。
- [[summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践|Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践]] — 腾讯云这篇实践文章的价值在于其「从实践中来」的视角。
- [[summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark|AgentOps AI Infrastructure Platform Market Research Report 2034]] — 这是一份典型的付费行业研究报告，其价值不在于方法论创新，而在于提供了经过多源交叉验证的市场规模、增长率和竞争格局数据。对于构建 Agent 可观测性综述而言，这类产业报告的最大用途是弥补学术文献在"市场采纳度"和"企业真实痛点"方面的信息缺口。学术文献通常从故障检测、追踪语义、评估基准等技术角度出发，而行业报告则揭示了这些技术问题背后的商业紧迫性——当一家金融或医疗企业决定采购 AgentOps 平台时，其决策往往不是由某个追踪算法的创新驱动的，而是由合规截止日期、Token 成本失控或生产事故触发的。

## 相关词条

- [[terms/cost-attribution|成本归因]]
- [[terms/token-budget|Token 预算]]
- [[terms/context-bloat|上下文膨胀]]
- [[terms/cost-visibility|成本可见性]]
