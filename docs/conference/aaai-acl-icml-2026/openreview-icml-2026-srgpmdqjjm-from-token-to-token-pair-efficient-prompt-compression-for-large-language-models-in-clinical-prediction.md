---
title: "From Token to Token Pair: Efficient Prompt Compression for Large Language Models in Clinical Prediction"
title_zh: 从Token到Token对：面向临床预测的大语言模型高效提示压缩
authors: "Mingcheng Zhu, Zhiyao Luo, Yu Liu, Tingting Zhu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/65645f4babbd2bb22cce2ab1b40a995ac8370759.pdf"
tags: ["query:ehr-es"]
score: 7.0
evidence: 将电子健康记录作为自然语言进行死亡预测与表型分析
tldr: 该工作针对将电子健康记录作为自然语言序列输入大模型时，纵向或高频记录导致token序列过长、计算开销高且性能下降的问题。作者提出Medical Token-Pair Encoding分层方法，扩展标准分词实现无损压缩，无需额外推理延迟也不损失临床信息。实验表明该方法在死亡预测与表型分析等临床预测任务上保持甚至提升性能。其意义在于为EHR序列建模提供了高效且不丢信息的表示压缩方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 纵向或高频电子健康记录会生成过长token序列，导致大模型计算成本高且性能下降。
method: 提出Medical Token-Pair Encoding分层方法，扩展标准分词实现token序列的无损压缩。
result: 方法在不增加推理延迟、不丢失临床信息的前提下压缩序列，保持死亡预测与表型分析性能。
conclusion: 为EHR自然语言序列的高效建模提供可行方案，兼顾成本与临床预测准确性。
---

## Abstract
By processing electronic health records (EHRs) as natural language sequences, large language models (LLMs) have shown potential in clinical prediction tasks such as mortality prediction and phenotyping. However, longitudinal or highly frequent EHRs often yield excessively long token sequences that result in high computational costs and even reduced performance. Existing solutions either add modules for compression or remove less important tokens, which introduce additional inference latency or risk losing clinical information. To achieve lossless compression of token sequences without additional cost or loss of performance, we propose Medical Token-Pair Encoding (MedTPE), a layered method that extends standard tokenisation for EHR sequences. MedTPE merges frequently co-occurring medical token pairs into composite tokens, providing lossless compression while preserving the computational complexity through a dependency-aware replacement strategy. Only the embeddings of the newly introduced tokens of merely 0.5-1.0\% of the LLM’s parameters are fine-tuned via self-supervised learning. Experiments on real-world datasets for two clinical scenarios demonstrate that MedTPE reduces input token length by up to 31\% and inference latency by 34-63\%, while maintaining or even improving both predictive performance and output format compliance across multiple LLMs and four clinical prediction tasks. Furthermore, MedTPE demonstrates robustness across different input context lengths and generalisability to scientific and financial domains and different languages. The code is available in the GitHub repository.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
将电子健康记录作为自然语言进行死亡预测与表型分析。

### 2. 核心内容
该工作针对将电子健康记录作为自然语言序列输入大模型时，纵向或高频记录导致token序列过长、计算开销高且性能下降的问题。作者提出Medical Token-Pair Encoding分层方法，扩展标准分词实现无损压缩，无需额外推理延迟也不损失临床信息。实验表明该方法在死亡预测与表型分析等临床预测任务上保持甚至提升性能。其意义在于为EHR序列建模提供了高效且不丢信息的表示压缩方案。

### 3. 对应检索需求
downstream tasks for EHR sequence modeling including mortality prediction and multi label diagnosis。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=SRGpmDQjJM](https://openreview.net/forum?id=SRGpmDQjJM)
