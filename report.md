# 智能体轨迹可观测性综述：从日志采集到诊断、评测与治理

> 时间边界：2023-2026  
> 语料基础：`agentic_trace_insight/notes` 中的 117 篇本地笔记，以及由这些笔记刷新得到的 `llm-wiki` 词条、观点与对比页  
> 报告性质：研究与工程综述，不是产品选型白皮书

---

## 摘要

智能体可观测性正在从“记录模型调用日志”的工程附属功能，演变为支撑智能体可靠性、安全性、合规性和成本控制的核心基础设施。117 篇本地笔记覆盖了学术论文、产品文档、工程博客、标准草案和产业材料；它们共同指向一个清晰结论：智能体系统的关键问题已经不再只是“最终答案对不对”，而是“执行过程中发生了什么、哪里首先不可恢复地出错、是否违反系统规范、证据能否被审计、成本能否被归因”。

本综述将现有材料重构为五层架构。第一层是轨迹证据层，负责将用户意图、模型消息、工具调用、工具返回、状态变化、记忆读写、环境观测和评测结果组织成可复用证据。第二层是 schema 与插桩层，围绕 OpenTelemetry、OpenInference、AgentTrace、Hermes trajectory format 和平台自定义格式展开，解决跨框架采集与语义保真问题。第三层是诊断与归因层，以 AgentRx、Who&When、DoVer、HORIZON、AgentDiagnose、MASPrism 等工作为代表，试图回答“哪个智能体、哪个步骤、哪条依赖链导致失败”。第四层是过程评测与治理层，以 AgentPex、Monitoring Monitorability、HarnessAudit、AgentPro、安全审计和防篡改 audit trail 为代表，强调最终成功率不足以覆盖过程违规、策略绕过和不可追责行为。第五层是生产平台与 token 经济层，包括 Langfuse、Arize Phoenix、Braintrust、AgentOps、Helicone、Datadog、Splunk、Elastic、New Relic、AWS、Google、阿里云、百度、Coze 等产品材料，显示可观测性正在与评估、数据集、实验、成本、预算和合规平台合流。

全文的核心判断是：智能体可观测性的真正对象不是日志，而是“可行动证据”。日志只回答发生了什么；可行动证据还必须支持失败定位、过程合规、审计追责、成本归因、预算控制和系统演化。因而，未来的智能体可观测系统不会只是 APM 的 LLM 插件，而会成为连接运行时、评测器、诊断器、安全策略、数据飞轮、token 经济学和 harness 工程的公共证据层。

---

## 1. 范围与材料组织

本综述的材料来自四类来源。

第一类是智能体轨迹诊断和评测论文，主要包括 AgentRx、AgentPex、AIOpsLab、DoVer、PROBE、Monitoring Monitorability、Beyond the Black Box、Continual Harness、Agentic Harness Engineering、Meerkat、AgentTrace、VCC、HORIZON、HarnessAudit、EAGER、OpsAgent、SeqCV、Why Do Multi-Agent LLM Systems Fail、Who&When、EvoCF、Lifting Traces to Logic、AgentSight、AgentPro、Do Code Semantics Help、FLARE、AgentDiagnose 和 Teaching Text Agents to Learn from Failure 等 `p-001` 到 `p-030` 条目。

第二类是 agent 可观测性、trace schema、OpenTelemetry、OpenInference、audit trail、安全护栏、MCP tracing 和产品架构相关技术材料，主要分布在 `c-*` 与 `s3-*` 条目。

第三类是云平台与商业工具材料，覆盖 Google ADK / Vertex AI、AWS Bedrock AgentCore、阿里云 AgentLoop、百炼、百度千帆、Coze Loop、Datadog、Splunk、Elastic、New Relic、LangSmith、Langfuse、Arize Phoenix、Braintrust、AgentOps、Helicone 等。

第四类是 coding agent 与 agent framework 材料，覆盖 Claude Code、Codex CLI、OpenAI Swarm / Agents SDK、Hermes Agent、OpenClaw、Llama Stack 和多智能体协作示例。

这些材料的质量并不均匀。学术论文通常给出明确任务定义、数据集和实验结果，但部署成本、权限模型和组织流程讨论不足。产品文档和产业文章更贴近生产接入和团队工作流，但常常缺少可复现实验和 schema 细节。综述因此不采用单一路线，而是把每类材料放入不同证据位置：论文用于定义问题和方法边界，产品材料用于刻画落地需求和平台能力，标准与协议材料用于判断互操作性和长期演进方向。

---

## 2. 核心词条：从 trace 到可行动证据

### 2.1 智能体轨迹

智能体轨迹是按时间记录的用户输入、模型消息、工具调用、工具返回、状态更新、环境观测和评测结果。它不是普通日志的同义词。普通日志往往服务于运行状态回放，而智能体轨迹还必须支撑语义判断：模型是否误读了工具输出，是否违反了系统提示，是否在多智能体协作中传播了错误，是否在成本上进入无效循环。

AgentTrace 将轨迹组织为系统级、认知级和环境级三类表面，使日志从“API 请求记录”变成面向 agent 行为的结构化事件流。Hermes trajectory format 则展示了训练数据视角的轨迹规范：每轮工具调用和响应都应保持一致结构，以便后续训练、重放和分析。OpenInference 进一步尝试把 LLM、agent、tool、retriever、embedding、evaluator、guardrail 等 span kind 纳入 OpenTelemetry 生态。

由此可以得到第一条原则：trace 的字段设计必须从下游问题反推。如果目标只是统计 token 和延迟，普通 span 足够；如果目标是失败归因和审计，trace 必须保留工具参数、工具返回、状态变化、策略版本、agent 身份、任务上下文和事件间依赖。

### 2.2 失败归因

失败归因关注失败由哪个智能体、哪个步骤、哪类约束违反或哪条依赖链触发。AgentRx 把问题具体化为定位“第一个不可恢复关键步骤”，并用约束违反证据解释失败类别。Who&When 把多智能体失败归因拆成“哪个 agent”和“什么时候”两个维度。DoVer 则质疑只让 LLM 阅读日志后归因的可靠性，强调干预式验证。HORIZON 从长程任务角度揭示失败机制随任务长度迁移，说明短轨迹上的诊断成功不能直接外推到长轨迹。

失败归因的核心困难在于区分根因和后果。长轨迹中后续多个步骤都可能异常，但它们往往只是早期错误传播的结果。AgentRx 用工具 schema、领域策略和执行前缀抽取约束，试图把“原因”限制在可验证违反处。MASPrism 则显示，失败归因不一定总需要 frontier LLM；在多智能体轨迹中，prefill-stage 信号和注意力/NLL 特征可以为轻量模型提供诊断线索。

