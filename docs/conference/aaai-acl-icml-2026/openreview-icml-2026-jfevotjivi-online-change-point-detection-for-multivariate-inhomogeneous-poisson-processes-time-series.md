---
title: Online Change Point Detection for Multivariate Inhomogeneous Poisson Processes Time Series
title_zh: 多变量非齐次泊松过程时间序列的在线变点检测
authors: "Xiaokai Luo, Haotian Xu, Carlos Misael Madrid Padilla, OSCAR HERNAN MADRID PADILLA"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/6b84f1c7dcb2124b588f480f9b7b0ef64c410e05.pdf"
tags: ["query:tpp-es"]
score: 6.0
evidence: 点过程强度函数建模与推断
tldr: 多变量非齐次泊松点过程时间序列的在线变点检测在地震、气候与流行病监测中常见，但机器学习与统计文献研究不足。本文提出用低秩矩阵表示多变量泊松强度函数，构建自适应非参数检测流程，每次新观测仅需常数计算开销且为单遍算法。作者给出了控制整体虚警概率与检测延迟的理论保证，为点过程强度建模与在线推断提供了有效方法。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 多变量非齐次泊松点过程时间序列的在线变点检测研究不足，缺乏高效推断方法。
method: 用低秩矩阵表示多变量泊松强度函数，构建单遍、常数开销的自适应非参数检测算法。
result: 给出控制整体虚警概率与刻画检测延迟的理论保证。
conclusion: 为点过程强度建模与在线变点推断提供了高效且有理论支撑的方案。
---

## Abstract
We study online change point detection for multivariate inhomogeneous Poisson point process time series. This setting arises commonly in applications such as earthquake seismology, climate monitoring, and epidemic surveillance, yet  remains underexplored in the machine learning and statistics literature.   We propose a method that  uses   low-rank matrices  to represent the  multivariate Poisson intensity functions, resulting in an adaptive nonparametric detection procedure. Our algorithm is single-pass and requires only constant computational cost per new observation, independent of the elapsed length of the time series.  We  provide theoretical guarantees to control  the overall false alarm probability and  characterize  the detection delay under temporal dependence. We also develop a new Matrix Bernstein inequality for temporally dependent Poisson point process time series, which may be of independent interest.
Numerical experiments demonstrate that our method is both statistically robust and computationally efficient.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
点过程强度函数建模与推断。

### 2. 核心内容
多变量非齐次泊松点过程时间序列的在线变点检测在地震、气候与流行病监测中常见，但机器学习与统计文献研究不足。本文提出用低秩矩阵表示多变量泊松强度函数，构建自适应非参数检测流程，每次新观测仅需常数计算开销且为单遍算法。作者给出了控制整体虚警概率与检测延迟的理论保证，为点过程强度建模与在线推断提供了有效方法。

### 3. 对应检索需求
temporal point process model and inference。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=JFevoTJIVi](https://openreview.net/forum?id=JFevoTJIVi)
