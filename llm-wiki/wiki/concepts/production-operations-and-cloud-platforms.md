# Production Operations and Cloud Platforms

## Working Definition

Tracks AWS, Google, Alibaba, Baidu, and enterprise deployment guidance for operating agentic systems. In this wiki, the concept is compiled from local source notes rather than general background knowledge.

## Why It Matters

Agentic systems make decisions through multi-step trajectories: prompts, model calls, tool calls, memory updates, environment observations, planner decisions, and post-hoc evaluations. Ordinary request logging is too flat for that behavior. The notes linked here treat observability as a way to recover the trajectory, explain failures, assign responsibility, and create evidence that can be reviewed after deployment.

## Synthesis

- The corpus repeatedly separates **runtime telemetry** from **evaluation evidence**. Telemetry captures what happened; evaluation and audit layers decide whether the behavior was acceptable.
- Trace quality depends on schema discipline. Useful pages in this cluster tend to name the event surface, span or step boundary, metadata context, and downstream debugging question.
- Production material emphasizes integration cost, platform coverage, dashboards, and alerting. Academic material emphasizes failure taxonomies, attribution, monitorability, and formal structure.
- A recurring gap is that many product pages promise agent observability without exposing enough schema detail to compare cognitive, operational, and contextual traces.

## Source Notes

- [[summaries/c-018-AI-Agents-in-Production-Monitoring-Guard|AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-002-AIOpsLab-A-Holistic-Framework-to-Evaluat|AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds]] (n.d., evidence: unknown) — AIOpsLab 评估了四个基于大模型的智能体以及三个传统非大模型方法，在 48 个场景上共进行 288 次评估。四个智能体分别为 GPT-4-with-Shell、GPT-3.5-with-Shell、ReAct、Flash。
- [[summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark|AgentOps AI Infrastructure Platform Market Research Report 2034]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践|Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-012-Beyond-the-Black-Box-Next-Gen-AI-Agent-M|Beyond the Black Box: Next-Gen AI Agent Monitoring]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-010-LLM-and-agentic-AI-observability-Elasti|Elastic LLM与Agentic AI可观测性技术文档]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-017-Essential-Framework-for-AI-Agent-Guardra|Essential Framework for AI Agent Guardrails]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s1-004-Google-ADK-vs-AWS-AgentCore-Enterprise-F|Google ADK vs AWS AgentCore: Enterprise Framework Selection Guide]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s1-001-Google-Cloud-Trace-observability-for-ADK|Google Cloud Trace observability for ADK]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s1-002-Google-boosts-Vertex-AI-Agent-Builder-wi|Google boosts Vertex AI Agent Builder with new observability and deployment tools]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-022-Helicone-LLM-Observability-Platform-Lea|Helicone LLM 可观测性平台深度评测：一键集成与智能成本优化]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-023-Helicone-Open-source-LLM-observability-f|Helicone：开源 LLM 可观测性与 AI 网关一体化平台]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-015-AI-Agent-Observability-Platform-Langfuse|Langfuse 完成 5000 万美元 B 轮融资：AI Agent 可观测性迎来产业级拐点]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s1-009-Operating-agentic-AI-with-Amazon-Bedrock|Operating agentic AI with Amazon Bedrock AgentCore and Datadog LLM Observability: Lessons from NTT DATA]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-009-Introduction-to-Splunk-AI-Agent-Monitori|Splunk AI Agent Monitoring：企业级 AI 代理可观测性官方文档]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-007-The-Reliability-Gap-Agent-Benchmarks-for|The Reliability Gap: Agent Benchmarks for Enterprise]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s3-015-What-Is-AI-Agent-Observability-Why-Cost|What Is AI Agent Observability? Why Cost Is What You're Missing]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-003-Appbuilder-Trace跟踪功能基本用法-百度千帆文档|千帆AppBuilder Trace跟踪功能基本用法]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- Plus 40 additional linked summaries in [[wiki/index|Index]].

## Related Concepts

- [[concepts/agent-observability-landscape]]
- [[concepts/trace-schema-and-telemetry-standards]]
- [[concepts/runtime-instrumentation-and-otel]]