### 2.3 过程合规性

过程合规性评估智能体是否按系统提示、工具 schema、业务规则和安全策略行动，而不只看最终答案是否正确。AgentPex 是这一方向的代表：它从提示和工具规范中抽取行为规则，再用 judge 对完整轨迹进行多维合规评分。其关键贡献不是替代最终奖励，而是证明最终奖励和过程规范不等价。一个任务可以最终成功，却在中途跳过必要确认、调用错误工具、泄露不该泄露的信息，或违反输出格式要求。

这一点对生产系统尤其重要。在客户服务、医疗、金融、企业自动化和受监管场景中，过程违规本身就是失败。最终数据库状态正确不能抵消不合规访问、越权工具调用或缺失审批链。因而，智能体评测应至少分成三层：最终结果、过程规范、失败诊断。只报告 pass@1 或 reward 的 benchmark 很难指导工程修复。

### 2.4 Harness

Harness 是模型外部可编辑的执行表面，包括系统提示、工具描述、工具实现、中间件、技能、子智能体配置和长期记忆。Agentic Harness Engineering 的贡献在于把 harness 从手工经验对象变成可观测、可回滚、可演化的工程对象。它提出组件可观测性、经验可观测性和决策可观测性三根支柱：组件必须文件化，轨迹经验必须被压缩成可消费证据，编辑决策必须带有可证伪预测。

这一方向改变了“失败归因”的责任边界。很多失败不应简单归咎于模型能力，而可能来自工具描述含糊、中间件缺失、技能不可发现、记忆污染或系统提示与工具行为不一致。Harness 作为可编辑表面，使智能体改进从“换更强模型”扩展到“改造模型外部工作环境”。

### 2.5 审计轨迹、成本归因与 Token 经济学

审计轨迹面向责任追踪、合规和事后取证，要求完整性、时间顺序、身份绑定、敏感信息控制和防篡改能力。Agent Audit Trail 草案、AutoGen tamper-evident audit trail RFC、OWASP agentic security 材料和多篇治理文章都指出：智能体日志如果可以被管理员事后随意修改，就难以成为合规证据。

成本归因则把 token、模型调用、工具调用、重试、缓存、失败和多智能体依赖链连接起来。Token economics 相关材料显示，智能体任务的 token 消耗可能远高于单轮调用，且不同运行间方差很大。成本因此不是财务尾项，而是运行时信号：长上下文膨胀、失败重试、工具循环和多智能体低效协作都会首先体现在成本曲线上。

Token 经济学比“省钱”更宽。它关注 token 投入如何转化为任务质量、延迟、可靠性和业务价值。只看 token 降低会把系统推向廉价但无效的执行；只看成功率又会掩盖 token 暴涨。合理的分析单位应从单次模型调用上移到完整任务、用户会话、agent 子链和失败轨迹：每个层级都要同时报告 token、模型价格、工具成本、延迟、质量评分、失败类别和重试链。

这一视角把几个工程词条连成一组。Token 预算负责设定任务、会话、用户或工作流的上限与降级策略；上下文膨胀解释长程 agent 为什么在没有显式错误时变贵；缓存与复用通过 prompt cache、语义缓存和工具结果缓存降低重复计算；模型路由根据任务难度、风险和预算在不同模型间选择；成本可见性则要求在账单到来之前把这些信号按 trace、用户、功能和失败模式展示出来。

---

## 3. 五层架构：智能体可观测性的系统分解

本章的核心判断是：智能体可观测性不是一个单点工具，而是一条从运行轨迹到治理决策的证据流水线。它至少包含五层：轨迹证据层、schema 与插桩层、诊断与归因层、过程评测与治理层、生产平台与 token 经济层。五层之间不是简单上下游关系，而是互相约束：轨迹字段决定诊断上限，诊断结果决定评测数据如何回流，治理要求反过来规定审计字段，成本控制又要求把 token、模型、工具和预算策略写入同一 trace 域。

### 3.1 轨迹证据层

**判断。** 轨迹证据层回答“发生了什么”，但它的目标不是保存聊天记录，而是保留足以复原任务路径、解释失败、检查合规和计算成本的证据。一个合格的 agent trace 至少应包含用户意图、模型消息、工具调用、工具返回、状态读写、环境变化、用户反馈、失败标签和评测结果。

**机制。** 传统日志以单条事件为中心，agent trace 以事件序列和因果上下文为中心。用户请求触发规划，规划触发工具调用，工具返回改变状态，状态变化影响下一轮模型输入；如果只保留模型输入输出，就会把工具、状态和环境压扁成不可解释的文本。AgentTrace、Hermes trajectory format、OpenClaw 会话日志、Claude Code 的 OTel events、Coze 调试链路和 Llama Stack/MCP tracing 实践都说明：轨迹证据层必须支持可重放、可查询和可关联。

![AgentTrace 系统流程图](notes/p-014_AgentTrace_A_Structured_Logging_Framewor/images/fig1_system_flow.png)

图 3-1 支撑的判断是：agent trace 需要同时覆盖系统执行、认知步骤和环境交互。它解释了为什么只记录 LLM request span 不够：工具调用、状态更新和环境反馈才是很多失败的真实触发点。

**含义。** 轨迹证据层的主要风险是“记录很多，但不可诊断”。大量非结构化消息并不能自动告诉开发者哪里错了。若缺乏 agent 身份、工具 schema、状态变化、父子 span、call id、策略版本和任务上下文，后续诊断器只能做文本猜测。因而，这一层的设计原则应从下游问题反推：要诊断就记录约束和状态，要审计就记录身份和策略版本，要控成本就记录 token、模型、缓存和重试链。

### 3.2 Schema 与插桩层

**判断。** Schema 与插桩层回答“如何把发生的事情标准化”。OpenTelemetry 更适合作为传输和关联骨架，OpenInference、AgentTrace、Hermes、AAT 和平台自定义字段则提供 agent-specific 语义。二者缺一不可。

**机制。** OTel 能稳定表达 trace id、span id、parent-child、上下文传播、指标和日志生态，但它本身不知道“计划”“工具语义”“handoff”“记忆读写”“过程规范”和“失败类别”。反过来，自定义 agent schema 可以保留语义，却容易失去跨平台工具链。更合理的路径是：用 OTel 处理传播和后端生态，用 agent-specific 属性承载诊断语义，并把敏感字段控制、采样和审计策略作为 schema 的一部分。

**证据。** OpenInference 规范把 LLM、agent、tool、retriever、embedding、evaluator、guardrail 等 span kind 纳入 OTel 语义空间；AgentTrace 从系统级、认知级和环境级三类表面组织日志；AAT 草案要求审计记录带身份、时间顺序、动作和完整性字段。MCP tracing 进一步暴露了边界问题：MCP 统一了工具协议，但如果 server 内部执行不回传 span 或 trace id，工具调用对上游 agent 仍然是黑盒。

