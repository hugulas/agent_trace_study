# Agentic Trace Insight Wiki

This is a Karpathy-style LLM wiki compiled from `agentic_trace_insight/notes/`.

## Scope

The wiki tracks agentic AI tracing, observability, audit trails, failure diagnosis, evaluation, production operations, cost attribution, and market/tooling evidence. The current raw corpus contains 162 Markdown notes copied into `raw/notes/`.

## Operating Rules

- Treat `raw/notes/` as immutable source material.
- Write synthesized knowledge under `wiki/`.
- Prefer nearby source-summary links for claims.
- Use concept pages for durable synthesis and summary pages for per-source evidence.
- When new notes arrive, copy them into `raw/notes/`, regenerate affected summaries, update concept pages, update `wiki/index.md`, and append a log entry.

## Naming Conventions

- Concept pages use lowercase kebab-case under `wiki/concepts/`.
- Entity pages use title-derived slugs under `wiki/entities/`.
- Source summaries preserve the original note filename stem as much as possible under `wiki/summaries/`.

## Current Open Questions

- Which trace schema is most actionable for cross-platform agent failure diagnosis?
- Where is OpenTelemetry sufficient, and where do agent-specific cognitive/contextual fields remain necessary?
- Which observability product exposes enough raw trajectory data to support forensic audit rather than dashboard-only monitoring?
- How should cost attribution be joined with tool-call, model-call, and multi-agent dependency traces?
