## 2. 核心词条：从 trace 到可行动证据

本章先澄清若干核心词条。这里的目的不是给出孤立定义，而是建立后文综述的推理链条：智能体系统首先需要把运行过程记录成可分析的轨迹；轨迹经过 schema 和插桩规范化后，才能支持失败归因、过程合规、harness 改进、审计追责和 token 经济学分析。换言之，本文所说的 trace 不是“日志文件”的同义词，而是贯穿学术方法和产业平台的共同证据层。

### 2.1 智能体轨迹

智能体轨迹是按时间组织的执行证据，覆盖用户意图、模型消息、工具调用、工具返回、状态读写、环境观测、评测结果和成本事件。它与普通日志的关键差别在于，普通日志主要回答“发生了什么”，而智能体轨迹还要回答“为什么这样发生、是否应该这样发生、后续能否据此修复”。因此，轨迹必须保留事件之间的上下文关系，而不能只保存一组离散的请求和响应。

学术界对轨迹的处理重点是字段语义和分析可用性。[AgentTrace](../../../notes/p-014_AgentTrace_A_Structured_Logging_Framewor.md) [[R001]](../../../notes/p-014_AgentTrace_A_Structured_Logging_Framewor.md) 将智能体行为拆成系统级、认知级和环境级三类表面，使执行、推理和环境反馈都能进入同一条可分析记录；[Hermes Agent Trajectory Format](../../../notes/c-013_Hermes_Agent_Trajectory_Format.md) [[R002]](../../../notes/c-013_Hermes_Agent_Trajectory_Format.md) 从训练数据和重放角度强调工具调用、工具响应和消息结构的一致性；[OpenInference Specification](../../../notes/c-014_OpenInference_Specification.md) [[R003]](../../../notes/c-014_OpenInference_Specification.md) 则把 LLM、agent、tool、retriever、embedding、evaluator、guardrail 等 span kind 纳入 OpenTelemetry 语义空间。三者的共同点是：轨迹字段不是越多越好，而是必须面向后续诊断、评测、审计和训练任务。

![AgentTrace 系统流程图](../../../notes/p-014_AgentTrace_A_Structured_Logging_Framewor/images/fig1_system_flow.png)

图 2-1 说明，AgentTrace 并不把智能体压缩成一次 LLM request，而是同时记录系统执行、认知步骤和环境交互。这正是 agent trace 与普通 API 日志的分水岭：工具调用、状态更新和环境反馈经常是失败根因，若这些事件没有结构化记录，后续只能靠人工阅读文本猜测。

产业界的做法更关注接入路径和可视化运营。[Datadog LLM Observability](../../../notes/s2-006_Monitor_troubleshoot_and_improve_AI_agen.md) [[R004]](../../../notes/s2-006_Monitor_troubleshoot_and_improve_AI_agen.md) 将 agent 执行流、token 使用和错误位置纳入既有 APM 体验；[Langfuse](../../../notes/s2-014_langfuselangfuse__GitHub.md) [[R005]](../../../notes/s2-014_langfuselangfuse__GitHub.md) 以开源自托管方式连接 trace、prompt、eval 和 dataset；[Arize Phoenix](../../../notes/s2-016_Arize-aiphoenix__GitHub.md) [[R006]](../../../notes/s2-016_Arize-aiphoenix__GitHub.md) 强调 open instrumentation 与评估；[AgentOps](../../../notes/s2-020_AgentOps_-_AI_Agent_Monitoring_and_Obser.md) [[R007]](../../../notes/s2-020_AgentOps_-_AI_Agent_Monitoring_and_Obser.md) 则将 session replay、token tracking 和 agent 运行监控产品化。产业路线的优点是把 trace 变成团队能使用的 timeline、dashboard、query 和 replay；局限是许多产品仍停留在“看见执行流”，尚未稳定支持因果诊断和跨平台 schema 互操作。