**含义。** Schema 是产品能力边界。若 schema 只记录 prompt、completion、latency 和 token，平台最多做 LLM 请求监控；若 schema 能表达 agent、tool、handoff、memory、state、policy、eval、cost 和 audit chain，平台才可能支持完整 agent observability。产品成熟度不应只看 dashboard，而应看原始轨迹能否导出、字段是否稳定、是否能和 OTel/OpenInference 对齐。

### 3.3 诊断与归因层

**判断。** 诊断与归因层回答“为什么失败，应该修哪里”。它把轨迹从事后回放材料转化为修复线索：哪个智能体、哪个步骤、哪条依赖链、哪类约束违反导致失败。

**机制。** 这一层至少包含四类方法。第一类是约束驱动诊断，用工具 schema、领域策略和提示规范定义可检查条件，例如 AgentRx。第二类是数据集和分类法驱动诊断，用人工标注失败轨迹训练或评估模型，例如 Who&When、HORIZON 和 AgentDiagnose。第三类是干预式诊断，通过改变步骤、替换输出或验证依赖来确认根因，例如 DoVer。第四类是信号驱动轻量诊断，用 NLL、attention、执行 trace 表征或程序语义特征降低诊断成本，例如 MASPrism 和执行轨迹语义工作。

![AgentRx 诊断流程](notes/p-001_AgentRx_Diagnosing_AI_Agent_Failures_from_Execution_Trajectories/images/fig1_agentrx.png)

图 3-2 支撑的判断是：失败诊断必须把“读轨迹”变成“定位关键失败步骤和约束违反”。AgentRx 的流程体现了从轨迹到约束、再到故障定位的路径，避免把后续连锁错误误判为根因。

**含义。** 该层尚未成熟的原因有三点。第一，失败分类法碎片化。AgentRx、Who&When、HORIZON、HarnessAudit、AgentDiagnose 和各类产品平台使用的失败类别并不统一。第二，长轨迹中的因果链容易断裂，LLM-as-judge 在长上下文下会混淆根因与后果。第三，多智能体失败的责任边界不清晰，错误可能跨 agent、跨工具和跨共享状态传播。因此，未来诊断系统不应只依赖单体 LLM judge，而要结合约束、干预、结构化信号和人工复核。

### 3.4 过程评测与治理层

**判断。** 过程评测与治理层回答“行为是否被允许、是否可追责、是否可验证”。它与诊断层的区别在于：诊断关注失败后如何修复，治理关注执行过程是否符合规范，即使最终任务成功也可能判为风险。

**机制。** AgentPex 从提示和工具规范中抽取行为规则，再用 judge 对完整轨迹进行多维合规评分；HarnessAudit 把安全评估单元从最终输出移动到完整执行轨迹；Monitoring Monitorability 和 alignment auditing agents 说明，很多危险行为必须在过程层观察，不能只依赖最终输出分类器。治理层还引入身份、策略版本、时间戳、签名、hash chain、WORM storage、OPA 策略记录和访问审计等要求。

![HarnessAudit 流程](notes/p-017_Auditing_Agent_Harness_Safety/images/pipline.png)

图 3-3 支撑的判断是：审计和安全评估必须围绕完整 harness 与执行轨迹展开。它把风险对象从“最终回答”扩展到提示、工具、策略和中间行为。

**含义。** 治理要求会反过来约束 trace schema。如果日志需要作为证据，字段就不能只为调试便利而设计，还必须支持证明“谁在何时依据哪个规则允许了哪个动作”。这也解释了为什么调试日志和审计日志应分层：调试日志追求信息充分，审计日志追求证据可信。

### 3.5 生产平台与 Token 经济层

**判断。** 生产平台与 token 经济层回答“如何落地、如何运营、如何控制成本，并在质量不崩塌的前提下提高单位 token 产出”。它是前四层在真实组织中的承载面。

**机制。** 这一层的共同趋势是从 tracing 工具走向“观测 + 评估 + 数据集 + 实验 + 成本 + 治理”的平台化。Langfuse 强调开源、自托管、trace、prompt、eval、dataset 闭环。Arize Phoenix 和 OpenInference 强调开放 instrumentation 与评估。Braintrust 强调 eval、trace 查询和团队工作流。Helicone 以 proxy/gateway 进入请求、缓存和成本管理。Datadog、Splunk、Elastic、New Relic 则把 agent telemetry 接入已有 APM 和企业运维栈。中国云厂商和低代码平台更强调应用观测、节点级调试、BadCase 回流和数据飞轮。

![AWS AgentCore 成本分解框架](notes/images/[s1-007]/amazon_bedrock_agentcore_production_guide_cost_decomposition.png)

图 3-4 支撑的判断是：成本不是单一模型账单，而是模型 token、runtime、memory、可观测性流量和工具调用共同形成的系统成本。它说明 token 经济层必须把成本归因拆到 agent、工具、模型和工作流，而不能只看月度账单。

**含义。** Token 经济层暴露了一个新的平台分水岭：成本可见性是否能转化为成本控制。只展示每次请求花了多少钱，仍然只是事后观察；真正的控制需要记录和执行预算策略、模型路由、上下文裁剪、缓存命中、批量异步、采样策略和超预算降级。AWS AgentCore 材料把成本分解为模型 token、runtime、memory 和可观测性流量，并给出模型路由、提示缓存和 batch inference 等杠杆；GenAIOps on AWS 把 input/output token、模型成本、检索质量、TTFT 和上下文窗口保护写入同一观测路径；Datadog、AgentOps、Helicone 等产品材料也都把 token 使用和成本异常作为 agent 监控的一等信号。

### 3.6 五层之间的闭环

五层架构的关键不是分层本身，而是闭环。轨迹证据层生成原始材料；schema 与插桩层决定这些材料能否跨工具复用；诊断与归因层把失败压缩成修复线索；过程评测与治理层把行为纳入规范和审计；生产平台与 token 经济层把质量、成本和组织流程连接起来。若其中任一层缺失，系统都会退化：没有轨迹就无法复盘，没有 schema 就无法规模化，没有诊断就只能人工读日志，没有治理就无法进入受监管场景，没有 token 经济层就无法判断系统是否可持续运行。

## 4. 七个核心观点

本章把前面的架构分解压缩成七个可操作判断。每个判断都按同一逻辑展开：先说明立场，再解释机制，再给出图表或材料证据，最后落到工程含义。

### 4.1 智能体可观测性不是日志收集

