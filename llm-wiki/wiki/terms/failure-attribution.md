# 失败归因

## 定义

失败归因关注失败由哪个智能体、哪个步骤、哪类约束违反或哪条依赖链触发。它把可观测性从“发生了失败”推进到“应该修哪里”。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 第一个不可恢复步骤在哪里？
- 错误是根因还是后果？
- 责任主体是模型、工具、路由、提示还是 harness？

## 证据入口

- [Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems](summaries/p-022-Which-Agent-Causes-Task-Failures-and-Whe.md) — 本文首次形式化并系统研究了 LLM 多智能体系统的自动化故障归因问题，构建了 Who-When 数据集，发现即便最优方法在定位故障步骤上的准确率也远低于实用门槛，揭示了该任务的根本性困难。
- [AgentRx: Diagnosing AI Agent Failures from Execution Trajectories](summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories.md) — AgentRx 是一个面向智能体执行轨迹的失败诊断框架，核心目标是在长轨迹中定位第一个关键失败步骤，并用约束违反证据解释失败类别。
- [MASPrism: Lightweight Failure Attribution for Multi-Agent Systems Using Prefill-Stage Signals](summaries/c-006-MASPrism-Lightweight-Failure-Attribution.md) — MASPrism 最吸引我的地方在于它从根本上重新定义了「诊断」与「推理」之间的关系。
- [AgentDiagnose: An Open Toolkit for Diagnosing LLM Agent Trajectories](summaries/p-029-AgentDiagnose-An-Open-Toolkit-for-Diagno.md) — AgentDiagnose 是一个开源诊断工具包，通过 LLM 驱动的多维度评估与交互式可视化，帮助研究者超越成功与失败二分法，深入理解智能体轨迹的内在行为质量，并能以轨迹质量信号筛选出少量高价值训练数据带来性能提升。
- [LLM Agent Cost Attribution: Complete Production 2026 Guide](summaries/s3-014-LLM-Agent-Cost-Attribution-Complete-Prod.md) — 这篇指南的价值在于它将成本归因从一个财务部门的报表需求，重新定义为工程团队的基础设施责任。
- [DoVer: Intervention-Driven Auto Debugging for LLM Multi-Agent Systems](summaries/p-003-DoVer-Intervention-Driven-Auto-Debugging.md) — 当前基于大语言模型的多智能体系统在开发和部署过程中频繁出现非崩溃型故障：系统执行未中断，但输出结果不正确或不符合预期。现有主流做法是让大语言模型分析执行日志，将故障归因到特定智能体或特定步骤。然而，作者通过复现研究指出这一范式面临以下根本性问题。
- [What Is AI Agent Observability? Why Cost Is What You're Missing](summaries/s3-015-What-Is-AI-Agent-Observability-Why-Cost.md) — 这篇文章的价值在于它把「成本」从可观测性的附属指标提升为核心信号。
- [The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break](summaries/p-016-The-Long-Horizon-Task-Mirage-Diagnosing.md) — 本文提出跨领域诊断基准 HORIZON，通过统一视界度量、七维失败分类体系和 LLM-as-a-Judge 归因流程，系统揭示了当前最先进智能体在长程任务中的性能崩溃规律与失败机制转移，指出仅靠基础模型缩放不足以解决规划错误和灾难性遗忘等主导瓶颈。
- [Systematic debugging for AI agents: Introducing the AgentRx framework](summaries/a-003-Systematic-debugging-for-AI-agents-Intro.md) — AgentRx 博客的价值不仅在于技术本身，更在于它清晰地展示了一个从学术研究到开源工具的完整叙事。
- [防篡改 AI Agent 审计追踪：SIEM 集成的合规要求与实践指南](summaries/s3-010-Tamper-Evident-Audit-Trails-for-AI-Agent.md) — 这篇文章的价值在于它将一个通常被视为 "合规 checkbox" 的议题提升到了安全架构的核心位置。作者没有停留在 "你需要审计追踪来满足合规" 的表面陈述，而是深入论证了审计追踪为何是唯一能够验证其他安全控制是否生效的机制。这种 "元控制" 的视角非常深刻——如果身份认证、策略执行和加密保护都在运行，但没有审计记录来证明它们确实在运行，那么从监管和治理角度而言，这些控制的存在与否并无区别。这一逻辑对于构建可信 AI 系统具有重要的方法论意义。

## 相关词条

- [智能体轨迹](terms/agent-trace.md)
