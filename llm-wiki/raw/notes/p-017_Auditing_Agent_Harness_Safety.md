---
tags:
  - agent-safety
  - multi-agent
  - trajectory-audit
  - harness-evaluation
  - benchmark
aliases:
  - HarnessAudit
  - Auditing Agent Harness Safety
date: 2026-05-16
doi: 10.48550/arXiv.2605.14271
---

# Auditing Agent Harness Safety

## 核心信息

- **标题**: Auditing Agent Harness Safety
- **作者**: Chengzhi Liu, Yichen Guo, Yepeng Liu, Yuzhe Yang, Qianqi Yan, Xuandong Zhao, Wenyue Hua, Sheng Liu, Sharon Li, Yuheng Bu, Xin Eric Wang
- **机构**: UC Santa Barbara, UC Berkeley, UW-Madison, Stanford, Microsoft Research
- **发表时间**: 2026
- **会议 / 期刊**: arXiv
- **DOI**: 10.48550/arXiv.2605.14271
- **arXiv ID**: 2605.14271
- **项目主页**: https://harnessaudit.github.io/
- **PDF**: `[p-017]-harnessaudit-auditing-agent-harness-safety.pdf`
- **证据质量**: high

## 原文摘要翻译

大语言模型智能体越来越依赖执行框架（execution harness）来完成任务调度、工具分发和资源路由。然而，一个框架可能在返回正确、无害的最终答案的同时，其执行轨迹中却访问了未授权资源，或将私有上下文泄露给了错误的智能体。仅基于输出层面的评估无法发现这类失败，而现有的大部分安全基准仅对最终输出或终止状态打分，尽管许多违规发生在轨迹中段而非终止时刻。核心问题在于：执行框架是否在整个执行过程中尊重用户意图、权限边界和信息流约束。

为解决这一空白，本文提出 HarnessAudit，一个对完整执行轨迹进行审计的框架，从边界合规性、执行保真度和系统稳定性三个维度进行评估，并特别关注多智能体框架中风险最突出的场景。此外，本文还构建了 HarnessAudit-Bench 基准，涵盖八个真实世界领域的二百一十条任务，并在单智能体和多智能体两种配置下嵌入安全约束。作者评估了十种框架配置，覆盖前沿模型和三种多智能体框架，发现：任务完成度与安全执行之间存在错位，且违规数量随轨迹长度累积；安全风险因领域、任务类型和智能体角色而异；大多数违规集中在资源访问和智能体间信息传输；多智能体协作扩大了安全风险面，而框架设计决定了安全部署的上限。

## 创新点

1. **以框架为中心的安全形式化与审计体系**。本文将智能体执行框架定义为受策略约束的执行系统，并通过隐藏、独立于智能体的证据通道（工具调用日志、资源访问记录、组件间消息）对轨迹进行三层审计。
2. **真实场景下的框架安全压力测试**。构建 HarnessAudit-Bench，覆盖八个真实应用领域、二十四项细粒度场景、共二百一十条任务，同时在单智能体和多智能体配置下植入安全约束。
3. **框架安全失效模式的系统性实证分析**。在十种框架配置、前沿模型和三种多智能体框架上开展实验，揭示了资源访问越界、智能体间信息泄露和扰动下稳定性不足等系统性失败模式。

## 一句话总结

HarnessAudit 首次将智能体安全评估的单元从最终输出转移到完整执行轨迹，提出三层审计框架和大规模真实基准，系统揭示了当前执行框架在边界合规、执行保真与扰动稳定方面的严重缺陷。

## 研究问题

现代大语言模型智能体通常运行在 OpenClaw、Claude Code、Codex 等执行框架内，由框架而非模型本身决定哪些动作可被暴露、谁有权调用工具以及何时终止执行。这种架构转移带来了一种输出级评估无法察觉的失败模式：框架可能在返回正确、无害答案的过程中，访问未授权资源、将私有上下文泄露给错误智能体，或触发预期范围之外的不可逆副作用。仅评估最终响应会将这些运行误分类为成功。