**判断。** 日志收集只是必要条件，不是充分条件。一个系统可以记录所有消息，却仍然无法回答为什么失败。AgentRx、AgentTrace、AgentDiagnose 和多篇工程材料共同说明，可观测性必须把轨迹转化为可诊断、可评测、可审计的证据。

**机制。** 日志回答“发生了什么”，可观测性还要回答“这意味着什么”。这要求平台具备三种额外能力。第一，结构化：事件必须带有 agent、tool、state、span、task 和 policy 上下文。第二，解释性：系统应能把事件映射到失败类别、规范违反或成本异常。第三，闭环：诊断结果应能回流到 prompt、tool schema、harness、评测数据集或安全策略。

**证据。** AgentTrace 的系统流程图显示，agent 行为横跨系统、认知和环境三类表面；AgentRx 则进一步把轨迹变成失败步骤与约束违反。二者合起来说明，记录消息只是起点，真正的可观测性必须让日志进入诊断和修复流程。

**含义。** 评价一个 observability 平台时，不应只看是否有 timeline UI，而应检查它是否能导出原始轨迹、是否保留工具和状态语义、是否能连接 eval、是否能把失败样本变成 regression case。没有这些能力，平台只是更好看的日志浏览器。

### 4.2 最终奖励不足以评估智能体

**判断。** 最终任务成功可能掩盖过程违规。AgentPex 是最清晰的证据，HarnessAudit、AgentPro、Monitoring Monitorability 和 alignment auditing materials 也指向同一问题：智能体评估不能只看最终答案，而应同时看执行路径是否合规、是否安全、是否可解释、是否可复现。

**机制。** 智能体的风险往往发生在中间过程：跳过必要确认、调用错误工具、泄露敏感信息、违反输出格式、绕过策略或在高风险场景中做出未授权动作。这些行为可能并不改变最终答案，甚至可能帮助任务“成功”。因此，最终 reward 与过程规范不是同一个指标。

![CoT monitorability 聚合结果](notes/p-006_Monitoring_Monitorability/images/fig1_aggregate_monitorability.png)

图 4-1 支撑的判断是：过程信号会改变监控能力。Monitoring Monitorability 相关结果说明，很多风险需要观察推理或过程证据才能更早发现；只看最终输出会丢失关键线索。

**含义。** 未来 benchmark 应报告至少四类指标：最终任务结果、过程规范得分、失败归因准确率和资源/成本效率。单一 pass@1 会把“偶然成功”“违规成功”和“稳健成功”混在一起。对于生产系统，过程违规本身就应进入失败标签和审计记录。

### 4.3 Schema 决定产品边界

**判断。** Schema 不是后端细节，而是产品能力边界。若 schema 只记录 prompt、completion、latency、tokens，那么产品只能做 LLM 请求监控。若 schema 能表达 agent、tool、handoff、memory、state、policy、eval、cost 和 audit chain，平台才可能支持完整 agent observability。

**机制。** 产品能力由可查询字段决定。没有 agent 身份，就无法比较多 agent 分工；没有工具参数和返回摘要，就无法定位工具误用；没有 policy version，就无法证明动作是否按规则执行；没有 cost 和 token 字段，就无法做预算控制；没有 eval 结果，就无法把质量和运行指标 join。Schema 的遗漏会直接变成产品问题的盲区。

**证据。** OpenTelemetry 提供传播骨架，OpenInference/AgentTrace/Hermes/AAT 提供 agent-specific 语义。它们的差别不是技术口味，而是问题边界：OTel 让 trace 进入企业后端生态，agent-specific schema 让 trace 保留诊断语义。

**含义。** 谁能把 OTel 骨架、agent 语义、隐私策略和成本字段稳定结合，谁就更可能成为跨框架事实标准。反过来，只做私有字段和 UI 的平台短期容易演示，长期会被数据迁移、审计和跨工具诊断限制。

### 4.4 Harness 是可优化的工程表面

**判断。** Agentic Harness Engineering 把智能体可靠性问题从“模型是否足够强”转移到“模型外部工作环境是否可改进”。系统提示、工具描述、工具实现、中间件、技能、子智能体和长期记忆都是可编辑对象。

**机制。** 很多失败不来自模型本身，而来自工具描述含糊、系统提示和工具实现不一致、技能不可发现、记忆污染、子 agent 角色不清或中间件缺失。Harness 是这些外部条件的集合。轨迹证据不仅用于诊断失败，也可用于自动演化 harness：把失败样本压缩成经验，提出 patch，声明预期修复，再通过回归任务验证。

![Agentic Harness Engineering 方法](notes/p-011_Agentic_Harness_Engineering_Observabilit/images/method.png)

图 4-2 支撑的判断是：harness 可以作为可观测、可编辑、可回滚的工程对象，而不是隐藏在 prompt 和工具代码里的经验集合。

**含义。** 当 agent 失败时，修复动作不应只有换模型和改 prompt。更常见的修复可能是收紧工具 schema、增加中间件、拆分技能、改写记忆策略、约束子 agent 或修改 evaluation harness。平台应记录这些 harness 变更的版本、预期影响和回滚条件。

### 4.5 审计能力需要防篡改证据链

**判断。** 审计日志和调试日志目标不同。调试日志追求信息充分；审计日志追求证据可信。受监管智能体系统需要记录身份、策略版本、动作、结果、时间戳、敏感字段处理和完整性证明。

**机制。** 如果智能体能调用企业系统、访问用户数据或影响业务状态，事后只拿普通日志截图无法满足责任追踪。审计能力必须在动作发生时生成证据链：谁发起、谁授权、依据哪个策略、调用哪个工具、返回什么结果、敏感字段如何处理、记录是否被篡改。AAT、AutoGen RFC、SIEM 集成和 OWASP agentic security 材料都说明，审计能力不是事故后整理日志，而是运行时协议的一部分。

![Agent harness safety auditing pipeline](notes/p-017_Auditing_Agent_Harness_Safety/images/pipline.png)

图 4-3 支撑的判断是：安全审计要覆盖完整执行管线，而不是只检查最终输出。它使审计对象从 answer 扩展到 prompt、tool、policy、state 和 action。

**含义。** 这会推动可观测系统引入签名、hash chain、Merkle tree、WORM storage、OPA 策略记录和访问审计。它也会加剧隐私与诊断之间的张力：越完整的轨迹越有助于复盘，但也越可能包含敏感数据。工程上应把调试日志和审计日志分层，分别设置保留、脱敏、访问和完整性策略。

### 4.6 成本是可观测性信号

**判断。** Token 成本、工具调用成本、重试成本和缓存命中率正在成为 agent observability 的核心指标。成本异常往往意味着系统行为异常：上下文无限膨胀、工具循环、失败重试、agent 间重复工作、检索不命中或模型路由错误。

