# 过程合规性

## 定义

过程合规性评估智能体是否按系统提示、工具 schema、业务规则和安全策略行动，而不只看最终答案或最终状态是否正确。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 最终成功是否掩盖了违规过程？
- 提示词和工具定义能否被抽取成可检查规范？
- judge 评分与最终奖励如何互补？

## 证据入口

- [Willful Disobedience: Automatically Detecting Failures in Agentic Traces](summaries/p-004-Willful-Disobedience-Automatically-Detecting-Failures-in-Agentic-Traces.md) — AgentPex 是一个从提示和工具规范中抽取行为规则、再自动检查智能体轨迹是否违反这些规则的过程性评测工具。
- [Willful Disobedience: Automatically Detecting Failures in Agentic Traces](summaries/AgentPex-Willful-Disobedience.md) — AgentPex 通过从提示自动提取行为规范并以大语言模型作为裁判逐条评估轨迹合规性，弥补了仅结果评估无法发现的过程性失败，在四百二十四条 tau-squared-bench 轨迹上揭示了模型特有的故意不服从模式。
- [OpenInference Specification - openinference](summaries/c-014-OpenInference-Specification.md) — OpenInference 规范的最大价值在于它提供了一个"AI 原生"的追踪语义层，而不是让 AI 应用去适配传统 HTTP 服务的追踪模型。在 HTTP 服务中，一次 span 只需要 method、status_code、path 等属性就足够理解；但在 LLM 应用中，同样的"一次调用"背后是多轮对话历史、系统提示词、工具定义、温度参数、token 消耗、模型版本等数十个维度的信息。如果这些信息散落在不同的日志格式中，不仅无法聚合分析，更无法在不同框架之间进行横向比较。
- [防篡改 AI Agent 审计追踪：SIEM 集成的合规要求与实践指南](summaries/s3-010-Tamper-Evident-Audit-Trails-for-AI-Agent.md) — 这篇文章的价值在于它将一个通常被视为 "合规 checkbox" 的议题提升到了安全架构的核心位置。作者没有停留在 "你需要审计追踪来满足合规" 的表面陈述，而是深入论证了审计追踪为何是唯一能够验证其他安全控制是否生效的机制。这种 "元控制" 的视角非常深刻——如果身份认证、策略执行和加密保护都在运行，但没有审计记录来证明它们确实在运行，那么从监管和治理角度而言，这些控制的存在与否并无区别。这一逻辑对于构建可信 AI 系统具有重要的方法论意义。
- [What Are AI Agent Audit Trails? Why They Matter for Compliance](summaries/s3-007-What-Are-AI-Agent-Audit-Trails-Why-They.md) — - 这篇博客的最大价值在于提供了一份"监管者视角的需求清单"， 这对纯技术研究往往缺失。
- [RFC: should AutoGen support tamper-evident audit trails for multi-agent conversations in regulated industries?](summaries/s3-008-RFC-should-AutoGen-support-tamper-eviden.md) — 这篇 RFC 的价值不仅在于提出了 AutoGen 的合规增强方案，更在于它揭示了多智能体系统从"功能可用"走向"生产可信"时必须跨越的治理鸿沟。当前大多数可观测性方案（包括 OpenTelemetry、LangSmith、Datadog LLM Observability 等）擅长回答系统行为的"是什么"和"什么时候"，但在"是否被允许"这一策略维度上缺乏密码学级别的证明能力。日志可以告诉你某条 API 请求在 14:32 被发出，却无法证明该请求在发出前已经通过了有效的策略审查；传统数据库的写入权限可以被拥有管理员凭证的人员事后修改，而 tamper
- [AgentOps AI Infrastructure Platform Market Research Report 2034](summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark.md) — 这是一份典型的付费行业研究报告，其价值不在于方法论创新，而在于提供了经过多源交叉验证的市场规模、增长率和竞争格局数据。对于构建 Agent 可观测性综述而言，这类产业报告的最大用途是弥补学术文献在"市场采纳度"和"企业真实痛点"方面的信息缺口。学术文献通常从故障检测、追踪语义、评估基准等技术角度出发，而行业报告则揭示了这些技术问题背后的商业紧迫性——当一家金融或医疗企业决定采购 AgentOps 平台时，其决策往往不是由某个追踪算法的创新驱动的，而是由合规截止日期、Token 成本失控或生产事故触发的。
- [Auditing Agent Harness Safety](summaries/p-017-Auditing-Agent-Harness-Safety.md) — HarnessAudit 首次将智能体安全评估的单元从最终输出转移到完整执行轨迹，提出三层审计框架和大规模真实基准，系统揭示了当前执行框架在边界合规、执行保真与扰动稳定方面的严重缺陷。
- [OpenTelemetry for AI Agents: Implementing Observability in MCP Workflows](summaries/s3-004-OpenTelemetry-for-AI-Agents-Implementing.md) — 这篇博客的价值在于它将 OpenTelemetry 的通用可观测性框架与 MCP 这一特定协议场景进行了深度对接，提供了一套从概念到实践的完整实施路径。与许多停留在理念层面的可观测性文章不同，本文给出了具体的集成模式、采样策略配置建议和敏感数据处理方案，具有较强的工程参考价值。
- [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](summaries/c-012-Agent-Audit-Trail-A-Standard-Logging-For.md) — 这份 IETF 草案的出现在时机上极具战略意义：2026 年 3 月发布，恰好赶在欧盟 AI 法案 8 月生效之前，为高风险 AI 系统的日志合规提供了急需的标准化框架。作者 Raza Sharif 来自 CyberSecAI Ltd，这一背景也解释了为何文档对 SOC 2、PCI DSS 等企业合规框架有如此细致的映射。从标准演进角度看，AAT 目前仍处于 Individual 提交的 Internet-Draft 阶段，尚未被 IETF 正式背书，这意味着其在未来六个月内可能经历大幅修订，甚至被其他草案取代。在综述中引用时需注意其"work in p

## 相关词条

- [审计轨迹](terms/audit-trail.md)
