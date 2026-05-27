# 智能体轨迹可观测性综述：从日志、诊断到治理与 Token 经济学

> 时间边界：2023-2026
> 语料基础：`notes` 中的本地论文/材料笔记、`llm-wiki` 的词条与对比页，以及已整理的论文图表和产品材料
> 报告性质：研究综述。本文重在综合问题、方法谱系、证据和研究缺口，而不是记录整理过程。

---

## 摘要

大语言模型智能体把软件系统的可观测性问题推向了新的层级。传统 APM 主要关注请求、服务、延迟、错误和资源使用；智能体系统还必须解释模型如何规划、何时调用工具、如何读取和写入状态、为什么在长程任务中偏离目标、是否违反过程规范，以及 token 和工具成本为何失控。因此，智能体可观测性的核心对象不再是单次模型调用日志，而是贯穿用户意图、模型推理、工具调用、环境反馈、状态变化、评测结果、审计记录和成本信号的执行轨迹。

本文综述 2023-2026 年间围绕 agent trace、失败诊断、过程评测、审计治理、平台化可观测性和 token 经济学的研究与工程材料。综合 AgentTrace、OpenInference、AgentRx、DoVer、AgentPex、Monitoring Monitorability、HarnessAudit、Agentic Harness Engineering、Why Do Multi-Agent LLM Systems Fail、Who&When、AgentSight、AWS AgentCore、GenAIOps、Langfuse、Arize Phoenix、Braintrust、AgentOps、Helicone、Datadog 等材料后，可以形成一个统一判断：智能体可观测性正在从“看见执行过程”演化为“生成可行动证据”。所谓可行动证据，是能够支持失败归因、过程合规、安全审计、成本归因和系统改进的结构化轨迹。

本文将相关工作组织为五条主线：第一，轨迹与 schema 标准化解决“记录什么、如何互操作”；第二，失败诊断与归因解决“哪里首先出错、为什么出错”；第三，过程评测与治理解决“是否按规范行动、是否可追责”；第四，harness 与数据飞轮解决“如何把失败经验转化为系统改进”；第五，生产平台与 token 经济学解决“如何在质量、成本、延迟和合规之间做可观测权衡”。这些主线共同指向一个研究议程：未来的 agent observability 不应只是 trace viewer，而应是连接 OpenTelemetry 生态、agent-specific schema、自动诊断、过程评测、审计证据、成本控制和持续改进的证据基础设施。

---

## 1. 引言：为什么智能体需要新的可观测性

智能体系统的运行方式不同于普通 LLM 应用。普通 LLM 应用通常可以被近似为一次或多次模型调用；智能体系统则在模型调用之间引入工具、记忆、检索、环境状态、子智能体、外部 API 和长程控制流。一个错误不一定表现为异常，也不一定出现在最终答案中。它可能是一次错误工具调用、一次遗漏确认、一次不合规状态访问、一次错误的 agent handoff，或一次看似成功但成本极高的重试循环。

这使得“最终答案是否正确”不足以评价智能体。AgentPex 的过程合规研究说明，最终 reward 和过程规范并不等价；Monitoring Monitorability 说明，过程信号会显著影响风险检测能力；AgentRx 和 DoVer 表明，失败根因常常隐藏在早期轨迹前缀或需要干预验证的中间步骤中；多智能体失败研究进一步说明，错误可能跨 agent、消息边和共享状态传播。换言之，智能体的可靠性问题是轨迹级问题。

因此，智能体可观测性应回答五类问题。第一，执行过程是否被完整、结构化地记录。第二，记录是否足以定位失败根因。第三，过程是否遵守系统提示、工具 schema、业务规则和安全策略。第四，记录是否能支撑审计和事后取证。第五，系统是否以经济高效的方式完成任务。本文的综述框架正是围绕这五类问题展开。

---

## 2. 语料范围与证据分层

