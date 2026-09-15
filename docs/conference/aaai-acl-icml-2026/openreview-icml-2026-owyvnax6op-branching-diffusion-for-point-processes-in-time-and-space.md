---
title: Branching Diffusion for Point Processes in Time and Space
title_zh: 面向时间与空间点过程的分支扩散模型
authors: "Chao Yang, Wenjie Shen, Shuang Li"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/574a07a3ab057971ab142c75a5fd8ad25a7c8312.pdf"
tags: ["query:tpp-es"]
score: 9.0
evidence: 基于分支扩散生成时空点过程
tldr: 针对时空点过程的生成建模，本文提出一种非自回归的分支扩散模型。方法从Wasserstein-Fisher-Rao梯度流这一几何原理出发，构造可处理的正向加噪机制，包含扰动事件位置与时间的漂移-扩散步骤以及通过稀疏化与泊松复制改变事件数的生灭分支步骤。作者用置换等变去噪器学习逆向动力学并预测漂移场与净增长场。该模型能联合生成事件的位置、时间与数量，为时空点过程生成与综合提供了新的连续时间框架。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 时空点过程生成需要同时刻画事件的位置、时间与数量，传统自回归方法难以高效建模。
method: 提出非自回归分支扩散模型，基于WFR梯度流设计漂移-扩散与生灭分支加噪，用置换等变去噪器学习逆过程。
result: 模型能联合生成事件位置、时间与计数，实现对时空点过程的有效采样与综合。
conclusion: 该工作为时空点过程的生成建模提供了有理论依据的扩散式框架。
---

## Abstract
We propose a non-autoregressive branching diffusion model for generating spatio-temporal point processes.
Starting from a geometric principle---the Wasserstein-Fisher-Rao (WFR) gradient flow of a generalized KL divergence toward a simple reference intensity---we obtain a tractable forward noising mechanism with two interpretable components:
(i) a Langevin-type \emph{drift-diffusion} step that perturbs event locations and times, and
(ii) a \emph{birth-death branching} step that changes the event count via location-dependent thinning (deaths) and Poisson offspring replication (births).
We learn the reverse-time dynamics using a permutation-equivariant denoiser that predicts a drift field and a net-growth field, and we train it using an entropic-regularized unbalanced optimal transport (UOT), which naturally handles count mismatch between noisy and clean samples.
The resulting generator produces complete spatio-temporal event sets without autoregressive simulation or explicit intensity normalization.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于分支扩散生成时空点过程。

### 2. 核心内容
针对时空点过程的生成建模，本文提出一种非自回归的分支扩散模型。方法从Wasserstein-Fisher-Rao梯度流这一几何原理出发，构造可处理的正向加噪机制，包含扰动事件位置与时间的漂移-扩散步骤以及通过稀疏化与泊松复制改变事件数的生灭分支步骤。作者用置换等变去噪器学习逆向动力学并预测漂移场与净增长场。该模型能联合生成事件的位置、时间与数量，为时空点过程生成与综合提供了新的连续时间框架。

### 3. 对应检索需求
spatio-temporal point process for events with locations and time。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=oWyvNaX6op](https://openreview.net/forum?id=oWyvNaX6op)
