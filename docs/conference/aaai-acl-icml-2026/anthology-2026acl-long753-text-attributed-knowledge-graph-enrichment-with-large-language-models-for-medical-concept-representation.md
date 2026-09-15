---
title: Text-Attributed Knowledge Graph Enrichment with Large Language Models for Medical Concept Representation
title_zh: 面向医学概念表示的文本属性知识图大语言模型增强
authors: "Mohsen Nayebi Kerdabadi, Arya Hadizadeh Moghaddam, Chen Chen, Dongjie Wang, Zijun Yao"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.acl-long.753.pdf"
tags: ["query:ehr-es"]
score: 6.0
evidence: 面向下游临床预测的EHR医学概念表示学习
tldr: 在EHR挖掘中，学习高质量的医学概念（诊断、药物、操作编码）表示是下游临床预测的基础，但现有本体资源常缺失跨类型依赖，且丰富的临床语义难以与知识图结构融合。本文提出用大语言模型对文本属性知识图进行增强，补齐诊断-药物、药物-操作等跨类型关系，并将文本语义整合进图结构以改进表示学习。该方法提升了医学概念表示质量，从而支持更准确的临床预测任务。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long753/fig-001.webp\", \"caption\": \"\", \"page\": 3, \"index\": 1, \"width\": 1305, \"height\": 703}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long753/fig-002.webp\", \"caption\": \"\", \"page\": 4, \"index\": 2, \"width\": 832, \"height\": 1296}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long753/fig-003.webp\", \"caption\": \"\", \"page\": 13, \"index\": 3, \"width\": 1797, \"height\": 1165}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long753/fig-004.webp\", \"caption\": \"\", \"page\": 17, \"index\": 4, \"width\": 1603, \"height\": 790}]"
motivation: EHR医学概念表示受限于跨类型依赖缺失与临床语义难以融合，影响下游预测。
method: 用大语言模型增强文本属性知识图，补齐跨类型关系并融合文本语义。
result: 提升了医学概念表示质量，改善下游临床预测表现。
conclusion: 为EHR概念表示学习提供了知识图与大模型结合的有效方案。
---

## Abstract
In electronic health record (EHR) mining, learning high-quality representations of medical concepts (e.g., standardized diagnosis, medication, and procedure codes) is fundamental for downstream clinical prediction. However, robust concept representation learning is hindered by two key challenges: (i) clinically important cross-type dependencies (e.g., diagnosis-medication and medication-procedure relations) are often missing or incomplete in existing ontology resources, limiting the ability to model complex EHR patterns; and (ii) rich clinical semantics are often missing from structured resources, and even when available as text, are difficult to integrate with KG structure for representation learning. To address these challenges, we present MedCo, an LLM-empowered graph learning framework for medical concept representation. MedCo first builds a global knowledge graph (KG) over medical codes by combining statistically reliable associations mined from EHRs with type-constrained LLM prompting to infer semantic relations. It then utilizes LLMs to enrich the KG into a text-attributed graph by generating node descriptions and edge rationales, providing semantic signals for both concepts and their relationships. Finally, MedCo jointly trains a LoRA-tuned LLaMA text encoder with a heterogeneous GNN, fusing text semantics and graph structure into unified concept embeddings. Extensive experiments on MIMIC-III and MIMIC-IV show that MedCo consistently improves prediction performance and serves as an effective plug-in concept encoder for standard EHR pipelines.

---

## 论文详细总结（自动生成）

# 论文总结：MEDCO——基于大语言模型增强文本属性知识图的医学概念表示

## 1. 核心问题与整体含义（研究动机与背景）

- **背景**：在电子健康记录（EHR）挖掘中，学习高质量的医学概念表示（标准化的诊断 dx、药物 rx、操作 px 编码）是下游临床预测任务的基础。
- **核心挑战一**：临床重要的**跨类型依赖关系**（如诊断-药物、药物-操作关系）在现有本体资源（ICD、CCS、ATC、SNOMED CT、UMLS）中往往缺失或残缺，导致难以建模复杂的 EHR 模式。
- **核心挑战二**：结构化资源中缺乏丰富的**临床语义**；即使以文本形式存在，也难以与知识图（KG）结构有效融合用于表示学习。
- **关键张力**：LLM 虽编码广泛生物医学知识，但无约束提示会产生"看似合理却无证据支持"的边，且同一概念输出不一致；因此临床 KG 构建必须**证据驱动、类型感知、全局一致**。
- **整体含义**：论文提出 **MEDCO**，一个 LLM 赋能的图学习框架，旨在构建临床可解释、经验证支持的知识图，并通过 KG-LLM 协同学习获得统一医学概念嵌入。

