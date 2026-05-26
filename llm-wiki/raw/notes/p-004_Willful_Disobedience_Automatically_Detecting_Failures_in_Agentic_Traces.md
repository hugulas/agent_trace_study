---
tags:
  - papers/agent-observability
aliases:
  - "AgentPex"
date: 2026
doi: 10.1145/3786335.3813153
---

# Willful Disobedience: Automatically Detecting Failures in Agentic Traces

## 核心信息

- 标题: Willful Disobedience: Automatically Detecting Failures in Agentic Traces
- 作者: Reshabh K Sharma, Shraddha Barke, Benjamin Zorn
- 年份: 2026
-  venue: Proceedings of the ACM Conference on AI and Agentic Systems
- DOI: 10.1145/3786335.3813153
- 本地文件: `agentic_trace_insight/cited-materials/p-004-agentpex-automatically-detecting-failures-in-agent.pdf`

## 原文摘要翻译

人工智能智能体正越来越多地嵌入真实软件系统中，通过多轮对话、工具调用和中间决策执行多步骤工作流。这些很长的执行历史被称为智能体轨迹，它们让验证变得困难。只看结果的基准可能漏掉关键过程性失败，例如错误的工作流路由、不安全的工具使用，或违反提示中指定的规则。本文提出 AgentPex，这是一个由人工智能驱动的工具，旨在系统评估智能体轨迹。AgentPex 从智能体提示和系统指令中抽取行为规则，然后用这些规范自动评估轨迹是否合规。作者在来自 `${\tau}^2$-bench` 的 424 条轨迹上评估 AgentPex，覆盖电信、零售和航空客户服务中的多个模型。结果表明，AgentPex 能区分不同模型的智能体行为，并发现只看结果评分无法捕捉的规范违反。它还提供按领域和指标划分的细粒度分析，使开发者能够大规模理解智能体的强项和弱点。AgentPex 源代码发布在 `https://github.com/microsoft/agentpex`。

## 创新点

1. AgentPex 把智能体评估从最终状态正确性扩展到过程合规性，能发现结果奖励没有覆盖的规则违反。
2. 方法从提示、系统指令和工具定义中抽取行为规范，再用规范评估轨迹，使评测对象从“答案”变成“执行过程”。
3. 论文在 424 条 `${\tau}^2$-bench` 轨迹上比较多个模型和三个客户服务领域，提供了模型、领域和指标粒度的失效画像。
4. 论文把 AgentPex 分数与 $\tau^2$ 结果奖励对齐分析，并报告 `output_spec` 作为失败分类器时的 ROC-AUC 为 0.680，说明过程评测和结果评测有相关性但不完全重合。

## 一句话总结

AgentPex 是一个从提示和工具规范中抽取行为规则、再自动检查智能体轨迹是否违反这些规则的过程性评测工具。

## 研究问题

结果型 benchmark 的问题是视野太窄。一个智能体可能最终碰巧得到正确数据库状态，但过程中调用了错误工具、暴露了不该暴露的信息，或者违反了系统提示中的操作顺序。相反，一个任务也可能最终失败，但开发者仍然需要知道失败来自参数错误、路由错误、计划偏离还是输出格式不合规。

AgentPex 针对的是这种“轨迹合规性”问题：给定系统提示、工具 schema 和完整消息日志，自动抽取可检查规范，并对轨迹进行多维度评分。它不是替代最终奖励，而是补足最终奖励无法解释过程错误的缺口。

## 数据与任务定义

实验数据来自 $\tau^2$-bench，论文使用 424 条轨迹，覆盖电信、零售和航空客户服务场景。$\tau^2$ 原始评测根据最终数据库状态和最终通信内容计算二元奖励，并使用包含 93 个任务、1145 条人工标准的标注集合。

作者为每个领域抽取约 50 条轨迹，并通过自动选择脚本平衡任务多样性、成功失败比例和轨迹复杂度。论文中的模型包括 Claude 3.5 Sonnet、GPT-4.1 和 o4-mini。AgentPex 输出的不是单一成功失败标签，而是一组 0 到 100 的合规性评分。

