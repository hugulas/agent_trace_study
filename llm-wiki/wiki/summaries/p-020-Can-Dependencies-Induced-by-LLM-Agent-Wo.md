# Can Dependencies Induced by LLM-Agent Workflows Be Trusted?

## Source

- Raw note: `raw/notes/p-020_Can_Dependencies_Induced_by_LLM-Agent_Wo.md`
- Metadata: not available in note

## Compiled Summary

LLM-agent 系统通常将高层目标分解为子任务依赖图，并假设每个子任务的输出是可靠的，且在其他子任务给定其父节点响应的条件下条件独立。然而，这一假设在执行过程中经常失效，因为真实响应不可获取，导致智能体间失序——即由智能体之间的不一致和协调崩溃引发的失败。为解决该问题，本文提出 SeqCV，一种在条件独立性假设被违反时仍能保证可靠执行的动态框架。SeqCV 按顺序执行子任务，每个子任务都以所有先前已验证的响应为条件，并在智能体生成短令牌序列后立即执行一致性检查。在每个检查点，只有当令牌序列代表了跨多种大语言模型一致支持的共享知识时才被接受；否则将其丢弃，并触发递归子任务分解以获得更细粒度的推理。尽管 SeqCV 采用顺序执行，它

## Evidence Notes

- 本文围绕以下核心问题展开：
- 在基于有向无环图的多智能体编排系统中，为什么理论上假设的子任务响应条件独立性在实际执行中难以成立？
- 当条件独立性被违反时，隐藏依赖如何导致智能体间失序，进而引发不一致或协调崩溃？
- 如何设计一种执行框架，在不牺牲端到端效率的前提下，保证每个子任务输出在流入下游之前已被可靠验证？
传统图式编排系统假设每个子任务的输出仅依赖于其父节点输出，且与其他节点条件独立。然而，由于大语言模型生成的是近似响应而非真实响应，图中存在至少一条路径使得不同子任务输出在给定父节点的情况下仍然保持依赖关系。这一结构性矛盾是智能体间失序的根源。
- ![Fig.
- SeqCV 的核心设计思想是：既然条件独立性无法保证，就显式地将每个子任务条件化为全部已验证响应的历史，并通过早期验证与动态拆分将错误控制在最小粒度。
- ### 机制流程
SeqCV 的执行管线可归纳为以下四个核心步骤：
1.
- ### 主实验结果
Table 1 展示了 SeqCV 与基线在七个任务上的平均表现。SeqCV 在三项指标上均取得最高分，平均总分达到 88%，显著优于所有对比方法。
- **Table 1 各方法在七个 agentic 任务上的平均性能**
| Method | HR | ES | CA | AVG |
|--------|----|----|----|-----|
| Atom | 26% | 40% | 30% | 29% |
| AFlow | 36% | 30% | 40% | 36% |
| Flow | 56% | 70% | 40% | 58% |
| o4-mini-high | 81% | 100% | 70% | 82% |
| **SeqCV** | **83%** | **100%** | **100%** | **88%** |
SeqCV 相比 o4-mini-high 

## Wiki Connections

- Concepts: [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
