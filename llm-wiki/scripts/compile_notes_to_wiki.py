#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_NOTES = ROOT / "raw" / "notes"
WIKI = ROOT / "wiki"
SUMMARIES = WIKI / "summaries"
CONCEPTS = WIKI / "concepts"
ENTITIES = WIKI / "entities"
LOG = ROOT / "log"


CONCEPTS_DEF = {
    "agent-observability-landscape": {
        "title": "Agent Observability Landscape",
        "category": "Foundations",
        "summary": "Frames agent observability as traces, evaluations, governance, and production operations rather than ordinary LLM logging.",
        "keywords": ["observability", "monitoring", "debugging", "tracing", "telemetry", "black box", "metrics"],
    },
    "trace-schema-and-telemetry-standards": {
        "title": "Trace Schema and Telemetry Standards",
        "category": "Foundations",
        "summary": "Compares structured agent trace schemas, OpenTelemetry alignment, OpenInference, Hermes-style trajectories, and audit-trail formats.",
        "keywords": ["schema", "standard", "opentelemetry", "openinference", "trace format", "trajectory", "logging framework", "agenttrace"],
    },
    "runtime-instrumentation-and-otel": {
        "title": "Runtime Instrumentation and OpenTelemetry",
        "category": "Engineering",
        "summary": "Covers implementation patterns for instrumenting agents, MCP servers, tool calls, model calls, and distributed workflows.",
        "keywords": ["instrument", "otel", "opentelemetry", "mcp", "span", "cloud trace", "node", "python", "distributed tracing"],
    },
    "failure-diagnosis-and-attribution": {
        "title": "Failure Diagnosis and Attribution",
        "category": "Engineering",
        "summary": "Collects work on localizing failures across agent steps, tools, dependencies, multi-agent coordination, and harnesses.",
        "keywords": ["failure", "diagnose", "debug", "attribution", "root cause", "dependenc", "multi-agent", "task failures"],
    },
    "evaluation-and-benchmarking": {
        "title": "Evaluation and Benchmarking",
        "category": "Evaluation",
        "summary": "Organizes benchmark, white-box evaluation, monitorability, alignment auditing, and long-horizon task evaluation notes.",
        "keywords": ["benchmark", "evaluation", "eval", "monitorability", "alignment", "long-horizon", "audit", "verify", "formal verification"],
    },
    "audit-trails-security-and-governance": {
        "title": "Audit Trails, Security, and Governance",
        "category": "Governance",
        "summary": "Synthesizes tamper-evident audit trails, guardrails, safety violations, agent vulnerabilities, and governance evidence.",
        "keywords": ["audit", "security", "safety", "guardrail", "tamper", "vulnerab", "owasp", "attack", "defense", "governance"],
    },
    "production-operations-and-cloud-platforms": {
        "title": "Production Operations and Cloud Platforms",
        "category": "Operations",
        "summary": "Tracks AWS, Google, Alibaba, Baidu, and enterprise deployment guidance for operating agentic systems.",
        "keywords": ["aws", "amazon", "bedrock", "agentcore", "google", "vertex", "cloud", "aliyun", "baidu", "production", "enterprise"],
    },
    "observability-products-and-market-map": {
        "title": "Observability Products and Market Map",
        "category": "Operations",
        "summary": "Maps product-level agent observability tools such as LangSmith, Langfuse, Arize Phoenix, Braintrust, AgentOps, Datadog, Elastic, New Relic, Splunk, Helicone, and Opik.",
        "keywords": ["langsmith", "langfuse", "arize", "phoenix", "braintrust", "agentops", "datadog", "elastic", "new relic", "splunk", "helicone", "opik", "platform", "product"],
    },
    "cost-token-and-resource-attribution": {
        "title": "Cost, Token, and Resource Attribution",
        "category": "Operations",
        "summary": "Treats cost visibility as part of observability: token economics, invoice prediction, resource attribution, and optimization.",
        "keywords": ["cost", "token", "invoice", "economics", "budget", "pricing", "attribution", "optimization"],
    },
    "agent-frameworks-and-coding-agents": {
        "title": "Agent Frameworks and Coding Agents",
        "category": "Systems",
        "summary": "Connects traces and observability to concrete agent frameworks, coding agents, Claude Code, Codex, Swarm, AgentRx, and workflow systems.",
        "keywords": ["claude code", "codex", "swarm", "agentrx", "llama stack", "agent framework", "coding", "workflow", "multi-agent research"],
    },
}


