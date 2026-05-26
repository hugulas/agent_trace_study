---
tags:
  - Llama-Stack
  - observability
  - metrics
  - telemetry
  - Prometheus
  - GitHub-Issue
  - ogx
  - GenAI-ops
aliases:
  - s1-014
  - Llama Stack 遥测指标增强提案
  - ogx-ai/ogx Issue #2596
date: 2025-07-03
url: https://github.com/ogx-ai/ogx/issues/2596
---

# Llama Stack 遥测可观测性指标增强提案

## 核心信息

- **标题**: Observability: Add Additional Metrics to Llama Stack Telemetry
- **来源类型**: GitHub Issue（功能增强提案）
- **仓库**: ogx-ai / ogx
- **编号**: #2596
- **状态**: Closed as not planned
- **标签**: enhancement, stale
- **提出者**: leseb（Collaborator）
- **提出时间**: 2025 年 7 月 3 日
- **关联里程碑**: Road to v1
- **本地材料**: `[s1-014]-observability-add-additional-metrics-to-llama-stack-telemetr.pdf`
- **证据质量**: medium

## 内容摘要

本议题是 ogx-ai/ogx 仓库中关于 Llama Stack 遥测系统可观测性指标扩展的详细功能提案，
由社区协作者 leseb 于 2025 年 7 月提出。
该提案系统梳理了 Llama Stack 当前仅提供基础 token 统计的现状，
并针对七大核心 API 网关提出了数十项新增指标的完整设计，
旨在将 Llama Stack 的遥测能力从简单的 token 计数提升到生产级可观测平台的标准。

当前 Llama Stack 的遥测系统仅暴露三项基础指标：
`llama_stack_prompt_tokens_total`（输入 token 总量）、
`llama_stack_completion_tokens_total`（输出 token 总量）
以及 `llama_stack_tokens_total`（token 总计）。
这三项指标对于理解推理负载而言是最低限度的，
但在生产环境中运行多模型、多 provider、多 API 的复杂系统时，
运维人员难以回答以下关键问题：
请求成功率如何？
不同 provider 的路由分布是否均衡？
向量检索延迟是否在接受范围内？
Agent 工作流为何频繁失败？
安全检测的误报率是多少？
成本是否在预算之内？
评估任务是否按预期完成？
工具调用是否超时？

提案将新增指标按 API 维度划分为七大类别，
形成了一套覆盖全栈的指标矩阵。

第一类是 API 网关层通用指标，
涵盖请求级别的总量、成功率、错误率、P95 延迟、并发请求数，
以及 provider 路由层面的请求分布和错误分类。
具体包括 `llama_stack_requests_total`（按 api 和 status 标签拆分）、
`llama_stack_request_duration_seconds`（按 api 和 quantile 标签记录 P95 延迟）、
`llama_stack_concurrent_requests`（当前并发数）、
`llama_stack_provider_requests_total`（按 api 和 provider 拆解，如 openai、vllm）、
`llama_stack_provider_errors_total`（按 error_type 进一步细分，如 rate_limit、model_unavailable）。
这些指标是平台运营者了解整体流量分布、
识别热点 provider、定位异常错误模式的第一道防线。

第二类是 Inference API 指标，
这是整个提案中最丰富的指标族。
它不仅细化了模型级请求统计
（`llama_stack_model_requests_total` 按 model_id 和 model_type 拆分），
还新增了流式请求追踪
（`llama_stack_streaming_requests_total`、`llama_stack_streaming_chunks_total`），
这对实时交互场景（如聊天机器人）至关重要。
性能指标方面，提案引入了
`llama_stack_time_to_first_token_seconds`（TTFT，首 token 时间，按 P95 统计）、
`llama_stack_tokens_per_second`（TPS，生成吞吐量，按 P50 统计）、
`llama_stack_inference_duration_seconds`（推理总时长，按 P95 统计）。
此外，token 指标被增强为支持 model_id 和 provider 多维下钻，
例如 `llama_stack_prompt_tokens_total{model_id="llama-3.2-3b",provider="openai"}`，
使得成本归因从平台级精确到模型级。
限流与配额指标（`llama_stack_rate_limit_hits_total`、`llama_stack_quota_exceeded_total`）
则按 user_id 拆分，直接支撑多租户运营治理。

