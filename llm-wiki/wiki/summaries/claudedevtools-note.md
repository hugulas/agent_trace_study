# claude-devtools: Open-Source DevTools for Claude Code

## Source

- Raw note: `raw/notes/claudedevtools_note.md`
- Metadata: not available in note

## Compiled Summary

claude-devtools 是 Claude Code 的调试工具。它读取本地机器上已保存的 Claude Code 日志和会话转录（位于 .claude 目录），并重构所有隐藏信息。

## Evidence Notes

- 自 v2.1.20 版本起，Claude Code 用不透明摘要替代了详细输出：只显示「读取 3 个文件」「搜索 1 个模式」「编辑 2 个文件」，没有文件路径、没有内容、没有行号。思维链推理完全不可见；工具调用的实际输入输出被折叠；子代理的活动只展示最终结果；上下文窗口仅用三段进度条表示，没有任何明细。唯一的替代方案是 --verbose，但它会输出原始 JSON、内部系统提示和数千行噪音，没有中间地带。
- Claude Code 作为终端内的智能编码助手，在 v2.1.20 之后将详细的执行输出替换为高度压缩的摘要。这种设计虽然降低了终端噪音，却造成了严重的可观测性缺口：
- 开发者无法查看工具调用的实际参数和返回内容
- 思维链和扩展思考完全不可见
- 子代理的层级调用关系和各自成本无迹可寻
- 上下文窗口的消耗构成仅以三段进度条呈现，无法诊断膨胀原因
- 团队消息、任务委托和关闭请求被埋没
唯一的原生替代方案 --verbose 输出原始 JSON 和系统提示，信息过载严重。因此，核心问题是：如何在零侵入、零配置的前提下，为 Claude Code 提供结构化、可导航、可过滤的调试界面？
> [!figure] Fig.
- 1: 上下文压缩可视化与七维归因界面示意图
> 建议位置：研究问题 / 数据与任务定义 / 方法主线 / 关键结果 / 深度分析 / 局限 / 我的笔记
> 放置原因：展示工具的核心可视化能力，帮助理解七维归因和压缩可视化的交互方式
> 当前状态：占位符
- claude-devtools 的核心设计是被动日志解析器而非主动拦截器。它利用 Claude Code 已经持久化到磁盘的日志数据，在后处理阶段重建完整的执行历史。
- ### 机制流程
1.

## Wiki Connections

- Concepts: [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [Langfuse](entities/Langfuse.md), [Helicone](entities/Helicone.md), [Claude Code](entities/Claude-Code.md)
