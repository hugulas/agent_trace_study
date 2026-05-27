# FeatureBench: Benchmarking Agentic Coding for Complex Feature Development

## 核心信息

- 标题: FeatureBench: Benchmarking Agentic Coding for Complex Feature Development
- 作者: Qixing Zhou, Jiacheng Zhang, Haiyang Wang, Rui Hao, Jiahe Wang, Minghao Han, Yuxue Yang, Shuzhe Wu, Feiyang Pan, Lue Fan, Dandan Tu, Zhaoxiang Zhang
- 年份: 2026
- 会议/期刊: ICLR 2026
- DOI: 10.48550/arXiv.2602.10975
- 论文链接: https://arxiv.org/abs/2602.10975
- 代码: github.com/LiberCoders/FeatureBench

## 原文摘要翻译

由大语言模型驱动的智能体正越来越多地被软件行业所采用，以协作者甚至自主开发者的身份贡献代码。随着它们的普及，评估当前编码能力边界的重要性日益凸显。然而，现有的智能体编码基准测试覆盖的任务范围有限，例如仅限于单个拉取请求内的错误修复，并且往往依赖不可执行的评估方式，或缺乏持续更新评估覆盖范围的自动化方法。为解决这些问题，我们提出了 FeatureBench，一个旨在评估端到端、面向功能的软件开发中智能体编码性能的基准测试。FeatureBench 采用基于执行的评估协议和可扩展的测试驱动方法，能够以最少的人工工作量自动从代码仓库中派生任务。通过从单元测试出发沿依赖图进行追踪，我们的方法可以识别出横跨开发时间线上分散的多个提交和拉取请求的功能级编码任务，同时确保分离后其他功能的正常运行。利用这一框架，我们在基准测试的首个版本中从24个开源仓库筛选出200个具有挑战性的评估任务和3825个可执行环境。实证评估表明，最先进的智能体模型 Claude 4.5 Opus 在 SWE-bench 上取得了74.4%的解决率，但在本基准的任务上仅成功完成了11.0%，这为推进智能体编码开辟了新的机会。此外，受益于我们的自动化任务采集工具包，本基准可以方便地扩展和更新，以缓解数据泄露问题。所构建环境固有的可验证性也使得我们的方法对智能体训练具有潜在价值。

## 创新点

1. **功能级端到端评估协议** 现有基准大多聚焦单拉取请求内的错误修复，而 FeatureBench 将评估范围扩展到跨多个提交和拉取请求的功能开发任务。这一扩展更贴近真实软件工程中需求驱动开发的场景，能够检验智能体在规划、推理和长程任务管理上的综合能力。

2. **基于依赖图的自动化任务采集管道** 作者提出了一套从开源仓库自动提取功能级任务的工具链。该管道通过动态追踪单元测试运行时的对象依赖关系，构建依赖图，进而自动合成代码补丁、生成前置未解决代码库并撰写问题描述。相比手工构建基准，该方法将人工干预降至最低，同时支持持续更新。

3. **执行验证与后验检查机制** 每个任务实例均配备可执行的 Docker 环境和单元测试套件。通过后验验证确保移除目标功能后，仓库中其余功能仍能正常运行。这种可执行、可验证的设计避免了非执行评估中的歧义，也为智能体训练提供了可靠的环境基础。

4. **可扩展与抗数据泄露的更新机制** 得益于自动化采集工具包，FeatureBench 可以从训练截止日期之后创建的仓库中持续生成新任务实例。这一特性有效缓解了传统基于公开拉取请求的基准所面临的数据污染风险，使评估结果更具可信度。

## 一句话总结

FeatureBench 是一个面向功能级软件开发的智能体编码基准，通过自动化测试驱动采集管道从真实仓库生成200个高难度任务，实证揭示了当前最先进模型在该场景下的成功率骤降至约11%，显著低于其在传统错误修复基准上的表现。

## 研究问题

随着大语言模型在软件开发中的应用日益深入，智能体编码系统正从辅助补全走向自主完成复杂任务。Claude Code、Qwen Code 等工具的出现标志着需求驱动型智能体能够自主规划、执行并与编译器等外部工具交互，将人类角色推向监督层面。然而，现有评估这一范式转变的基准存在明显局限：

