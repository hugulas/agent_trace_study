# 审计轨迹

## 定义

审计轨迹是面向责任追踪、合规和事后取证的事件记录，通常要求完整性、时间顺序、身份绑定、敏感信息控制和防篡改能力。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 哪些事件必须可证明未被篡改？
- 审计记录和调试日志如何分层？
- 敏感推理与合规证据如何平衡？

## 证据入口

- [[summaries/s3-010-Tamper-Evident-Audit-Trails-for-AI-Agent|防篡改 AI Agent 审计追踪：SIEM 集成的合规要求与实践指南]] — 这篇文章的价值在于它将一个通常被视为 "合规 checkbox" 的议题提升到了安全架构的核心位置。作者没有停留在 "你需要审计追踪来满足合规" 的表面陈述，而是深入论证了审计追踪为何是唯一能够验证其他安全控制是否生效的机制。这种 "元控制" 的视角非常深刻——如果身份认证、策略执行和加密保护都在运行，但没有审计记录来证明它们确实在运行，那么从监管和治理角度而言，这些控制的存在与否并无区别。这一逻辑对于构建可信 AI 系统具有重要的方法论意义。
- [[summaries/p-008-Building-and-Evaluating-Alignment-Auditi|Building and evaluating alignment auditing agents]] — 本文构建了三种自主对齐审计智能体，在合成审计游戏和生产模型审计中验证了它们发现隐藏目标、构建行为评估和暴露问题行为的能力，同时揭示了可解释性工具和语义检索是提升审计成功率的关键手段。
- [[summaries/s3-007-What-Are-AI-Agent-Audit-Trails-Why-They|What Are AI Agent Audit Trails? Why They Matter for Compliance]] — - 这篇博客的最大价值在于提供了一份"监管者视角的需求清单"， 这对纯技术研究往往缺失。
- [[summaries/s3-008-RFC-should-AutoGen-support-tamper-eviden|RFC: should AutoGen support tamper-evident audit trails for multi-agent conversations in regulated industries?]] — 这篇 RFC 的价值不仅在于提出了 AutoGen 的合规增强方案，更在于它揭示了多智能体系统从"功能可用"走向"生产可信"时必须跨越的治理鸿沟。当前大多数可观测性方案（包括 OpenTelemetry、LangSmith、Datadog LLM Observability 等）擅长回答系统行为的"是什么"和"什么时候"，但在"是否被允许"这一策略维度上缺乏密码学级别的证明能力。日志可以告诉你某条 API 请求在 14:32 被发出，却无法证明该请求在发出前已经通过了有效的策略审查；传统数据库的写入权限可以被拥有管理员凭证的人员事后修改，而 tamper
- [[summaries/p-017-Auditing-Agent-Harness-Safety|Auditing Agent Harness Safety]] — HarnessAudit 首次将智能体安全评估的单元从最终输出转移到完整执行轨迹，提出三层审计框架和大规模真实基准，系统揭示了当前执行框架在边界合规、执行保真与扰动稳定方面的严重缺陷。
- [[summaries/c-012-Agent-Audit-Trail-A-Standard-Logging-For|Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems]] — 这份 IETF 草案的出现在时机上极具战略意义：2026 年 3 月发布，恰好赶在欧盟 AI 法案 8 月生效之前，为高风险 AI 系统的日志合规提供了急需的标准化框架。作者 Raza Sharif 来自 CyberSecAI Ltd，这一背景也解释了为何文档对 SOC 2、PCI DSS 等企业合规框架有如此细致的映射。从标准演进角度看，AAT 目前仍处于 Individual 提交的 Internet-Draft 阶段，尚未被 IETF 正式背书，这意味着其在未来六个月内可能经历大幅修订，甚至被其他草案取代。在综述中引用时需注意其"work in p
- [[summaries/a-007-Monitoring-Claude-Code-Docs|Monitoring - Claude Code Docs]] — Claude Code 的监控文档是目前公开资料中最完整、最系统化的企业级 agent 遥测实现方案。与社区驱动的实验性项目（如 Codex CLI 的 rollout trace 或各类开源 agent 框架的日志系统）不同，Anthropic 的设计体现了生产环境所需的完整性、安全性、可管理性和可扩展性。
- [[summaries/s3-009-OWASP-Top-10-for-Agentic-Applications-Co|OWASP Top 10 for Agentic Applications: Compliance Guide]] — 这篇指南的实用性在于它跳出了纯理论威胁模型的范畴，将 OWASP 的安全框架与 Arize 的可观测性产品能力进行了深度结合。
- [[summaries/p-013-Detecting-Safety-Violations-Across-Many|Detecting Safety Violations Across Many Agent Traces]] — 当前 AI 安全监控研究大多聚焦于逐轨迹的异常检测，即判断单条智能体交互记录是否包含破坏、隐藏目标或其他不安全行为。然而在实际部署中，安全违规的证据往往分散在大量轨迹之中，单看任何一条轨迹都可能是无害的。例如 Anthropic 曾发现的大规模网络间谍活动，正是通过多条看似正常的查询组合在一起才构成了完整攻击，只有事后仔细的跨轨迹监控才能揭露。
- [[summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark|AgentOps AI Infrastructure Platform Market Research Report 2034]] — 这是一份典型的付费行业研究报告，其价值不在于方法论创新，而在于提供了经过多源交叉验证的市场规模、增长率和竞争格局数据。对于构建 Agent 可观测性综述而言，这类产业报告的最大用途是弥补学术文献在"市场采纳度"和"企业真实痛点"方面的信息缺口。学术文献通常从故障检测、追踪语义、评估基准等技术角度出发，而行业报告则揭示了这些技术问题背后的商业紧迫性——当一家金融或医疗企业决定采购 AgentOps 平台时，其决策往往不是由某个追踪算法的创新驱动的，而是由合规截止日期、Token 成本失控或生产事故触发的。

## 相关词条

- [[terms/process-compliance|过程合规性]]
