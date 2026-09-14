---
title: Unlocking Point Processes through Point Set Diffusion
authors: "David Lüdke, Enric Rabasseda Raventós, Marcel Kollovieh, Stephan Günnemann"
date: 2025
pdf: "https://proceedings.iclr.cc/paper_files/paper/2025/file/cceb6b5d1781b6eb848f7e87bff5f74b-Paper-Conference.pdf"
tags: ["query:TPP-ES"]
score: 10
source: ICLR-2025-Accepted
selection_source: long-range
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
id: openreview-iclr-2025-4anfphj0wf
canonical_id: "work:f3ada80ee8ba85f08e2c61d7"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: pending
---

## Abstract
Point processes model the distribution of random point sets in mathematical spaces, such as spatial and temporal domains, with applications in fields like seismology, neuroscience, and economics.
Existing statistical and machine learning models for point processes are predominantly constrained by their reliance on the characteristic intensity function, introducing an inherent trade-off between efficiency and flexibility.
In this paper, we introduce Point Set Diffusion, a diffusion-based latent variable model that can represent arbitrary point processes on general metric spaces without relying on the intensity function.
By directly learning to stochastically interpolate between noise and data point sets, our approach effectively captures the distribution of point processes and enables efficient, parallel sampling and flexible generation for complex conditional tasks.
Experiments on synthetic and real-world datasets demonstrate that Point Set Diffusion achieves state-of-the-art performance in unconditional and conditional generation of spatial and spatiotemporal point processes while providing up to orders of magnitude faster sampling.

## 专题评审

专题相关性评分：10/10。

论文直接研究点过程生成建模，涵盖时空点过程。

<!-- research-reading-pending -->
中文总结与全文内容待生成；当前仅提供原始论文元数据与摘要。
<!-- /research-reading-pending -->
