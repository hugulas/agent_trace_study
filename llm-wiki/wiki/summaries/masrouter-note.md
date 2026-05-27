# MasRouter: 面向多智能体系统的大语言模型路由学习

## Source

- Raw note: `raw/notes/masrouter_note.md`
- Metadata: not available in note

## Compiled Summary

由大语言模型驱动的多智能体系统在拓展大语言模型能力边界方面已展现出显著成效，但它们往往带来高昂的计算开销，并且在动态选择大语言模型时面临挑战。现有的大语言模型路由方法通过在单智能体场景中为每个查询定制化地选择模型，有效降低了推理成本，却忽视了多智能体系统中协作模式和智能体角色的关键决策。针对这一挑战，本文首次提出了多智能体系统路由问题，将多智能体系统的所有组件整合到一个统一的路由框架中。为此，我们提出了 MasRouter，这是首个兼具高性能、经济性和归纳性的多智能体系统路由解决方案。MasRouter 通过级联控制器网络依次完成协作模式判定、角色分配和大语言模型路由，逐步构建一个兼顾效果与效率的多智能体系统。大量实验表明，MasR

## Evidence Notes

- 大语言模型智能体在代码生成、数学推理和具身行动等任务中取得了显著进展。随着可用模型池不断扩大，如何为单个智能体选择最合适的大语言模型已成为研究热点。现有工作如 PromptLLM、RouteLLM、FrugalGPT 和 RouterDC 等，通过在查询级别路由到最优模型，有效降低了单智能体系统的推理成本。然而，这些方法仅解决了一个相对简单的问题：给定一个查询，选一个模型。
- 多智能体系统（MAS）的场景远比单智能体复杂。一个有效的多智能体系统需要同时解决三个层面的决策：
- **协作模式判定**：根据任务复杂度选择链式、树状、图状或辩论等通信拓扑；
- **角色分配**：为不同智能体分配合适的专业角色（如程序员、数学家、物理学家）；
- **模型路由**：为每个智能体分配最擅长其任务域的大语言模型。
- ### 问题形式化
给定模型池 M、预定义角色集 R 和协作模式集 T，一个多智能体系统 S 可表示为三元组：
$$S = \{M_i\}_{i=1}^k, \{R_i\}_{i=1}^k, T$$
其中 k 为智能体数量，$M_i$ 取自模型池 M，$R_i$ 取自角色集 R，$T$ 取自协作模式集 T。MASR 的目标是学习一个查询到多智能体系统的映射：
$$f: M \times R \times T \longrightarrow S$$
使得在查询 Q 上生成的答案正确概率最大化，同时控制推理成本。
- ### 级联控制器网络
MasRouter 的核心是三个级联的控制器模块，它们依次缩小搜索空间：
1.
- **主实验结果**。MasRouter 在 MMLU、GSM8K、MATH、HumanEval 和 MBPP 五个数据集上的平均表现优于所有基线：
- 相比现有最优的单智能体路由方法 RouterDC，MasRouter 在五个数据集上平均提升 **3.51%**；
- 在 MBPP 数据集上，MasRouter 比动态多智能体方法 AgentPrune 提升 **8.20%**（pass@1），比 AFlow 提升 **1.80%**；
- 在 HumanEval 上，MasRouter 将推理开销从 RouterDC 的约 0.363 美元降至约 0.185 美元，降幅达 **52.07%**。
- **与现有 MAS 框架的即插即用集成**。MasRouter 可作为插件接入 MAD 和 MacNet：
- 接入 MAD 后，在 HumanEval 上性能提升 **1.55%**（pass@1），成本降低 **17.21% 至 28.17%**；
- 接入 MacNet 后，在 MMLU 上性能提升 **0.36%**，成本降低约 **30.6%**（从 8.482 美元降至 5.892 美元）；
- 在更大规模数据集上，接入 MAD 后在 MMLU 上节省推理成本 **6.17 至 7.63 美元**。

## Wiki Connections

- Concepts: [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
