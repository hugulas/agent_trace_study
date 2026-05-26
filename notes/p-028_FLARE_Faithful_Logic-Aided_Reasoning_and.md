---
tags: [LLM, reasoning, faithfulness, CoT, neuro-symbolic, Prolog, EMNLP2025]
aliases: [FLARE, p-028]
date: 2025-11
doi: 10.18653/v1/2025.emnlp-main.1193
---

# FLARE: Faithful Logic-Aided Reasoning and Exploration

## 核心信息

- 标题: FLARE: Faithful Logic-Aided Reasoning and Exploration
- 作者: Erik Arakelyan, Pasquale Minervini, Patrick Lewis, Pat Verga, Isabelle Augenstein
- 机构: University of Copenhagen, University of Edinburgh, NVIDIA, Cohere
- 发表时间: 2025
- 会议 / 期刊: EMNLP 2025
- DOI: 10.18653/v1/2025.emnlp-main.1193
- 论文链接: https://aclanthology.org/2025.emnlp-main.1193/
- 论文类型: 方法论文

## 原文摘要翻译

现代问答与推理方法普遍采用大语言模型的思维链提示，但其最终输出往往与中间推理链不一致。
神经符号方法（如 Faithful CoT）虽然借助外部求解器可获得更高的忠实度，却需要代码专用模型，并且难以处理模糊任务。
本文提出 FLARE，该方法利用大语言模型制定解题计划、将查询形式化为逻辑程序，并通过多跳搜索模拟代码执行，而无需外部求解器。
FLARE 在九个多样化推理基准中的七个以及三个逻辑推理基准上均达到最优结果，同时支持对推理忠实度的量化。
实验表明，模型忠实度与性能正相关；成功推理轨迹中唯一涌现事实平均增加百分之十八点一，代码定义关系与执行轨迹关系的重叠度提高百分之八点六，未使用关系减少百分之三点六。

## 创新点

1. **三模块解耦的推理范式**。FLARE 将自然语言查询的求解过程显式拆分为计划、代码与模拟搜索三个模块，使大模型既能进行软推理，又能保留形式化结构，摆脱对外部符号求解器的依赖。
2. **内建忠实度度量**。通过对比模型生成的模拟搜索轨迹与真实 Prolog 执行轨迹，使用 ROUGE-Lsum 计算相似度，首次在无需额外标注的情况下实现推理忠实度的自动评估，并验证其与最终准确率高度正相关。
3. **对非代码模型的友好性**。Faithful CoT 等神经符号方法在 Llama-3.1-8B、CmDR 等非代码专用模型上频繁崩溃（执行失败率极高或接近零分），而 FLARE 依靠模拟执行避免语法崩溃，在四个不同规模的通用模型上均取得稳定提升。
4. **可解释的故障诊断**。基于代码与搜索轨迹的事实—关系精确匹配，FLARE 能够显式定位两类推理故障：搜索中出现但代码中不存在的事实（幻觉），以及代码中定义却未在搜索中使用的关系（次优推理）。
5. **在十二个基准上的领先表现**。在九个问答基准（含数学词问题、多跳问答、关系推理）中的七个，以及三个逻辑推理基准中的两个上取得最优结果；加入两轮代码自精炼后，逻辑基准全部达到最优。

## 一句话总结

FLARE 通过让大语言模型依次生成自然语言计划、Prolog 代码与模拟搜索轨迹，在不依赖外部求解器的前提下实现了高忠实度的可解释推理，并在多个推理基准上达到最优结果。

## 研究问题

当前大模型推理面临的核心矛盾是：思维链等自然语言中间链虽灵活，但模型输出常背离这些链（不忠实）；神经符号方法虽忠实，却要求代码专用模型与严格可执行的形式化，无法处理需要常识与软推理的模糊问题。
因此，本文试图回答：如何在保持形式化结构以度量产出的同时，让通用大模型也能进行可靠的多跳软推理，并自动诊断其中的不一致？

## 数据与任务定义

论文在九个问答任务与三个逻辑推理任务上评估 FLARE，涵盖数学词问题、多跳问答、关系推理与逻辑演绎四大类。
具体数据集统计如下：

**Table 7** 数据集统计与示例。来自 LaTeX 源码 `data_stat.tex`。

