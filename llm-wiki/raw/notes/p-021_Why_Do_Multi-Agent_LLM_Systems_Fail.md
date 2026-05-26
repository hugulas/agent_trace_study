---
tags:
  - MAS
  - multi-agent
  - failure-analysis
  - taxonomy
  - dataset
  - NeurIPS2025
aliases:
  - MAST
  - MAST-Data
  - p-021
date: 2025-05-25
arxiv_id: "2503.13657"
---

# Why Do Multi-Agent LLM Systems Fail?

## 核心信息

- **标题**: Why Do Multi-Agent LLM Systems Fail?
- **作者**: Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Keutzer, Aditya Parameswaran, Dan Klein, Kannan Ramchandran, Matei Zaharia, Joseph E. Gonzalez, Ion Stoica
- **年份**: 2025
- **来源**: NeurIPS 2025 Track on Datasets and Benchmarks
- **arXiv**: 2503.13657
- **PDF**: `[p-021]-why-do-multi-agent-llm-systems-fail.pdf`
- **证据质量**: high

## 原文摘要翻译

尽管多智能体大语言模型系统（MAS）受到了广泛关注，但它们在主流基准测试上的性能提升往往十分有限。
这一差距凸显了从原理层面理解 MAS 为何失败的迫切需求。
回答该问题需要系统性地识别和分析失败模式。
本文提出 MAST-Data，一个涵盖 1600 余条标注轨迹的综合数据集，采集自 7 个主流 MAS 框架。
MAST-Data 是首个用于刻画 MAS 失败动力学并指导未来系统改进的多智能体数据集。
为实现对 MAST-Data 中失败的系统分类，本文构建首个多智能体系统失败分类法 MAST。
研究者通过对 150 条轨迹进行严格分析，在专家人工标注员的密切参与下，以高标注者间一致性（$\kappa = 0.88$）进行验证，最终识别出 14 种独特失败模式，聚类为 3 大类：（i）系统设计问题、（ii）智能体间失配、（iii）任务验证。
为实现可扩展标注，本文还开发了一套 LLM-as-a-Judge 流水线，其与人工标注具有高度一致性。
研究利用 MAST 与 MAST-Data 分析了跨模型与跨任务的失败模式。
所涉模型包括 GPT-4、Claude 3、Qwen2.5、CodeLlama；任务涵盖编程、数学与通用智能体场景。
结果表明，通过更好的 MAS 设计仍存在显著改进空间。
分析结果揭示，已识别的失败需要更复杂的解决方案，为未来研究指明了清晰路线图。
本文已公开发布 MAST-Data 数据集、MAST 分类法及 LLM 标注器。

## 创新点

1. **首个 MAS 失败分类法 MAST**：基于扎根理论对 150 条轨迹进行严格分析，经三轮标注者间一致性迭代，最终得到 14 种细粒度失败模式，归并为 3 大类别，并达到 $\kappa = 0.88$ 的高一致性。
2. **首个大规模 MAS 失败数据集 MAST-Data**：涵盖 1642 条来自 7 个主流框架的标注轨迹，覆盖编程、数学解题与通用智能体任务，并包含多模型家族（GPT-4 系列、Claude 系列、Qwen2.5、CodeLlama）。
3. **可扩展的 LLM-as-a-Judge 标注流水线**：基于 OpenAI o1 模型构建，经少量样本校准后，在留出集上达到 94% 准确率与 $\kappa = 0.77$，且在两个未见过的框架与基准上泛化得到 $\kappa = 0.79$。
4. **超越模型能力的系统设计洞察**：通过干预实验表明，仅改进系统工作流与提示设计，在使用相同底层模型的情况下，任务成功率可提升最高 15.6%，证明大量失败根因在于系统设计而非单模型能力。

## 一句话总结

本文通过构建首个经验驱动的 MAS 失败分类法 MAST 与大规模标注数据集 MAST-Data，系统揭示了当前多智能体系统 41%–86.7% 高失败率的 14 种根因，并证明这些失败主要源于系统设计缺陷而非底层 LLM 局限，为未来 MAS 的可靠性改进提供了标准化语言与实证基础。

## 研究问题

