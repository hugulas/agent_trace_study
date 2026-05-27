# Why Do Multi-Agent LLM Systems Fail?

## Source

- Raw note: `raw/notes/p-021_Why_Do_Multi_Agent_LLM_Systems_Fail.md`
- 作者: Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Keutzer, Aditya Parameswaran, Dan Klein, Kannan Ramchandran, Matei Zaharia, Joseph E. Gonzalez, Ion Stoica
- 年份: 2025
- DOI: 10.3362/9781780441061.013
- arXiv: 2503.13657
- 证据质量: high

## Compiled Summary

尽管多智能体大语言模型系统（MAS）受到广泛关注，但它们在主流基准测试上的性能提升往往微乎其微。

## Evidence Notes

- 这一差距凸显了对 MAS 失效原因进行系统性理解的迫切需求。
- 本文提出的核心问题是：**为什么多智能体大语言模型系统会失败？**
研究将失败定义为「多智能体系统未能达成其预期任务目标」的实例。动机来源于以下观察：尽管多智能体系统在软件工程、药物发现、科学模拟和通用智能体等领域被广泛探索，但它们在流行基准上的性能增益往往微乎其微，甚至不如单智能体框架或简单的 best-of-N 采样基线。作者在 7 个开源系统上测得 41% 至 86.7% 的失败率，且社区对如何构建稳健可靠的系统缺乏共识。
- 该问题的挑战性在于：失败的根因检测难以验证真实标签，且缺乏标准化的失败定义框架。这要求研究者不仅要识别表面错误，还需理解系统动态与智能体交互的深层机制。
- ### 机制流程
本文构建数据集的方法包含以下关键步骤：
1.
- **收集初始轨迹并执行开放式编码**：从 5 个框架（HyperAgent、AppWorld、AG2、ChatDev、MetaGPT）收集 150 条轨迹，由 6 名专家采用扎根理论方法进行逐行分析，通过理论采样确保覆盖不同系统目标与交互模式。

## Wiki Connections

- Concepts: [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md)
- Entities: None identified