- **任务范围狭窄**：SWE-bench 等主流基准主要关注单个拉取请求内的错误修复，缺乏对功能开发场景的覆盖。
- **评估方式受限**：部分基准依赖非可执行的评估，难以准确判定实现是否满足功能要求。
- **采集方式不可扩展**：手工构建或基于预定义轨迹的生成管道难以持续更新，容易导致数据泄露。

因此，论文核心动机是：如何构建一个能够评估智能体在真实、功能级、端到端软件开发场景中能力的基准，并且该基准具备自动化采集、执行验证和持续扩展的特性？

> [!figure] Fig. 1: a) The agent must implement a directly callable feature based on the task description and interface definitions, either by developing from scratch or extending an existing repository. b) Our benchmark shows that even Claude Opus 4.5 achieves only a 11.0% solution rate.
> 建议位置：研究问题 / 数据与任务定义
> 放置原因：展示 FeatureBench 的任务形式（任务描述+接口定义→智能体生成可直接调用的实现）以及当前模型在该基准上的低成功率
> 当前状态：占位符

## 数据与任务定义

**数据集规模**

首个版本的 FeatureBench 包含：
- 200 个评估任务
- 3825 个可执行环境
- 来源于 24 个真实开源 GitHub 仓库
- 任务时间跨度：2022年5月至2025年9月

**任务形式**

每个 FeatureBench 实例向智能体提供：
- 高层任务描述（自然语言）
- 指定的功能接口定义
- 禁止访问的 URL 黑名单（防止作弊）
- 定义执行环境的 Dockerfile

智能体需要在现有代码库基础上进行编辑，或从零开始实现，生成一个满足功能要求且可直接调用的解决方案。

**难度分级**

- **L1（Extend）**：在已有代码库基础上扩展功能，需要理解现有架构并进行增量修改。
- **L2（从零开始）**：完全从零实现指定功能，不依赖现有代码库中的相关实现。L2 显著更难，因为智能体无法复用现有代码结构。

**评估指标**

采用执行验证方式，核心指标为：
- **Resolved Rate**：智能体生成的解决方案是否通过所有单元测试（包括 Fail-to-Pass 和 Pass-to-Pass 测试）。
- **Pass Rate**：测试用例的通过率。
- **Token / Cost**：完成任务消耗的 token 数量和估计成本。

> [!figure] Table 3: Average numbers characterizing different attributes of a SWE-bench task instance, as well as our FeatureBench (L1 set).
> 建议位置：数据与任务定义 / 关键结果
> 放置原因：量化展示 FeatureBench 相比 SWE-bench 在任务复杂度上的大幅提升（问题文本长度、代码行数、文件数、测试数）
> 当前状态：占位符

## 方法主线

FeatureBench 的核心是一套从开源仓库自动生成功能级评估实例的管道。该管道围绕单元测试和依赖图展开，确保生成的任务既反映真实开发场景，又具备可执行验证能力。

### 机制流程

**步骤1：环境初始化与测试选取**

- **输入**：一个 GitHub 代码仓库及其单元测试套件。
- **动作**：通过 Docker 自动搭建开发环境，执行所有单元测试。基于测试结果将测试划分为 Fail-to-Pass（F2P，目标功能缺失时失败）和 Pass-to-Pass（P2P，目标功能缺失后仍应通过，用于验证其他功能未被破坏）。
- **输出**：经过验证的 F2P 和 P2P 测试集合，以及初始代码库状态。

**步骤2：动态追踪与依赖图构建**

- **输入**：F2P 测试集合和完整代码库。
- **动作**：对 F2P 测试进行动态追踪，捕获运行时对象依赖关系，构建对象依赖图。通过图遍历识别与目标功能直接相关的代码路径和函数集合。
- **输出**：对象依赖图，以及依赖图中标记为目标功能独有的函数集合。

**步骤3：代码补丁合成与前置代码库生成**

- **输入**：依赖图标记的目标功能相关代码片段和完整代码库。
- **动作**：提取实现目标功能的代码片段作为黄金补丁（Gold Patch）。将原代码库中目标功能相关代码移除，生成前置未解决代码库（Pre-solved Codebase）。
- **输出**：修改后的前置代码库（缺失目标功能但保持其他功能完整）和互补的黄金补丁代码片段。

**步骤4：问题描述生成与实例封装**

