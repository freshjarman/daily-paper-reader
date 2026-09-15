---
title: Experience Retrieval-Augmentation with Electronic Health Records Enables Accurate Discharge QA
title_zh: 基于电子健康记录的经验检索增强实现准确的出院问答
authors: "Justice Ou, Tinglin Huang, Yilun Zhao, Ziyang Yu, Peiqing Lu, Yifei Shen, Rex Ying"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.acl-long.1073.pdf"
tags: ["query:ehr-es"]
score: 5.0
evidence: 基于电子健康记录的检索增强临床推理
tldr: 该工作针对大模型在临床应用中仅依赖通用医学知识、缺乏真实病例经验上下文的问题。作者提出基于电子健康记录的ExpRAG经验检索增强框架，通过由粗到细的检索流程和基于EHR的报告排序器识别相似患者并提取相关上下文。方法为临床推理提供来自其他患者出院报告的病例级知识支持，提升出院问答的准确性与可靠性。其贡献在于将EHR检索增强用于临床问答，与EHR事件流建模主题相关但侧重问答任务。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1073/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 542, \"height\": 519}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1073/fig-002.webp\", \"caption\": \"\", \"page\": 3, \"index\": 2, \"width\": 2440, \"height\": 925}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1073/fig-003.webp\", \"caption\": \"\", \"page\": 13, \"index\": 3, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1073/fig-004.webp\", \"caption\": \"\", \"page\": 13, \"index\": 4, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1073/fig-005.webp\", \"caption\": \"\", \"page\": 13, \"index\": 5, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1073/fig-006.webp\", \"caption\": \"\", \"page\": 13, \"index\": 6, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1073/fig-007.webp\", \"caption\": \"\", \"page\": 13, \"index\": 7, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1073/fig-008.webp\", \"caption\": \"\", \"page\": 13, \"index\": 8, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1073/fig-009.webp\", \"caption\": \"\", \"page\": 13, \"index\": 9, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1073/fig-010.webp\", \"caption\": \"\", \"page\": 13, \"index\": 10, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1073/fig-011.webp\", \"caption\": \"\", \"page\": 13, \"index\": 11, \"width\": 512, \"height\": 512}]"
motivation: 大模型临床推理仅依赖通用医学知识，缺乏真实病例经验上下文，影响可靠性与准确性。
method: 提出基于电子健康记录的ExpRAG框架，用由粗到细检索与EHR报告排序器获取相似患者上下文。
result: 方法从其他患者出院报告中检索相关经验上下文，提升出院问答等临床推理任务表现。
conclusion: 将EHR检索增强引入临床问答，为可信临床推理提供病例级知识支撑。
---

## Abstract
To improve the reliability of Large Language Models (LLMs) in clinical applications, retrieval-augmented generation (RAG) is extensively applied to provide factual medical knowledge. However, beyond general medical knowledge from open-ended datasets, clinical case-based knowledge is also critical for effective medical reasoning, as it provides context grounded in real-world patient experiences. Motivated by this, we propose Experience Retrieval-Augmentation ExpRAG framework based on Electronic Health Record(EHR), aiming to offer the relevant context from other patients’ discharge reports. ExpRAG performs retrieval through a coarse-to-fine process, utilizing an EHR-based report ranker to efficiently identify similar patients, followed by an experience retriever to extract task-relevant content for enhanced medical reasoning. To evaluate ExpRAG, we introduce DischargeQA, a clinical QA dataset with 1,280 discharge-related questions across diagnosis, medication, and instruction tasks. Each problem is generated using EHR data to ensure realistic and challenging scenarios. Experimental results demonstrate that ExpRAG consistently outperforms a text-based ranker, achieving an average relative improvement of 5.2%, highlighting the importance of case-based knowledge for medical reasoning.

---

## 论文详细总结（自动生成）

# 论文总结：基于电子健康记录的经验检索增强实现准确的出院问答

## 1. 核心问题与研究动机

- **背景**：大语言模型（LLM）在医疗领域展现出复杂推理潜力，但存在幻觉与领域知识不足的问题，限制其在真实临床场景中的可靠性。
- **现有方案的局限**：传统检索增强生成（RAG）多从开放数据库（如 Wikipedia 药物描述）检索通用医学事实，这类知识虽能补充事实性概念，却难以应对真实临床病例中常见的**多病症共存**情形。
- **核心洞察**：作者指出，除通用医学事实外，**临床病例级经验**同样关键——经验丰富的临床医生常依赖既往相似病例来指导诊断、治疗决策与出院规划。
- **研究目标**：提出基于电子健康记录（EHR）的**经验检索增强框架 ExpRAG**，从其他患者的出院报告中检索相关上下文，为 LLM 的医学推理提供真实世界临床经验支撑。
- **整体含义**：该工作将 EHR 从"结构化数据源"拓展为"病例经验知识库"，强调病例级相似性检索在临床决策中的价值，与通用事实检索形成互补。