本文使用的本地材料可以分为四类。第一类是学术论文，覆盖失败诊断、过程评测、多智能体失败、harness 演化、监控器可监控性和长程任务分析等方向，例如 AgentRx、AgentPex、DoVer、Monitoring Monitorability、HORIZON、EAGER、Why Do Multi-Agent LLM Systems Fail、Who&When、AgentSight 和 Lifting Traces to Logic。第二类是标准、规范和技术草案，例如 OpenInference、OpenTelemetry GenAI 语义、AgentTrace、Hermes trajectory format、Agent Audit Trail 和 MCP tracing 提案。第三类是产品和云平台材料，例如 Langfuse、Arize Phoenix、Braintrust、AgentOps、Helicone、Datadog、Elastic、New Relic、AWS Bedrock AgentCore、Google ADK、阿里云 AgentLoop、百度千帆和 Coze Loop。第四类是 coding agent 和 agent framework 材料，例如 Claude Code、Codex CLI、OpenAI Swarm/Agents SDK、Llama Stack 和多智能体研究系统。

这些材料的证据作用不同。论文适合定义问题、提出方法和报告可比较实验，但经常低估生产接入、权限、隐私和组织流程。产品材料更贴近部署现实，能暴露团队如何接入 trace、eval、dashboard、告警和成本监控，但常缺少可复现实验。标准与协议材料决定长期互操作性。框架和 coding agent 材料则揭示工具、harness、子智能体和开发工作流如何影响可观测边界。

| 证据类型 | 主要回答的问题 | 代表材料 | 综述中的用途 |
|---|---|---|---|
| 学术论文 | 失败机制、评测任务、方法效果 | AgentRx、AgentPex、DoVer、HORIZON、Who&When | 定义问题和方法边界 |
| 标准/协议 | 轨迹如何表达、如何互操作 | OpenInference、AgentTrace、AAT、MCP tracing | 判断 schema 和生态演进 |
| 产品/云平台 | 如何接入、运营、告警和控成本 | Langfuse、Phoenix、AgentOps、Datadog、AWS AgentCore | 刻画落地需求 |
| Agent 框架 | 工具、harness、子智能体如何组织 | Claude Code、Codex、Llama Stack、Swarm | 理解工程表面 |

这种证据分层很重要。若只读论文，综述会把智能体可观测性理解为离线诊断问题；若只读产品材料，又会把它误解为 dashboard 和 SDK 接入问题。真正的综述必须把方法、schema、平台和组织约束合并考虑。

---

## 3. 从日志到轨迹：证据层与 Schema 层

智能体轨迹是按时间组织的执行证据，包括用户意图、模型消息、工具调用、工具返回、状态读写、环境反馈、评测结果和成本信号。它与普通日志的差别在于，普通日志主要服务于回放和排错，而智能体轨迹还必须支持语义判断：模型是否误读工具输出，是否违反过程规范，是否在多智能体协作中传播错误，是否因上下文膨胀或重试循环造成成本异常。

AgentTrace 将智能体事件组织为系统级、认知级和环境级表面，强调 agent 行为不能被压缩成一次 LLM request span。Hermes trajectory format 从训练数据角度要求工具调用和响应结构一致。OpenInference 则在 OpenTelemetry 生态内补充 LLM、agent、tool、retriever、embedding、evaluator 和 guardrail 等 span kind。它们共同说明：智能体可观测性的第一步不是多记录，而是以面向下游任务的 schema 记录。

![AgentTrace 系统流程图](notes/p-014_AgentTrace_A_Structured_Logging_Framewor/images/fig1_system_flow.png)

图 1 展示了 AgentTrace 如何把系统执行、认知步骤和环境交互组织成一条可分析轨迹。该图支撑的核心判断是：如果 trace 不记录工具、状态和环境反馈，后续失败诊断只能停留在对模型消息的文本解释。

OpenTelemetry 与 agent-specific schema 的关系是这一层的核心张力。OTel 提供 trace id、span id、parent-child、上下文传播和后端生态，但缺少 agent 任务语义；agent-specific schema 能表达意图、计划、工具语义、记忆读写、handoff、过程规范和失败类别，但容易碎片化。合理路径不是二选一，而是以 OTel 作为传播骨架，以 OpenInference、AgentTrace、Hermes 或 AAT 等格式提供语义层。

这一点在 MCP tracing 中尤其明显。MCP 统一了工具协议，但如果 server 内部执行不回传 span 或 trace id，工具调用仍是黑盒。也就是说，工具协议标准化不自动等于可观测性标准化。未来 MCP、OTel 和 agent semantic conventions 是否能稳定对接，将直接影响跨工具 agent 的诊断能力。