如果把例子具体到互联网和云厂商，轨迹的产品形态会更清楚。Google 路线把 ADK/Vertex AI Agent Builder 的 agent 执行接入 Cloud Trace，使开发者能沿着分布式 trace 查看 agent、工具和后端服务之间的调用链，[Google Cloud Trace observability for ADK](../../../notes/s1-001_Google_Cloud_Trace_observability_for_ADK.md) [[R032]](../../../notes/s1-001_Google_Cloud_Trace_observability_for_ADK.md) 的重点不是单独展示 prompt，而是把 agent 作为云应用的一段可追踪执行。AWS 路线更偏生产运维：[Amazon CloudWatch generative AI observability](../../../notes/s1-006_Amazon_CloudWatch_generative_AI_observab.md) [[R033]](../../../notes/s1-006_Amazon_CloudWatch_generative_AI_observab.md) 将生成式 AI 指标、日志和 trace 纳入 CloudWatch，[AgentCore Runtime Observability](../../../notes/s1-008_Part_3_AgentCore_Runtime_Observability.md) [[R034]](../../../notes/s1-008_Part_3_AgentCore_Runtime_Observability.md) 则把 Bedrock AgentCore 的 runtime、session、工具调用和错误信号放进云端观测路径。这些材料说明，大厂的 trace 不是孤立 LLM 调试器，而是要和云监控、权限、计费、告警和服务链路统一。

国内互联网和云厂商的例子也体现了类似方向，但更强调平台入口和业务开发体验。[阿里云 AgentLoop](../../../notes/s2-001_什么是AgentLoop-云监控CMS__阿里云文档.md) [[R035]](../../../notes/s2-001_什么是AgentLoop-云监控CMS__阿里云文档.md) 将智能体链路观测放进云监控 CMS，[百炼 Model Studio 应用观测](../../../notes/s2-002_应用观测-大模型服务平台百炼Model_Studio__阿里云文档.md) [[R036]](../../../notes/s2-002_应用观测-大模型服务平台百炼Model_Studio__阿里云文档.md) 关注应用级调用、模型请求和运行指标；[百度千帆 AppBuilder Trace](../../../notes/s2-003_Appbuilder_Trace跟踪功能基本用法__百度千帆文档.md) [[R037]](../../../notes/s2-003_Appbuilder_Trace跟踪功能基本用法__百度千帆文档.md) 提供应用构建过程中的 trace 跟踪能力；[Coze Loop](../../../notes/s2-005_目前主流的智能体可观测性和智能体评测相关的产品调研__Coze_Loop详细介绍.md) [[R038]](../../../notes/s2-005_目前主流的智能体可观测性和智能体评测相关的产品调研__Coze_Loop详细介绍.md) 则把 trace、评测、数据集和 prompt/agent 迭代组织成产品工作流。这些例子补足了一个事实：互联网厂商更关心 trace 如何嵌入“应用搭建-评测-发布-运营”的闭环，而不仅是研究原型里的轨迹格式。

因此，智能体轨迹的定义应从下游用途反推。若目标只是统计 token 和延迟，普通 LLM span 足够；若目标是失败归因，必须记录工具 schema、参数、返回、状态变化和事件依赖；若目标是审计，必须记录身份、时间顺序、策略版本和完整性字段；若目标是 token 经济学，必须记录模型选择、缓存命中、重试链、预算策略和任务质量。

### 2.2 失败归因

失败归因关注失败由哪个智能体、哪个步骤、哪类约束违反或哪条依赖链触发。它不是简单地把失败轨迹交给 LLM 总结，而是要把“看起来异常的步骤”转化为“可验证的根因”。这一区分很重要：长轨迹中后续多个步骤都可能异常，但它们往往只是早期错误传播的结果；多智能体系统中，最终输出错误也可能来自上游 agent 的错误信息、共享状态污染或角色分工失效。

