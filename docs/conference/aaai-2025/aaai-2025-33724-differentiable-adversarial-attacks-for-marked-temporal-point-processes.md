---
title: Differentiable Adversarial Attacks for Marked Temporal Point Processes
authors: "Pritish Chakraborty, Vinayak Gupta, Rahul R, Srikanta J. Bedathur, Abir De"
date: 2025
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/33724/35879"
tags: ["query:TPP-ES"]
score: 8
source: AAAI-2025-Accepted
selection_source: long-range
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
id: aaai-2025-33724
canonical_id: "work:c344845ceca6ab6467a6c836"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: pending
---

## Abstract
Marked temporal point processes (MTPPs) have been shown to be extremely effective in modeling continuous time event sequences (CTESs). In this work, we present adversarial attacks designed specifically for MTPP models. A key criterion for a good adversarial attack is its imperceptibility. For objects such as images or text, this is often achieved by bounding perturbation in some fixed Lp norm-ball. However, similarly minimizing distance norms between two CTESs in the context of MTPPs is challenging due to their sequential nature and varying time-scales and lengths. We address this challenge by first permuting the events and then incorporating the additive noise to the arrival timestamps. However, the worst case optimization of such adversarial attacks is a hard combinatorial problem, requiring exploration across a permutation space that is factorially large in the length of the input sequence. As a result, we propose a novel differentiable scheme - PERMTPP - using which we can perform adversarial attacks by learning to minimize the likelihood, while minimizing the distance between two CTESs. Our experiments on four real-world datasets demonstrate the offensive and defensive capabilities, and lower inference times of PERMTPP.

## 专题评审

专题相关性评分：8/10。

摘要明确研究marked temporal point processes上的对抗攻击，属于该专题直接工作。

<!-- research-reading-pending -->
中文总结与全文内容待生成；当前仅提供原始论文元数据与摘要。
<!-- /research-reading-pending -->