ENTITIES_DEF = {
    "OpenTelemetry": ["opentelemetry", "otel"],
    "OpenInference": ["openinference"],
    "AgentTrace": ["agenttrace"],
    "Hermes Agent Trajectory Format": ["hermes agent trajectory"],
    "LangSmith": ["langsmith"],
    "Langfuse": ["langfuse"],
    "Arize Phoenix": ["arize", "phoenix"],
    "Braintrust": ["braintrust"],
    "AgentOps": ["agentops"],
    "Helicone": ["helicone"],
    "AWS AgentCore": ["agentcore", "bedrock"],
    "Google ADK and Vertex AI": ["google adk", "vertex"],
    "Claude Code": ["claude code"],
    "Codex CLI": ["codex"],
}


PLACEHOLDERS = (
    "（待补充",
    "（bundle 中未提取到相关内容）",
    "（待补充：BibTeX 引用）",
)


def slugify(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9\u4e00-\u9fff]+", "-", text).strip("-")
    return text[:90] or "untitled"


def link_label(text: str) -> str:
    return text.replace("[", "(").replace("]", ")").replace("|", "-")


def clean_lines(value: str) -> str:
    lines = []
    for line in value.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if any(token in stripped for token in PLACEHOLDERS):
            continue
        if stripped.startswith("```"):
            continue
        lines.append(stripped)
    return "\n".join(lines).strip()


def first_sentences(text: str, limit: int = 3) -> list[str]:
    text = clean_lines(text)
    if not text:
        return []
    chunks = re.split(r"(?<=[。.!?])\s+", text)
    out = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        out.append(chunk[:320])
        if len(out) >= limit:
            break
    return out


