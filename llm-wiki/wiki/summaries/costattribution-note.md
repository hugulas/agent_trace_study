# LLM Agent Cost Attribution: Complete Production 2026 Guide

## Source

- Raw note: `raw/notes/costattribution_note.md`
- Metadata: not available in note

## Compiled Summary

生产级大语言模型智能体成本归因指南，涵盖按用户、按任务、按租户拆解的消耗模式、token 会计方法，以及面向 2026 年部署场景的代理公司利润保护策略。

## Evidence Notes

- 核心要点如下：
- 从第一天开始埋点：成本归因只有在请求创建时就打上标签才算可靠。事后从日志中补打标签总会遗漏边界情况，并低估长链路智能体轨迹的真实消耗。
- 在多租户 LLM 智能体产品化过程中，团队最常见的失败模式并非计算错误，而是埋点过晚。团队在首发智能体时把成本归因推迟到“有流量之后”，然后花整整一个季度回溯性地将 CloudWatch 日志与客户记录关联，才能搞清楚毛利率为何下降了四个百分点。等到数据可读时，与失控租户之间的定价对话已经变得尴尬。
- 本文识别出三种几乎涵盖所有生产成本事故的根因模式：
- **均值掩盖分布**：按客户平均成本报告会掩盖长尾分布，即 3% 的租户消耗了 60% 的 token。没有分位数报告，定价团队实际上是在对着虚构数据做优化。
- 本文的方法主线是一个由八个模块组成的生产级成本归因技术栈，可概括为：先分账、再归因、后计价、上报、报告、保护、定价、排错。
- ### 四层 Token 分账
每个智能体请求消耗的四层 token 必须在编排层拆分，而不是依赖供应商返回的合并输入计数：
- **提示词层**：系统提示词 + 用户输入 + 少样本示例。通常是单次请求中最大的固定成本，也是缓存收益最大的层。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md)
