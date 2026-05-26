---
tags:
  - agent-observability
  - failure-diagnosis
  - github
  - microsoft
  - agentrx
aliases:
  - "AgentRx"
  - "microsoft/AgentRx"
date: 2026-03-11
url: https://github.com/microsoft/AgentRx
---

# GitHub — microsoft/AgentRx

## 核心信息

- **标题**: GitHub — microsoft/AgentRx
- **来源**: Microsoft Research 官方开源仓库
- **类型**: GitHub 仓库与 README 文档
- **日期**: 2026-03-11
- **URL**: https://github.com/microsoft/AgentRx
- **本地文件**: `[a-002]-github--microsoftagentrx.pdf`
- **证据质量**: high（官方发布，可直接运行复现）

## 内容摘要

AgentRx 是由 Microsoft Research 开源的一款面向 AI Agent 执行轨迹的自动化失败诊断框架，其核心目标是在复杂、长程、多智能体的执行过程中，精准定位导致任务失败的第一个关键步骤（critical failure step），并给出可审计的失败归因。与传统仅关注最终任务是否成功的评估方式不同，AgentRx 将诊断粒度下沉到单步级别，通过约束合成与逐步验证，将失败诊断从黑盒猜测转变为白盒证据驱动。

该框架的整体处理流程可概括为六个阶段：

1. Raw logs（原始日志）
2. Trajectory IR（轨迹中间表示）
3. Invariants（不变量/约束）
4. Checker（检查器）
5. Judge（裁决器）
6. Reports（诊断报告）

首先，框架将来自不同领域、不同格式的原始执行日志归一化为统一的 Trajectory IR，这一步解决了跨域复用的前提问题。随后，系统基于领域策略、工具 schema 与执行前缀，自动生成静态不变量（static invariants）和动态不变量（dynamic invariants）。

静态不变量覆盖以下维度：
- 策略合规性
- 工具调用格式正确性
- 结构约束满足度

动态不变量则是针对每一步执行上下文生成的特定约束，具有上下文感知能力。接下来，Checker 模块逐条评估不变量是否被违反，并生成带有证据的审计日志。最终，LLM-based Judge 根据约束违反日志定位关键失败步骤，并将失败归入一个包含十个类别的 grounded taxonomy。

AgentRx 在三个差异显著的应用领域进行了验证：

- 结构化 API 工作流（Tau-bench 零售客服）
- 事故管理（Flash 编排器轨迹）
- 开放式网页与文件任务（Magentic-One 多智能体）

这种跨域设计体现了框架的 domain-agnostic 特性——只要提供相应的领域策略和工具 schema，即可将同一套诊断管道迁移到新场景。仓库内置了示例轨迹（`trajectories/` 目录），支持通过 `python run.py trajectory.json` 一键运行端到端管道，也支持按阶段逐步执行，方便开发者调试和审计中间结果。

配置方面，AgentRx 默认使用 Azure OpenAI 端点，也支持 Microsoft Research 内部的 TRAPI 端点（外部团队建议使用 `--endpoint azure`）。认证采用 Azure AD token 或 Managed Identity。仓库提供了 `.env.example` 模板，开发者只需复制并填入端点地址与模型部署名即可开始本地开发。此外，框架为未知格式的日志提供了基于 LLM 的 IR fallback，降低了接入门槛。

在失败分类方面，AgentRx 定义了一套包含十个类别的 grounded taxonomy：

- Instruction/Plan Adherence Failure（指令/计划遵循失败）
- Invention of New Information（信息虚构）
- Invalid Invocation（无效工具调用）
- Misinterpretation of Tool Output（工具输出误读）
- Intent-Plan Misalignment（意图与计划错位）
- Underspecified User Intent（用户意图欠指定）
- Intent Not Supported（意图不被支持）
- Guardrails Triggered（安全护栏触发）
- System Failure（系统基础设施错误）
- Inconclusive（证据不足无法归类）

这一分类法不仅为失败归因提供了结构化输出，也为后续修复动作指明了方向。