| Domain | Dataset | Shots | Test Samples | Example |
|--------|---------|-------|--------------|---------|
| Math Word Problems | GSM8K | 8 | 1,319 | Q: A robe takes 2 bolts... A: 3 |
| Math Word Problems | SVAMP | 8 | 1,000 | Q: Dan had \$3... A: 1 |
| Math Word Problems | MultiArith | 8 | 600 | Q: A pet store had 13 cats... A: 8 |
| Math Word Problems | ASDiv | 8 | 2,096 | Q: Adam has five more apples... A: 14 |
| Math Word Problems | AQuA | 8 | 254 | Q: A man walks at 5 kmph... A: A |
| Multi-hop QA | StrategyQA | 6 | 2,290 | Q: Did Aristotle use a laptop? A: False |
| Multi-hop QA | Date Understanding | 10 | 359 | Q: Yesterday was April 30... A: 05/02/2021 |
| Multi-hop QA | Sports Understanding | 10 | 977 | Q: Is the following sentence plausible... A: False |
| Relational Inference | CLUTRR | 8 | 1,042 | Q: [Carlos] is [Clarence]'s brother... A: mother |

## 方法主线

FLARE 包含三个顺序生成的模块：计划、代码与模拟搜索。
给定自然语言查询，模型在逐步累积的少样本上下文支持下依次完成各模块，最终得到答案。

### 机制流程

1. 输入自然语言查询与少样本计划示例，大模型在指令的引导下生成计划，输出任务分析与形式化步骤。
2. 将计划与代码示例拼接为扩展上下文，模型据此生成 Prolog 代码；通过正则提取得到代码中的事实集合、关系集合与目标。
3. 在扩展上下文后追加真实 Prolog 执行轨迹，构造新的少样本示例；模型模拟代码执行并输出搜索轨迹，从中提取搜索事实、搜索关系与答案路径，最终汇总得到答案。

计划生成的条件概率形式如下：

$$
\mathcal{P}_i \sim p_{\mathcal{M}}(T^{\mathcal{P}}_i \mid T^{\mathcal{P}}_{:i-1}, \mathcal{E}_{\mathcal{P}}, \mathcal{Q}, \mathcal{I}^{\mathcal{P}})
$$

代码生成的条件概率形式如下：

$$
\mathcal{C}_i \sim p_{\mathcal{M}}(T^{\mathcal{C}}_i \mid T^{\mathcal{C}}_{:i-1}, \mathcal{E}_{\mathcal{C}}, \mathcal{Q}, \mathcal{I}^{\mathcal{P}}, \mathcal{P}, \mathcal{I}^{\mathcal{C}})
$$

搜索模拟的条件概率形式如下：

$$
\mathcal{S}_i \sim p_{\mathcal{M}}(T^{\mathcal{S}}_i \mid T^{\mathcal{S}}_{:i-1}, \mathcal{E}_{\mathcal{S}}, \mathcal{Q}, \mathcal{I}^{\mathcal{P}}, \mathcal{P}, \mathcal{I}^{\mathcal{C}}, \mathcal{C}, \mathcal{I}^{\mathcal{S}})
$$

最终答案生成的条件概率形式如下：

$$
\mathcal{A}_{\text{Final}} \sim p_{\mathcal{M}}(T^{\mathcal{A}}_i \mid T^{\mathcal{A}}_{:i-1}, \mathcal{E}_{\mathcal{A}}, \mathcal{Q}, \mathcal{I}^{\mathcal{P}}, \mathcal{P}, \mathcal{I}^{\mathcal{C}}, \mathcal{C}, \mathcal{I}^{\mathcal{S}}, \mathcal{S}, \mathcal{I}^{\mathcal{A}})
$$

![Fig. 1 FLARE 的三个模块示意图：计划、代码与模拟搜索](p-028_FLARE_Faithful_Logic-Aided_Reasoning_and/images/fig1_flare_overview.png)

### 检测推理不一致性

FLARE 对每一对代码与模拟搜索轨迹进行事实与关系的精确字符串匹配，识别两类推理故障。
第一类是幻觉：搜索中使用了代码中不存在的事实或关系，即模型在形式化阶段遗漏知识，或在模拟阶段凭空捏造信息（直接推理得到的涌现事实除外）。
第二类是次优推理：代码中定义了某些事实或关系，却在搜索中未被使用，说明模型未能充分探索问题空间，或在形式化阶段引入了不相关知识。

