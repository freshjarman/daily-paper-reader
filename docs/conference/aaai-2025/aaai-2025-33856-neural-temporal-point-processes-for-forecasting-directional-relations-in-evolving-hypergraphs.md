---
title: Neural Temporal Point Processes for Forecasting Directional Relations in Evolving Hypergraphs
authors: "Tony Gracious, Arman Gupta, Ambedkar Dukkipati"
date: 2025
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/33856/36011"
tags: ["query:TPP-ES"]
score: 9
source: AAAI-2025-Accepted
selection_source: long-range
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
id: aaai-2025-33856
canonical_id: "work:32b08e2439a0021b9825c581"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: pending
---

## Abstract
Forecasting relations between entities is paramount in the current era of data and AI. However, it is often overlooked that real-world relationships are inherently directional, involve more than two entities, and can change with time. In this paper, we provide a comprehensive solution to the problem of forecasting directional relations in a general setting, where relations are higher-order, i.e., directed hyperedges in a hypergraph. This problem has not been previously explored in the existing literature. The primary challenge in solving this problem is that the number of possible hyperedges is exponential in the number of nodes at each event time. To overcome this, we propose a sequential generative approach that segments the forecasting process into multiple stages, each contingent upon the preceding stages, thereby reducing the search space involved in predictions of hyperedges. The first stage involves a temporal point process-based node event forecasting module that identifies the subset of nodes involved in an event. The second stage is a candidate generation module that predicts hyperedge sizes and adjacency vectors for nodes observing events. The final stage is a directed hyperedge predictor that identifies the truth by searching over the set of candidate hyperedges. To validate the effectiveness of our model, we compiled five datasets and conducted an extensive empirical study to assess each downstream task. Our proposed method achieves a performance gain of 32% and 41%  compared to the state-of-the-art pairwise and hyperedge event forecasting models, respectively, for the event type prediction.

## 专题评审

专题相关性评分：9/10。

论文使用时序点过程预测演化超图中的方向关系事件。

<!-- research-reading-pending -->
中文总结与全文内容待生成；当前仅提供原始论文元数据与摘要。
<!-- /research-reading-pending -->
