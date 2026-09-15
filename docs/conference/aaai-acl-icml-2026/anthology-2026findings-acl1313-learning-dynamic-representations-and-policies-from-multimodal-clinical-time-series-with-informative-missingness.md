---
title: Learning Dynamic Representations and Policies from Multimodal Clinical Time-Series with Informative Missingness
title_zh: 从具有信息性缺失的多模态临床时间序列中学习动态表示与策略
authors: "Zihan Liang, Ziwen Pan, Ruoxuan Xiong"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.findings-acl.1313.pdf"
tags: ["query:ehr-es"]
score: 6.0
evidence: 多模态临床时间序列的患者表示学习
tldr: 该工作针对多模态临床记录中观测稀疏且缺失模式本身蕴含患者状态信息的问题。作者提出一个面向多模态临床时间序列的患者表示学习框架，显式建模结构化测量与临床笔记两种模态各自的观测过程与缺失机制。方法能够从缺失模式中提取额外信息用于临床预测与决策。其贡献在于揭示了观测过程本身的价值，为电子健康记录序列建模提供了新的表示学习思路。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1313/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 1078, \"height\": 922}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1313/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 1078, \"height\": 922}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1313/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 1079, \"height\": 832}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1313/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 1202, \"height\": 880}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1313/fig-005.webp\", \"caption\": \"\", \"page\": 4, \"index\": 5, \"width\": 2912, \"height\": 1440}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1313/fig-006.webp\", \"caption\": \"\", \"page\": 4, \"index\": 6, \"width\": 1030, \"height\": 344}]"
motivation: 多模态临床时间序列观测稀疏，且是否被记录取决于患者潜在状态，现有方法忽视了观测过程本身携带的信息。
method: 提出一个面向多模态临床时间序列的患者表示学习框架，显式建模结构化测量与临床笔记各自的观测与缺失过程。
result: 框架能够提取并利用观测过程所蕴含的信息，提升对患者健康状态演化的建模与下游任务表现。
conclusion: 表明缺失模式具有可利用价值，为电子健康记录序列表示学习提供了新方向。
---

## Abstract
Multimodal clinical records contain structured measurements and clinical notes recorded over time, offering rich temporal information about the evolution of patient health. Yet these observations are sparse, and whether they are recorded depends on the patient’s latent condition. Observation patterns also differ across modalities, as structured measurements and clinical notes arise under distinct recording processes. While prior work has developed methods that accommodate missingness in clinical time series, how to extract and use the information carried by the observation process itself remains underexplored. We therefore propose a patient representation learning framework for multimodal clinical time series that explicitly leverages informative missingness. The framework combines (1) a multimodal encoder that captures signals from structured and textual data together with their observation patterns, (2) a Bayesian filtering module that updates a latent patient state over time from observed multimodal signals, and (3) downstream modules for offline treatment policy learning and patient outcome prediction based on the learned patient state. We evaluate the framework on ICU sepsis cohorts from MIMIC-III, MIMIC-IV, and eICU. It improves both offline treatment policy learning and adverse outcome prediction, achieving FQE 0.679 versus 0.528 for clinician behavior and AUROC 0.886 for post-72-hour mortality prediction on MIMIC-III.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：电子健康记录（EHR）是多模态、纵向的，包含结构化测量（生命体征、实验室指标）和临床文本（护理记录、影像/微生物报告）。这些数据能反映患者健康演化，但观测高度稀疏、不规则。
- **核心问题**：临床观测是否被记录，本身取决于患者潜在病情和医生决策，即存在**信息性缺失 / MNAR**。此外，结构化测量与临床文本由不同记录机制产生，其观测模式跨模态不同。
- **现有不足**：已有方法多将缺失视为需要插补或容忍的噪声，或只做结构化时序建模；虽有工作显式建模 MNAR，但缺少跨模态、跨时间的动态建模，也少用于离线治疗策略学习。
- **整体含义**：论文主张“观测过程本身携带信息”，应显式利用结构化测量和文本的观测/文档模式，学习动态患者表示，并服务于离线治疗策略优化与结局预测。

