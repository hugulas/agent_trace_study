# FLARE: Faithful Logic-Aided Reasoning and Exploration

## Source

- Raw note: `raw/notes/p-028_FLARE_Faithful_Logic-Aided_Reasoning_and.md`
- Metadata: not available in note

## Compiled Summary

现代问答与推理方法普遍采用大语言模型的思维链提示，但其最终输出往往与中间推理链不一致。

## Evidence Notes

- 神经符号方法（如 Faithful CoT）虽然借助外部求解器可获得更高的忠实度，却需要代码专用模型，并且难以处理模糊任务。
- 当前大模型推理面临的核心矛盾是：思维链等自然语言中间链虽灵活，但模型输出常背离这些链（不忠实）；神经符号方法虽忠实，却要求代码专用模型与严格可执行的形式化，无法处理需要常识与软推理的模糊问题。
- 因此，本文试图回答：如何在保持形式化结构以度量产出的同时，让通用大模型也能进行可靠的多跳软推理，并自动诊断其中的不一致？
- FLARE 包含三个顺序生成的模块：计划、代码与模拟搜索。
- 给定自然语言查询，模型在逐步累积的少样本上下文支持下依次完成各模块，最终得到答案。

## Wiki Connections

- Concepts: [[concepts/trace-schema-and-telemetry-standards]]
- Entities: None identified