## 2. 方法论

### 核心思想
构建证据驱动的异质知识图，将其增强为**文本属性图**，再通过 LoRA 微调的 LLaMA 文本编码器与异质 GNN 的**端到端协同训练**，融合文本语义与图结构。

### 四步流程
1. **证据抽取（Evidence Extraction）**：从 EHR 中计算**就诊内共现**与**下次就诊转移**统计，保留统计显著的编码对。
2. **KG 归纳（KG Induction）**：使用**类型约束、证据条件化**的 LLM 提示，分配有向关系类型、置信度与推理依据。
3. **KG 增强（KG Enrichment）**：LLM 生成节点描述（诊断/操作/药物的临床表现、适应证等）与边元数据（关系标签、置信度、理由、统计指标）。
4. **协同学习（Co-Learning）**：联合训练 LoRA 微调的 LLaMA 编码器与关系感知 GNN。

### 关键技术细节
- **三元统计证据**（用于候选边过滤）：
  - 平滑条件概率：$P(c_j|c_i) = \frac{x(c_i,c_j)+\alpha}{x(c_i)+\alpha|C|}$（Laplace 平滑缓解稀疏）
  - PMI 式关联：$\text{PMI}(c_i,c_j)=\log_2\frac{p(c_i,c_j)}{p_{src}(c_i)p_{tgt}(c_j)}$
  - 卡方显著性检验（2×2 列联表，p>0.05 的边被剔除）
- **类型约束关系池**：覆盖 dx-dx、rx-dx、px-dx、rx-rx、px-px、px-rx 六类组合，共 **28 种**临床关系（如 causes、treats、contraindicated_for、sequential_care 等），并提供保守弃权标签（no_significant_relation、cannot_decide）。
- **结构化提示**：输入编码标识、文本名、父类、边缘频率、8 项统计指标、候选关系、决策规则；输出严格 JSON（单一关系标签、有向三元组、校准置信度、50–60 词推理）。
- **LLM-GNN 架构**：LLaMA 编码节点描述 $z_i^{text}=f_\theta(s_i)$，经类型专属线性映射得到 $h_i^{(0)}=W_{\tau(i)}z_i^{text}$，初始化关系感知异质 GNN 进行消息传递（MSG/AGG/UPDATE）。
- **两阶段采样调度**：早期"最少更新优先"确保长尾编码覆盖；后期混合最少更新与高频编码，摊销 LLM 计算并避免更新不均衡。
- **下游集成**：学到的概念嵌入矩阵 $Z$ 供标准 EHR 主干使用，以多标签交叉熵训练。

## 3. 实验设计

- **数据集**：MIMIC-III（7,515 患者，12,430 样本，515 个诊断标签）与 MIMIC-IV（18,829 患者，25,028 样本，562 个标签）。ICD 映射到 CCS，NDC 映射到 ATC。
- **任务**：下次就诊诊断预测（多标签、类别不均衡）。
- **评估指标**：AUPRC（按标签频率分层）、Acc@k（k=15/20/30）、F1；5 折平均。
- **对比方法**：
  - 主干：AdaCare、Transformer、RETAIN、TCN（插件式对比）
  - 概念编码器基线：GRAM、MMORE、KAME、HAP、G-BERT、ADORE（SNOMED）、KAMPNet、GraphCare（UMLS+LLM）、LINKO
- **研究问题**：RQ1 插件增强效果；RQ2 与现有编码器对比；RQ3 组件/边类别消融；RQ4 数据稀缺与稀有病症表现。
- **额外实验**：LLM 主干敏感性（Llama-3.2-1B、Gemma-2-2B、Qwen2.5-1.5B/0.5B、SmolLM2-1.7B）、成本-精度权衡、临床专家审计。

## 4. 资源与算力

