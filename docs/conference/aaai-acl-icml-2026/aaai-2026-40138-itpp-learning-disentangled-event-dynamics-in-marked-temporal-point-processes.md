---
title: "ITPP: Learning Disentangled Event Dynamics in Marked Temporal Point Processes"
title_zh: ITPP：学习标记时间点过程中的解耦事件动态
authors: "Wang-Tao Zhou, Zhao Kang, Ke Yan, Ling Tian"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40138/44099"
tags: ["query:tpp-es"]
score: 9.0
evidence: 面向异步事件序列的通道独立MTPP架构与ODE骨干
tldr: 现有标记时间点过程模型多采用通道混合策略，将不同事件类型编码进单一固定隐表示，导致类型特异动态被混淆并加剧过拟合。本文提出ITPP，一种通道独立架构，用基于ODE的编码器-解码器框架结合类型感知的倒置自注意力显式建模事件类型间的相互作用。方法在多个事件序列数据集上提升了预测性能并缓解过拟合，为解耦式时间点过程建模提供了新范式。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 现有标记时间点过程模型用通道混合策略把不同事件类型混入单一隐表示，导致类型特异动态被掩盖并加剧过拟合。
method: 提出ITPP通道独立架构，采用ODE骨干的编码器-解码器与类型感知倒置自注意力，显式建模事件类型间关系。
result: 实验表明该解耦建模缓解了过拟合并提升了事件预测性能。
conclusion: 通道独立与类型感知注意力为时间点过程建模提供了更稳健的表示学习方案。
---

## Abstract
Marked Temporal Point Processes (MTPPs) provide a principled framework for modeling asynchronous event sequences by conditioning on the history of past events. However, most existing MTPP models rely on channel-mixing strategies that encode information from different event types into a single, fixed-size latent representation. This entanglement can obscure type-specific dynamics, leading to performance degradation and increased risk of overfitting. In this work, we introduce ITPP, a novel channel-independent architecture for MTPP modeling that decouples event type information using an encoder-decoder framework with an ODE-based backbone. Central to ITPP is a type-aware inverted self-attention mechanism, designed to explicitly model inter-channel correlations among heterogeneous event types. This architecture enhances effectiveness and robustness while reducing overfitting. Comprehensive experiments on multiple real-world and synthetic datasets demonstrate that ITPP consistently outperforms state-of-the-art MTPP models in both predictive accuracy and generalization.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：标记时间点过程（Marked Temporal Point Processes, MTPPs）用于建模连续时间中的异步事件序列，每个事件由时间 \(t_i\) 和类型/标记 \(m_i\) 组成，核心是条件强度函数 \(\lambda_m(t|\mathcal{H}_t)\)。
- **核心问题**：现有 MTPP 模型大多采用**通道混合（channel-mixing）**策略，即把所有事件类型的历史信息编码进一个统一、固定大小的隐表示。这会把不同事件类型的动态“纠缠”在一起，掩盖类型特异模式，引入噪声与干扰，并增加过拟合风险。
- **论文含义**：作者提出 **ITPP**，一种通道独立（channel-independent）的 MTPP 架构，先解耦不同事件类型的动态，再显式建模类型间相关性。其目标是提升预测准确性、泛化能力与鲁棒性，同时缓解过拟合。
- **直观例子**：论文用淘宝浏览历史说明，若把服装、手机、食品等不同类别混合编码，模型难以隔离类别特有模式；通道独立可避免这种模式混淆。

## 2. 论文提出的方法论

- **核心思想**：采用“**编码—相关—解码**”架构：
  - 编码阶段：对每个事件类型通道独立建模；
  - 中间阶段：用类型感知倒置自注意力捕捉跨通道依赖；
  - 解码阶段：对每个通道独立输出类型特异强度 \(\lambda_k(t)\)。
- **通道独立上下文编码**：
  - 将不同事件类型视为不同通道，每个通道独立编码为时变隐状态 \(z_k(t)\in\mathbb{R}^d\)。
  - 使用带跳变的神经 ODE 建模细粒度动态：
    - **外推（extrapolation）**：事件间隔内的平滑演化  
      \[
      dz_k(t)=f_{\theta_f}(z_k(t),t)dt
      \]
    - **跳变（jump）**：事件发生时的突变  
      \[
      z_k(t^+_{k,i})=g_{\theta_g}(z_k(t^-_{k,i}))
      \]
  - 不同通道共享同一套 ODE 参数，但状态独立演化。
