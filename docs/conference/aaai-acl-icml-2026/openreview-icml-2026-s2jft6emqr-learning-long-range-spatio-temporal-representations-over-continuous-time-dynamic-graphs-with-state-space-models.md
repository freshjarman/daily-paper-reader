---
title: Learning Long Range Spatio-Temporal Representations over Continuous Time Dynamic Graphs with State Space Models
title_zh: 基于状态空间模型的连续时间动态图长程时空表示学习
authors: "Ayushman Raghuvanshi, Thummaluru Siddartha Reddy, Sundeep Prabhakar Chepuri, Mahesh Chandran"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/37cec4572480e013f9050c56badc98308cdff2cc.pdf"
tags: ["query:tpp-es"]
score: 5.0
evidence: 连续时间动态图上的长程时空表示学习
tldr: 该工作针对连续时间动态图中长程信息传播困难、现有方法仅能捕捉单跳或局部时间邻域而难以建模多跳全局结构的问题，从第一性原理推导出参数高效的状态空间建模框架CTDG-SSM。方法引入连续时间拓扑感知高阶多项式投影算子以保留并更新长时程信息。实验表明其在长程时空表示学习上更具表达力。该工作与连续时间事件序列表示相关，但面向动态图而非点过程。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 连续时间动态图中长程信息传播困难，现有方法仅捕捉局部时间邻域。
method: 从第一性原理推导状态空间框架，引入连续时间拓扑感知高阶多项式投影算子。
result: 在长程时空表示学习上相较局部邻域方法更具表达力。
conclusion: 与连续时间事件序列表示相关，但面向动态图而非时间点过程。
---

## Abstract
Continuous-time dynamic graphs (CTDGs) provide a richer framework to capture fine-grained temporal patterns in evolving relational data. Long-range information propagation is a key challenge while learning representations, wherein it is important to retain and update information over long temporal horizons. Existing approaches restrict models to capture one-hop or local temporal neighborhoods and fail to capture multi-hop or global structural patterns. To mitigate this, we derive a parameter-efficient state-space modeling framework for continuous-time dynamic graphs $\texttt{(CTDG-SSM)}$ from first principles. We first introduce continuous-time Topology-Aware higher order polynomial projection operator ($\texttt{CTT-HiPPO}$), a novel memory-based reformulation of  $\texttt{HiPPO}$ to jointly encode temporal dynamics and graph structure. The solution from $\texttt{CTT-HiPPO}$ is obtained by projecting the classical HiPPO solution through a polynomial of the Laplacian matrix, yielding topology-aware memory updates that admit an equivalent state-space formulation for CTDGs ($\texttt{CTDG-SSM}$). Then a computationally efficient discrete formulation is obtained using the zero-order hold approach for model implementation.
   Across benchmarks on dynamic link prediction, dynamic node classification, and sequence classification, $\texttt{CTDG-SSM}$ achieves state-of-the-art performance. Notably, it achieves large performance gains on datasets that require long range temporal (LRT) and spatial reasoning.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
连续时间动态图上的长程时空表示学习。

### 2. 核心内容
该工作针对连续时间动态图中长程信息传播困难、现有方法仅能捕捉单跳或局部时间邻域而难以建模多跳全局结构的问题，从第一性原理推导出参数高效的状态空间建模框架CTDG-SSM。方法引入连续时间拓扑感知高阶多项式投影算子以保留并更新长时程信息。实验表明其在长程时空表示学习上更具表达力。该工作与连续时间事件序列表示相关，但面向动态图而非点过程。

### 3. 对应检索需求
continuous-time event sequence analysis。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=S2jfT6EMqr](https://openreview.net/forum?id=S2jfT6EMqr)