### 忠实度度量

对于数据集中的每个查询，FLARE 生成一组代码与一组模拟搜索轨迹。
随后使用 Prolog 引擎执行所有语法正确的代码，获得真实执行轨迹。
通过对比真实轨迹与模型生成的模拟轨迹，采用 ROUGE-Lsum（基于最长公共子序列的逐行匹配）计算忠实度分数。
该方法同时衡量推理内容与推理结构的相似性，且与仅使用字符串匹配的其他技术趋势一致。

## 关键结果

**Table 1** 各模型在不同数据集上的准确率（%）。来自 LaTeX 源码 `results.tex`。
其中每模型的最优值以 **粗体** 标出，最差值以 *斜体* 标出。

| Method | GSM8K | SVAMP | MultiArith | ASDiv | AQuA | StrategyQA | Date | Sport | CLUTRR |
|--------|-------|-------|------------|-------|------|------------|------|-------|--------|
| Llama-3.1-8B_FLARE | 72.7 | **86.0** | **96.3** | **83.1** | **62.9** | **70.2** | **59.3** | 76.6 | 36.8 |
| Llama-3.1-8B_F-CoT | *0* | *0* | *0* | *0* | *12.2* | 53.2 | *0* | *0* | *32* |
| Llama-3.1-8B_CoT | **85.2** | 82.4 | 91.6 | 79.1 | 51.6 | *43.5* | 74.1 | **89.4** | **45.7** |
| CmDR_FLARE | **52.4** | **74.0** | **84.5** | **72.2** | **43.7** | **67.0** | **52.3** | **78.9** | 29.1 |
| CmDR_F-CoT | *0* | *0* | *0* | *0* | *0* | 59.7 | *0* | *0* | *8.6* |
| CmDR_CoT | 46.5 | 57.3 | 83.1 | 37.2 | 28.3 | *21.3* | 47.4 | 55.2 | **29.5** |
| CmDR+_FLARE | **71.4** | **83.5** | **90.4** | **81.3** | **55.9** | **70.8** | 61.8 | **77.7** | **41.0** |
| CmDR+_F-CoT | *0* | *0* | *0* | *0* | *15.4* | 57.6 | *0* | *0* | *35.3* |
| CmDR+_CoT | 48.7 | 81.1 | 86.6 | 44.6 | 44.1 | 48.4 | **79.1** | 62.6 | 42.5 |
| GPT-3.5_FLARE | **82.1** | 82.7 | **98.3** | **85.4** | 55.1 | **65.5** | **82.4** | 85.6 | **49.8** |
| GPT-3.5_F-CoT | 75.8 | **83.0** | 95.3 | 81.7 | 53.5 | *51.5* | 73.5 | *52.3* | *12.1* |
| GPT-3.5_CoT | 79.8 | 82.4 | 98.2 | 75.8 | **59.4** | 51.7 | 69.9 | **95.8** | *4.3* |

**Table 2** 逻辑推理基准对比（准确率 %）。来自 LaTeX 源码 `logiclm_compare.tex`。

| Dataset | ChatGPT Standard | ChatGPT CoT | ChatGPT Logic-LM | ChatGPT FLARE | ChatGPT FLARE_SR=2 | GPT-4 Standard | GPT-4 CoT | GPT-4 Logic-LM | GPT-4 FLARE | GPT-4 FLARE_SR=2 |
|---------|------------------|-------------|------------------|---------------|--------------------|----------------|-----------|----------------|-------------|------------------|
| PrOntoQA | 47.40 | 67.80 | 61.00 | 73.40 | **79.40** | 77.40 | 98.79 | 83.20 | 98.87 | **99.24** |
| LogicalDeduction | 40.00 | 42.33 | **65.67** | 58.60 | 64.43 | 71.33 | 75.25 | 87.63 | 88.00 | **90.33** |
| AR-LSAT | 20.34 | 17.31 | 26.41 | 27.39 | **30.73** | 33.33 | 35.06 | 43.04 | 39.82 | **45.02** |

