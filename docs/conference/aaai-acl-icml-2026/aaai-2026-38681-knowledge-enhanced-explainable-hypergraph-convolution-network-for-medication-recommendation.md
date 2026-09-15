---
title: Knowledge-Enhanced Explainable Hypergraph Convolution Network for Medication Recommendation
title_zh: 知识增强可解释超图卷积网络用于用药推荐
authors: "Zihan Zhang, Hongzhi Liu, Xiaoshuang Guo, Tianqi Sun, Zhonghai Wu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38681/42643"
tags: ["query:ehr-es"]
score: 6.0
evidence: 建模电子健康记录中复杂关系用于用药推荐
tldr: 现有用药推荐方法在电子健康记录复杂关系建模、数据稀疏与可解释性方面存在不足。本文提出知识增强可解释超图卷积网络KEHGCN，构建分层超图结构捕捉EHR多层级关系，并引入外部知识图谱补充正关系以缓解数据稀疏。实验证明其在用药推荐上兼具准确性与可解释性。该工作面向EHR事件流建模的下游临床预测任务。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 现有用药推荐难以充分建模EHR中的复杂关系，且存在数据稀疏与缺乏可解释性的问题。
method: 构建分层超图捕捉EHR多层级关系，并融合外部知识图谱补充正关系以缓解数据稀疏。
result: 在用药推荐任务上提升了准确性，并增强了推荐结果的可解释性。
conclusion: 为基于EHR的患者记录建模与临床决策支持提供了知识增强的可解释方案。
---

## Abstract
Medication recommendation systems aim to provide personalized and safe medication options based on individual patient records. However, existing approaches often face challenges related to inadequate modeling of complex relationships within Electronic Health Records (EHRs), data sparsity, and a lack of explainability for recommendations. In this paper, we present a Knowledge-enhanced Explainable HyperGraph Convolution Network (KEHGCN) that constructs a hierarchical hypergraph structure to capture the multi-level relationships within EHR data. By incorporating external knowledge graphs, our approach introduces additional positive relations that help alleviate the impact of data sparsity on model learning. Furthermore, by performing generalized metapath construction and selection on the knowledge graph, our approach achieves effective knowledge filtering and extracts semantically meaningful metapaths, thereby further enhancing the explainability of the recommendation results. We also explicitly introduce negative relations present in the domain knowledge to improve the safety of medication recommendation. Extensive experiments on different hospital departments of MIMIC-III and MIMIC-IV datasets demonstrate that KEHGCN outperforms other state-of-the-art baselines.

---

## 论文详细总结（自动生成）

# 论文总结：Knowledge-Enhanced Explainable Hypergraph Convolution Network for Medication Recommendation

## 1. 核心问题与整体含义
- **研究任务**：面向电子健康记录（EHR）的个性化、安全用药推荐，即根据患者当前诊断、操作和历史就诊记录，预测当前就诊应开具的药物集合。
- **核心问题**：
  - 现有方法对 EHR 中复杂、高阶关系的建模不足，常只建模简单的成对关联，忽略就诊内共现、患者纵向轨迹等多层级依赖。
  - EHR 数据高度稀疏：患者一旦用药有效，后续交互很少更新，导致传统协同过滤式推荐学习困难。
  - 外部知识利用不充分：已有知识增强方法多关注正关系，较少显式利用禁忌、药物相互作用等负关系。
  - 可解释性不足：用药推荐属于高风险临床决策，但多数方法只追求预测精度，难以说明“为何推荐该药”。
- **整体含义**：论文提出 KEHGCN，将分层超图、UMLS 知识图谱、广义元路径、负关系安全约束统一到一个可解释用药推荐框架中，试图同时提升准确性、安全性与可解释性。

## 2. 方法论
### 2.1 核心思想
- 构建 **分层超图** 表示 EHR：就诊级超边刻画一次就诊内疾病、操作、药物的共现；患者级超边聚合患者多次就诊，刻画纵向治疗轨迹。
- 从外部知识图谱中抽取 **广义元路径**，补充正关系以缓解稀疏，并通过元路径权重提供推荐解释。
- 显式引入 **负关系**：疾病—药物禁忌和药物—药物不良相互作用，用于安全约束。
- 采用 **多视角预测**：元路径视角捕捉语义匹配，实例视角捕捉相似患者历史经验。

### 2.2 关键技术细节
- **分层超图构建**：
  - 对每次就诊 \(v_i\)，构造超边 \(E_{v_i}=D_{v_i}\cup P_{v_i}\cup M_{v_i}\)，即该次就诊的疾病、操作、药物节点集合。
  - 对每个患者 \(u_j\)，构造患者超边 \(E_{u_j}\)，聚合其所有就诊超边。
  - 当前查询就诊超边由当前疾病、当前操作和上一次就诊药物共同构成，用于预测当前药物。
- **广义元路径抽取与知识过滤**：
  - 基于 UMLS 构建知识图谱，抽取临床正关系元路径。
  - 常规元路径如：`(Disease, TreatedBy, Medication)`、`(Disease, MolecularAbnormality, Molecular, ActiveIngredientOf, Medication)`、`(Disease, ClassifiedAs, Classification, Classifies, Medication)`。
  - 提出广义元路径，将就诊超边也视为医学实体，如 `(VisitHyperedge, Includes, Disease, TreatedBy, Medication)`，从而在同一就诊上下文中建模更细粒度关系。
- **知识驱动超图卷积**：
  - **超图卷积**：更新疾病、操作、药物节点表示，聚合同一就诊超边内节点信息；再聚合节点表示更新就诊超边，捕获共现关系。
  - **元路径卷积**：
    - 元路径内聚合
