# AgentDropout 深度阅读笔记

## 核心信息

- 标题: AgentDropout: Dynamic Agent Elimination for Token-Efficient and High-Performance LLM-Based Multi-Agent Collaboration
- 作者: Zhexuan Wang, Yutong Wang, Xuebo Liu, Liang Ding, Miao Zhang, Jie Liu, Min Zhang
- 年份: 2025
- 会议/期刊: Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)
- DOI: 10.18653/v1/2025.acl-long.1170
- 论文链接: http://arxiv.org/abs/2503.18891v1
- 代码链接: https://github.com/wangzx1219/AgentDropout
- arXiv ID: 2503.18891

## 原文摘要翻译

基于大型语言模型的多智能体系统在协作问题解决中展现了显著潜力。然而，它们仍面临通信效率低下和任务性能不佳的重大挑战，这使得对智能体通信拓扑的精心设计尤为重要。受高效团队中角色常被动态调整这一管理理论启发，我们提出了AgentDropout，该方法通过优化通信图的邻接矩阵来识别不同通信轮次中的冗余智能体和冗余通信，并将其消除，以同时提升token效率和任务性能。与现有最优方法相比，AgentDropout平均减少了21.6%的提示词token消耗和18.4%的补全token消耗，同时任务性能提升了1.14。此外，扩展实验表明AgentDropout具有显著的领域迁移能力和结构鲁棒性，证明了其可靠性与有效性。我们在以下地址公开了代码：https://github.com/wangzx1219/AgentDropout。

## 创新点

1. **动态角色消除机制**：不同于现有方法在所有通信轮次中采用固定智能体集合和统一剪枝策略，AgentDropout首次将团队中角色应随任务动态调整的管理学思想引入多智能体通信优化，实现了按轮次动态剔除低贡献智能体的Node Dropout机制。这使得系统能在不同推理阶段灵活配置参与者，而非维持静态拓扑。

2. **节点与边联合Dropout**：论文提出了Node Dropout与Edge Dropout的组合策略。Node Dropout基于学习到的边权重计算节点度并淘汰低贡献智能体；Edge Dropout进一步剪除轮内和轮间冗余通信边。两者协同作用，在降低token消耗的同时避免了单一剪枝策略可能带来的信息瓶颈。

3. **基于少量样本的拓扑学习**：AgentDropout仅需数十条训练样本即可优化通信图的邻接矩阵参数，随后将学习到的矩阵应用于dropout过程。这一特性使得拓扑优化成本极低，且为后续的领域迁移实验奠定了基础，训练好的邻接矩阵可直接迁移到同类任务上。

4. **在token效率与任务性能上同时取得提升**：与当时最优的AgentPrune相比，AgentDropout不仅在Llama3-8B、Qwen2.5-72B、Deepseek-V3-671B三个量级模型上均取得更高准确率，还将提示词token和补全token分别平均降低21.6%和18.4%，打破了多智能体协作必然伴随高token开销的固有印象。

## 一句话总结

AgentDropout通过少量样本学习通信图邻接矩阵，并在每轮对话中动态执行节点淘汰与边剪枝，从而在降低多智能体系统token消耗的同时提升协作推理性能。

## 研究问题

当前基于大语言模型的多智能体系统虽然在数学推理、代码生成等任务上展现了超越单智能体的潜力，但普遍存在两个核心问题：

- **通信效率低下**：多轮对话中智能体频繁生成消息并互相传递，导致prompt token和completion token开销巨大，实际部署成本高昂。
- **静态角色约束**：现有方法如AgentPrune虽然通过可训练的图掩码剪除了部分冗余边，但参与每一轮讨论的智能体角色集合固定不变，只能应用跨轮次的统一剪枝策略，限制了系统在效率和性能上的进一步提升。

论文将多智能体协作类比为人类团队决策，指出高效团队会根据任务需求动态调整成员职责。由此出发，作者试图回答：能否在多智能体系统的每一轮通信中动态调整参与智能体及其连接关系，在保证甚至提升任务性能的前提下显著压缩token消耗？

