---
title: "MultiDx: A Multi-Source Knowledge Integration Framework towards Diagnostic Reasoning"
title_zh: MultiDx：面向诊断推理的多源知识整合框架
authors: "Yimin Deng, Zhenxi Lin, Yejing Wang, Guoshuai Zhao, Pengyue Jia, Zichuan Fu, Derong Xu, Yefeng Zheng, Xiangyu Zhao, Li Zhu, Xian Wu, Xueming Qian"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.findings-acl.1646.pdf"
tags: ["query:ehr-es"]
score: 6.0
evidence: 诊断推理与鉴别诊断预测
tldr: 该工作针对大语言模型在诊断推理中受限于领域知识、且仅关注最终预测准确率而忽视与标准临床推理轨迹对齐的问题，提出两阶段诊断推理框架MultiDx。方法从多个知识源收集证据进行鉴别诊断，并强调与临床推理路径的一致性。实验表明该框架在诊断预测与推理对齐方面取得改进。其为基于多源知识整合的疾病诊断提供了思路，但未聚焦EHR序列建模本身。
source: ACL-2026-Findings
selection_source: conference_retrieval
motivation: LLM诊断推理受限于领域知识，且仅追求预测准确率而忽视与临床推理轨迹对齐。
method: 提出两阶段诊断推理框架，整合多知识源证据进行鉴别诊断并对齐临床推理路径。
result: 在诊断预测与临床推理轨迹对齐方面相较基线取得改进。
conclusion: 为多源知识整合的疾病诊断提供思路，但未深入EHR事件序列建模。
---

## Abstract
Diagnostic prediction and clinical reasoning are critical tasks in healthcare applications. While large language models have shown strong capabilities in commonsense reasoning, they still struggle with diagnostic reasoning due to limited domain knowledge. Existing approaches often rely on internal model knowledge or static knowledge bases, which are insufficient to support the knowledge demands of diagnostic reasoning. Moreover, these methods focus solely on the accuracy of final predictions, overlooking alignment with standard clinical reasoning trajectories. To this end, we propose MultiDx, a two-stage diagnostic reasoning framework that performs differential diagnosis by analyzing evidence collected from multiple knowledge sources. Specifically, it first generates suspected diagnoses and reasoning traces by leveraging knowledge from web search, SOAP-formatted case, and clinical case database. Then it integrates multi-perspective evidence through matching, voting, and differential diagnosis to generate the final prediction. Extensive experiments demonstrate the effectiveness of our approach.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义
- **研究动机**：诊断预测与临床推理是医疗 AI 的关键任务，但 LLM 虽在常识推理上表现强，在诊断推理中仍受限于**领域知识不足**。
- **现有方法问题**：
  - 依赖模型内部知识或静态知识库，导致知识不足、适应性有限，尤其面对未见或罕见病例时更明显。
  - 多聚焦最终预测准确率，忽视与**标准临床推理轨迹**的对齐，导致可解释性、可验证性和临床可信度不足。
- **整体含义**：论文提出 **MultiDx**，一个两阶段诊断推理框架，通过整合多源知识进行鉴别诊断，同时生成更符合临床标准的推理路径，以提升诊断准确性与推理质量。

## 2. 方法论
### 2.1 核心思想
- 采用**两阶段框架**：
  1. **多源知识引导的诊断生成**：从 Web 搜索、SOAP 结构化病例、临床病例数据库等来源分别生成疑似疾病列表及推理依据。
  2. **证据整合与鉴别诊断**：通过疾病匹配、投票聚合、鉴别诊断和重排序，生成最终诊断与推理轨迹。
- 设计目标是对齐临床诊断流程：先形成疑似疾病列表，再进行鉴别诊断。

### 2.2 关键技术细节
- **SOAP 结构化**：
  - 将非结构化病例转为 Subjective、Objective、Assessment、Plan 四部分。
  - 因输入通常不含初步诊断和治疗计划，生成的 SOAP 中 Assessment 和 Plan 标记为缺失。
  - 公式：`C_SOAP = LLM(I_toSOAP, C)`，`H_SOAP = LLM(I_SOAP, C_SOAP)`。
- **医学病例数据库检索**：
  - 使用 BM25 检索 top-k 相似病例：`TopK(C) = arg top-k BM25(C, C_i)`。
  - 生成：`H_case = LLM(I_case, TopK(C), C)`。
  - 进一步做**细粒度推理轨迹检索**：将推理轨迹切分为步骤，用 SciSpaCy 抽取生物医学实体，计算 Jaccard 相似度：
    `Sim(C, R_i,j) = |E_C ∩ E_i,j| / |E_C ∪ E_i,j|`。
  - 检索 top-k 推理片段：`TopK_entity(C) = arg top-k Sim(C, R_i,j)`，生成 `H_trace`。
- **Web 搜索模块**：
  - 类似 deep research：生成搜索计划 `P = (Q, T, N)`，包括查询、工具类型、检索步数。
  - 逐步调用工具：`s_i = Invoke(t_i, q_i)`，并更新记忆：`m_i = LLM(m_{i-1}, s_i)`。
  - 最终生成疾病列表：`H_web = LLM(I_web, m_N)`。
  - 为防止数据泄漏，屏蔽 PubMed 和 Hugging Face 访问。
- **第二阶段：证据整合与鉴别诊断**：
  - 输入四个疾病列表：`H_web, H_SOAP, H_case, H_trace`。
  - 步骤包括：疾病匹配统一同义词、投票聚合支持度、对高排名候选进行鉴别诊断、最终重排序输出。
  - 公式：`(R, D) = LLM(I_multi, C, H_web, H_SOAP, H_case, H_trace)`。

## 3. 实验设计
- **数据集与场景**：
  - **MedCaseReasoning**：14,489 个诊断 QA，带人工标注推理路径；使用 13,092 个训练样本构建病例数据库；因计算资源有限，从测试集随机选 **300 个样本**评估。
  - **DiReCT**：临床笔记数据，由医生标注完整诊断推理过程；随机选 **50 个样本**评估。
- **Benchmark 与指标**：
  - 推理召回率（Reasoning Recall）。
  - 诊断准确率：Hit@1、Hit@5、Hit@10。
- **对比方法**：
  - **Base models**：DeepSeek-R1、Qwen3-14B、LLaMA-3.1-8B-Instruct、Qwen-2.5-7B。
  - **Fine-tuned models**：LLaMA-3.1-8B-Instruct (SFT)、Qwen-2.5-7B (SFT)。
  - **Agentic methods**：Self-refinement、MedAgents、OpenAI-DR。
  - 所有 agentic 方法统一基于 DeepSeek-R1 实现，以保证公平比较。
- **兼容性实验**：在 Qwen3-14B 上比较 MultiDx 与 MedAgents、Self-refinement。
- **补充
