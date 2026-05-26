# AgentPro: Enhancing LLM Agents with Automated Process Supervision

## Source

- Raw note: `raw/notes/p-026_AgentPro_Enhancing_LLM_Agents_with_Autom.md`
- Metadata: not available in note

## Compiled Summary

大语言模型智能体通过思维链推理和工具调用等机制，在解决复杂任务方面展现出巨大潜力。然而，现有框架在推理过程中缺乏显式监督，这可能导致错误在推理链中传播，并阻碍中间决策阶段的优化。本文提出了一种新颖的框架 AgentPro，通过自动化的过程监督来提升大语言模型智能体的性能。AgentPro 采用蒙特卡洛树搜索自动生成分步级别的标注，并基于这些标注训练过程奖励模型，从而实现对推理过程的细粒度质量评估。通过采用拒绝采样策略，大语言模型智能体动态调整生成概率分布，以防止错误路径的延续，进而提升推理能力。在四个数据集上的大量实验表明，本文方法显著优于现有的基于智能体的大语言模型方法（例如在 HotpotQA 数据集上准确率提升了 6.32%）

## Evidence Notes

- 当前的大语言模型智能体框架（如 ReAct、Reflexion、ExpeL）在处理多步复杂任务时，通常只对最终输出进行验证，而缺乏对中间推理步骤的显式监督。这种缺陷会导致以下问题：
- **错误传播**：一旦某个中间步骤出错，后续步骤会在错误基础上继续推导，最终导致整体失败。
- - **难以优化**：没有细粒度的步骤级反馈，智能体无法针对性地改进其决策策略。
- AgentPro 的核心思路是将过程监督自动化的三个环节串联起来：自动标注、PRM 训练、拒绝采样微调。整个框架围绕两个核心模型展开，分别记为 $M_a$（待优化的智能体）与 $M_p$（过程奖励模型）。
- ### 机制流程
1.
- ### 主实验结果
在 LLaMA-3.1-8B-Instruct 上的主实验表明，AgentPro 在四个数据集上均稳定超越所有基线：
- **FEVER**：相比最优基线 ExpeL（51.87%）提升 3.59%，达到 55.46%（按文中 Fig.
- 3 及描述推算）。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]]
- Entities: None identified
