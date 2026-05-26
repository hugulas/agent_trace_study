---
tags:
  - papers/agent-observability
aliases:
  - "AgentRx"
date: 2026
doi: 10.48550/arXiv.2602.02475
---

# AgentRx: Diagnosing AI Agent Failures from Execution Trajectories

## 核心信息

- 标题: AgentRx: Diagnosing AI Agent Failures from Execution Trajectories
- 作者: Shraddha Barke, Arnav Goyal, Alind Khare, Avaljot Singh, Suman Nath, Chetan Bansal
- 年份: 2026
-  venue: arXiv
- 论文编号: arXiv:2602.02475
- 本地文件: `agentic_trace_insight/cited-materials/p-001-agentrx-diagnosing-ai-agent-failures-from-executio.pdf`

## 原文摘要翻译

当前本地元数据没有抽取到完整摘要。根据论文正文中的问题陈述和贡献描述，本文研究如何从智能体执行轨迹中诊断失败原因，尤其是定位导致任务无法完成的第一个不可恢复关键步骤，并给出失败类别。作者构建了一个包含 115 条失败轨迹的标注数据集，覆盖结构化应用程序接口工作流、事故管理和开放式网页或文件任务，并提出 AgentRx 框架，用执行前缀、工具约束、策略约束和观测到的违规证据来做失败归因。

## 创新点

1. 论文把智能体调试问题从“最终是否成功”推进到“哪一步首先不可恢复地导致失败”，使可观测性从结果指标转向轨迹级证据。
2. 数据集包含 115 条失败轨迹，并提供步骤级失败定位和跨领域失败类别标注，为后续失败归因方法提供了可复用基准。
3. AgentRx 不只让模型阅读完整轨迹后猜测原因，而是显式抽取工具、策略和执行前缀中的约束，再把约束违反作为失败归因证据。
4. 论文同时评估智能体定位、步骤定位、失败类别预测和不同容忍窗口下的准确率，比单一最终奖励更适合诊断长轨迹系统。

## 一句话总结

AgentRx 是一个面向智能体执行轨迹的失败诊断框架，核心目标是在长轨迹中定位第一个关键失败步骤，并用约束违反证据解释失败类别。

## 研究问题

智能体系统的调试难点不在于“失败是否发生”，而在于失败如何沿着消息、工具调用、观测和状态更新传播。传统结果评测通常只检查最终数据库状态、最终回复或任务奖励，因此无法回答开发者真正需要的问题：是哪一个动作、哪一个工具调用或哪一次决策让后续执行不可恢复。

论文把问题定义为失败归因和步骤定位：给定一条已经失败的执行轨迹，系统需要找出导致任务无法成功完成的关键步骤，并将失败归入可解释类别。这一设定更接近生产环境中的调试需求，因为工程师需要知道应该修复提示、工具 schema、路由逻辑、状态更新还是安全策略。

![Fig. 1 AgentRx 任务与框架概览](p-001_AgentRx_Diagnosing_AI_Agent_Failures_from_Execution_Trajectories/images/fig1_agentrx.png)
*论文原图编号：Fig. 1。图片来自 LaTeX 源码 `agentrx.png`，概括了 AgentRx 如何根据领域策略、工具 schema 和失败轨迹输出关键失败步骤与失败类别。*

## 数据与任务定义

论文构建的数据集包含 115 条失败智能体执行轨迹，覆盖三个领域：结构化应用程序接口工作流、事故管理，以及开放式网页或文件任务。每条轨迹不仅有失败标签，还标注了第一个不可恢复关键步骤，并分配一个跨领域失败类别。

作者还采样了一个失败归因数据集中的 44 条失败多智能体轨迹。对于 tau-bench，论文评估全部 29 条轨迹；对于 Magentic-One，论文使用 16 条与该数据集标注步骤一致的轨迹。这种设计说明作者关心的不是只在单一基准上拟合，而是希望验证“步骤级失败归因”能否跨任务形态成立。

任务输出至少包含三个层次：失败智能体或失败责任主体、失败步骤索引，以及失败类别。步骤定位被表述为在执行轨迹上的单步识别问题，因此评估时需要比较预测步骤与人工标注关键步骤之间的一致性。

![Fig. 2 跨领域失败时间线](p-001_AgentRx_Diagnosing_AI_Agent_Failures_from_Execution_Trajectories/images/fig2_failure_timelines.png)
*论文原图编号：Fig. 2。图片来自 LaTeX 源码 `failure_timelines.pdf`，展示不同领域中失败在轨迹时间线上的位置分布。*

**Table 1 关键失败标签在不同领域中的分布，来自 LaTeX 源码 `benchmark.tex`。**

| Root-cause category | tau-bench | Flash | Magentic |
|---|---:|---:|---:|
| Instruction Adherence | 10.3 | 23.8 | 18.2 |
| Invention of Information | 0 | 9.5 | 9.1 |
| Invalid Invocation | 3.4 | 0 | 0 |
| Misinterpretation of Tool Output | 24.1 | 33.3 | 34.1 |
| Intent-Plan Misalignment | 24.1 | 0 | 9.1 |
| Under-specified Intent | 27.6 | 19 | 0 |
| Intent Not Supported | 6.9 | 0 | 6.8 |
| Guardrails Triggered | 0 | 0 | 20.5 |
| System Failure | 3.4 | 14.3 | 2.3 |
| Failed trajectories | 29 | 42 | 44 |

