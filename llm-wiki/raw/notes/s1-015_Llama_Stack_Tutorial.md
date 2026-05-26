---
tags:
  - llama-stack
  - red-hat
  - tutorial
  - opentelemetry
  - observability
  - llama-guard
  - mcp
  - rag
  - react
  - github-repo
aliases:
  - "Llama Stack Tutorial"
  - "Red Hat Llama Stack 教程"
date: 2025-03-19
url: https://github.com/rh-aiservices-bu/llama-stack-tutorial
---

# Llama Stack Tutorial

## 核心信息

- **标题**: Llama Stack Tutorial
- **来源**: Red Hat AI Services Business Unit（rh-aiservices-bu）
- **类型**: GitHub 教程仓库与动手实验指南
- **日期**: 2025-03-19
- **URL**: https://github.com/rh-aiservices-bu/llama-stack-tutorial
- **本地文件**: `[s1-015]-llama-stack-tutorial.pdf`
- **证据质量**: medium（官方教程，实践导向，内容覆盖较广但深度有限）

## 内容摘要

Llama Stack Tutorial 是由 Red Hat AI Services Business Unit 维护的一套面向开发者的开源教程仓库，旨在系统性地降低 Llama Stack 框架的学习与使用门槛。Llama Stack 本身是一个开源的大语言模型应用开发框架，核心定位是在自有基础设施上简化大模型的构建、运行与实验流程。该框架由 Meta 主导开源，Red Hat 社区则通过本教程提供了从入门到进阶的完整实践路径。

从框架架构来看，Llama Stack 提供了四大核心能力模块。首先是统一接口层，该层屏蔽了底层模型提供者的差异，开发者可以通过同一套 API 与 Ollama、vLLM 等不同推理后端交互，无需为每个后端维护独立的调用代码。其次是工具与 Agent 能力，框架内置了复杂 AI 工作流所需的工具调用、多步推理与 Agent 编排机制，使开发者能够快速构建具备任务分解与外部工具调用能力的智能应用。第三是安全与遥测模块，Llama Stack 将内容安全过滤（基于 Llama Guard）与运行时可观测性（基于 OpenTelemetry）作为内置能力集成，开发者无需修改应用代码即可获取基础的追踪与指标数据。第四是多形态开发接口，框架同时提供了 CLI、Python SDK 与 Web Playground 三种交互方式，覆盖了从脚本化批量测试到交互式原型验证的不同开发阶段需求。

本教程仓库的内容组织采用了清晰的分级结构，将学习路径划分为初级（Elementary）、中级（Intermediate）两个层次。初级模块涵盖 CLI 与 Python SDK 的快速入门、Web Playground 的使用方法以及基础模型交互，这些章节的目标是帮助开发者在本地环境中快速跑通第一个 Llama Stack 应用。中级模块则深入框架的高级特性，包括 Model Context Protocol（MCP）集成、Retrieval Augmented Generation（RAG）实现、基于 ReAct 范式的交互式 Agent 构建、Llama Guard 内容安全过滤、OpenTelemetry 遥测与可观测性，以及内置的模型评估框架。这种由浅入深的编排方式使得不同经验水平的开发者都能找到合适的切入点。

在可观测性方面，教程明确将遥测与可观测性定位为中级主题，这说明 Red Hat 社区认为在掌握基础用法之后，开发者应当进一步理解如何监控和度量其 AI 应用的运行状态。教程中涉及的遥测技术栈包括 OpenTelemetry 用于分布式追踪与指标采集，以及 Jaeger 作为追踪数据的可视化前端（默认访问地址为 `http://localhost:16686`）。这种技术选型与当前云原生可观测性生态的主流趋势高度一致，也为将 Llama Stack 应用接入企业级监控体系奠定了基础。

从部署与访问方式来看，教程提供了一体化的本地部署方案，并预设了多个服务的默认访问端口：Web Playground 运行于 `8502` 端口，Llama Stack API 服务暴露于 `8321` 端口，Jaeger 遥测界面使用 `16686` 端口，而教程本身的静态站点则通过 `./utilities/lab-serve` 脚本在 `8080` 端口提供服务。这种端口规划使得开发者可以在单一主机上同时运行应用、监控与文档服务，形成完整的本地开发闭环。

