---
title: Disentangling Latent Risk Pathways via Bayesian Hypergraph Inference
title_zh: 通过贝叶斯超图推断解耦潜在风险通路
authors: "Shengxian Ding, Haonan Gao, Pangpang Liu, Xinyuan Tian, Yize Zhao"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/482bad8ecc74d2b77ba63c04d648ff928fe2ed51.pdf"
tags: ["query:ehr-es"]
score: 7.0
evidence: EHR多疾病建模与贝叶斯不确定性量化
tldr: 针对电子健康记录中多疾病建模结果稀有、受共享风险因素影响，且现有黑箱模型缺乏不确定性量化的问题，本文提出贝叶斯超图推断框架，将多疾病建模重构为受风险因素调制的潜在疾病通路。风险因素作用于超边，使疾病可参与多条通路，从而获得可解释的高阶结构。实验表明该方法在保持预测性能的同时提供了原则性的不确定性量化，对可信临床预测有重要意义。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 电子健康记录中多疾病结果稀有且受共享风险因素影响，现有模型忽视不确定性量化。
method: 提出贝叶斯超图推断框架，以风险因素调制的潜在疾病通路对多疾病建模。
result: 方法实现可解释的高阶结构并给出原则性不确定性量化。
conclusion: 为可信多疾病风险建模与临床预测提供了可解释且带不确定性的方案。
---

## Abstract
Electronic health records (EHR) pose large-scale multi-disease modeling problems in which many outcomes are rare and strongly influenced by shared risk factors. While modern approaches achieve strong predictive performance, they often treat diseases independently or rely on black-box architectures, offering limited insight into how risk factors organize disease risk and little principled uncertainty quantification.
We introduce a Bayesian hypergraph inference framework that reframes multi-disease modeling around **latent, risk-factor-modulated disease pathways**. Risk factors act on hyperedges, latent disease subsets with shared risk patterns, allowing diseases to participate in multiple distinct pathways and enabling interpretable, higher-order structure beyond pairwise associations. A repulsion prior encourages parsimonious and identifiable structure, while posterior inference provides calibrated uncertainty over both disease groupings and risk-factor influence. 
To enable scalable inference on large EHR datasets, we develop a structured variational inference algorithm that preserves logical dependencies among hyperedge existence, disease membership, and pathway-level effects. 
Experiments on simulated data and UK Biobank demonstrate stable and interpretable disease pathway structure, well-calibrated uncertainty, improved estimation for rare diseases, and competitive predictive performance.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
EHR多疾病建模与贝叶斯不确定性量化。

### 2. 核心内容
针对电子健康记录中多疾病建模结果稀有、受共享风险因素影响，且现有黑箱模型缺乏不确定性量化的问题，本文提出贝叶斯超图推断框架，将多疾病建模重构为受风险因素调制的潜在疾病通路。风险因素作用于超边，使疾病可参与多条通路，从而获得可解释的高阶结构。实验表明该方法在保持预测性能的同时提供了原则性的不确定性量化，对可信临床预测有重要意义。

### 3. 对应检索需求
Papers central to 查找关于EHR Event Stream相关的论文，包括EHR序列建模、Foundation models以及下游任务如疾病诊断、死亡预测和患者轨迹生成以及更可信的反事实、因果、不确定性等。, especially work that connects or combines: EHR event stream modeling; electronic health record sequence modeling; patient trajectory generation using EHR; multi-label disease diagnosis from electronic health records; clinical event sequence modeling; electronic health records generation models; reliable and trustworthy prediction for EHR event stream modeling and downstream tasks, relevant to counterfactual analysis, causal inference, or uncertainty quantification / calibration; how to model EHR event sequences with foundation models; downstream tasks for EHR sequence modeling including mortality prediction and multi label diagnosis; generative models for patient trajectory generation from clinical time series.

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=vNfbqRzash](https://openreview.net/forum?id=vNfbqRzash)