学术界已经形成几条互补路线。[AgentRx](../../../notes/p-001_AgentRx_Diagnosing_AI_Agent_Failures_from_Execution_Trajectories.md) [[R008]](../../../notes/p-001_AgentRx_Diagnosing_AI_Agent_Failures_from_Execution_Trajectories.md) 将问题具体化为定位“第一个不可恢复关键步骤”，并利用工具 schema、领域策略和执行前缀构造约束检查；[DoVer](../../../notes/p-003_DoVer_Intervention-Driven_Auto_Debugging.md) [[R009]](../../../notes/p-003_DoVer_Intervention-Driven_Auto_Debugging.md) 强调干预式验证，通过替换或修改关键步骤来判断归因是否真的影响结果；[Which Agent Causes Task Failures and When](../../../notes/p-022_Which_Agent_Causes_Task_Failures_and_Whe.md) [[R010]](../../../notes/p-022_Which_Agent_Causes_Task_Failures_and_Whe.md) 把多智能体归因拆成“哪个 agent”和“什么时候失败”；[Long-Horizon Task Mirage](../../../notes/p-016_The_Long-Horizon_Task_Mirage_Diagnosing_.md) [[R011]](../../../notes/p-016_The_Long-Horizon_Task_Mirage_Diagnosing_.md) 则提醒我们，短任务上的诊断成功不能直接外推到长程任务。

![AgentRx 诊断流程](../../../notes/p-001_AgentRx_Diagnosing_AI_Agent_Failures_from_Execution_Trajectories/images/fig1_agentrx.png)

图 2-2 展示了 AgentRx 从轨迹到约束再到失败定位的流程。它支撑的核心观点是：失败归因需要结构化约束和可检查证据，而不是只依赖自然语言解释。

产业界通常从另一个入口开始：先发现异常，再组织复盘。[Datadog LLM Observability](../../../notes/s2-006_Monitor_troubleshoot_and_improve_AI_agen.md) [[R004]](../../../notes/s2-006_Monitor_troubleshoot_and_improve_AI_agen.md) 通过执行流、错误 span 和性能指标帮助工程师定位可疑步骤；[AgentOps](../../../notes/s2-020_AgentOps_-_AI_Agent_Monitoring_and_Obser.md) [[R007]](../../../notes/s2-020_AgentOps_-_AI_Agent_Monitoring_and_Obser.md) 通过 session replay 和 token tracking 暴露异常会话；[Arize Phoenix](../../../notes/s2-016_Arize-aiphoenix__GitHub.md) [[R006]](../../../notes/s2-016_Arize-aiphoenix__GitHub.md) 则把 trace 与评估结合，支持开发者在数据集和实验层面复盘失败。产业工具的强项是快速定位入口和协作排查，弱项是因果验证。一个 span 标红或成本异常并不自动说明它是根因，仍需要 AgentRx/DoVer 式的约束和干预思想补足。

互联网厂商的失败归因更常以“生产事故排查”出现，而不是以论文里的 root-cause benchmark 出现。Google ADK 接入 Cloud Trace 后，工程师可以把一次 agent 失败放回完整服务链路：是 agent 决策错、工具服务慢、后端 API 报错，还是检索/数据库层返回异常 [[R032]](../../../notes/s1-001_Google_Cloud_Trace_observability_for_ADK.md)。AWS 的 CloudWatch 与 AgentCore Runtime 观测路径把模型调用、runtime 错误、工具链路和成本/延迟指标放在一起，使排查从“读 agent 对话”扩展为“看云服务调用链和运行指标” [[R033]](../../../notes/s1-006_Amazon_CloudWatch_generative_AI_observab.md) [[R034]](../../../notes/s1-008_Part_3_AgentCore_Runtime_Observability.md)。阿里云 AgentLoop、百炼、百度千帆和 Coze Loop 则更接近应用平台场景：开发者先在 trace 中看到哪一步组件、插件、知识库或模型调用异常，再把 bad case 放入评测或迭代流程 [[R035]](../../../notes/s2-001_什么是AgentLoop-云监控CMS__阿里云文档.md) [[R036]](../../../notes/s2-002_应用观测-大模型服务平台百炼Model_Studio__阿里云文档.md) [[R037]](../../../notes/s2-003_Appbuilder_Trace跟踪功能基本用法__百度千帆文档.md) [[R038]](../../../notes/s2-005_目前主流的智能体可观测性和智能体评测相关的产品调研__Coze_Loop详细介绍.md)。