近年来，基于 LLM 的智能体系统在软件工程、药物发现、科学模拟与通用智能体等领域迅速兴起。
多智能体系统通过任务分解、并行化执行、上下文隔离、专用模型集成与多样化推理讨论来协同工作。
然而，现有研究表明，MAS 在主流基准上的性能增益往往微乎其微，甚至不及单智能体框架或简单的 best-of-N 采样基线。
作者对 7 个开源 SOTA MAS 进行实证分析，发现其失败率高达 41% 至 86.7%。
更关键的是，社区目前对如何构建鲁棒可靠的 MAS 缺乏共识。

基于上述背景，本文提出并回答核心问题：Why do MAS fail?
研究将失败定义为 MAS 未能达成其预期任务目标的实例。
为系统回答该问题，作者认为必须解决两大挑战：
（1）MAS 失败的根因往往涉及复杂的智能体交互与复合效应，难以像传统软件那样直接定位。
（2）当前缺乏标准化的失败定义框架，导致跨系统比较与标注不一致。

## 数据与任务定义

### 数据来源与规模

本文构建的数据集 MAST-Data 共包含 1642 条标注执行轨迹，采集自 7 个主流 MAS 框架。
这些框架包括 ChatDev、MetaGPT、HyperAgent、AppWorld、AG2 与 OpenManus。
另外还包含 Magentic-One。
轨迹覆盖编程、数学解题以及通用智能体任务。
具体基准包括 ProgramDev、SWE-Bench Lite、GSM-Plus、OlympiadBench 与 MMLU。
此外还涵盖 GAIA 与 AppWorld Test-C。
模型家族涵盖 GPT-4 系列、Claude-3.7-Sonnet、Qwen2.5-Coder-32B-Instruct 与 CodeLlama-7b-Instruct。

Table 1 来自 LaTeX 源码 `08-mad-tab.tex`，汇总了 MAST-Data 的配置细节：

| MAS | Benchmark | LLM | Annotation | Trace # |
|-----|-----------|-----|------------|---------|
| ChatDev | ProgramDev | GPT-4o | HE, HA, LA | 30 |
| MetaGPT | ProgramDev | GPT-4o | HE, HA, LA | 30 |
| HyperAgent | SWE-Bench Lite | Claude-3.7-Sonnet | HE, HA, LA | 30 |
| AppWorld | Test-C | GPT-4o | HE, HA, LA | 30 |
| AG2 (MathChat) | GSM-Plus | GPT-4 | HE, HA, LA | 30 |
| Magentic-One | GAIA | GPT-4o | HE, HA, LA | 30 |
| OpenManus | ProgramDev | GPT-4o | HE, HA, LA | 30 |
| ChatDev | ProgramDev-v2 | GPT-4o | LA | 100 |
| MetaGPT | ProgramDev-v2 | GPT-4o | LA | 100 |
| MetaGPT | ProgramDev-v2 | Claude-3.7-Sonnet | LA | 100 |
| ChatDev | ProgramDev-v2 | Qwen2.5-Coder-32B-Instruct | LA | 100 |
| MetaGPT | ProgramDev-v2 | Qwen2.5-Coder-32B-Instruct | LA | 100 |
| ChatDev | ProgramDev-v2 | CodeLlama-7b-Instruct-hf | LA | 100 |
| MetaGPT | ProgramDev-v2 | CodeLlama-7b-Instruct-hf | LA | 100 |
| AG2 (MathChat) | OlympiadBench | GPT-4o | HE, LA | 206 |
| AG2 (MathChat) | GSMPlus | Claude-3.7-Sonnet | HE, LA | 193 |
| AG2 (MathChat) | MMLU | GPT-4o-mini | HE, LA | 168 |
| Magentic-One | GAIA | GPT-4o | HE, LA | 165 |

其中 HE 表示人工评估任务完成率，HA 表示人工标注失败模式，LA 表示 LLM-as-a-Judge 标注失败模式。
此外，研究还发布了 MAST-Data-human，包含 21 条由三位专家各自独立标注的轨迹，用于标注者间一致性研究。

### 任务定义

本文的核心任务是失败模式识别与分类。
对每一条 MAS 执行轨迹，标注员需要判断其是否发生失败，并将失败归因到 MAST 分类法中的具体模式。
失败被统一界定为：MAS 未能实现其预期任务目标。
该定义避免了因系统差异导致的判断偏差，使跨框架比较成为可能。

![Fig. 3 MAST-Data 轨迹片段示例](p-021_Why_Do_Multi-Agent_LLM_Systems_Fail/images/phone-agent-narrow.png)

