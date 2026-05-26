---
tags:
  - MAS
  - multi-agent-system
  - failure-taxonomy
  - dataset
  - LLM-agent
  - NeurIPS-2025
aliases:
  - MAST
  - MAST-Data
  - Why Do Multi-Agent LLM Systems Fail
date: 2025-10-27
doi: 10.3362/9781780441061.013
---

# Why Do Multi-Agent LLM Systems Fail?

## 核心信息

- **标题**: Why Do Multi-Agent LLM Systems Fail?
- **作者**: Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Keutzer, Aditya Parameswaran, Dan Klein, Kannan Ramchandran, Matei Zaharia, Joseph E. Gonzalez, Ion Stoica
- **机构**: UC Berkeley, Intesa Sanpaolo
- **年份**: 2025
- **会议**: NeurIPS 2025 Datasets and Benchmarks Track
- **DOI**: 10.3362/9781780441061.013
- **arXiv**: 2503.13657
- **证据质量**: high

## 原文摘要翻译

尽管多智能体大语言模型系统（MAS）受到广泛关注，但它们在主流基准测试上的性能提升往往微乎其微。
这一差距凸显了对 MAS 失效原因进行系统性理解的迫切需求。
回答该问题需要对失败模式进行系统识别与分析。
本文提出 MAST-Data，一个涵盖 7 个流行 MAS 框架、包含 1600 余条标注执行轨迹的综合数据集。
该数据集是首个用于刻画 MAS 失败动态、指导未来系统改进的多智能体系统数据集。
为支撑系统化分类，本文构建了首个多智能体系统失败分类体系 MAST。
研究团队基于 150 条轨迹的严谨分析，在专家人工标注者指导下完成 MAST 的构建，并通过高标注者一致性（Cohen's $\kappa = 0.88$）加以验证。
该过程识别出 14 种独特失败模式，并聚类为 3 大类：（i）系统设计问题、（ii）智能体间失配、（iii）任务验证问题。
为实现可扩展标注，团队开发了大模型裁判流水线，与人类标注保持高度一致。
研究利用 MAST 与 MAST-Data 跨模型和跨任务分析失败模式，揭示了通过改进 MAS 设计可获得的提升空间。
分析表明，已识别的失败需要更复杂的解决方案，为未来研究勾勒出清晰路线图。
团队已公开释放数据集、分类体系及自动标注器。

## 创新点

1. **首个大规模 MAS 失败数据集 MAST-Data**：覆盖 7 个流行框架、4 个模型家族，共 1642 条标注执行轨迹，并附带 21 条三人独立人工标注轨迹。
2. **首个经验驱动的 MAS 失败分类体系 MAST**：通过扎根理论方法从 150 条轨迹中提炼，经三轮标注者一致性迭代验证，定义 14 种细粒度失败模式，归为 3 大类别。
3. **可扩展的自动标注流水线**：基于 o1 模型构建标注器，在人类一致性数据上达到 94% 准确率、Cohen's $\kappa = 0.77$；在未见过的框架与基准上仍保持 $\kappa = 0.79$。
4. **干预案例研究揭示系统设计的首要性**：在相同底层模型下，仅通过系统工作流与提示调整即可带来最高 15.6% 的任务成功率提升，说明许多失败源于系统设计而非模型能力。

## 一句话总结

本文通过构建经验驱动的失败分类体系 MAST 与大规模标注数据集 MAST-Data，系统揭示了当前多智能体系统的 14 种失败模式，并证明这些失败主要来自系统设计与协调缺陷而非底层模型局限。

## 研究问题

本文提出的核心问题是：**为什么多智能体大语言模型系统会失败？**

研究将失败定义为「多智能体系统未能达成其预期任务目标」的实例。动机来源于以下观察：尽管多智能体系统在软件工程、药物发现、科学模拟和通用智能体等领域被广泛探索，但它们在流行基准上的性能增益往往微乎其微，甚至不如单智能体框架或简单的 best-of-N 采样基线。作者在 7 个开源系统上测得 41% 至 86.7% 的失败率，且社区对如何构建稳健可靠的系统缺乏共识。

