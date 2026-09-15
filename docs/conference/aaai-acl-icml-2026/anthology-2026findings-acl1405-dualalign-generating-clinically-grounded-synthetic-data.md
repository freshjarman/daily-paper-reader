---
title: "DualAlign: Generating Clinically Grounded Synthetic Data"
title_zh: DualAlign：生成临床可信的合成数据
authors: "Rumeng Li, XWang, Hong Yu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.findings-acl.1405.pdf"
tags: ["query:ehr-es"]
score: 7.0
evidence: 隐私保护合成EHR叙述生成
tldr: 电子健康记录受隐私约束、罕见病标注稀缺且存在人群偏差，因此合成临床数据至关重要，但LLM生成文本难以兼顾临床可信与下游可用。本文提出疾病无关框架DualAlign，通过人格对齐（以人口学与风险因素为条件）与症状轨迹对齐提升生成保真度。实验显示其能生成隐私保护且临床忠实的合成EHR叙述，助力下游建模。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1405/fig-001.webp\", \"caption\": \"\", \"page\": 3, \"index\": 1, \"width\": 1998, \"height\": 573}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1405/fig-002.webp\", \"caption\": \"\", \"page\": 5, \"index\": 2, \"width\": 456, \"height\": 501}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1405/fig-003.webp\", \"caption\": \"\", \"page\": 7, \"index\": 3, \"width\": 2868, \"height\": 962}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1405/fig-004.webp\", \"caption\": \"\", \"page\": 19, \"index\": 4, \"width\": 2992, \"height\": 1408}]"
motivation: EHR隐私约束与标注稀缺使合成临床数据需求迫切。
method: 提出DualAlign，用人口学人格对齐与症状轨迹对齐生成合成EHR叙述。
result: 生成隐私保护且临床可信的合成数据，支持下游建模。
conclusion: 为疾病无关的合成EHR生成提供了双重对齐框架。
---

## Abstract
Synthetic clinical data are essential for advancing AI in healthcare, given strict privacy constraints on electronic health records (EHRs), the scarcity of annotated data for rare or slowly progressing conditions, and demographic biases in observational cohorts. Large language models (LLMs) can generate fluent clinical text, but ensuring that such outputs are both clinically grounded and useful for downstream modeling remains challenging. We present DualAlign, a disease-agnostic framework for generating privacy-preserving, clinically faithful synthetic EHR narratives. DualAlign improves generation fidelity through two complementary alignment mechanisms: persona alignment, which conditions generation on patient demographics and risk factors, and symptom-trajectory alignment, which grounds narratives in empirically observed longitudinal symptom patterns. Using Alzheimer’s disease (AD) as a case study, DualAlign produces context-aware, symptom-rich sentences that more closely reflect real-world clinical documentation. Augmenting limited gold-standard data with DualAlign substantially improves AD symptom classification, outperforming both gold-only training and unconstrained synthetic baselines. Overall, DualAlign provides a generalizable approach for generating high-utility synthetic clinical text in chronic and progressive diseases, reducing annotation burden while enabling scalable and privacy-conscious clinical NLP research.

---

## 论文详细总结（自动生成）

# DualAlign 论文中文结构化总结

> 论文：DualAlign: Generating Clinically Grounded Synthetic Data  
> 会议：ACL 2026 Findings，pp. 28189–28208  
> 作者：Rumeng Li, Xun Wang, Hong Yu

## 1. 核心问题与整体含义

- **研究动机**：电子健康记录受隐私法规、机构政策和合规要求限制，难以自由共享；罕见或缓慢进展疾病的标注数据稀缺；观察性队列常存在人口学偏差。因此，隐私保护的合成临床数据对医疗 AI 研究至关重要。
- **核心问题**：LLM 虽能生成流畅临床文本，但现有方法多依赖表格摘要、短文本片段或孤立段落，缺少临床上下文、症状覆盖、时间一致性和事实保真度，难以直接用于下游建模，尤其在阿尔茨海默病（AD）等慢性进展性疾病中更突出。
- **整体含义**：论文提出疾病无关框架 **DualAlign**，通过“人格对齐”和“症状轨迹对齐”生成隐私保护、临床可信、症状丰富的合成 EHR 叙述，并用 AD 作为案例验证其能提升下游症状分类，减少对大量人工标注的依赖。

## 2. 方法论

- **核心思想**：将合成生成分解为两个可控对齐机制：
  - **Persona alignment**：以人口学特征和 AD 风险因素为条件，生成多样化且人口学一致的患者画像。
  - **Symptom-trajectory alignment**：以真实世界观察到的纵向症状模式为基础，约束叙事中的症状出现、类别和时间趋势。
- **真实世界基础**：
  - 使用 VA Corporate Data Warehouse 构建 AD 队列，共 **35,308 名患者**：需至少两次 AD 诊断，且至少一次由神经科、精神科、老年医学等专科提供者记录。
  - 提取 2000–2022 年纵向临床笔记，覆盖初级保健、急诊、神经科、记忆门诊、精神科等场景。
- **患者画像生成**：
  - 因 VA 队列不具全国代表性，按 2024 Alzheimer’s Disease Facts and Figures 对年龄、性别、种族/族裔重新加权采样。
  - 纳入医学共病、神经精神状况、生活方式、心理社会压力源、结构性障碍等 AD 风险因素和 SDOH。
- **时间对齐**：
  - 为每位合成患者模拟诊断前 **10 年** 的笔记轨迹。
  - 笔记数量和类型与 VA 队列经验模式对齐，并映射到 AD 阶段，如早期前驱期、MCI、轻度痴呆、中度痴呆。
  - 初级保健在各时期占主导，专科就诊在诊断前最后几年增加。
- **语义对齐**：
  - 构建 **122 个 AD 相关术语** 的词表，由六位临床/研究专家验证，覆盖六大症状域：语言、记忆、学习/感知、协助需求、生理变化、神经精神症状。
  - 分析关键词在真实笔记中的时间频率和类别比例；真实笔记症状稀疏，平均每篇 2.7–4.2 个提及，因此施加 **5× 密度乘子**，同时保持类别比例。
  - 生成时顺序执行：采样提及数量 → 分配症状类别 → 从对应词表选词 → 嵌入结构化提示。
- **生成与标注**：
  - 使用结构化提示生成 SOAP 风格临床笔记，并变化措辞、缩写和文档风格。
  - 合成队列含 **100 名患者**，每名患者最多 10 年历史，中位 **106 篇笔记**，平均长度 138 tokens。
  - 使用 LLM 标注器按五类标签进行句子级标注：认知损伤、他人担忧、功能损伤、生理变化、神经精神症状，共产生 **233,014 条标注句子**。
  - 论文强调标注基于临床意义和功能变化，而非关键词重叠，以降低关键词—标签泄漏风险。

## 3. 实验设计

- **Benchmark**：
  - 使用 gold 数据集：**11,571 条人工标注句子**，来自 76 名真实 AD 患者的 **5,112