教程的内容构建采用了 Antora 文档框架，源文件位于 `content/modules/ROOT/pages/` 目录下，这意味着社区贡献者可以通过标准的 Markdown/AsciiDoc 工作流向教程提交改进。这种开放的文档构建方式有助于教程内容随着 Llama Stack 框架的演进而持续更新。

值得注意的是，虽然教程内容较为全面地覆盖了 Llama Stack 的核心功能，但其对可观测性章节的处理相对基础，主要聚焦于如何启用遥测、查看 Jaeger 界面以及理解基本的追踪概念。对于需要深入定制指标、配置采样策略或集成外部监控平台的场景，开发者仍需参考 OpenTelemetry 与 Llama Stack 的官方文档进行补充学习。

此外，教程对 Llama Guard 安全过滤的介绍主要停留在配置层面，尚未深入到内容过滤策略的自定义、多语言支持以及与其他安全框架（如 Azure Content Safety、AWS Comprehend）的对比分析。对于需要在生产环境中部署内容安全机制的团队，这部分内容可能需要结合 Llama Guard 的官方文档进行扩展学习。

教程中提到的模型评估框架同样值得关注。虽然中级章节涵盖了模型评估的基础方法，但具体的评估指标定义、基准数据集选择以及与业界标准（如 AgentBoard、AgentHarm、Tau-bench）的对比验证等内容在教程中并未充分展开。这意味着开发者在使用 Llama Stack 内置评估工具时，可能需要自行设计评估策略以确保模型选型的科学性与可靠性。

## 关键要点

1. **多后端统一接口**
   Llama Stack 通过统一接口层屏蔽 Ollama、vLLM 等模型提供者的差异，开发者使用同一套 API 即可切换底层推理后端，显著降低多环境适配成本。

2. **内置安全与遥测**
   框架将 Llama Guard 内容过滤与 OpenTelemetry 遥测作为内置模块提供，开发者无需修改应用代码即可启用基础安全检测与分布式追踪能力。

3. **分级教程体系**
   初级模块覆盖 CLI、SDK 与 Playground 入门；中级模块深入 MCP、RAG、ReAct Agent、安全过滤与可观测性，适配不同经验水平的学习者。

4. **Model Context Protocol 支持**
   教程包含 MCP 集成章节，说明 Llama Stack 已具备与外部工具/数据源通过标准化协议进行交互的能力，这是构建复杂 Agent 工作流的重要基础。

5. **ReAct Agent 构建**
   中级教程涵盖基于 ReAct（Reasoning + Acting）范式的交互式 Agent 开发，展示了如何在 Llama Stack 中实现多步推理与工具调用的闭环。

6. **OpenTelemetry + Jaeger 技术栈**
   遥测方案采用 OpenTelemetry 采集追踪数据，Jaeger 提供可视化界面（`localhost:16686`），与云原生可观测性生态无缝对接。

7. **一体化本地部署**
   预设端口体系（API `8321`、Playground `8502`、Jaeger `16686`、教程站点 `8080`）支持在单机上快速搭建完整的开发-监控闭环。

8. **Antora 文档框架**
   教程使用 Antora 构建，源文件位于 `content/modules/ROOT/pages/`，便于社区通过标准开源工作流持续贡献与维护。

9. **Web Playground 快速验证**
   内置的 Web Playground（`localhost:8502`）为开发者提供了无需编写代码即可与模型交互的界面，加速了原型验证与参数调优过程。

10. **模型评估内置框架**
    中级教程包含模型评估章节，说明 Llama Stack 提供了用于评测模型输出质量的内置工具，有助于建立系统化的模型选型与回归测试流程。

11. **Llama Guard 安全过滤**
    教程涵盖 Llama Guard 的内容安全过滤配置，为 Agent 应用提供了开箱即用的有害内容检测能力，是生产环境中保障输出安全的基础防线。

12. **Antora 文档的社区开放性**
    采用 Antora 构建的文档体系支持社区贡献者通过标准 Git 工作流提交改进，这种开放的文档建设模式有助于教程内容随框架版本迭代而持续更新。

## 与综述的关联

