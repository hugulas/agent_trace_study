# Retrieval-Conditioned Topology Selection with Provable Budget Conservation for Multi-Agent Code Generation

## Source

- Raw note: `raw/notes/retrievaltopo_note.md`
- Metadata: not available in note

## Compiled Summary

面向代码生成的多智能体大语言模型系统面临一个根本性的路由问题：最优的编排拓扑取决于待修改代码的结构复杂度，但现有系统在选拓扑时并不参考代码库。本文提出检索引导自适应编排（RGAO），其架构通过从分层代码索引中提取结构复杂度向量，再据此选择编排拓扑，从而将这一环路闭合。RGAO 运行在 Code-Agent 多智能体框架内，该框架的子智能体受形式化契约约束，契约内包含六维预算向量。本文的核心贡献是将此前相互独立的两条研究线——复杂度条件化的大语言模型路由与形式化资源代数——加以组合，获得了单独一方均不具备的性质：在检索条件化的动态拓扑选择下，预算具有可证明的守恒性。具体贡献包括：（1）一种复杂度条件化拓扑路由器，在代理评估中将误路由率

## Evidence Notes

- 现有面向代码生成的多智能体系统通常采用固定或仅基于查询文本的编排拓扑，无法区分单文件修补与跨模块重构所需的协作规模，导致资源错配与效率损失。如何根据待修改代码的实际结构复杂度自适应选择拓扑，并在动态选择过程中给出可证明的预算守恒保证，是本文要解决的核心问题。
- CODE-AGENT 框架包含三层：检索层、路由层与执行层。子智能体通过形式化契约管理，契约包含指令与完成条件、六维预算向量、按风险格过滤的工具白名单以及模型配置四个维度。RGAO 在检索层提取结构复杂度向量，在路由层基于规则映射到四种拓扑之一，在执行层通过预算代数静态验证后再调度。
- 预算向量的定义如下：
$$B = (B_{\text{iter}}, B_{\text{calls}}, B_{\text{tok}}, B_{\text{sec}}, B_{\text{retry}}, B_{\text{handoff}}) \in \mathbb{N}^6$$
并行组合操作定义为：
$$B_1 \oplus B_2 = (B_{1,i} + B_{2,i})_{i=1}^6$$
委托约束要求子智能体的预算组合不超过父智能体：
$$\bigoplus_{i=1}^{k} B_i \preceq B_{\text{parent}}$$
复杂度向量为五维：
$$c = (d_{\text{dep}}, n_f, n_
- - 路由精度：在 150 例测试集上，规则型路由器将误路由率从基于正则的基线 30.1%（95% 置信区间 [26.4, 34.1]）降至 8.2%（[6.1, 10.9]），绝对降低 21.9 个百分点，相对降低 73%。配对检验的统计量为 $\chi^2 = 43.6$，$p < 10^{-6}$。收益主要来自正则基线被关键词误导，而本文方法通过复杂度向量识别出实际范围有限的场景。
- - 任务解决率：在代理评估中，本文系统 pass@1 为 40.0%，对比基线分别为 45.9%、41.0% 与 66.4%（最后一项存在数据污染）。各基线模型如下：
- Claude Opus 4.5：45.9%
- GPT-5.2 Codex：41.0%
- OpenHands（Verified*）：66.4%
- 流水线正确性与成本：在 5 条 SWE-CI 流水线上，CODE-AGENT 达到 100% 流水线正确率，平均每条流水线约 6,000 token，包含两次通过状态机恢复的干预。

## Wiki Connections

- Concepts: [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [Codex CLI](entities/Codex-CLI.md)