---

## 4. 从轨迹到诊断：失败归因的研究谱系

失败诊断研究试图回答“哪里首先出错，为什么出错，应该修哪里”。AgentRx 将失败定位为第一个不可恢复关键步骤，并用工具 schema、领域策略和执行前缀抽取约束，避免把后续连锁错误误判为根因。DoVer 进一步指出，仅让 LLM 阅读日志并给出解释并不可靠，必须通过干预或替换关键步骤验证归因。Who&When 和 Why Do Multi-Agent LLM Systems Fail 则把问题扩展到多智能体场景，关注哪个 agent、哪个时间点、哪条依赖链导致失败。

![AgentRx 诊断流程](notes/p-001_AgentRx_Diagnosing_AI_Agent_Failures_from_Execution_Trajectories/images/fig1_agentrx.png)

图 2 展示了从轨迹到约束再到失败定位的流程。它说明失败诊断不是阅读日志后的自然语言总结，而是把执行前缀、工具约束和状态变化转化为可验证的失败证据。

![DoVer 干预式调试流程](notes/p-003_DoVer_Intervention-Driven_Auto_Debugging/images/fig2_pipeline.png)

图 3 展示了干预式调试的必要性。DoVer 的意义在于区分“看起来像原因”的步骤和“改变后会影响结果”的步骤。这一点对长轨迹尤其重要，因为后续多个异常往往只是早期错误传播的结果。

多智能体失败使归因更复杂。单智能体失败通常可以在一条轨迹内定位工具参数错误、计划偏离或输出不合规；多智能体失败还涉及角色分工、消息传递、依赖链、共享状态和协调策略。`p-021` 的多智能体失败分类图说明，错误可能由底层模型、agent 设计、通信协议或系统架构触发；`p-022` 进一步把“哪个 agent”和“什么时候失败”作为显式问题。这要求 trace schema 记录 agent 身份、handoff、交互边和共享资源访问，而不能把多智能体执行压扁成单条消息流。

![多智能体失败分类图](notes/p-021_Why_Do_Multi_Agent_LLM_Systems_Fail/images/taxonomy_neurips_final_10_23_25.png)

图 4 支撑的判断是：多智能体失败不是单智能体错误的简单相加。它增加了协作层、通信层和系统设计层的失败机制。

现有诊断方法可以分为四类：约束驱动诊断、数据集/分类法驱动诊断、干预式诊断和结构化信号驱动诊断。AgentRx 属于约束驱动，Who&When 和 HORIZON 属于分类法与数据集驱动，DoVer 属于干预式诊断，MASPrism 和 EAGER 则展示了轻量表示和轨迹信号降低诊断成本的可能性。未来更可靠的诊断系统很可能是混合式的：先用结构化信号筛选可疑片段，再用约束和干预验证根因，最后把结果回流为评测数据和 harness patch。

---

## 5. 从结果评测到过程治理

智能体评估不能只看最终结果。AgentPex 说明，任务最终成功可能掩盖过程违规：模型可能跳过必要确认、调用错误工具、违反输出格式或绕过系统指令。Monitoring Monitorability 进一步表明，过程信号会影响风险检测能力；只看最终输出会丢失思维链和中间行为中的风险线索。HarnessAudit 和安全评测材料则把评估对象从最终回答扩展到完整 harness 和执行轨迹。

![CoT monitorability 聚合结果](notes/p-006_Monitoring_Monitorability/images/fig1_aggregate_monitorability.png)

图 5 的意义在于说明过程证据本身是一种监控资源。若系统隐藏或丢弃中间过程，就会削弱发现错误、欺骗或风险行为的能力。

![Agent harness safety auditing pipeline](notes/p-017_Auditing_Agent_Harness_Safety/images/pipline.png)

图 6 展示了安全审计如何覆盖完整 harness 和执行轨迹。它支撑的观点是：安全评估不应只检查最终回答，还应检查提示、工具、策略、状态和中间动作。