## 方法主线

### 机制流程

![Fig. 1 AgentPex 轨迹违规示例](p-004_Willful_Disobedience_Automatically_Detecting_Failures_in_Agentic_Traces/images/fig1_agentpex_example.png)
*论文原图编号：Fig. 1。图片来自 LaTeX 源码 `figures/agentpex-example.pdf`，展示智能体虽然达到正确最终结果，但违反转换、输出和预测计划规范。*

![Fig. 3 AgentPex 处理流水线](p-004_Willful_Disobedience_Automatically_Detecting_Failures_in_Agentic_Traces/images/fig3_agentpex_pipeline.png)
*论文原图编号：Fig. 3。图片来自 LaTeX 源码 `figures/agentpex.pdf`，展示从原始轨迹导入、规范抽取到多指标评估和聚合评分的流程。*

1. 轨迹规范化：AgentPex 把不同来源的轨迹转换成统一表示，包括系统提示、工具 schema，以及由用户、助手和工具消息构成的顺序日志。
2. 规范抽取：系统从提示和工具定义中抽取行为规则，例如事实性声明需要引用来源、不得泄露内部推理、输出需要满足指定格式。
3. 轨迹评估：多个基于大模型的 judge 对轨迹进行合规性评分，分数范围为 0 到 100。
4. 聚合分析：AgentPex 按模型、领域、指标和单条轨迹输出结果，帮助开发者定位模型弱点和具体违反类型。

### 指标设计

AgentPex 的指标覆盖输出规范、参数规范、预测计划和预测最终状态等维度。这个拆分很重要，因为同一个最终失败可能由不同过程问题导致；同一个根因也可能在多个指标上产生连锁反应。论文没有把所有错误压缩成一个 reward，而是保留多维诊断信息。

## 关键结果

论文发现，AgentPex 能区分不同模型和领域中的行为差异，并能发现 `${\tau}^2` 结果评分没有直接暴露的规范违反。Fig. 5 显示，当轨迹按 AgentPex 聚合分数排序时，低 `${\tau}^2` 轨迹集中在低 AgentPex 分数区域，说明过程合规性与最终任务结果存在一致性。

![Fig. 5 AgentPex 聚合分数与 tau2 复合分数的关系](p-004_Willful_Disobedience_Automatically_Detecting_Failures_in_Agentic_Traces/images/fig5_tau_sq_vs_aggregate_trace.png)
*论文原图编号：Fig. 5。图片来自 LaTeX 源码 `figures/tau_sq_vs_aggregate_trace.png`，展示 AgentPex 聚合分数与 $\tau^2$ 复合分数之间的对应关系。*

进一步地，论文把 `output_spec` 评估器当作 $\tau^2$ 失败的二分类器，报告 ROC-AUC 为 0.680。这个数值不表示 AgentPex 可以完全替代结果标签，而是说明过程规范违反与最终失败之间存在可测相关性。

![Fig. 6 不同模型的分指标得分](p-004_Willful_Disobedience_Automatically_Detecting_Failures_in_Agentic_Traces/images/fig6_all_model_perf_metrics_chart.png)
*论文原图编号：Fig. 6。图片来自 LaTeX 源码 `figures/all_model_perf_metrics_chart.png`，比较不同模型在各类规范指标上的表现。*

![Fig. 7 不同领域的分指标得分](p-004_Willful_Disobedience_Automatically_Detecting_Failures_in_Agentic_Traces/images/fig7_domain_perf_metrics_chart.png)
*论文原图编号：Fig. 7。图片来自 LaTeX 源码 `figures/domain_perf_metrics_chart.png`，展示电信、零售和航空领域的指标差异。*

![图 8 输出规范评分对 tau2 失败的分类曲线](p-004_Willful_Disobedience_Automatically_Detecting_Failures_in_Agentic_Traces/images/fig8_threshold_analysis.png)
*论文原图编号：Fig. 8。图片来自 LaTeX 源码 `figures/threshold_analysis.png`，评估 `output_spec` 分数作为失败分类信号时的区分能力。*

