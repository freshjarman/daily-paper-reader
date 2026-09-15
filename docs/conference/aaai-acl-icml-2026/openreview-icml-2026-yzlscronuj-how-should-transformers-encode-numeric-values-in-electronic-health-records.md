---
title: How Should Transformers Encode Numeric Values in Electronic Health Records?
title_zh: Transformer应如何编码电子健康记录中的数值？
authors: "Maria Elkjær Montgomery, Christian Igel, Mikkel Fruelund Odgaard, Martin Sillesen, Mads Nielsen"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/09c27a6364174159b7adc19e21f245e2400437dd.pdf"
tags: ["query:ehr-es"]
score: 7.0
evidence: 在基于Transformer的电子健康记录序列处理中编码数值
tldr: 在电子健康记录等序列处理中，如何用Transformer编码数值仍缺乏系统认识。本文对比离散、连续与混合三类数值编码策略，利用嵌入真实EHR的合成算术任务及真实临床预测任务进行评测。结果显示显式建模数值-概念交互的方法在精度敏感任务上最优，而保留数值并先分箱再投影的混合token方案更稳健通用。该研究为EHR序列建模的数值表示提供了实证指导。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: Transformer处理EHR等序列时如何编码数值尚不明确，不同策略的取舍缺乏系统比较。
method: 对比离散、连续与混合数值编码策略，并用嵌入真实EHR的合成算术任务与真实临床预测任务评测。
result: 显式数值-概念交互法在精度敏感任务最优，混合token方案更稳健通用。
conclusion: 研究为EHR序列建模中的数值表示选择提供了实证指导。
---

## Abstract
How do we encode numeric values in transformer-based sequence processing, particularly in electronic health record (EHR) data? We systematically compare discrete, continuous, and hybrid value encoding strategies using synthetic arithmetic tasks embedded within real-world EHR data, as well as real-world clinical prediction tasks. Our study reveals trade-offs between numeric precision, optimisation stability, and architectural flexibility. We find that approaches that explicitly model value-concept interactions perform best on precision-sensitive arithmetic tasks when architectural constraints permit. Hybrid token-based approaches that retain numeric values but apply binning prior to projection provide a more robust and broadly applicable alternative, with the optimal number of bins following a simple empirically derived power-law in dataset size. Across tasks, models consistently exhibit reliable “good enough” numeric computation rather than exact arithmetic, while clinical gains from incorporating laboratory values are task-dependent. This suggests that robustness and deployability often outweigh maximal numeric precision in practice, motivating hybrid token-based approaches as a practical default.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
在基于Transformer的电子健康记录序列处理中编码数值。

### 2. 核心内容
在电子健康记录等序列处理中，如何用Transformer编码数值仍缺乏系统认识。本文对比离散、连续与混合三类数值编码策略，利用嵌入真实EHR的合成算术任务及真实临床预测任务进行评测。结果显示显式建模数值-概念交互的方法在精度敏感任务上最优，而保留数值并先分箱再投影的混合token方案更稳健通用。该研究为EHR序列建模的数值表示提供了实证指导。

### 3. 对应检索需求
electronic health record sequence modeling。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=YzlscRoNUj](https://openreview.net/forum?id=YzlscRoNUj)