**机制。** Agent 的成本不是单次模型价格，而是任务路径的函数。一个规划错误可能导致多轮工具循环，一个检索错误可能扩大上下文，一个模型路由错误可能把简单任务送到昂贵模型，一个失败恢复机制可能在不可行任务上反复重试。成本曲线因此是系统行为的投影。

![成本分解框架](notes/images/[s1-007]/amazon_bedrock_agentcore_production_guide_cost_decomposition.png)

图 4-4 支撑的判断是：成本应分解到模型 token、runtime、memory、可观测性流量和工具链，而不是只在账单层汇总。

**含义。** 成本分析不能停留在月度账单。生产平台应支持按任务、用户、agent、工具、模型、失败类别和 trace 片段 drill down。更合理的指标不是单次调用成本，而是单次成功任务成本、单位质量成本和失败样本浪费成本。

### 4.7 Token 效率必须带质量分母

**判断。** Token 经济学的核心不是把 token 压到最低，而是理解 token 投入的边际收益。多智能体系统、长上下文 agent 和自愈合工作流都可能通过消耗更多 token 获得更高成功率；但如果报告只展示成功率提升，不展示 token、延迟和调用次数，就无法判断这种提升是架构改进，还是单纯把计算预算放大。

**机制。** Token 效率至少有三个分母：任务质量、延迟约束和失败风险。压缩上下文会降低输入成本，但可能丢失诊断和审计证据；使用强模型会提高单次成本，但可能减少重试；自愈合机制会提高恢复概率，但在不可行工作流上可能成为成本陷阱。因此，token 优化必须和质量评测、失败归因、预算策略一起报告。

**证据。** Anthropic 多智能体研究系统中“token 消耗解释大部分性能差异”的观察，AI-NativeBench 对 token 经济学和自愈合成本陷阱的讨论，以及 AgentCore/GenAIOps 对模型路由、prompt caching、batch inference 和上下文窗口保护的实践，都说明 token 效率已经成为 agent 系统评价的一条主轴。

**含义。** 综述应把“成本/token/质量”作为三元指标，而不是把成本放在附录。合理的比较至少包括三类指标：每请求或每会话 token、成功率/token 或质量/美元、失败 trace 的浪费成本。生产平台也应把预算策略作为可观测对象记录下来，包括预算层级、阈值、降级动作、模型候选、缓存命中和人工豁免。

## 5. 关键对比

本章的对比不是为了给论文或产品排名，而是为了帮助系统设计者选择分析层。每张表都回答一个实际决策问题：当前问题应该用日志、诊断、合规、运行监控、离线分析，还是 token 经济学来处理。

### 5.1 失败诊断、过程合规与结构化日志

| 维度 | 失败诊断 | 过程合规 | 结构化日志 |
|---|---|---|---|
| 核心问题 | 哪里失败、为什么失败 | 是否按规范行动 | 发生了什么、如何复现 |
| 典型输入 | 失败轨迹、工具约束、人工标注 | 系统提示、工具 schema、完整轨迹 | 消息、工具调用、状态、span |
| 典型输出 | 关键失败步骤、失败类别、责任主体 | 多维合规评分、违规类型 | 结构化事件、可查询 trace |
| 适用阶段 | 失败后调试与 benchmark 分析 | 持续评测与治理审计 | 运行时采集与离线分析基底 |
| 代表工作 | AgentRx、Who&When、DoVer、GUIDE | AgentPex、Monitoring Monitorability、HarnessAudit | AgentTrace、OpenInference、OTel、Hermes |

**读法。** 三者不能互相替代。结构化日志是底座，过程合规是规范检查，失败诊断是根因解释。只做日志会停留在“可看见”；只做合规会知道违规但未必知道如何修；只做诊断而没有稳定 schema 则难以规模化。

**工程决策。** 如果系统刚进入生产，优先补结构化日志和导出能力；如果业务风险来自越权、遗漏审批或工具误用，优先补过程合规；如果已经积累失败样本但修复效率低，优先投入失败诊断和根因分类。成熟平台应把三者连成闭环：日志采集事件，合规标记风险，诊断定位修复点。

### 5.2 学术论文与产品材料

| 维度 | 学术论文 | 产品/工程材料 |
|---|---|---|
| 关注对象 | 失败机制、归因任务、评测基准、形式化定义 | SDK 接入、dashboard、告警、成本、团队流程 |
| 证据形态 | 数据集、实验、消融、统计指标 | 文档、集成示例、架构图、客户案例 |
| 优势 | 问题定义清晰，能比较方法效果 | 贴近生产需求，暴露部署约束 |
| 盲区 | 部署成本和组织流程不足 | schema 细节和可复现实验不足 |
| 综述用法 | 概念和方法基准 | 工程需求和落地证据 |

**读法。** 这两类材料必须合读。只读论文会低估平台接入、权限、成本、隐私和组织流程问题；只读产品材料会高估 dashboard 对失败诊断的帮助，并低估可复现实验的重要性。

**工程决策。** 学术材料适合回答“这个问题是否被形式化、有没有基准、方法是否可比较”；产品材料适合回答“这个能力如何接入、谁来维护、数据如何流转、成本如何控制”。综述在引用时应明确证据类型，避免用厂商叙述替代方法证据，也避免用离线 benchmark 直接外推生产效果。

### 5.3 OpenTelemetry 与 Agent-specific Schema

| 维度 | OpenTelemetry | Agent-specific Schema |
|---|---|---|
| 擅长 | 跨服务 trace、span 传播、指标/日志生态、厂商集成 | 意图、计划、工具语义、记忆、推理步骤、规范和失败类别 |
| 不足 | 容易丢失 agent 任务语义 | 容易碎片化，生态互通弱 |
| 最佳组合 | OTel 作为传输和关联骨架 | agent-specific 字段作为诊断语义层 |

**读法。** 未来成熟方案大概率不是二选一，而是“OTel + agent semantic conventions + 可控隐私策略”。OTel 解决跨服务传播和企业后端集成，agent-specific schema 解决诊断语义。两者的结合决定 trace 是只能看，还是能诊断、评测和审计。

**工程决策。** 如果团队已有 Datadog、New Relic、Elastic、Splunk 或 CloudWatch，优先把 agent trace 接入 OTel 生态；如果团队要做失败归因、过程合规或 harness 演化，必须在 OTel span 上补充 agent、tool、state、policy、eval、cost 等语义字段。

### 5.4 单智能体失败与多智能体失败

