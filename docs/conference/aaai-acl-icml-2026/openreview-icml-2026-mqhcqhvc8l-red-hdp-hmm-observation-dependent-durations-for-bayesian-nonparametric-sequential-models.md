---
title: "RED-HDP-HMM: Observation-Dependent Durations for Bayesian Nonparametric Sequential Models"
title_zh: RED-HDP-HMM：面向贝叶斯非参数序列模型的观测依赖时长
authors: "Mikołaj Słupiński, Piotr Lipinski"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/2a56f88a43dabfba81d52cb6b677c97d0c74ae0a.pdf"
tags: ["query:tpp-es"]
score: 5.0
evidence: 面向时空数据的显式时长贝叶斯非参数序列模型
tldr: 该工作针对HDP-HMM及其半马尔可夫扩展假设状态时长平稳、限制表达力的问题，提出递归显式时长HDP-HMM模型RED-HDP-HMM。方法引入递归的显式时长建模并设计Gibbs采样实现高效推断。实验在合成与真实分割数据上验证了模型更强的灵活性。该工作属于序列建模的方法论桥接，与时间点过程主题相关但并非直接的点过程强度建模。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: HDP-HMM及其半马尔可夫扩展假设状态时长平稳，限制了模型表达力。
method: 引入递归显式时长建模构建RED-HDP-HMM，并用Gibbs采样进行高效推断。
result: 在合成与真实分割数据上展现出更强且更灵活的建模能力。
conclusion: 属序列建模方法论桥接，与点过程主题相关但非直接的强度建模。
---

## Abstract
The Hierarchical Dirichlet Process Hidden Markov Model (HDP-HMM) is a Bayesian nonparametric extension of the classical Hidden Markov Model, well-suited for learning from (spatio-)temporal data. To relax the restrictive geometric assumption on state durations, the HDP Hidden Semi-Markov Model was introduced. However, both models assume stationary state durations, which limits their expressive power. In this work, we extend the HDP-HMM framework by incorporating recurrent explicit duration modeling, resulting in a more general and flexible model: the Recurrent Explicit Duration HDP-HMM (RED-HDP-HMM). We propose a Gibbs sampling method for efficient inference in this model. Empirical results on both synthetic and real-world segmentation tasks demonstrate that RED-HDP-HMM consistently outperforms the disentangled sticky HDP-HMM and the standard sticky HDP-HMM.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
面向时空数据的显式时长贝叶斯非参数序列模型。

### 2. 核心内容
该工作针对HDP-HMM及其半马尔可夫扩展假设状态时长平稳、限制表达力的问题，提出递归显式时长HDP-HMM模型RED-HDP-HMM。方法引入递归的显式时长建模并设计Gibbs采样实现高效推断。实验在合成与真实分割数据上验证了模型更强的灵活性。该工作属于序列建模的方法论桥接，与时间点过程主题相关但并非直接的点过程强度建模。

### 3. 对应检索需求
temporal point process model and inference。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=MqhcqHVc8l](https://openreview.net/forum?id=MqhcqHVc8l)
