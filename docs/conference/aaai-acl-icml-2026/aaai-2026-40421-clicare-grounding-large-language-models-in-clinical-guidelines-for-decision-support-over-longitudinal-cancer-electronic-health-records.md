---
title: "CliCARE: Grounding Large Language Models in Clinical Guidelines for Decision Support over Longitudinal Cancer Electronic Health Records"
title_zh: CliCARE：将大语言模型接地于临床指南以支持纵向癌症电子健康记录决策
authors: "Dongchen Li, Jitao Liang, Wei Li, Xiaoyu Wang, Longbing Cao, Kun Yu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40421/44382"
tags: ["query:ehr-es"]
score: 7.0
evidence: 面向纵向EHR时序分析的LLM建模
tldr: 针对大模型在纵向癌症电子健康记录决策支持中难以处理冗长碎片化记录、易产生临床幻觉且缺乏可靠评估的问题，本文提出CliCARE，将模型接地于过程导向的临床指南，弥补常规检索增强方法难以融入流程化知识之不足。实验表明该方法提升了长病程记录的时序分析与决策可信度。该工作推进了以基础模型建模EHR事件序列并支撑临床决策的方向。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 大模型处理冗长碎片化的纵向癌症EHR时面临时序分析、幻觉与评估三大挑战。
method: 提出CliCARE，将大模型接地于过程导向的临床指南以增强长记录推理。
result: 提升了纵向EHR时序分析与临床决策支持的可信度。
conclusion: 为以基础模型建模EHR事件序列并支撑决策提供了新范式。
---

## Abstract
Large Language Models (LLMs) hold significant promise for improving clinical decision support and reducing physician burnout by synthesizing complex, longitudinal cancer Electronic Health Records (EHRs). However, their implementation in this critical field faces three primary challenges: the inability to effectively process the extensive length and fragmented nature of patient records for accurate temporal analysis; a heightened risk of clinical hallucination, as conventional grounding techniques such as Retrieval-Augmented Generation (RAG) do not adequately incorporate process-oriented clinical guidelines; and unreliable evaluation metrics that hinder the validation of AI systems in oncology.
To address these issues, we propose CliCARE, a framework for Grounding Large Language Models in Clinical Guidelines for Decision Support over Longitudinal Cancer Electronic Health Records. The framework operates by transforming unstructured, longitudinal EHRs into patient-specific Temporal Knowledge Graphs (TKGs) to capture long-range dependencies, and then grounding the decision support process by aligning these real-world patient trajectories with a normative guideline knowledge graph. This approach provides oncologists with evidence-grounded decision support by generating a high-fidelity clinical summary and an actionable recommendation.
We validated our framework using large-scale, longitudinal data from a private Chinese cancer dataset and the public English MIMIC-IV dataset. In these settings, CliCARE significantly outperforms baselines, including leading long-context LLMs and Knowledge Graph-enhanced RAG methods. The clinical validity of our results is supported by a robust evaluation protocol, which demonstrates a high correlation with assessments made by oncologists.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究动机**：大语言模型（LLM）有望改善临床决策支持、减轻医生负担，但在肿瘤等高风险的纵向电子健康记录（EHR）场景中，实际落地仍面临显著障碍。
- **三大核心挑战**：
  - **长上下文与时序推理困难**：患者记录可跨越多年、超过 20,000 tokens，且碎片化、多语言，LLM 难以进行准确的时间分析与长程依赖建模。
  - **临床幻觉风险高**：常规检索增强生成（RAG）多检索孤立文本片段，难以融入“过程导向”的临床指南，也无法有效建模患者轨迹中的时序依赖。
  - **评估不可靠**：传统自动指标（如 ROUGE、BLEU）难以衡量临床有效性、事实准确性与安全性；LLM-as-a-Judge 又存在位置偏差、冗长偏好等系统性问题。
- **整体含义**：论文主张前沿不只是开发更强模型，而是构建可靠、安全、以专家医学知识为 grounding 的框架，辅助而非替代医生。其目标任务是支持肿瘤医生核心工作流：从多年病史生成**临床摘要（Clinical Summary）**，并据此生成**可操作的临床推荐（Clinical Recommendation）**。

## 2. 方法论：CliCARE 框架