- **输入**：提取的代码片段、前置代码库、对应单元测试。
- **动作**：利用代码片段中的文档字符串自动生成问题描述；若文档缺失，则调用大语言模型从代码片段生成。将问题描述、前置代码库、黄金补丁、单元测试套件和 Docker 环境封装为一个完整实例。
- **输出**：一个完整的 FeatureBench 评估实例，包含自然语言问题描述、未开发代码库、已验证代码补丁和对应单元测试。

> [!figure] Fig. 2: Given a GitHub repository, our automated toolkit initializes the development environment via Docker. For each benchmark instance, it validates and selects fail-to-pass and pass-to-pass tests. Then, the system performs dynamic tracing to capture runtime behavior and construct an object dependency graph. Leveraging this graph, the toolkit synthesizes code patches, derives corresponding pre-solved codebases, and formulates final problem statements.
> 建议位置：方法主线 / 机制流程
> 放置原因：直观展示自动化采集管道的完整流程，帮助理解从仓库到评估实例的转换过程
> 当前状态：占位符

## 关键结果

论文评估了7种框架与模型的组合配置。模型侧覆盖 DeepSeek-V3.2、Claude Opus 4.5 等闭源与开源前沿模型；框架侧包括 OpenHands、Claude Code 等代表性智能体脚手架。

**主要实验结果**

- **Claude Code (routing) + Claude Opus 4.5**：在 Lite 子集上取得最高解决率 20.0%，但在完整测试集上仅为 11.0%。
- **Codex + GPT-5.1-Codex (medium reasoning)**：解决率 12.5%。
- **OpenHands + Claude Opus 4.5**：Lite 子集 10.5%，完整集 6.7%。
- **其他配置**：多数低于 10%，部分甚至为 0%。

作为参照，Claude Opus 4.5 在 SWE-bench 上的解决率为 74.4%，而在 FeatureBench 共享仓库子集上的解决率骤降至 5.2%。这一巨大差距揭示了功能级任务相比错误修复的显著更高难度。

> [!figure] Table 2: The performance of various frontier large models combined with advanced agentic frameworks on the Lite set.
> 建议位置：关键结果
> 放置原因：直接展示各前沿模型与框架组合在 FeatureBench Lite 子集上的核心性能数据
> 当前状态：占位符

> [!figure] Table 4: Compare the performance of the frontier agents on SWE-bench and our FeatureBench, using a subset of our benchmark including only repositories shared with SWE-bench for a fair comparison.
> 建议位置：关键结果
> 放置原因：在相同仓库集合上公平对比 SWE-bench 与 FeatureBench 的性能差距，凸显功能级任务的挑战性
> 当前状态：占位符

**任务复杂度对比**

与 SWE-bench 相比，FeatureBench 任务在多个维度上呈现数量级增长：
- 问题文本长度：4818.0 词 vs 195.1 词
- 黄金解决方案代码行数：790.2 行 vs 32.8 行
- 涉及文件数：15.7 个 vs 1.7 个
- Fail-to-Pass 测试点数：62.7 个 vs 9.1 个
- 总测试点数：302.0 个 vs 120.8 个

## 深度分析

**性能差距的结构性原因**

FeatureBench 上约 11% 的顶尖解决率与 SWE-bench 上 74.4% 的解决率之间存在断崖式差距。这一差距并非偶然，而是源于任务本质的不同：

1. **问题描述复杂度**：FeatureBench 的问题描述平均长度接近 5000 词，是 SWE-bench 的 25 倍。智能体需要理解高层需求、接口定义、参数约束和返回要求，并进行长程规划。
2. **代码修改规模**：平均需要修改近 800 行代码、跨越约 16 个文件，这要求智能体具备系统级的代码理解和架构导航能力。
3. **从零实现 vs 增量修复**：L2 级别任务要求完全从零实现功能，而非在现有代码上打补丁。当前智能体在缺乏现有代码结构参考时，规划能力和实现正确性均大幅下降。

**可见单元测试与接口的影响**

消融实验显示，当智能体获得真实单元测试（而非仅任务描述和接口）时，解决率显著提升。例如，部分模型在可见测试条件下的解决率提升可达 40 个百分点以上，测试通过率也有 20 个百分点的增长。这说明当前智能体在仅凭高层需求描述推导具体测试预期方面存在明显短板。

**执行步数的影响**

