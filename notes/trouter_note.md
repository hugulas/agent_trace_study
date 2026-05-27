# Task-Aware LLM Routing with Multi-Level Task-Profile-Guided Data Synthesis for Cold-Start Scenarios

## 核心信息

- 标题: Task-Aware LLM Routing with Multi-Level Task-Profile-Guided Data Synthesis for Cold-Start Scenarios
- 作者: Hui Liu, Bin Zou, Kecheng Chen, Jie Liu, Wenya Wang, Haoliang Li
- 机构: City University of Hong Kong, University of Hong Kong, Nanyang Technological University
- 发表时间: 2026
- 会议 / 期刊: arXiv
- DOI: 10.48550/arXiv.2604.09377
- 论文链接: https://arxiv.org/pdf/2604.09377

## 原文摘要翻译

大型语言模型在不同任务和查询上的性能与计算成本存在显著差异，这促使研究者构建能够根据用户特定的成本与性能权衡来选择模型的路由系统。然而，现有路由器在缺乏领域内训练数据的冷启动场景中泛化能力较差。本文通过一种多级任务画像引导的数据合成框架来解决这一局限，该框架构建层次化任务分类体系并生成多样化的问答对，以逼近测试时的查询分布。在此基础上，本文提出 TRouter，一种任务类型感知的路由方法，它通过隐式任务类型变量对查询条件下的成本与性能进行建模，并利用合成任务分类体系导出的先验进行正则化。这一设计提升了 TRouter 在冷启动与有数据场景下的路由效用。在多个基准测试上的实验表明，本文的合成框架能够缓解冷启动问题，且 TRouter 能够实现有效的语言模型路由。

## 创新点

1. **首次系统识别并解决 LLM 路由中的冷启动问题。** 现有路由方法普遍假设可以获取领域内标注数据，本文明确指出真实部署中常面临无标注资源的冷启动场景，并针对性地提出数据合成方案。
2. **提出多级任务画像引导的数据合成框架。** 该框架仅需少量领域描述作为输入，即可通过层次化任务分类体系自动生成逼近测试分布的多样化问答数据，显著降低人工标注与全模型评估成本。
3. **设计 TRouter，将任务类型作为隐式变量引入路由决策。** 通过任务识别模块与多组度量预测模块的协同，TRouter 利用合成分类体系先验对任务类型分布进行正则化，有效解耦任务语义与其他输入特征。
4. **在开源与商业模型池上均验证有效，且在小样本下保持稳健。** 实验表明该方法在冷启动与有数据设定下均优于现有分类与回归基线，同时难度级任务画像的采样效率显著高于粗粒度画像。

## 一句话总结

通过构建层次化任务分类体系合成冷启动训练数据，并引入隐式任务类型先验正则化，TRouter 在多种偏好设定下实现了稳定且优于基线的路由效用。

## 研究问题

现有大语言模型路由方法大多假设能够获取领域内标注训练数据，并在此基础上评估所有候选模型以收集性能与成本指标，进而训练轻量路由器。然而，真实部署中个人用户与早期产品常面临冷启动困境，缺乏资源收集标注数据。此外，预训练路由器在部署时常因训练与测试输入之间的领域偏移而泛化不佳。实验表明，即使在跨域设定下，现有分类与回归方法的表现甚至可能弱于简单的规则基线。

> [!figure] Fig. 1: Comparison between the traditional data preparation pipeline and our proposed LLM-based data synthesis approach for the LLM router training.
> 建议位置：研究问题
> 放置原因：该图直观对比了传统方法需要人工标注与全模型评估的高成本流程，与本文提出的低成本自动化合成数据方案，有助于读者理解冷启动问题的动机。
> 当前状态：占位符

## 数据与任务定义

论文选取四项数据集进行主实验，并在附录中补充额外任务以验证通用性。
主数据集包括 Alpaca（混合任务）、CSQA（常识问答）、DROP（阅读理解）与 Multi-News（摘要）。
补充数据集涵盖 WMT、Guha 与 MedMcQA 等。
各任务的评估指标包括 Accuracy 与 F1。

候选模型采用 Qwen3 系列开源模型，参数量从 0.6B 到 32B 不等。补充实验还使用了 GPT-4.1、Gemini-2.5-flash 等商业闭源模型。为贴近真实部署需求，论文在主要实验中采用较新的先进模型，而非早期过时模型。

