---
title: "SpikeLab: Agentic tools for spike data analysis"
title_zh: SpikeLab：用于脉冲数据分析的智能体工具
authors: "Van der Molen, T., Cheney, L., Hussain, K., Brahme, O., Robbins, A., Lim, M., Spaeth, A., Geng, J., Parks, D., Kosik, K., Teodorescu, M., Haussler, D., Sharf, T."
date: 2026-04-29
pdf: "https://www.biorxiv.org/content/10.64898/2026.04.25.720833v1.full.pdf"
tags: ["query:tpp-es"]
score: 6.5
evidence: 用于神经脉冲数据分析和事件相关任务的代理工具
tldr: 针对大语言模型在神经科学分析中易产生方法性错误和不可重复结果的问题，本文提出了SpikeLab。这是一个专为神经脉冲数据设计的文本到分析框架，通过结合可组合数据结构与受限自主权的智能体系统，强制使用专家验证的方法并要求在歧义时寻求澄清。实验证明，SpikeLab在多项电生理任务中表现优于原生模型，实现了跨物种、跨场景的高可靠性自动化分析。
source: biorxiv
selection_source: fresh_fetch
motivation: 解决大语言模型在科学研究中因缺乏领域特定结构而导致的分析错误、决策不透明及结果不可重复等问题。
method: 开发了SpikeLab框架，利用受限自主权的智能体系统和专家验证的技能库，通过自然语言驱动神经脉冲数据的标准化分析。
result: 在电生理数据基准测试中，SpikeLab显著优于原生LLM，成功避免了方法伪造和数据缩减等错误，并验证了其在多种生物样本中的通用性。
conclusion: SpikeLab证明了通过引入领域约束和智能体工具，可以实现复杂神经科学数据的高效、准确且可重复的自动化分析。
---

## 摘要
大语言模型具有变革科学研究与分析的潜力，但若缺乏特定领域的结构，它们会产生隐蔽的方法论错误、未报告的决策以及不可重复的结果。在此，我们介绍了 SpikeLab，这是一个用于神经脉冲数据的“文本到分析”框架，它将可组合的数据结构与基于技能的智能体系统相结合，并实施受限自主性：强制使用经专家审核的方法、正确性优先于效率，以及针对模糊请求寻求澄清。在一项针对电生理数据的受控基准测试中，搭载 SpikeLab 的 Sonnet 4.6 在所有任务中均产生了正确且可重复的结果，其表现优于未经辅助的 Sonnet 以及能力更强的 Opus 4.6，后者表现出确定性的失败，包括临时发明方法、隐蔽的数据缩减以及不一致的实验设计。我们展示了该框架在活体小鼠、人类以及离体脑类器官记录中的通用性，并将其应用于一项药理学剂量反应研究，涵盖了单单元动力学、成对网络结构、爆发级时间序列以及潜在群体状态，所有这些均通过自然语言提示完成，无需编写分析代码。

## Abstract
Large language models have the potential to transform scientific research and analysis, but without domain-specific structure they produce silent methodological errors, unreported decisions, and irreproducible results. Here we present SpikeLab, a text-to-analysis framework for neural spike data that combines composable data structures with a skill-based agentic system enforcing bounded autonomy: mandatory use of expert-vetted methods, correctness over efficiency, and clarification-seeking on ambiguous requests. In a controlled benchmark on electrophysiology data, Sonnet 4.6 with SpikeLab produced correct and reproducible results across all tasks, outperforming both the unassisted Sonnet and the more capable Opus 4.6, which exhibited deterministic failures including ad hoc method invention, silent data reduction, and inconsistent experimental designs. We demonstrate versatility across in vivo mouse, human, and in vitro brain organoid recordings, and apply the framework to a pharmacological dose-response study spanning single-unit dynamics, pairwise network structure, burst-level temporal sequences, and latent population states, all through natural language prompts without writing analysis code.