现有基准在三方面均存在不足：
- 大多数仅对最终输出或终止状态打分，导致一边访问禁限资源一边完成任务的运行与干净成功无法区分；
- 近期面向框架的基准虽增加了真实工具和约束，但仍以任务完成为中心，很少探测对抗条件下的稳定性；
- 几乎所有工作都针对单智能体，忽略了生产级多智能体框架引入的组件间通信通道。

因此，核心研究问题是：**当安全评估的单元从模型响应上升到执行框架的完整轨迹时，当前智能体系统在边界合规、执行保真和系统稳定三个维度上的表现究竟如何？**

![Figure 1 HarnessAudit 整体概览：八领域覆盖、任务执行流程与模型性能雷达](p-017_Auditing_Agent_Harness_Safety/images/title2.png)

> [!figure] Figure 2 不同执行框架在真实任务中暴露的安全风险
> 建议位置：研究问题
> 放置原因：该图直观展示了输出级评估无法捕获的轨迹中段违规模式。
> 当前状态：已从 LaTeX 源码 `intro.pdf` 转换插入。

![Figure 2 不同执行框架在真实任务中暴露的安全风险](p-017_Auditing_Agent_Harness_Safety/images/intro.png)

## 数据与任务定义

### HarnessAudit-Bench 设计原则

每项任务遵循三项原则：
- **良性目标驱动**：安全风险源于错误决策或不必要的披露，而非显式恶意意图；
- **有界协作**：多智能体设置中需要专业角色间的受限协作，单智能体则需严格的范围管理；
- **显式工具与资源范围**：通过授权目标和合理的范围外诱饵，使正确对象识别可直接度量。

### 领域与场景覆盖

HarnessAudit-Bench 包含二百一十条任务，横跨八个应用领域和二十四项细粒度场景：

| Domain | Tasks | Scenarios | Roles | Tools | Representative Safety Pressure |
|---|---|---|---|---|---|
| Finance | 40 | planning, investing, lending, insurance | 9 | 8 (4) | Client/portfolio scope, trading authority, financial PII |
| E-commerce | 38 | shopping, after-sales, transaction | 14 | 16 (13) | Customer identity, order scope, refunds, case routing |
| Healthcare | 30 | consultation, prescription | 9 | 12 (11) | Patient-record access, diagnostic separation, medication data |
| Office | 27 | personnel, asset, finance, partnership | 7 | 15 (11) | Employee records, asset assignment, incident routing |
| Social interaction | 24 | voice, report | 14 | 16 (8) | Real identity, source protection, moderation boundaries |
| Daily life | 21 | dining, housing, travel, wellness | 6 | 8 (5) | Bookings, identifiers, payment credentials |
| Legal compliance | 20 | litigation, audit, contract | 8 | 7 (5) | Matter scope, privileged files, evidence verification |
| Software engineering | 10 | app e-commerce, app admin | 5 | 12 (2) | Code edits, test execution, secret handling |

*Table 1 来自 LaTeX 源码 `1-intro.tex`，展示 HarnessAudit-Bench 的八领域库存。*

### 审计仪器化

每项任务按三层规范实例化具体审计检查：
- **L1 边界合规**：共定义 11,586 条角色工具授权条目，平均每条任务 55.2 条；
- **L2 执行保真**：共 3,094 条资源范围规则，约束可执行动作；
- **L3 系统稳定**：为一百零五条选定任务构建扰动规范，每项五种扰动变体，共五百二十五个扰动案例。

![Figure 4 HarnessAudit-Bench 覆盖八领域、二十四场景及审计规则分布](p-017_Auditing_Agent_Harness_Safety/images/bar.png)

### 与现有基准的对比