过程治理还涉及审计可信度。Agent Audit Trail 草案强调身份、时间顺序、动作、参数、结果和完整性字段；AutoGen tamper-evident audit RFC 讨论防篡改记录；OWASP agentic security 材料提供越权、工具滥用、数据泄露和策略绕过等风险背景。三者共同说明，受监管场景中的日志不能只是 debug artifact，而必须是运行时生成的证据链。

这带来一个重要设计结论：调试日志和审计日志应分层。调试日志追求信息充分，便于工程师复盘；审计日志追求证据可信，需要身份绑定、策略版本、完整性保护和访问控制。完整 trace 有助于诊断，但也可能包含敏感数据；脱敏、hash、采样和最小化记录可以降低隐私风险，但可能破坏诊断证据。这一张力是 agent observability 在生产落地中的核心难题之一。

---

## 6. Harness、数据飞轮与系统改进

仅靠更强模型不能解决所有智能体失败。Agentic Harness Engineering 把系统提示、工具描述、工具实现、中间件、技能、子智能体配置和长期记忆视为可观测、可编辑、可回滚的工程表面。很多失败来自工具描述含糊、系统提示与工具行为不一致、技能不可发现、记忆污染或子 agent 角色不清，而不是模型本身缺少能力。

![Agentic Harness Engineering 方法](notes/p-011_Agentic_Harness_Engineering_Observabilit/images/method.png)

图 7 展示了 harness 作为工程对象的处理方式。它支撑的核心观点是：智能体改进不应只依赖换模型或调 prompt，而应管理模型外部工作环境的版本、预测、回归测试和回滚条件。

Lifting Traces to Logic 进一步说明，轨迹不只是失败记录，也可以被提升为规则、技能或程序化结构。Teaching Text Agents to Learn from Failure 强调从失败中学习顺序决策经验。AgentLoop、Coze Loop 和多类平台材料则把 bad case 回流、评测集、数据集和 prompt/harness patch 连接起来。由此形成一个数据飞轮：trace 记录失败，诊断定位原因，评测固化样本，harness 产生改动，回归测试验证改动，再进入下一轮 trace。

![Lifting Traces to Logic 方法概览](notes/p-024_Lifting_Traces_to_Logic_Programmatic_Ski/images/fig2_overview.png)

图 8 说明轨迹可以从经验材料转化为可执行结构。该图支撑的判断是：trace 的最终价值不只是观察，而是驱动系统演化。

数据飞轮的风险是不可审计的自动演化。如果系统自动修改 prompt、工具、记忆或技能，却不记录修改意图、预期收益、潜在破坏和回滚条件，那么改进过程本身会变成新的黑盒。因此，未来 harness engineering 需要与可观测性深度绑定：每次变更都应带有版本、证据、预测和验证结果。

---

## 7. 平台化可观测性与 Token 经济学

产业材料显示，agent observability 正在从单点 trace viewer 走向平台化。Langfuse 强调开源、自托管、trace、prompt、eval 和 dataset 闭环；Arize Phoenix 和 OpenInference 强调 open instrumentation 与评估；Braintrust 强调 eval、trace 查询和团队工作流；AgentOps 强调 session replay、token tracking 和 runaway cost 检测；Helicone 以 gateway/proxy 方式切入请求记录、缓存和成本管理；Datadog、Elastic、New Relic、Splunk 则把 agent telemetry 接入已有 APM 栈。

![AgentSight 系统架构](notes/p-025_AgentSight_System-Level_Observability_fo/images/fig2_agentsight_system_architecture.png)

图 9 展示了系统级 observability 需要连接 agent framework、instrumentation、storage、analysis 和 UI，而不是只提供一个 SDK 或 timeline 页面。

平台化趋势的另一面是 token 经济学。智能体系统的成本不是单次模型调用价格，而是任务路径、上下文长度、模型路由、工具调用、缓存命中、重试和失败恢复的函数。AWS AgentCore 将成本拆成模型 token、runtime、memory 和可观测性流量，并提出模型路由、prompt caching、batch inference 等杠杆；GenAIOps on AWS 把 input/output token、生成成本、检索质量、TTFT 和上下文窗口保护写入同一观测路径；AgentOps 和 Helicone 等产品也把 token 使用与成本异常作为核心监控对象。

