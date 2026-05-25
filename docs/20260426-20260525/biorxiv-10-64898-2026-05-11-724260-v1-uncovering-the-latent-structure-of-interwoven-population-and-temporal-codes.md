---
title: Uncovering the latent structure of interwoven population and temporal codes
title_zh: 揭示交织的群体编码和时间编码的潜在结构
authors: "Friedenberger, Z., Cao, Y., Naud, R."
date: 2026-05-12
pdf: "https://www.biorxiv.org/content/10.64898/2026.05.11.724260v1.full.pdf"
tags: ["query:tpp-es"]
score: 8.0
evidence: 将神经脉冲序列分解为爆发和单脉冲潜在因子，直接与标记时点过程建模对齐
tldr: 群体分析方法通常忽略精确尖峰时序中的信息，尤其是爆发编码。本文开发一种因子分析方法，将爆发与单个尖峰的因子分离，无需外部协变量即可从数据结构中研究爆发编码。对模拟和实验数据的分析表明，仅用发放率会掩盖潜在结构，而该方法能正确推断并检验爆发编码的存在。该框架将爆发变化与注意、感知和学习等内部变量联系起来。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有群体分析方法主要基于率编码，忽略了爆发等精细时序信息，限制了编码理解。
method: 开发一种因子分析方法，将爆发和单个尖峰因子解耦，直接从尖峰序列中推断潜在结构。
result: 模拟和实验数据表明，该方法能正确推断爆发编码的潜在结构，并检验其存在性。
conclusion: 融合群体与爆发编码视角，为揭示内在变量与爆发变化的关系提供新框架。
---

## 摘要
群体分析方法已成为解析神经数据复杂性的标准方法。然而，这些方法通常假设速率编码，忽略了尖峰精确时序中编码的信息。关键在于，动作电位爆发中编码的额外信息可能被遗漏。在此，我们开发了一种因子分析方法，能够将爆发相关因子与单个尖峰相关因子分离开来。这使得可以直接从数据结构中研究爆发编码，无需外部协变量。我们证明，仅分析放电率会掩盖爆发背后的潜在结构和因子。将我们的方法应用于模拟和实验数据，我们展示了它能推断出正确的潜在结构，并可用于测试爆发编码的存在。通过融合群体编码和爆发编码的视角，我们提供了一个框架，将爆发变化与涉及注意力、感知和学习的内部变量联系起来。

## Abstract
Population analysis methods have become standard for navigating the complexity of neural data. However, these methods often assume a rate code, neglecting information encoded in the precise timing of spikes. Critically, additional information encoded in bursts of action potentials may be missed. Here, we develop a factor analysis method that disentangles the factors associated with bursts and individual spikes. This enables burst codes to be investigated directly from the structure of the data, without requiring external covariates. We demonstrate that analyzing firing rates alone obscures the latent structure and factors underlying bursts. Applying our method to simulated and experimental data, we show that it can infer the correct latent structure and be used to test for the presence of burst coding. By merging the population and burst coding perspectives, we provide a framework for linking changes in bursting to internal variables involved in attention, perception, and learning.