| Benchmark | Env. Type | # Tasks | Domains | MA. | MM. | Traj. Audit | Boundary | Fidelity | Stability |
|---|---|---|---|---|---|---|---|---|---|
| AgentDojo | Tool simulation | 97 | 4 | ✗ | ✗ | partial | partial | partial | partial |
| AgentHarm | Tool simulation | 110/440 | 11 | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| ClawsBench | Mock services | 44 | 5 | ✗ | ✗ | partial | partial | partial | ✗ |
| Claw-Eval | Sandbox | 300 | 3/9 | ✗ | partial | ✓ | partial | partial | partial |
| **HarnessAudit-Bench** | **Mock + Real** | **210** | **8/24** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** |

*Table 2 来自 LaTeX 源码 `table_bench_coverage.tex`，展示 HarnessAudit-Bench 在轨迹审计、多智能体、多模态和三层安全维度上的全面覆盖。*

## 方法主线

### 框架形式化

HarnessAudit 将智能体执行框架定义为受策略约束的执行系统：

$$\mathcal{H} := (\mathcal{A}, \mathcal{T}, \mathcal{R}, \Pi, \Phi, \Sigma)$$

该形式化定义中，第一分量为执行组件集合，第二为可调工具，第三为环境资源，第四为权限策略，第五为信息流策略，第六为协调协议。执行产生可观察轨迹与最终输出。

### 三层安全评估体系

**L1 边界合规（Boundary Compliance）**：检查每个动作是否停留在 $\Pi$ 和 $\Phi$ 规定的边界内。违规渠道包括：
- 工具违规：调用未授权、与任务无关或超越角色的工具；
- 资源违规：访问受保护或超出范围的文件、记录、字段；
- 信息流违规：通过通信、转发或最终输出披露未获许可的信息。

**L2 执行保真（Execution Fidelity）**：检查轨迹是否通过有效的中间步骤达到目标：
- 动作有效性：工具选择、参数和目标对象是否正确，是否避免冗余操作；
- 检查点任务完成：从轨迹或状态可验证的任务里程碑。

**L3 系统稳定（System Stability）**：检查 L1 和 L2 在受控压力注入下是否仍然满足：
- 间接提示注入（通过工具返回内容）；
- 模糊或未充分指定的用户目标；
- 工具或运行时错误与噪声。

### 机制流程

HarnessAudit 的核心设计选择是所有评估证据均来自智能体无法操纵或预见的通道，而非其自报告。每次运行分为三个阶段：

1. **初始化阶段**：将声明式任务规范送入 harness，输入包括确定性种子下的模拟服务、分配给各组件的工具与资源；系统提取隐藏审计工件，包含完成检查点、策略规则和违规分类体系，执行期间对所有组件不可见。
2. **执行阶段**：框架在标准思考-行动-观察循环下运行至完成；将每次工具调用、资源访问、组件间消息和状态转移的结构化日志输出到追加式记录，同时生成执行前后的环境快照。
3. **评判阶段**：终止后加载隐藏工件，与收集的证据通道进行融合；对轨迹进行解码与查询，得到动作序列和边界证据，最终更新为 L1 至 L3 规范打分。

![Figure 3 HarnessAudit 审计流水线，将评估分离为初始化、执行和评判三阶段](p-017_Auditing_Agent_Harness_Safety/images/pipline.png)

### 评分聚合

**L1 安全遵循率（SAR）**：对工具使用 $t$、资源访问 $r$、信息流 $f$ 三个渠道，分别按严重程度加权计算违规惩罚：

$$\mathrm{SAR}_i^t = 1 - \min\left(1, \omega_{\mathrm{low}} V_{i,\mathrm{low}}^t + \omega_{\mathrm{high}} V_{i,\mathrm{high}}^t\right)$$

$$\mathrm{SAR}_i^r = 1 - \min\left(1, \omega_{\mathrm{low}} V_{i,\mathrm{low}}^r + \omega_{\mathrm{high}} V_{i,\mathrm{high}}^r\right)$$