该问题的挑战性在于：失败的根因检测难以验证真实标签，且缺乏标准化的失败定义框架。这要求研究者不仅要识别表面错误，还需理解系统动态与智能体交互的深层机制。

## 数据与任务定义

**MAST-Data** 是一个综合性、经验驱动的多智能体系统失败数据集，包含 1642 条来自 7 个流行框架的标注执行轨迹，覆盖编程、数学和通用任务三大领域。标注方式分为三类：人工检查任务完成率（HE）、人工标注失败模式（HA）、大模型自动标注（LA）。

来自 LaTeX 源码 `08-mad-tab.tex` 的表 1 展示了数据集配置详情：

| 框架 | 基准 | 模型 | 标注方式 | 轨迹数 |
|:---|:---|:---|:---|---:|
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

![图 1 MAST 失败模式分类体系](p-021_Why_Do_Multi_Agent_LLM_Systems_Fail/images/taxonomy_neurips_final_10_23_25.png)

## 方法主线

### 机制流程

本文构建数据集的方法包含以下关键步骤：

1. **收集初始轨迹并执行开放式编码**：从 5 个框架（HyperAgent、AppWorld、AG2、ChatDev、MetaGPT）收集 150 条轨迹，由 6 名专家采用扎根理论方法进行逐行分析，通过理论采样确保覆盖不同系统目标与交互模式。
2. **迭代提炼失败模式并构建分类体系**：利用持续比较分析与备忘录技术，将观察到的失败行为归纳结构化为初始模式；经三轮三人独立一致性研究，迭代修正定义，最终达到 Cohen's $\kappa = 0.88$。
3. **校准大模型裁判标注器**：将验证后的分类定义与少量示例输入 o1 模型，在保留的人工标注数据上验证，实现 94% 准确率与 $\kappa = 0.77$；并在两个未见框架（OpenManus、Magentic-One）与新基准上验证泛化性，获得 $\kappa = 0.79$。
4. **扩展生成完整数据集**：利用校准后的自动标注器对 1642 条轨迹进行规模化标注，每条轨迹附带失败模式及文本理由；同时保留人工标注对照集。

![图 2 数据集构建方法流程](p-021_Why_Do_Multi_Agent_LLM_Systems_Fail/images/arxiv_figure_neurips_cropped.png)

### MAST 分类体系结构

MAST 将 14 种失败模式映射到执行阶段（Pre-Execution、Execution、Post-Execution），并归入 3 大类别：

- **FC1：系统设计问题（41.8%）**
  - 1.1 违背任务规格（11.8%）
  - 1.2 违背角色规格（1.5%）
  - 1.3 步骤重复（15.7%）
  - 1.4 对话历史丢失（2.8%）
  - 1.5 未意识到终止条件（12.4%）

- **FC2：智能体间失配（36.9%）**
  - 2.1 对话重置（2.2%）
  - 2.2 未请求澄清（6.8%）
  - 2.3 任务偏离（7.4%）
  - 2.4 信息隐瞒（0.8%）
  - 2.5 忽略其他智能体输入（1.9%）
  - 2.6 推理与行动不匹配（13.2%）

- **FC3：任务验证（21.3%）**
  - 3.1 过早终止（6.2%）
  - 3.2 验证缺失或不完整（8.2%）
  - 3.3 验证错误（9.1%）

来自 LaTeX 源码 `04_methodology.tex` 的表 2 展示了自动标注器性能：

| 模型 | 准确率 | 召回率 | 精确率 | F1 | Cohen's $\kappa$ |
|:---|---:|---:|---:|---:|---:|
| o1 | 0.89 | 0.62 | 0.68 | 0.64 | 0.58 |
| o1 (few shot) | 0.94 | 0.77 | 0.833 | 0.80 | 0.77 |

## 关键结果

**失败率统计**：在 7 个开源系统上，失败率介于 41% 至 86.7% 之间。不同系统的失败分布差异显著，反映出其独特架构特征与设计哲学。

![图 5 七个开源系统的失败率](p-021_Why_Do_Multi_Agent_LLM_Systems_Fail/images/multi_agent_systems_failure_rates.png)

