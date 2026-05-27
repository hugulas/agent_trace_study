# MAS-Bench: A Unified Benchmark for Shortcut-Augmented Hybrid Mobile GUI Agents

## Source

- Raw note: `raw/notes/masbench_note.md`
- Metadata: not available in note

## Compiled Summary

应用程序接口和深度链接等快捷方式（shortcuts）已经成为灵活图形用户界面操作的高效补充，催生了一种有前景的基于多模态大语言模型的移动自动化混合范式。然而，对图形用户界面与快捷方式混合智能体的系统评测在很大程度上仍未被探索。为填补这一空白，本文提出 MAS-Bench，这是一个率先专注于移动领域的图形用户界面与快捷方式混合智能体评测基准。除使用预定义快捷方式外，MAS-Bench 还评估智能体通过发现和创建可复用、低成本工作流来自主生成快捷方式的能力。该基准涵盖 11 个真实世界应用中的 139 项复杂任务，包含 88 个预定义快捷方式（应用程序接口、深度链接、机器人流程自动化脚本）的知识库，以及 9 项评测指标。实验表明，混合

## Evidence Notes

- ### 为什么纯图形用户界面智能体不够
基于大语言模型的图形用户界面智能体通过模拟人类点击、滑动、输入等操作来完成移动设备上的复杂任务，具备跨应用的通用性。然而，完全依赖大语言模型进行细粒度图形用户界面交互带来了两个核心问题：
- **效率与成本问题**：对于常规任务，智能体需要逐步执行大量图形用户界面操作，导致执行路径冗长、推理开销高昂。
- - **可靠性与累积误差问题**：在复杂操作中，大语言模型的幻觉或对界面状态的误读会引发累积错误，降低任务成功率和系统可靠性。
- ### 机制流程
MAS-Bench 中一个典型任务的执行流程可概括为以下四个步骤：
1.
- **任务解析与规划**：智能体接收自然语言任务指令，基于当前屏幕截图和指令内容进行理解，制定初步执行计划。对于混合智能体，此阶段还需判断哪些子任务适合通过快捷方式完成。
- ### 总体性能对比
在全部 139 项任务上使用预定义快捷方式知识库的实验结果（Table 2）揭示了四个关键发现：
1.
- **混合操作显著提升成功率与效率**：以 Gemini-2.5-Pro 为基座的 MAS-MobileAgent 相比纯图形用户界面的 MobileAgentV2，成功率从百分之三十五点二提升至百分之六十三点三，相对提升百分之七十九点八；成功任务的平均步数比率下降百分之三十八点九，效率提升明显。

## Wiki Connections

- Concepts: [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
