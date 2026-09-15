---
title: Conformal Event Prediction with Temporal Knowledge Graph
title_zh: 基于时序知识图的保形事件预测
authors: "Cheng Hu, Cong Cao, Fangfang Yuan, Diandian Guo, Pin Xu, Yu Liu, Yanbing Liu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.findings-acl.258.pdf"
tags: ["query:tpp-es"]
score: 6.0
evidence: 事件预测与保形不确定性量化
tldr: 在军事、公共安全与医疗等高风险场景中，基于时序知识图的事件预测直接影响决策与资源分配，但现有方法缺乏严格的不确定性量化，可靠性受限。本文提出CFEP，一种面向事件预测的保形预测框架，通过非一致性分数扩散与端到端优化，在保证覆盖率的同时提升预测效率。该方法为高风险连续时间事件预测提供了可信的不确定性量化手段，但面向的是时序知识图而非经典点过程强度建模。
source: ACL-2026-Findings
selection_source: conference_retrieval
motivation: 高风险场景下的事件预测缺乏严格不确定性量化，可靠性不足影响决策。
method: 提出CFEP保形预测框架，采用非一致性分数扩散与端到端优化保证覆盖率。
result: 在保证预测覆盖率的同时提升预测效率，增强事件预测可靠性。
conclusion: 为高风险事件预测提供了可信的不确定性量化框架。
---

## Abstract
Event prediction plays a critical role in high-stakes applications such as military operations, public safety, and healthcare. Current methods learn temporal knowledge graphs to predict events at future timestamps, and the predictions directly influence decision-making and resource allocation. However, these methods lack rigorous uncertainty quantification, which limits their reliability for decision-making, especially in high-stakes scenarios where the cost of errors is high. In this paper, we propose CFEP, a conformal prediction framework tailored for event prediction to address this challenge. This is achieved through end-to-end optimization that ensures coverage while improving efficiency. Specifically, we first introduce non-conformity score diffusion, which captures both topological and temporal uncertainty in temporal knowledge graphs. Additionally, we propose an efficiency-aware optimization algorithm to reduce the coverage gap and improve computational efficiency. Experimental results on three public datasets demonstrate that our approach consistently guarantees statistical coverage while improving efficiency. The code and datasets are available at https://github.com/hucheng-IIE/CFEP.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义
- **研究动机**：事件预测在军事、公共安全、医疗等高风险场景中直接影响决策与资源分配，但现有基于时序知识图的方法大多只输出点预测，缺乏严格的不确定性量化。
- **背景矛盾**：保形预测可提供分布无关的统计覆盖保证，但其核心假设是数据可交换。时序知识图中的事件存在时间依赖、拓扑依赖和标签/特征演化，导致校准集与测试集分布不同，标准保形预测的覆盖保证会被破坏。
- **论文目标**：提出 CFEP（Conformal Event Prediction），面向时序知识图事件预测，在保证统计覆盖的同时提高预测集效率，即生成更紧凑、可用于决策的预测集合。

## 2. 方法论
### 2.1 核心思想
- 先证明事件预测中可交换性条件不成立，并定义“覆盖间隙”：目标覆盖率与实际覆盖率之差。
- 推导覆盖间隙上界，指出**加权分位数**和**非一致性分数**是关键因素。
- 通过两个模块降低覆盖间隙：**非一致性分数扩散**与**效率感知
