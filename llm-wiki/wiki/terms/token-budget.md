# Token 预算

## 定义

Token 预算是在任务、会话、用户、团队或工作流层面对输入、输出、思考、工具返回和重试 token 设置上限、配额和告警阈值的工程机制。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 预算应该绑定到单次请求、完整任务还是用户会话？
- 超预算时应该降级模型、压缩上下文还是中止执行？
- 预算策略如何避免牺牲关键任务质量？

## 证据入口

- [Token Economics for LLM Agents: A Dual-View Study from Computing and Economics](summaries/s3-011-Token-Economics-for-LLM-Agents-A-Dual-Vi.md) — 在 agentic trace 分析的研究中，我们通常关注功能正确性和执行效率，但往往忽视了经济维度。
- [A Guide to AI Agent Cost Optimization With Observability](summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi.md) — 这篇指南的最大价值在于它将「可观测性」从「事后排查工具」重新定位为「成本工程的基础设施」。
- [LLM Agent Cost Attribution: Complete Production 2026 Guide](summaries/s3-014-LLM-Agent-Cost-Attribution-Complete-Prod.md) — 这篇指南的价值在于它将成本归因从一个财务部门的报表需求，重新定义为工程团队的基础设施责任。
- [AI Cost Visibility: How to Track and Optimize Token Spend Before the Invoice Arrives](summaries/s3-012-AI-Cost-Visibility-Before-the-Invoice-Ho.md) — 这篇技术文章的实践价值极高，因为它揭示了一个被学术界和工业界同时忽视的问题：agent 系统的真实运行成本与其设计时的成本预估之间存在数量级的差距。
- [AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices](summaries/c-018-AI-Agents-in-Production-Monitoring-Guard.md) — 这篇博客的最大价值在于其极强的可操作性。与多数学术论文聚焦评估指标与算法改进不同，本文给出了大量可直接运行或稍加修改即可部署的 Python 代码片段，从 Streamlit UI 到 FastAPI 端点，从 Langfuse CallbackHandler 到熔断器类实现，工程师可以按图索骥在数小时内搭建最小可行生产系统。这种「从零到一」的指导意义，使其在综述的工程实践章节中占据了独特位置。
- [Llama Stack 遥测可观测性指标增强提案](summaries/s1-014-Observability-Add-Additional-Metrics-to.md) — 这份 GitHub Issue 虽被标记为 "Closed as not planned"， 但其系统性的指标框架令人印象深刻， 甚至可以说是一份被低估的 "GenAI 平台可观测性指标设计指南"。
- [Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践](summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践.md) — 腾讯云这篇实践文章的价值在于其「从实践中来」的视角。
- [How we built our multi-agent research system — Anthropic Engineering Blog](summaries/a-009-How-we-built-our-multi-agent-research-sy.md) — Anthropic 这篇文章堪称多智能体系统从原型到生产的最完整工程复盘之一，其价值不仅在于架构设计，更在于对"为什么有效"和"代价是什么"的坦诚剖析。90.2% 的性能提升令人印象深刻，但"token 消耗解释 80% 方差"这一发现更具理论意义——它暗示多智能体系统的性能提升在很大程度上是"推理容量扩展"的结果，而非某种神秘的涌现智能。这对综述的方法论有重要启示：在评估多智能体系统时，必须将 token 效率与结果质量同时纳入指标，否则可能产生误导性的结论。一个消耗 15 倍 token 却只提升 10% 准确率的系统，与一个消耗 2 倍 token
- [AgentOps AI Infrastructure Platform Market Research Report 2034](summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark.md) — 这是一份典型的付费行业研究报告，其价值不在于方法论创新，而在于提供了经过多源交叉验证的市场规模、增长率和竞争格局数据。对于构建 Agent 可观测性综述而言，这类产业报告的最大用途是弥补学术文献在"市场采纳度"和"企业真实痛点"方面的信息缺口。学术文献通常从故障检测、追踪语义、评估基准等技术角度出发，而行业报告则揭示了这些技术问题背后的商业紧迫性——当一家金融或医疗企业决定采购 AgentOps 平台时，其决策往往不是由某个追踪算法的创新驱动的，而是由合规截止日期、Token 成本失控或生产事故触发的。
- [GenAIOps on AWS: 端到端可观测性栈](summaries/s1-010-GenAIOps-on-AWS-End-to-End-Observability.md) — 这篇文章是少数能将 GenAI 可观测性的 "为什么" 和 "怎么做" 同时讲透的工业博客。

## 相关词条

- [成本归因](terms/cost-attribution.md)
- [Token 经济学](terms/token-economics.md)
- [上下文膨胀](terms/context-bloat.md)
