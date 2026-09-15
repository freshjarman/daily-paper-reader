---
title: "PathwayLLM: Explainable Clinical Trajectory Modeling with Structured Pathways for Sepsis Prediction"
title_zh: PathwayLLM：面向脓毒症预测的结构化通路可解释临床轨迹建模
authors: "Zhengqiu Yu, Yueping Ding, Xiangrong Liu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/332b8086024ec5fc16abadd70b4c9eec768198a8.pdf"
tags: ["query:ehr-es"]
score: 8.0
evidence: 基于EHR时序信号的临床轨迹建模与脓毒症预测
tldr: 该工作针对患者级脓毒症预测需跟踪临床恶化并整合EHR异构结构化证据的问题，提出可解释的临床轨迹建模框架PathwayLLM。方法分三阶段，将生理测量、时序动态、患者-诊断-药物异构图及依赖推导的通路信号编码后注入预训练语言模型。实验表明该多视图轨迹框架在脓毒症预测上兼顾性能与可解释性。其为EHR临床事件序列建模与轨迹预测提供了结构化融合方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 患者级脓毒症预测需跟踪临床恶化并整合EHR中的异构结构化证据。
method: 三阶段框架编码生理测量、时序动态、异质图与依赖推导通路信号并注入语言模型。
result: 在脓毒症预测任务上兼顾预测性能与临床可解释性。
conclusion: 为EHR临床事件序列建模与轨迹预测提供了结构化多视图融合方案。
---

## Abstract
Patient-level sepsis prediction requires models that track clinical deterioration over time and integrate heterogeneous structured evidence from electronic health records. We present PathwayLLM, a trajectory-based framework that grounds prediction on temporal signals, graph-structured evidence, and pathway-level clinical information derived from statistical dependency discovery. PathwayLLM follows a three-stage design. First, each observation window is encoded from multiple structured views, including physiological measurements, temporal dynamics, a heterogeneous patient-diagnosis-medication graph, and dependency-derived pathway signals. Second, these representations are injected into a pretrained language model as auxiliary contextual embeddings so that risk prediction and evidence-conditioned explanations can be learned jointly. Third, a Clinical Trajectory LSTM with Deterioration Attention aggregates window-level representations to highlight critical deterioration points and produce patient-level risk scores. On MIMIC-IV (15,410 ICU patients; 8.45% sepsis prevalence), PathwayLLM achieves AUROC 0.891 and AUPRC 0.724, outperforming strong time-series and pretrained baselines. External validation on eICU achieves AUROC 0.842 zero-shot and 0.867 after light fine-tuning. Ablation studies indicate that trajectory aggregation and structured clinical signals are key contributors, and clinician review suggests coherent, interpretable, and clinically relevant explanations.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于EHR时序信号的临床轨迹建模与脓毒症预测。

### 2. 核心内容
该工作针对患者级脓毒症预测需跟踪临床恶化并整合EHR异构结构化证据的问题，提出可解释的临床轨迹建模框架PathwayLLM。方法分三阶段，将生理测量、时序动态、患者-诊断-药物异构图及依赖推导的通路信号编码后注入预训练语言模型。实验表明该多视图轨迹框架在脓毒症预测上兼顾性能与可解释性。其为EHR临床事件序列建模与轨迹预测提供了结构化融合方案。

### 3. 对应检索需求
clinical event sequence modeling。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=oB7gZX7MKP](https://openreview.net/forum?id=oB7gZX7MKP)
