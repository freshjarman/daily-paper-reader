---
title: Learning Coupled Continuous-Time Latent Dynamics from Irregular Events
title_zh: 从不规则事件中学习耦合的连续时间潜动力学
authors: "Jiankai Zuo, Yang Zhang, Yu Zhang, Jiarui Liang, Yaying Zhang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/e9eb9c533628d2319255745f80c227d50ec80bfb.pdf"
tags: ["query:tpp-es"]
score: 8.0
evidence: 基于不规则事件序列的耦合连续时间潜动力学
tldr: 该工作针对从事件序列建模动态依赖时，个体状态连续演化又受群体动态影响、而现有方法孤立建模或离散近似难以刻画长程不规则与稀疏观测的问题，提出耦合连续时间潜动力学框架CoCLD。方法让个体事件序列与全局分布过程异步交互、连续演化。实验表明其在捕捉长程时间不规则性与稀疏观测上优于离散近似方法。该工作直接推进了连续时间事件序列分析。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 个体状态连续演化又受群体动态影响，现有方法孤立建模或离散近似难以刻画长程不规则。
method: 提出CoCLD框架，让个体事件序列与全局分布过程异步交互并连续演化。
result: 在长程时间不规则性与稀疏观测建模上优于离散近似方法。
conclusion: 直接推进了连续时间事件序列分析与耦合潜动力学建模。
---

## Abstract
Modeling dynamic dependencies from irregularly sampled event sequences is a fundamental challenge in modern machine learning. In many real-world systems, individual-level states evolve continuously over time while being simultaneously influenced by population-level dynamics. However, existing methods typically model these processes in isolation or rely on discrete-time approximations that fail to capture long-range temporal irregularities and sparse observations. This paper studies the problem of learning coupled continuous-time latent dynamics from irregular events, where individual event sequences and global distributional processes evolve asynchronously and interact over time. We propose a Coupled Continuous-Time Latent Dynamics (CoCLD) framework that jointly models individual latent dynamics and population-level distributional shifts, and aligns them in a continuous-time latent space. CoCLD integrates a Diffusion-based Latent Interpolator with neural ordinary differential equations, enabling principled interpolation, generation, and alignment of latent states across arbitrary time points. We show that the proposed coupling mechanism yields a consistent estimator of continuous-time latent dynamics under sparse and irregular observations. Empirical evaluations show CoCLD effectively captures dynamic dependencies and generalizes across tasks like next-event prediction, mobility trajectory generation, and sequential behavior modeling, indicating that learning coupled continuous-time latent dynamics is a powerful paradigm for irregular event sequence modeling.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于不规则事件序列的耦合连续时间潜动力学。

### 2. 核心内容
该工作针对从事件序列建模动态依赖时，个体状态连续演化又受群体动态影响、而现有方法孤立建模或离散近似难以刻画长程不规则与稀疏观测的问题，提出耦合连续时间潜动力学框架CoCLD。方法让个体事件序列与全局分布过程异步交互、连续演化。实验表明其在捕捉长程时间不规则性与稀疏观测上优于离散近似方法。该工作直接推进了连续时间事件序列分析。

### 3. 对应检索需求
continuous-time event sequence analysis。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=HfQ0X1lTGg](https://openreview.net/forum?id=HfQ0X1lTGg)