> [!figure] Fig. 1: An overview of AgentDropout, in comparison with vanilla MAS and AgentPrune (Zhang et al., 2025), highlighting its dynamic adjustments of participant roles in each discussion to enhance cooperation effectiveness and efficiency.
> 建议位置：研究问题 / 方法主线
> 放置原因：直观对比了vanilla MAS、AgentPrune与AgentDropout在角色动态调整上的差异，帮助理解研究动机
> 当前状态：占位符

## 数据与任务定义

### 数据集
实验覆盖了推理、数学和代码生成三类任务：
- **通用推理**：MMLU
- **数学推理**：GSM8K、MultiArith、AQuA、SVAMP
- **代码生成**：HumanEval

### 基线方法
- **单智能体**：Vanilla（直接推理）、Chain-of-Thought（CoT）
- **多智能体单轮**：MASround=1（仅轮内通信的单轮对话）
- **多智能体多轮**：MASround=T（多轮轮内加轮间通信）、AgentPrune（与AgentDropout同样基于MASround=T优化，是最直接的对比基线）

### 评估指标
- **性能指标**：各数据集上的准确率，并报告跨数据集平均值。
- **效率指标**：Prompt token和Completion token数量，分别衡量输入提示长度和智能体生成输出的总长度。

### 模型与实现
实验在三个不同规模的模型上进行：
- Meta-Llama3-8B-Instruct
- Qwen2.5-72B-Instruct
- Deepseek-V3-671B-Instruct

Llama3和Qwen2.5使用vllm在Nvidia A800 GPU上推理；Deepseek-V3通过官方API调用。温度参数设为1。

## 方法主线

AgentDropout的核心思想是将多智能体通信建模为图，并通过可学习的邻接矩阵权重识别冗余节点和边，在推理阶段执行动态淘汰。整个流程分为拓扑学习与推理执行两个阶段。

### 图形式化

将多智能体系统表示为通信图：

$$G = (V, E, F)$$

其中节点集合 $V$ 包含全部智能体，边集合 $E$ 包含轮内通信边与轮间通信边，映射集合 $F$ 描述各智能体的推理函数。

全局图结构可展开为：

$$G = (V, E, F), \quad V = \bigcup_t V^{(t)}, \quad E = \left(\bigcup_t E^{(t)}_{\text{intra}}\right) \cup \left(\bigcup_t E^{(t)}_{\text{inter}}\right)$$

论文定义通信冗余如下：若子图满足

