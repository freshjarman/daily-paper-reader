---
title: "OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data"
title_zh: OpenTSLM：面向多变量医学文本与时间序列数据推理的时间序列语言模型
authors: "Patrick Langer, Thomas Kaar, Max Rosenblattl, Maxwell A Xu, Winnie Chow, Martin Maritsch, Robert Jakob, Ning Wang, Juncheng Liu, Aradhana Verma, Brian Han, Daniel Seung Kim, Henry Chubb, Scott R. Ceresnak, Aydin Zahedivash, Alexander T Sandhu, Fatima Rodriguez, Daniel McDuff, Elgar Fleisch, Oliver Oppers Aalami, Filipe Barata, Paul Schmiedmayer"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/5fef491b44184070e60180fcf08920003a8c4ef9.pdf"
tags: ["query:ehr-es"]
score: 6.0
evidence: 面向多变量医学数据的时间序列语言模型
tldr: 该工作针对大语言模型虽擅长多模态理解却难以处理时间序列数据的问题，尤其在纵向与可穿戴医疗数据场景。作者提出OpenTSLM开源时间序列语言模型家族，通过软提示或交叉注意力将时间序列作为原生模态整合进预训练大模型，并构建多个推理数据集。模型支持以自然语言对多变量医学时间序列进行提示与推理，服务于数字健康应用。其意义在于将基础模型范式引入临床时间序列建模与推理。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 大语言模型擅长多模态理解但难以处理时间序列，纵向与可穿戴医疗数据难以转化为可用洞见。
method: 提出OpenTSLM时间序列语言模型家族，通过软提示或交叉注意力将时间序列作为原生模态接入预训练大模型。
result: 模型支持用自然语言对多变量医学时间序列进行提示与推理，并配套构建多个时间序列推理数据集。
conclusion: 将基础模型范式扩展到临床时间序列，为医学多模态推理提供开源方案。
---

## Abstract
Large Language Models have shown strong capabilities in interpreting multimodal data but remain limited in handling time-series data. Addressing this gap could help to translate longitudinal and wearable data into actionable insights and patient-facing digital health applications.
We propose OpenTSLM, an open-source family of Time Series Language Models integrating time-series as a native modality into pretrained LLMs, enabling natural-language prompting and reasoning over multiple time-series via either soft prompting (OpenTSLM-SoftPrompt) or cross-attention (OpenTSLM-Flamingo). 
To enable training models for time-series reasoning, we introduce three datasets: HAR-CoT (human activity recognition), Sleep-CoT (sleep staging), and ECG-QA-CoT (electrocardiogram question answering). 
Across tasks, OpenTSLM models outperform baselines, reaching F1 scores of 69.88% in sleep staging and 67.64% in HAR; OpenTSLM-Flamingo also scales more efficiently in memory as the number and length of time series increase.
Expert evaluations with cardiologists show that OpenTSLMs exhibit strong reasoning capabilities on raw ECG data.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
面向多变量医学数据的时间序列语言模型。

### 2. 核心内容
该工作针对大语言模型虽擅长多模态理解却难以处理时间序列数据的问题，尤其在纵向与可穿戴医疗数据场景。作者提出OpenTSLM开源时间序列语言模型家族，通过软提示或交叉注意力将时间序列作为原生模态整合进预训练大模型，并构建多个推理数据集。模型支持以自然语言对多变量医学时间序列进行提示与推理，服务于数字健康应用。其意义在于将基础模型范式引入临床时间序列建模与推理。

### 3. 对应检索需求
how to model EHR event sequences with foundation models。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=FHDRzhKm0f](https://openreview.net/forum?id=FHDRzhKm0f)