![AWS AgentCore 成本分解框架](notes/images/[s1-007]/amazon_bedrock_agentcore_production_guide_cost_decomposition.png)

图 10 支撑的判断是：成本应按模型、runtime、memory、可观测性流量和工具链拆解，而不是只在账单层汇总。

Token 经济学在方法上至少包含五类架构路线。第一类是成本可见性路线，以 gateway/proxy、SDK 或 APM 插桩记录请求、模型、token、价格、工具调用和用户/功能标签，代表 Helicone、AgentOps、Datadog、Elastic、GenAIOps 等材料。第二类是运行时控制路线，在 agent runtime 内做模型路由、预算护栏、降级、batch inference 和人工豁免，代表 AWS AgentCore 和多类生产化 agent 平台。第三类是上下文与缓存优化路线，通过 prompt caching、语义缓存、工具结果缓存、上下文裁剪和摘要减少重复计算。第四类是质量归一化路线，把成功率、评测分数、失败类别、延迟和 token 消耗合并，计算成功率/token、质量/美元和失败浪费成本。第五类是数据飞轮路线，把高成本失败 trace 转成评测集、harness patch 和回归测试，使成本控制不只是账单优化，而是系统改进的一部分。

![Token 经济学架构谱系](assets/token-economics-architecture.svg)

图 11 把这些路线放在同一架构中。gateway/proxy 路线接入快，适合账单、缓存和跨模型统计，但难以观察 agent 内部状态；agent runtime 路线能记录工具、记忆、handoff、重试和预算策略，但要求框架深度集成；eval/data flywheel 路线能把成本与质量和失败机制关联，但实时止损能力较弱。因此，token 经济学不是“选择一个降本工具”，而是根据系统边界组合观测、控制、优化和治理层。

| 架构/做法 | 主要作用点 | 典型收益 | 主要风险 | 必须记录的观测字段 |
|---|---|---|---|---|
| Gateway/proxy 成本可见性 | 模型请求入口 | 接入快、账单清晰、适合跨模型统计 | 看不到 agent 内部工具链和状态变化 | prompt/completion token、模型、价格、用户/功能标签、缓存命中 |
| Agent runtime 预算控制 | 规划、工具、记忆、handoff 和重试 | 能按任务难度、风险和预算动态决策 | 与框架耦合深，策略错误会降低质量 | 路由理由、候选模型、预算余额、降级动作、人工豁免 |
| 上下文压缩与缓存 | 输入 token 和重复计算 | 降低延迟、减少重复模型/工具调用 | 丢失证据、缓存陈旧、错误复用或隐私泄露 | 压缩比例、被裁剪摘要、缓存来源、失效策略、命中率 |
| Eval-first 质量归一化 | 评测、数据集和实验 | 能判断少花是否仍然有效 | 离线评测可能低估生产风险 | 任务难度、评测分数、成功率/token、质量/美元、失败类别 |
| 数据飞轮与 harness 改进 | 高成本失败样本和回归测试 | 把失败浪费转化为系统修复 | 自动修复不可审计时会引入新风险 | trace id、失败根因、patch 版本、回归结果、回滚条件 |

![Token 经济学控制闭环](assets/token-economics-control-loop.svg)

图 12 展示了更完整的控制闭环：先采集 token、价格、延迟、工具、缓存和重试信号，再按用户、功能、任务、模型、agent 和失败类别归因；随后由 policy engine 做模型路由、预算阈值、缓存和上下文压缩决策；执行时必须记录候选、理由、命中、失败和人工豁免；最后用评测分数、成功率/token、质量/美元和失败浪费成本验证策略是否有效。这个闭环强调，成本策略必须可解释、可审计、可回滚。

Token 经济学必须带质量分母。`s3-011 Token Economics for LLM Agents` 从计算和经济双视角讨论 token 消耗；Anthropic 多智能体研究系统观察到性能提升与 token 消耗高度相关；AI-NativeBench 指出自愈合机制在不可行工作流上可能成为成本乘数。三者共同说明，“更多 token”可能是有效扩展推理预算，也可能只是失败循环造成的浪费。合理指标应包括每任务成本、成功率/token、质量/美元、失败 trace 浪费成本和预算策略触发记录。

---

## 8. 研究缺口