- **核心思想**：将非结构化、纵向癌症 EHR 转化为患者特定**时序知识图谱（Temporal Knowledge Graph, TKG）**，再把真实患者轨迹与规范性**临床指南知识图谱**对齐，为 LLM 提供证据接地的上下文，最终生成高保真临床摘要与可操作推荐。框架可适配通用 LLM 与蒸馏后的专用 LLM。
- **关键技术流程**：
  - **EHR-to-TKG 转换**：
    - 患者文档序列按时间排序，经上下文处理管线压缩、提炼、结构化，形成关键临床事件序列。
    - 使用临床文本预训练的 Longformer 对历史记录做抽取式摘要，最近一次临床记录作为“现病史”，二者拼接后由 BERT 抽取诊断、分期、治疗方案、生物标志物趋势、影像评估等事实。
    - 构建患者中心 TKG：\(G_t=(E_t,R_t,T)\)，并通过实体链接函数将文本提及映射到静态生物医学知识图谱中的标准概念。实体表示为标准实体、时间戳和事件属性的组合。
    - 时间粒度分层：宏观临床就诊赋予精确时间戳，就诊内事件用相对时间关系连接，以贴近真实临床记录结构。
  - **轨迹-指南对齐（Trajectory-Guideline Alignment）**：
    - 指南知识图谱 \(G_g=(E_g,R_g)\) 基于权威临床实践指南构建，节点为抽象医学概念，边为逻辑与推荐关系。
    - 将患者 TKG 组织为时间有序轨迹 \(Tr_p=\langle e_1,\dots,e_m\rangle\)，并枚举指南路径 \(Pa_k=\langle s_1,\dots,s_l\rangle\)。
    - **相似度匹配**：用生物医学 BERT 计算每个指南步骤与患者轨迹中最相似事件的余弦相似度，并求和得到路径匹配分数；选择最高分路径作为最优对齐。公式思想为：  
      \(Score(Tr_p,Pa_k)=\sum_j \max_{e_i} \cos\_sim(f_{BERT}(desc(s_j)), f_{BERT}(desc(e_i)))\)，再取 \(Pa^*=\arg\max Score\)。
    - **LLM 重排序**：以零样本方式向 LLM 提供患者轨迹、Top-N 候选指南路径及匹配分数，让 LLM 作为临床推理器输出重排后的路径列表。
    - **对齐扩展**：受 bootstrapping 启发，以重排后最高路径及其节点对为高置信种子集，对未对齐事件选择与已有种子对一致性最高的指南节点，逐步扩展对齐关系。公式思想为选择使与种子集一致性得分之和最大的指南节点。
    - 最后将患者轨迹证据融合进指南知识图谱，形成证据融合知识表示，作为 LLM 生成临床摘要和推荐的直接上下文。
- **评估方法**：设计 Expert-Validated LLM-as-a-Judge，使用与资深肿瘤医生共同设计的四维评分标准：事实准确性、完整性与彻底性、临床合理性、可操作性与相关性，每维 1–5 分。为缓解偏差，使用三个强 LLM 组成评审集成并取平均分，同时随机打乱展示顺序；再用 Spearman 秩相关验证与人类专家评分的一致性。

## 3. 实验设计

- **数据集/场景**：
  - **CancerEHR（私有中国数据集）**：来自辽宁癌症医院的 2,000 名患者纵向记录，部分跨度超过二十年，输入可达 20,000 tokens，包含医嘱、实验室结果、手术记录等多种数据类型。
  - **MIMIC-Cancer（公共英文数据集）**：从公开 MIMIC-IV 中筛选癌症相关诊断患者，用于测试跨语言、跨数据结构的泛化性。
  - 两个数据集分别简称为 \(D_{CEHR}\) 和 \(D_{MC}\)。
- **任务与 Benchmark**：
  - **TCS**：回顾性临床摘要。
  - **TCR**：前瞻性临床推荐。
  - 评估基准为上述 Expert-Validated LLM-as-a-Judge 四维评分协议，并用专家评分验证其可靠性。
- **对比方法**：
  - 标准 RAG 管线：Mistral-7B、Mistral-Instruct-v0.1-7B、BioMistral-7B、Qwen3-8B。
  - KG 增强 RAG / 长上下文方法：BriefContext、MedRAG、KG2RAG、GNN-RAG。
  - 通用强模型：Deepseek-R1、Gemini 2.5 Pro、GPT-4.1、Claude-4.0-Sonnet。
- **主要实验表格**：
  - 表 1：Qwen-3-8B 与 Gemini 2.5 Pro 下，CliCARE 与 Standard RAG、BriefContext、MedRAG、KG2RAG、GNN-RAG 对比。
  - 表 2：7 个模型在 Standard RAG 与 CliCARE 下的性能提升对比。
  - 表 3：消融实验，移除 Alignment Expansion、LLM-based Reranking、TKG-based Compression。
  - 表 4：按 EHR 长度分层（短/中/长）分析性能。

## 4. 资源与算力

- 论文明确提到：
  - 使用 **4 张 NVIDIA A800 GPU**。
  - 训练设置：2,000 样本中 1,800 为训练集、200 为测试集，训练集中 10% 作验证；batch size 为 1；最大上下文长度 20,000 tokens；初始学习率 \(5\times10^{-5}\)，余弦调度；BF16 混合精度；最大输出长度 4,096 tokens；训练 3 个 epoch。
  - 知识图谱对齐阶段，BERT 语义余弦相似度阈值设为 0.7。
- **未明确说明**：训练总时长、总 GPU 小时、能耗、推理成本等未给出。因此无法从文中判断完整算力开销。

## 5. 实验数量与充分性

- **实验规模大致包括**：
  - 2 个数据集 × 2 个任务（TCS/TCR）的主实验。
  - 表 1：2 种模型设置下，与多类 RAG/KG-RAG 基线对比。
  - 表 2：7 个模型分别在 Standard RAG 与 CliCARE 下的成对比较。
  - 表 3：2 个代表模型 × 2 个数据集 × 2 个任务 × 3 个消融组
