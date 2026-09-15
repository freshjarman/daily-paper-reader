---
title: Exploring Accurate and Transparent Domain Adaptation in Predictive Healthcare via Concept-Grounded Orthogonal Inference
title_zh: 通过概念接地的正交推断探索预测性医疗中准确且透明的域自适应
authors: "Pengfei Hu, Chang Lu, Feifan Liu, Yue Ning"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/5c8ab9e38823df6b3a58a5c396975a5c2249e12b.pdf"
tags: ["query:ehr-es"]
score: 7.0
evidence: EHR临床事件预测的可信与透明
tldr: 针对电子健康记录上临床事件预测模型在分布偏移下性能下降、且域自适应方法黑箱难以被临床信任的问题，本文提出ExtraCare，将患者表示分解为不变分量与协变分量，并通过监督与正交约束在保留标签信息的同时暴露域特定变化。实验表明该方法比多数特征对齐模型更准确且更透明。该工作推进了可信临床预测与域泛化，与EHR事件流建模的可信性要求高度契合。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: EHR临床事件预测模型在分布偏移下性能下降，域自适应方法黑箱难以信任。
method: 提出ExtraCare，将患者表示分解为不变与协变分量并施加正交约束。
result: 在保留标签信息的同时暴露域变化，预测更准确且更透明。
conclusion: 为可信、可解释的临床事件预测与域自适应提供了新方法。
---

## Abstract
Deep learning models for clinical event prediction on electronic health records (EHR) often suffer performance degradation when deployed under different data distributions. 
While domain adaptation (DA) methods can mitigate such shifts, their "black-box" nature prevents widespread adoption in clinical practice where transparency is essential for trust and safety.
We propose ExtraCare to decompose patient representations into invariant and covariant components. 
By supervising these two components and enforcing their orthogonality during training, our model preserves label information while exposing domain-specific variation at the same time for more accurate predictions than most feature alignment models.
More importantly, it offers human-understandable explanations by mapping sparse latent dimensions to medical concepts and quantifying their contributions via targeted ablations.
ExtraCare is evaluated on two real-world EHR datasets across multiple domain partition settings, demonstrating superior performance along with enhanced transparency, as evidenced by its accurate predictions and explanations from extensive case studies.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
EHR临床事件预测的可信与透明。

### 2. 核心内容
针对电子健康记录上临床事件预测模型在分布偏移下性能下降、且域自适应方法黑箱难以被临床信任的问题，本文提出ExtraCare，将患者表示分解为不变分量与协变分量，并通过监督与正交约束在保留标签信息的同时暴露域特定变化。实验表明该方法比多数特征对齐模型更准确且更透明。该工作推进了可信临床预测与域泛化，与EHR事件流建模的可信性要求高度契合。

### 3. 对应检索需求
reliable and trustworthy prediction for EHR event stream modeling and downstream tasks, relevant to counterfactual analysis, causal inference, or uncertainty quantification / calibration。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=KidQq3EaOe](https://openreview.net/forum?id=KidQq3EaOe)