从工程结构来看，AgentRx 的代码组织清晰，采用标准 Python 包结构。主入口为 `run.py`，包配置使用 `pyproject.toml`，依赖管理通过 `requirements.txt` 完成。核心模块包括：

- `agentrx/ir/`：负责将原始日志归一化为 Trajectory IR
- `agentrx/invariants/`：负责不变量的生成与检查
- `agentrx/judge/`：负责 LLM-as-a-Judge 评估与根因分类
- `agentrx/llm_clients/`：封装 Azure OpenAI 与 TRAPI 客户端
- `agentrx/pipeline/`：包含全局配置与工具函数
- `agentrx/reports/`：负责分析与可视化

此外，仓库还包含：
- `data/` 目录：存放领域策略与工具 schema
- `trajectories/` 目录：存放样本轨迹
- `runs/` 目录：存放每次运行的输出结果

这种模块化的目录设计使得每个阶段都可以独立运行和替换，便于学术复现与工业集成。

在快速开始方面，AgentRx 支持两种安装方式：

1. 本地克隆后通过 `pip install -e .` 进行可编辑安装
2. 直接通过 `pip install git+https://github.com/microsoft/AgentRx.git` 从 GitHub 安装

安装完成后，开发者需要复制 `.env.example` 为 `.env` 并填入 Azure 或 TRAPI 的端点信息。对于本地开发，可以设置 `AZURE_TOKEN_CREDENTIALS=dev` 以跳过 ManagedIdentity IMDS 探测。运行完整管道的命令为 `python run.py trajectory.json`，也可通过 `--domain tau` 显式指定领域。

分阶段使用的流程设计得非常细致：

- 第一阶段 IR 归一化：生成 `trajectory_ir.json`
- 第二阶段静态不变量：输出 `static_invariants.json`
- 第三阶段动态不变量：按步骤生成，存放在 `dynamic_invariants/` 目录
- 第四阶段检查器：评估结果写入 `checker_results/`
- 第五阶段 Judge：输出进入 `judge_output/`
- 第六阶段报告：生成失败频率图表等可视化结果

这种分阶段设计不仅便于调试，也使得研究者可以在任意中间阶段插入自定义逻辑。

支持的三个领域中：

- `--domain tau`：Tau-bench 零售客服场景
- `--domain flash`：Flash 事故编排与运维场景
- `--domain magentic`：Magentic-One 多智能体网页与文件操作场景

框架具备自动域检测能力，当输入格式未知时会回退到基于 LLM 的 IR 生成，这一设计显著提升了框架的通用性。

## 关键要点

1. **轨迹级诊断而非结果级评估**
   AgentRx 不满足于"任务是否成功"的二元判断，而是深入执行轨迹内部，定位第一个不可恢复的关键失败步骤，使诊断结果可直接指导工程修复。

2. **约束驱动的证据生成**
   通过将领域策略与工具 schema 自动编译为可执行的不变量，Checker 模块生成的约束违反日志是可审计、可复现的，避免了纯 LLM 猜测的不稳定性。

3. **六阶段可拆分管道**
   从 IR 归一化到报告生成的完整链路被拆分为六个独立阶段，每个阶段均可单独运行并持久化中间结果（`runs/<run_name>/`），便于大规模批量诊断与增量调试。

4. **跨域复用与开箱即用**
   内置对 Tau-bench、Flash、Magentic-One 三个域的支持，且提供自动域检测与 LLM-based fallback，使框架在缺乏人工适配的情况下也能处理新格式日志。

5. **十类失败分类法**
   Grounded taxonomy 覆盖了从高层意图对齐到底层系统故障的完整谱系，为构建统一的 agent 失败基准数据集提供了类别框架。

6. **生产级认证与部署**
   支持 Azure AD token、Managed Identity 等企业级认证方式，配置通过环境变量管理，符合 Microsoft 内部及外部企业的安全合规要求。

7. **模块化代码架构**
   `ir`、`invariants`、`judge`、`llm_clients`、`pipeline`、`reports` 六大子包职责分明，方便二次开发与学术复现。

8. **多种安装与使用模式**
   既支持端到端一键运行，也支持分阶段逐步执行，还提供了直接从 GitHub 安装的便捷途径，降低了使用门槛。

