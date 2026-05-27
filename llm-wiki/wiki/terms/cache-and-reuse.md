# 缓存与复用

## 定义

缓存与复用通过 prompt cache、语义缓存、工具结果缓存、检索结果复用和中间产物复用降低重复 token 与外部调用成本，但需要处理失效、隐私和一致性问题。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 哪些输入和工具结果可以安全复用？
- 缓存命中率如何进入 trace 与成本归因？
- 缓存错误会如何放大为任务失败或合规风险？

## 证据入口

- [Helicone LLM 可观测性平台深度评测：一键集成与智能成本优化](summaries/s2-022-Helicone-LLM-Observability-Platform-Lea.md) — Helicone 的评测让我对"Proxy 模式 versus SDK 插桩模式"的架构之争 有了更具体、更工程化的理解。
- [LLM Agent Cost Attribution: Complete Production 2026 Guide](summaries/s3-014-LLM-Agent-Cost-Attribution-Complete-Prod.md) — 这篇指南的价值在于它将成本归因从一个财务部门的报表需求，重新定义为工程团队的基础设施责任。
- [A Guide to AI Agent Cost Optimization With Observability](summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi.md) — 这篇指南的最大价值在于它将「可观测性」从「事后排查工具」重新定位为「成本工程的基础设施」。
- [Helicone：开源 LLM 可观测性与 AI 网关一体化平台](summaries/s2-023-Helicone-Open-source-LLM-observability-f.md) — Helicone 的产品档案让我对"AI Gateway + Observability"的融合趋势有了更清晰的认知。
- [Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering Agents](summaries/p-005-Debugging-the-Debuggers-Failure-Anchored.md) — 本文围绕软件工程智能体的失败后恢复提出三个核心挑战： - **挑战一：保留恢复关键证据**。有效的恢复不仅依赖最终错误信息，还需要保留异常签名、重复工具失败、执行顺序、智能体与环境状态及评估器反馈。现有基准大多仅关注任务目标是否达成，未保留支持恢复的细粒度诊断信号。当遥测被压缩为通用摘要或未分类日志时，这些关键证据极易丢失。
- [AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices](summaries/c-018-AI-Agents-in-Production-Monitoring-Guard.md) — 这篇博客的最大价值在于其极强的可操作性。与多数学术论文聚焦评估指标与算法改进不同，本文给出了大量可直接运行或稍加修改即可部署的 Python 代码片段，从 Streamlit UI 到 FastAPI 端点，从 Langfuse CallbackHandler 到熔断器类实现，工程师可以按图索骥在数小时内搭建最小可行生产系统。这种「从零到一」的指导意义，使其在综述的工程实践章节中占据了独特位置。
- [Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks](summaries/p-024-Lifting-Traces-to-Logic-Programmatic-Ski.md) — 当前 LLM 驱动的智能体虽然具备感知、推理与行动能力，但在特定真实世界领域往往缺乏 grounding 知识，导致领域特定的推理缺口，表现为工具使用不可靠与长程规划失败。为弥合通用能力与任务需求之间的鸿沟，智能体需要通过环境交互进行自我演进。
- [Process-Centric Analysis of Agentic Software Systems](summaries/c-009-Process-Centric-Analysis-of-Agentic-Soft.md) — Graphectory 的核心价值在于将"轨迹"从线性序列提升为语义图， 这一视角转变对智能体评估具有方法论层面的重要意义。
- [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](summaries/p-012-A-Unified-Review-of-Memory-Skills-Protoc.md) — 本文采用**概念综述与系统框架构建**的研究方法，核心方法论特点如下： - **理论锚定**：以 Norman 的认知人工制品理论和 Kirsh 的互补策略理论为分析基石，将工程设计选择与认知科学中的外部化概念对接。
- [Operating agentic AI with Amazon Bedrock AgentCore and Datadog LLM Observability: Lessons from NTT DATA](summaries/s1-009-Operating-agentic-AI-with-Amazon-Bedrock.md) — 这篇案例的核心价值在于它并非产品宣传文档，而是来自 NTT DATA 这一大型系统集成商在真实客户场景中的验证经验。作者身份（SRE 工程师）决定了文章视角偏向运维可靠性与工程实践，而非算法创新或模型优化，这与综述关注"agentic AI 如何落地"的基调高度一致。系统集成商的视角尤为珍贵，因为他们需要同时理解平台技术能力、客户业务需求和运维现实约束，这种"三角视角"是单一厂商案例或学术研究难以提供的。在综述写作中，应当充分利用这种来自一线运维人员的声音，以平衡技术理想与工程现实之间的张力。

## 相关词条

- [智能体轨迹](terms/agent-trace.md)
