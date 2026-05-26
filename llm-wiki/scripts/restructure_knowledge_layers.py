#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_NOTES = ROOT / "raw" / "notes"
WIKI = ROOT / "wiki"
TERMS = WIKI / "terms"
VIEWPOINTS = WIKI / "viewpoints"
COMPARISONS = WIKI / "comparisons"
LOG = ROOT / "log"


def slugify(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9\u4e00-\u9fff]+", "-", text).strip("-")[:90] or "untitled"


def link_label(text: str) -> str:
    return text.replace("[", "(").replace("]", ")").replace("|", "-")


def clean_text(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_sentences(text: str) -> list[str]:
    text = clean_text(text)
    parts = re.split(r"(?<=[。.!?])\s+", text)
    return [p.strip() for p in parts if len(p.strip()) >= 24]


def first_sentences(text: str, limit: int = 2) -> list[str]:
    out = []
    for sentence in split_sentences(text):
        if "待补充" in sentence or "bundle 中未提取" in sentence:
            continue
        out.append(sentence[:280])
        if len(out) >= limit:
            break
    return out


def parse_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    matches = list(re.finditer(r"^##\s+(.+)$", text, re.M))
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[match.group(1).strip()] = text[start:end].strip()
    return sections


def parse_meta(text: str, key: str) -> str:
    patterns = [
        rf"^- \*\*{re.escape(key)}\*\*:\s*(.*)$",
        rf"^- {re.escape(key)}:\s*(.*)$",
        rf"^-  {re.escape(key.lower())}:\s*(.*)$",
        rf"^- {re.escape(key.lower())}:\s*(.*)$",
    ]
    for pattern in patterns:
        m = re.search(pattern, text, re.M)
        if m:
            return m.group(1).strip()
    return ""


def parse_note(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+)$", text, re.M)
    title = title_match.group(1).strip() if title_match else path.stem
    sections = parse_sections(text)
    body_for_evidence = "\n\n".join(
        sections.get(name, "")
        for name in ["一句话总结", "研究问题", "方法主线", "关键结果", "深度分析", "我的笔记"]
    )
    return {
        "path": path,
        "name": path.name,
        "stem": path.stem,
        "slug": slugify(path.stem),
        "title": title,
        "text": text,
        "lower": text.lower(),
        "sections": sections,
        "evidence": body_for_evidence or text[:5000],
        "year": parse_meta(text, "年份") or parse_meta(text, "date") or "n.d.",
        "quality": parse_meta(text, "证据质量") or "unknown",
    }


def select_notes(notes: list[dict], keywords: list[str], limit: int = 12) -> list[dict]:
    scored = []
    for note in notes:
        score = sum(note["lower"].count(k.lower()) for k in keywords)
        if score:
            scored.append((score, note["title"], note))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [item[2] for item in scored[:limit]]


def evidence_lines(notes: list[dict], keywords: list[str], limit: int = 8) -> list[str]:
    lines = []
    for note in notes:
        sentences = []
        section_order = ["一句话总结", "研究问题", "方法主线", "关键结果", "深度分析", "我的笔记", "原文摘要翻译"]
        for section_name in section_order:
            text = note["sections"].get(section_name, "")
            if not text:
                continue
            keyword_hit = any(k.lower() in text.lower() for k in keywords)
            if keyword_hit:
                sentences = first_sentences(text, 1)
                break
        if not sentences:
            sentences = first_sentences(note["evidence"], 1)
        if sentences:
            lines.append(f"- [[summaries/{note['slug']}|{link_label(note['title'])}]] — {sentences[0]}")
        if len(lines) >= limit:
            break
    return lines


TERMS_DEF = {
    "agent-trace": {
        "title": "智能体轨迹",
        "definition": "智能体轨迹是按时间记录的用户输入、模型消息、工具调用、工具返回、状态更新、环境观测和评测结果。它是失败诊断、合规评测、审计和成本归因的共同证据层。",
        "keywords": ["trace", "trajectory", "轨迹", "工具调用", "状态更新", "span", "messages"],
        "questions": ["这条轨迹是否足以复现失败？", "轨迹中是否保留了工具参数、观测和状态变化？", "哪些字段应进入审计而不是普通日志？"],
    },
    "failure-attribution": {
        "title": "失败归因",
        "definition": "失败归因关注失败由哪个智能体、哪个步骤、哪类约束违反或哪条依赖链触发。它把可观测性从“发生了失败”推进到“应该修哪里”。",
        "keywords": ["failure", "归因", "diagnos", "root cause", "attribution", "关键失败步骤", "不可恢复"],
        "questions": ["第一个不可恢复步骤在哪里？", "错误是根因还是后果？", "责任主体是模型、工具、路由、提示还是 harness？"],
    },
    "process-compliance": {
        "title": "过程合规性",
        "definition": "过程合规性评估智能体是否按系统提示、工具 schema、业务规则和安全策略行动，而不只看最终答案或最终状态是否正确。",
        "keywords": ["compliance", "规范", "合规", "spec", "AgentPex", "output_spec", "transition"],
        "questions": ["最终成功是否掩盖了违规过程？", "提示词和工具定义能否被抽取成可检查规范？", "judge 评分与最终奖励如何互补？"],
    },
    "monitorability": {
        "title": "可监控性",
        "definition": "可监控性描述从模型外部或过程信号中发现错误、违规或欺骗行为的能力。它不等同于可解释性，而是面向部署监控与安全评估的可检测性问题。",
        "keywords": ["monitorability", "monitor", "可监控", "监控", "chain-of-thought", "CoT"],
        "questions": ["哪些行为只能通过过程信号发现？", "隐藏推理或压缩轨迹会损害哪些监控能力？", "监控器自身如何被评估？"],
    },
    "trace-schema": {
        "title": "轨迹 Schema",
        "definition": "轨迹 Schema 是把智能体事件结构化的字段约定，决定跨平台日志能否被诊断器、评测器、审计器和成本分析器复用。",
        "keywords": ["schema", "standard", "OpenTelemetry", "OpenInference", "Hermes", "AgentTrace", "logging framework", "format"],
        "questions": ["哪些字段是跨平台最小集合？", "OTel span 与智能体认知事件如何映射？", "schema 是否保留足够上下文用于事后取证？"],
    },
    "harness": {
        "title": "Harness",
        "definition": "Harness 是模型外部可编辑的执行表面，包括系统提示、工具描述、工具实现、中间件、技能、子智能体配置和长期记忆。它决定模型如何使用环境。",
        "keywords": ["harness", "Agentic Harness", "工具实现", "中间件", "技能", "长期记忆", "coding-agent"],
        "questions": ["失败模式能否映射到具体 harness 组件？", "变更是否可回滚、可归因、可证伪？", "演化出的 harness 是否能跨模型迁移？"],
    },
    "audit-trail": {
        "title": "审计轨迹",
        "definition": "审计轨迹是面向责任追踪、合规和事后取证的事件记录，通常要求完整性、时间顺序、身份绑定、敏感信息控制和防篡改能力。",
        "keywords": ["audit", "trail", "审计", "tamper", "governance", "compliance", "SIEM"],
        "questions": ["哪些事件必须可证明未被篡改？", "审计记录和调试日志如何分层？", "敏感推理与合规证据如何平衡？"],
    },
    "cost-attribution": {
        "title": "成本归因",
        "definition": "成本归因把 token、模型调用、工具调用、重试、缓存、失败和多智能体依赖链连接起来，使团队能把费用分摊到任务、用户、功能或失败模式。",
        "keywords": ["cost", "token", "invoice", "budget", "成本", "pricing", "resource attribution"],
        "questions": ["成本应该按请求、任务、工具链还是智能体分摊？", "失败重试和长上下文膨胀如何暴露？", "成本信号如何与 trace join？"],
    },
    "token-economics": {
        "title": "Token 经济学",
        "definition": "Token 经济学把智能体系统中的 token 视为可计量、可归因、可预算和可优化的计算资源，关注 token 投入如何转化为任务质量、延迟、可靠性和业务价值。",
        "keywords": ["token economics", "token", "economics", "token 经济", "token经济", "消耗", "成本", "efficiency", "spend"],
        "questions": ["token 增加带来的质量收益是否递减？", "多智能体性能提升是协作收益还是 token 预算扩张？", "哪些 token 消耗属于必要推理，哪些属于浪费？"],
    },
    "token-budget": {
        "title": "Token 预算",
        "definition": "Token 预算是在任务、会话、用户、团队或工作流层面对输入、输出、思考、工具返回和重试 token 设置上限、配额和告警阈值的工程机制。",
        "keywords": ["budget", "quota", "limit", "token", "预算", "配额", "限额", "guardrail"],
        "questions": ["预算应该绑定到单次请求、完整任务还是用户会话？", "超预算时应该降级模型、压缩上下文还是中止执行？", "预算策略如何避免牺牲关键任务质量？"],
    },
    "context-bloat": {
        "title": "上下文膨胀",
        "definition": "上下文膨胀指长程智能体在累积消息、工具返回、检索片段、记忆和多智能体通信时不断扩大 prompt，导致成本、延迟和错误传播同步上升。",
        "keywords": ["context", "long context", "上下文", "膨胀", "token", "history", "memory", "retrieval"],
        "questions": ["哪些历史信息真正影响下一步决策？", "上下文压缩会损失哪些可监控和审计信号？", "长上下文成本应如何与失败风险一起评估？"],
    },
    "cache-and-reuse": {
        "title": "缓存与复用",
        "definition": "缓存与复用通过 prompt cache、语义缓存、工具结果缓存、检索结果复用和中间产物复用降低重复 token 与外部调用成本，但需要处理失效、隐私和一致性问题。",
        "keywords": ["cache", "caching", "缓存", "reuse", "复用", "memoization", "dedup", "重复"],
        "questions": ["哪些输入和工具结果可以安全复用？", "缓存命中率如何进入 trace 与成本归因？", "缓存错误会如何放大为任务失败或合规风险？"],
    },
    "model-routing": {
        "title": "模型路由",
        "definition": "模型路由根据任务难度、上下文长度、风险等级、延迟目标和预算在不同模型之间动态选择，以在质量、成本和速度之间取得可控折中。",
        "keywords": ["routing", "router", "model routing", "模型路由", "cascade", "cascading", "gpt-4o-mini", "quality cost"],
        "questions": ["路由器如何判断任务是否需要昂贵模型？", "级联推理何时比单次强模型调用更经济？", "错误路由的质量损失如何被监控？"],
    },
    "cost-visibility": {
        "title": "成本可见性",
        "definition": "成本可见性是在账单到来之前，把 token、模型价格、工具调用、重试、缓存命中和用户/功能维度实时呈现出来，使团队能在运行期发现成本异常。",
        "keywords": ["cost visibility", "invoice", "bill", "billing", "spend", "成本可见", "账单", "成本异常"],
        "questions": ["成本异常应按什么粒度告警？", "账单维度如何回连到 trace、用户和功能？", "成本可见性如何转化为具体优化动作？"],
    },
    "multi-agent-failure": {
        "title": "多智能体失败",
        "definition": "多智能体失败来自角色分工、通信协议、依赖链、协调策略和共享状态中的错误传播，不能只用单智能体最终成功率解释。",
        "keywords": ["multi-agent", "多智能体", "coordination", "MAS", "dependency", "collaboration", "agent causes"],
        "questions": ["失败是单个智能体决策错误还是协作协议错误？", "依赖链中哪个输出被后续错误放大？", "是否需要群体级 trace schema？"],
    },
    "runtime-instrumentation": {
        "title": "运行时插桩",
        "definition": "运行时插桩是在模型调用、工具调用、MCP server、环境事件和业务状态变更处记录结构化遥测，为实时监控和离线诊断提供数据。",
        "keywords": ["instrument", "instrumentation", "runtime", "MCP", "OpenTelemetry", "span", "eBPF", "telemetry"],
        "questions": ["哪些边界应产生 span？", "插桩开销和隐私风险如何控制？", "被动 eBPF 与应用级 SDK 各适合什么场景？"],
    },
}


VIEWPOINTS_DEF = {
    "observability-is-not-logging": {
        "title": "智能体可观测性不是日志收集",
        "thesis": "单纯存下消息和工具调用并不能回答为什么失败；可观测性必须把轨迹转化为可诊断、可评测、可审计的证据。",
        "keywords": ["observability", "trace", "diagnos", "归因", "AgentRx", "AgentTrace", "debug"],
        "implications": ["日志平台需要上接诊断器、评测器和审计器。", "字段设计要从问题反推，而不是只记录容易拿到的数据。", "轨迹质量比轨迹体量更重要。"],
    },
    "final-reward-is-insufficient": {
        "title": "最终奖励不足以评估智能体",
        "thesis": "最终成功率会掩盖过程违规、错误工具使用和偶然成功；轨迹级过程评测应与结果评测并列。",
        "keywords": ["reward", "AgentPex", "benchmark", "过程", "合规", "tau", "最终"],
        "implications": ["benchmark 应同时报告最终状态、过程规范和失败类别。", "合规场景中过程违规本身就是失败。", "多指标评测比单一 reward 更能指导修复。"],
    },
    "schema-is-the-product-boundary": {
        "title": "Schema 决定可观测产品边界",
        "thesis": "谁拥有更好的 agent trace schema，谁就更容易连接监控、调试、评测、安全和成本归因；schema 是产品能力边界而不是后端细节。",
        "keywords": ["schema", "OpenTelemetry", "OpenInference", "AgentTrace", "Hermes", "standard"],
        "implications": ["平台比较应看字段可解释性，而不是只看 dashboard。", "OTel 解决传输和 span 生态，但 agent-specific 字段仍需补足。", "schema 稳定性决定历史数据能否复用。"],
    },
    "harness-is-optimizable-surface": {
        "title": "Harness 是可优化的工程表面",
        "thesis": "模型能力之外，系统提示、工具、中间件、技能和记忆共同决定智能体表现；这些组件应被视为可观测、可回滚、可演化的工程对象。",
        "keywords": ["harness", "Agentic Harness", "AHE", "self-evolution", "技能", "中间件"],
        "implications": ["调试不应默认归咎于模型。", "组件级版本历史能让性能变化可归因。", "自动演化必须记录预测和回滚依据。"],
    },
    "auditability-requires-tamper-evidence": {
        "title": "审计能力需要防篡改证据链",
        "thesis": "生产智能体的审计轨迹不仅要可读，还要能证明事件顺序、身份、完整性和敏感字段处理，否则难以支撑监管与事故复盘。",
        "keywords": ["audit", "tamper", "SIEM", "governance", "security", "guardrail"],
        "implications": ["审计日志应与普通调试日志分层。", "安全事件需要可验证链路，而不是事后拼接截图。", "隐私脱敏策略本身也应进入审计。"],
    },
    "cost-is-observability-signal": {
        "title": "成本是可观测性信号",
        "thesis": "token 和调用成本不是财务尾项，而是反映长上下文、重试、工具循环、失败恢复和多智能体协作效率的运行信号。",
        "keywords": ["cost", "token", "invoice", "budget", "成本", "optimization"],
        "implications": ["成本 dashboard 必须能 drill down 到 trace。", "失败样本应同时看质量损失和资源浪费。", "优化策略需要区分模型成本、工具成本和重试成本。"],
    },
    "token-efficiency-needs-quality-denominator": {
        "title": "Token 效率必须带质量分母",
        "thesis": "只看 token 降低会把系统推向廉价但无效的执行；只看成功率又会掩盖 token 暴涨。合理的 token 经济学应把单位成本质量、单位任务成本和失败浪费同时纳入分析。",
        "keywords": ["token", "efficiency", "quality", "成本", "消耗", "成功率", "accuracy", "variance"],
        "implications": ["报告性能提升时应同步报告 token、延迟和调用次数。", "优化目标应区分节省 token 与提升 token 产出率。", "多智能体系统尤其需要用质量/token 比例解释收益。"],
    },
    "cost-control-is-policy-not-only-dashboard": {
        "title": "成本控制不是只做 dashboard",
        "thesis": "成本可见性只能说明钱花在哪里，真正的成本控制还需要预算策略、模型路由、缓存复用、上下文裁剪和超预算降级等运行时政策。",
        "keywords": ["budget", "routing", "cache", "cost optimization", "成本优化", "成本控制", "limit"],
        "implications": ["trace schema 应记录预算决策和降级动作。", "告警之后必须能定位到可执行的优化旋钮。", "平台应把成本策略作为生产 guardrail，而不是财务报表。"],
    },
    "context-is-economic-liability": {
        "title": "上下文是一种经济负债",
        "thesis": "长上下文改善智能体记忆和可解释性，但每轮复制历史都会增加 token 成本、延迟和错误传播面；上下文管理应被视为成本工程核心问题。",
        "keywords": ["context", "long context", "memory", "token", "上下文", "压缩", "retrieval"],
        "implications": ["上下文裁剪要与审计和监控需求共同设计。", "记忆、检索和摘要都应报告成本收益。", "长程任务的成本异常常常首先表现为上下文膨胀。"],
    },
}


COMPARISONS_DEF = {
    "diagnosis-vs-compliance-vs-logging": {
        "title": "失败诊断、过程合规与结构化日志的分工",
        "keywords": ["AgentRx", "AgentPex", "AgentTrace", "failure", "schema", "logging", "compliance"],
        "axes": [
            ("核心问题", "哪里失败、为什么失败", "是否按规范行动", "发生了什么、如何复现"),
            ("典型输入", "失败轨迹、工具约束、人工标注", "系统提示、工具 schema、完整轨迹", "消息、工具调用、状态、span"),
            ("典型输出", "关键失败步骤、失败类别、责任主体", "多维合规评分、违规类型", "结构化事件、可查询 trace"),
            ("适用阶段", "失败后调试与 benchmark 分析", "持续评测与模型/领域对比", "运行时采集与离线分析基底"),
            ("代表来源", "AgentRx, Who&When, GUIDE", "AgentPex, monitorability work", "AgentTrace, OpenInference, OTel material"),
        ],
    },
    "academic-vs-product-observability": {
        "title": "学术论文与产品材料中的可观测性差异",
        "keywords": ["benchmark", "product", "LangSmith", "Langfuse", "Arize", "AgentOps", "academic", "failure"],
        "axes": [
            ("关注对象", "失败机制、归因、评测任务、形式化定义", "接入 SDK、dashboard、告警、成本和团队工作流"),
            ("证据形态", "数据集、实验表格、消融、统计指标", "产品页面、文档、集成示例、市场叙述"),
            ("优势", "问题定义清晰，能比较方法效果", "贴近生产接入，覆盖运行和组织流程"),
            ("盲区", "部署成本、权限和合规集成不足", "schema 细节和可复现实验常常不足"),
            ("wiki 使用方式", "作为概念和方法基准", "作为工具地图和落地需求证据"),
        ],
    },
    "otel-vs-agent-specific-schema": {
        "title": "OpenTelemetry 与 Agent-specific Schema 的边界",
        "keywords": ["OpenTelemetry", "OpenInference", "schema", "span", "trajectory", "AgentTrace", "MCP"],
        "axes": [
            ("OTel 擅长", "跨服务 trace、span 传播、指标/日志生态、厂商集成"),
            ("Agent-specific 擅长", "意图、计划、工具语义、记忆、推理步骤、合规规范和失败类别"),
            ("连接方式", "把模型调用、工具调用、MCP server 和环境事件映射为 span，同时保留 agent 语义属性"),
            ("风险", "只用 OTel 容易丢失认知/任务语义；只用自定义 schema 容易失去生态互通"),
            ("结论", "生产系统应采用 OTel 作为传输与关联骨架，叠加 agent-specific 字段作为诊断语义层"),
        ],
    },
    "single-agent-vs-multi-agent-failure": {
        "title": "单智能体失败与多智能体失败对比",
        "keywords": ["multi-agent", "single-agent", "failure", "dependency", "coordination", "agent causes"],
        "axes": [
            ("失败边界", "单条轨迹内的步骤、工具和状态", "多个角色之间的消息、依赖和共享状态"),
            ("主要根因", "工具参数错误、计划偏离、误读观察、输出不合规", "通信丢失、角色职责混淆、依赖传播、冲突决策"),
            ("归因难点", "第一个不可恢复步骤不唯一", "责任可能跨 agent 和时间扩散"),
            ("所需 trace", "步骤级消息和工具调用", "agent 身份、交互边、依赖链、共享资源访问"),
            ("代表来源", "AgentRx, AgentPex, AgentSight", "Why Do Multi-Agent LLM Systems Fail, Who&When, EvoCF, MASPrism"),
        ],
    },
    "runtime-monitoring-vs-offline-analysis": {
        "title": "运行时监控与离线分析对比",
        "keywords": ["runtime", "monitor", "offline", "diagnosis", "audit", "evaluation", "instrumentation"],
        "axes": [
            ("目标", "及时发现异常、告警、限流或阻断", "解释失败、比较模型、生成证据和改进系统"),
            ("延迟要求", "低延迟、低开销、可在线执行", "可接受批处理和较高 judge 成本"),
            ("数据粒度", "核心 span、指标、错误和抽样日志", "完整轨迹、原始上下文、人工/自动标注和实验结果"),
            ("常见方法", "OpenTelemetry、eBPF、SDK 插桩、产品 dashboard", "AgentRx、AgentPex、AHE、benchmark 分析"),
            ("设计取舍", "实时性优先，解释可能较浅", "解释性优先，成本和隐私压力更高"),
        ],
    },
    "observability-product-map": {
        "title": "可观测产品和开源工具对比地图",
        "keywords": ["LangSmith", "Langfuse", "Arize", "Phoenix", "Braintrust", "AgentOps", "Datadog", "Helicone", "Splunk", "Elastic", "New Relic"],
        "axes": [
            ("LangSmith / Langfuse", "面向 LLM 应用开发、trace、prompt、eval 和数据集闭环"),
            ("Arize Phoenix / OpenInference", "强调 open instrumentation、eval 和 OpenTelemetry 语义连接"),
            ("Braintrust / Helicone", "强调 eval、gateway、请求记录、成本和开发工作流"),
            ("Datadog / Splunk / Elastic / New Relic", "把 LLM/agent telemetry 接入既有 APM 和企业运维栈"),
            ("AgentOps", "更明确面向 agent session、工具调用和 agent 运行监控"),
        ],
    },
    "token-cost-vs-quality": {
        "title": "Token 成本与质量收益对比",
        "keywords": ["token", "cost", "quality", "accuracy", "成功率", "效率", "消耗", "成本"],
        "axes": [
            ("优化目标", "降低总 token 花费", "提高单位 token 产出的任务质量", "降低失败与重试造成的浪费"),
            ("主要指标", "每请求 token、每会话成本、账单预测", "成功率/token、质量/美元、边际收益", "失败 trace 成本、重试次数、循环调用成本"),
            ("风险", "过度压缩导致质量下降", "高质量样本可能掩盖成本不可扩展", "只处理失败不处理正常路径低效"),
            ("需要的 trace 字段", "prompt/completion token、模型价格、用户/功能标签", "评测分数、任务难度、模型选择", "失败类别、重试链、工具循环、终止原因"),
            ("适用场景", "预算治理、账单预警", "模型和架构比较", "生产事故复盘与系统优化"),
        ],
    },
    "model-routing-vs-context-compression-vs-cache": {
        "title": "模型路由、上下文压缩与缓存复用对比",
        "keywords": ["routing", "cache", "context", "compression", "模型路由", "缓存", "上下文", "成本优化"],
        "axes": [
            ("机制", "按任务难度和预算选择模型", "裁剪、摘要或分层保留历史上下文", "复用 prompt、工具结果或语义相似响应"),
            ("主要收益", "降低昂贵模型调用占比", "降低每轮输入 token 与延迟", "减少重复计算和外部调用"),
            ("主要风险", "低估任务难度导致质量下降", "丢失关键证据或审计上下文", "缓存陈旧、隐私泄漏或错误复用"),
            ("观测要求", "记录路由理由、候选模型和降级结果", "记录被裁剪内容摘要与压缩比例", "记录命中率、失效策略和复用来源"),
            ("更适合", "任务异质性高的产品", "长程 agent 和多轮会话", "重复查询、稳定工具和高频工作流"),
        ],
    },
    "financial-cost-vs-computational-cost": {
        "title": "财务成本与计算成本对比",
        "keywords": ["invoice", "pricing", "compute", "latency", "token", "账单", "成本", "resource"],
        "axes": [
            ("财务成本", "供应商账单、模型单价、API 调用费、外部工具费用"),
            ("计算成本", "token 数、上下文长度、延迟、吞吐、重试和缓存开销"),
            ("差异", "财务成本回答花了多少钱；计算成本解释为什么会花这些钱"),
            ("连接方式", "把 trace 中的 token、模型、工具和用户/功能标签映射到价格表与账单维度"),
            ("结论", "没有计算成本分解的账单只能报账，不能指导 agent 系统优化"),
        ],
    },
}


def write_terms(notes: list[dict]) -> None:
    TERMS.mkdir(parents=True, exist_ok=True)
    for old in TERMS.glob("*.md"):
        old.unlink()
    for slug, cfg in TERMS_DEF.items():
        linked = select_notes(notes, cfg["keywords"], 14)
        lines = evidence_lines(linked, cfg["keywords"], 10)
        related = [
            other_slug
            for other_slug, other in TERMS_DEF.items()
            if other_slug != slug and set(k.lower() for k in cfg["keywords"]) & set(k.lower() for k in other["keywords"])
        ][:5]
        content = f"""# {cfg['title']}

## 定义

{cfg['definition']}

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

{chr(10).join(f"- {q}" for q in cfg["questions"])}

## 证据入口

{chr(10).join(lines) if lines else "- 暂无足够匹配的本地笔记证据。"}

## 相关词条

{chr(10).join(f"- [[terms/{r}|{TERMS_DEF[r]['title']}]]" for r in related) if related else "- [[terms/agent-trace|智能体轨迹]]"}
"""
        (TERMS / f"{slug}.md").write_text(content, encoding="utf-8")


def write_viewpoints(notes: list[dict]) -> None:
    VIEWPOINTS.mkdir(parents=True, exist_ok=True)
    for old in VIEWPOINTS.glob("*.md"):
        old.unlink()
    for slug, cfg in VIEWPOINTS_DEF.items():
        linked = select_notes(notes, cfg["keywords"], 14)
        lines = evidence_lines(linked, cfg["keywords"], 9)
        counter = "这个观点不是说相邻层不重要，而是说单独依赖该层会留下诊断或治理缺口。"
        content = f"""# {cfg['title']}

## 观点

{cfg['thesis']}

## 为什么成立

{chr(10).join(lines) if lines else "- 暂无足够匹配的本地笔记证据。"}

## 工程含义

{chr(10).join(f"- {item}" for item in cfg["implications"])}

## 反例与边界

{counter} 对于低风险 demo，轻量日志可能足够；对于生产智能体、长程任务、多智能体协作或合规场景，必须把 trace、评测、审计和成本信号组织成可追溯证据。

## 相关词条

- [[terms/agent-trace|智能体轨迹]]
- [[terms/failure-attribution|失败归因]]
- [[terms/trace-schema|轨迹 Schema]]
"""
        (VIEWPOINTS / f"{slug}.md").write_text(content, encoding="utf-8")


def write_comparisons(notes: list[dict]) -> None:
    COMPARISONS.mkdir(parents=True, exist_ok=True)
    for old in COMPARISONS.glob("*.md"):
        old.unlink()
    for slug, cfg in COMPARISONS_DEF.items():
        linked = select_notes(notes, cfg["keywords"], 16)
        evidence = evidence_lines(linked, cfg["keywords"], 8)
        width = max(len(row) for row in cfg["axes"])
        if width == 2:
            header = "| 维度 | 结论 |\n|---|---|"
            rows = "\n".join(f"| {row[0]} | {row[1]} |" for row in cfg["axes"])
        else:
            header_cells = ["维度"] + [f"对象 {i}" for i in range(1, width)]
            header = f"| {' | '.join(header_cells)} |\n| {' | '.join(['---'] * width)} |"
            padded_rows = []
            for row in cfg["axes"]:
                padded = list(row) + [""] * (width - len(row))
                padded_rows.append(f"| {' | '.join(padded)} |")
            rows = "\n".join(padded_rows)
        content = f"""# {cfg['title']}

## 对比表

{header}
{rows}

## 读法

这个对比页用于帮助选择分析层，而不是给工具或论文排名。若要解释单条失败轨迹，优先看诊断与归因；若要比较模型和领域，优先看过程评测；若要做生产接入，先保证结构化采集和 schema 稳定。

## 证据入口

{chr(10).join(evidence) if evidence else "- 暂无足够匹配的本地笔记证据。"}

## 相关页面

- [[terms/agent-trace|智能体轨迹]]
- [[viewpoints/observability-is-not-logging|智能体可观测性不是日志收集]]
- [[viewpoints/final-reward-is-insufficient|最终奖励不足以评估智能体]]
"""
        (COMPARISONS / f"{slug}.md").write_text(content, encoding="utf-8")


def update_index() -> None:
    index = WIKI / "index.md"
    text = index.read_text(encoding="utf-8")
    block = """## Knowledge Layers
- [[terms/agent-trace|词条：智能体轨迹]] · [[terms/cost-attribution|成本归因]] · [[terms/token-economics|Token 经济学]] · [[terms/token-budget|Token 预算]] · [[terms/context-bloat|上下文膨胀]]
- [[terms/cache-and-reuse|缓存与复用]] · [[terms/model-routing|模型路由]] · [[terms/cost-visibility|成本可见性]] · [[terms/trace-schema|轨迹 Schema]] · [[terms/harness|Harness]]
- [[viewpoints/cost-is-observability-signal|观点：成本是可观测性信号]] · [[viewpoints/token-efficiency-needs-quality-denominator|Token 效率必须带质量分母]] · [[viewpoints/cost-control-is-policy-not-only-dashboard|成本控制不是只做 dashboard]] · [[viewpoints/context-is-economic-liability|上下文是一种经济负债]]
- [[comparisons/token-cost-vs-quality|对比：Token 成本与质量收益]] · [[comparisons/model-routing-vs-context-compression-vs-cache|模型路由/上下文压缩/缓存]] · [[comparisons/financial-cost-vs-computational-cost|财务成本与计算成本]]
"""
    text = re.sub(r"\n## Knowledge Layers\n(?:.*\n)*?(?=\n## )", "\n", text)
    text = text.replace("\n## Concepts\n", f"\n{block}\n## Concepts\n")
    index.write_text(text, encoding="utf-8")


def main() -> None:
    notes = [parse_note(path) for path in sorted(RAW_NOTES.glob("*.md"))]
    write_terms(notes)
    write_viewpoints(notes)
    write_comparisons(notes)
    update_index()

    now = datetime.now()
    LOG.mkdir(parents=True, exist_ok=True)
    log_path = LOG / f"{now:%Y%m%d}.md"
    if not log_path.exists():
        log_path.write_text(f"# {now:%Y-%m-%d}\n\n", encoding="utf-8")
    with log_path.open("a", encoding="utf-8") as f:
        f.write(
            f"\n## [{now:%H:%M}] restructure | terms viewpoints comparisons\n"
            f"- Rebuilt {len(TERMS_DEF)} term pages, {len(VIEWPOINTS_DEF)} viewpoint pages, "
            f"and {len(COMPARISONS_DEF)} comparison pages from {len(notes)} raw notes.\n"
        )


if __name__ == "__main__":
    main()
