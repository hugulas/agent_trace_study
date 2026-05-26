# EAGER: Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation

## Source

- Raw note: `raw/notes/p-018_EAGER_Efficient_Failure_Management_for_M.md`
- 作者: Lingzhe Zhang, Tong Jia, Mingyu Wang, Weijie Hong, Chiming Duan, Minghua He, Rongqian Wang, Xi Peng, Meiling Wang, Gong Zhang, Renhai Chen, Ying Li
- DOI: 10.48550/arXiv.2603.21522
- PDF: [p-018]-eager-efficient-failure-management-for-multi-agent-systems-w.pdf

## Compiled Summary

基于大语言模型的多智能体系统已经成为软件系统设计的新范式，日益展现出强大的推理与协作能力。随着这类系统变得愈发复杂和自主，有效的故障管理对于保障系统的可靠性与可用性至关重要。然而，现有方法往往依赖逐轨迹推理，导致效率低下，同时忽视了历史故障模式，从而限制了诊断的准确性。本文首先开展了一项初步实证研究，论证了在多智能体系统故障管理中利用历史故障模式的必要性、潜力与挑战。基于这一洞察，我们提出了 EAGER，一种基于推理轨迹表示的多智能体系统高效故障管理框架。EAGER 采用无监督的推理范围对比学习，同时对智能体内部推理与智能体间协调进行编码，从而在历史故障知识的引导下实现实时的逐步骤故障检测、诊断与反射式缓解。在三个开源多智能体系统上

## Evidence Notes

- 基于大语言模型的多智能体系统已在软件工程、智能助手和科学工作流等多个领域得到广泛应用。然而，这些系统的动态行为与推理过程会带来不可预测的故障，传统的监控与调试手段往往难以及时、准确地处理。AgentOps 概念由此提出，旨在利用智能体级别的推理轨迹系统性地管理、诊断和缓解故障。
- 现有 AgentOps 方法大致分为两类：异常检测方法判断某段多智能体系统推理是否失败或被篡改；故障诊断方法则定位失败的智能体、步骤与错误类型。这些方法在通用多智能体系统上已取得一定效果，但在实际部署中面临两个核心挑战：
- **逐轨迹推理导致效率低下**。现有方法通常让大型评判语言模型对每条轨迹独立进行语义推理分析，不仅单条处理成本高，而且在大吞吐量场景下整体运营效率显著下降。
- EAGER 的整体框架如 Figure 1 所示。系统运行时首先捕获多智能体交互过程中生成的推理轨迹，其中既包含智能体内部的推理过程，也包含智能体间的编排模式。随后，经过推理范围对比学习训练的专用表示模型将这些轨迹编码到统一潜在空间中，实现对智能体内语义与智能体间语义的联合对齐。在运行阶段，EAGER 执行逐步骤检测，将每一步推理与历史故障知识进行比对，实时识别潜在故障；一旦检测到故障，便触发反射式缓解机制，允许智能体自我反思、重新规划或重新生成响应。当用户确认最终输出错误时，系统还会启动可选的专家审查与智能体根因分析流程，持续更新故障知识库。这一闭环设计的核心思想是：检测与缓解能力不应停留在静态部署，而应随着系统运行不断从实际故障
- ![Fig.
- 作者在三个开源多智能体系统上开展了初步评估，核心实验结果分为异常检测与故障诊断性能、检测延迟以及任务性能提升三个维度。
- 值得注意的是，Table 3 中异常检测的 F1 普遍高于故障诊断，这在方法论上是合理的：粗粒度检测只需判断轨迹是否与已知失败模式相似，而细粒度诊断还需定位具体错误步骤。两种任务的难度差异也解释了为什么 EAGER 采用分层检测策略——先用低成本粗粒度过滤快速捕获大部分失败，再在必要时启用更精细的诊断。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/observability-products-and-market-map]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: [[entities/AgentOps|AgentOps]]
