# How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks

## Source

- Raw note: `raw/notes/spendmoney_note.md`
- Metadata: not available in note

## Compiled Summary

人工智能智能体在复杂人类工作流程中的广泛普及正在推动大语言模型 token 消耗的快速增长。当智能体被部署到需要大量 token 的任务上时，有三个问题自然浮现：第一，人工智能智能体把 token 花在了哪里？第二，哪些模型在 token 效率上更优？第三，智能体能否在任务执行前预测自己的 token 使用量？
本文首次对智能体编码任务中的消耗模式进行了系统性研究。我们在 SWE-bench Verified 基准上分析了八种前沿大语言模型的执行轨迹，并评估了模型在任务执行前预测自身成本的能力。

## Evidence Notes

- 研究发现任务消耗呈现五大特征。第一，消耗量极为高昂，比代码推理和对话任务多出约一千倍，输入量而非输出量是成本主导因素。第二，使用量高度可变且本质上随机：同一任务不同运行间总量可相差高达三十倍，更高消耗不带来更高准确率，准确率通常在中等成本处峰值并饱和。第三，模型效率差异显著。两款高消耗模型的平均消耗量比 GPT-5 多出一百五十万以上。这两款模型分别为 Kimi-K2 与 Claude 第四代半版本。第四，人类专家评定的任务难度与实际成本仅存在弱相关，揭示了人类感知复杂性与智能体实际计算付出之间的根本鸿沟。第五，前沿模型无法准确预测自身的使用量，相关最高为 0.39，且系统性地低估真实成本。本研究为智能体经济学提供了新的洞察，并有望
- 随着编码智能体（Coding Agents）的能力不断扩展，它们已被越来越多地应用于超越纯编码的复杂长程任务。然而，当前智能体的定价模式面临两大批评：一是缺乏透明度，用户在任务完成前无法知晓最终成本；二是无完成保障，任务失败后用户仍需支付全部 token 费用。这些问题汇聚为一个核心研究问题：我们能否在任务执行前预测 token 消耗？
围绕这一核心问题，本文提出三个具体研究问题：
- 智能体在编码任务中把 token 花在了哪些地方？
- 在相同任务和相同智能体框架下，哪些模型的 token 效率更高？
- 前沿模型能否在执行前准确预测自身的 token 使用量？
若能在执行前给出可靠的 token 用量估计，用户将能更好地理解潜
- > [!figure] Fig.
- 本文采用纯实证分析路线，不提出新的训练方法或模型架构，而是通过控制变量实验和细粒度轨迹解析来回答研究问题。核心方法包含两条主线：一是对已有执行轨迹的消耗模式进行描述性统计与对比分析；二是让模型在执行前进行自预测，评估其预测能力。
- ### 机制流程
**步骤 1：轨迹生成与采集**
- 输入信号：SWE-bench Verified 的问题描述、对应代码仓库、OpenHands 智能体框架配置、八种大语言模型的接口。

## Wiki Connections

- Concepts: [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
