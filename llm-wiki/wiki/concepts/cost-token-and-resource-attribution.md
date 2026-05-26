# Cost, Token, and Resource Attribution

## Working Definition

Treats cost visibility as part of observability: token economics, invoice prediction, resource attribution, and optimization. In this wiki, the concept is compiled from local source notes rather than general background knowledge.

## Why It Matters

Agentic systems make decisions through multi-step trajectories: prompts, model calls, tool calls, memory updates, environment observations, planner decisions, and post-hoc evaluations. Ordinary request logging is too flat for that behavior. The notes linked here treat observability as a way to recover the trajectory, explain failures, assign responsibility, and create evidence that can be reviewed after deployment.

## Synthesis

- The corpus repeatedly separates **runtime telemetry** from **evaluation evidence**. Telemetry captures what happened; evaluation and audit layers decide whether the behavior was acceptable.
- Trace quality depends on schema discipline. Useful pages in this cluster tend to name the event surface, span or step boundary, metadata context, and downstream debugging question.
- Production material emphasizes integration cost, platform coverage, dashboards, and alerting. Academic material emphasizes failure taxonomies, attribution, monitorability, and formal structure.
- A recurring gap is that many product pages promise agent observability without exposing enough schema detail to compare cognitive, operational, and contextual traces.

## Source Notes

- [[summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi|A Guide to AI Agent Cost Optimization With Observability]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-019-AI-Agent-Vulnerabilities-Understanding-S|AI Agent Vulnerabilities: Understanding and Mitigating Emerging Security Risks]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-018-AI-Agents-in-Production-Monitoring-Guard|AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/a-021-AI-agent-observability-tracing-debugging|AI agent observability: tracing, debugging, and monitoring multi-agent systems]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-012-Agent-Audit-Trail-A-Standard-Logging-For|Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark|AgentOps AI Infrastructure Platform Market Research Report 2034]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories|AgentRx: Diagnosing AI Agent Failures from Execution Trajectories]] (n.d., evidence: unknown) — 论文报告了失败归因准确率，并把评估拆成智能体级定位和步骤级定位。证据包中显示，AgentRx 在 tau-bench 和 Magentic-One 轨迹上都优于既有失败归因基线。尤其在步骤定位上，论文关注平均值和标准差，并进一步分析容忍窗口下的准确率，说明严格单步命中和邻近步骤命中都被纳入讨论。
- [[summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践|Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-011-Agentic-Harness-Engineering-Observabilit|Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses]] (n.d., evidence: unknown) — ### RQ1：主结果
在 Terminal-Bench 2 上运行十轮 AHE 迭代（从仅含命令行的 NexAU$_0$ 种子出发，耗时约 32 小时），最佳配置记为 AHE。
- [[summaries/s2-012-Beyond-the-Black-Box-Next-Gen-AI-Agent-M|Beyond the Black Box: Next-Gen AI Agent Monitoring]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-027-Do-Code-Semantics-Help-A-Comprehensive-S|Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models]] (2025, evidence: unknown) — ### 全参数微调结果
来自 LaTeX 源码 `results.tex` 的 Table 2 展示了三种基座模型在全参数微调后的性能：
**Table 2 全参数微调性能对比（Pass@1，贪心解码）**
| 基座模型 | 训练语料 | 下游微调 | 轨迹 | MBPP-R | MBPP | BigCodeBench | LiveCodeBench | CRUXEval-I | CRUXEval-O |
|---------|---------|---------|------|--------|------|-
- [[summaries/p-003-DoVer-Intervention-Driven-Auto-Debugging|DoVer: Intervention-Driven Auto Debugging for LLM Multi-Agent Systems]] (2025, evidence: unknown) — ### 故障翻转实验结果
来自 LaTeX 源码 `ada_arXiv_v2.tex` 中 Table 2 的数据：
| 数据集 | 干预试炼数 | 试炼成功率 | 进展增益 |
|--------|-----------|-----------|---------|
| WW-AB | 72 | 17.6% | +0% |
| WW-GAIA | 99 | 17.6% | +8.8% |
| GAIA-Level-1 | 63 | 27.5% | +15.7% |
| GSMPlus | 198 | 49.0% 
- [[summaries/s2-010-LLM-and-agentic-AI-observability-Elasti|Elastic LLM与Agentic AI可观测性技术文档]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-017-Essential-Framework-for-AI-Agent-Guardra|Essential Framework for AI Agent Guardrails]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s1-004-Google-ADK-vs-AWS-AgentCore-Enterprise-F|Google ADK vs AWS AgentCore: Enterprise Framework Selection Guide]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s1-002-Google-boosts-Vertex-AI-Agent-Builder-wi|Google boosts Vertex AI Agent Builder with new observability and deployment tools]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-022-Helicone-LLM-Observability-Platform-Lea|Helicone LLM 可观测性平台深度评测：一键集成与智能成本优化]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-023-Helicone-Open-source-LLM-observability-f|Helicone：开源 LLM 可观测性与 AI 网关一体化平台]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- Plus 60 additional linked summaries in [[wiki/index|Index]].

## Related Concepts

- [[concepts/failure-diagnosis-and-attribution]]
