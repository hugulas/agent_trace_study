# 最终奖励不足以评估智能体

## 观点

最终成功率会掩盖过程违规、错误工具使用和偶然成功；轨迹级过程评测应与结果评测并列。

## 为什么成立

- [Willful Disobedience: Automatically Detecting Failures in Agentic Traces](summaries/p-004-Willful-Disobedience-Automatically-Detecting-Failures-in-Agentic-Traces.md) — AgentPex 是一个从提示和工具规范中抽取行为规则、再自动检查智能体轨迹是否违反这些规则的过程性评测工具。
- [Willful Disobedience: Automatically Detecting Failures in Agentic Traces](summaries/AgentPex-Willful-Disobedience.md) — AgentPex 通过从提示自动提取行为规范并以大语言模型作为裁判逐条评估轨迹合规性，弥补了仅结果评估无法发现的过程性失败，在四百二十四条 tau-squared-bench 轨迹上揭示了模型特有的故意不服从模式。
- [防篡改 AI Agent 审计追踪：SIEM 集成的合规要求与实践指南](summaries/s3-010-Tamper-Evident-Audit-Trails-for-AI-Agent.md) — 这篇文章的价值在于它将一个通常被视为 "合规 checkbox" 的议题提升到了安全架构的核心位置。作者没有停留在 "你需要审计追踪来满足合规" 的表面陈述，而是深入论证了审计追踪为何是唯一能够验证其他安全控制是否生效的机制。这种 "元控制" 的视角非常深刻——如果身份认证、策略执行和加密保护都在运行，但没有审计记录来证明它们确实在运行，那么从监管和治理角度而言，这些控制的存在与否并无区别。这一逻辑对于构建可信 AI 系统具有重要的方法论意义。
- [AgentPro: Enhancing LLM Agents with Automated Process Supervision](summaries/p-026-AgentPro-Enhancing-LLM-Agents-with-Autom.md) — AgentPro 利用蒙特卡洛树搜索自动构造步骤级训练标签来训练过程奖励模型，再通过拒绝采样策略筛选高分响应并微调智能体，从而在四个基准数据集上显著提升了大语言模型智能体的推理与决策准确率。
- [What Are AI Agent Audit Trails? Why They Matter for Compliance](summaries/s3-007-What-Are-AI-Agent-Audit-Trails-Why-They.md) — - 这篇博客的最大价值在于提供了一份"监管者视角的需求清单"， 这对纯技术研究往往缺失。
- [RFC: should AutoGen support tamper-evident audit trails for multi-agent conversations in regulated industries?](summaries/s3-008-RFC-should-AutoGen-support-tamper-eviden.md) — 这篇 RFC 的价值不仅在于提出了 AutoGen 的合规增强方案，更在于它揭示了多智能体系统从"功能可用"走向"生产可信"时必须跨越的治理鸿沟。当前大多数可观测性方案（包括 OpenTelemetry、LangSmith、Datadog LLM Observability 等）擅长回答系统行为的"是什么"和"什么时候"，但在"是否被允许"这一策略维度上缺乏密码学级别的证明能力。日志可以告诉你某条 API 请求在 14:32 被发出，却无法证明该请求在发出前已经通过了有效的策略审查；传统数据库的写入权限可以被拥有管理员凭证的人员事后修改，而 tamper
- [Auditing Agent Harness Safety](summaries/p-017-Auditing-Agent-Harness-Safety.md) — HarnessAudit 首次将智能体安全评估的单元从最终输出转移到完整执行轨迹，提出三层审计框架和大规模真实基准，系统揭示了当前执行框架在边界合规、执行保真与扰动稳定方面的严重缺陷。
- [AgentOps AI Infrastructure Platform Market Research Report 2034](summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark.md) — 这是一份典型的付费行业研究报告，其价值不在于方法论创新，而在于提供了经过多源交叉验证的市场规模、增长率和竞争格局数据。对于构建 Agent 可观测性综述而言，这类产业报告的最大用途是弥补学术文献在"市场采纳度"和"企业真实痛点"方面的信息缺口。学术文献通常从故障检测、追踪语义、评估基准等技术角度出发，而行业报告则揭示了这些技术问题背后的商业紧迫性——当一家金融或医疗企业决定采购 AgentOps 平台时，其决策往往不是由某个追踪算法的创新驱动的，而是由合规截止日期、Token 成本失控或生产事故触发的。
- [Monitoring Monitorability](summaries/p-006-Monitoring-Monitorability.md) — 随着前沿模型能力不断提升，其造成潜在危害的能力也在增长。确保模型安全部署的两大方向是对齐与控制。尽管对齐研究取得了进展，模型仍偶尔出现不良行为，因此深度防御至关重要。控制协议通常包含某种形式的不良行为分类器，它们可以访问智能体的部分观测信息，例如输入提示、智能体行为、最终输出或内部神经激活。

## 工程含义

- benchmark 应同时报告最终状态、过程规范和失败类别。
- 合规场景中过程违规本身就是失败。
- 多指标评测比单一 reward 更能指导修复。

## 反例与边界

这个观点不是说相邻层不重要，而是说单独依赖该层会留下诊断或治理缺口。 对于低风险 demo，轻量日志可能足够；对于生产智能体、长程任务、多智能体协作或合规场景，必须把 trace、评测、审计和成本信号组织成可追溯证据。

## 相关词条

- [智能体轨迹](terms/agent-trace.md)
- [失败归因](terms/failure-attribution.md)
- [轨迹 Schema](terms/trace-schema.md)
