---
title: "DualTimesField: Rethinking Time Series as Continuous-Time Trends and Events"
title_zh: DualTimesField：将时间序列重新思考为连续时间趋势与事件
authors: "Wencheng Zhang, Long Li, Huayi Qin, Zongjuan Wu, Jing Li, Wanghu Chen"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/ab0b0c0d2553a91e8e698a2d28c74ef5e3f9221d.pdf"
tags: ["query:tpp-es"]
score: 6.0
evidence: 连续时间下的趋势与离散事件表示
tldr: 该工作针对离散时间表示难以处理不规则采样、而传统隐式神经表示存在谱偏置与频率纠缠的问题。作者从连续时间视角将时间序列重新概念化为平滑趋势与离散事件的叠加，提出DualTimesField双隐式神经场框架。其连续时间场以带限参数化刻画平滑趋势，离散几何场建模瞬态事件。方法为不规则采样的连续时间事件序列分析与表示提供了新工具，对连续时间事件建模具有借鉴价值。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 离散时间表示难以应对不规则采样，隐式神经表示又存在谱偏置与频率纠缠。
method: 提出DualTimesField框架，用连续时间场建模平滑趋势、用离散几何场建模瞬态事件的双隐式神经场方法。
result: 该框架从连续时间视角更好地表示趋势与离散事件，缓解谱偏置并适应不规则采样。
conclusion: 为连续时间事件序列表示提供新范式，可迁移至连续时间事件分析与建模。
---

## Abstract
Effective time series representation is critical for revealing temporal dynamics in many fields. However, existing approaches encounter fundamental limitations. Discrete-time representations struggle with irregular sampling and the tradeoff of fidelity and efficiency, while traditional implicit neural representations suffer from spectral bias and frequency entanglement. To address these challenges, we conceptualize time series as the superposition of continuous trends and discrete events from a continuous-time perspective and propose DualTimesField, a framework that utilizes dual implicit neural fields. Its Continuous Time Field captures smooth trends through bandwidth-limited parameterization, while a Discrete Geometric Field models transient events using learnable Gabor atoms, gated sparsity, and coarse-to-fine scale annealing. This explicit field separation effectively overcomes both limitations. Experiments on nine real-world benchmarks demonstrate substantial improvements in representation fidelity, achieving 51.2% average MSE reduction over discrete-time baselines and competitive interpolation on irregular data. Code is available at https://github.com/WisdomTogether/DualTimesField.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
连续时间下的趋势与离散事件表示。

### 2. 核心内容
该工作针对离散时间表示难以处理不规则采样、而传统隐式神经表示存在谱偏置与频率纠缠的问题。作者从连续时间视角将时间序列重新概念化为平滑趋势与离散事件的叠加，提出DualTimesField双隐式神经场框架。其连续时间场以带限参数化刻画平滑趋势，离散几何场建模瞬态事件。方法为不规则采样的连续时间事件序列分析与表示提供了新工具，对连续时间事件建模具有借鉴价值。

### 3. 对应检索需求
continuous-time event sequence analysis。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=w6pabBPG7D](https://openreview.net/forum?id=w6pabBPG7D)
