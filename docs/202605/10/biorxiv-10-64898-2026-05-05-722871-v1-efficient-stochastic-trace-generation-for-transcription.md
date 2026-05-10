---
title: Efficient Stochastic Trace Generation for Transcription
title_zh: 转录的高效随机轨迹生成
authors: "Ferdowsi, A., Fuegger, M., Nowak, T."
date: 2026-05-08
pdf: "https://www.biorxiv.org/content/10.64898/2026.05.05.722871v1.full.pdf"
tags: ["query:tpp-es"]
score: 6.5
evidence: 具有加性零星跳跃的随机轨迹生成
tldr: 本研究针对单细胞转录过程中产生的爆发式表达分布，提出了一种高效的随机轨迹生成框架。由于传统的Gillespie算法计算成本高，而现有的SDE模型难以捕捉重尾噪声，作者开发了统一的SDE框架，结合了确定性漂移、高斯波动和任意分布的随机跳跃。该框架支持向量化生成，并提供了开源工具bcrnnoise，在保持高精度的同时将计算速度提升了两个数量级。
source: biorxiv
selection_source: fresh_fetch
motivation: 传统的Gillespie随机采样算法在模拟大量单细胞转录轨迹时计算成本过高，且现有简化模型难以准确描述重尾噪声。
method: 提出一个统一的随机微分方程（SDE）框架，融合了确定性漂移、高斯波动及任意分布的加性随机跳跃，并实现向量化计算。
result: 实验表明，该框架在多种代理模型下均能保持高精度，且计算速度比传统方法提升了高达两个数量级。
conclusion: 该研究为高效模拟复杂的单细胞转录动力学提供了强有力的工具，平衡了计算效率与生物物理过程的模拟精度。
---

## 摘要
单细胞中的爆发式转录通常会产生过度分散、偏斜且有时呈现重尾特征的表达分布，这些分布可以通过启动子的两状态马尔可夫模型来解释。虽然模拟的金标准是使用 Gillespie 算法进行精确随机采样，但获取数千条定时轨迹的计算成本很高。基于随机微分方程 (SDE) 的代理模型被广泛用于加速这一模拟过程。例如，基于高斯噪声的化学朗之万方程 (Chemical Langevin Equation)，但它无法捕捉重尾噪声。在这项工作中，我们提出了一个统一的 SDE 框架，该框架结合了确定性漂移、高斯波动和任意分布的加性零星跳跃，并提供了一个开源 Python 实现 bcrnnoise。该框架涵盖了标准的代理模型，并允许矢量化生成批量转录轨迹。我们评估了常见代理模型以及新模型的计算速度和准确性，结果表明在保持高准确性的同时，计算成本可降低多达两个数量级。

## Abstract
Bursty transcription in single cells typically produces over-dispersed, skewed, and sometimes heavy-tailed expression distributions that are explained by two-state Markov models of the promoters. While the gold standard for simulation is exact stochastic sampling with Gillespie's algorithm, obtaining thousands of timed traces is computationally costly. Surrogate models based on stochastic differential equations (SDEs) are widely used to speed up this simulation process. An example is the Chemical Langevin Equation based on Gaussian noise, which, however, does not capture heavy-tailed noise. In this work, we present a unified SDE framework that combines deterministic drift, Gaussian fluctuations, and additive sporadic jumps of arbitrary distributions, and provide an open-source Python implementation, bcrnnoise. The framework subsumes standard surrogate models and allows for vectorized generation of batches of transcription traces. We assess computational speed and accuracy of common surrogate models along with new models, showing that high accuracy can be obtained while reducing computational cost up to two orders of magnitude.