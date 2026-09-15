---
title: "Learning What to Ignore: Mitigating Negative Transfer in Medical Knowledge Fusion via Clinical Task-Adaptive Selection"
title_zh: 学会忽略：通过临床任务自适应选择缓解医学知识融合中的负迁移
authors: "Xinyan Deng, Shoubin Dong, Xiaorou Zheng"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.acl-long.1067.pdf"
tags: ["query:ehr-es"]
score: 6.0
evidence: 面向纵向EHR建模的可信知识融合
tldr: 将外部医学知识融入纵向电子健康记录建模可缓解数据稀疏，但静态本体与LLM推理之间存在可靠性与时效性两难，且盲目融合会引入负迁移。本文提出可信知识增强框架TrustKE，构建双层知识图并按临床任务自适应选择知识。实验表明其能抑制无关知识噪声、保留患者特异性信号并提升下游预测可信度。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1067/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 1486, \"height\": 1642}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1067/fig-002.webp\", \"caption\": \"\", \"page\": 4, \"index\": 2, \"width\": 2741, \"height\": 1432}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1067/fig-003.webp\", \"caption\": \"\", \"page\": 8, \"index\": 3, \"width\": 1504, \"height\": 1076}]"
motivation: EHR建模融合外部知识时面临可靠性与负迁移问题。
method: 提出TrustKE，构建双层知识图并做临床任务自适应知识选择。
result: 抑制任务无关知识噪声，增强患者特异性信号与下游性能。
conclusion: 为可信的纵向EHR知识融合提供自适应选择方案。
---

## Abstract
Integrating external medical knowledge into longitudinal electronic health record modeling is a prevailing paradigm to mitigate clinical data sparsity. However, existing approaches face a reliability-timeliness dilemma, struggling to balance the structural authority of static ontologies with the reasoning flexibility of large language models. Furthermore, most frameworks overlook the risk of relative negative transfer, where indiscriminately fusing task-irrelevant knowledge can introduce noise or even cause conflicts that weakens patient-specific signals. In this paper, we propose TrustKE, a Trustworthy Knowledge Enhancement framework. First, we construct a dual-layer knowledge graph that anchors dynamic, evidence-based chain-of-thought reasoning from medical literature within the stable structure of medical knowledge graph. Second, we introduce a task-adaptive knowledge selection mechanism that dynamically optimizes the graph, retaining only task-specific signals. Extensive experiments on MIMIC-III and MIMIC-IV across four clinical tasks show that TrustKE outperforms state-of-the-art baselines. Our analysis confirms that TrustKE effectively mitigates negative transfer while offering transparent reasoning for clinical decision-making.

---

## 论文详细总结（自动生成）

## 论文信息
- **标题**：Learning What to Ignore: Mitigating Negative Transfer in Medical Knowledge Fusion via Clinical Task-Adaptive Selection
- **中文标题**：学会忽略：通过临床任务自适应选择缓解医学知识融合中的负迁移
- **作者**：Xinyan Deng, Shoubin Dong, Xiaorou Zheng（华南理工大学计算机科学与工程学院）
- **发表**：ACL 2026 Long Papers，pp. 23295–23309
- **核心框架**：TrustKE（Trustworthy Knowledge Enhancement）

## 1. 核心问题与整体含义
- **研究背景**：纵向电子健康记录（EHR）建模在死亡率预测、再入院、药物推荐、疾病预测等临床任务中很重要，但真实临床数据存在稀疏性、长尾分布和少样本泛化差的问题。
- **主流思路**：引入外部医学知识增强患者表示，例如结构化医学本体、知识图谱、LLM/RAG 推理。
- **关键矛盾**：
  - **可靠性与时效性两难**：静态本体（如 UMLS）权威但更新慢、覆盖有限；LLM 推理灵活但可能幻觉、缺乏患者生理状态 grounding。
  - **相对负迁移被忽视**：现有框架常把全局 KG 或检索上下文不加区分地融合进患者表示，任务无关知识会引入噪声、稀释患者特异性信号，甚至造成冲突。
- **论文主张**：知识增强并不必然带来信息增益；“学会忽略”与“扩展知识”同样重要。TrustKE 旨在平衡知识可信度与任务自适应选择，缓解负迁移并提供可解释推理。

## 2. 方法论
### 2.1 核心思想
- 构建**双层知识图**：用 UMLS 稳定结构锚定 LLM 从医学文献中抽取的动态证据链推理。
- 引入**任务自适应知识选择**：根据下游临床任务动态收缩图结构，只保留任务相关边。
- 使用**患者引导异质融合**：将任务特化知识与患者时序状态对齐，生成预测表示。

### 2.2 关键技术细节
- **双层知识构建**：
  - **Layer 1 本体基图**：将 ICD、NDC 等 EHR 编码映射到 UMLS，筛选高频种子实体，