## 2. 方法论

### 2.1 核心思想

- 提出 **OPL-MT-MNAR**：Off-Policy Learning under Multimodal Observations with Temporal Missing-Not-At-Random Patterns。
- 两阶段框架：
  - **Stage 1**：从多模态观测中学习动态患者状态表示；
  - **Stage 2**：用学到的状态做离线策略优化和结局预测。
- 核心结合：MNAR 感知多模态编码 + 贝叶斯滤波/VAE 潜信念状态 + 动作条件动态 + IQL 离线策略学习。

### 2.2 Stage 1：患者状态表示学习

- **结构化观测编码**：
  - 基于 **GRU-D**，对缺失变量用“上次观测值向经验均值衰减”的方式处理。
  - 引入显式 MNAR 特征：时间间隔、累计观测计数、累计缺失率、窗口内观测频率。
  - 这些特征与测量值一起进入 GRU-D 门控，捕捉监测强度与病情严重度的关联。
- **临床文本编码与融合**：
  - 文本用 ClinicalBERT 编码。
  - 构造**文档过程因子**：由文本是否存在、距上次文本时间、近期文档密度，经 MLP 和 GRU 更新得到。
  - 用结构化嵌入对文本嵌入做**多头跨注意力**；文本缺失时使用可学习的缺失嵌入。
  - 用门控机制融合结构化表示与文本表示，门控受文档过程因子影响，从而区分“无文本、旧文本、刚更新文本”等不同情况。
- **潜信念状态与贝叶斯滤波**：
  - 用 VAE 建模潜状态 \(z_h\)，其转移为动作条件动态：\(p(z_{h+1}|z_h,\phi_h,a_h)\)。
  - 后验 \(q(z_{h+1}|\phi_{h+1},x)\) 在训练时利用下一步观测。
  - 最终患者状态 \(s_h = g_\theta(\phi_h,z_h)\)，实现中采用残差形式 \(s_h=\phi_h+\text{proj}(z_h)\)。
- **理论动机**：
  - 论文证明：若潜动态不依赖动作，则未来奖励对当前动作的梯度为 0，策略无法学习早期干预对长期结局的影响。
  - 因此，动作条件潜动态对离线序贯决策是必要的。
- **状态验证**：
  - 通过重建损失验证状态是否保留结构化观测、缺失掩码、文本内容和文档过程信息。

### 2.3 Stage 2：策略学习与结局预测

- **离线策略优化**：
  - 采用 **Implicit Q-Learning (IQL)**。
  - 双 Q 网络缓解过估计；价值函数用 expectile 回归；策略通过优势加权行为克隆提取。
  - 优势权重截断，避免过度偏离医生行为。
- **结局预测**：
  - 在 72 小时窗口内存活患者上预测后续院内死亡等结局。
  - 多任务联合学习，使表示同时受益于 RL 奖励和辅助监督信号。
- **训练流程**：
  - 三阶段：表示预训练 → 冻结编码器训练 RL → 联合微调。
  - 监控策略熵和后验坍缩；采用 KL 退火、free-bits、动作条件等缓解后验坍缩。

## 3. 实验设计

### 3.1 数据集与场景

- **MIMIC-III**：主 benchmark，15,415 ICU stays，13.2% 死亡率；高频护理文档，护理笔记覆盖 94.2% 决策步，影像/微生物文本覆盖 41.3% / 28.6%。
- **MIMIC-IV**：32,837 ICU stays，11.8% 死亡率；低频诊断文本，影像/微生物覆盖 83.6% / 45.5%。
- **eICU**：24,562 ICU stays，12.1% 死亡率；跨机构、无文本，用于泛化测试。
- **任务设定**：ICU 脓毒症，72 小时观察窗口，4 小时决策步，共 18 步；动作空间 9 个（3 级液体 × 3 级血管加压药）。
- **防泄漏**：文本仅使用时间戳不晚于当前决策步的报告。

### 3.2 Benchmark 与指标

- 主指标：**Fitted Q-Evaluation (FQE)**，避免重要性加权在策略偏离医生时
