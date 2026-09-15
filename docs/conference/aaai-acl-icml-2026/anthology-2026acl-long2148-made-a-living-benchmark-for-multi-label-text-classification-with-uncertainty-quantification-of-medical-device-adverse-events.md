---
title: "MADE: A Living Benchmark for Multi-Label Text Classification with Uncertainty Quantification of Medical Device Adverse Events"
title_zh: MADE：面向医疗器械不良事件多标签分类与不确定性量化的活体基准
authors: "Raunak Agarwal, Markus A. Wenzel, Simon Baur, Jonas Zimmer, George Harvey, Jackie Ma"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.acl-long.2148.pdf"
tags: ["query:ehr-es"]
score: 5.0
evidence: 高风险医疗多标签分类中的不确定性量化
tldr: 在高风险医疗领域，机器学习不仅需要强预测性能，还需可靠的不确定性量化以支持人工监督，而现有多标签文本分类基准日益饱和且可能受数据污染影响。本文提出MADE，一个基于医疗器械不良事件报告构建并持续更新的活体多标签分类基准，强调不确定性量化评估。该基准可缓解记忆化问题，更真实地区分模型的推理能力，为可信医疗预测研究提供可靠的评测平台。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long2148/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 1320, \"height\": 570}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long2148/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 1948, \"height\": 388}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long2148/fig-003.webp\", \"caption\": \"\", \"page\": 5, \"index\": 3, \"width\": 1897, \"height\": 885}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long2148/fig-004.webp\", \"caption\": \"\", \"page\": 5, \"index\": 4, \"width\": 8692, \"height\": 4346}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long2148/fig-005.webp\", \"caption\": \"\", \"page\": 5, \"index\": 5, \"width\": 8692, \"height\": 4346}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long2148/fig-006.webp\", \"caption\": \"\", \"page\": 6, \"index\": 6, \"width\": 2622, \"height\": 1837}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long2148/fig-007.webp\", \"caption\": \"\", \"page\": 8, \"index\": 7, \"width\": 2151, \"height\": 1723}]"
motivation: 高风险医疗多标签分类需要可靠的不确定性量化，但现有基准趋于饱和且可能受数据污染影响。
method: 提出MADE活体基准，基于医疗器械不良事件报告构建并持续更新，专门评测多标签分类与不确定性量化。
result: 该基准通过持续更新缓解记忆化问题，更真实地区分模型的推理能力与泛化表现。
conclusion: MADE为可信医疗预测与不确定性量化研究提供了可持续的评测基础。
---

## Abstract
Machine learning in high-stakes domains such as healthcare requires not only strong predictive performance but also reliable uncertainty quantification (UQ) to support human oversight. Multi-label text classification (MLTC) is a central task in this domain, yet remains challenging due to label imbalances, dependencies, and combinatorial complexity. Existing MLTC benchmarks are increasingly saturated and may be affected by training data contamination, making it difficult to distinguish genuine reasoning capabilities from memorization. We introduce MADE, a living MLTC benchmark derived from m edical device ad verse e vent reports and continuously updated with newly published reports to prevent contamination. MADE features a long-tailed distribution of hierarchical labels and enables reproducible evaluation with strict temporal splits. We establish baselines across more than 20 encoder- and decoder-only models under fine-tuning and few-shot settings (instruction-tuned/reasoning variants, local/API-accessible). We systematically assess entropy-/consistency-based and self-verbalized UQ methods. Results show clear trade-offs: smaller discriminatively fine-tuned decoders achieve the strongest head-to-tail accuracy while maintaining competitive UQ; generative fine-tuning delivers the most reliable UQ; large reasoning models improve performance on rare labels yet exhibit surprisingly weak UQ; and self-verbalized confidence is not a reliable proxy for uncertainty. Our work is publicly available at https://hhi.fraunhofer.de/aml-demonstrator/made-benchmark.

---

## 论文详细总结（自动生成）

# MADE 论文中文总结

## 1. 核心问题与整体含义

- **研究动机**：医疗等高风险场景中的机器学习不仅要求预测性能强，还要求可靠的不确定性量化（UQ），以便将可疑或模糊样本交由人工复核。多标签文本分类（MLTC）是该场景的核心任务，但面临标签不平衡、标签依赖和组合爆炸等问题。
- **现有基准的不足**：已有 MLTC 基准逐渐饱和，且可能因进入 LLM 预训练语料而受数据污染，难以区分模型是真正推理还是记忆；同时，很多基准缺少真实场景中的长尾分布、层级依赖和严格时间切分。
- **论文整体含义**：作者提出 **MADE**，一个基于美国 FDA 医疗器械不良事件报告构建的“活体”MLTC 基准。它通过持续纳入新发布的报告来避免污染，并提供严格时间划分、层级长尾标签和系统 UQ 评估。论文还建立 20 多个编码器/解码器模型的基线，比较微调、少样本提示和多种 UQ 方法，旨在为可靠医疗 MLTC 提供可复现评测平台。

## 2. 方法论

### 2.1 数据构建：MADE 基准

- **数据来源**：从 FDA openFDA 收集 2015 年至 2025 年中的医疗器械不良事件报告，提取事件描述、事件类型、器械信息，以及产品问题和患者问题标签。
- **标签体系**：将 FDA 标签映射到国际医疗器械监管机构论坛（IMDRF）的三级层级编码；每个具体码向上传播，加入所有祖先码，避免模型因预测有效父类而被惩罚。将产品问题和患者问题标签扁平化为目标标签并集。
- **标签冻结与过滤**：将标签分类体系冻结在 2023 年 12 月，丢弃之后新出现的标签；移除出现次数少于 5 的极罕见标签，最终得到 **1,154 个标签**，呈长尾分布。
- **去重与下采样**：按事件描述去重，只保留首次出现；使用 HDBSCAN 对事件描述嵌入聚类，选择簇代表并保留较高比例稀有标签；所有标记为死亡的事件均保留。
- **时间切分
