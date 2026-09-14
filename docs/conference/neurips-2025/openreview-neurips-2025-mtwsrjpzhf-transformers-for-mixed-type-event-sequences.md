---
title: Transformers for Mixed-type Event Sequences
authors: "Felix Draxler, Yang Meng, Kai Nelson, Lukas Laskowski, Yibo Yang, Theofanis Karaletsos, Stephan Mandt"
date: 2025
pdf: "https://papers.neurips.cc/paper_files/paper/2025/file/a6c7515ac435277dc92b75a07bb2257c-Paper-Conference.pdf"
tags: ["query:TPP-ES"]
score: 9
source: NeurIPS-2025-Accepted
selection_source: long-range
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
id: openreview-neurips-2025-mtwsrjpzhf
canonical_id: "work:1a3064af9c2021429cc13711"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: pending
---

## Abstract
Event sequences appear widely in domains such as medicine, finance, and remote sensing, yet modeling them is challenging due to their heterogeneity: sequences often contain multiple event types with diverse structures—for example, electronic health records that mix discrete events like medical procedures with continuous lab measurements. Existing approaches either tokenize all entries, violating natural inductive biases, or ignore parts of the data to enforce a consistent structure. In this work, we propose a simple yet powerful Marked Temporal Point Process (MTPP) framework for modeling event sequences with flexible structure, using a single unified model. Our approach employs a single autoregressive transformer with discrete and continuous prediction heads, capable of modeling variable-length, mixed-type event sequences. The continuous head leverages an expressive normalizing flow to model continuous event attributes, avoiding the numerical integration required for inter-event times in most competing methods. Empirically, our model excels on both discrete-only and mixed-type sequences, improving prediction quality and enabling interpretable uncertainty quantification. We make our code public at https://github.com/czi-ai/FlexTPP.

## 专题评审

专题相关性评分：9/10。

摘要明确提出marked temporal point process框架建模混合类型事件序列，直接相关。

<!-- research-reading-pending -->
中文总结与全文内容待生成；当前仅提供原始论文元数据与摘要。
<!-- /research-reading-pending -->
