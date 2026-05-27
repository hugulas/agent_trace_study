# SWE-Chain: Benchmarking Coding Agents on Chained Release-Level Package Upgrades

## Source

- Raw note: `raw/notes/swechain_note.md`
- Metadata: not available in note

## Compiled Summary

由大语言模型驱动的编码智能体日益被期望执行超越孤立问题修复的真实软件维护任务。现有基准测试已逐步转向逼真的软件演化场景，但它们很少以软件包发布的粒度来捕捉持续维护过程。在这个粒度上，变更被打包、发布并被后续版本继承。

## Evidence Notes

- 本文提出 SWE-Chain，一个用于评估智能体在链式发布级软件包升级任务上的基准测试，其中每一次版本过渡都建立在智能体此前修改过的代码库之上。为了生成升级规格说明，作者设计了一套分治式合成管线，将每个版本过渡对应的发布说明与代码差异进行对齐，从而确保需求基于实际代码变更、对智能体具有信息量且可实际实现。
- 随着大语言模型编码智能体从孤立任务走向仓库级操作，评估范式也从任务级问题演进到真实项目问题修复。然而，一个关键缺口始终存在：现有基准的任务边界与上游维护者实际发布软件版本的时机不对齐。
- 具体而言，SWE-CI 使用基准自选的基础到目标提交对，SlopCodeBench 使用合成检查点，EvoClaw 从提交历史重建里程碑。这些分段方式虽然揭示了迭代代码退化和持续集成式可维护性的失败，却未触及发布边界处的真实维护动力学。SWE-EVO 首次将发布版本作为评估单元，但其任务仍是孤立的端到端过渡，规格由发布说明与代码仓库问题原始内容拼接而成，充斥着终端输出和图像引用等噪声，且无法评估智能体能否在自身修改的基础上持续维护代码库。
- SWE-Chain 的核心方法论包含两部分：一是 DecompSynth 分治式规格合成管线，用于从发布说明与代码差异中生成结构化、有依据且可实施的升级规格；二是顺序版本升级评估协议，用于在链式场景下公平评估智能体的维护能力。
- > [!figure] Fig.

## Wiki Connections

- Concepts: [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