## 与综述的关联

AgentRx 是综述中"失败定位与归因"技术路线的重要工程落地案例。综述在执行轨迹定义、失败诊断管道架构以及跨域可复用性等章节多次引用 AgentRx 作为 state-of-the-art 实现 [a-001][a-002][a-004]。具体而言：

- **轨迹中间表示（Trajectory IR）**
  综述将 AgentRx 的 IR 归一化层作为跨域 trace 统一格式的工程参考，说明其如何通过读取 OpenAPI schema 与自然语言策略实现一次性生成、跨域复用。

- **约束合成与检查**
  AgentRx 的 static/dynamic invariant 生成机制为综述中"守卫式检查器"（guardian checker）概念提供了具体实现范式，展示了如何将高层策略自动下沉为逐步可验证的规则。

- **失败分类法**
  综述在讨论 agent 失败分类基准时，直接采用 AgentRx 的十类 taxonomy 作为分类框架，并指出其 115 条人工标注失败轨迹是目前该领域最系统的公开基准之一。

- **与观测性栈的衔接**
  AgentRx 的输入是原始执行日志，输出是结构化诊断报告，这使其天然位于观测性 pipeline 的"分析层"，与 OpenTelemetry 等采集层、LangSmith 等平台层形成互补。

- **数值证据**
  综述提到 AgentRx 在关键失败步骤定位上相比基线取得了 23.6% 的绝对提升，在根因归因上取得了 22.9% 的提升，这些数据来自 AgentRx 论文实验，而本仓库是这些实验的完整代码实现。

## 我的笔记

AgentRx 的设计哲学值得在综述中重点展开：它将"诊断"视为一个独立于"执行"的工程环节，通过引入 Trajectory IR 和约束合成，把原本需要人工逐行阅读日志的调试工作自动化。这种分层思想——采集层（原始日志）→ 表示层（IR）→ 规则层（不变量）→ 证据层（检查器）→ 判断层（Judge）→ 应用层（报告）——为 agent 可观测性提供了一个完整的方法论闭环。

从工程复现角度，该仓库的 CLI 设计非常友好。`python run.py trajectory.json --stage ir` 等分阶段命令降低了调试成本，而 `runs/` 目录的持久化设计使得批量评估与历史对比变得容易。对于希望在综述中补充实验验证的读者，可以直接使用仓库提供的 `trajectories/` 样本数据进行端到端复现。安装过程也很简洁，`pip install -e .` 或直接从 GitHub 安装均可快速搭建环境。

在代码架构层面，AgentRx 遵循了 Python 包的最佳实践：使用 `pyproject.toml` 管理包元数据，`requirements.txt` 锁定依赖，`cli.py` 提供 console script 入口。`ir`、`invariants`、`judge` 三个子包的划分对应了数据处理、规则生成、智能判断三个核心职责，这种高内聚低耦合的结构便于社区贡献者针对单一模块进行优化或替换。

需要进一步追踪的问题包括：

- 动态不变量的生成成本（每一步都调用 LLM 可能带来显著延迟与费用）
- 十类 taxonomy 在多智能体场景下的互斥性与覆盖度
- Judge 模块对 LLM 模型版本的敏感性
- 对 Anthropic Claude、Google Gemini 等非 Azure 端点的适配情况

另一个值得关注的方向是 AgentRx 与 CI/CD 流水线的集成潜力。由于支持命令行一键运行与结构化 JSON 输出，它可以被嵌入到自动化测试或回归验证流程中，作为 agent 质量的门禁（gate）工具。未来如果能够将诊断报告与代码变更（diff）关联起来，将形成从代码提交到失败归因的完整 DevOps 闭环。

此外，AgentRx 的失败分类法在实际落地时可能需要根据具体业务领域进行扩展。例如，金融领域的 agent 可能需要增加"合规性检查失败"这一类别，而医疗领域则可能需要"隐私数据泄露风险"类别。如何在不破坏原有 taxonomy 一致性的前提下进行领域化扩展，是一个值得后续研究的问题。