def parse_note(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    title = re.search(r"^#\s+(.+)$", text, re.M)
    title_value = title.group(1).strip() if title else path.stem
    meta = {}
    for key in ["标题", "作者", "年份", "来源", "DOI", "arXiv", "PDF", "证据质量"]:
        m = re.search(rf"^- \*\*{re.escape(key)}\*\*:\s*(.*)$", text, re.M)
        meta[key] = m.group(1).strip() if m else ""

    sections: dict[str, str] = {}
    matches = list(re.finditer(r"^##\s+(.+)$", text, re.M))
    for i, m in enumerate(matches):
        name = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[name] = text[start:end].strip()

    haystack = " ".join([title_value, path.name, text[:6000]]).lower()
    concepts = []
    for slug, cfg in CONCEPTS_DEF.items():
        if any(k in haystack for k in cfg["keywords"]):
            concepts.append(slug)
    if not concepts:
        concepts = ["agent-observability-landscape"]

    entities = []
    for name, keys in ENTITIES_DEF.items():
        if any(k in haystack for k in keys):
            entities.append(name)

    return {
        "path": path,
        "text": text,
        "title": title_value,
        "meta": meta,
        "sections": sections,
        "concepts": concepts,
        "entities": entities,
        "summary_slug": slugify(path.stem),
    }


def dedupe_summary_slugs(notes: list[dict]) -> None:
    seen: dict[str, int] = defaultdict(int)
    for note in notes:
        base = note["summary_slug"]
        seen[base] += 1
        if seen[base] > 1:
            note["summary_slug"] = f"{base}-{seen[base]}"


def write_summary(note: dict) -> None:
    meta = note["meta"]
    sections = note["sections"]
    takeaways = []
    for section_name in ["原文摘要翻译", "研究问题", "方法主线", "关键结果", "局限", "我的笔记"]:
        takeaways.extend(first_sentences(sections.get(section_name, ""), 2))
        if len(takeaways) >= 6:
            break
    if not takeaways:
        takeaways = [f"This source is indexed primarily by title and metadata; the extracted note has little substantive body text."]

    concept_links = ", ".join(f"[{c}](concepts/{c}.md)" for c in note["concepts"])
    entity_links = ", ".join(f"[{e}](entities/{slugify(e)}.md)" for e in note["entities"]) or "None identified"
    raw_rel = f"raw/notes/{note['path'].name}"
    pdf = meta.get("PDF", "").replace("`", "")
    source_bits = []
    for label in ["作者", "年份", "来源", "DOI", "arXiv", "证据质量"]:
        value = meta.get(label, "")
        if value:
            source_bits.append(f"- {label}: {value}")
    if pdf:
        source_bits.append(f"- PDF: {pdf}")

    content = f"""# {note['title']}

## Source

- Raw note: `{raw_rel}`
{chr(10).join(source_bits) if source_bits else "- Metadata: not available in note"}

## Compiled Summary

{takeaways[0]}

## Evidence Notes

{chr(10).join(f"- {item}" for item in takeaways[1:]) if len(takeaways) > 1 else "- No additional extracted evidence in the source note."}

## Wiki Connections

- Concepts: {concept_links}
- Entities: {entity_links}
"""
    (SUMMARIES / f"{note['summary_slug']}.md").write_text(content, encoding="utf-8")


def summarize_note_for_concept(note: dict) -> str:
    meta = note["meta"]
    quality = meta.get("证据质量", "unknown") or "unknown"
    year = meta.get("年份", "") or "n.d."
    section = note["sections"].get("关键结果") or note["sections"].get("研究问题") or note["sections"].get("原文摘要翻译", "")
    sentence = first_sentences(section, 1)
    body = sentence[0] if sentence else "Indexed as relevant by title and metadata."
    return f"- [{link_label(note['title'])}](summaries/{note['summary_slug']}.md) ({year}, evidence: {quality}) — {body[:260]}"


def write_concept(slug: str, cfg: dict, notes: list[dict]) -> None:
    notes = sorted(notes, key=lambda n: (n["meta"].get("证据质量", ""), n["title"]))
    source_lines = [summarize_note_for_concept(n) for n in notes[:18]]
    overflow = len(notes) - len(source_lines)
    if overflow > 0:
        source_lines.append(f"- Plus {overflow} additional linked summaries in [Index](index.md).")

    related = [s for s, other in CONCEPTS_DEF.items() if s != slug and set(cfg["keywords"]) & set(other["keywords"])]
    if not related:
        related = [s for s in CONCEPTS_DEF if s != slug][:3]

    content = f"""# {cfg['title']}

## Working Definition

{cfg['summary']} In this wiki, the concept is compiled from local source notes rather than general background knowledge.

## Why It Matters

Agentic systems make decisions through multi-step trajectories: prompts, model calls, tool calls, memory updates, environment observations, planner decisions, and post-hoc evaluations. Ordinary request logging is too flat for that behavior. The notes linked here treat observability as a way to recover the trajectory, explain failures, assign responsibility, and create evidence that can be reviewed after deployment.

## Synthesis

- The corpus repeatedly separates **runtime telemetry** from **evaluation evidence**. Telemetry captures what happened; evaluation and audit layers decide whether the behavior was acceptable.
- Trace quality depends on schema discipline. Useful pages in this cluster tend to name the event surface, span or step boundary, metadata context, and downstream debugging question.
- Production material emphasizes integration cost, platform coverage, dashboards, and alerting. Academic material emphasizes failure taxonomies, attribution, monitorability, and formal structure.
- A recurring gap is that many product pages promise agent observability without exposing enough schema detail to compare cognitive, operational, and contextual traces.

## Source Notes

{chr(10).join(source_lines)}

## Related Concepts

{chr(10).join(f'- [{r}](concepts/{r}.md)' for r in related[:5])}
"""
    (CONCEPTS / f"{slug}.md").write_text(content, encoding="utf-8")


def write_entity(name: str, notes: list[dict]) -> None:
    slug = slugify(name)
    lines = [summarize_note_for_concept(n) for n in notes[:12]]
    content = f"""# {name}

## Role in This Wiki

`{name}` appears as a recurring entity in the local notes corpus. This page is intentionally lightweight: it anchors wikilinks and points to the source summaries where the entity is discussed.

## Linked Source Notes

{chr(10).join(lines) if lines else "- No linked source notes after compilation."}

## Related Concepts

- [Agent Observability Landscape](concepts/agent-observability-landscape.md)
- [Trace Schema and Telemetry Standards](concepts/trace-schema-and-telemetry-standards.md)
- [Observability Products and Market Map](concepts/observability-products-and-market-map.md)
"""
    (ENTITIES / f"{slug}.md").write_text(content, encoding="utf-8")


def write_claude(notes: list[dict]) -> None:
    content = f"""# Agentic Trace Insight Wiki

This is a Karpathy-style LLM wiki compiled from `agentic_trace_insight/notes/`.

## Scope

The wiki tracks agentic AI tracing, observability, audit trails, failure diagnosis, evaluation, production operations, cost attribution, and market/tooling evidence. The current raw corpus contains {len(notes)} Markdown notes copied into `raw/notes/`.

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
"""
    (ROOT / "CLAUDE.md").write_text(content, encoding="utf-8")


def write_index(notes: list[dict], by_concept: dict[str, list[dict]], by_entity: dict[str, list[dict]]) -> None:
    lines = [
        "# Index — Agentic Trace Insight",
        "",
        "> A compiled wiki for agent trace observability, auditability, failure diagnosis, production operations, and cost visibility.",
        "",
        "## Navigation",
        "- [#Knowledge Layers](#knowledge-layers) · [#Concepts](#concepts) · [#Entities](#entities) · [#Summaries](#summaries) · [#Open Questions](#open-questions)",
        "",
        "## Knowledge Layers",
        "- [词条：智能体轨迹](terms/agent-trace.md) · [失败归因](terms/failure-attribution.md) · [过程合规性](terms/process-compliance.md) · [轨迹 Schema](terms/trace-schema.md) · [Harness](terms/harness.md)",
        "- [观点：可观测性不是日志收集](viewpoints/observability-is-not-logging.md) · [观点：最终奖励不足以评估智能体](viewpoints/final-reward-is-insufficient.md) · [观点：Schema 决定产品边界](viewpoints/schema-is-the-product-boundary.md)",
        "- [对比：诊断/合规/日志](comparisons/diagnosis-vs-compliance-vs-logging.md) · [对比：OTel 与 Agent Schema](comparisons/otel-vs-agent-specific-schema.md) · [对比：产品工具地图](comparisons/observability-product-map.md)",
        "",
        "## Concepts",
    ]
    by_category = defaultdict(list)
    for slug, cfg in CONCEPTS_DEF.items():
        by_category[cfg["category"]].append((slug, cfg))
    for category in sorted(by_category):
        lines.append(f"### {category}")
        for slug, cfg in sorted(by_category[category], key=lambda item: item[1]["title"]):
            count = len(by_concept.get(slug, []))
            lines.append(f"- [{cfg['title']}](concepts/{slug}.md) — {cfg['summary']} ({count} linked notes)")
        lines.append("")

    lines.append("## Entities")
    for name in sorted(by_entity):
        count = len(by_entity[name])
        lines.append(f"- [{name}](entities/{slugify(name)}.md) — recurring entity in {count} source notes)")
    lines.append("")

    lines.append("## Summaries")
    for note in sorted(notes, key=lambda n: n["summary_slug"]):
        q = note["meta"].get("证据质量", "unknown") or "unknown"
        lines.append(f"- [{link_label(note['title'])}](summaries/{note['summary_slug']}.md) — evidence quality: {q}")
    lines.append("")

    lines.append("## Open Questions")
    lines.extend([
        "- Which agent trace events are essential across platforms, and which are product-specific?",
        "- How should cognitive traces be captured without leaking sensitive reasoning or private data?",
        "- Can failure attribution be standardized across single-agent, multi-agent, and coding-agent workflows?",
        "- What minimum evidence should a production agent audit trail preserve for compliance and incident response?",
    ])
    (WIKI / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    for directory in [SUMMARIES, CONCEPTS, ENTITIES, LOG]:
        directory.mkdir(parents=True, exist_ok=True)
    for directory in [SUMMARIES, CONCEPTS, ENTITIES]:
        for old in directory.glob("*.md"):
            old.unlink()

    notes = [parse_note(p) for p in sorted(RAW_NOTES.glob("*.md"))]
    dedupe_summary_slugs(notes)
    by_concept: dict[str, list[dict]] = defaultdict(list)
    by_entity: dict[str, list[dict]] = defaultdict(list)

    for note in notes:
        write_summary(note)
        for concept in note["concepts"]:
            by_concept[concept].append(note)
        for entity in note["entities"]:
            by_entity[entity].append(note)

    for slug, cfg in CONCEPTS_DEF.items():
        write_concept(slug, cfg, by_concept.get(slug, []))
    for entity_name in sorted(by_entity):
        write_entity(entity_name, by_entity[entity_name])

    write_claude(notes)
    write_index(notes, by_concept, by_entity)

    now = datetime.now()
    log_path = LOG / f"{now:%Y%m%d}.md"
    if not log_path.exists():
        log_path.write_text(f"# {now:%Y-%m-%d}\n\n", encoding="utf-8")
    with log_path.open("a", encoding="utf-8") as f:
        f.write(
            f"\n## [{now:%H:%M}] compile | notes corpus to wiki\n"
            f"- Compiled {len(notes)} raw notes into {len(notes)} summaries, "
            f"{len(CONCEPTS_DEF)} concept pages, {len(by_entity)} entity pages, and rebuilt index.md.\n"
        )


if __name__ == "__main__":
    main()
