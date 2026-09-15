---
title: Marrying Generative Model of Healthcare Events with Digital Twin of Social Determinants of Health for Disease Reasoning
title_zh: 融合医疗事件生成模型与健康社会决定因素数字孪生的疾病推理
authors: "Ziquan Wei, Tingting Dan, Guorong Wu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/d831dc201066880cfcebb565565bb35f8330a20e.pdf"
tags: ["query:ehr-es"]
score: 7.0
evidence: 医疗事件生成模型用于疾病推理
tldr: 现有疾病预测生成模型多依赖医院与登记数据的事件级表示，忽视了健康社会决定因素（SDoH），限制了疾病建模与临床决策支持的个性化能力。本文提出一种条件隐扩散生成框架，将ICD编码的SDoH代理与医疗事件结合，实现面向疾病推理的计算机内建模。该方法在多因素疾病场景中建立了社会因素与临床事件之间的联系，为个性化疾病建模和临床决策支持提供了新的生成式工具。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有疾病预测模型仅依赖医院事件表示，忽略健康社会决定因素，难以支持个性化疾病建模。
method: 提出条件隐扩散生成框架，将ICD编码的SDoH代理与医疗事件结合进行疾病推理。
result: 在计算机内建模中建立了社会因素与临床事件联系，提升多因素疾病建模能力。
conclusion: 为个性化疾病建模与临床决策支持提供了融合社会因素的生成式方法。
---

## Abstract
Despite the central role of sensor-derived measurements such as imaging traits and plasma biomarkers in biomedical research and clinical practice, existing generative models for disease prediction largely depend on event-level representations from hospital and registry data. Given the multi-factorial nature of human disease, the absence of explicit modeling of social determinants of health (SDoH) limits the capacity for personalized disease modeling and clinical decision support.
To address this limitation, we propose a generative model with ICD-coded proxies of SDoH for \textit{in silico} modeling of disease reasoning, a conditioned latent diffusion framework that establishes the connection between multi-organ sensor data with tokenized healthcare events. Specifically, we introduce a novel geometric diffusion model to characterize the temporal evolution of complex data representation such as brain networks (region-to-region connectivity encoded in a graph), in parallel with diffusion models for tabular data from other organ systems.
Together, we integrate the generative model with digitalized SDoH proxies (coined **DiffDT**) for simulated intervention and reasoning of future disease trajectories.
We conduct extensive experiments on the UK Biobank (UKB) dataset, which contains organ-specific imaging traits, including brain (44,834), heart (23,987), liver (28,722), and kidney (32,155), along with nearly 500k medical history sequences (age range: 25$\sim$89 years). Our **DiffDT** achieves significant improvements over state-of-the-art human disease autoregressive models and imaging trait generative baselines.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
医疗事件生成模型用于疾病推理。

### 2. 核心内容
现有疾病预测生成模型多依赖医院与登记数据的事件级表示，忽视了健康社会决定因素（SDoH），限制了疾病建模与临床决策支持的个性化能力。本文提出一种条件隐扩散生成框架，将ICD编码的SDoH代理与医疗事件结合，实现面向疾病推理的计算机内建模。该方法在多因素疾病场景中建立了社会因素与临床事件之间的联系，为个性化疾病建模和临床决策支持提供了新的生成式工具。

### 3. 对应检索需求
electronic health records generation models。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=9GKURFWGeh](https://openreview.net/forum?id=9GKURFWGeh)
