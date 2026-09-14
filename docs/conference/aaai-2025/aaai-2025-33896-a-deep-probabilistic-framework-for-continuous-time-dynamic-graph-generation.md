---
title: A Deep Probabilistic Framework for Continuous Time Dynamic Graph Generation
authors: "Ryien Hosseini, Filippo Simini, Venkatram Vishwanath, Henry Hoffmann"
date: 2025
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/33896/36051"
tags: ["query:TPP-ES"]
score: 7
source: AAAI-2025-Accepted
selection_source: long-range
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
id: aaai-2025-33896
canonical_id: "work:383341fb8e8dfc83e0a2aadd"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: pending
---

## Abstract
Recent advancements in graph representation learning have shifted attention towards dynamic graphs, which exhibit evolving topologies and features over time. The increased use of such graphs creates a paramount need for generative models suitable for applications such as data augmentation, obfuscation, and anomaly detection. However, there are few generative techniques that handle continuously changing temporal graph data; existing work largely relies on augmenting static graphs with additional temporal information to model dynamic interactions between nodes. In this work, we propose a fundamentally different approach: We instead directly model interactions as a joint probability of an edge forming between two nodes at a given time. This allows us to autoregressively generate new synthetic dynamic graphs in a largely assumption free, scalable, and inductive manner. We formalize this approach as DG-Gen, a generative framework for continuous time dynamic graphs, and demonstrate its effectiveness over five datasets.  Our experiments demonstrate that DG-Gen not only generates higher fidelity graphs compared to traditional methods but also significantly advances link prediction tasks.

## 专题评审

专题相关性评分：7/10。

直接对连续时间动态图中边形成时间建模并生成事件，实质邻近连续时间事件序列生成。

<!-- research-reading-pending -->
中文总结与全文内容待生成；当前仅提供原始论文元数据与摘要。
<!-- /research-reading-pending -->
