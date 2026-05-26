# 成本是可观测性信号

## 观点

token 和调用成本不是财务尾项，而是反映长上下文、重试、工具循环、失败恢复和多智能体协作效率的运行信号。

## 为什么成立

- [[summaries/s3-012-AI-Cost-Visibility-Before-the-Invoice-Ho|AI Cost Visibility: How to Track and Optimize Token Spend Before the Invoice Arrives]] — 这篇技术文章的实践价值极高，因为它揭示了一个被学术界和工业界同时忽视的问题：agent 系统的真实运行成本与其设计时的成本预估之间存在数量级的差距。
- [[summaries/s3-011-Token-Economics-for-LLM-Agents-A-Dual-Vi|Token Economics for LLM Agents: A Dual-View Study from Computing and Economics]] — 在 agentic trace 分析的研究中，我们通常关注功能正确性和执行效率，但往往忽视了经济维度。
- [[summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi|A Guide to AI Agent Cost Optimization With Observability]] — 这篇指南的最大价值在于它将「可观测性」从「事后排查工具」重新定位为「成本工程的基础设施」。
- [[summaries/s3-014-LLM-Agent-Cost-Attribution-Complete-Prod|LLM Agent Cost Attribution: Complete Production 2026 Guide]] — 这篇指南的价值在于它将成本归因从一个财务部门的报表需求，重新定义为工程团队的基础设施责任。
- [[summaries/s3-015-What-Is-AI-Agent-Observability-Why-Cost|What Is AI Agent Observability? Why Cost Is What You're Missing]] — 这篇文章的价值在于它把「成本」从可观测性的附属指标提升为核心信号。
- [[summaries/s1-010-GenAIOps-on-AWS-End-to-End-Observability|GenAIOps on AWS: 端到端可观测性栈]] — 这篇文章是少数能将 GenAI 可观测性的 "为什么" 和 "怎么做" 同时讲透的工业博客。
- [[summaries/s3-004-OpenTelemetry-for-AI-Agents-Implementing|OpenTelemetry for AI Agents: Implementing Observability in MCP Workflows]] — 这篇博客的价值在于它将 OpenTelemetry 的通用可观测性框架与 MCP 这一特定协议场景进行了深度对接，提供了一套从概念到实践的完整实施路径。与许多停留在理念层面的可观测性文章不同，本文给出了具体的集成模式、采样策略配置建议和敏感数据处理方案，具有较强的工程参考价值。
- [[summaries/s1-007-Amazon-Bedrock-AgentCore-Production-Oper|Amazon Bedrock AgentCore Production Operations Guide - Observability, Cost Optimization, and Disaster Recovery]] — 这篇指南最突出的价值在于它的「实战导向」写作风格。
- [[summaries/s2-010-LLM-and-agentic-AI-observability-Elasti|Elastic LLM与Agentic AI可观测性技术文档]] — Elastic的LLM可观测性文档虽然篇幅精炼，但战略意图清晰。

## 工程含义

- 成本 dashboard 必须能 drill down 到 trace。
- 失败样本应同时看质量损失和资源浪费。
- 优化策略需要区分模型成本、工具成本和重试成本。

## 反例与边界

这个观点不是说相邻层不重要，而是说单独依赖该层会留下诊断或治理缺口。 对于低风险 demo，轻量日志可能足够；对于生产智能体、长程任务、多智能体协作或合规场景，必须把 trace、评测、审计和成本信号组织成可追溯证据。

## 相关词条

- [[terms/agent-trace|智能体轨迹]]
- [[terms/failure-attribution|失败归因]]
- [[terms/trace-schema|轨迹 Schema]]
