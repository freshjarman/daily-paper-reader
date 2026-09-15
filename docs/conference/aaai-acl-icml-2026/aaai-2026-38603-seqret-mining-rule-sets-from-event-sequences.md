---
title: "SEQRET: Mining Rule Sets from Event Sequences"
title_zh: SEQRET：从事件序列中挖掘规则集
authors: "Aleena Siji, Joscha Cüppers, Osman Mian, Jilles Vreeken"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38603/42565"
tags: ["query:tpp-es"]
score: 4.0
evidence: 从事件序列中挖掘规则集
tldr: 针对多数事件序列挖掘方法忽视条件依赖、仅关注序列模式的问题，本文研究从事件序列中发现条件与无条件依赖关系。作者以X到Y的序列模式规则形式刻画依赖，并基于最小描述长度原则将规则集发现问题形式化。由于搜索空间巨大且缺乏结构，提出SEQRET方法高效挖掘高质量、简洁且非冗余的规则集，为事件序列的可解释总结提供了新工具。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 现有事件序列总结方法多忽视条件依赖，仅关注序列模式发现，难以刻画模式间关系。
method: 提出SEQRET，以序列模式间的X到Y规则形式刻画依赖，并用最小描述长度原则形式化规则集发现问题。
result: 方法在庞大搜索空间中挖掘出简洁、非冗余的高质量规则集，实现事件序列的有效总结。
conclusion: 该工作为事件序列挖掘提供了兼具条件依赖刻画与可解释性的规则发现途径。
---

## Abstract
Summarizing event sequences is a key aspect of data mining. Most existing methods neglect conditional dependencies and focus on discovering sequential patterns only. In this paper, we study the problem of discovering both conditional and unconditional dependencies from event sequences. We do so by discovering rules of the form X --> Y where X and Y are sequential patterns. Rules like these are simple to understand and provide a clear description of the relation between the antecedent and the consequent. To discover succinct and non-redundant sets of rules we formalize the problem in terms of the Minimum Description Length principle. As the search space is enormous and does not exhibit helpful structure, we propose the SEQRET method to discover high-quality rule sets in practice. Through extensive empirical evaluation we show that unlike the state of the art, SEQRET ably recovers the ground truth on synthetic datasets and finds useful rules from real datasets.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
从事件序列中挖掘规则集。

### 2. 核心内容
针对多数事件序列挖掘方法忽视条件依赖、仅关注序列模式的问题，本文研究从事件序列中发现条件与无条件依赖关系。作者以X到Y的序列模式规则形式刻画依赖，并基于最小描述长度原则将规则集发现问题形式化。由于搜索空间巨大且缺乏结构，提出SEQRET方法高效挖掘高质量、简洁且非冗余的规则集，为事件序列的可解释总结提供了新工具。

### 3. 对应检索需求
continuous-time event sequence analysis。

### 4. 来源与原文
- Source：AAAI-2026-Accepted
- OpenReview：[https://ojs.aaai.org/index.php/AAAI/article/view/38603](https://ojs.aaai.org/index.php/AAAI/article/view/38603)