第三类是 Vector I/O API 指标，
覆盖向量数据库的全生命周期操作。
吞吐量指标包括
`llama_stack_vector_inserts_total`（按 vector_db 和 operation 拆分）、
`llama_stack_vector_queries_total`、
`llama_stack_vector_deletes_total`。
性能指标包括
`llama_stack_vector_query_duration_seconds`（查询延迟，P95）
和 `llama_stack_vector_insert_duration_seconds`（插入延迟，P95）。
此外还有
`llama_stack_vector_chunks_processed_total`（已处理 chunk 数量）、
`llama_stack_vector_stores_total`（向量存储数量）、
`llama_stack_vector_files_total`（向量文件数量）、
`llama_stack_vector_dimensions`（向量维度，如 384）。
这组指标对于 RAG 系统的检索性能调优具有直接指导意义——
当查询延迟上升时，
可以通过 documents_retrieved 和 avg_similarity_score 判断是索引问题还是召回质量问题。

第四类是 Safety API 指标。
安全检测不仅统计通过/拦截次数，还按违规类别拆解。
具体指标包括
`llama_stack_safety_checks_total`（按 shield_id 和 status 拆分，如 passed/blocked）、
`llama_stack_safety_violations_total`（按 category 细分，如 violence、hate、sexual、harassment）、
`llama_stack_safety_check_duration_seconds`（检测耗时，P95）、
以及极为少见的 `llama_stack_safety_false_positives_total`（误报计数）。
这种设计体现了提案者对安全系统持续运营的理解：
拦截率本身不足以评估安全策略优劣，
误报对用户体验的损害同样需要量化。

第五类是 Agents API 指标，
这是最具 Agent 特色的指标族。
`llama_stack_agent_workflows_total` 按 agent_id 和 status（completed/failed）
统计工作流完成度；
`llama_stack_agent_steps_total` 记录每个 Agent 的执行步骤数；
`llama_stack_agent_step_duration_seconds` 记录单步耗时；
`llama_stack_agent_tool_calls_total` 追踪工具调用频率与成功率；
`llama_stack_agent_memory_reads_total` 和 `llama_stack_agent_memory_writes_total`
记录内存操作；
`llama_stack_agent_memory_retrieval_duration_seconds` 则衡量内存检索性能。
这些指标填补了当前 Agent 可观测性的关键空白——
主流工具链更关注单次 LLM 调用的 trace，
而对多步骤 Agent 工作流的宏观指标缺乏原生支持。

第六类是 Evaluation API 指标，
包括 `llama_stack_evaluation_tasks_total`（评估任务总数）、
`llama_stack_evaluation_success_rate`（成功率）、
`llama_stack_evaluation_scores_distribution`（评分分布）、
`llama_stack_evaluation_baseline_comparison`（基准对比）等。
这些指标使得持续评估（continuous evaluation）
从离线脚本升级为在线可观测维度。

第七类是 Tool Runtime API 指标，
涵盖 `llama_stack_tool_invocations_total`（工具调用总次数）、
`llama_stack_tool_execution_duration_seconds`（执行时长）、
`llama_stack_tool_timeouts_total`（超时次数）、
`llama_stack_tool_errors_total`（错误次数）、
`llama_stack_tool_by_type_total`（按工具类型分布）。
这对监控外部 API 依赖的健康状态至关重要。

从指标设计风格来看，
提案完全遵循 Prometheus 的命名与标签规范，
所有指标均以 `llama_stack_` 为前缀，
通过 `api`、`provider`、`model_id`、`vector_db`、
`shield_id`、`agent_id`、`user_id`、`quantile` 等标签实现多维下钻。
这种设计与云原生可观测生态
（如 Grafana、Prometheus Alertmanager、VictoriaMetrics）天然兼容，
便于构建统一的监控大盘和告警策略。
尽管该 Issue 最终被标记为 "Closed as not planned"
并因 stale 自动关闭，
但其指标设计框架仍具有极高的参考价值，
可作为任何 LLM 服务平台遥测体系建设的蓝图与 checklist。

## 关键要点

- **现状不足**: Llama Stack 遥测仅提供 prompt/completion/total 三项 token 指标，
  缺乏延迟、错误分类、provider 分布、成本、限流、Agent 状态等生产关键维度。
- **设计哲学**: 采用 Prometheus 原生风格，`llama_stack_` 统一前缀 + 多维标签
  （api、provider、model_id、quantile、user_id 等），便于聚合、下钻与告警。
- **七大 API 全覆盖**: API Gateway、Inference、Vector I/O、Safety、Agents、Evaluation、Tool Runtime，
  每层均有专属指标族，形成全栈可观测矩阵。
