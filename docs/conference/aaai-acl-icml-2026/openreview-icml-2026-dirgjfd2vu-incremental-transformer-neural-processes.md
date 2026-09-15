---
title: Incremental Transformer Neural Processes
title_zh: 增量式Transformer神经过程
authors: "Philip Mortimer, Cristiana Diaconu, Tommy Rochussen, Bruno Kacper Mlodozeniec, Richard E. Turner"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/1d95be813abd1061a98747476fbba3e698bca88d.pdf"
tags: ["query:tpp-es"]
score: 5.0
evidence: 神经过程处理连续数据流与时空序列预测
tldr: 现有Transformer神经过程在实时传感器读数等连续数据流场景下，每次新观测都需从头重算内部表示，缺乏廉价的增量更新能力。本文提出增量式TNP，借鉴大语言模型引入因果掩码、键值缓存与数据高效自回归训练策略。实验表明其性能与标准TNP相当，同时支持高效的在线增量更新。该工作为流式连续观测的序列建模提供了可迁移的增量推理方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有Transformer神经过程在连续数据流中缺乏廉价增量更新能力，难以适应实时观测场景。
method: 借鉴大语言模型，采用因果掩码、键值缓存与数据高效的自回归训练策略构建增量式TNP。
result: 在时空预测等任务上匹配原有TNP的性能，并支持对新观测的高效增量更新。
conclusion: 为流式连续观测的序列建模提供了可迁移的高效增量推理方案。
---

## Abstract
Neural Processes (NPs), and specifically Transformer Neural Processes (TNPs), have demonstrated remarkable performance across tasks ranging from spatiotemporal forecasting to tabular data modelling. However, many of these applications are inherently sequential, involving continuous data streams such as real-time sensor readings or database updates. In such settings, models should support cheap, incremental updates rather than recomputing internal representations from scratch for every new observation—a capability existing TNP variants lack. Drawing inspiration from Large Language Models, we introduce the Incremental TNP ($\texttt{incTNP}$). By leveraging causal masking, Key-Value (KV) caching, and a data-efficient autoregressive training strategy, $\texttt{incTNP}$ matches the predictive performance of standard TNPs while reducing the computational cost of updates from quadratic to linear time complexity. We empirically evaluate our model on a range of synthetic and real-world tasks, including tabular regression and temperature prediction. Our results show that, surprisingly, $\texttt{incTNP}$ delivers performance comparable to—or better than—non-causal TNPs while unlocking orders-of-magnitude speedups for sequential inference. Finally, we assess the consistency of the model's updates---by adapting a metric of "implicit Bayesianness", we show that under a one-at-a-time streaming protocol, $\texttt{incTNP}$ retains a prediction rule as implicitly Bayesian as standard non-causal TNPs, demonstrating that $\texttt{incTNP}$ achieves the computational benefits of causal masking without sacrificing the consistency required for streaming inference.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
神经过程处理连续数据流与时空序列预测。

### 2. 核心内容
现有Transformer神经过程在实时传感器读数等连续数据流场景下，每次新观测都需从头重算内部表示，缺乏廉价的增量更新能力。本文提出增量式TNP，借鉴大语言模型引入因果掩码、键值缓存与数据高效自回归训练策略。实验表明其性能与标准TNP相当，同时支持高效的在线增量更新。该工作为流式连续观测的序列建模提供了可迁移的增量推理方案。

### 3. 对应检索需求
continuous-time event sequence analysis。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=diRgjfD2vu](https://openreview.net/forum?id=diRgjfD2vu)