> [!figure] Table 1: Overview of Datasets.
> 建议位置：数据与任务定义
> 放置原因：该表汇总了主实验使用的数据集及其任务类型、评估指标与样本规模，是理解实验范围的基础。
> 当前状态：占位符

> [!figure] Table 2: Overview of open-source and commercial LLMs, their sizes, and costs per million tokens.
> 建议位置：数据与任务定义
> 放置原因：该表列出候选模型的规模与每百万 token 成本，为后续成本敏感路由实验提供定价依据。
> 当前状态：占位符

数据预处理阶段将所有采样数据聚合，并按 7:1:2 划分为训练、验证与测试集。为估计响应质量，论文采用大模型作为评判者来打分，而不依赖真值标签。模型成本按输入与输出的 token 数量乘以各模型单价计算。为支持基于效用的优化，性能与成本指标均经过归一化以消除量纲差异。

用户偏好设定为三种场景，分别为成本优先（性能权重 0.2，成本权重 0.8）、均衡偏好（各 0.5）与性能优先（性能权重 0.8，成本权重 0.2）。其中性能优先未设为极端权重，以避免退化为始终选择最大模型的平凡策略。

## 方法主线

### 问题形式化

设候选模型集合为 $M = \{m_1, \dots, m_M\}$，用户查询为 $q$。LLM 路由的目标是选择模型 $m^*$ 以最大化如下效用函数：

$$m^* = \arg\max_{m \in M} U(m,q) = \mu_r \cdot r(m,q) - \mu_c \cdot c(m,q)$$

$$\text{s.t.} \quad \mu_r + \mu_c = 1, \quad \mu_r, \mu_c \geq 0$$

其中 $r(\cdot)$ 与 $c(\cdot)$ 分别为性能函数与成本函数。$\mu_r$ 与 $\mu_c$ 反映用户对性能与成本权衡的偏好。性能评估指标随任务类型而异。成本则由输入输出词元数量与模型单价共同决定。

### 机制流程

1. **输入领域描述，任务类型生成器自顶向下逐层扩展并输出三级层次分类体系。** 以高层领域信息为种子，生成器迭代产生领域、子类别与难度级别节点，最终得到包含多个粒度层次的层次化任务分类体系。
2. **任务类型质量评估器对候选子任务集合进行校验与修订。** 评估器检查节点间的凝聚力与多样性，迭代剔除低质量节点并补充新节点，输出修订后的子任务类型集合。
3. **问答对生成器依据难度级任务画像批量提取并合成问答数据。** 生成器按任务画像批量产生问答对，通过句子变换器计算语义相似度并去重，得到合成数据集 Dsyn。
4. **TRouter 接收查询，经编码与拼接后输出最优模型选择。** 查询先送入任务识别模块编码为任务类型分布，再与模型标识拼接后送入多组度量预测模块，得到性能与成本估计，最终通过效用最大化得到最优模型。

> [!figure] Figure 2: (a) Overview of our proposed task-profile-guided data synthesis framework. The task type generator and quality evaluator collaboratively construct a hierarchical task taxonomy, while the question-answer pair generator produces diverse QA pairs based on task profiles from difficulty-level task types. (b) Overview of our proposed task-type–aware LLM routing method, introducing a latent task-type variable into cost and performance prediction.
> 建议位置：方法主线 / 机制流程
> 放置原因：该图清晰展示了数据合成框架的三组件协作关系以及 TRouter 的任务识别加度量预测双模块架构，是理解全文方法的核心示意图。
> 当前状态：占位符

### TRouter 架构

基于合成的任务分类体系，本文进一步提出 TRouter。其核心思想是将任务类型 $t$ 视为隐式变量，对查询条件化的成本与性能进行建模。具体而言，TRouter 假设给定查询 $q$ 与模型 $m$ 时，指标 $h$ 的条件分布可通过任务类型分解：

$$p(h|q,m) = \sum_{t \in T} p(h|t,m)p(t|q)$$

公式中的两项分别具有明确意义。第一项为查询上的任务类型先验：
$p(t|q)$
第二项为给定任务类型与模型时的指标分布：
$p(h|t,m)$
该分解使 TRouter 能够解耦任务语义对度量预测的影响。