> [!figure] 各数据集独立的准确率—忠实度散点图
> 建议位置：关键结果
> 放置原因：附录中包含每个数据集单独的 model accuracy vs. ROUGE 散点图，可进一步细化不同任务上的忠实度—性能关系。
> 当前状态：保留占位；原始 PDF 位于 LaTeX 源码 `figures/` 目录，可按需补充。

## 深度分析

### 计划消融实验

**Table 3** 计划消融（准确率 %）。来自 LaTeX 源码 `prompt_only.tex`。

| Method | CmDR_plan-only | CmDR_FLARE | CmDR+_plan-only | CmDR+_FLARE | GPT-3.5_plan-only | GPT-3.5_FLARE |
|--------|----------------|------------|-----------------|-------------|-------------------|---------------|
| GSM8K | 24.7 | **52.4** | 40.7 | **71.4** | 36.1 | **68.1** |
| AQuA | 35.0 | **43.7** | 55.1 | **55.9** | 54.3 | **55.1** |
| StrategyQA | 65.5 | **67.0** | **75.7** | 70.8 | 62.3 | **65.5** |

仅生成计划而跳过代码与搜索时，模型性能显著下降（如 CmDR 在 GSM8K 上从 52.4 降至 24.7）。
这说明单纯依赖自然语言计划不足以完成充分的问题空间探索，代码形式化与模拟搜索对准确推理至关重要。

### 忠实度与性能的相关性

论文使用 ROUGE-Lsum 将模拟搜索轨迹与真实 Prolog 执行轨迹进行对齐，发现模型准确率与忠实度呈强正相关。

![Fig. 2 模型平均准确率与平均忠实度的关系](p-028_FLARE_Faithful_Logic-Aided_Reasoning_and/images/fig2_faith_vs_acc.png)

与此同时，实验显示所有模型平均能在百分之六十七的情况下生成语法正确的可执行 Prolog 代码，最低不低于百分之五十。
然而，语义精确且可执行的代码本身仅在平均百分之四十七的情况下直接得到正确答案。
这表明：单纯执行代码（如 Faithful CoT）不足以处理需要常识软推理的复杂任务，而 FLARE 通过模拟搜索在保持结构忠实的同时保留了软推理能力。

![Fig. 3 各模型可执行代码比例（上）与可执行代码准确率（下）](p-028_FLARE_Faithful_Logic-Aided_Reasoning_and/images/fig3a_code_exec_perc.png)

![Fig. 3（续）各模型可执行代码准确率](p-028_FLARE_Faithful_Logic-Aided_Reasoning_and/images/fig3b_code_exec_acc.png)

### 搜索轨迹统计

**Table 4** 正确与错误答案的搜索轨迹统计。来自 LaTeX 源码 `reasoning_stats_basic.tex`。

**Incorrect Answers**

| Model | #Paths | #Hops/p | #Fails/p | TotHops | TotFails |
|-------|--------|---------|----------|---------|----------|
| Llama-3.1-8B | 1.55 | 11.12 | 1.52 | 15.09 | 2.26 |
| CmDR | 1.51 | 6.55 | 0.68 | 10.56 | 1.39 |
| CmDR+ | 0.92 | 7.52 | 1.13 | 8.57 | 1.32 |
| GPT-3.5 | 0.68 | 5.22 | 0.71 | 5.32 | 0.74 |

**Correct Answers**

| Model | #Paths | #Hops/p | #Fails/p | TotHops | TotFails |
|-------|--------|---------|----------|---------|----------|
| Llama-3.1-8B | 1.43 | 9.12 | 0.62 | 12.36 | 0.96 |
| CmDR | 1.19 | 7.10 | 0.42 | 11.29 | 0.66 |
| CmDR+ | 0.97 | 7.19 | 0.42 | 8.22 | 0.61 |
| GPT-3.5 | 0.82 | 5.65 | 0.26 | 5.69 | 0.27 |

导致错误答案的轨迹在单位路径上的失败次数更高。
这说明最优推理并非单纯依赖更多探索路径或更深的跳数，而是能够借助强常识能力跳过退化解。

**Table 5** 正确与错误答案的涌现事实、关系重叠与未使用关系比例。来自 LaTeX 源码 `reasoning_stats_deep.tex`。

