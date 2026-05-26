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

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/evaluation-and-benchmarking]], [[concepts/audit-trails-security-and-governance]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: [[entities/Claude-Code|Claude Code]], [[entities/Codex-CLI|Codex CLI]]