## 2. 方法论

### 2.1 核心思想
- 采用**由粗到细（coarse-to-fine）**的两阶段检索：先通过 EHR 结构化数据快速筛选相似患者，再通过文本检索器从候选患者的出院报告中抽取任务相关内容。
- 任务形式化：给定患者 $p$、医学查询 $q$ 和出院报告集合 $\mathcal{D}=\{D_i\}$，目标为 $d^* = f_{\text{ExpRAG}}(p, q, \mathcal{D})$。

### 2.2 关键技术细节

- **第一阶段：EHR-based 报告排序器（Report Ranking）**
  - 利用三类结构化医学实体衡量患者相似度：
    - **诊断**：ICD-10 编码集合 $E_p^{\text{Diag}}$
    - **药物**：NDC 编码集合 $E_p^{\text{Med}}$
    - **手术**：ICD-10 编码集合 $E_p^{\text{Proc}}$
  - 对每个模态计算集合相似度（采用 **Jaccard 指数**，因患者表示为稀疏正例编码集合，共享存在比共享缺失更具临床信息量）：
    - $\tau_{\text{Diag}} = f_{\text{similarity}}(E_p^{\text{Diag}}, E_{p'}^{\text{Diag}})$
    - $\tau_{\text{Med}} = f_{\text{similarity}}(E_p^{\text{Med}}, E_{p'}^{\text{Med}})$
    - $\tau_{\text{Proc}} = f_{\text{similarity}}(E_p^{\text{Proc}}, E_{p'}^{\text{Proc}})$
  - 加权聚合：$\tau = \lambda_1 \tau_{\text{Diag}} + \lambda_2 \tau_{\text{Med}} + \lambda_3 \tau_{\text{Proc}}$，默认 $\lambda_{1/2/3}=1/3$。
  - 返回 top-k 最相似患者的出院报告作为候选池 $D'$。

- **第二阶段：经验检索（Experience Retrieval）**
  - 在候选池 $D'$ 上使用文本检索器抽取与查询相关的内容：$d^* = f_{\text{Retriever}}(q, D')$。
  - 默认使用 **Auto-merging** 检索器，并对比了 Sentence-window、BM25、BM25+、FLARE、Contriever。

- **效率分析**：Jaccard 计算可借助 Faiss、NumPy 加速；结构化实体索引支持快速查找，避免对百万级出院报告全库密集检索。

## 3. 实验设计

### 3.1 数据集 / 场景
- **DischargeQA**：作者构建的临床问答数据集，共 **1,280 个 QA 对**，基于 MIMIC-IV 构建。
  - **诊断推断**：436 题，多选，问题背景为临床概况，选项来自出院报告与 EHR。
  - **药物推断**：444 题，多选，背景含临床概况与住院进展，选项来自出院报告与 EHR。
  - **指令推断**：400 题，单选，背景含临床概况与住院进展，选项来自出院报告与 AI 生成。
- **背景生成**：按出院报告结构（临床概况 → 住院进展 → 出院计划）逐阶段揭示，避免标签泄漏。
- **选项生成**：正确选项直接取自出院报告；干扰项由 EHR 结构化表经 GPT-4o 筛选生成，确保非平凡。

### 3.2 Benchmark 与对比方法
- **对比设置**：
  - **Direct-Ask**：直接提问，无检索增强。
  - **Text-based ranker**：使用 bge-small-en 等嵌入模型对患者级出院报告排序后检索。
  - **ExpRAG EHR**：本文提出的基于 EHR 的排序器。
- **对比 LLM 骨干（共 9 个）**：GPT-3.5、GPT-4o、GPT-5-mini、GPT-5-nano、DeepSeek-R1-8B、DeepSeek-V3.1、Llama-4-17B、Qwen3-30B-A3B、BaichuanM2。
- **额外排序器对比**：all-MiniLM-L6、paraphrase-MiniLM-L3、MedCPT。
- **检索相关性实验**：随机采样 100 个目标患者，各构造 100 个候选，由 GPT-4o-mini 标注相似度，计算 Pearson/Spearman 相关性。

## 4. 资源与算力

- **论文未明确说明**所使用的 GPU 型号、数量、训练时长或总计算量。
- 实验主要基于 **API 调用**（GPT-3.5-turbo-1106、GPT-4o-2024-11-20、GPT-5-mini-2025-08-07 等）及开源模型推理，**无大规模模型训练过程**。
- 解码参数：闭源模型 temperature=0、top-p 默认；Qwen3-30B 使用 temperature=0.6、top-p=0.95。
- 由于缺乏算力细节，无法评估其计算成本与可复现性边界。

## 5. 实验数量与充分性

- **主实验**：9 个 LLM × 3 类任务 × 3 种设置（Direct-Ask、Text-based、ExpRAG），覆盖诊断、药物、指令三大临床决策环节。
- **消融实验**：
  - 平衡系数 $\lambda$ 的 3 种分配策略（均匀、任务聚焦、互补）。
  - 相似患者数 $k \in \{5, 10, 15, 20, 25\}$。
  - 6 种文本检索器对比。
- **排序器对比**：4 种文本/领域嵌入模型 vs. EHR-based ranker。
- **检索相关性实验**：100 目标 × 100 候选的标注与相关性分析。
- **案例研究**：对一例双侧尺神经感觉异常患者的诊断推断进行定性分析。
- **充分性评价**：
  - 优点：实验维度较丰富，覆盖多骨干、多检索器、多超参，且方法排序在不同设置下保持一致。
  - 局限：所有实验均在**单一 MIMIC-IV 队列**内进行，未做跨机构/跨数据集验证；未与最新 KG-based 方法（如 MedRAG、KARE）直接端到端对比；仅使用多选格式评估，未涉及开放式生成。

## 6. 主要结论与发现

- **ExpRAG EHR 在多数指标上取得最强或并列最强结果**，平均相对提升 **5.2%**，优于纯文本排序器。
- **EHR-based ranker 优于文本嵌入排序器**：在与 GPT-4o-mini 标注的相关性对比中，ExpRAG EHR 的 Pearson（0.669）与 Spearman（0.648）均高于 bge-small-en-v1.5、all-MiniLM-L6、paraphrase-MiniLM-L3。
- **多选任务（诊断、药物）显著更难**：多数 LLM 准确率低于 20%，说明当前 LLM 的医学推理能力仍有限。
- **均匀加权（λ 各为 1/3）在多数情况下最优**，表明多临床维度信息互补。
- **k 值影响因任务而异**：指令任务随 k 增大持续提升；诊断/药物任务在 k>20 后出现波动，提示过多检索可能引入无关或冲突信息。
- **Auto-merging 检索器表现最佳**，优于 BM25、Contriever、FLARE 等。
- **案例研究表明**：相似患者的出院报告能提供共享诊断特征（如椎间盘突出、椎管狭窄、上肢神经症状），帮助模型确认目标患者诊断。

## 7. 优点

- **方法设计亮点**：
  - 首次利用**结构化 EHR 相似度**（ICD/NDC 编码 + Jaccard）进行病例级经验检索，避免对全库笔记的密集嵌入。
  - 粗到细框架兼顾**效率与临床相关性**：结构化 gating 先筛候选，再文本检索抽取内容。
  - 仅依赖常规 ICD/NDC 表，**隐私鲁棒性较好**，且可解释性强（每次匹配可追溯至具体编码）。
  - 计算成本低，可作即插即用组件部署于更大系统。

- **数据集亮点**：
  - DischargeQA 聚焦**出院流程**（诊断、药物、指令），填补现有基准空白。
  - 采用**时间感知评估协议**，按决策时间点逐步揭示信息，防止标签泄漏。
  - 正确选项来自临床医生撰写的出院报告，GPT-4o 仅用于生成干扰项，避免循环性。
  - 多选格式模拟真实临床中多病症共存决策，任务难度高。

- **实验亮点**：
  - 覆盖 9 个 LLM、多种检索器与排序器，验证方法泛化性。
  - 引入与 GPT-4o-mini 标注的相关性分析，提供更客观的排序质量评估。

## 8. 不足与局限

- **数据模态有限**：仅使用诊断、药物、手术三类结构化数据，未利用实验室结果、影像报告、生命体征时间序列等，作者承认这是"初始探索"。
- **单队列局限**：评估仅在单一 MIMIC-IV 派生队列内进行，查询患者与候选患者同源，**跨机构/跨数据集泛化性未验证**。
- **任务形式单一**：DischargeQA 目前仅含多选问题，缺乏开放式生成评估，无法全面衡量 LLM 的生成能力。
- **药物任务表现极低**：多数模型准确率不足 10%，F1 低于 0.7，反映任务难度与当前模型能力差距；作者归因于出院用药方案变异大、缺失关键临床上下文（如实验室趋势）。
- **检索噪声问题**：k 值过大时性能波动，说明检索可能引入无关或冲突信息。
- **未与 KG-based 方法端到端对比**：如 MedRAG、KARE 等知识图谱方法未直接比较，定位为"互补"但缺乏实证。
- **算力与成本未披露**：未说明 API 调用成本、推理延迟或计算资源，影响可复现性与部署评估。
- **选项生成依赖 GPT-4o**：干扰项质量与临床合理性依赖 LLM，可能存在潜在偏差。
- **失败分析显示**：23% 失败因检索患者缺乏全部正确答案点，47% 因信息不完整，15% 因数值不准确，说明检索完整性与数值保真度仍是瓶颈。

（完）