- **类型感知倒置自注意力**：
  - 与普通 Transformer 对同质 token 建模不同，MTPP 中不同事件类型本质异质。
  - 对通道 \(k\) 计算 query/key/value：
    \[
    q_k(t)=W^Qz_k(t)+b^Q_k,\quad
    k_k(t)=W^Kz_k(t)+b^K_k,\quad
    v_k(t)=W^Vz_k(t)+b^V_k
    \]
  - 映射矩阵 \(W^Q,W^K,W^V\) 跨通道共享，但偏置 \(b_k\) 通道特异，以保留事件类型固有特征。
  - 跨通道注意力：
    \[
    \mathrm{ATTN}(Q,K,V)=\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
    \]
  - 加入残差连接与 LayerNorm，支持多头注意力。
- **通道独立强度解码**：
  - 每个通道独立解码：
    \[
    \lambda_k(t)=r_{\theta_r}(h_k(t))
    \]
  - 下一事件联合概率：
    \[
    f(t,k)=\lambda_k(t)\exp\left(-\int_{\bar t}^{t}\lambda(\tau)d\tau\right)
    \]
    其中 \(\lambda(t)=\sum_k\lambda_k(t)\)。
- **训练**：使用最大似然估计，损失为负对数似然：
  \[
  \mathcal{L}_\theta(S)=-\sum_{i=1}^{L}\log\lambda_{m_i}(t_i)+\int_0^T\lambda(\tau)d\tau
  \]
  通过伴随敏感度方法反向传播 ODE 梯度。

## 3. 实验设计

- **数据集**：共 6 个，包含 4 个真实数据集和 2 个合成数据集：
  - StackOverflow：142,777 事件，平均长度 65，2,203 序列，22 类型；
  - MIMIC：2,419 事件，平均长度 4，650 序列，75 类型；
  - Taobao：115,397 事件，平均长度 58，2,000 序列，17 类型；
  - Earthquake：70,723 事件，平均长度 16，4,300 序列，7 类型；
  - Poisson：39,893 事件，平均长度 80，500 序列，3 类型；
  - Hawkes：21,166 事件，平均长度 42，500 序列，3 类型。
- **评估任务与指标**：
  - **概率评估**：平均负对数似然 NLL，包括联合 TM-NLL、时间 T-NLL、标记 M-NLL；
  - **预测评估**：时间预测 RMSE，标记预测 F1；
  - **强度恢复**：在 Poisson、Hawkes 合成数据上使用 MAPE，并可视化 Hawkes 强度恢复；
  - **消融研究**：验证通道独立与倒置自注意力的贡献；
  - **过拟合分析**：比较训练/测试损失曲线。
- **对比方法**：共 10 个基线：
  - RNN 类：RMTPP、NHP、LogNormMix；
  - 自注意力类：THP、SAHP、AttNHP；
  - 卷积类：CTPP；
  - 微分方程类：NeuralODE、ODE-GRU、NJDTPP。
- **主要结果**：
  - 表 1 中，ITPP 在四个真实数据集的 TM-NLL 上全部取得最佳；
  - 表 3 预测评估中，ITPP 在 6 个指标中 5 个最佳，Earthquake 的 F1 略低于最优；
  - 强度恢复上，ITPP 显著优于现有基于强度的 MTPP 模型；
  - 消融显示，移除通道独立或倒置自注意力都会明显降低性能；
  - 过拟合分析显示，ITPP 比 LogNormMix、ODE-GRU 等更稳定，测试损失不易后期激增。

## 4. 资源与算力

- 论文中**未明确说明**使用的 GPU 型号、GPU 数量、训练时长、总计算量或超参数搜索成本。
- 仅提及代码链接与基金致谢，因此无法从文中评估其算力需求、训练成本与能耗。
- 这一点属于可复现性和实际应用评估上的信息缺口。

## 5. 实验数量与充分性

- **实验数量**：大致包括四组主实验：
  1. 概率评估：4 个真实数据集，10 个基线，3 个 NLL 指标；
  2. 预测评估：3 个真实数据集，RMSE 与 F1；
  3. 强度恢复：2 个合成数据集，MAPE 与可视化；
  4. 消融研究：通道独立、倒置自注意力，主要在 StackOverflow 与 Earthquake 上；
  5. 过拟合分析：训练/测试损失曲线。
- **充分性**：
  - 覆盖面较广，真实与合成数据结合，基线数量多，指标较全面；
  - 消融实验直接验证两个核心设计，过拟合分析也支持论文动机；
  - 结果整体支持“通道独立 + 类型感知注意力”的有效性。
- **不足**：
  - 未报告多次运行的均值、标准差、显著性检验；
  - 未说明所有基线是否经过统一、充分的超参数调优；
  - 强度恢复仅限合成数据；
  - 消融实验只在两个数据集上展开；
  - 未系统评估计算复杂度、事件类型数量增长下的扩展性、类型不平衡等场景。

## 6. 论文的主要结论与发现

- ITPP 在多个真实与合成数据集上**一致优于现有最先进 MTPP 模型**。
- 在概率拟合上，
