---
title: Deep Representation Learning for Forecasting Recursive and Multi-Relational Events in Temporal Networks
authors: "Tony Gracious, Ambedkar Dukkipati"
date: 2025
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/33857/36012"
tags: ["query:TPP-ES"]
score: 9
source: AAAI-2025-Accepted
selection_source: long-range
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
id: aaai-2025-33857
canonical_id: "work:0ca299fa6fd516ef821aa065"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: pending
---

## Abstract
Understanding relations arising out of interactions among entities can be very difficult, and predicting them is even more challenging. This problem has many applications in various fields, such as financial networks and e-commerce. These relations can involve much more complexities than just involving more than two entities. One such scenario is evolving recursive relations between multiple entities, and so far, this is still an open problem. This work addresses the problem of forecasting higher-order interaction events that can be multi-relational and recursive. We pose the problem in the framework of representation learning of temporal hypergraphs that can capture complex relationships involving multiple entities. The proposed model, \textit{Relational Recursive Hyperedge Temporal Point Process} (RRHyperTPP) uses an encoder that learns a dynamic node representation based on the historical interaction patterns and then a hyperedge link prediction-based decoder to model the occurrence of interaction events. These learned representations are then used for downstream tasks involving forecasting the type and time of interactions. The main challenge in learning from hyperedge events is that the number of possible hyperedges grows exponentially with the number of nodes in the network. This will make the computation of negative log-likelihood of the temporal point process expensive, as the calculation of survival function requires a summation over all possible hyperedges. In our work, we develop a noise contrastive estimation method to learn the parameters of our model, and we have experimentally shown that our models perform better than previous state-of-the-art methods for interaction forecasting.

## 专题评审

专题相关性评分：9/10。

论文提出关系递归超边时序点过程用于时序网络事件预测。

<!-- research-reading-pending -->
中文总结与全文内容待生成；当前仅提供原始论文元数据与摘要。
<!-- /research-reading-pending -->