当前文献和产品实践已经形成清晰方向，但仍存在若干关键缺口。

第一，跨格式语义映射仍缺失。OpenTelemetry、OpenInference、AgentTrace、Hermes、AAT 和各产品私有格式之间没有稳定映射，导致诊断器、评测器和审计工具难以跨平台复用。

第二，失败分类法碎片化。AgentRx、Who&When、HORIZON、HarnessAudit、AgentDiagnose、AgentPex 和安全材料使用不同类别体系。未来需要分层分类法：底层描述事件和工具错误，中层描述认知、计划和协作错误，高层描述业务和治理风险。

第三，长轨迹与多智能体因果推断仍不可靠。长轨迹中根因和后果容易混淆，多智能体场景中责任可能跨 agent 边界传播。单体 LLM judge 在这类问题上不够稳定，需要结构化信号、约束和干预验证。

第四，过程评测依赖规范质量。AgentPex 类方法要求系统提示、工具 schema 和业务规则能够被抽取为可检查规范；真实业务规则却常隐藏在文档、人工习惯和隐式流程中。如何把业务规范变成可评测对象，是过程治理落地的瓶颈。

第五，隐私与诊断深度冲突。完整 trace 有助于复盘和审计，但也可能包含用户数据、企业机密、文件内容和工具返回。脱敏和采样会降低风险，也可能破坏诊断证据。当前材料对这一权衡讨论不足。

第六，成本归因与质量归因尚未统一。成本平台能展示 token 和调用费用，评测平台能展示质量和失败，但二者经常分离。真正有用的指标应是单位成功任务成本、单位质量成本和失败根因对应浪费成本。这需要 trace、eval、billing 和 policy engine 可 join。

第七，自动修复缺少生产实证。AHE、Continual Harness 和 Lifting Traces to Logic 显示 trace 可以驱动系统演化，但生产环境中自动修改 harness、prompt、tool 和 memory 的风险仍未充分评估。自动修复需要版本控制、预测声明、回滚机制和人类审批。

---

## 9. 面向系统设计的建议

第一，把 trace schema 作为产品/API 设计的一部分，而不是日志后处理格式。每次模型调用、工具调用、状态读写、handoff、评测结果和成本事件都应能进入同一 trace 域。

第二，采用 OTel 作为传播骨架，同时保留 agent-specific 语义字段。OTel 解决生态和关联，agent schema 解决诊断和治理。

第三，将最终 reward、过程规范、失败类别、成本和安全事件写入同一关联域。只有这样，质量、可靠性、合规和成本才能一起分析。

第四，对多智能体系统显式记录 agent 身份、消息边、依赖链、共享状态访问和子 agent 生命周期。否则，多智能体失败无法归因。

第五，区分调试日志和审计日志。调试日志追求诊断充分性，审计日志追求证据可信度；二者应采用不同保留、脱敏、访问和完整性策略。

第六，把 token 预算作为运行时策略对象记录下来，包括预算层级、剩余额度、触发阈值、降级动作、模型候选、缓存命中和人工豁免。

第七，让失败样本进入数据飞轮：诊断、标注、评测集、prompt/tool/harness patch、回归测试和版本记录应形成闭环。

---

## 10. 结论

智能体可观测性正在成为 agent 系统从演示走向可靠生产的基础设施。它以轨迹为原始材料，但目标不是保存日志，而是生成可行动证据。这个证据层同时服务于运行时监控、失败诊断、过程评测、安全审计、成本归因和系统演化。

现有研究已经证明，最终答案不足以评价智能体，普通日志不足以诊断智能体，单一 dashboard 不足以治理智能体。产业实践则说明，trace、eval、dataset、prompt 管理、成本控制和合规正在合流为平台能力。两条路线正在汇合：学术界提供问题定义和方法谱系，产业界提供部署约束和平台形态。

未来真正有价值的 agent observability 系统，不会只是 APM 的 LLM 插件，也不会只是一个漂亮的 trace viewer。它应当是一个证据基础设施：以标准化轨迹为底座，以 agent-specific schema 保留语义，以诊断和过程评测生成解释，以审计链保证可信，以 token 经济学衡量可持续性，并以数据飞轮推动 harness 和系统持续改进。