| 维度 | 单智能体失败 | 多智能体失败 |
|---|---|---|
| 失败边界 | 单条轨迹内的步骤、工具和状态 | 多个角色之间的消息、依赖和共享状态 |
| 主要根因 | 工具参数错误、计划偏离、误读观察、输出不合规 | 通信丢失、角色职责混淆、依赖传播、冲突决策 |
| 归因难点 | 第一个不可恢复步骤不唯一 | 责任可能跨 agent 和时间扩散 |
| 所需 trace | 步骤级消息和工具调用 | agent 身份、交互边、依赖链、共享资源访问 |
| 代表材料 | AgentRx、AgentPex、AgentSight | Who&When、Why Do Multi-Agent LLM Systems Fail、EvoCF、MASPrism |

![多智能体失败分类图](notes/p-021_Why_Do_Multi_Agent_LLM_Systems_Fail/images/taxonomy_neurips_final_10_23_25.png)

图 5-1 支撑的判断是：多智能体失败不是单智能体错误的简单相加，而是引入了通信、角色、依赖和共享状态等新的失败轴。

**工程决策。** 单智能体系统可以先从步骤级 trace 和工具 schema 入手；多智能体系统必须额外记录 agent 身份、handoff、消息边、依赖关系和共享资源访问。否则，失败归因会被压扁成单条日志流，无法区分“某个 agent 做错了”与“协作协议把错误放大了”。

### 5.5 运行时监控与离线分析

| 维度 | 运行时监控 | 离线分析 |
|---|---|---|
| 目标 | 及时发现异常、告警、限流或阻断 | 解释失败、比较模型、生成证据和改进系统 |
| 延迟要求 | 低延迟、低开销、可在线执行 | 可接受批处理和较高 judge 成本 |
| 数据粒度 | 核心 span、指标、错误和抽样日志 | 完整轨迹、原始上下文、标注和实验结果 |
| 常见方法 | OTel、eBPF、SDK 插桩、dashboard | AgentRx、AgentPex、AHE、benchmark 分析 |
| 取舍 | 实时性优先，解释可能较浅 | 解释性优先，成本和隐私压力更高 |

**读法。** 生产系统需要二者配合。运行时监控负责及时发现和止损，离线分析负责系统性修复和知识沉淀。二者的分界不是工具类型，而是延迟、成本和解释深度的取舍。

**工程决策。** 对高吞吐常规路径，可用抽样 trace 加全量 metrics；对错误路径、高成本路径、安全敏感路径，应保留完整 trace。这样既控制存储和隐私成本，又保留足够诊断证据。

### 5.6 Token 成本与质量收益

| 维度 | 降低总 token 花费 | 提高单位 token 质量产出 | 降低失败浪费 |
|---|---|---|---|
| 优化目标 | 控制账单和预算 | 提升质量/美元或成功率/token | 减少失败、重试和工具循环造成的无效消耗 |
| 主要指标 | 每请求 token、每会话成本、账单预测 | 成功率/token、质量/美元、边际收益 | 失败 trace 成本、重试次数、循环调用成本 |
| 风险 | 过度压缩导致质量下降 | 高质量样本掩盖成本不可扩展 | 只处理失败路径，不处理正常路径低效 |
| 需要字段 | prompt/completion token、模型价格、用户/功能标签 | 评测分数、任务难度、模型选择 | 失败类别、重试链、工具循环、终止原因 |

**读法。** Token 经济学不能被简化为“少用 token”。很多优化会在不同维度上移动成本：上下文压缩降低输入 token，但可能损失审计和诊断证据；更强模型减少重试，但单次调用价格更高；自愈合机制提升可恢复性，但在不可行任务上可能形成成本陷阱。

**工程决策。** 任何性能结论都应同时报告质量、token、延迟和调用次数。一个消耗 15 倍 token 只提升少量准确率的架构，与一个消耗 2 倍 token 获得显著可靠性提升的架构，其工程价值完全不同。

### 5.7 模型路由、上下文压缩与缓存复用

| 维度 | 模型路由 | 上下文压缩 | 缓存复用 |
|---|---|---|---|
| 机制 | 按任务难度、风险和预算选择模型 | 裁剪、摘要或分层保留历史上下文 | 复用 prompt、工具结果或语义相似响应 |
| 主要收益 | 降低昂贵模型调用占比 | 降低每轮输入 token 与延迟 | 减少重复计算和外部调用 |
| 主要风险 | 低估任务难度导致质量下降 | 丢失关键证据或审计上下文 | 缓存陈旧、隐私泄漏或错误复用 |
| 观测要求 | 记录路由理由、候选模型和降级结果 | 记录被裁剪内容摘要与压缩比例 | 记录命中率、失效策略和复用来源 |

**读法。** 这三类机制是当前最实用的成本控制杠杆。它们共同要求 trace schema 记录“为什么做出成本决策”，而不仅是“最后花了多少钱”。否则，团队只能看到成本下降或质量下降，却无法判断是哪条策略导致变化。

**工程决策。** 模型路由适合任务异质性高的产品，上下文压缩适合长程 agent 和多轮会话，缓存复用适合重复查询、稳定工具和高频工作流。三者都应绑定质量回归测试：成本下降如果伴随过程违规、失败率上升或审计证据丢失，就不是有效优化。

## 6. 方法谱系

本章的核心判断是：现有方法不是一组松散论文，而是一条从 trace capture 到 diagnosis、governance、platformization 和 token economics 的流水线。每个谱系解决一个不同的中间环节，缺少任何一环都会让可观测性退化为“能看见但不能行动”。

### 6.1 轨迹记录与标准化

**判断。** 轨迹记录与标准化是所有后续能力的前提。AgentTrace、OpenInference、Hermes trajectory format、AAT 草案、OpenTelemetry GenAI 语义约定和各平台 SDK 构成了这一谱系。

**机制。** 这一谱系的中心问题是如何在互操作性、隐私和诊断语义之间取得平衡。AgentTrace 强调 agent 行为不能只用普通 request span 表示；OpenInference 把 LLM/agent 应用接入 OTel 生态；Hermes 从训练数据角度强制轨迹格式一致；AAT 把审计和合规需求提前纳入日志结构。它们分别服务不同下游，但最终会在同一个生产系统中相遇。

**证据对象。** AgentTrace 流程图适合解释 agent 行为三表面；OpenInference 规范适合解释 OTel 语义扩展；AAT 草案适合解释审计字段为什么不能事后补。三类证据共同说明：记录格式不是存储细节，而是下游诊断、评测和审计的能力边界。

**含义。** 标准化的目标不是抹平所有平台差异，而是定义可交换的最小公共证据层。平台可以保留私有增强字段，但应保证核心 trace、span、agent、tool、eval、cost 和 audit 信息能跨系统迁移。

### 6.2 失败诊断与根因定位

