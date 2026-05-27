# SWE-Edit: Rethinking Code Editing for Efficient SWE-Agent

## Source

- Raw note: `raw/notes/sweedit_note.md`
- 作者: Yikai Zhang, Jiaxin Pei, Kenan Li, Maoquan Wang, Jin Pan, Yu Kang, Shengyu Fu, Elsie Nallipogu, Junjie Hu, Yufan Huang, Zijian Jin
- 年份: 2026
- DOI: 10.48550/arXiv.2604.26102

## Compiled Summary

大语言模型智能体在软件工程任务上取得了显著进展，然而当前方法存在一个根本性的上下文耦合问题：标准的代码编辑接口将代码检查、修改规划和编辑执行混在同一个上下文窗口中，迫使智能体将探索性的代码浏览与严格格式化的编辑生成交错进行。这导致无关信息不断累积，从而降低智能体的性能。为解决这一问题，本文提出 SWE-Edit，将代码编辑分解为两个专门的子智能体：一个按需提取任务相关代码的查看器，以及一个根据高层计划执行修改的编辑器，从而让主智能体专注于推理，同时将上下文密集的操作委托给干净的专用上下文窗口。本文进一步探究了何种因素造就了一个有效的编辑模型：观察到主流的查找替换格式容易出错，作者使用 GRPO 训练 Qwen3-8B 来自适应地选择

## Evidence Notes

- 当前 LLM 编程智能体的核心瓶颈在于上下文耦合问题：代码查看、修改规划和编辑执行被压缩在同一个上下文窗口中，造成三类结构性矛盾。
- 第一，探索与精确的矛盾。有效的调试需要广泛浏览多个文件、追踪依赖、验证假设，但每一次查看的代码片段都会保留在上下文中，无论其最终是否相关。与此同时，生成正确的代码编辑需要对精确位置和格式的聚焦关注。先前研究已证实，当任务相关信息被淹没在无关上下文中时，大语言模型性能会显著下降。
- SWE-Edit 的框架包含两个层面的优化：脚手架层面的接口解耦与模型层面的编辑策略学习。两者共同作用，但各自独立可解释。
- ### 脚手架解耦设计
**Viewer 子智能体**：接收完整文件内容，根据主智能体发出的查询按需提取与任务相关的代码片段。它使用较小规模的模型处理完整文件，并将精简后的上下文返回给主智能体。这样，主智能体的上下文窗口不再被探索性浏览污染。
- **主实验结果（SWE-bench Verified，500 实例，3 次运行平均）**：
- 基线（单体智能体）：解决率 69.9%，成本 243.7 美元，编辑成功率 93.4%。
- - 仅添加 Viewer：解决率 70.3%（+0.4 个百分点），成本 225.0 美元（-7.7%）。

## Wiki Connections

- Concepts: [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
