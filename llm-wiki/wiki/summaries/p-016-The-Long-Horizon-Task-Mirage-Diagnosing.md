# The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break

## Source

- Raw note: `raw/notes/p-016_The_Long-Horizon_Task_Mirage_Diagnosing_.md`
- 作者: Xinyu Jessica Wang, Haoyue Bai, Yiyou Sun, Haorui Wang, Shuibai Zhang, Wenjie Hu, Mya Schroder, Bilge Mutlu, Dawn Song, Robert D. Nowak
- 年份: 2026
- 来源: arXiv preprint
- DOI: 10.48550/arXiv.2604.11978
- 证据质量: medium
- PDF: [p-016]-horizon-the-long-horizon-task-mirage-diagnosing-where-and-wh.pdf

## Compiled Summary

大语言模型智能体在短程和中程任务上表现强劲，但在需要长时间、相互依赖动作序列的长程任务上经常崩溃。尽管智能体系统发展迅速，这些长程失败模式仍然缺乏系统刻画，阻碍了对失败原因的有原则诊断以及跨领域的公平比较。为填补这一空白，本文提出 HORIZON，一个初始的跨领域诊断基准，用于系统性地构造任务并分析基于大语言模型的智能体的长程失败行为。利用 HORIZON，作者评估了来自多个模型家族的最先进智能体，在四个代表性智能体领域中收集了 3100 余条轨迹，研究随任务视界延长而产生的性能退化模式。此外，作者提出了一种基于轨迹的大语言模型裁判流程，用于可扩展且可复现的失败归因，并通过人工标注轨迹进行了验证，取得了高度一致性（标注者间 $\ka

## Evidence Notes

- 本文围绕两个核心研究问题展开：
- **RQ1（Where）**：随着任务视界增加，智能体在何处出现崩溃？即性能退化的转折区域（breaking region）出现在什么位置，不同领域间有何差异？
- **RQ2（Why）**：这些失败为何产生？即长程任务中的失败模式如何随视界增长而发生组成变化？
现有研究的碎片化使得上述问题难以回答：领域专用基准的视界定义互不兼容，评估往往只报告聚合成功率，缺乏轨迹级失败归因，导致跨领域比较和系统性诊断缺乏共同基础。此外，长程行为本质上是领域依赖的——例如，具身智能体可能在仅需少量连续动作的任务上就出现断崖式崩溃，而网页导航智能体在同等步数下仍保持稳健——这使得单一普适的"断裂点"定义不可能存在。
- HORIZON 的整体方法可概括为"度量–扩展–归因"三步闭环：
- **统一度量**：用 $H^*$ 和 $s$ 为不同领域任务提供可比的结构化复杂度指标；
- **受控扩展**：通过深度或广度扩展系统性地增加任务视界，构造嵌套任务集（层级 $h+1$ 包含层级 $h$ 的全部任务并增加更长执行需求），确保相邻层级间的比较是受控的；
- **轨迹归因**：对失败轨迹应用七维分类体系进行结构化标注，通过大语言模型裁判实现规模化，并以人工标注验证可靠性。
- ### 机制流程
![Fig.
- ### 主结果：性能随视界的非线性退化
![Fig.
- 3 模型性能随视界扩展的变化](p-016_The_Long-Horizon_Task_Mirage_Diagnosing_/images/fig3_horizon_performance.png)
*图 3：当前模型性能随视界扩展的变化。图中展示成功率与组合深度 $s$ 的关系，每个数据点报告三次独立运行的均值，误差条为标准差。评估覆盖 GPT-5-mini 与 Claude-4-Sonnet 在所有四个领域上的表现。*
如图 3 所示，跨所有领域观察到三个一致的退化模式：
- **性能随 $s$ 非线性下降**：在较小 $s$ 时成功率相对稳定或缓慢下降，并非与每增加一个子任务成比例衰减；
- **超过小 $s$ 后出现断崖式下

## Wiki Connections

- Concepts: [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md)
- Entities: None identified
