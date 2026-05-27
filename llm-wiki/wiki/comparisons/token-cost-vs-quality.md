# Token 成本与质量收益对比

## 对比表

| 维度 | 对象 1 | 对象 2 | 对象 3 |
| --- | --- | --- | --- |
| 优化目标 | 降低总 token 花费 | 提高单位 token 产出的任务质量 | 降低失败与重试造成的浪费 |
| 主要指标 | 每请求 token、每会话成本、账单预测 | 成功率/token、质量/美元、边际收益 | 失败 trace 成本、重试次数、循环调用成本 |
| 风险 | 过度压缩导致质量下降 | 高质量样本可能掩盖成本不可扩展 | 只处理失败不处理正常路径低效 |
| 需要的 trace 字段 | prompt/completion token、模型价格、用户/功能标签 | 评测分数、任务难度、模型选择 | 失败类别、重试链、工具循环、终止原因 |
| 适用场景 | 预算治理、账单预警 | 模型和架构比较 | 生产事故复盘与系统优化 |

## 读法

这个对比页用于帮助选择分析层，而不是给工具或论文排名。若要解释单条失败轨迹，优先看诊断与归因；若要比较模型和领域，优先看过程评测；若要做生产接入，先保证结构化采集和 schema 稳定。

## 证据入口

- [Token Economics for LLM Agents: A Dual-View Study from Computing and Economics](summaries/s3-011-Token-Economics-for-LLM-Agents-A-Dual-Vi.md) — 在 agentic trace 分析的研究中，我们通常关注功能正确性和执行效率，但往往忽视了经济维度。
- [AI Cost Visibility: How to Track and Optimize Token Spend Before the Invoice Arrives](summaries/s3-012-AI-Cost-Visibility-Before-the-Invoice-Ho.md) — 这篇技术文章的实践价值极高，因为它揭示了一个被学术界和工业界同时忽视的问题：agent 系统的真实运行成本与其设计时的成本预估之间存在数量级的差距。
- [A Guide to AI Agent Cost Optimization With Observability](summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi.md) — 这篇指南的最大价值在于它将「可观测性」从「事后排查工具」重新定位为「成本工程的基础设施」。
- [LLM Agent Cost Attribution: Complete Production 2026 Guide](summaries/s3-014-LLM-Agent-Cost-Attribution-Complete-Prod.md) — 这篇指南的价值在于它将成本归因从一个财务部门的报表需求，重新定义为工程团队的基础设施责任。
- [What Is AI Agent Observability? Why Cost Is What You're Missing](summaries/s3-015-What-Is-AI-Agent-Observability-Why-Cost.md) — 这篇文章的价值在于它把「成本」从可观测性的附属指标提升为核心信号。
- [GenAIOps on AWS: 端到端可观测性栈](summaries/s1-010-GenAIOps-on-AWS-End-to-End-Observability.md) — 这篇文章是少数能将 GenAI 可观测性的 "为什么" 和 "怎么做" 同时讲透的工业博客。
- [OpenTelemetry for AI Agents: Implementing Observability in MCP Workflows](summaries/s3-004-OpenTelemetry-for-AI-Agents-Implementing.md) — 这篇博客的价值在于它将 OpenTelemetry 的通用可观测性框架与 MCP 这一特定协议场景进行了深度对接，提供了一套从概念到实践的完整实施路径。与许多停留在理念层面的可观测性文章不同，本文给出了具体的集成模式、采样策略配置建议和敏感数据处理方案，具有较强的工程参考价值。
- [Elastic LLM与Agentic AI可观测性技术文档](summaries/s2-010-LLM-and-agentic-AI-observability-Elasti.md) — Elastic的LLM可观测性文档虽然篇幅精炼，但战略意图清晰。

## 相关页面

- [智能体轨迹](terms/agent-trace.md)
- [智能体可观测性不是日志收集](viewpoints/observability-is-not-logging.md)
- [最终奖励不足以评估智能体](viewpoints/final-reward-is-insufficient.md)
