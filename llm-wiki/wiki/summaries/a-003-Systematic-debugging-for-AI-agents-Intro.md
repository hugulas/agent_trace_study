# Systematic debugging for AI agents: Introducing the AgentRx framework

## Source

- Raw note: `raw/notes/a-003_Systematic_debugging_for_AI_agents_Intro.md`
- 作者: Microsoft Research Blog（官方团队博文）

## Compiled Summary

AgentRx 博客的价值不仅在于技术本身，更在于它清晰地展示了一个从学术研究到开源工具的完整叙事。

## Evidence Notes

- 四阶段流水线的设计思路非常务实：
不归一化就无法跨域复用，不合成约束就无法脱离人工规则编写，不做守卫评估就会在无关约束上浪费计算，不用 LLM 法官就无法把结构化证据映射到人类可理解的失败类别。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [Claude Code](entities/Claude-Code.md), [Codex CLI](entities/Codex-CLI.md)