上图展示了 MAST-Data 中一段典型轨迹片段，呈现了电话智能体与主管智能体之间的对话。
电话智能体未将 API 的用户名格式要求（应为手机号）传递给主管，而主管也未主动澄清，导致反复登录失败，最终任务失败。
该案例对应 MAST 中的失败模式 FM-2.4（信息隐瞒，Information Withholding）。

## 方法主线

本文的方法论围绕“如何从经验数据中系统提炼 MAS 失败模式”展开，分为四个阶段：

### 机制流程

1. 输入原始 MAS 执行轨迹，送入 Grounded Theory 定性分析流程，由 6 名专家进行开放式编码。
2. 提取观察到的失败行为，通过持续比较分析与理论化，编码为初步失败模式定义。
3. 生成标准化分类法 MAST，输出 14 种细粒度失败模式与 3 大类别，并经过三轮标注者间一致性迭代验证。
4. 得到可扩展的 LLM-as-a-Judge 标注流水线，将人类验证后的 MAST 定义与少量样本输入 o1 模型，输出大规模带标签的 MAST-Data 数据集，用于后续失败分析。

![Fig. 1 MAST 失败分类法全景](p-021_Why_Do_Multi-Agent_LLM_Systems_Fail/images/taxonomy_neurips_final_10_23_25.png)

![Fig. 2 MAST-Data 构建方法论流程](p-021_Why_Do_Multi-Agent_LLM_Systems_Fail/images/arxiv_figure_neurips_cropped.png)

### 扎根理论与 MAST 构建

为在无预设假设的前提下让失败模式自然涌现，研究团队采用扎根理论方法，对 150 条轨迹进行迭代分析。
具体技术包括：

- **理论抽样**：选择五个框架，覆盖编程与数学两类任务。
- **开放式编码**：逐条标记观察到的失败行为。
- **持续比较分析**：在不同系统间比较失败行为的共性与差异。
- **备忘录**：记录分析过程中的洞察。
- **理论化**：将观察结构化为初始失败模式集合。

当进一步分析不再产生新模式时，即达到理论饱和。
此阶段每位专家平均投入超过 20 小时。

### 标注者间一致性验证

从扎根理论得到的初步分类需经标准化才能用于大规模标注。
研究进行了三轮 IAA 迭代：每轮随机抽取 5 条轨迹，由 3 名专家独立标注，随后集体讨论解决分歧，并据此调整、合并或新增失败模式定义。
最终达到平均 $\kappa = 0.88$，证明 MAST 定义具有高度清晰度与共享可理解性。

### LLM-as-a-Judge 标注器

为将标注规模从数百条扩展至 1642 条，研究开发了基于 OpenAI o1 的 LLM 标注器。
输入为执行轨迹、MAST 定义与人类标注的少量样本，输出为该轨迹对应的失败模式及理由。
在留出测试集上，该标注器达到如下性能：

Table 2 来自 LaTeX 源码 `04_methodology.tex`：

| Model | Accuracy | Recall | Precision | F1 | Cohen's $\kappa$ |
|-------|----------|--------|-----------|----|------------------|
| o1 | 0.89 | 0.62 | 0.68 | 0.64 | 0.58 |
| o1 (few shot) | 0.94 | 0.77 | 0.833 | 0.80 | 0.77 |

加入少量样本后，各项指标显著提升，尤其 $\kappa$ 从 0.58 提升至 0.77，接近人类专家水平。
在泛化验证中，将该标注器直接应用于未见过的框架及新基准，人类 IAA 仍保持 $\kappa = 0.79$，证明 MAST 具有良好的跨系统迁移性。

## 关键结果

### 失败模式分布

基于 MAST-Data 中 210 条人工与 LLM 共同标注的轨迹，14 种失败模式的分布如下：

- **系统设计问题（FC1）**，占比 41.8%：
  - FM-1.1 违背任务规范（11.8%）
  - FM-1.2 违背角色规范（1.5%）
  - FM-1.3 步骤重复（15.7%）
  - FM-1.4 对话历史丢失（2.8%）
  - FM-1.5 未意识到终止条件（12.4%）

- **智能体间失配（FC2）**，占比 36.9%：
  - FM-2.1 对话重置（2.2%）
  - FM-2.2 未主动澄清（6.8%）
  - FM-2.3 任务偏离（7.4%）
  - FM-2.4 信息隐瞒（0.8%）
  - FM-2.5 忽略其他智能体输入（1.9%）
  - FM-2.6 推理与行动不匹配（13.2%）