- **硬件明确说明**：Intel Xeon Silver 4214R CPU（24 核）、256 GiB RAM、**1 张 RTX A6000 GPU（48 GB）**。
- **训练时长**（batch size 128，MIMIC-IV 每 epoch）：
  - 无 KG/LLM 基线：22.0 s
  - 仅 GNN：42.7 s
  - LLM LoRA + GNN（K=5）：183.4 s；（K=10）：275.4 s
- **显存**：峰值训练内存最高 24,260 MiB（LoRA K=10）；推理峰值 518 MiB（KG 变体），基线 106 MiB。
- **推理效率**：推理时移除 LLM，使用缓存的节点表示 + GNN + 下游编码器，部署轻量。
- **配置**：LoRA rank r=8、α=32；GNN 2 层、每层 1 个注意力头、dropout 0.4。

## 5. 实验数量与充分性

- **实验规模**：涉及 2 个数据集、4 个下游主干（插件分析）、约 10 个概念编码器基线、组件消融（4 级递进）、6 类边消融、5 个 LLM 主干、4 个训练集比例（25%/50%/75%/100%）、成本-精度对比、50 条边的临床专家审计。
- **充分性**：整体较充分——覆盖多数据集、多主干、多 LLM、分层稀有度分析、数据稀缺分析和人工临床验证。
- **客观公平性**：所有编码器集成到**同一下游主干**进行受控比较；报告 5 折均值；消融递进清晰。
- **潜在不足**：专家审计仅 50 条边（每关系类型 5 条），规模有限；对比方法实现细节（如是否统一调参）未完全披露。

## 6. 主要结论与发现

- **插件有效性（RQ1）**：MEDCO 在所有 4 个主干部显著提升性能，是有效的即插即用概念编码器。
- **基线对比（RQ2）**：MEDCO 整体最优——MIMIC-III AUPRC 47.21（次优 LINKO 44.91）；MIMIC-IV AUPRC 50.00（次优 LINKO 48.14），且在稀有标签（0–25% 分位）提升最显著。
- **消融（RQ3）**：加入 KG 带来最大增益；边特征、LLM 节点描述（冻结）逐步提升；LoRA 微调最佳。边类别中 px-px、dx-rx、rx-rx 移除后性能下降最大。
- **数据稀缺（RQ4）**：训练数据减少时 MEDCO 仍带来显著增益，鲁棒性强。
- **LLM 敏感性**：不同开源 LLM 主干性能稳定（AUPRC 49.31–50.31），更大模型增益有限，说明性能主要由证据驱动 KG 与图传播贡献。
- **临床有效性**：50 条采样边专家评分均值 4.84±0.29，各关系类型均 ≥4.40，表明幻觉风险受控。

## 7. 优点

- **证据驱动与临床约束并重**：统计过滤 + 类型约束提示 + 弃权标签，有效抑制无支持边的生成。
- **文本属性图建模**：将 LLM 生成节点描述与边理由融入图结构，兼顾关系表达力与语义丰富度。
- **协同学习机制**：LoRA 微调 LLM 与异质 GNN 端到端训练，两阶段采样调度平衡计算成本与长尾覆盖。
- **即插即用灵活性**：可集成到多种标准 EHR 主干，且推理时移除 LLM，部署轻量。
- **实验严谨**：多数据集、多主干、分层稀有度分析、数据稀缺分析、LLM 主干敏感性、成本-精度前沿，并附**独立临床专家审计**验证。

## 8. 不足与局限

- **计算成本**：联合 KG-LLM 训练仍资源密集；扩展到更大词表、更长上下文或更大 LLM 时成本上升（作者自述局限）。
- **任务与数据覆盖有限**：仅验证"下次就诊诊断预测"单一任务，仅用 MIMIC-III/IV 两个公开数据集，泛化性未在更多临床场景验证。
- **审计规模小**：临床验证仅 50 条边、2 名评审，统计代表性有限，无法全面反映全图质量。
- **关系语境依赖**：许多临床关系随队列、护理环境与时间变化，静态全局图可能无法捕捉动态语境。
- **偏差风险**：LLM 生成描述与关系可能继承预训练数据的偏差；尽管未向 LLM 发送患者级数据，但概念级知识仍受模型知识边界约束。
- **对比公平性细节**：部分基线（如 GraphCare、LINKO）的实现与调参细节披露有限，可能影响对比的绝对公平性。

（完）