**判断。** 失败诊断谱系试图把人工读日志变成半自动或自动诊断。AgentRx、Who&When、DoVer、HORIZON、AgentDiagnose、MASPrism、GUIDE、EAGER、OpsAgent、SeqCV 等工作从不同角度推进这一目标。

**机制。** AgentRx 是约束驱动诊断的核心代表；Who&When 形式化了多智能体失败主体和时间定位；DoVer 强调通过干预验证归因；HORIZON 把长程任务失败拆成可比较维度；AgentDiagnose 通过 toolkit 和可视化支持轨迹质量分析；MASPrism 和执行轨迹语义工作展示了轻量模型和结构化信号的可能性。

![DoVer 干预式调试流程](notes/p-003_DoVer_Intervention-Driven_Auto_Debugging/images/fig2_pipeline.png)

图 6-1 支撑的判断是：诊断不能只让 LLM 阅读日志后给解释，还需要通过干预或替换关键步骤验证归因。它把“看起来像原因”的步骤和“确实改变结果”的步骤区分开。

**含义。** 这一谱系短期内更现实的定位是“放大工程师的注意力”：先筛出关键步骤、可疑 agent、违规工具调用和高价值失败样本，再由人确认修复。长期目标才是端到端自动诊断。

### 6.3 过程评测与自动监督

**判断。** 过程评测谱系反对只看最终结果。AgentPex、AgentPro、HarnessAudit、Monitoring Monitorability、alignment auditing agents、Detecting Safety Violations Across Many Agent Traces 和相关安全评测材料共同说明，智能体行为需要过程级监督。

**机制。** 过程评测的关键是把系统提示、工具 schema、业务规则和安全策略转成可检查规范。提示和工具 schema 写得越清楚，过程规范越容易抽取；业务规则越隐含，judge 越可能不稳定。Monitorability 相关材料进一步说明，观察推理和中间行为会改变风险检测能力。

**证据对象。** CoT monitorability 图表说明过程信号对监控能力有独立贡献；HarnessAudit 流程说明安全评估应覆盖完整 harness；AgentPex 说明最终 reward 和过程规范分数相关但不等价。

**含义。** 未来系统可能需要把“可评测性”作为 prompt/tool/harness 设计要求：规范如果不能被机器检查，就很难成为稳定治理机制。过程评测的质量不只取决于 judge 模型，也取决于上游规范是否清晰、可枚举、可追踪。

### 6.4 Harness 演化与数据飞轮

**判断。** Harness 演化谱系说明 trace 的最终价值不只是观察，而是改进。Agentic Harness Engineering、Continual Harness、Lifting Traces to Logic、FLARE、Teaching Text Agents to Learn from Failure、AgentLoop、Coze Loop 和各类评估数据集材料共同构成“从 trace 到改进”的数据飞轮。

**机制。** 失败轨迹可以转化为训练数据、规则、技能、memory、prompt patch、tool schema patch 或 harness 组件变更。AHE 的“可证伪编辑契约”尤其重要：每次自动修改都应声明预期修复和潜在回退，下一轮用任务级结果验证。这比让 agent 自我解释“为什么改”更可靠。

![Lifting Traces to Logic 方法概览](notes/p-024_Lifting_Traces_to_Logic_Programmatic_Ski/images/fig2_overview.png)

图 6-2 支撑的判断是：轨迹可以被提升为可组合的程序化技能或规则，而不只是保存在日志系统里。它把 trace reuse 从经验总结推进到可执行结构。

**含义。** 数据飞轮不应只收集“好样本”和“坏样本”，还应记录每次 harness 变更的预测、版本、评测结果和回滚条件。否则，自动演化会变成不可审计的 prompt drift。

### 6.5 安全、审计与合规

**判断。** 安全审计谱系要求 trace 不只是可读，还要可信。AgentVerify、OWASP ASI、Attack and Defense Landscape survey、Agent Audit Trail、AutoGen audit RFC、tamper-evident audit trail 和企业治理材料共同构成这一方向。

**机制。** 在这一谱系中，运行时监控、策略执行和审计记录必须联动。策略检查没有审计记录，无法证明执行过；审计记录没有防篡改，无法作为证据；防篡改记录没有语义字段，无法支持调查。智能体安全治理因此会推动 trace schema 变得更重、更严格。

**证据对象。** AAT 草案的记录字段、AutoGen tamper-evident RFC 的完整性要求、OWASP agentic security 的风险分类和 HarnessAudit 的执行轨迹评估共同说明：安全不只是输出过滤，而是贯穿策略、工具、身份、状态和审计的系统问题。

**含义。** 安全审计会提高采集成本和隐私压力，但这是生产化的必要代价。工程上需要通过字段分层、脱敏、hash、签名、采样和访问控制来平衡诊断深度与数据暴露。

### 6.6 产品平台与市场

**判断。** 产品平台谱系显示，agent observability 正在从单点 trace viewer 走向 eval、dataset、prompt 管理、成本控制和治理的一体化平台。Langfuse、Arize Phoenix、Braintrust、AgentOps、Helicone、LangSmith、Datadog、Splunk、Elastic、New Relic、AWS、Google、阿里云、百度、Coze 等材料构成这一市场图谱。

**机制。** 这些平台之间的差异可以按四条轴看：开源与闭源、自托管与 SaaS、LLM/agent 专用与传统 APM 扩展、eval-first 与 monitoring-first。Langfuse 和 Phoenix 更强调开放与自托管，Braintrust 更强调 eval 与团队工作流，Helicone 借 proxy/gateway 进入请求与成本管理，Datadog/Elastic/New Relic/Splunk 则利用已有 APM 生态承接企业运维。

![AgentSight 系统架构](notes/p-025_AgentSight_System-Level_Observability_fo/images/fig2_agentsight_system_architecture.png)

图 6-3 支撑的判断是：系统级 observability 需要把 agent framework、instrumentation、storage、analysis 和 UI 连接成完整平台，而不是只提供单个 SDK。

**含义。** 产品层最重要的趋势是 eval 和 observability 的融合。传统 APM 关注延迟、错误和吞吐；LLM/agent 平台还必须关注输出质量、安全性、成本、提示版本、数据集和评测实验。只做 trace viewer 的工具会被平台化能力挤压。

### 6.7 Token 经济学与成本控制

**判断。** Token 经济学谱系正在成为 agent observability 的独立分支。它不只是成本归因，而是把 token 投入、模型选择、工具调用、上下文管理、缓存、质量和失败风险放在同一优化框架中。

