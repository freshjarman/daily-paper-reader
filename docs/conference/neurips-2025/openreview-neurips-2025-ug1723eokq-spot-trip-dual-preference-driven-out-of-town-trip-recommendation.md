---
title: "SPOT-Trip: Dual-Preference Driven Out-of-Town Trip Recommendation"
authors: "Yinghui Liu, Hao Miao, Guojiang Shen, Yan Zhao, Xiangjie Kong, Ivan Lee"
date: 2025
pdf: "https://papers.neurips.cc/paper_files/paper/2025/file/d32abef446ead79ac1e7f80419a7b82f-Paper-Conference.pdf"
tags: ["query:TPP-ES"]
score: 6
source: NeurIPS-2025-Accepted
selection_source: long-range
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
id: openreview-neurips-2025-ug1723eokq
canonical_id: "work:3e5851035cfa26042e10aaf8"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: pending
---

## Abstract
Out-of-town trip recommendation aims to generate a sequence of Points of Interest (POIs) for users traveling from their hometowns to previously unvisited regions based on personalized itineraries, e.g., origin, destination, and trip duration. Modeling the complex user preferences--which often exhibit a two-fold nature of static and dynamic interests--is critical for effective recommendations. However, the sparsity of out-of-town check-in data presents significant challenges in capturing such user preferences. Meanwhile, existing methods often conflate the static and dynamic preferences, resulting in suboptimal performance. In this paper, we for the first time systematically study the problem of out-of-town trip recommendation. A novel framework SPOT-Trip is proposed to explicitly learns the dual static-dynamic user preferences. Specifically, to handle scarce data, we construct a POI attribute knowledge graph to enrich the semantic modeling of users’ hometown and out-of-town check-ins, enabling the static preference modeling through attribute relation-aware aggregation. Then, we employ neural ordinary differential equations (ODEs) to capture the continuous evolution of latent dynamic user preferences and innovatively combine a temporal point process to describe the instantaneous probability of each preference behavior. Further, a static-dynamic fusion module is proposed to merge the learned static and dynamic user preferences. Extensive experiments on real data offer insight into the effectiveness of the proposed solutions, showing that SPOT-Trip achieves performance improvement by up to 17.01%.

## 专题评审

专题相关性评分：6/10。

该文主要研究异地旅行推荐，虽结合时间点过程描述偏好行为，但点过程仅为辅助组件而非主要任务。

<!-- research-reading-pending -->
中文总结与全文内容待生成；当前仅提供原始论文元数据与摘要。
<!-- /research-reading-pending -->
