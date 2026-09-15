---
title: Nested Spatio-Temporal Time Series Forecasting
title_zh: 嵌套式时空时间序列预测
authors: "YingHao Ai, Yukai Zhou, Ruoxi Jiang, Junyi An, Chao Qu, Zhijian Zhou, Shiyu Wang, Fenglei Cao, Zenglin Xu, Furao Shen, Yuan Qi"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/b1fdb152a8b7d6ed58c6557e6db99d08b5215b51.pdf"
tags: ["query:tpp-es"]
score: 4.0
evidence: 时空预测建模
tldr: 针对交通等时空预测任务中高噪声条件下时序相关性演化与系统性误差难以建模的问题，本文提出嵌套预测框架，通过谱聚类构造语义一致区域，并用渐进式由粗到细预测器将宏观区域趋势注入节点级预测。实验表明该方法在细粒度节点预测上取得更高精度。该工作为时空数据的宏观微观耦合建模提供了思路，但与点过程的事件强度建模仍属不同范式。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 时空预测在高噪声下难以捕捉演化时序相关性与系统性误差。
method: 提出嵌套框架，用谱聚类构造区域并以由粗到细预测器注入宏观动态。
result: 在节点级时空预测任务上取得更优精度。
conclusion: 为时空数据的宏观微观耦合预测提供了有效范式。
---

## Abstract
Spatio-temporal forecasting is critical for real-world applications like traffic management, yet capturing complex interactions under high-noise conditions remains challenging. While current methods have shown improved accuracy using spatial physical priors, they often struggle with evolving temporal correlations and systematic errors. In this work, we propose a nested forecasting framework that couples future macro-level regional trends with micro-level historical observations, enabling top-down guidance from abstract future representations for fine-grained forecasting. Specifically, we construct semantically coherent regions via spectral clustering and design a progressive coarse-to-fine predictor to inject macro-dynamics into node-level forecasting. Extensive experiments on multiple real-world datasets demonstrate that our method consistently outperforms state-of-the-art baselines, validating the effectiveness of future macro-guided nested forecasting.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
时空预测建模。

### 2. 核心内容
针对交通等时空预测任务中高噪声条件下时序相关性演化与系统性误差难以建模的问题，本文提出嵌套预测框架，通过谱聚类构造语义一致区域，并用渐进式由粗到细预测器将宏观区域趋势注入节点级预测。实验表明该方法在细粒度节点预测上取得更高精度。该工作为时空数据的宏观微观耦合建模提供了思路，但与点过程的事件强度建模仍属不同范式。

### 3. 对应检索需求
spatio-temporal point process for events with locations and time。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=x5xKTcGemE](https://openreview.net/forum?id=x5xKTcGemE)