- **性能指标细化**: TTFT（首 token 时间）、TPS（每秒 token 数）、推理总时长
  按 P50/P95/P99 分位数上报，满足 SLA 监控与容量规划需求。
- **成本与配额治理**: 引入 `rate_limit_hits_total`、`quota_exceeded_total` 等运营指标，
  按 user_id 拆分，直接支撑多租户场景下的公平使用与预算控制。
- **流式场景支持**: `streaming_requests_total` 与 `streaming_chunks_total`
  专门覆盖实时交互场景的吞吐量观测。
- **安全可观测深化**: 安全检测不仅统计通过/拦截，
  还按违规类别（violence、hate 等）拆解并记录误报，
  支撑安全策略的持续优化与 A/B 测试。
- **Agent 专属填补空白**: Agent 工作流状态、步骤数、步骤耗时、工具调用成功率、
  内存操作延迟等指标在当前开源可观测工具链中极为稀缺。
- **持续评估在线化**: Evaluation API 指标将离线评估脚本转化为可实时监控的生产指标，
  支撑模型迭代的快速反馈闭环。
- **现状状态**: 提案已被关闭（not planned），
  但指标框架本身具备高度通用性，
  可被 Llama Stack 之外的其他项目直接借鉴或移植。
- **标签基数风险**: model_id + provider 等高基数标签的组合
  可能导致 Prometheus 时间序列爆炸，
  生产部署需配合 recording rules 或聚合策略使用。
- **工程参考价值**: 即使未合并，该 Issue 仍是开源社区中
  最系统的 GenAI 平台指标设计文档之一。

## 与综述的关联

本材料与综述中 "Agent 可观测性与遥测" 主题高度相关。
综述在讨论 Agent 执行轨迹追踪时指出，
当前开源 Agent 框架普遍缺乏标准化的运行时指标暴露机制，
大多数工具仅通过 callback 或 hook 机制输出日志，
难以转化为结构化的时序数据。
Llama Stack 作为 Meta 主导的 Agent 构建平台，
其遥测提案恰好回应了这一痛点——
特别是 Agent 工作流、工具调用、内存操作等 Agent 专属指标的设计，
为 "轨迹可观测性" 提供了量化维度，
使得 Agent 的健康度评估从定性描述升级为定量仪表盘。

此外，提案中 Inference API 的 TTFT、TPS、流式指标
与综述中 "大模型服务性能评估" 章节形成直接呼应。
学术文献通常关注模型层面的准确率与鲁棒性，
而工程实践更关心服务层面的延迟分布与吞吐量。
本提案的指标设计恰好架起了这座桥梁：
通过 Prometheus 的分位数直方图，
将学术上的 "生成速度" 概念转化为运维人员可直接配置告警的 SLA 指标。

Vector I/O 的检索延迟与质量指标
则直接支撑综述对 RAG 检索可观测性的讨论。
当前综述引用的学术文献（如 AIOpsLab、MASPrism）
更多关注 RAG 的端到端准确性评估，
而本提案提供的 `vector_query_duration_seconds`、
`vector_chunks_processed_total` 等指标
则从系统性能角度补充了 RAG 检索的可观测维度。
二者结合，可形成 "效果评估 + 性能监控" 的完整 RAG 可观测性视图。

Safety API 的违规分类统计
也为综述中 "Agent 安全护栏" 部分提供了可量化的监控抓手。
综述在讨论安全机制时往往聚焦于检测算法本身
（如 Llama Guard、ShieldGemma），
而本提案的指标设计则提醒读者：
安全系统的运营同样需要度量——
误报率、检测延迟、按类别的违规分布，
都是安全策略迭代不可或缺的反馈信号。

若将本提案与 s1-010（AWS CloudWatch GenAI Observability）对比，
可发现两者在指标维度上高度一致：token、延迟、成本、错误、质量。
区别在于 AWS 提供托管式开箱即用的仪表盘与自动埋点能力，
而本提案偏向开源框架层面的底层指标定义。
综述可将二者结合，论证一个正在发生的产业趋势：
无论云厂商还是开源社区，GenAI 可观测性的指标语义正在快速收敛，
但真正的差距在于 "从定义到落地" 的自动化程度与生态整合深度。
AWS 通过 ADOT 和 CloudWatch 大幅降低了埋点成本，
而开源方案（如 Llama Stack）仍需开发者手动 instrument 或等待社区贡献。

