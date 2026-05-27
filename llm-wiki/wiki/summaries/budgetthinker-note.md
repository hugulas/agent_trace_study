# BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens

## Source

- Raw note: `raw/notes/budgetthinker_note.md`
- Metadata: not available in note

## Compiled Summary

大语言模型的最新进展利用了增加的测试时计算量来增强推理能力，但这种策略在带来性能提升的同时，也造成了显著的延迟和资源开销，限制了其在现实世界中对时间敏感或成本敏感场景的适用性。本文提出了 BudgetThinker，一种旨在赋予大语言模型预算感知推理能力的新框架，使其能够精确控制思维过程的长度。我们所提出的方法在推理过程中周期性插入特殊控制令牌，以持续告知模型剩余的令牌预算。该方法配套了一个完整的两阶段训练流水线：首先通过监督微调使模型熟悉预算约束，然后通过基于课程表的强化学习阶段，利用长度感知的奖励函数同时优化准确率和预算遵守率。实验表明，BudgetThinker 在多个挑战性数学基准上、在不同推理预算下均显著优于强基线方法。本

## Evidence Notes

- 大语言模型通过测试时缩放生成极长的思维链，显著提升了数学和代码等复杂任务的性能，但也带来了极高的延迟与计算开销。对于自动驾驶、机器人控制和实时智能体等存在硬时延约束的场景，简单堆砌推理长度是不可行的。因此，核心问题是如何让模型在**指定的计算预算内**完成推理，并同时保持较高的任务准确率。作者将这一能力定义为**预算遵守**（budget following）。
- 现有方法存在明显不足：直接在提示中插入预算约束往往无法可靠控制输出长度；在"思考模式"与"非思考模式"之间切换的方法缺乏对可变预算的细粒度控制；即便是基于 SFT 或 RL 的训练方法，也难以强制模型严格遵守给定的长度约束。BudgetThinker 旨在解决这一精确控制推理长度的问题。
- BudgetThinker 的核心思想是：仅靠初始提示声明预算约束是不够的，模型需要在生成过程中被**持续提醒**剩余预算。为此，论文提出了控制令牌机制，并配套了从数据构建到训练再到推理的完整方案。
- ### 机制流程
1.
- 论文在 MATH-500、AMC 2023 和 AIME 2024 上，使用 1.5B 和 7B 两种参数规模的模型进行了系统评估。
- **主实验结果**
在 MATH-500 和 AMC 2023 上，BudgetThinker 在各预算档位下的单次生成正确率均显著优于原始模型和对比基线。平均而言，BudgetThinker 比原始模型提升 **4.2%** 的准确率，比 ThinkPrune 提升 **5.7%**。

## Wiki Connections

- Concepts: [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
