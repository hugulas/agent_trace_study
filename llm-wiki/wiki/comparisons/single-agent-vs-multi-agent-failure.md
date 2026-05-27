# 单智能体失败与多智能体失败对比

## 对比表

| 维度 | 对象 1 | 对象 2 |
| --- | --- | --- |
| 失败边界 | 单条轨迹内的步骤、工具和状态 | 多个角色之间的消息、依赖和共享状态 |
| 主要根因 | 工具参数错误、计划偏离、误读观察、输出不合规 | 通信丢失、角色职责混淆、依赖传播、冲突决策 |
| 归因难点 | 第一个不可恢复步骤不唯一 | 责任可能跨 agent 和时间扩散 |
| 所需 trace | 步骤级消息和工具调用 | agent 身份、交互边、依赖链、共享资源访问 |
| 代表来源 | AgentRx, AgentPex, AgentSight | Why Do Multi-Agent LLM Systems Fail, Who&When, EvoCF, MASPrism |

## 读法

这个对比页用于帮助选择分析层，而不是给工具或论文排名。若要解释单条失败轨迹，优先看诊断与归因；若要比较模型和领域，优先看过程评测；若要做生产接入，先保证结构化采集和 schema 稳定。

## 证据入口

- [Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems](summaries/p-022-Which-Agent-Causes-Task-Failures-and-Whe.md) — 随着 LLM 多智能体系统（如 AutoGen、CAMEL、MetaGPT 等）在编码、科学发现、复杂现实世界问题求解等领域展现出巨大潜力，系统开发通常遵循一个迭代循环：在基准上评估系统表现，然后手动进行故障归因，最后针对性地改进系统。然而，故障归因——即识别直接导致任务失败的系统组件——目前几乎完全依赖人工完成。开发人员需要分析复杂的历史执行日志，理解每个智能体的行为逻辑，并判断哪些动作是正确的、哪些动作误导了整个求解过程。随着系统复杂度增加，组件数量增多，手动故障归因变得愈发困难且耗时。
- [EAGER: Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation](summaries/p-018-EAGER-Efficient-Failure-Management-for-M.md) — EAGER 的整体框架如 Figure 1 所示。系统运行时首先捕获多智能体交互过程中生成的推理轨迹，其中既包含智能体内部的推理过程，也包含智能体间的编排模式。随后，经过推理范围对比学习训练的专用表示模型将这些轨迹编码到统一潜在空间中，实现对智能体内语义与智能体间语义的联合对齐。在运行阶段，EAGER 执行逐步骤检测，将每一步推理与历史故障知识进行比对，实时识别潜在故障；一旦检测到故障，便触发反射式缓解机制，允许智能体自我反思、重新规划或重新生成响应。当用户确认最终输出错误时，系统还会启动可选的专家审查与智能体根因分析流程，持续更新故障知识库。这一闭环设
- [Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering Agents](summaries/p-005-Debugging-the-Debuggers-Failure-Anchored.md) — PROBE 将软件工程智能体的失败后恢复建模为从失败运行遥测到有边界恢复指导的结构化转换。核心架构包含三个耦合阶段：遥测层、诊断层和引导门。
- [Why Do Multi-Agent LLM Systems Fail?](summaries/p-021-Why-Do-Multi-Agent-LLM-Systems-Fail.md) — 本文的方法论围绕“如何从经验数据中系统提炼 MAS 失败模式”展开，分为四个阶段： ### 机制流程 1.
- [MASPrism: Lightweight Failure Attribution for Multi-Agent Systems Using Prefill-Stage Signals](summaries/c-006-MASPrism-Lightweight-Failure-Attribution.md) — MASPrism 最吸引我的地方在于它从根本上重新定义了「诊断」与「推理」之间的关系。
- [OpsAgent: An Evolving Multi-agent System for Incident Management in Microservices](summaries/p-019-OpsAgent-An-Evolving-Multi-Agent-System.md) — OpsAgent 整体架构包含三大核心模块：无需训练的数据处理器、多智能体协作框架和双重自进化机制，分别对应上述三大挑战。
- [How we built our multi-agent research system — Anthropic Engineering Blog](summaries/a-009-How-we-built-our-multi-agent-research-sy.md) — Anthropic 这篇文章堪称多智能体系统从原型到生产的最完整工程复盘之一，其价值不仅在于架构设计，更在于对"为什么有效"和"代价是什么"的坦诚剖析。90.2% 的性能提升令人印象深刻，但"token 消耗解释 80% 方差"这一发现更具理论意义——它暗示多智能体系统的性能提升在很大程度上是"推理容量扩展"的结果，而非某种神秘的涌现智能。这对综述的方法论有重要启示：在评估多智能体系统时，必须将 token 效率与结果质量同时纳入指标，否则可能产生误导性的结论。一个消耗 15 倍 token 却只提升 10% 准确率的系统，与一个消耗 2 倍 token
- [Willful Disobedience: Automatically Detecting Failures in Agentic Traces](summaries/p-004-Willful-Disobedience-Automatically-Detecting-Failures-in-Agentic-Traces.md) — 1。图片来自 LaTeX 源码 figures/agentpex-example.pdf，展示智能体虽然达到正确最终结果，但违反转换、输出和预测计划规范。* *论文原图编号：Fig.

## 相关页面

- [智能体轨迹](terms/agent-trace.md)
- [智能体可观测性不是日志收集](viewpoints/observability-is-not-logging.md)
- [最终奖励不足以评估智能体](viewpoints/final-reward-is-insufficient.md)
