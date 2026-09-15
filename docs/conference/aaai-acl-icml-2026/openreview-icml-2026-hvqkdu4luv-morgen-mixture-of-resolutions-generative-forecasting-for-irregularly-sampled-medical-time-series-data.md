---
title: "MoRGen: Mixture-of-Resolutions Generative Forecasting for Irregularly Sampled Medical Time-Series Data"
title_zh: MoRGen：面向不规则采样医学时间序列的混合分辨率生成式预测
authors: "Nassim Oufattole, Matthew B.A. McDermott, Collin Stultz"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/f4fceded86d8b4ef33516f42e57b4ede96474281.pdf"
tags: ["query:ehr-es"]
score: 7.0
evidence: 针对不规则采样临床时间序列的自回归生成式预测
tldr: 面向不规则采样临床时间序列的自回归生成模型常用于零样本风险预测，但现有方法多采用单一固定时间分辨率，导致模型分辨率与预测终点的时间动态不匹配时性能下降。本文提出MoRGen，融合在多个时间分辨率上训练的生成式专家，通过低容量任务特定混合器提升预测精度。实验证明其改善了逐终点的零样本预测效果。该工作对临床时间序列的生成式患者轨迹建模具有直接价值。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有临床时间序列生成模型采用单一固定分辨率，难以匹配不同预测终点的时间动态。
method: 提出MoRGen，融合多个时间分辨率下训练的生成式专家，用低容量任务特定混合器整合预测。
result: 提升了不规则采样临床时间序列在零样本风险预测上的逐终点准确度。
conclusion: 为临床时间序列的生成式建模与患者轨迹风险预测提供了多分辨率融合方案。
---

## Abstract
Autoregressive generative models for irregularly sampled clinical time-series data are increasingly used for zero-shot risk forecasting. Prior work typically adopts a single fine-grained discretization of time, where tokens are generated at one fixed, predetermined temporal resolution. We demonstrate that the zero-shot accuracy of individual generative forecasters varies with temporal resolution: performance can degrade when the model resolution is poorly matched to the temporal dynamics of the endpoint being evaluated. We then propose MoRGen (Mixture-of-Resolutions Generation), which fuses forecasts from generative experts trained at multiple temporal resolutions using a low-capacity task-specific mixture, improving performance across tasks with different temporal dynamics. Across multiple horizons and outcomes on three independent clinical datasets, MoRGen achieves lower binary cross-entropy (BCE) and statistically significant AUROC gains over autoregressive generative models that forecast tokens at a fixed temporal resolution.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
针对不规则采样临床时间序列的自回归生成式预测。

### 2. 核心内容
面向不规则采样临床时间序列的自回归生成模型常用于零样本风险预测，但现有方法多采用单一固定时间分辨率，导致模型分辨率与预测终点的时间动态不匹配时性能下降。本文提出MoRGen，融合在多个时间分辨率上训练的生成式专家，通过低容量任务特定混合器提升预测精度。实验证明其改善了逐终点的零样本预测效果。该工作对临床时间序列的生成式患者轨迹建模具有直接价值。

### 3. 对应检索需求
generative models for patient trajectory generation from clinical time series。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=Hvqkdu4Luv](https://openreview.net/forum?id=Hvqkdu4Luv)
