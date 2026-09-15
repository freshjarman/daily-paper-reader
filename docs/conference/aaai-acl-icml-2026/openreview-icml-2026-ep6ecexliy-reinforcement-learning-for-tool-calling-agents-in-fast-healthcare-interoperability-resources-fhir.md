---
title: Reinforcement Learning for Tool-Calling Agents in Fast Healthcare Interoperability Resources (FHIR)
title_zh: 面向FHIR中工具调用智能体的强化学习
authors: "Marius Knorr, Robert Müller, Jan Peter Bremer, Nils Schweingruber"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/bd05a8c09d5fdcdaa68c9960b7206311f97e1367.pdf"
tags: ["query:ehr-es"]
score: 4.0
evidence: 在FHIR电子健康记录资源上进行推理的强化学习智能体
tldr: FHIR是医疗数据互操作的主流标准，其电子健康记录构成资源有向图，回答临床问题需跨资源多步推理与聚合，现有工具增强LLM智能体常选错资源或违反遍历约束。本文在FHIR-AgentBench上将FHIR推理建模为序列决策问题，用强化学习训练工具调用智能体。实验提升了资源选择与遍历正确性，为结构化EHR数据的可靠访问提供了方法。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: FHIR中电子健康记录构成资源有向图，现有LLM智能体在跨资源推理时常选错资源或违反遍历约束。
method: 将FHIR临床问答建模为序列决策问题，用强化学习训练工具调用智能体。
result: 在FHIR-AgentBench上提升了资源选择与遍历的正确性。
conclusion: 强化学习为结构化EHR数据上的可靠多步推理提供了可行方案。
---

## Abstract
Fast Healthcare Interoperability Resources (FHIR) is the dominant standard for interoperable exchange of healthcare data. In FHIR, electronic health records form a directed graph of resources. Answering clinically meaningful questions over FHIR requires agents to perform multi-step reasoning, filtering, and aggregation across multiple resource types. Prior work shows that even tool-augmented LLM agents (retrieval, code execution, multi-turn planning) often select the wrong resources or violate traversal constraints. We study this problem in the context of FHIR-AgentBench, a benchmark for realistic question answering over real-world hospital data, and frame reasoning on FHIR as a sequential decision-making problem over a queryable structured graph. We implement a multi-turn CodeAct agent and post-train it with reinforcement learning using a custom harness and tools. A LLM Judge provides execution-grounded rewards. Compared to prompt-based, closed-model baselines, RL post-training improves performance while enforcing data-integrity constraints. Empirically, our approach improves answer correctness from 50% (o4-mini) to 77% on FHIR-AgentBench using a smaller and cheaper Qwen3-8B model. We present an end-to-end post-training pipeline (environment building, harness construction, model training and custom evaluation) that reliably improves multi-turn reasoning over structured clinical graphs.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
在FHIR电子健康记录资源上进行推理的强化学习智能体。

### 2. 核心内容
FHIR是医疗数据互操作的主流标准，其电子健康记录构成资源有向图，回答临床问题需跨资源多步推理与聚合，现有工具增强LLM智能体常选错资源或违反遍历约束。本文在FHIR-AgentBench上将FHIR推理建模为序列决策问题，用强化学习训练工具调用智能体。实验提升了资源选择与遍历正确性，为结构化EHR数据的可靠访问提供了方法。

### 3. 对应检索需求
EHR event stream modeling。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=Ep6EcExLIY](https://openreview.net/forum?id=Ep6EcExLIY)