本教程是综述中"开源 Agent 框架可观测性生态"章节的重要参考来源 [s1-015]。具体而言：

- **框架层内置遥测**
  综述引用该教程证实 Llama Stack 将安全与遥测能力设计为内置模块，开发者无需修改应用代码即可获取基础追踪数据。这一设计模式与 LangChain 的 LangSmith 集成、Google ADK 的 Cloud Trace 集成形成对比，代表了开源框架在可观测性方面的不同工程哲学。

- **OpenTelemetry 作为事实标准**
  教程将 OpenTelemetry 遥测定位为中级必修内容，综述据此论证 OpenTelemetry 已成为开源 AI 框架可观测性的事实标准。无论是 Llama Stack、Strands 还是其他框架，OpenTelemetry 几乎均为首选的埋点与传输协议。

- **遥测深度与语义覆盖的局限**
  综述指出，尽管 Llama Stack 提供了基础遥测能力，但其原生指标更偏向基础设施层（如 token 计数、请求延迟）而非应用层语义（如 Agent 工作流步骤、工具调用成功率）。该教程的内容编排（将遥测置于中级而非高级）也间接反映了当前框架在可观测性深度上的天花板。

- **与 Red Hat 生态的衔接**
  综述将本教程作为企业级开源 AI 平台（如 Red Hat OpenShift AI）与社区框架（Llama Stack）之间桥梁作用的例证，说明企业厂商如何通过高质量教程降低社区技术的采用门槛。

- **Jaeger 可视化前端**
  综述在讨论追踪数据的可视化与分析时，引用教程中 Jaeger UI（`localhost:16686`）的访问方式，作为开发者本地调试阶段的标准工具链配置参考。

- **安全与观测的协同**
  教程将 Llama Guard 安全过滤与 OpenTelemetry 遥测同时纳入中级内容，综述据此论证安全检测与运行观测在 Agent 工程实践中日益呈现协同趋势——安全事件本身也应成为可观测性数据流的一部分。

- **教程分级与认知负荷**
  综述将本教程的初级/中级分层设计作为技术文档降低认知负荷的范例，说明如何将复杂的可观测性主题拆解为循序渐进的认知单元，避免初学者因信息过载而放弃学习。

- **模型评估与基准对齐**
  综述指出教程中模型评估章节的浅层处理反映出当前开源框架在评估体系标准化方面的共性短板，建议将 Llama Stack 内置评估工具与 AgentBoard、Tau-bench 等外部基准结合使用，以建立更可靠的模型选型流程。

## 我的笔记

该教程虽然内容篇幅不长，但作为 Red Hat 官方背书的学习材料，其技术选型与内容编排具有显著的参考价值。从工程实践角度，我认为 Llama Stack 的架构设计体现了当前开源大模型应用框架的几个关键趋势：

第一，统一接口层的重要性日益凸显。随着模型部署方式的多样化（本地 Ollama、自托管 vLLM、云 Bedrock 等），开发者越来越需要一个与后端解耦的抽象层。Llama Stack 的统一接口不仅简化了代码维护，也为 A/B 测试不同模型提供了便利——开发者可以在不修改业务逻辑的情况下切换后端模型，仅需调整配置即可。

第二，内置遥测是框架竞争力的核心维度之一。本教程将可观测性明确纳入中级必修内容，说明社区已经认识到：一个缺乏观测能力的框架难以进入生产环境。Llama Stack 选择将 OpenTelemetry 作为内置遥测方案，而非自建专用协议，这一决策符合云原生生态的标准化趋势，也降低了与企业现有监控体系的集成成本。然而，需要注意的是，当前 Llama Stack 的内置遥测在 Agent 语义层面的覆盖仍有不足。根据社区讨论，现有版本主要提供 `llama_stack_prompt_tokens_total`、`llama_stack_completion_tokens_total` 与 `llama_stack_tokens_total` 三类基础计数器，对于 `agent_workflows_total`、`agent_steps_total`、`agent_workflow_duration_seconds`、`agent_tool_calls_total` 等应用层语义指标的支持尚处于提案阶段。这意味着开发者在进行复杂的 Agent 性能分析时，可能需要自行补充自定义指标。