![Fig. 9 不同模型的 tau2 复合分数与 AgentPex 聚合分数](p-004_Willful_Disobedience_Automatically_Detecting_Failures_in_Agentic_Traces/images/fig9_all_tau_sq_performance_comparison.png)
*论文原图编号：Fig. 9。图片来自 LaTeX 源码 `figures/all_tau_sq_performance_comparison.png`，显示结果型评估难以区分模型间过程合规差异。*

**Table 1 按模型聚合的多指标分数，来自 LaTeX 源码 `evaluation.tex`。**

| Metric | Claude 3.5 Sonnet | GPT-4.1 | o4-mini |
|---|---:|---:|---:|
| Overall Aggregate | 57.6 | 62.6 | 62.9 |
| Output Spec | 63.6 | 65.0 | 66.9 |
| Transition Spec | 59.2 | 63.7 | 80.6 |
| Predicted Plan Spec | 81.0 | 80.1 | 77.0 |
| Argument Groundedness | 98.7 | 99.1 | 98.1 |
| tau2 Reward | 41.4 | 37.5 | 38.6 |

**Table 2 平均每条轨迹评估成本，来自 LaTeX 源码 `evaluation.tex`。**

| Computational cost metric | Cost |
|---|---:|
| API calls | 约 9 次大模型调用 |
| Total tokens | 约 77621，其中约 69000 输入、8500 输出 |
| Wall-clock time | 139 秒 |
| Estimated cost | 0.019 美元 |

## 深度分析

AgentPex 的核心贡献是把“提示词中的要求”变成可执行评测规范。很多智能体系统的问题不是没有日志，而是日志无法自动说明是否违反了系统设计意图。AgentPex 通过规范抽取把系统意图显式化，再让 judge 对轨迹逐项检查，这比只看最终状态更接近工程调试需要。

这篇论文也提示了一个重要设计方向：智能体评测应该分层。最终奖励回答“任务是否完成”，过程规范回答“完成方式是否合规”，多指标诊断回答“哪里不合规”。在客户服务、合规和安全场景中，第二层和第三层往往比最终结果更重要，因为违规过程本身就可能造成风险。

不过，AgentPex 的可靠性取决于规范抽取质量和 judge 稳定性。如果提示写得含糊，或工具 schema 无法表达真实业务规则，抽出的规范可能不完整。另一个风险是多指标之间不独立：一次错误参数可能同时导致计划偏离、输出不合规和最终状态错误，因此指标分析需要避免把连锁后果误解成多个独立根因。

## 局限

1. AgentPex 使用大模型 judge，评测稳定性会受到 judge 模型、提示和上下文长度影响。
2. 规范抽取依赖原始提示和工具 schema 的质量，弱规格系统可能抽不出可检查规则。
3. 论文实验集中在 `${\tau}^2$-bench` 的客户服务任务上，对更开放任务或多智能体协作场景还需要额外验证。
4. ROC-AUC 0.680 说明过程指标与结果失败相关，但距离稳定替代最终奖励还有差距。

## 我的笔记

AgentPex 和 AgentRx 可以形成互补：AgentPex 更偏“规范合规性检测”，适合持续评估和横向比较模型；AgentRx 更偏“失败根因定位”，适合失败后调试。放在可观测性系统里，AgentPex 可以作为轨迹规则评测层，AgentRx 可以作为失败样本的根因分析层。

这篇论文对生产系统的启发是：不要只存轨迹，也不要只算最终成功率。更好的做法是把系统提示、工具 schema、业务约束和 trace 放在一起，让评测器能回答“智能体是否按要求行动”。这也是智能体 observability 区别于传统日志平台的地方。

## 引用

- `${\tau}^2$-bench`.
- Claude 3.5 Sonnet.
- GPT-4.1.
- o4-mini.
