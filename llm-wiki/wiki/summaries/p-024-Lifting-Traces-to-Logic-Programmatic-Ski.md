# Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks

## Source

- Raw note: `raw/notes/p-024_Lifting_Traces_to_Logic_Programmatic_Ski.md`
- 作者: Jie-Jing Shao, Haiyan Yin, Yueming Lyu, Xingrui Yu, Lan-Zhe Guo, Ivor W. Tsang, James T. Kwok, Yu-Feng Li
- 年份: 2026
- 来源: ICML 2026 / ArXiv 2605.01293
- DOI: 10.48550/arXiv.2605.01293
- 证据质量: high

## Compiled Summary

由基础模型驱动的智能体在进行长程规划时常常陷入困境，因为基于纯提示的推理具有瞬时性，难以积累稳定的执行策略。现有的技能归纳方法通过将经验蒸馏为无状态的参数化脚本来缓解这一问题，但这些脚本无法捕捉动态环境中执行所需的条件逻辑。本文提出神经符号技能归纳（NSI），一种将交互轨迹提升为模块化、逻辑 grounding 程序的框架。NSI 通过显式合成控制流与动态变量绑定，使智能体能够自主发现“何时行动”以及“为何行动”。该范式实现了高效泛化，允许智能体从少样本示例中归纳技能，并灵活适应未见过的目标。在一系列智能体任务上的实验表明，NSI 持续优于当前最优基线，使智能体能够自我演进为逻辑 grounding 技能的架构师。

## Evidence Notes

- 当前 LLM 驱动的智能体虽然具备感知、推理与行动能力，但在特定真实世界领域往往缺乏 grounding 知识，导致领域特定的推理缺口，表现为工具使用不可靠与长程规划失败。为弥合通用能力与任务需求之间的鸿沟，智能体需要通过环境交互进行自我演进。
- 技能归纳是这一演进的核心范式，它利用智能体任务的交互本质，从经验中提取可复用、可执行的程序。然而，现有方法通常将技能诱导为无状态的参数化脚本（例如“打开(容器) → 拾取(对象)”），这些脚本无视环境状态变化，无法忠实表达底层执行逻辑。如图 1 所示，在执行“打开冰箱”后，理想的执行逻辑应检查目标对象是否存在：若存在，则动态绑定并拾取；若不存在，则分支到别处搜索。这种条件逻辑是传统参数化脚本无法表达的。
- NSI 的核心思想是将技能从静态脚本重新定义为动态的、逻辑 grounding 的工作流。整个框架包含三个层次：神经符号表示、离线归纳与在线演进。
- **神经符号技能表示**：每个技能被形式化为三元组，分别对应调用参数、神经 grounding 模块与符号执行图。具体形式如下：
$$
\pi_\omega = (\theta_\omega, \phi_\omega, G_\omega)
$$
神经 grounding 模块由 LLM 担任语义感知器，将原始观测转换为结构化的符号状态 $Z_t$；符号执行图 $G_\omega$ 则由符号解释器执行，基于条件确定性控制执行流程。
- 实验在三个智能体基准上进行：ALFWorld（具身家居任务，134 个测试实例）、WebShop（电商网页导航，评估购买成功率与奖励分）、TextCraft（Minecraft 合成递归任务，200 个深度 2–4 的未见任务）。所有技能归纳方法使用 GPT-4o 作为主干模型，温度设为 0，报告 3 次运行的均值 ± 标准差。
- 来自 LaTeX 源码 `nesy_skill.tex` 的 Table 1：
**Table 1.

## Wiki Connections

- Concepts: [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md)
- Entities: None identified