第三，MCP 与 RAG 的纳入标志着框架向企业级应用演进。Model Context Protocol 的标准化工具调用协议与检索增强生成技术的内置支持，使得 Llama Stack 不再只是一个简单的模型调用包装器，而是具备了构建复杂业务 Agent 的基础能力。ReAct Agent 的教程覆盖则进一步证明了框架在多步推理与工具编排方面的成熟度。

第四，教程的分级设计值得借鉴。将内容划分为初级与中级两个层次，并为每个层次设定明确的学习目标（初级侧重"跑通"，中级侧重"用好"），这种结构降低了学习曲线，也便于团队根据成员经验水平分配学习任务。对于希望在组织内部推广 Llama Stack 的技术负责人，可以直接采用这套分级体系设计内部培训计划。

需要进一步追踪的问题包括：

- Llama Stack 社区对 Agent 语义级指标扩展提案（如 GitHub issue #2596）的落地时间线
- OpenTelemetry 自动埋点在异步并发场景下的性能开销与采样策略调优指南
- Llama Guard 内容过滤与遥测数据的关联方式（例如，安全拦截事件是否生成独立的追踪 span）
- 教程中提到的内置模型评估框架与业界标准基准（如 AgentBoard、AgentHarm）的可比性
- Llama Stack 在多节点分布式部署场景下的遥测聚合方案（当前教程主要聚焦单机部署）

第五，教程对模型评估的处理揭示了开源框架在评估体系标准化方面的共性挑战。虽然 Llama Stack 提供了内置的评估工具，但缺乏与业界公认基准（如 AgentBoard、AgentHarm）的直接对齐，这使得开发者在进行模型选型时难以获得跨框架可比的结果。建议在综述中强调：当前开源 Agent 框架的评估生态仍处于碎片化状态，每个框架都有自己的评估方法论，但缺乏统一的基准测试协议与公开排行榜，这在一定程度上阻碍了社区对框架能力的客观比较。

第六，Llama Guard 的配置虽然简单，但在多语言与多文化场景下的有效性仍需验证。教程主要展示了 Llama Guard 的基础启用流程，但对于中文、日文等非英语内容的过滤效果、误报率与漏报率等关键指标并未涉及。对于计划在全球范围内部署 Llama Stack 应用的团队，这部分内容需要额外的测试与调优。

需要进一步追踪的问题包括：

- Llama Stack 社区对 Agent 语义级指标扩展提案（如 GitHub issue #2596）的落地时间线
- OpenTelemetry 自动埋点在异步并发场景下的性能开销与采样策略调优指南
- Llama Guard 内容过滤与遥测数据的关联方式（例如，安全拦截事件是否生成独立的追踪 span）
- 教程中提到的内置模型评估框架与业界标准基准（如 AgentBoard、AgentHarm）的可比性
- Llama Stack 在多节点分布式部署场景下的遥测聚合方案（当前教程主要聚焦单机部署）
- Llama Guard 对中文等非英语内容的过滤效果与误报率数据
- Red Hat OpenShift AI 与 Llama Stack 的集成路线图及企业级支持计划
- 教程社区贡献者的活跃度与内容更新频率

从复现角度，该教程的本地部署流程设计得较为简洁，通过预设端口体系避免了服务间的端口冲突。建议在复现时优先启动 Jaeger（`16686`），这样可以在运行后续实验的同时实时观察追踪数据，形成"边运行边观测"的学习体验。对于初学者，建议按照教程的顺序逐步推进：先完成初级模块中的 CLI 与 SDK 入门，确保能够成功发起第一次模型调用；再进入 Web Playground 进行交互式探索，验证模型响应质量；最后才进入中级模块的可观测性章节，此时已经具备了足够的上下文来理解追踪数据的意义。

此外，由于教程使用 Antora 构建，贡献者可以通过修改 `content/modules/ROOT/pages/` 目录下的源文件来补充自己的实验笔记，这种将个人学习过程与社区文档结合的方式有助于知识的持续沉淀。对于希望在组织内部推广 Llama Stack 的技术负责人，可以考虑 fork 该仓库并基于实际业务场景定制内部教程，例如将天气查询示例替换为客服问答、文档摘要等贴近业务的场景，以提升团队的学习兴趣与实际应用能力。
