---
title: "Time-Conditioned Foreseeing: An EHR-Specific Foundation Model for Irregular Dynamics and Calendrical Time"
title_zh: 时间条件预见：面向不规则动态与日历时间的EHR专用基础模型
authors: "Bong Gyun Kang, Junyong Ahn, Hyeongrok Han, Sungroh Yoon"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/86216bfeed28703e5e97f96edb45fea5d0ecb332.pdf"
tags: ["query:ehr-es"]
score: 9.0
evidence: 捕获不规则动态与日历时间的EHR专用基础模型
tldr: 现有电子健康记录基础模型多沿用不契合的NLP式方法，难以刻画EHR特有的不规则动态与时间结构。本文提出面向EHR的预训练方案：病理聚焦分箱按临床显著数值区间量化，双日历旋转位置编码同时编码绝对与相对时间信号，并提出时间条件预见目标对齐临床趋势。实验表明其更好地捕捉临床事件时序。该工作直接服务于以基础模型建模EHR事件序列。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有EHR基础模型沿用不适合的NLP方法，难以建模临床事件的不规则动态与时间结构。
method: 提出病理聚焦分箱、双日历旋转位置编码与时间条件预见目标，构建EHR专用预训练框架。
result: 在临床事件时序建模上更准确地捕捉绝对时间与相对间隔信号。
conclusion: 为以基础模型建模EHR事件序列并支撑临床预测提供了针对性方案。
---

## Abstract
Electronic Health Records (EHRs) possess unique characteristics distinct from natural language, yet existing EHR foundation models often rely on suboptimal NLP-based approaches. We propose a pretraining method tailored to EHRs' distinct features. First, we introduce Pathology-Focused Binning, a density-based quantization strategy that prioritizes clinically significant numerical ranges over usual values. Second, to jointly capture both the exact timing of clinical events and the relative intervals between them, we propose Dual-Calendar Rotary Positional Embedding (RoPE), which encodes absolute and relative temporal signals. Third, we introduce the Time-Conditioned Foreseeing (TCF) objective, aligning with clinical treatment planning to forecast events across multiple temporal horizons by explicitly modeling event timing. Our approach establishes a temporal generative EHR model that outperforms existing foundation models on eleven diverse downstream tasks—achieving up to a 54% improvement in AUPRC—and enables the generation of realistic, temporally consistent patient trajectories. Code is available at https://github.com/Pusheen-cat/TCF_PFM.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
捕获不规则动态与日历时间的EHR专用基础模型。

### 2. 核心内容
现有电子健康记录基础模型多沿用不契合的NLP式方法，难以刻画EHR特有的不规则动态与时间结构。本文提出面向EHR的预训练方案：病理聚焦分箱按临床显著数值区间量化，双日历旋转位置编码同时编码绝对与相对时间信号，并提出时间条件预见目标对齐临床趋势。实验表明其更好地捕捉临床事件时序。该工作直接服务于以基础模型建模EHR事件序列。

### 3. 对应检索需求
how to model EHR event sequences with foundation models。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=IalpB5Mzaz](https://openreview.net/forum?id=IalpB5Mzaz)