这些厂商例子也暴露了当前产业归因的边界：它们能较好回答“异常出现在哪个组件、哪次调用、哪个 session”，但较少直接证明“这一步就是根因”。例如工具服务 500、知识库无召回、模型输出越界、token 激增，都可能只是上游错误传播后的现象。因而本节的判断应更精确：产业平台提供的是归因入口和证据组织能力，学术方法提供的是根因验证机制；二者结合后，才可能从生产 replay 走向可验证 failure attribution。

因此，失败归因在综述中应被理解为一条从运行时信号到可验证解释的链条：异常会话触发关注，结构化 trace 提供证据，约束或分类法生成候选根因，干预或回归测试验证判断，最终形成修复建议。只停在任一环节，都不能称为完整诊断。

### 2.3 过程合规性

过程合规性评估智能体是否按系统提示、工具 schema、业务规则、权限边界和安全策略行动，而不是只看最终答案是否正确。这个词条解决的是评价对象的问题：最终成功可以掩盖过程违规，例如跳过必要确认、调用未授权工具、泄露敏感信息、绕过系统指令，或在用户不可见的中间步骤里违反业务流程。

学术界对过程合规的贡献在于把“过程”变成可评测对象。[AgentPex](../../../notes/p-004_Willful_Disobedience_Automatically_Detecting_Failures_in_Agentic_Traces.md) [[R012]](../../../notes/p-004_Willful_Disobedience_Automatically_Detecting_Failures_in_Agentic_Traces.md) 从提示和工具规范中抽取行为规则，再用 judge 对完整轨迹进行合规评分，证明最终 reward 和过程规范并不等价；[Monitoring Monitorability](../../../notes/p-006_Monitoring_Monitorability.md) [[R013]](../../../notes/p-006_Monitoring_Monitorability.md) 研究过程信号是否能支持风险检测，说明中间推理和过程可见性本身就是监控资源；[HarnessAudit](../../../notes/p-017_Auditing_Agent_Harness_Safety.md) [[R014]](../../../notes/p-017_Auditing_Agent_Harness_Safety.md) 把安全评估单元从最终输出扩展到完整 harness 与执行轨迹。

这三篇论文解决的问题并不相同。AgentPex 的重点是“规则从哪里来”：它把系统提示、任务约束和工具 schema 中的要求抽取成可检查规范，再判断 agent 轨迹是否出现 willful disobedience。因此它适合讨论“最终成功但过程违规”的场景，例如 agent 获得正确答案但跳过必要确认、使用了不该使用的工具，或没有遵守工具参数约束。Monitoring Monitorability 的重点是“过程是否足以被监督”：如果系统没有暴露中间状态、候选动作、风险信号或可解释过程，那么后续 monitor 即使模型很强，也缺少可用输入。HarnessAudit 的重点则是“安全评估对象是谁”：它不只看模型输出，而是把 prompt、tool、memory、权限边界和 harness 组合视为被审计对象，强调安全问题常常发生在模型与外部执行环境的连接处。

| 论文 | 过程合规对象 | 主要机制 | 对本文的支撑 | 局限 |
| --- | --- | --- | --- | --- |
| AgentPex [[R012]](../../../notes/p-004_Willful_Disobedience_Automatically_Detecting_Failures_in_Agentic_Traces.md) | 系统提示、任务规范、工具 schema 与完整执行轨迹 | 从规范中抽取规则，再用 judge 检测轨迹违背 | 证明最终 reward 与过程合规不等价 | 依赖规范可抽取，隐式业务 SOP 难覆盖 |
| Monitoring Monitorability [[R013]](../../../notes/p-006_Monitoring_Monitorability.md) | 中间过程信号、风险特征和可监控性 | 分析过程可见性对 monitor 效果的影响 | 说明“能否被监控”本身是系统能力 | 对生产权限、审计和组织流程讨论较少 |
| HarnessAudit [[R014]](../../../notes/p-017_Auditing_Agent_Harness_Safety.md) | prompt、tool、memory、权限边界和 harness 运行轨迹 | 把安全审计从输出扩展到 harness 与轨迹 | 支撑过程安全和审计证据链 | 自动化修复和大规模生产验证仍不足 |

![AgentPex 过程合规流程](../../../notes/p-004_Willful_Disobedience_Automatically_Detecting_Failures_in_Agentic_Traces/images/fig3_agentpex_pipeline.png)