- **任务验证（FC3）**，占比 21.3%：
  - FM-3.1 过早终止（6.2%）
  - FM-3.2 无验证或验证不完整（8.2%）
  - FM-3.3 验证错误（9.1%）

![Fig. 4 各系统失败模式分布](p-021_Why_Do_Multi-Agent_LLM_Systems_Fail/images/masft_bar.png)

上图按系统展示了失败模式的分布。
值得注意的是，不同框架的失败剖面差异显著：AppWorld 经常出现过早终止，可能与其星型拓扑与缺乏预定义工作流有关；OpenManus 倾向于步骤重复；HyperAgent 则受步骤重复与错误验证困扰。
这说明不存在“一刀切”的通用解决方案。

### 跨模型与跨架构比较

在 MetaGPT 框架下比较 GPT-4o 与 Claude 3.7 Sonnet 的编程任务表现时，GPT-4o 整体更优，且 FC1 失败减少 39%。
而在同一基准上比较 MetaGPT 与 ChatDev 时，前者在 FC1 与 FC2 上的失败比后者低 60%–68%。
但前者的 FC3 失败却是后者的 1.56 倍。
这揭示了模型选型与架构设计对失败分布的深刻影响。

### 七大系统失败率

![Fig. 5 七个主流 MAS 的失败率](p-021_Why_Do_Multi-Agent_LLM_Systems_Fail/images/multi_agent_systems_failure_rates.png)

上图汇总了使用 GPT-4o 与 Claude-3.7-Sonnet 时六个流行 MAS 的失败率。
失败率范围从 41.0%（MetaGPT + GPT-4o）到 86.7%（AG2 + Claude-3.7-Sonnet）不等，整体成功率普遍偏低。

### 干预实验效果

研究进行了两项小规模干预案例研究：

- **ChatDev 角色规范优化**：确保 CEO 智能体拥有最终决策权，消除 CPO 智能体擅自终止对话的问题。
  该工作流调整在使用相同底层模型与相同提示的情况下，将整体任务成功率提升了 +9.4%。
- **ChatDev 高层目标验证增强**：在现有代码级检查之上，增加对高层任务目标的验证步骤。
  该架构改动在 ProgramDev 上带来 +15.6% 的绝对成功率提升。

## 深度分析

### 系统设计的根本性作用

本文的核心论点之一是：MAS 失败不能简单归咎于当前 LLM 的固有限制（如幻觉或指令跟随能力不足）。
作者引用高可靠性组织与正常事故理论指出，即使由高度成熟的个体组成的组织，若结构设计存在缺陷，也可能发生灾难性失败。
同理，MAS 的失败很大程度上源于组织设计与智能体协调的挑战，而非单个智能体的能力局限。

这一观点得到干预实验的强有力支持：仅通过改进工作流与提示设计，在不更换底层模型的情况下，即可实现最高 15.6% 的绝对性能提升。
然而，即便经过优化，任务完成率仍然偏低，表明需要更根本性的结构重设计。

### 三大失败类别的深层含义

**FC1：系统设计问题** 中的 FM-1.1（违背任务规范）与 FM-1.2（违背角色规范）表面上像是通用的指令跟随失败，但作者识别出更深层的三个根因：

1. MAS 在智能体角色与工作流设计上的缺陷。
2. 用户提示规范质量差或模糊。
3. 底层 LLM 的能力限制。

作者认为，一个良好设计的 MAS 应该能够以最小但清晰的用户输入来理解高层目标，从而缓解后两点的影响。

**FC2：智能体间失配** 揭示了 MAS 中信息流的崩溃。
作者特别指出，即使智能体使用自然语言在同一框架内通信，仍然会出现信息隐瞒、输入被忽略、推理与行动不匹配等问题。
这表明问题超越了通信协议层面（如 MCP 或 A2A 所解决的标准化消息格式），而涉及更深层的“社会推理”能力——即智能体需要准确建模其他智能体的信息需求。
解决 FC2 可能需要结合架构改进与模型在交际智能方面的能力提升。

**FC3：任务验证** 凸显了当前验证机制的不足。
拥有显式验证器的系统（如 MetaGPT、ChatDev）总体失败数确实更少，但验证器并非万能。
许多验证器仅执行表面检查（如代码是否编译通过、是否遗留 TODO 注释），而未能验证更深层的正确性。
作者主张从传统软件开发中汲取经验，引入多级验证：既检查低级正确性（代码编译、单元测试），也检查高级目标满足度。