| Model | UEF (%) | OR (%) | UR (%) |
|-------|---------|--------|--------|
| **Correct Answers** | | | |
| Llama-3.1-8B | 74.14 | 43.65 | 5.73 |
| CmDR | 59.06 | 35.96 | 4.02 |
| CmDR+ | 64.30 | 34.47 | 4.54 |
| GPT-3.5 | 64.46 | 37.55 | 1.90 |
| Avg. | 65.49 | 37.91 | 4.05 |
| **Incorrect Answers** | | | |
| Llama-3.1-8B | 54.69 | 35.04 | 9.28 |
| CmDR | 54.50 | 32.76 | 6.23 |
| CmDR+ | 44.12 | 24.98 | 8.22 |
| GPT-3.5 | 36.02 | 24.44 | 6.94 |
| Avg. | 47.33 | 29.31 | 7.67 |
| **Δ** | 18.16 | 8.60 | -3.62 |

正确轨迹的平均唯一涌现事实比例（UEF）比错误轨迹高十八点一六个百分点，关系重叠比例（OR）高八点六个百分点，未使用关系比例（UR）低三点六二个百分点。
这与论文摘要中报告的数字一致，说明成功推理需要充分的问题空间探索、较少的关系幻觉以及更高的代码关系利用率。

### 模型规模效应

**Table 6** 不同规模模型（8B 至 100B+）的搜索统计。来自 LaTeX 源码 `scale_effect.tex`。

| Model | Avg. hops per path | Hal. (%) | UK. (%) |
|-------|-------------------|----------|---------|
| Llama-3.1-8B | 9.4 | 63.3 | 62.9 |
| CmDR | 6.7 | 54.7 | 56.9 |
| CmDR+ | 7.2 | 54.3 | 56.3 |
| GPT-3.5 | 5.5 | 49.3 | 52.1 |

![Fig. 4 模型规模（8B 到 100B+）对准确率（左）与忠实度（右）的影响](p-028_FLARE_Faithful_Logic-Aided_Reasoning_and/images/fig4_effect_of_scale.png)

同一家族内的放大（CmDR 30B 到 CmDR+ 100B）同时提升了性能与忠实度，且幻觉比例与未使用知识比例随规模增大而降低。
这进一步证实：具备强常识软推理能力的模型能够在搜索中跳过冗余步骤，同时保持对代码定义结构的忠实。

## 局限

论文自身列出的局限包括：FLARE 依赖大模型生成计划与代码的质量，形式化错误会沿管道传播至模拟搜索；模拟搜索对极大或开放式问题空间的探索可能不彻底；提示敏感度会影响搜索完备性。

此外，从实验观察可以补充两点：第一，FLARE 相比单次思维链增加了计划、代码、搜索、答案四次顺序生成，推理延迟与 token 消耗显著更高，但论文未报告具体成本数据；第二，代码自精炼仅在三个逻辑基准上使用，其在九个问答基准上的效果尚未验证。

## 我的笔记

- **复现思路**：需要部署 SWI-Prolog 环境以执行生成的代码并获取真实轨迹，用于计算 ROUGE-Lsum 忠实度分数。少样本示例需从训练集中人工挑选，确保覆盖多跳推理、关系推理与数值推理等模式。
- **与相关工作的联系**：FLARE 可视为思维链与 Faithful CoT 的折中——保留前者的软推理能力，同时引入后者的形式化结构以度量忠实度。未来可将其与 Tree-of-Thoughts 结合，把模拟搜索扩展为显式的树形回溯与剪枝。
- **潜在改进**：当前代码自精炼仅在逻辑基准上验证，若引入问答基准可能进一步提升鲁棒性；此外，可尝试将 Prolog 替换为 Datalog 或 Python，检验形式化语言选择对软推理与忠实度测量的影响。

## 引用

```bibtex
@inproceedings{arakelyan-etal-2025-flare, title = {{FLARE}: Faithful Logic-Aided Reasoning and Exploration}, author = {Arakelyan, Erik and Minervini, Pasquale and Lewis, Patrick and Verga, Pat and Augenstein, Isabelle}, booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing}, pages = {23385--23403}, year = {2025}, publisher = {Association for Computational Linguistics}, address = {Suzhou, China}, doi = {10.18653/v1/2025.emnlp-main.1193}, url = {https://aclanthology.org/2025.emnlp-main.1193/} }
```