图 2-3 展示了 AgentPex 如何从任务规范和工具约束出发检查轨迹。它说明过程合规不是主观“看起来合理”，而是把提示、工具 schema 和业务规则转化为可检查条件。

产业界更关心如何把合规要求落实到运行系统。[AI Agents in Production](../../../notes/c-018_AI_Agents_in_Production_Monitoring_Guard.md) [[R015]](../../../notes/c-018_AI_Agents_in_Production_Monitoring_Guard.md) 讨论 guardrail、熔断器、回退和监控实践；[AWS AgentCore Production Guide](../../../notes/s1-007_Amazon_Bedrock_AgentCore_Production_Oper.md) [[R016]](../../../notes/s1-007_Amazon_Bedrock_AgentCore_Production_Oper.md) 把生产运维、成本、可靠性和可观测性放在同一框架中；[OWASP Agentic Top 10](../../../notes/s3-009_OWASP_Top_10_for_Agentic_Applications_Co.md) [[R017]](../../../notes/s3-009_OWASP_Top_10_for_Agentic_Applications_Co.md) 从越权、工具滥用、数据泄露和策略绕过等角度给出风险分类。产业做法的特点是把过程合规转成 policy、guardrail、audit log、alert 和 human review workflow，而不只是离线 benchmark。

这一词条的关键结论是：合规性必须前移到轨迹层。在客户服务、医疗、金融、企业自动化和受监管场景中，过程违规本身就是失败。最终数据库状态正确，不能抵消不合规访问或缺失审批链。因而后续所有关于评测、审计和治理的讨论，都应把过程合规作为与最终结果并列的评价维度。

### 2.4 Harness

Harness 是模型外部可编辑的执行表面，包括系统提示、工具描述、工具实现、中间件、技能、子智能体配置、记忆机制、权限边界和环境协议。它解释了为什么很多智能体失败不能简单归因于“模型不够强”：工具描述含糊、技能不可发现、记忆污染、中间件缺失、子 agent 角色不清，都会导致能力本来足够的模型在系统中失败。

学术界正在把 harness 从经验配置提升为工程对象。[Agentic Harness Engineering](../../../notes/p-011_Agentic_Harness_Engineering_Observabilit.md) [[R018]](../../../notes/p-011_Agentic_Harness_Engineering_Observabilit.md) 提出组件可观测性、经验可观测性和决策可观测性，要求 harness 组件文件化、轨迹经验可压缩、编辑决策带可证伪预测；[Lifting Traces to Logic](../../../notes/p-024_Lifting_Traces_to_Logic_Programmatic_Ski.md) [[R019]](../../../notes/p-024_Lifting_Traces_to_Logic_Programmatic_Ski.md) 进一步展示轨迹可以被提升为规则、技能或程序化结构，用于后续任务复用。两者共同说明，trace 的价值不只是复盘失败，还可以推动 harness 演化。

![Agentic Harness Engineering 方法](../../../notes/p-011_Agentic_Harness_Engineering_Observabilit/images/method.png)

图 2-4 说明，harness 改进需要把运行经验、组件状态和编辑决策连接起来。它把“调 prompt”扩展为更系统的工程任务：管理工具、记忆、技能、子 agent、回归测试和回滚条件。

产业界对 harness 的管理通常落在平台工作流中。[Langfuse](../../../notes/s2-014_langfuselangfuse__GitHub.md) [[R005]](../../../notes/s2-014_langfuselangfuse__GitHub.md) 以 prompt、trace、eval、dataset 形成闭环；[Arize Phoenix](../../../notes/s2-016_Arize-aiphoenix__GitHub.md) [[R006]](../../../notes/s2-016_Arize-aiphoenix__GitHub.md) 强调评估和实验；[AWS AgentCore Production Guide](../../../notes/s1-007_Amazon_Bedrock_AgentCore_Production_Oper.md) [[R016]](../../../notes/s1-007_Amazon_Bedrock_AgentCore_Production_Oper.md) 则把 runtime、memory、observability、成本和部署策略纳入生产运维。产业做法不一定使用 harness 这个术语，但 prompt registry、tool registry、eval set、sandbox、release、rollback 和 budget policy 实际上都在管理 harness。

