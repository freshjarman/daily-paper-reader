---
title: Privately Fine-Tuned LLMs Preserve Temporal Dynamics in Tabular Data
title_zh: 隐私微调的大语言模型保留表格数据中的时间动态
authors: "Lucas Rosenblatt, Peihan Liu, Ryan McKenna, Natalia Ponomareva"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/a3431ae1ce982bee3145b80a063f60c678f01e03.pdf"
tags: ["query:ehr-es"]
score: 7.0
evidence: 生成式框架保留纵向EHR表格数据的时间动态
tldr: 现有差分隐私合成表格数据研究多假设行独立同分布，忽略了电子健康记录等纵向数据中由同一患者贡献的序列事件的时间复杂性。本文提出PATH生成式框架，将整张事件表作为生成单元以保留时间连贯性，并指出扁平化历史向量无法维持时序一致性。实验验证其在保持有效边际分布的同时更好地保留时间动态。该工作对EHR生成模型与患者轨迹合成具有直接参考价值。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 差分隐私合成表格数据多忽略纵向EHR中序列事件的时间复杂性，扁平化建模会破坏时序连贯性。
method: 提出PATH生成式框架，将整张纵向事件表作为生成单元，保留患者序列事件的时间动态。
result: 在维持有效边际分布的同时，比扁平化方法更好地保留EHR的时间连贯性。
conclusion: 为隐私保护下的EHR事件流生成与患者轨迹合成提供了可行方案。
---

## Abstract
Research on differentially private synthetic tabular data has largely focused on independent and identically distributed rows where each record corresponds to a unique individual. This perspective neglects the temporal complexity in longitudinal datasets, such as electronic health records, where a user contributes an entire (sub) table of sequential events. While practitioners might attempt to model such data by flattening user histories into high-dimensional vectors for use with standard marginal-based mechanisms, we demonstrate that this strategy is insufficient. Flattening fails to preserve temporal coherence even when it maintains valid marginal distributions. We introduce PATH, a novel generative framework that treats the full table as the unit of synthesis and leverages the autoregressive capabilities of privately fine-tuned large language models. Extensive evaluations show that PATH effectively captures long-range dependencies that traditional methods miss. Empirically, our method reduces the distributional distance to real trajectories by over 60% and reduces state transition errors by nearly 50% compared to leading marginal mechanisms while achieving similar marginal fidelity.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
生成式框架保留纵向EHR表格数据的时间动态。

### 2. 核心内容
现有差分隐私合成表格数据研究多假设行独立同分布，忽略了电子健康记录等纵向数据中由同一患者贡献的序列事件的时间复杂性。本文提出PATH生成式框架，将整张事件表作为生成单元以保留时间连贯性，并指出扁平化历史向量无法维持时序一致性。实验验证其在保持有效边际分布的同时更好地保留时间动态。该工作对EHR生成模型与患者轨迹合成具有直接参考价值。

### 3. 对应检索需求
electronic health records generation models。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=hZJAUJ5l9t](https://openreview.net/forum?id=hZJAUJ5l9t)