### MAST 作为实用开发工具

MAST 的价值不仅在于学术研究，更在于工程实践。
通过 LLM 标注器对执行轨迹进行定量失败分解，开发者可以：

- 识别系统中最频繁出现的失败模式，优先投入资源解决高影响区域；
- 在进行系统优化前后进行对照分析，超越聚合成功率的局限，精确理解“为什么”某项干预有效；
- 发现干预带来的潜在权衡（例如减少某类失败可能引入另一类失败）。

> [!figure] Table 3 到 Table 9 其他实验与消融表格
> 建议位置：深度分析
> 放置原因：原文附录中包含更多跨模型对比表、干预实验详细结果表、失败模式相关性热力表等，可进一步支撑定量分析。
> 当前状态：保留占位；核心结果已由 Table 1、Table 2 及 Figure 4、Figure 5 覆盖，其余表格可从附录继续补充。

## 局限

1. **非穷尽性**：作者明确声明 MAST 不声称覆盖所有潜在失败模式。
   随着 MAS 架构的持续演化，新的失败模式可能涌现，需要分类法的迭代扩展。
2. **聚焦正确性**：MAST 主要关注与任务正确性和完成度相关的失败。
   在实际部署中，效率（如冗余对话导致的 token 浪费）、成本、延迟、鲁棒性与安全性等维度同样关键，但这些未被纳入当前分类法。
3. **标注成本与规模**：尽管 LLM 标注器大幅扩展了标注规模，但其性能仍依赖于 MAST 定义的清晰度与人类标注的少量样本质量。
   对于极端复杂或领域特定的轨迹，LLM 标注器可能仍存在误判。
4. **干预实验规模有限**：当前案例研究规模较小，且主要集中在 ChatDev 与 AG2 两个框架上。
   更大规模、覆盖更多框架的系统性干预验证仍是未来工作。
5. **底层模型演进**：随着下一代模型的发布，部分失败模式（尤其是 FC1 中与指令跟随相关的模式）的分布可能发生变化，需要持续追踪。

## 我的笔记

本文是 MAS 领域一篇极具里程碑意义的数据集与基准论文。
与许多聚焦“如何构建更好 MAS”的工作不同，本文选择了一条更具基础性的路径：先系统理解“为什么现有 MAS 失败”。
这种“诊断优先”的方法论值得借鉴。
MAST 分类法的 14 种失败模式不仅为研究者提供了共同语言，更为工程师提供了可操作的调试框架。

从个人角度看，本文最有启发性的发现是 FC2（智能体间失配）中提到的“社会推理”缺失。
当前多智能体通信协议（如 MCP、A2A）主要解决消息格式标准化问题，但本文证据表明，即使格式正确，智能体仍可能因缺乏对他人信息需求的建模而失败。
这提示未来工作可能需要将“心智理论”（ToM）显式引入智能体设计，或通过在多智能体交互数据上的专门训练来提升模型的交际智能。

另一个值得关注的点是验证（FC3）的多层次性。
+15.6% 的干预提升来自于简单地增加了一层高层目标验证，这说明当前许多 MAS 的验证设计过于片面。
对于复杂软件生成任务，或许可以借鉴传统软件测试中的单元测试、集成测试与验收测试分层思想，为 MAS 构建类似的模块化验证体系。

在复现与扩展方面，MAST-Data 与 LLM 标注器均已开源，这为后续研究提供了良好基础。
一个可能的研究方向是将 MAST 应用于闭源商业 MAS 或企业级工作流自动化系统，检验分类法在更复杂真实场景中的适用性。
此外，将失败模式与具体修复策略进行自动映射（类似于自动程序修复中的缺陷模式-修复模板对应），也是一个有潜力的延伸方向。

## 引用

```bibtex
@article{cemri2025why, title={Why Do Multi-Agent LLM Systems Fail?}, author={Cemri, Mert and Pan, Melissa Z. and Yang, Shuyi and Agrawal, Lakshya A. and Chopra, Bhavya and Tiwari, Rishabh and Keutzer, Kurt and Parameswaran, Aditya and Klein, Dan and Ramchandran, Kannan and Zaharia, Matei and Gonzalez, Joseph E. and Stoica, Ion}, journal={arXiv preprint arXiv:2503.13657}, year={2025}, url={https://arxiv.org/abs/2503.13657}}
```
