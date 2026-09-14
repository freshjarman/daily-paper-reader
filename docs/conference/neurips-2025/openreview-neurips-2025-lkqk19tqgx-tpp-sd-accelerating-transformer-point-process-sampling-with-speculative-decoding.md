---
title: "TPP-SD: Accelerating Transformer Point Process Sampling with Speculative Decoding"
authors: "Shukai Gong, YIYANG FU, Fengyuan Ran, Quyu Kong, Feng Zhou"
date: 2025
pdf: "https://papers.neurips.cc/paper_files/paper/2025/file/b0a844fbfd7f5840baeec02a8e7e406d-Paper-Conference.pdf"
tags: ["query:TPP-ES"]
score: 9
source: NeurIPS-2025-Accepted
selection_source: long-range
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
id: openreview-neurips-2025-lkqk19tqgx
canonical_id: "work:6d464afe4679b2aa768553bd"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: pending
---

## Abstract
We propose TPP-SD, a novel approach that accelerates Transformer temporal point process (TPP) sampling by adapting speculative decoding (SD) techniques from language models. By identifying the structural similarities between thinning algorithms for TPPs and speculative decoding for language models, we develop an efficient sampling framework that leverages a smaller draft model to generate multiple candidate events, which are then verified by the larger target model. TPP-SD maintains the same output distribution as autoregressive sampling while achieving significant acceleration. Experiments on both synthetic and real datasets demonstrate that our approach produces samples from identical distributions as standard methods, but with 2-6$\times$ speedup. Our ablation studies analyze the impact of hyperparameters such as draft length and draft model size on sampling efficiency. TPP-SD bridges the gap between powerful Transformer TPP models and the practical need for rapid sequence generation.

## 专题评审

专题相关性评分：9/10。

标题和摘要明确研究Transformer temporal point process采样加速，直接相关。

<!-- research-reading-pending -->
中文总结与全文内容待生成；当前仅提供原始论文元数据与摘要。
<!-- /research-reading-pending -->