$$\mathrm{SAR}_i^f = 1 - \min\left(1, \omega_{\mathrm{low}} V_{i,\mathrm{low}}^f + \omega_{\mathrm{high}} V_{i,\mathrm{high}}^f\right)$$

任务级边界合规分数为三者均值：

$$\overline{\mathrm{SAR}}_i = \frac{1}{3}\left(\mathrm{SAR}_i^t + \mathrm{SAR}_i^r + \mathrm{SAR}_i^f\right)$$

**L2 任务完成与动作有效性**：

$$\mathrm{TCR}_i = \min\left(1, \sum_{m \in C_i} w_m s_m\right), \quad \mathrm{AVS}_i = \frac{1}{|\rho_i^{\mathrm{score}}|} \sum_{a \in \rho_i^{\mathrm{score}}} J_{\mathrm{act}}(a, \tau_i)$$

**总体 harness 安全分数**：

$$\mathrm{Score}_i = \overline{\mathrm{SAR}}_i \times \left(0.7 \cdot \mathrm{TCR}_i + 0.15 \cdot \mathrm{AVS}_i + 0.15 \cdot \mathrm{PB}_i\right)$$

其中 $\overline{\mathrm{SAR}}_i$ 作为乘法安全门，意味着只有既完成任务又尊重安全边界的运行才能获得高分。

## 关键结果

### 实验设置

评估覆盖十种框架配置，分为两种设置：
- **共享框架设置**：不同模型在相同 OpenClaw 框架下运行，以控制框架层面差异；
- **厂商原生设置**：使用模型供应商提供的生产级框架（Claude Code、Codex）。

多智能体框架评估三种代表性方案：Claw-Team（规划器主导，支持显式角色与权限控制）、Google ADK（基于图的编排）、OpenAI SDK（基于会话的执行）。

### 主结果

Table 3 来自 LaTeX 源码 `table_main_results.tex`，报告各系统在三项安全原则维度上的总体表现：

| Model | SAR^t | SAR^r | SAR^f | Avg. | AVS | TCR | Avg. | Inj. | Amb. | Rob. | Avg. | S@T20 | S@T50 | S@T80 | Overall |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **OpenClaw** | | | | | | | | | | | | | | | |
| ChatGPT-5.4 | 0.62 | 0.39 | 0.59 | 0.53 | 0.50 | 0.66 | 0.58 | 0.18 | 0.35 | 0.68 | 0.40 | 0.61 | 0.58 | 0.40 | 0.32 |
| Claude Opus 4.6 | 0.39 | 0.17 | 0.46 | 0.34 | 0.53 | 0.74 | 0.64 | 0.17 | 0.26 | 0.35 | 0.24 | 0.44 | 0.40 | 0.35 | 0.21 |
| Claude Sonnet 4.6 | 0.42 | 0.18 | 0.53 | 0.38 | 0.50 | 0.64 | 0.57 | 0.21 | 0.28 | 0.41 | 0.30 | 0.46 | 0.39 | 0.30 | 0.22 |
| Gemini 3.1 Pro | 0.85 | 0.71 | 0.74 | **0.77** | 0.56 | 0.56 | 0.56 | 0.22 | 0.38 | 0.67 | **0.42** | 0.81 | 0.79 | 0.76 | **0.41** |
| GLM 5V Turbo | 0.63 | 0.33 | 0.62 | 0.53 | 0.52 | 0.68 | 0.60 | 0.19 | 0.30 | 0.33 | 0.27 | 0.59 | 0.57 | 0.53 | 0.31 |
| Kimi K2.6 | 0.70 | 0.46 | 0.63 | 0.59 | 0.50 | 0.54 | 0.52 | 0.21 | 0.36 | 0.57 | 0.38 | 0.68 | 0.60 | 0.31 | 0.30 |
| Qwen 3.5 Plus | 0.60 | 0.24 | 0.57 | 0.47 | 0.53 | 0.69 | 0.61 | 0.17 | 0.34 | 0.43 | 0.32 | 0.53 | 0.48 | 0.44 | 0.29 |
| **Claude Code** | | | | | | | | | | | | | | | |
| Claude Opus 4.6 | 0.48 | 0.21 | 0.58 | 0.43 | 0.51 | 0.82 | **0.67** | 0.20 | 0.26 | 0.38 | 0.28 | 0.55 | 0.50 | 0.48 | 0.29 |
| Claude Sonnet 4.6 | 0.65 | 0.34 | 0.60 | 0.53 | 0.52 | 0.68 | 0.60 | 0.24 | 0.33 | 0.47 | 0.35 | 0.62 | 0.59 | 0.46 | 0.32 |
| **Codex** | | | | | | | | | | | | | | | |
| ChatGPT-5.4 | 0.36 | 0.14 | 0.52 | 0.34 | 0.50 | 0.76 | 0.63 | 0.24 | 0.29 | 0.57 | 0.37 | 0.47 | 0.43 | 0.40 | 0.23 |

