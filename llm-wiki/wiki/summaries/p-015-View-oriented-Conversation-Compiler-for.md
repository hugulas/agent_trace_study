# View-oriented Conversation Compiler for Agent Trace Analysis

## Source

- Raw note: `raw/notes/p-015_View-oriented_Conversation_Compiler_for_.md`
- 作者: Lvmin Zhang, Maneesh Agrawala
- 年份: 2026
- 来源: ArXiv.org
- DOI: 10.48550/arXiv.2603.29678
- 证据质量: high
- PDF: [p-015]-vcc-view-oriented-conversation-compiler-for-agent-trace-anal.pdf

## Compiled Summary

智能体轨迹在智能系统与上下文工程中承载着日益增长的解析价值，然而大多数现有工作将对话格式视为微不足道的实现细节。

## Evidence Notes

- 现代智能体会话却包含深层结构化内容——嵌套工具调用与结果、思维链推理块、子智能体调用、上下文窗口压缩边界以及工具注入的系统指令——其复杂度远超简单的用户与助手交换。
- 上下文学习研究长期关注高层架构选择：生成器、反射器与策展人的角色分解，层次化记忆的组织与检索，工具使用，以及从智能体轨迹中提取经验并泛化。
- 然而，消息本身的格式——即智能体轨迹如何被表示并呈现给大语言模型进行分析——在很大程度上被当作微不足道的实现细节，纯文本、JSON、YAML 与 grep 成为默认惯例。
- VCC 将原始智能体 JSONL 日志编译为结构化视图。
- 其核心并非单层格式转换（如 JSON 转 Markdown），而是执行完整的编译器流水线，并包含大量轨迹特定的变换：
- 工具调用参数从转义 JSON 编译为可读 YAML，使用块标量处理多行值。

## Wiki Connections

- Concepts: [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [Claude Code](entities/Claude-Code.md), [Codex CLI](entities/Codex-CLI.md)