**系统级失败分布**：图 4 展示了数据集中 210 条轨迹的失败模式分布。AppWorld 频繁出现过早终止（3.1），可能与其星型拓扑及缺乏预定义工作流有关；OpenManus 倾向于步骤重复（1.3）；HyperAgent 则需重点解决步骤重复与错误验证（3.3）。

![图 4 数据集失败分布](p-021_Why_Do_Multi_Agent_LLM_Systems_Fail/images/masft_bar.png)

**模型与架构的影响**：
- 在 MetaGPT 框架下比较两款模型，GPT-4o 在系统设计问题与智能体间失配上的失败显著更少。
- 但两款模型在任务验证上均表现薄弱。
- 在相同模型下比较两款编程框架，MetaGPT 的系统设计问题与智能体间失配失败比 ChatDev 低 60%–68%。
- 但 MetaGPT 的任务验证失败是 ChatDev 的 1.56 倍，说明 ChatDev 的测试与评审阶段在验证方面更具优势。

![不同底层模型对失败模式的影响](p-021_Why_Do_Multi_Agent_LLM_Systems_Fail/images/effect_of_underlying_llm_system_design.png)

![不同架构对失败模式的影响](p-021_Why_Do_Multi_Agent_LLM_Systems_Fail/images/effect_of_mas_architecture_system_design.png)

**干预实验**：
- ChatDev 上改进角色提示并增加高层任务目标验证步骤，在 ProgramDev 上带来 +15.6% 的成功率提升。
- 确保 CEO 智能体拥有最终决策权的工作流调整，使整体任务成功率提升 +9.4%。
- 在数学对话系统上，改进提示使 GPT-4 配置从 84.75% 提升至 89.75%。
- 新拓扑使 GPT-4o 配置从 84.25% 提升至 88.83%，统计检验 $p = 0.03$。

来自 LaTeX 源码 `09_solutions.tex` 的表 3 展示了干预实验的准确率对比：

| 配置 | 数学A | 数学B | 编程A | 编程B |
|:---|---:|---:|---:|---:|
| 基线 | 84.75 ± 1.94 | 84.25 ± 1.86 | 25.0 | 89.6 |
| 改进提示 | 89.75 ± 1.44 | 89.00 ± 1.38 | 34.4 | 90.3 |
| 新拓扑 | 85.50 ± 1.18 | 88.83 ± 1.51 | 40.6 | 91.5 |

注：数学A 使用 AG2 数学对话框架、GPT-4 模型、GSM-Plus 基准。
数学B 使用 AG2 数学对话框架、GPT-4o 模型、GSM-Plus 基准。
编程A 使用 ChatDev 框架、ProgramDev-v0 基准。
编程B 使用 ChatDev 框架、HumanEval 基准。

> [!figure] 图 6 与图 7 干预前后失败模式变化
> 建议位置：关键结果
> 放置原因：这两张图分别展示 AG2 与 ChatDev 在基线、改进提示和新拓扑三种配置下的各失败模式占比变化，可直观呈现干预措施对具体失败模式的消解效果。
> 当前状态：已转换为本地 PNG，路径分别为 `intervention_comparison_threeway_ag2_system_design.png` 与 `intervention_comparison_threeway_chatdev_system_design.png`，建议插入至关键结果末尾。

## 深度分析

**系统设计的首要性**：作者指出，失败并非仅仅是底层大模型能力局限的产物。在相同模型下，通过更好的系统设计即可显著提升性能。这与高可靠性组织理论一致——即使个体能力出众，组织结构缺陷仍可导致灾难性失败。

**三大类别的深层洞察**：

1. **FC1 系统设计问题**：许多看似「指令遵循失败」的现象，深层原因在于系统对智能体角色与工作流的设计缺陷、用户提示规格不清，或模型本身的局限。一个设计良好的系统应当能在最小但清晰的用户输入下理解高层目标。例如，ChatDev 在生成 Wordle 游戏时，即使提示明确要求「不要固定词库」，仍反复生成固定列表，说明系统对规格的解释机制存在问题。

2. **FC2 智能体间失配**：这类失败要求智能体具备更深层的「社会推理」能力，即准确建模其他智能体的信息需求（心智理论）。虽然 MCP、Agent-to-Agent 等协议改善了通信格式标准化，但 FC2 中的失败即使在同一框架内使用自然语言交流时仍频繁出现，说明问题不在于消息格式，而在于内容层面的信息需求推断。解决 FC2 可能需要结合架构改进与模型层面的交际智能增强。

