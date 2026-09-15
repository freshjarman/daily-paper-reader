---
title: "ReMedi: Reasoner for Medical Clinical Prediction"
title_zh: ReMedi：面向医学临床预测的推理器
authors: "Yushi Cao, Yiming Chen, Hongchao Jiang, Hung-yi Lee, Robby T. Tan"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.findings-acl.1011.pdf"
tags: ["query:ehr-es"]
score: 7.0
evidence: 基于EHR并借助推理预测临床结局
tldr: 从电子健康记录预测未来临床结局因患者数据的复杂与异质而颇具挑战，现有大模型方法多依赖知识蒸馏或检索增强，主要靠模型内部能力解读上下文。本文提出ReMedi框架，通过挑战性样本再生机制生成理由-答案对，利用真实答案作为提示增强推理，并结合微调与偏好调优。该方法提升了基于EHR的临床结局预测推理质量，为可解释的临床预测提供了新的训练范式。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1011/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1011/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 512, \"height\": 512}]"
motivation: 从EHR预测临床结局受数据复杂异质影响，现有大模型方法多依赖知识增强，缺乏显式推理能力。
method: 提出ReMedi框架，通过挑战性样本再生生成理由-答案对，以真实答案作提示增强推理并做微调与偏好调优。
result: 方法提升了基于EHR的临床结局预测的推理质量与预测表现。
conclusion: 该工作为可解释、可推理的EHR临床预测提供了新的训练与增强范式。
---

## Abstract
Predicting future clinical outcomes from electronic health records (EHR) remains challenging due to the complexity and heterogeneity of patient data. LLMs have shown strong potential for such predictive tasks, yet existing approaches mainly focus on enhancing medical knowledge through distillation or RAG while relying on the model’s internal ability to interpret contextual information. In this work, we present ReMedi (Reasoner for Medical Clinical Prediction), a framework for improving clinical outcome prediction from EHR. ReMedi generates rationale–answer pairs using a challenging sample regeneration mechanism for complex clinical questions, which leverages ground-truth answers as hints to enhance reasoning for further fine-tuning and preference tuning. ReMedi integrates ground-truth outcome guidance into the preference data construction loop, regenerating rationale-answer variants. By tuning on these rationale-answer pairs, the model improves its predictive performance. Experiments on multiple EHR prediction tasks demonstrate substantial gains of up to 19.9% over state-of-the-art baselines in terms of F1 score, underscoring ReMedi’s effectiveness in real-world clinical prediction.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义（研究动机和背景）
- **背景**：从电子健康记录（EHR）预测未来临床结局（如再入院、住院时长、死亡）对患者护理与医院资源管理非常重要。但 EHR 数据具有结构化、异质、纵向复杂等特点，建模困难。
- **现有问题**：LLM 在医学任务中有潜力，但已有临床预测方法多依赖医学知识蒸馏、RAG 或结构化医学图谱；这些方法常忽略模型自身的推理能力，且部分方法依赖