将最大执行步数从 50 增加到 500，Gemini-3-Pro-Preview 的解决率从 3.3% 提升至 10.0%，Qwen3-Coder 从 3.3% 提升至 6.7%。这表明智能体在 FeatureBench 上需要大量交互步骤才能接近任务完成，长程规划与执行稳定性仍是核心瓶颈。

**提交时间与特征复杂度的关系**

论文分析了任务通过率与初始提交时间戳、所需代码行数之间的关系。结果显示，通过率与代码长度呈明显负相关，而与提交时间几乎无关。这说明当前模型在 FeatureBench 上的表现差异主要由功能复杂度驱动，而非训练数据的时间分布。不过作者也指出，随着智能体越来越多地参与功能开发，未来数据泄露风险可能会上升。

> [!figure] Table 5: An ablation study to evaluate the necessity of manual verification for the examples generated by our system.
> 建议位置：深度分析
> 放置原因：验证自动采集管道生成样本的可靠性，说明人工修订子集与原数据集性能高度一致
> 当前状态：占位符

## 局限

1. **语言范围限制**：当前版本的 FeatureBench 仅覆盖 Python 仓库，尚未扩展到其他编程语言。这限制了评估结论在多语言软件开发场景下的普适性。

2. **人工验证开销**：虽然采集管道自动化程度较高，但仍需人工验证环节来确保生成的任务实例质量。对于大规模扩展，这部分开销可能成为瓶颈。

3. **L2 任务成功率极低**：在从零实现（L2）的设置下，所有被测模型的解决率均接近或等于零。这表明当前智能体在完全自主的功能开发方面几乎不具备实用能力，也暗示 FeatureBench 在 L2 层面的区分度有限——几乎所有模型都失败。

4. **任务难度分布不均**：不同仓库之间的任务难度差异较大，部分仓库的解决率显著高于其他仓库。这使得跨仓库的平均指标可能掩盖特定类型任务的模型表现差异。

5. **未充分探索的训练价值**：论文提到构建环境的可验证性对智能体训练具有潜在价值，但并未实际开展基于 FeatureBench 的训练实验来验证这一假设。

## 我的笔记

FeatureBench 的提出标志着一个重要的认知转变：智能体编码的评估正从修复缺陷走向功能开发。SWE-bench 曾经定义了编码智能体的黄金标准，但其在一年内从不到10%的解决率迅速攀升至超过70%，说明错误修复任务的难度天花板已经显现。FeatureBench 将评估焦点转向更贴近工业实践的功能开发，这既是必要的，也是及时的。

从技术设计角度看，基于依赖图的自动采集管道是一个亮点。通过动态追踪单元测试构建对象依赖图，再反向提取功能相关代码片段，这种方法巧妙地绕过了手工标注的瓶颈。不过，该管道对测试覆盖率较高的项目效果更好；对于测试稀疏的遗留代码库，依赖图可能不完整，导致生成的任务质量下降。

一个值得关注的发现是可见单元测试的巨大影响。当智能体获得真实测试后，性能提升极为显著。这提示了一种可能的工程路径：在需求描述不够精确时，提供高质量的测试规范可能比单纯扩大模型规模更有效。不过这也引发了评估公平性的问题——在真实开发中，测试往往也需要智能体自行设计。

在与相关工作的对比中，SWE-Flow 等同期工作也尝试从仓库自动生成数据，但它们忽略了 Pass-to-Pass 测试，也未保证未开发代码库中其他功能的完整性。FeatureBench 通过后验验证填补了这一差距，使其任务设定更贴近真实开发环境。

未来方向方面，我认为 FeatureBench 的设计天然适合作为智能体训练环境。其可执行、可验证的特性使其能够支持强化学习或在线学习范式。如果后续研究能结合 FeatureBench 开展训练实验，可能会催生新一代专门面向功能开发的代码智能体。

## 引用

```bibtex
@article{zhou2026featurebench, title={FeatureBench: Benchmarking Agentic Coding for Complex Feature Development}, author={Zhou, Qixing and Zhang, Jiacheng and Wang, Haiyang and Hao, Rui and Wang, Jiahe and Han, Minghao and Yang, Yuxue and Wu, Shuzhe and Pan, Feiyang and Fan, Lue and Tu, Dandan and Zhang, Zhaoxiang}, journal={arXiv preprint arXiv:2602.10975}, year={2026}}
```
