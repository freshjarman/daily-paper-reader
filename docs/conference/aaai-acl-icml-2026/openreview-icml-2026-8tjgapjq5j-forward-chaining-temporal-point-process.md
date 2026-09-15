---
title: Forward-Chaining Temporal Point Process
title_zh: 前向链式时间点过程
authors: "Chao Yang, Wendi Ren, Shuang Li"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/d282d38eb7c44aa6044cb072845459a48df8168e.pdf"
tags: ["query:tpp-es"]
score: 9.0
evidence: 用于可控连续时间序列生成的时间点过程
tldr: 临床工作流等复杂系统的事件序列往往稀疏且不完整，下游模型仅能捕捉部分动态，而合成序列生成需保持真实、满足领域约束并可控。本文提出前向链式时间点过程（FC-TPP），维护编码高层谓词的显式隐符号状态，通过可微多跳前向链式算子与逻辑规则更新状态，实现连续时间下受约束且可控的序列生成。该方法可用于补全缺失结构、提升稀有模式覆盖，是面向连续时间异步事件序列生成与合成的核心工作。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 临床等复杂系统的事件序列稀疏不完整，合成生成需兼顾真实性与可控性。
method: 提出FC-TPP，用隐符号状态与可微前向链式逻辑算子进行约束感知的连续时间生成。
result: 实现受约束且可控的连续时间序列生成，可补全缺失结构并覆盖稀有模式。
conclusion: 为连续时间异步事件序列的可控生成与合成提供了点过程框架。
---

## Abstract
Event sequences from complex systems, such as clinical workflows, are often sparse and incomplete. As a result, downstream models are trained on data that only partially captures the underlying dynamics. Synthetic sequence generation can augment real data by filling in missing structure and improving coverage of rare patterns, but generated trajectories must remain realistic, satisfy domain constraints, and allow control. We propose the Forward-Chaining Temporal Point Process (FC-TPP), a framework for constraint-aware and controllable sequence generation in continuous time. FC-TPP maintains an explicit latent symbolic state encoding high-level predicates, which evolves through a differentiable multi-hop forward-chaining operator. Logical rules update the latent state based on recent events, while a temporal point process decoder generates future event times and types conditioned on this evolving state. By tying the generative dynamics to multi-hop reasoning in latent space, FC-TPP incorporates symbolic structure throughout generation rather than relying directly on raw event histories. Experiments on synthetic data and four semi-synthetic/real-world benchmarks—LogiCity, MIMIC-IV, EPIC-100, and IKEA ASM—show that FC-TPP achieves higher generation quality under limited and incomplete data, with stronger constraint adherence and greater controllability than purely neural and prior neuro-symbolic baselines.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
用于可控连续时间序列生成的时间点过程。

### 2. 核心内容
临床工作流等复杂系统的事件序列往往稀疏且不完整，下游模型仅能捕捉部分动态，而合成序列生成需保持真实、满足领域约束并可控。本文提出前向链式时间点过程（FC-TPP），维护编码高层谓词的显式隐符号状态，通过可微多跳前向链式算子与逻辑规则更新状态，实现连续时间下受约束且可控的序列生成。该方法可用于补全缺失结构、提升稀有模式覆盖，是面向连续时间异步事件序列生成与合成的核心工作。

### 3. 对应检索需求
find papers on continuous time asynchronous event sequence generation and synthesis。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=8tjGapjQ5J](https://openreview.net/forum?id=8tjGapjQ5J)