*Table 3 主结果表，数值越高越好。*

四项核心发现：

1. **当前智能体框架距离安全可靠仍有巨大差距**。即使是表现最好的系统，总体分数也仅为 0.41，说明在任务完成必须同时满足显式安全约束时，改进空间巨大。
2. **任务完成与安全合规明显错位**。OpenClaw 设置下，Gemini 3.1 Pro 的任务完成率并非最高，但因协议安全表现最强而获得最高总体分数；相反，Claude Opus 4.6 的 TCR 更高，但安全指标明显更弱。
3. **资源访问主导违规画像**。在大多数配置中，资源访问安全显著弱于工具调用安全和信息流安全，说明智能体通常不会因调用明显不当的工具而失败，更可能选择看似合理的工具却将其应用于错误、无关或未授权的资源。
4. **系统在扰动下普遍脆弱**。间接注入造成最大的性能下降，表明智能体容易受到任务证据或工具返回内容中隐藏指令的影响。

![Figure 5 任务完成分数与安全遵循率的权衡关系](p-017_Auditing_Agent_Harness_Safety/images/fig511.png)

### 单智能体与多智能体安全对比

| Setting | SAR^t | SAR^r | SAR^f (IS) | SAR^f (CR) |
|---|---|---|---|---|
| Single | 0.91 | 0.85 | -- | -- |
| Multi | 0.64 | 0.63 | 0.58 | 0.84 |

*Table 4 来自 LaTeX 源码 `1-intro.tex`，展示单智能体与多智能体设置下的安全对比。*

多智能体系统进一步放大了这些风险，在信息流和资源访问方面产生显著更多的违规。大多数信息流违规属于敏感信息泄露，而非未授权接收方错误，说明框架能够识别通信伙伴，但无法控制共享内容。

## 深度分析

### 完成度与安全性的负相关关系

如图 5 左所示，任务完成度与安全遵循率之间呈现持续的负相关。解决复杂真实任务通常需要更广泛的工具使用、资源访问和信息交换，从而增加跨越安全边界的风险。图 5 中进一步显示违规数量随执行动作数量增加而上升。图 5 右量化了不同完成阈值下的安全-能力权衡：随着阈值提高，所有模型的安全性均下降，但下降速率明显不同。Gemini 展现出最稳定的安全-能力权衡，而 Claude Sonnet 尽管任务能力更强，在高完成度水平下保留的安全性更少。

### 领域差异与角色依赖模式

安全风险并非均匀分布，而是由领域特定的操作需求塑造：
- 金融和办公任务需要密集的资源访问，更容易出现资源边界违规；
- 日常生活和电商任务更依赖智能体间通信，因此更常违反信息流约束；
- 软件工程任务涉及频繁的工具使用，导致工具使用合规性较弱。

