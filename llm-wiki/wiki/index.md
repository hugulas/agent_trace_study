# Index — Agentic Trace Insight

> A compiled wiki for agent trace observability, auditability, failure diagnosis, production operations, and cost visibility.

## Navigation
- [#Knowledge Layers](#knowledge-layers) · [#Concepts](#concepts) · [#Entities](#entities) · [#Summaries](#summaries) · [#Open Questions](#open-questions)

## Knowledge Layers
- [词条：智能体轨迹](terms/agent-trace.md) · [失败归因](terms/failure-attribution.md) · [过程合规性](terms/process-compliance.md) · [轨迹 Schema](terms/trace-schema.md) · [Harness](terms/harness.md)
- [观点：可观测性不是日志收集](viewpoints/observability-is-not-logging.md) · [观点：最终奖励不足以评估智能体](viewpoints/final-reward-is-insufficient.md) · [观点：Schema 决定产品边界](viewpoints/schema-is-the-product-boundary.md)
- [对比：诊断/合规/日志](comparisons/diagnosis-vs-compliance-vs-logging.md) · [对比：OTel 与 Agent Schema](comparisons/otel-vs-agent-specific-schema.md) · [对比：产品工具地图](comparisons/observability-product-map.md)

## Concepts
### Engineering
- [Failure Diagnosis and Attribution](concepts/failure-diagnosis-and-attribution.md) — Collects work on localizing failures across agent steps, tools, dependencies, multi-agent coordination, and harnesses. (72 linked notes)
- [Runtime Instrumentation and OpenTelemetry](concepts/runtime-instrumentation-and-otel.md) — Covers implementation patterns for instrumenting agents, MCP servers, tool calls, model calls, and distributed workflows. (97 linked notes)

### Evaluation
- [Evaluation and Benchmarking](concepts/evaluation-and-benchmarking.md) — Organizes benchmark, white-box evaluation, monitorability, alignment auditing, and long-horizon task evaluation notes. (87 linked notes)

### Foundations
- [Agent Observability Landscape](concepts/agent-observability-landscape.md) — Frames agent observability as traces, evaluations, governance, and production operations rather than ordinary LLM logging. (102 linked notes)
- [Trace Schema and Telemetry Standards](concepts/trace-schema-and-telemetry-standards.md) — Compares structured agent trace schemas, OpenTelemetry alignment, OpenInference, Hermes-style trajectories, and audit-trail formats. (77 linked notes)

### Governance
- [Audit Trails, Security, and Governance](concepts/audit-trails-security-and-governance.md) — Synthesizes tamper-evident audit trails, guardrails, safety violations, agent vulnerabilities, and governance evidence. (45 linked notes)

### Operations
- [Cost, Token, and Resource Attribution](concepts/cost-token-and-resource-attribution.md) — Treats cost visibility as part of observability: token economics, invoice prediction, resource attribution, and optimization. (115 linked notes)
- [Observability Products and Market Map](concepts/observability-products-and-market-map.md) — Maps product-level agent observability tools such as LangSmith, Langfuse, Arize Phoenix, Braintrust, AgentOps, Datadog, Elastic, New Relic, Splunk, Helicone, and Opik. (74 linked notes)
- [Production Operations and Cloud Platforms](concepts/production-operations-and-cloud-platforms.md) — Tracks AWS, Google, Alibaba, Baidu, and enterprise deployment guidance for operating agentic systems. (66 linked notes)

### Systems
- [Agent Frameworks and Coding Agents](concepts/agent-frameworks-and-coding-agents.md) — Connects traces and observability to concrete agent frameworks, coding agents, Claude Code, Codex, Swarm, AgentRx, and workflow systems. (67 linked notes)

## Entities
- [AWS AgentCore](entities/AWS-AgentCore.md) — recurring entity in 20 source notes)
- [AgentOps](entities/AgentOps.md) — recurring entity in 10 source notes)
- [AgentTrace](entities/AgentTrace.md) — recurring entity in 19 source notes)
- [Arize Phoenix](entities/Arize-Phoenix.md) — recurring entity in 26 source notes)
- [Braintrust](entities/Braintrust.md) — recurring entity in 9 source notes)
- [Claude Code](entities/Claude-Code.md) — recurring entity in 19 source notes)
- [Codex CLI](entities/Codex-CLI.md) — recurring entity in 13 source notes)
- [Google ADK and Vertex AI](entities/Google-ADK-and-Vertex-AI.md) — recurring entity in 15 source notes)
- [Helicone](entities/Helicone.md) — recurring entity in 12 source notes)
- [Hermes Agent Trajectory Format](entities/Hermes-Agent-Trajectory-Format.md) — recurring entity in 2 source notes)
- [LangSmith](entities/LangSmith.md) — recurring entity in 24 source notes)
- [Langfuse](entities/Langfuse.md) — recurring entity in 27 source notes)
- [OpenInference](entities/OpenInference.md) — recurring entity in 17 source notes)
- [OpenTelemetry](entities/OpenTelemetry.md) — recurring entity in 66 source notes)