$$G_{\text{sub}} = (V, E', F), \quad E' \subseteq E, \quad \mu(G_{\text{sub}}) \geq \mu(G)$$

则称被剪除的边和节点为冗余，度量函数 $\mu(\cdot)$ 代表任务性能。

### 机制流程

1. **准备与权重学习**：输入初始通信图与少量样本，更新邻接矩阵参数并提取高贡献边权重信息，输出优化后的加权邻接矩阵。  
   **输入**：初始通信图、来自当前任务训练集或验证集的数十条样本。  
   **操作**：将通信图转换为可学习的加权邻接矩阵集合。轮内连接权重与轮间连接权重分别用两个矩阵表示，元素取值在0到1之间。利用少量样本端到端更新这些矩阵参数，提取高贡献边的权重信息，使重要连接获得更高权重。具体而言，每次前向传播后根据任务损失回传梯度，更新邻接矩阵中的可学习元素。

2. **节点淘汰（Node Dropout）**：输入优化后的邻接矩阵，提取节点贡献度并移除低贡献智能体，输出每轮更新后的节点集合。  
   **输入**：优化后的邻接矩阵。  
   **操作**：基于边权重计算各节点在每一轮的度，提取节点贡献度排序，识别对当前任务贡献最小的智能体节点，并按轮次将其从通信图中移除。例如，若某智能体在多轮中的加权入度持续低于阈值，则该智能体在对应轮次被静默。这使得不同轮次可以保留不同的智能体子集，模拟人类团队中不同阶段由不同成员主导的协作模式。

3. **边剪枝（Edge Dropout）**：输入经节点淘汰后的图结构，提取 Top-k 边并压缩通信图，输出稀疏化后的邻接矩阵。  
   **输入**：经节点淘汰后的剩余图结构。  
   **操作**：对轮内和轮间邻接矩阵分别执行TopkEdges操作，仅提取权重最高的前k条边，其中k由边dropout率控制。该步骤进一步剪除冗余连接，生成更稀疏的邻接矩阵。与节点淘汰不同，边剪枝不改变参与者集合，而是精简它们之间的信息流。

4. **DAG采样与协作推理**：输入测试查询与稀疏化矩阵，融合各智能体输出得到最终预测答案。  
   **输入**：测试查询、稀疏化后的邻接矩阵。  
   **操作**：使用DAGSample从优化后的邻接矩阵中采样得到最终通信有向无环图。各智能体按照该拓扑进行多轮通信：每轮中智能体接收来自其入边邻居的输出集合，聚合各方信息并生成自身输出。最终融合所有智能体回答得到预测结果。

## 关键结果

### 性能对比
AgentDropout在全部六个基准和三种模型规模上均优于单智能体CoT和多智能体基线。以Llama3-8B为例：

| 方法 | MMLU | GSM8K | AQuA | MultiArith | SVAMP | HumanEval | 平均 |
|------|------|-------|------|------------|-------|-----------|------|
| Vanilla | 53.59 | 70.23 | 41.67 | 91.11 | 75.00 | 53.33 | 64.16 |
| CoT | 56.86 | 70.47 | 43.75 | 92.25 | 76.17 | 54.17 | 65.61 |
| MASround=T | 60.13 | 71.48 | 45.41 | 90.56 | 77.56 | 49.17 | 65.72 |
| AgentPrune | 60.78 | 71.02 | 47.22 | 90.00 | 78.34 | 51.67 | 66.51 |
| **AgentDropout** | **62.75** | **73.13** | **47.78** | **92.59** | **80.11** | **55.84** | **68.70** |

关键数字：
- 在Llama3-8B上，AgentDropout平均准确率68.70，较AgentPrune提升2.19，较MASround=T提升2.98。
- 在Qwen2.5-72B上，平均准确率91.58，较AgentPrune提升0.77。
- 在Deepseek-V3-671B上，平均准确率93.72，较AgentPrune提升0.47。

一个值得注意的现象是：当模型能力较弱时（如Llama3），单智能体CoT带来的性能增益相对显著；而多智能体交互方法（MAS、AgentPrune）的增益波动较大。AgentDropout在弱模型上依然取得了最大的绝对提升（在MMLU上相较Vanilla提升9.16），说明其拓扑优化对弥补单智能体能力短板具有实际价值。

### Token消耗对比
在Llama3模型上，AgentDropout在全部六个数据集上均实现了token消耗的降低：
- **Prompt token**：从MASround=T的约160万到470万降至AgentDropout的约110万到330万；
- **Completion token**：从MASround=T的约39万到100万降至AgentDropout的约33万到84万。

与AgentPrune相比，AgentDropout在GSM8K上将prompt token从1500万降至1200万，在HumanEval上将completion token从465K降至359K。整体平均来看，AgentDropout减少了21.6%的prompt token和18.4%的completion token。

### 结构鲁棒性
论文测试了三种初始通信拓扑：全连接图、分层图和随机图。结果表明：无论以何种拓扑初始化，AgentDropout均一致地提升性能并降低token消耗。例如在全连接初始化下AgentDropout平均准确率为68.70、prompt token约330万、completion token约839K；分层图初始化下为68.19、270万、834K；随机图初始化下为66.31、340万、100万。虽然随机初始化的绝对性能略低，但AgentDropout相对各自基线的提升趋势保持一致，验证了方法对初始结构不敏感。

> [!figure] Table 1: Performance comparison between AgentDropout and other baseline reasoning techniques. Edge DR. and Node DR. represent the Edge Dropout and Node Dropout methods, respectively.
> 建议位置：关键结果
> 放置原因：承载主实验性能结果，直接支撑性能提升核心结论
> 当前状态：占位符

> [!figure] Table 2: Token consumption comparison in the Llama model. Ptok. denotes the number of prompt tokens for the agents, while Ctok. represents the number of completion tokens generated by the agents.
> 建议位置：关键结果
> 放置原因：量化token效率增益，是论文核心贡献之一
> 当前状态：占位符

> [!figure] Table 3: Performance and average token consumption achieved with different initial communication graph topological structures.
> 建议位置：关键结果
> 放置原因：证明AgentDropout对初始拓扑不敏感，增强方法可信度
> 当前状态：占位符

## 深度分析

### Dropout率的影响
论文系统分析了边dropout率对性能与token消耗的权衡。以Llama3为例：

| Dropout率 | 平均准确率 | Prompt token | Completion token |
|-----------|-----------|--------------|------------------|
| 0.8 | 66.01 | 856K | 230K |
| 0.6 | 66.25 | 130万 | 434K |
| 0.4 | 66.48 | 190万 | 648K |
| 0.2 | 68.70 | 330万 | 839K |

趋势非常清晰：dropout率越高，图越稀疏，token消耗越低，但性能随之下降；dropout率0.2时取得最佳性能68.70，但token开销最高。这说明通信图中确实存在大量冗余边，但过度剪枝会切断关键信息传递路径。实际部署中可根据预算选择不同dropout率，0.4到0.6区间似乎是一个性能与成本较优的平衡点。

### 消融实验：策略组合与随机淘汰
论文对比了单独使用Node Dropout、单独使用Edge Dropout、两者联用（AgentDropout）以及随机淘汰策略：
- 单独Node Dropout或Edge Dropout均能带来相对vanilla MAS的提升；
- 两者联用（AgentDropout）取得最优性能（68.70）；
- 在AgentDropout框架内随机淘汰节点或边均导致性能下降。

这表明：简单的稀疏化不足以保证性能，必须基于学习到的权重进行有选择的淘汰；Node Dropout与Edge Dropout具有互补性，前者解决谁参与的问题，后者解决谁与谁通信的问题。

### 领域迁移性
论文使用不同数据集组合训练邻接矩阵并在另一数据集上测试。核心发现：
- 当训练集与测试集同领域时（如均在数学数据集上），迁移效果最佳；
- 在更具挑战性的AQuA上训练后，跨域平均性能提升达1.59；
- 在较简单的MultiArith上训练后，跨域平均提升为0.81。

作者建议：将AgentDropout应用于少样本场景时，应选择与目标任务相似的数据集进行拓扑训练。这一结论进一步验证了邻接矩阵学习到的并非数据集特定技巧，而是具有一定泛化性的协作模式。

### 与AgentPrune的本质差异
AgentPrune仅剪边且所有轮次共享同一剪枝掩码，相当于在全局图上做静态稀疏化。AgentDropout则引入了轮次维度的动态性：不同轮次可以保留不同的智能体子集（Node Dropout），且边剪枝也基于学习到的动态权重（Edge Dropout）。从实现角度看，AgentDropout需要为每一轮维护独立的邻接矩阵参数，参数量和优化复杂度略高于AgentPrune，但由于训练样本仅需数十条，实际开销可控。

> [!figure] Fig. 2: The overall process of AgentDropout. The first and second rows present Node Dropout and Edge Dropout procedures, respectively. The third row illustrates the cooperative reasoning process for both intra- and inter-round communication, as well as the generation of the final answer.
> 建议位置：深度分析
> 放置原因：详细展示了Node Dropout、Edge Dropout与多轮协作推理的完整流程，辅助理解技术实现细节
> 当前状态：占位符

> [!figure] Table 4: Impact of varying dropout rates on the performance and average token consumption of AgentDropout.
> 建议位置：深度分析
> 放置原因：展示性能与token效率的核心权衡，是部署决策的关键依据
> 当前状态：占位符

> [!figure] Table 5: Performance achieved with different dropout strategies. For Random Dropout, checkmark denotes the random dropout strategy is applied to the marked dropout step, while the dropout strategy in the other step remains unchanged, as per AgentDropout.
> 建议位置：深度分析
> 放置原因：消融实验，证明基于学习权重的淘汰优于随机淘汰
> 当前状态：占位符

> [!figure] Table 6: Performance comparison using different combinations of training and test sets. The row headers indicate the training set used for graph topology learning, and the column headers represent the test set.
> 建议位置：深度分析
> 放置原因：验证领域迁移能力，说明拓扑学习的泛化性
> 当前状态：占位符

## 局限

论文作者在结论部分明确指出了以下不足：

1. **任务范围有限**：验证任务主要集中在常规推理、数学推理和代码生成三类，缺乏对更开放域、多模态或长程规划任务的评估。AgentDropout在这些场景中的有效性尚未得到证明。

2. **依赖预定义角色与提示词**：当前框架仍然受限于人工预设的智能体角色和系统提示词。当面对全新领域任务时，仍需仔细设计新的初始角色和提示模板，未能实现完全自动化的角色配置。

3. **Token消耗仍偏高**：尽管AgentDropout显著降低了MAS的token使用量，但相比单智能体方法如CoT，多智能体协作的绝对token开销仍然很大，存在进一步优化空间。

4. **未充分探索自动角色设计**：作者建议未来工作可结合自动角色与提示词设计方法，以增强系统灵活性。这暗示当前方法在高度动态或未知任务环境下的自适应性不足。

## 我的笔记

1. **管理学启发的技术迁移值得注意**：将Locke和Kozlowski关于团队动态角色分配的管理学理论引入多智能体系统优化，是一次跨学科视角的成功尝试。它提示我们，人类组织行为学中关于协作效率的成熟结论，可能为大规模智能体系统设计提供新的启发式。

2. **少样本学习拓扑是一个实用亮点**：仅需数十条样本即可训练出有效的通信拓扑，这意味着AgentDropout在实际业务场景中具有快速部署潜力。企业无需为维护多智能体系统准备大量标注数据，只需利用现有验证集即可优化协作结构。

3. **Node Dropout的意义被低估**：现有工作包括AgentPrune过度关注谁与谁通信的边优化，而忽略了谁应该参与的节点优化。AgentDropout证明，在多轮推理中让不同智能体按轮次动态入场和退场，不仅能省token，还能通过减少噪声参与者来提升决策质量。这一思路可延伸至更复杂的层级架构或多阶段工作流设计。

4. **与当前研究的关联**：近期多智能体研究热点包括AutoGen、MetaGPT等框架，它们强调角色专业化与工作流编排。AgentDropout可被视为这些框架的后端优化器，在角色和工作流确定后，进一步通过数据驱动的方式精简执行路径。未来若将AgentDropout与自动角色生成机制结合，可能实现从角色设计到执行拓扑的全链路自动化优化。

5. **对多智能体经济学的启示**：token消耗直接对应API调用成本。AgentDropout在Llama3上将部分任务的prompt token从1600万降至1200万，completion token从714K降至594K，这种量级降低对于高频部署场景具有显著经济意义。随着模型规模扩大，动态拓扑优化可能从性能优化手段演变为成本控制刚需。

## 引用

- Wang, Zhexuan; Wang, Yutong; Liu, Xuebo; Ding, Liang; Zhang, Miao; Liu, Jie; Zhang, Min. AgentDropout: Dynamic Agent Elimination for Token-Efficient and High-Performance LLM-Based Multi-Agent Collaboration. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2025.
- DOI: 10.18653/v1/2025.acl-long.1170
- arXiv: 2503.18891
- 代码: https://github.com/wangzx1219/AgentDropout