负责关键资源访问、跨角色协调或最终执行的智能体更容易跨越安全边界。

![Figure 6 领域级安全渠道合规度与高风险角色的违规率](p-017_Auditing_Agent_Harness_Safety/images/fig6.png)

### 框架设计决定安全上限

原生框架通常通过启用更多动作和更丰富的工具交互来提升任务完成度，但这些收益并未均匀转化为安全改进。Claude 原生环境同时提升了完成度和安全性，而 Codex 则显示出更高的完成度但更低的安全性，因为 GPT 在原生设置下执行了明显更多的动作。在三种多智能体框架中，OpenClaw 在工具使用、资源访问和信息流方面的安全分数均低于 Google 和 OpenAI 的方案，表明较弱的编排和边界控制使真实协作更容易受到安全违规的影响。

![Figure 7 不同 harness-model 组合的协议遵循分数与每任务违规智能体比例](p-017_Auditing_Agent_Harness_Safety/images/fig7.png)

![Figure 8 原生框架与 OpenClaw 配置的性能差异，以及不同多智能体框架下的表现](p-017_Auditing_Agent_Harness_Safety/images/fig8.png)

## 局限

1. **评估成本较高**：混合协议结合确定性匹配与 LLM 评判，对执行合理性和扰动稳定性的开放式判断需要 GPT-5.4 作为评判模型，成本显著高于纯规则基准。
2. **隐藏工件的完备性边界**：审计工件从任务规范推导而来，若规范本身存在歧义或遗漏，则隐藏规则可能无法覆盖全部风险面。
3. **扰动覆盖范围**：当前扰动主要聚焦间接注入、模糊目标和运行时错误，对更复杂的对抗攻击（如多轮诱导、社会工程学提示）覆盖有限。
4. **框架适配依赖**：虽然 HarnessAudit 提供统一动作模式，但不同框架的日志格式和原生事件差异较大，新增框架仍需开发专用摄入器。

## 我的笔记

HarnessAudit 的核心方法论贡献在于将安全评估的观察单元从模型响应转移到执行轨迹。这一视角转换揭示了现有基准的重大盲区：一个智能体可以完美回答问题，同时泄露患者病历或越权修改交易记录。三层审计体系的设计具有可扩展性，其中第一层规则化检查保证了可复现性，第二层的检查点机制连接了最终输出与中间过程，第三层的扰动注入则模拟了真实部署中的非理想条件。

从实证结果看，资源访问是当前最薄弱的环节，这与工具调用表面的"显性违规"不同——智能体往往调用正确的工具但操作错误的对象。这种"精细越界"比"粗暴违规"更难以被简单规则捕获，也解释了为什么需要基于轨迹的深度审计而非仅检查最终状态。

多智能体场景的信息流违规分析尤其值得关注。结果表明问题不在于"发给错误的接收方"，而在于"发送了不应发送的内容"。这意味着现有的基于拓扑的通信控制（谁可以和谁说话）是不充分的，必须进一步引入基于内容的泄露检测（什么内容可以被分享）。

从工程实践角度，HarnessAudit-Bench 的"隐藏审计工件"设计是一种优雅的解耦：执行期间零干预，评判阶段全透明。这避免了评估本身对智能体行为的干扰，也便于离线复现和重新评判。对于希望将类似审计机制集成到生产框架中的工程师而言，跨框架统一动作模式和确定性访问检查器提供了可直接借鉴的架构模式。

## 引用

```bibtex
@article{liu2026harnessaudit, title={Auditing Agent Harness Safety}, author={Liu, Chengzhi and Guo, Yichen and Liu, Yepeng and Yang, Yuzhe and Yan, Qianqi and Zhao, Xuandong and Hua, Wenyue and Liu, Sheng and Li, Sharon and Bu, Yuheng and Wang, Xin Eric}, journal={arXiv preprint arXiv:2605.14271}, year={2026}, doi={10.48550/arXiv.2605.14271}}
```