在实现上，TRouter 包含两个模块。
任务识别模块的表达式为
$q_\phi(t|q)$
多组度量预测模块的表达式为
$p_\theta(h|t,m)$
任务识别模块输出查询在各任务类型上的分布。
度量预测模块针对每个候选模型的每项指标进行估计。

### 训练目标

训练过程优化如下联合目标：

$$\mathcal{L} = \mathcal{L}_{CE} + \frac{1}{|M||H|}\sum_{m \in M}\sum_{h \in H}\mathcal{L}_{h,m}^{MSE}$$

训练目标包含两项。第一项为交叉熵损失：
$$\mathcal{L}_{CE} = -\sum_{q \in D} y \log q_\phi(t|q)$$
该项对应于变分后验与先验之间的散度正则化。第二项为各模型各指标预测的均方误差损失：
$$\mathcal{L}_{h,m}^{MSE}$$
第一项鼓励任务表示对模型指标具有预测性。第二项通过将变分后验拉向合成分类体系导出的先验来改善校准并缓解过拟合。

## 关键结果

论文在冷启动与有数据两种设定下对比了多种基线方法。主结果表格分别展示了使用传统指标与使用大模型评判估计性能的两种评估方式。在两种设定下，TRouter 在三种用户偏好场景中均取得最优或次优表现，且在有数据设定下将效用总和提升超过 0.3。相比之下，分类基线 RouterDC 与回归基线 MetricRouter 在跨域设定中表现不佳，甚至弱于简单的规则基线。

> [!figure] Table 3: Results across three user preference settings in both cold-start and in-domain scenarios. For in-domain training, candidate LLM performance is obtained using traditional metrics.
> 建议位置：关键结果
> 放置原因：该表呈现使用传统指标评估时的主实验结果，直接证明 TRouter 在冷启动与有数据场景下对多种基线的优势。
> 当前状态：占位符

> [!figure] Table 4: Results across three user preference settings in both cold-start and in-domain scenarios. For in-domain training, candidate LLM performance is obtained using LLM-as-a-judge.
> 建议位置：关键结果
> 放置原因：该表展示使用大模型评判估计性能时的结果，验证在缺乏真值标签的真实部署条件下 TRouter 依然有效。
> 当前状态：占位符

在消融实验中，论文比较了使用不同层次任务画像构建任务分类体系的效果。如图 3 所示，在固定采样轮次下，基于难度级画像的采样效率显著高于基于领域或子类别画像的方案，其有效问答对数量几乎线性增长，而粗粒度画像因冗余累积导致增长趋缓。这表明难度级条件能够产生更多样化的样本，更好地逼近测试分布。

> [!figure] Fig. 3: Effect of using task types of different taxonomy level to construct task-profile on sampling efficiency on Mathematics and Creative Writing domains.
> 建议位置：关键结果
> 放置原因：该图证明三级分类体系中难度级画像的采样效率最高，是支撑数据合成有效性的关键实验证据。
> 当前状态：占位符

Table 5 进一步展示了不同分类体系层级下采样规模 T 的影响。难度级画像在各偏好设定下均表现最佳，验证了细粒度任务描述对冷启动数据合成的重要性。

> [!figure] Table 5: Effect of T across three taxonomy levels.
> 建议位置：关键结果
> 放置原因：该表量化了不同分类粒度下采样规模对路由效用的影响，支持难度级最优的结论。
> 当前状态：占位符

消融实验对 TRouter 的不同设计选择进行了检验。结果表明，保留任务类型条件独立性假设的完整模型始终优于去除该假设的变体，说明隐式任务类型变量对准确建模成本与性能关系至关重要。此外，当训练样本量增加时，TRouter 的表现保持稳定，而 MetricRouter 则出现先降后升的不稳定现象，进一步验证了任务类型先验的鲁棒性。

> [!figure] Table 7: Ablation study of different designs of TRouter.
> 建议位置：关键结果
> 放置原因：该表从模型设计角度验证任务类型条件独立性假设与隐式变量机制的有效性。
> 当前状态：占位符

## 深度分析

TRouter 的核心优势在于将任务类型作为中间表示，解耦了任务语义与其他输入特征对度量预测的影响。传统回归方法直接建模如下分布：
$$p(h|q,m)$$
在查询分布偏移时难以泛化。而 TRouter 通过如下分解：
$$p(h|t,m)p(t|q)$$
使模型能够利用合成分类体系的结构化先验，在冷启动场景下仍能形成合理的任务类型分布估计。