此外，本提案与综述中引用的 OpenInference 规范（c-014、c-015）
也存在潜在关联。
OpenInference 定义了 LLM 应用的语义约定（semantic conventions），
本提案中的指标命名与标签设计若能与 OpenInference 对齐，
将极大提升跨平台可观测数据的互操作性。
综述可在讨论标准化进展时，
将本提案作为 "社区自发收敛" 的典型案例。

## 我的笔记

这份 GitHub Issue 虽被标记为 "Closed as not planned"，
但其系统性的指标框架令人印象深刻，
甚至可以说是一份被低估的 "GenAI 平台可观测性指标设计指南"。
它几乎覆盖了 LLM 服务平台运营所需的全部关键维度，
且严格遵循 Prometheus 最佳实践。
在实际项目中，如果我要为一个内部 Agent 平台搭建可观测体系，
会直接将此提案作为 checklist，
逐项评估是否需要实施，
并标注优先级（P0 为必需，P1 为建议，P2 为可选）。

有几个设计细节值得深入思考。
首先是标签粒度的权衡问题：
提案为 token 指标同时增加了 model_id 和 provider 两个高基数标签。
在 Prometheus 生态中，
高基数标签（high cardinality labels）
是导致时间序列爆炸（cardinality explosion）的首要原因。
如果平台同时对接 10 个 provider、每个 provider 提供 50 个模型，
则仅 token 指标就会产生 500 条时间序列，
再乘以 user_id、quantile 等维度，
规模可能迅速失控。
在生产环境中，需要评估是否真的需要同时保留两个高基数维度，
或者通过 recording rules 预先聚合部分视图，
抑或采用 VictoriaMetrics、Thanos 等支持更高基数的存储后端。

其次是 Safety API 的误报指标
（`llama_stack_safety_false_positives_total`）。
这在同类框架的可观测性设计中非常少见，
体现了提案者对安全系统持续运营的独特理解——
拦截率（block rate）本身不足以评估安全策略的优劣，
误报对用户体验的损害同样需要量化。
这一思路与综述中 "安全护栏" 章节的讨论高度契合，
建议在综述中专门引用此指标
作为 "安全可观测性不应止于拦截统计" 的证据。

另一个启发是 Agent 专属指标的设计。
当前主流可观测平台（如 LangSmith、Phoenix、Arize）
更关注单次 LLM 调用的 trace 与 span，
而对多步骤 Agent 工作流的宏观指标
（完成率、步骤数分布、工具调用模式、内存操作延迟）
缺乏原生支持。
提案中的 `llama_stack_agent_workflows_total`、
`llama_stack_agent_steps_total`、
`llama_stack_agent_step_duration_seconds` 等指标
恰好填补了这一空白，
可作为 Agent 健康度仪表盘的核心 KPI。
例如，若 `agent_steps_total` 的 P99 持续上升，
可能意味着 Agent 陷入了循环调用或推理链过度延伸；
若 `agent_tool_calls_total` 的成功率下降，
则可能指向某个外部 API 的稳定性问题。

Evaluation API 指标的设计也给我留下了深刻印象。
大多数团队将模型评估视为离线脚本（如 nightly CI），
而提案将其转化为在线可观测指标
（`evaluation_tasks_total`、`evaluation_success_rate`、
`evaluation_scores_distribution`）。
这意味着模型版本迭代的效果可以被实时追踪，
而非等待次日报告。
这种 "持续评估在线化" 的思路
对于追求快速迭代的产品团队极具吸引力。

从综述写作角度，
这份材料的价值在于它提供了一个 "理想态" 的指标清单。
即使 Llama Stack 本身未实施，
其他框架（如 LangChain、AutoGen、AG2、CrewAI）的设计者也可以参考。
建议在综述中引用此提案
作为 "开源社区对 GenAI 可观测性指标维度的共识性需求" 的证据，
与学术文献中的评估维度
（如 AIOpsLab 的操作维度、MASPrism 的失败归因维度）
进行交叉对比，
从而论证学术界与工业界在可观测性需求上的趋同。

最后，该 Issue 的关闭状态也反映了一个值得记录的现实：
开源项目资源有限，可观测性增强往往优先级低于核心功能。
综述在讨论 "Agent 可观测性的落地障碍" 时，
可将此作为典型案例——
即使社区已产出成熟的设计方案，
工程实现仍受项目优先级与维护者精力的制约。
这也从侧面解释了为何当前 Agent 可观测性生态呈现碎片化格局：
需求明确，但落地力量分散。