**机制。** 这一谱系可以分成三支。第一支是成本可见性：把 token、模型价格、工具调用、重试、用户/功能标签和账单预测接入同一 trace 域，代表材料包括 AI Cost Visibility、LLM Agent Cost Attribution、Helicone、AgentOps、Datadog、Elastic 和 GenAIOps。第二支是成本控制机制：模型路由、prompt caching、语义缓存、工具结果缓存、batch inference、上下文裁剪、采样和预算护栏，代表材料包括 AWS AgentCore、AI Agents in Production、A Guide to AI Agent Cost Optimization 和各类平台文档。第三支是质量归一化评价：把成功率、评测分数、失败类别和 token 消耗一起报告，代表材料包括 Token Economics for LLM Agents、AI-NativeBench、Anthropic 多智能体研究系统和安全/监控成本权衡相关工作。

**证据对象。** AWS AgentCore 的成本分解图适合说明成本桶；token 成本与质量收益表适合说明评价指标；模型路由、上下文压缩和缓存复用表适合说明控制杠杆。

**含义。** 这三支当前还没有完全汇合。成本可见性工具往往能回答“钱花在哪里”，但不能自动决定“下一次如何少花且不降质”；成本控制机制有工程效果，但缺少统一的质量/token 指标；学术评测开始关注 token 经济学，却常常没有接入真实账单、企业限流和多租户预算。未来更完整的系统应把 trace、eval、billing 和 policy engine 连接起来，使“预算策略”成为可观测、可解释、可回滚的运行时对象。

## 7. 研究缺口

### 7.1 跨格式语义映射仍缺失

OpenTelemetry、OpenInference、AgentTrace、Hermes、ShareGPT、AAT、各产品自定义格式之间尚无稳定映射。没有这个映射，诊断器很难跨平台复用，benchmark 也难以比较。

### 7.2 失败分类法碎片化

AgentRx、Who&When、HORIZON、HarnessAudit、AgentDiagnose、AgentPex 和安全材料都有自己的类别体系。未来需要一套分层分类法：底层描述事件和工具错误，中层描述认知/计划/协作错误，高层描述业务和治理风险。

### 7.3 长轨迹与多智能体因果推断仍不可靠

长轨迹中错误传播路径长，后果和根因容易混淆。多智能体场景中，责任还可能跨 agent 边界传播。现有 LLM-as-judge 方法在这类场景中需要更多结构化辅助和干预验证。

### 7.4 过程评测依赖规范质量

AgentPex 类方法依赖系统提示和工具 schema 中可抽取的规范。真实业务常常把规则藏在文档、人工习惯和隐式流程中。如何把业务规范转成可检查规则，是过程评测落地的瓶颈。

### 7.5 隐私与诊断深度冲突

完整 trace 可能包含用户数据、企业机密、文件内容、内部推理和工具返回。masking、hash、采样和最小化记录会保护隐私，但也可能破坏诊断证据。当前材料对这一权衡讨论不足。

### 7.6 成本归因与质量归因尚未统一

成本平台能展示 token 和调用费用，评测平台能展示质量和失败，但二者经常分离。真正有用的指标应是“单位成功任务成本”“单位质量成本”“失败根因对应浪费成本”。这需要 trace、eval 和 billing 数据可 join。更进一步，还需要把模型路由、缓存命中、上下文压缩和预算降级写入同一事件流，否则团队只能在账单层面看到结果，无法解释成本变化来自哪条控制策略。

### 7.7 Token 预算策略缺少标准化表示

当前材料对 token 预算的讨论多停留在产品或工程建议层：设置阈值、做告警、路由到便宜模型、压缩上下文或终止任务。但“预算策略”本身尚未成为标准化 trace 对象。一个生产系统应该能记录预算所属层级、预算剩余量、触发阈值、降级动作、模型候选、压缩比例、缓存命中和人工豁免。没有这些字段，预算控制无法审计，也无法与质量变化做因果分析。

### 7.8 自动修复缺少生产实证

AHE、Continual Harness、Lifting Traces to Logic 等工作显示 trace 可以驱动系统演化，但生产环境中自动修改 harness、prompt、tool 和 memory 的风险仍未充分评估。自动修复需要版本控制、预测声明、回滚机制和人类审批。

---

## 8. 面向系统设计的建议

1. 把 trace schema 作为产品/API 设计的一部分，而不是日志后处理格式。
2. 采用 OTel 作为传播骨架，同时保留 agent-specific 语义字段。
3. 每条工具调用至少记录工具名、参数摘要、返回摘要、错误、耗时、调用者 agent、父 span 和任务上下文。
4. 对多智能体系统显式记录 agent 身份、handoff、依赖边、共享状态访问和子 agent 侧链。
5. 将最终 reward、过程规范、失败类别、成本和安全事件写入同一 trace 关联域。
6. 对受监管场景区分调试日志和审计日志，审计日志要有身份、策略版本、时间戳和完整性保护。
7. 让失败样本进入数据飞轮：诊断、标注、评测集、prompt/tool/harness patch、回归测试。
8. 对自动修改建立可证伪变更契约：预期修复什么、可能破坏什么、如何回滚。
9. 产品选型时不要只看 dashboard，要检查原始轨迹导出、schema、隐私控制、eval 集成和成本 drill-down。
10. 对长轨迹和多智能体任务，不要只依赖单体 LLM judge；结合约束、干预、结构化信号和人工复核。
11. 把 token 预算作为运行时策略对象记录下来，包括预算层级、剩余额度、触发阈值、降级动作和豁免原因。
12. 把成本优化拆成模型路由、上下文压缩、缓存复用、批量异步和采样策略，并分别记录质量影响。
13. 报告 agent 质量时同步报告 token、延迟、调用次数和失败浪费成本，避免用更大计算预算伪装为架构改进。

---

## 9. 结论

智能体可观测性正在形成一个新的基础设施层。它以轨迹为原始材料，但目标不是保存日志，而是生成可行动证据。这个证据层同时服务于六件事：运行时监控、失败诊断、过程评测、安全审计、成本归因和 token 预算控制。

117 篇本地笔记显示，学术界已经把 trace 分析从黑盒结果评估推进到步骤级归因、过程合规、长程失败机制、harness 演化和 token 经济学；产业界则把可观测性与 eval、dataset、prompt 管理、成本控制、预算治理和合规集成到平台中。两条路线正在汇合。未来真正有价值的系统不是单点 trace viewer，而是能把 OpenTelemetry 生态、agent-specific schema、自动诊断、过程评测、审计证据、token 经济学和数据飞轮连接起来的综合平台。

因此，智能体可观测性的核心问题可以概括为一句话：如何把不可预测的智能体执行过程，转化为可复现、可解释、可验证、可审计、可改进的工程证据。这个问题将决定 2026 年以后 agent 系统能否从演示走向可靠生产。