从数据合成角度看，难度级任务画像之所以表现最优，关键在于其提供了最细粒度的生成控制。领域级画像过于宽泛，导致生成的问答对在主题上高度重叠；子类别级画像虽有所细化，但仍会在同一子类别内产生冗余。难度级画像将任务描述精确到具体能力层次，使生成器能够在固定采样预算下覆盖更广的查询分布，从而更有效地逼近测试时的真实分布。

论文还指出，由于 TRouter 在任务类型级别而非单个问答对级别建模成本与性能关系，它对单个合成样本的噪声具有天然鲁棒性。这与传统数据合成中需要严格规则过滤以避免性能崩溃的做法形成对比。如图 4 所示，在冷启动小样本设定中，当训练样本量增加时 TRouter 保持稳定，而基线方法则出现波动；这说明即使合成数据未经过穷尽验证，TRouter 仍能在噪声存在的情况下保持稳健的路由决策。

> [!figure] Fig. 4: Effect of shot number in the cold-start setting for TRouter and MetricRouter.
> 建议位置：深度分析
> 放置原因：该图展示了 TRouter 与 MetricRouter 在冷启动场景下随样本量增加的表现差异，直接支撑任务类型先验对噪声鲁棒性的分析。
> 当前状态：占位符

从部署角度看，TRouter 的样本效率较高。在少量合成数据（如小样本设定）下即可达到可接受的效用水平，这意味着在资源受限的冷启动场景中，该方法具备实际落地价值。此外，论文使用 Qwen3 系列模型与商业闭源模型分别验证了方法的通用性，表明其不依赖于特定模型族。

## 局限

论文坦诚地讨论了以下三点局限。

第一，任务画像引导的合成过程需要最少的人工输入来指定候选领域。虽然作者指出实际部署中提供者通常了解高层上下文，可以手动指定领域或让大模型自动生成，但这仍引入了不可避免的人工干预。不过，与现有方法需要完整的领域内标注数据相比，本文方案对冷启动场景更为友好。

第二，合成的问答对未经过穷尽验证。现有数据合成工作常依赖严格的规则过滤来避免性能崩溃，而本文选择在任务类型级别建模成本与性能关系，从而降低了对单个样本质量的苛刻要求。实验结果支持这一假设，但若部署场景对数据质量有极高要求，仍可能需要额外的验证步骤。

第三，使用大模型作为评判者可能引入模型偏见。评判模型的偏好与能力边界会影响性能估计的准确性，这在一定程度上限制了冷启动评估的可靠性。如何设计更校准的评判协议仍是开放问题。

## 我的笔记

TRouter 的工作对实际产品部署具有直接参考价值。在许多 to-B 或 to-C 场景中，新产品上线初期确实缺乏用户查询的标注数据，传统路由方法难以直接应用。本文提出的合成框架仅需领域描述即可启动，大大降低了冷启动门槛。不过，领域描述的质量仍会影响后续分类体系的合理性，因此在落地时建议结合业务专家的知识进行首轮领域筛选，再利用大模型自动扩展子类别与难度级别。

从技术演进角度看，本文将隐式变量模型引入路由决策，可视为对现有回归与分类框架的重要补充。未来可能的研究方向包括：将任务类型动态更新机制引入在线学习框架，使路由器能够随着真实用户数据的积累逐步调整先验；以及探索更高效的合成数据验证策略，在保持低成本的同时进一步提升数据质量。

与相关工作的联系方面，本文的数据合成思路与指令微调领域的合成数据研究有共通之处，但核心差异在于路由任务需要同时建模性能与成本两个维度，而非仅追求响应质量。此外，TRouter 的任务类型分解机制与多任务学习中的任务表示学习也有概念上的相似性，但前者更侧重于推断阶段的效用优化，而非训练阶段的参数共享。

## 引用

- Liu, H., Zou, B., Chen, K., Liu, J., Wang, W., & Li, H. (2026). Task-Aware LLM Routing with Multi-Level Task-Profile-Guided Data Synthesis for Cold-Start Scenarios. *arXiv preprint arXiv:2604.09377*. https://doi.org/10.48550/arXiv.2604.09377