## Summaries
- [Willful Disobedience: Automatically Detecting Failures in Agentic Traces](summaries/AgentPex-Willful-Disobedience.md) — evidence quality: medium（bundle 中 method/mechanism 部分提取不完整）
- [Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems](summaries/Dive-Into-Claude-Code.md) — evidence quality: medium（bundle 中大量方法机制内容提取失败，此处结合 PDF 直接阅读补充）
- [GitHub — microsoft/AgentRx](summaries/a-002-GitHub-microsoftAgentRx.md) — evidence quality: high（官方发布，可直接运行复现）
- [Systematic debugging for AI agents: Introducing the AgentRx framework](summaries/a-003-Systematic-debugging-for-AI-agents-Intro.md) — evidence quality: unknown
- [Monitoring - Claude Code Docs](summaries/a-007-Monitoring-Claude-Code-Docs.md) — evidence quality: high
- [How we built our multi-agent research system — Anthropic Engineering Blog](summaries/a-009-How-we-built-our-multi-agent-research-sy.md) — evidence quality: high
- [Opik Claude Code Plugin: Auto-Configure Agent Observability](summaries/a-010-Announcing-the-Opik-Claude-Code-Plugin.md) — evidence quality: medium
- [Advanced Configuration — Codex (Observability and telemetry)](summaries/a-013-Advanced-Configuration-Codex-Observabil.md) — evidence quality: high（官方一手文档，直接描述产品能力）
- [Building Consistent Workflows with Codex CLI & Agents SDK](summaries/a-014-Building-Consistent-Workflows-with-Codex.md) — evidence quality: unknown
- [Reverse engineering Codex CLI rollout traces - DEV Community](summaries/a-015-Reverse-engineering-Codex-CLI-rollout-tr.md) — evidence quality: high
- [GitHub — openai/swarm: Educational framework exploring ergonomic, lightweight multi-agent orchestration](summaries/a-019-GitHub-openaiswarm.md) — evidence quality: medium
- [Multi-Agent Portfolio Collaboration with OpenAI Agents SDK](summaries/a-020-Multi-Agent-Portfolio-Collaboration-with.md) — evidence quality: high
- [AI agent observability: tracing, debugging, and monitoring multi-agent systems](summaries/a-021-AI-agent-observability-tracing-debugging.md) — evidence quality: unknown
- [Agent Contracts: A Formal Framework for Resource-Bounded Autonomous AI Systems](summaries/agentcontracts-note.md) — evidence quality: unknown
- [AgentDropout 深度阅读笔记](summaries/agentdropout-note.md) — evidence quality: unknown
- [AgentPrune：面向大语言模型多智能体系统的经济通信管道](summaries/agentprune-note.md) — evidence quality: unknown
- [AgentTrace: A Structured Logging Framework for Agent System Observability](summaries/agenttracecausal-note.md) — evidence quality: unknown
- [BAMAS: Structuring Budget-Aware Multi-Agent Systems](summaries/bamas-note.md) — evidence quality: unknown
- [Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents](summaries/bavt-note.md) — evidence quality: unknown
- [BEAVER: A Training-Free Hierarchical Prompt Compression Method via Structure-Aware Page Selection](summaries/beaver-note.md) — evidence quality: unknown
- [BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens](summaries/budgetthinker-note.md) — evidence quality: unknown
- [AI Agent Observability: Tracing, Debugging, and the OpenTelemetry Standard](summaries/c-001-AI-Agent-Observability-Tracing-Debugging.md) — evidence quality: medium
- [Observability for Agentic Systems: What to Log, How to Redact, How to Debug](summaries/c-002-Observability-for-Agentic-Systems-What-t.md) — evidence quality: medium
- [AI Agent Observability - Evolving Standards and Best Practices - OpenTelemetry](summaries/c-003-OpenTelemetry-AI-Agent-Observability-Sta.md) — evidence quality: low
- [GitHub - Arize-ai/openinference: OpenTelemetry Instrumentation for AI Observability](summaries/c-004-OpenInference-OpenTelemetry-Instrumentat.md) — evidence quality: medium
- [LangSmith: AI Agent & LLM Observability Platform](summaries/c-005-LangSmith-AI-Agent-LLM-Observability-Pl.md) — evidence quality: medium
- [MASPrism: Lightweight Failure Attribution for Multi-Agent Systems Using Prefill-Stage Signals](summaries/c-006-MASPrism-Lightweight-Failure-Attribution.md) — evidence quality: medium
- [The Reliability Gap: Agent Benchmarks for Enterprise](summaries/c-007-The-Reliability-Gap-Agent-Benchmarks-for.md) — evidence quality: unknown
- [AI-NativeBench: An Open-Source White-Box Agentic Benchmark Suite for AI-Native Systems](summaries/c-008-AI-NativeBench-An-Open-Source-White-Box.md) — evidence quality: high
- [Process-Centric Analysis of Agentic Software Systems](summaries/c-009-Process-Centric-Analysis-of-Agentic-Soft.md) — evidence quality: medium
- [GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis](summaries/c-010-GUIDE-Interpretable-GUI-Agent-Evaluation.md) — evidence quality: medium
- [AgentTrace: A Structured Logging Framework for Agent System Observability](summaries/c-011-AgentTrace-A-Structured-Logging-Framewor.md) — evidence quality: medium
- [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](summaries/c-012-Agent-Audit-Trail-A-Standard-Logging-For.md) — evidence quality: unknown
- [Trajectory Format - Hermes Agent](summaries/c-013-Hermes-Agent-Trajectory-Format.md) — evidence quality: high
- [OpenInference Specification - openinference](summaries/c-014-OpenInference-Specification.md) — evidence quality: high（作为社区事实标准的技术规范文档）
- [What is OpenInference? OTel for LLM 2026](summaries/c-015-OpenInference-OpenTelemetry-for-LLM-Apps.md) — evidence quality: medium（作为生态概述和对比分析，时效性强，但带有 FutureAGI 自身产品视角）
- [AgentVerify: Compositional Formal Verification of AI Agent Safety Properties via LTL Model Checking](summaries/c-016-AgentVerify-Compositional-Formal-Verific.md) — evidence quality: medium
- [Essential Framework for AI Agent Guardrails](summaries/c-017-Essential-Framework-for-AI-Agent-Guardra.md) — evidence quality: unknown
- [AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices](summaries/c-018-AI-Agents-in-Production-Monitoring-Guard.md) — evidence quality: unknown
- [AI Agent Vulnerabilities: Understanding and Mitigating Emerging Security Risks](summaries/c-019-AI-Agent-Vulnerabilities-Understanding-S.md) — evidence quality: unknown
- [What Is AI Agent Monitoring? Key Metrics & Techniques](summaries/c-020-What-Is-AI-Agent-Monitoring-Key-Metrics.md) — evidence quality: medium
- [C3PO：概率成本约束下的LLM级联优化](summaries/c3po-note.md) — evidence quality: unknown
- [claude-devtools: Open-Source DevTools for Claude Code](summaries/claudedevtools-note.md) — evidence quality: unknown
- [What Is AI Agent Observability? Why Cost Is What You're Missing](summaries/cloudzerocost-note.md) — evidence quality: unknown
- [CoMem 深度阅读笔记](summaries/comem-note.md) — evidence quality: unknown
- [CompactPrompt 深度阅读笔记](summaries/compactprompt-note.md) — evidence quality: unknown
- [LLM Agent Cost Attribution: Complete Production 2026 Guide](summaries/costattribution-note.md) — evidence quality: unknown
- [Best LLM Cost Tracking Tools in 2026 深度阅读笔记](summaries/costtools2026-note.md) — evidence quality: unknown
- [AI Cost Visibility 深度阅读笔记](summaries/costvisibility-note.md) — evidence quality: unknown
- [Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning](summaries/cotprune-note.md) — evidence quality: unknown
- [ContextBudget: Budget-Aware Context Management for Long-Horizon Search Agents](summaries/ctxbudget-note.md) — evidence quality: unknown
- [Towards Efficient Large Language Reasoning Models via Extreme-Ratio Chain-of-Thought Compression](summaries/extcot-note.md) — evidence quality: unknown
- [FeatureBench: Benchmarking Agentic Coding for Complex Feature Development](summaries/featurebench-note.md) — evidence quality: unknown
- [A Guide to AI Agent Cost Optimization With Observability — 深度阅读笔记](summaries/galileocost-note.md) — evidence quality: unknown
- [Scaling Graph Chain-of-Thought Reasoning: A Multi-Agent Framework with Efficient LLM Serving](summaries/graphcot-note.md) — evidence quality: unknown
- [HybridFlow: Resource-Adaptive Subtask Routing for Efficient Edge-Cloud LLM Inference](summaries/hybridflow-note.md) — evidence quality: unknown
- [KVCOMM 深度阅读笔记](summaries/kvcomm-note.md) — evidence quality: unknown
- [llm-d KV 缓存感知路由深度笔记](summaries/llmd-note.md) — evidence quality: unknown
- [MAS-Bench: A Unified Benchmark for Shortcut-Augmented Hybrid Mobile GUI Agents](summaries/masbench-note.md) — evidence quality: unknown
- [MasRouter: 面向多智能体系统的大语言模型路由学习](summaries/masrouter-note.md) — evidence quality: unknown
- [AgentRx: Diagnosing AI Agent Failures from Execution Trajectories](summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories.md) — evidence quality: unknown
- [AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds](summaries/p-002-AIOpsLab-A-Holistic-Framework-to-Evaluat.md) — evidence quality: unknown
- [DoVer: Intervention-Driven Auto Debugging for LLM Multi-Agent Systems](summaries/p-003-DoVer-Intervention-Driven-Auto-Debugging.md) — evidence quality: unknown
- [Willful Disobedience: Automatically Detecting Failures in Agentic Traces](summaries/p-004-Willful-Disobedience-Automatically-Detecting-Failures-in-Agentic-Traces.md) — evidence quality: unknown
- [Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering Agents](summaries/p-005-Debugging-the-Debuggers-Failure-Anchored.md) — evidence quality: high
- [Monitoring Monitorability](summaries/p-006-Monitoring-Monitorability.md) — evidence quality: medium
- [评估思维链的可监控性](summaries/p-007-Evaluating-Chain-of-Thought-Monitorabili.md) — evidence quality: unknown
- [Building and evaluating alignment auditing agents](summaries/p-008-Building-and-Evaluating-Alignment-Auditi.md) — evidence quality: medium
- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](summaries/p-009-Beyond-the-Black-Box-Interpretability-of.md) — evidence quality: high
- [Continual Harness: Online Adaptation for Self-Improving Foundation Agents](summaries/p-010-Online-Adaptation-for-Self-Improving-Fou.md) — evidence quality: high
- [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](summaries/p-011-Agentic-Harness-Engineering-Observabilit.md) — evidence quality: unknown
- [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](summaries/p-012-A-Unified-Review-of-Memory-Skills-Protoc.md) — evidence quality: unknown
- [Detecting Safety Violations Across Many Agent Traces](summaries/p-013-Detecting-Safety-Violations-Across-Many.md) — evidence quality: high
- [AgentTrace: A Structured Logging Framework for Agent System Observability](summaries/p-014-AgentTrace-A-Structured-Logging-Framewor.md) — evidence quality: unknown
- [View-oriented Conversation Compiler for Agent Trace Analysis](summaries/p-015-View-oriented-Conversation-Compiler-for.md) — evidence quality: high
- [The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break](summaries/p-016-The-Long-Horizon-Task-Mirage-Diagnosing.md) — evidence quality: medium
- [Auditing Agent Harness Safety](summaries/p-017-Auditing-Agent-Harness-Safety.md) — evidence quality: high
- [EAGER: Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation](summaries/p-018-EAGER-Efficient-Failure-Management-for-M.md) — evidence quality: unknown
- [OpsAgent: An Evolving Multi-agent System for Incident Management in Microservices](summaries/p-019-OpsAgent-An-Evolving-Multi-Agent-System.md) — evidence quality: high
- [Can Dependencies Induced by LLM-Agent Workflows Be Trusted?](summaries/p-020-Can-Dependencies-Induced-by-LLM-Agent-Wo.md) — evidence quality: unknown
- [Why Do Multi-Agent LLM Systems Fail?](summaries/p-021-Why-Do-Multi-Agent-LLM-Systems-Fail.md) — evidence quality: high
- [Why Do Multi-Agent LLM Systems Fail?](summaries/p-021-Why-Do-Multi-Agent-LLM-Systems-Fail-2.md) — evidence quality: high
- [Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems](summaries/p-022-Which-Agent-Causes-Task-Failures-and-Whe.md) — evidence quality: high
- [EvoCF: Multi-Agent Collaboration via Agentic Memory-Driven Evolutionary Counterfactual Planning](summaries/p-023-EvoCF-Multi-Agent-Collaboration-via-Agen.md) — evidence quality: unknown
- [Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks](summaries/p-024-Lifting-Traces-to-Logic-Programmatic-Ski.md) — evidence quality: high
- [AgentSight: System-Level Observability for AI Agents Using eBPF](summaries/p-025-AgentSight-System-Level-Observability-fo.md) — evidence quality: unknown
- [AgentPro: Enhancing LLM Agents with Automated Process Supervision](summaries/p-026-AgentPro-Enhancing-LLM-Agents-with-Autom.md) — evidence quality: unknown
- [Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models](summaries/p-027-Do-Code-Semantics-Help-A-Comprehensive-S.md) — evidence quality: unknown
- [FLARE: Faithful Logic-Aided Reasoning and Exploration](summaries/p-028-FLARE-Faithful-Logic-Aided-Reasoning-and.md) — evidence quality: unknown
- [AgentDiagnose: An Open Toolkit for Diagnosing LLM Agent Trajectories](summaries/p-029-AgentDiagnose-An-Open-Toolkit-for-Diagno.md) — evidence quality: unknown
- [Teaching Text Agents to Learn Sequential Decision Making from Failure](summaries/p-030-Teaching-Text-Agents-to-Learn-Sequential.md) — evidence quality: unknown
- [价格反转现象：更便宜的推理模型反而成本更高](summaries/pricereversal-note.md) — evidence quality: unknown
- [Retrieval-Conditioned Topology Selection with Provable Budget Conservation for Multi-Agent Code Generation](summaries/retrievaltopo-note.md) — evidence quality: unknown
- [Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey](summaries/routesurvey-note.md) — evidence quality: unknown
- [Google Cloud Trace observability for ADK](summaries/s1-001-Google-Cloud-Trace-observability-for-ADK.md) — evidence quality: unknown
- [Google boosts Vertex AI Agent Builder with new observability and deployment tools](summaries/s1-002-Google-boosts-Vertex-AI-Agent-Builder-wi.md) — evidence quality: unknown
- [bq-agent-app：基于 Google ADK 与 BigQuery 的多智能体数据分析系统](summaries/s1-003-bq-agent-app-Observability-with-Agent-En.md) — evidence quality: medium（开源代码仓库，README 与配置文档详尽，但未经同行评审）
- [Google ADK vs AWS AgentCore: Enterprise Framework Selection Guide](summaries/s1-004-Google-ADK-vs-AWS-AgentCore-Enterprise-F.md) — evidence quality: unknown
- [Getting Started with AI Agent Observability using Vertex AI Agent Engine and Cloud Trace](summaries/s1-005-Getting-Started-with-AI-Agent-Observabil.md) — evidence quality: high（官方学习平台发布的结构化实验，提供真实预配环境与逐步验证）
- [Amazon CloudWatch Generative AI Observability Samples](summaries/s1-006-Amazon-CloudWatch-generative-AI-observab.md) — evidence quality: high（官方发布，覆盖多种部署场景）
- [Amazon Bedrock AgentCore Production Operations Guide - Observability, Cost Optimization, and Disaster Recovery](summaries/s1-007-Amazon-Bedrock-AgentCore-Production-Oper.md) — evidence quality: low
- [Amazon Bedrock AgentCore Runtime - Part 3 AgentCore Runtime Observability](summaries/s1-008-Part-3-AgentCore-Runtime-Observability.md) — evidence quality: high（AWS Hero 撰写的官方生态实践指南，包含大量控制台截图与配置步骤）
- [Operating agentic AI with Amazon Bedrock AgentCore and Datadog LLM Observability: Lessons from NTT DATA](summaries/s1-009-Operating-agentic-AI-with-Amazon-Bedrock.md) — evidence quality: unknown
- [GenAIOps on AWS: 端到端可观测性栈](summaries/s1-010-GenAIOps-on-AWS-End-to-End-Observability.md) — evidence quality: high
- [使用 Python 与 Llama Stack 实现可观测性](summaries/s1-011-How-to-implement-observability-with-Pyth.md) — evidence quality: medium（来自 Red Hat 官方开发者博客，作者为开源社区核心领袖，工程实践详实，但非经同行评审的学术论文）
- [使用 Node.js 与 Llama Stack 实现可观测性](summaries/s1-012-How-to-implement-observability-with-Node.md) — evidence quality: medium（来自 Red Hat 官方开发者博客，作者为 Node.js 社区核心领袖，工程实践详实，但非经同行评审的学术论文）
- [Oracle OCI 企业级生成式 AI 应用加速方案（来源已失效）](summaries/s1-013-Accelerating-Enterprise-Gen-AI-applicati.md) — evidence quality: very-low（内容不可读，仅存错误页面信息）
- [Llama Stack 遥测可观测性指标增强提案](summaries/s1-014-Observability-Add-Additional-Metrics-to.md) — evidence quality: medium
- [Llama Stack Tutorial](summaries/s1-015-Llama-Stack-Tutorial.md) — evidence quality: medium（官方教程，实践导向，内容覆盖较广但深度有限）
- [阿里云 AgentLoop — AI 应用全生命周期可观测与数据飞轮平台](summaries/s2-001-什么是AgentLoop-云监控CMS-阿里云文档.md) — evidence quality: unknown
- [阿里云百炼应用观测 — 大模型应用端到端可观测实践](summaries/s2-002-应用观测-大模型服务平台百炼Model-Studio-阿里云文档.md) — evidence quality: unknown
- [千帆AppBuilder Trace跟踪功能基本用法](summaries/s2-003-Appbuilder-Trace跟踪功能基本用法-百度千帆文档.md) — evidence quality: unknown
- [Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践](summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践.md) — evidence quality: unknown
- [目前主流的智能体可观测性和智能体评测相关的产品调研](summaries/s2-005-目前主流的智能体可观测性和智能体评测相关的产品调研-Coze-Loop详细介绍.md) — evidence quality: unknown
- [使用 Datadog LLM Observability 监控、排查与优化 AI Agent](summaries/s2-006-Monitor-troubleshoot-and-improve-AI-agen.md) — evidence quality: medium-high（基于官方产品文档，包含具体技术方案和可视化设计说明）
- [Datadog LLM Observability 产品页面深度解读](summaries/s2-007-Datadog-LLM-Observability-Product-Page.md) — evidence quality: 中（作为产品功能描述具有参考价值，但缺乏第三方独立验证或技术白皮书级别的细节披露）
- [Splunk 推出 AI Agent Monitoring，为企业级 Agent 应用提供全栈可观测性](summaries/s2-008-Monitor-LLM-and-agent-performance-with-A.md) — evidence quality: medium（基于官方产品发布声明，包含具体功能描述和技术架构信息）
- [Splunk AI Agent Monitoring：企业级 AI 代理可观测性官方文档](summaries/s2-009-Introduction-to-Splunk-AI-Agent-Monitori.md) — evidence quality: unknown
- [Elastic LLM与Agentic AI可观测性技术文档](summaries/s2-010-LLM-and-agentic-AI-observability-Elasti.md) — evidence quality: unknown
- [Elastic Brings Observability to AI Agents with Amazon Bedrock AgentCore](summaries/s2-011-Elastic-Brings-Observability-to-AI-Agent.md) — evidence quality: low
- [Beyond the Black Box: Next-Gen AI Agent Monitoring](summaries/s2-012-Beyond-the-Black-Box-Next-Gen-AI-Agent-M.md) — evidence quality: unknown
- [Introduction to AI monitoring - New Relic Documentation](summaries/s2-013-Introduction-to-AI-monitoring-New-Relic.md) — evidence quality: high
- [Langfuse: 开源 LLM 工程平台](summaries/s2-014-langfuselangfuse-GitHub.md) — evidence quality: high
- [Langfuse 完成 5000 万美元 B 轮融资：AI Agent 可观测性迎来产业级拐点](summaries/s2-015-AI-Agent-Observability-Platform-Langfuse.md) — evidence quality: unknown
- [Arize-ai/phoenix: AI Observability & Evaluation](summaries/s2-016-Arize-aiphoenix-GitHub.md) — evidence quality: medium
- [Arize AI Review 2026: AI Observability & LLM Evaluation](summaries/s2-017-Arize-AI-Review-2026-AI-Observability-L.md) — evidence quality: medium
- [What Is Braintrust? Is It the Best for AI Observability?](summaries/s2-018-What-Is-Braintrust-Is-It-the-Best-for-AI.md) — evidence quality: medium
- [Braintrust 完成 8000 万美元 B 轮融资，加速 AI 可观测性平台建设](summaries/s2-019-Braintrust-Raises-80M-Series-B-for-AI-Ob.md) — evidence quality: medium（基于官方融资公告及多个标杆客户证言）
- [AgentOps - AI Agent Monitoring and Observability 评测深度解读](summaries/s2-020-AgentOps-AI-Agent-Monitoring-and-Obser.md) — evidence quality: 中（第三方评测具有一定独立性，但内容深度受限于聚合平台的信息来源，缺乏原始用户访谈或量化基准测试）
- [AgentOps AI Infrastructure Platform Market Research Report 2034](summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark.md) — evidence quality: unknown
- [Helicone LLM 可观测性平台深度评测：一键集成与智能成本优化](summaries/s2-022-Helicone-LLM-Observability-Platform-Lea.md) — evidence quality: unknown
- [Helicone：开源 LLM 可观测性与 AI 网关一体化平台](summaries/s2-023-Helicone-Open-source-LLM-observability-f.md) — evidence quality: unknown
- [Mind the Metrics: Patterns for Telemetry-Aware In-IDE AI Application Development using Model Context Protocol (MCP)](summaries/s3-001-Mind-the-Metrics-Patterns-for-Telemetry.md) — evidence quality: medium
- [Distributed tracing for agentic workflows with OpenTelemetry](summaries/s3-002-Distributed-tracing-for-agentic-workflow.md) — evidence quality: medium
- [(Proposal) Adding OpenTelemetry Trace Support to MCP](summaries/s3-003-Proposal-Adding-OpenTelemetry-Trace-Supp.md) — evidence quality: high
- [OpenTelemetry for AI Agents: Implementing Observability in MCP Workflows](summaries/s3-004-OpenTelemetry-for-AI-Agents-Implementing.md) — evidence quality: low
- [OneUptime：MCP 服务器 OpenTelemetry 仪器化指南（原文已失效）](summaries/s3-005-How-to-Instrument-MCP-Servers-with-OpenT.md) — evidence quality: low（原文为 404 页面，实质技术内容缺失）
- [s3-006_The_Attack_and_Defense_Landscape_of_Agen](summaries/s3-006-The-Attack-and-Defense-Landscape-of-Agen.md) — evidence quality: unknown
- [What Are AI Agent Audit Trails? Why They Matter for Compliance](summaries/s3-007-What-Are-AI-Agent-Audit-Trails-Why-They.md) — evidence quality: low（概念阐述为主，缺乏技术实现细节）
- [RFC: should AutoGen support tamper-evident audit trails for multi-agent conversations in regulated industries?](summaries/s3-008-RFC-should-AutoGen-support-tamper-eviden.md) — evidence quality: 中（基于社区实践反馈与跨框架趋势观察）
- [OWASP Top 10 for Agentic Applications: Compliance Guide](summaries/s3-009-OWASP-Top-10-for-Agentic-Applications-Co.md) — evidence quality: medium
- [防篡改 AI Agent 审计追踪：SIEM 集成的合规要求与实践指南](summaries/s3-010-Tamper-Evident-Audit-Trails-for-AI-Agent.md) — evidence quality: medium（基于合规框架引用和具体技术要求，但带有厂商产品推广倾向）
- [Token Economics for LLM Agents: A Dual-View Study from Computing and Economics](summaries/s3-011-Token-Economics-for-LLM-Agents-A-Dual-Vi.md) — evidence quality: medium
- [Token Economics for LLM Agents 深度阅读笔记](summaries/s3-011-note.md) — evidence quality: unknown
- [AI Cost Visibility: How to Track and Optimize Token Spend Before the Invoice Arrives](summaries/s3-012-AI-Cost-Visibility-Before-the-Invoice-Ho.md) — evidence quality: low
- [A Guide to AI Agent Cost Optimization With Observability](summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi.md) — evidence quality: unknown
- [LLM Agent Cost Attribution: Complete Production 2026 Guide](summaries/s3-014-LLM-Agent-Cost-Attribution-Complete-Prod.md) — evidence quality: medium
- [What Is AI Agent Observability? Why Cost Is What You're Missing](summaries/s3-015-What-Is-AI-Agent-Observability-Why-Cost.md) — evidence quality: unknown
- [SafeSieve: From Heuristics to Experience in Progressive Pruning for LLM-based Multi-Agent Communication](summaries/safesieve-note.md) — evidence quality: unknown
- [SAGE: Selective Attention-Guided Extraction for Token-Efficient Document Indexing](summaries/sage-note.md) — evidence quality: unknown
- [SemShareKV: Efficient KVCache Sharing for Semantically Similar Prompts via Token-Level LSH Matching](summaries/semsharekv-note.md) — evidence quality: unknown
- [SentenceKV: Efficient LLM Inference via Sentence-Level Semantic KV Caching](summaries/sentencekv-note.md) — evidence quality: unknown
- [When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail](summaries/singleagentskills-note.md) — evidence quality: unknown
- [How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks](summaries/spendmoney-note.md) — evidence quality: unknown
- [Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents](summaries/squeez-note.md) — evidence quality: unknown
- [Stop Wasting Your Tokens: Towards Efficient Runtime Multi-Agent Systems](summaries/supervisoragent-note.md) — evidence quality: unknown
- [SWE-Chain: Benchmarking Coding Agents on Chained Release-Level Package Upgrades](summaries/swechain-note.md) — evidence quality: unknown
- [SWE-Edit: Rethinking Code Editing for Efficient SWE-Agent](summaries/sweedit-note.md) — evidence quality: unknown
- [Token-Budget-Aware LLM Reasoning](summaries/tale-note.md) — evidence quality: unknown
- [Agent psychometrics: 智能体代码基准的任务级性能预测](summaries/taskpredict-note.md) — evidence quality: unknown
- [Task-Aware LLM Routing with Multi-Level Task-Profile-Guided Data Synthesis for Cold-Start Scenarios](summaries/trouter-note.md) — evidence quality: unknown
- [ZEBRA: Zero-shot Budgeted Resource Allocation for LLM Orchestration](summaries/zebra-note.md) — evidence quality: unknown

## Open Questions
- Which agent trace events are essential across platforms, and which are product-specific?
- How should cognitive traces be captured without leaking sensitive reasoning or private data?
- Can failure attribution be standardized across single-agent, multi-agent, and coding-agent workflows?
- What minimum evidence should a production agent audit trail preserve for compliance and incident response?
