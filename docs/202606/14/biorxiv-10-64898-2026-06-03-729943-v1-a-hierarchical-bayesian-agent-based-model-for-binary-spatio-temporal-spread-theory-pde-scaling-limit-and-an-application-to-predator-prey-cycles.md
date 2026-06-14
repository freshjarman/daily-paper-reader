---
title: "A Hierarchical Bayesian Agent Based Model for Binary Spatio-Temporal Spread: Theory, PDE Scaling Limit, and an Application to Predator Prey Cycles"
title_zh: 用于二元时空传播的分层贝叶斯个体基模型：理论、PDE缩放极限及其在捕食者-猎物周期中的应用
authors: "pan, x."
date: 2026-06-08
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.03.729943v1.full.pdf"
tags: ["query:tpp-es"]
score: 7.0
evidence: 时空扩散的统计模型
tldr: 针对二元时空数据建模中需同时考虑局部持久、各向异性邻域扩散和长距离扩散的挑战，提出一种分层贝叶斯统计智能体模型。该模型将每个单元的占用状态建模为三种过程的伯努利混合，并嵌入共轭Beta和Dirichlet先验，实现高效MCMC推断。证明在小步长极限下，模型的拉格朗日递推可标度为经典平流-扩散偏微分方程。模拟实验验证了参数恢复能力和微观-宏观尺度一致性。贡献在于为生态传播过程（如捕食者-猎物周期）提供了兼具统计灵活性与理论可解释性的建模框架。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有模型难以同时刻画局部持久性、各向异性扩散和长距离传播等多种机制，且缺乏与偏微分方程的理论联系。
method: 构建伯努利混合统计智能体模型，采用分层贝叶斯框架和共轭先验，非平稳扩展通过高斯过程梯度连接扩散核与栖息地适宜性。
result: MCMC算法利用全条件分布实现精确推断，模拟显示参数恢复良好，且模型在微观步长下与平流-扩散PDE标度一致。
conclusion: 该模型为二元时空数据提供机械可解释的贝叶斯方法，兼具统计推断与连续尺度理论。
---

## 摘要
我们描述了一个用于二元时空数据的统计个体基模型（SABM），其中每个单元的占用状态作为三种机制上不同过程的伯努利混合演化：局部持久性、各向异性邻域扩散和长距离扩散。该模型嵌入在分层贝叶斯框架中，对持久性和长距离参数使用共轭Beta全条件分布，并在方向扩散核上使用狄利克雷先验。一个非平稳扩展通过高斯过程的方向梯度将扩散核与潜在的栖息地适宜性表面联系起来。我们证明了，在小步长条件下，扩散核的拉格朗日递归关系缩放为一个经典的二维平流-扩散偏微分方程，其漂移和扩散系数是扩散概率的一阶和二阶矩。我们提供了一个利用精确全条件分布的MCMC算法，并在一个模拟示例中展示了参数恢复和PDE缩放一致性。

## Abstract
We describe a statistical agent-based model (SABM) for binary spatio-temporal data in which the occupancy of each cell evolves as a Bernoulli mixture of three mechanistically distinct processes: local persistence, anisotropic neighborhood dispersal, and long-distance dispersal. The model is embedded in a hierarchical Bayesian framework with conjugate Beta full-conditionals for the persistence and long-distance parameters and a Dirichlet prior on the directional dispersal kernel. A nonstationary extension links the dispersal kernel to a latent habitat-suitability surface through directional gradients of a Gaussian process. We show that, in the small-step regime, the Lagrangian recurrence for the dispersal kernel scales to a classical two-dimensional advection-diffusion partial differential equation whose drift and dispersion coefficients are the first and second moments of the dispersal probabilities. We provide an MCMC algorithm exploiting the exact full-conditionals and demonstrate parameter recovery and PDE-scaling agreement in a simulated example.