3. **FC3 任务验证**：现有验证器往往只做表面检查（如代码是否编译、是否遗留待办标记），而缺少对高层目标与运行正确性的深度验证。作者借鉴传统软件开发中的模块化单元测试思想，主张采用多层级验证策略：结合外部知识检索、生成过程中持续收集测试输出、低层正确性与高层目标双重检查。

**失败模式的相关性与独特性**：附录中的相关性研究表明，各失败模式之间具有可区分性，不同表面行为可能源于不同根因。例如「信息缺失」既可能是信息隐瞒（2.4）、忽略他人输入（2.5），也可能是对话历史丢失（1.4），这凸显了细粒度分类的必要性。

> [!figure] 图 3 轨迹片段可视化（信息隐瞒示例）
> 建议位置：深度分析
> 放置原因：该图展示了一个具体的跨智能体对话失败案例，可作为对失败模式定义的形象化补充。
> 当前状态：已转换为本地 PNG，路径为 `phone-agent-narrow.png`。

## 局限

1. **非穷尽性**：MAST 明确承认不覆盖所有潜在失败模式，仅聚焦于可从系统设计、协调与验证角度改进的失败。诸如效率、成本、延迟、鲁棒性、可扩展性和安全性等维度未纳入当前分类。
2. **任务领域侧重**：数据集主要覆盖编程、数学和通用智能体任务，在科学模拟、药物发现等更专业领域的代表性有限。
3. **干预实验规模较小**：案例研究仅涉及两个系统的小规模干预，结果虽显示改进空间，但任务完成率仍偏低，说明需要更根本性的系统重设计。
4. **验证器局限性**：即使显式引入验证器角色，整体成功率仍然不高，表明「有验证器」不等于「有效验证」，当前大模型在执行深度验证方面的能力仍显不足。
5. **标注成本与偏差**：扎根理论分析阶段每位专家需投入 20 小时以上；自动标注器虽与人工高度一致，但仍可能在边缘案例上引入系统性偏差。

## 我的笔记

本文的核心价值在于将多智能体研究从「追求更高准确率」转向「理解为什么失败」。MAST 提供了一个结构化语言，使开发者能够从聚合指标背后看到具体的失败剖面。这对实际工程极具指导意义：当 ChatDev 在 ProgramDev 上只有 25% 成功率时，MAST 能明确指出是角色规格违背、验证不足还是任务偏离所致，从而针对性地调整架构或提示。

一个值得关注的发现是「相同模型加不同架构」带来的失败分布差异。MetaGPT 通过标准操作流程的强约束减少了系统设计问题和智能体间失配，却因验证机制相对薄弱而在任务验证上劣于 ChatDev；反之 ChatDev 的评审阶段虽有利于验证，却在角色协调上暴露更多问题。这提示未来设计需要在「控制」与「验证」之间取得平衡。

从可复现性角度看，数据集的公开释放为社区提供了宝贵的诊断工具。研究者可直接调用 MAST 作为 Python 库，对自有系统进行失败分析。这种「分类体系即基础设施」的思路值得后续工作借鉴。

未来可拓展方向包括：将效率与成本维度纳入分类体系、在更多垂直领域验证通用性、探索基于强化学习的智能体社交推理能力提升，以及开发可自动根据诊断结果推荐架构修改的自动修复系统。

## 引用

```bibtex
@inproceedings{cemri2025why, title={Why Do Multi-Agent LLM Systems Fail?}, author={Cemri, Mert and Pan, Melissa Z. and Yang, Shuyi and Agrawal, Lakshya A. and Chopra, Bhavya and Tiwari, Rishabh and Keutzer, Kurt and Parameswaran, Aditya and Klein, Dan and Ramchandran, Kannan and Zaharia, Matei and Gonzalez, Joseph E. and Stoica, Ion}, booktitle={Thirty-ninth Conference on Neural Information Processing Systems (NeurIPS 2025) Track on Datasets and Benchmarks}, year={2025}, url={https://arxiv.org/abs/2503.13657}}
```