因此，harness 是连接诊断和改进的中间层。失败归因告诉我们哪里出错；harness 工程决定修哪里、如何验证、如何回滚。若没有 harness 版本和变更记录，trace 只能解释过去，不能稳定改善未来。

### 2.5 审计轨迹、成本归因与 Token 经济学

审计轨迹、成本归因和 token 经济学看似属于不同主题，但在智能体系统中都依赖同一种能力：把运行行为转化为可追责、可聚合、可解释的证据。审计要回答谁在何时依据什么策略做了什么动作；成本归因要回答钱花在哪个用户、功能、模型、工具、agent 或失败链上；token 经济学则进一步追问这些花费是否换来了相应质量、可靠性和业务价值。

审计方向的学术和标准材料强调证据可信度。[Agent Audit Trail](../../../notes/c-012_Agent_Audit_Trail_A_Standard_Logging_For.md) [[R020]](../../../notes/c-012_Agent_Audit_Trail_A_Standard_Logging_For.md) 关注身份、动作、参数、结果、时间顺序和完整性字段；防篡改 audit trail 相关材料说明，多 agent 框架需要原生支持记录完整性；[HarnessAudit](../../../notes/p-017_Auditing_Agent_Harness_Safety.md) [[R014]](../../../notes/p-017_Auditing_Agent_Harness_Safety.md) 则把安全评估落到完整执行轨迹。成本方向的材料强调经济可解释性：[Token Economics](../../../notes/s3-011_Token_Economics_for_LLM_Agents_A_Dual-Vi.md) [[R021]](../../../notes/s3-011_Token_Economics_for_LLM_Agents_A_Dual-Vi.md) 从计算和经济双视角分析 token 投入，[LLM Agent Cost Attribution](../../../notes/s3-014_LLM_Agent_Cost_Attribution_Complete_Prod.md) [[R022]](../../../notes/s3-014_LLM_Agent_Cost_Attribution_Complete_Prod.md) 强调按 agent、功能和工作流拆解成本。

![Token 经济学架构谱系](../../../assets/token-economics-architecture.svg)

图 2-5 将 token 经济学拆成成本可见性、运行时控制、上下文与缓存、质量归一化、数据飞轮等路线。它说明 token 经济学不是“少用 token”的单点技巧，而是贯穿观测、决策、执行、评测和治理的系统架构。

产业界已经把这些主题产品化。[AWS AgentCore Production Guide](../../../notes/s1-007_Amazon_Bedrock_AgentCore_Production_Oper.md) [[R016]](../../../notes/s1-007_Amazon_Bedrock_AgentCore_Production_Oper.md) 将成本拆成模型 token、runtime、memory 和 observability 流量，并提出模型路由、prompt caching、batch inference 等杠杆；[GenAIOps on AWS](../../../notes/s1-010_GenAIOps_on_AWS_End-to-End_Observability.md) [[R023]](../../../notes/s1-010_GenAIOps_on_AWS_End-to-End_Observability.md) 把 input/output token、生成成本、检索质量、TTFT 和上下文窗口保护写入同一观测路径；[AgentOps](../../../notes/s2-020_AgentOps_-_AI_Agent_Monitoring_and_Obser.md) [[R007]](../../../notes/s2-020_AgentOps_-_AI_Agent_Monitoring_and_Obser.md) 强调 runaway cost 检测；[Helicone](../../../notes/s2-022_Helicone_LLM_Observability_Platform__Lea.md) [[R024]](../../../notes/s2-022_Helicone_LLM_Observability_Platform__Lea.md) 通过 gateway/proxy 路线进入请求记录、缓存和成本管理。

这组词条的共同结论是：审计、成本和 token 效率都不能在账单或事故之后才处理。它们必须进入运行时 trace：记录预算阈值、路由理由、缓存命中、压缩比例、人工豁免、策略版本、失败类别和质量分数。否则系统只能知道“花了多少钱”或“出了什么事”，却无法解释为什么发生、是否值得、下一次如何避免。