## 方法主线

### 机制流程

1. 系统先读取执行轨迹前缀，包括用户意图、智能体消息、工具调用、工具返回和状态更新。
2. AgentRx 从工具定义、系统策略和已观察到的执行上下文中抽取约束，例如必须调用哪些工具、参数应满足什么条件、某些信息是否允许暴露。
3. 框架将轨迹中的动作与这些约束对齐，寻找违反约束的证据。
4. 最后，系统基于违规证据预测关键失败步骤和失败类别，而不是只根据最终输出做整体判断。

这个机制的关键在于把失败诊断转化为证据约束问题。普通的模型判读容易受到长上下文噪声影响，也可能在失败已经扩散后把后果误认为原因；AgentRx 试图通过约束和执行前缀把“原因”限定在更早、更可解释的位置。

### 与运行时监控的区别

相关工作中有一类方法关注运行时保证、行为模型监测或计划一致性检查。AgentRx 的定位不同：它不是在运行时强制阻止行为，也不是只检查计划是否被遵守，而是在失败发生后对整条轨迹做诊断。这个定位更适合作为离线调试和 benchmark 分析工具。

## 关键结果

论文报告了失败归因准确率，并把评估拆成智能体级定位和步骤级定位。证据包中显示，AgentRx 在 tau-bench 和 Magentic-One 轨迹上都优于既有失败归因基线。尤其在步骤定位上，论文关注平均值和标准差，并进一步分析容忍窗口下的准确率，说明严格单步命中和邻近步骤命中都被纳入讨论。

**Table 2 失败归因准确率，来自 LaTeX 源码 `eval.tex`。**

| Method | tau-bench Agent | tau-bench Step | Magentic Agent | Magentic Step |
|---|---:|---:|---:|---:|
| Who&When modified | 62.0 | 17.2 | 6.2 | 56.3 |
| Our Baseline | 75.9 | 32.2 | 81.2 | 56.3 |

**Table 3 平均轨迹与步骤长度，来自 LaTeX 源码 `eval.tex`。**

| Metric | tau-bench | Flash | Magentic |
|---|---:|---:|---:|
| Avg tokens / step | 133 | 169 | 330 |
| Avg chars / step | 480 | 930 | 1280 |
| Avg tokens / trajectory | 4889 | 6415 | 16484 |

**Table 4 全局约束与动态约束消融，来自 LaTeX 源码 `eval.tex`。**

| Method | Step-index acc. | Category acc. |
|---|---:|---:|
| Baseline | 32.2 ± 3.2 | 25.3 ± 1.6 |
| Global-Only | 41.4 ± 2.8 | 28.7 ± 1.6 |
| Dynamic-Only | 43.7 ± 1.6 | 36.8 ± 1.6 |
| AgentRx | 48.3 ± 0 | 39.1 ± 1.6 |

> [!figure] Table 5 到 Table 9 其他消融实验
> 建议位置：关键结果
> 放置原因：这些表格分别检验 judge 输入、约束生成方式、步骤容忍窗口、few-shot 示例和自然语言检查等因素对 AgentRx 的影响。
> 当前状态：保留占位；后续可继续从 `eval.tex` 和 `main.tex` 转写完整表格。

## 深度分析

AgentRx 的价值在于把智能体可观测性中的“trace”变成可诊断对象。很多系统已经能记录消息、工具调用和状态，但日志本身并不自动给出失败原因。AgentRx 的思路是把 trace 与约束系统结合：如果某一步违反了工具参数约束、策略要求或执行前缀导出的条件，那么这一步就比后续失败现象更接近根因。

这个思路也解释了为什么论文强调“第一个不可恢复步骤”。在长轨迹中，后续多个步骤可能都看起来异常，但它们可能只是早期错误的传播结果。以生产调试视角看，定位后果并不能指导修复；定位第一个不可恢复步骤才可能告诉工程师应该修提示词、工具 schema、路由策略还是状态管理。

需要注意的是，AgentRx 仍依赖模型或规则抽取约束，约束质量会影响诊断质量。如果系统提示本身含糊，或者工具行为没有被清晰规格化，那么框架可能找不到稳定证据。换言之，AgentRx 更适合有明确工具接口和任务规则的智能体系统，对完全开放式任务的适用性需要更多验证。

## 局限

1. 数据集规模是 115 条失败轨迹，适合做诊断任务定义和初步评估，但还不足以覆盖所有真实生产故障模式。
2. 论文没有证明约束抽取在高度开放、弱规格任务中同样稳定。
3. 步骤级人工标注本身可能存在边界争议，尤其当多个错误连续发生时，“第一个不可恢复步骤”不一定唯一。
4. 当前 figure 资产抽取对表格支持不足，因此本笔记保留多个表格占位，避免插入不完整或错配图片。

## 我的笔记

这篇论文适合作为“智能体可观测性不等于日志收集”的核心引用。它把日志后的分析任务具体化为失败归因、步骤定位和类别预测，和很多只讲链路追踪、指标与成本归因的工程文章形成互补。后续如果要设计智能体调试平台，可以把 AgentRx 视为轨迹诊断层：底层记录 OpenTelemetry 风格事件，上层用约束和策略把事件解释成可修复的问题。

## 引用

- Zhang et al. (2025). Who&When failure attribution benchmark.
- Koohestani (2025). Runtime assurance for AI agents.
- Madaan et al. (2023). Self-Refine.
- Gou et al. (2024). Critic.
