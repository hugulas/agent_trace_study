# 模型路由

## 定义

模型路由根据任务难度、上下文长度、风险等级、延迟目标和预算在不同模型之间动态选择，以在质量、成本和速度之间取得可控折中。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 路由器如何判断任务是否需要昂贵模型？
- 级联推理何时比单次强模型调用更经济？
- 错误路由的质量损失如何被监控？

## 证据入口

- [Amazon Bedrock AgentCore Production Operations Guide - Observability, Cost Optimization, and Disaster Recovery](summaries/s1-007-Amazon-Bedrock-AgentCore-Production-Oper.md) — 这篇指南最突出的价值在于它的「实战导向」写作风格。
- [AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices](summaries/c-018-AI-Agents-in-Production-Monitoring-Guard.md) — 这篇博客的最大价值在于其极强的可操作性。与多数学术论文聚焦评估指标与算法改进不同，本文给出了大量可直接运行或稍加修改即可部署的 Python 代码片段，从 Streamlit UI 到 FastAPI 端点，从 Langfuse CallbackHandler 到熔断器类实现，工程师可以按图索骥在数小时内搭建最小可行生产系统。这种「从零到一」的指导意义，使其在综述的工程实践章节中占据了独特位置。
- [A Guide to AI Agent Cost Optimization With Observability](summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi.md) — 这篇指南的最大价值在于它将「可观测性」从「事后排查工具」重新定位为「成本工程的基础设施」。
- [Helicone：开源 LLM 可观测性与 AI 网关一体化平台](summaries/s2-023-Helicone-Open-source-LLM-observability-f.md) — Helicone 的产品档案让我对"AI Gateway + Observability"的融合趋势有了更清晰的认知。
- [Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models](summaries/p-027-Do-Code-Semantics-Help-A-Comprehensive-S.md) — ### 全参数微调结果 来自 LaTeX 源码 results.tex 的 Table 2 展示了三种基座模型在全参数微调后的性能： **Table 2 全参数微调性能对比（Pass@1，贪心解码）** | 基座模型 | 训练语料 | 下游微调 | 轨迹 | MBPP-R | MBPP | BigCodeBench | LiveCodeBench | CRUXEval-I | CRUXEval-O | |---------|---------|---------|------|--------|------|-------------|---------
- [Elastic LLM与Agentic AI可观测性技术文档](summaries/s2-010-LLM-and-agentic-AI-observability-Elasti.md) — Elastic的LLM可观测性文档虽然篇幅精炼，但战略意图清晰。
- [AI agent observability: tracing, debugging, and monitoring multi-agent systems](summaries/a-021-AI-agent-observability-tracing-debugging.md) — 这篇文章的价值在于它清晰地界定了"agent 可观测性"的问题边界，避免了业界将 LLM 可观测性工具简单套用到多智能体系统的常见误区。作者用"研究-写作-审阅"三 agent 流水线的具象案例，展示了传统工具在跨 agent 归因上的结构性失明，这种叙事方式对于向技术团队传达 agent 可观测性的必要性非常有效。相比学术论文的抽象定义，这种来自产业界一线的技术指南更容易被工程团队理解和接受。
- [AgentOps AI Infrastructure Platform Market Research Report 2034](summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark.md) — 这是一份典型的付费行业研究报告，其价值不在于方法论创新，而在于提供了经过多源交叉验证的市场规模、增长率和竞争格局数据。对于构建 Agent 可观测性综述而言，这类产业报告的最大用途是弥补学术文献在"市场采纳度"和"企业真实痛点"方面的信息缺口。学术文献通常从故障检测、追踪语义、评估基准等技术角度出发，而行业报告则揭示了这些技术问题背后的商业紧迫性——当一家金融或医疗企业决定采购 AgentOps 平台时，其决策往往不是由某个追踪算法的创新驱动的，而是由合规截止日期、Token 成本失控或生产事故触发的。
- [AgentSight: System-Level Observability for AI Agents Using eBPF](summaries/p-025-AgentSight-System-Level-Observability-fo.md) — ### 性能开销 来自 LaTeX 源码 eval-conclusion.tex： **Table 1.
- [Auditing Agent Harness Safety](summaries/p-017-Auditing-Agent-Harness-Safety.md) — HarnessAudit 首次将智能体安全评估的单元从最终输出转移到完整执行轨迹，提出三层审计框架和大规模真实基准，系统揭示了当前执行框架在边界合规、执行保真与扰动稳定方面的严重缺陷。

## 相关词条

- [智能体轨迹](terms/agent-trace.md)
