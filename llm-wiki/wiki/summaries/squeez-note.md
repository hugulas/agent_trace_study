# Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents

## Source

- Raw note: `raw/notes/squeez_note.md`
- Metadata: not available in note

## Compiled Summary

编程智能体反复消耗冗长的工具观测结果，尽管每次观测中只有很小一部分对下一步决策真正重要。本文研究任务驱动的工具输出裁剪：给定一个聚焦的查询和一份工具输出，返回智能体下一步应当检查的最小逐字证据块。我们构建了一个包含11477个样本的基准数据集，数据来源于SWE-bench代码仓库交互记录以及合成的多生态系统工具输出，其中测试集包含618个经人工筛选的样本。我们使用LoRA对Qwen 3.5 2B进行微调，并将其与更大的零样本模型以及启发式裁剪基线进行比较。我们的模型在召回率达到0.86、F1达到0.80的同时，移除了92%的输入token，在召回率上超过零样本Qwen 3.5 35B A3B达11个百分点，并以显著优势优于所有启发式

## Evidence Notes

- 编程智能体在工作流程中需要反复处理文件读取、grep命中、堆栈跟踪、构建日志、API响应和版本控制历史等工具输出。然而，在这些冗长观测中，仅有一小部分token与下一步决策相关，智能体却常常被迫重读完整输出。这使得裁剪成为智能体系统的核心效率问题。本文研究一个具体而实用的子问题：给定一个聚焦查询和一份工具输出，返回智能体下一步应当检查的最小逐字证据块。该任务的目标并非直接解决问题，而是在保留相关证据的同时丢弃无关内容。这一设定与通用提示压缩和文档级检索压缩存在本质区别，后者通常面向散文文档或检索段落，而非混合格式的工具输出；同时也有别于抽象式摘要，因为摘要重写内容而非保留原始逐字证据。
- 本文提出的Squeez-2B基于Qwen 3.5 2B进行LoRA微调。所有生成式基线使用相同的提示格式，即query与tool output配对的结构。微调后的模型通过vLLM部署，也可作为命令行过滤器直接处理管道化工具输出。这种轻量级预处理方式允许现有编程智能体在不改变核心规划逻辑的前提下，将裁剪步骤插入到下一次推理之前。
- ### 机制流程
1.
- 在618个样本的保留测试集上，Squeez-2B在所有系统中取得最高召回率0.86，同时保持0.92的压缩率。其主要指标为：精确率0.80、F1分数0.80、严格F1为0.79、精确匹配率为0.49。与18倍参数量的零样本模型Qwen 3.5 35B A3B相比，Squeez-2B在召回率上高出11个百分点；与未微调的同规模基线Qwen 3.5 2B相比，召回率高出33个百分点。Squeez-2B不仅是召回率最高的系统，也是精确率最高的系统，表明它学到了工具专用的提取策略，而非单纯的通用指令遵循。
- 在59个负例样本上，Squeez-2B有80%的概率正确返回空输出，而Qwen 3.5 35B A3B仅有7%。这显示专用微调显著提升了模型识别无关观测的能力。

## Wiki Connections

- Concepts: [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
