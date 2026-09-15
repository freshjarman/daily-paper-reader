---
title: "METP: Multi-Granularity Integration of External Covariates for Temporal Point Processes"
title_zh: METP：时间点过程中外部协变量的多粒度融合
authors: "Boyang Li, Lingzheng Zhang, Fugee Tsung, Xi Zhang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39448/43409"
tags: ["query:tpp-es"]
score: 9.0
evidence: 融合多粒度外部协变量的时间点过程强度建模
tldr: 准确的时间点过程建模对事件预测至关重要，但现有方法多依赖历史事件序列，忽视外部协变量的滞后效应及其多时间粒度影响。本文提出METP框架，提取周期性结构并将外部协变量分解到多个时间粒度，并在各粒度用滞后感知校准模块对齐协变量。实验表明该方法提升了强度估计与事件预测精度，拓展了时间点过程对外部驱动因素的建模能力。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 现有时间点过程多依赖历史事件，忽视外部协变量跨多时间粒度的滞后效应对未来强度的影响。
method: 提出METP，将外部协变量分解到多时间粒度，并用滞后感知校准模块对齐后融入强度建模。
result: 实验表明该框架提升了强度估计与事件预测的准确性。
conclusion: 多粒度外部协变量融合增强了时间点过程的预测与决策能力。
---

## Abstract
Accurate modeling of temporal point processes is critical for reliable event forecasting and informed decision-making. While historical event sequences provide a foundation for intensity estimation, existing approaches often neglect external covariates whose lagged effects impact future intensities across multiple temporal granularities. To address this gap, we propose Multi-Granularity Integration of External Covariates for Temporal Point Processes (METP), a framework for incorporating lagged external influences into intensity modeling. METP extracts periodic structures and decomposes external covariate series into multiple temporal granularities. At each granularity, a lag-aware calibration module is introduced to align covariates with event dynamics. Finally, a hierarchical mixture-of-experts strategy is employed to integrate the multi-granular external covariates with historical event embeddings, enabling a representation of the conditional intensity function with enhanced information. Extensive experiments on public and proprietary datasets demonstrate that METP consistently outperforms existing methods in predictive accuracy.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：时间点过程（TPP）广泛用于电商、社交网络、临床等连续时间事件序列建模。现有神经 TPP 方法多依赖历史事件序列估计条件强度，常忽视外部时序协变量。
- **核心问题**：外部协变量对事件强度具有**滞后效应**，且这种影响常跨越**多个时间粒度**，并可能包含**周期结构**；现有方法常采用固定滞后窗口，难以处理外部序列与事件序列之间的时间错位、长期趋势与短期波动。
- **整体含义**：论文提出 METP，将外部协变量的周期性、多粒度结构和滞后效应显式融入 TPP 强度建模，以提升下一事件时间预测和强度估计精度。论文声称这是首个在 TPP 中实现滞后效应自适应对齐的方法。

## 2. 方法论

- **问题定义**：给定历史事件时间序列 \(S_{1:n}=\{t_1,\dots,t_n\}\) 与外部输入序列 \(X_T=\{x_1,\dots,x_T\}\)，建模条件强度 \(\lambda(t)=F(t>T|S_{1:n},X_T)\)。由强度得到条件密度 \(\kappa(t)=\lambda(t)\exp(-\int_{t_n}^{t}\lambda(\tau)d\tau)\)，并预测下一事件期望时间 \(t_{n+1}=\int_T^\infty t\kappa(t)dt\)。
- **周期性与多粒度编码**：
  - 用离散傅里叶变换（DFT）从外部序列中提取主周期 \(\delta\)。
  - 滑动窗口构造周期矩阵 \(X(t)\in\mathbb{R}^{\delta\times m}\)，每行表示一个历史周期，每列表示周期内相同相对位置。
  - 对周期矩阵施加多组非重叠最大池化，得到不同粒度 \(s_k\) 下的表示 \(U_k(t)\)，以同时捕捉长期趋势和短期波动。
  - 采用正弦位置编码，但编码周期来自外部协变量的主周期，而非事件采样模式，使时间编码更“协变量感知”。
- **滞后效应分布对齐**：
  - 每个粒度 \(k\) 学习衰减参数 \(\phi_k=u_k w_k\)，构造反向几何先验 \(r_k(j)\)，刻画非对称时间衰减。
  - 用因果自注意力计算注意力分布 \(p_k(j)=\text{softmax}(q_k^\top k_j/\sqrt{l})\)。
  - 通过对称 KL 散度 \(D_{SKL}(k)=D_{KL}(p_k\|r_k)+D_{KL}(r_k\|p_k)\) 对齐注意力分布与反向几何先验，使模型既遵循滞后衰减先验，又保留数据驱动灵活性。
  - 聚合表示 \(z_t^k\) 由注意力加权历史层次向量得到，再经线性变换和 sigmoid 得到预测，损失为交叉熵加 SKL 正则项。
- **多粒度外部协变量与事件融合**：
  - 对齐后的外部表示 \(P_k(t)\) 由注意力权重、指数衰减权重 \(d_k(t-t_j)=(1-\phi_k)^{t-t_j}\) 和外部协变量嵌入加权求和。
  - 使用层次粒度混合专家（MoE）融合多粒度表示：第一粒度始终保留，其余粒度动态选择 top-\((K-1)\) 专家，得到统一环境感知上下文 \(P(t)\)。
  - 历史事件嵌入经多头自注意力和前馈网络处理，得到事件表示 \(H\)。
  - 条件强度建模为 \(\lambda(t|H_t)=\text{softplus}(\rho\frac{t-t_i}{t_i}+w_a^\top h_a(t)+b)\)，其中 \(h_a(t)=[h_t,p(t)]\)，softplus 保证非负。
- **训练目标**：负对数似然损失 \(L_p=-\sum_i\log\lambda(t_i|H_{t_i})+\sum_j\lambda(j|H_j)\)，总损失为 \(L=L_p+\sum_{k=1}^K L_k\)。采用两阶段优化以提升稳定性。

## 3. 实验设计

- **数据集/场景**：
  - **GTD**：专有汽油交易数据集，外部协变量为销售价格。
  - **Tianchi-Walmart Storm Sales Dataset**：多门店商品销售数据，外部协变量为温度时间序列。
  - **Elevator Fault Dataset**：电梯故障事件建模，外部特征为指示器时间序列。
  - **Global Earthquake Dataset**：地震记录，外部变量为极端天气条件。
- **评价指标**：NLL、NMAE、NRMSE，均为越低越好。NLL 衡量强度函数与观测事件的概率拟合，NMAE/NRMSE 衡量预测事件时间偏差。
- **对比方法**：
  - RMTPP、IFTPP、THP、SAHP、A-NHP、ITHP、XTSFormer。
  - 正文还列出 NJDTPP，但表 1 中未出现该模型的结果。
- **实验类型**：
  - 四个数据集上的主实验。
  - 在 GTD 和 Tianchi 上做消融：去掉外部变量、去掉滞后权重、去掉多尺度结构、去掉周期结构。
  - 超参数敏感性：对齐正则系数 \(\eta\)、时间编码维度 \(d\)、粒度数量 \(K\)。
  - 事件预测可视化：2023 年 1—6 月六个事件，与 THP、XTSFormer 对比。

## 4. 资源与算力

- 文中明确提到实现细节：PyTorch、3 层 Transformer 编码器、4 个注意力头、Adam 优化器、学习率 \(1e-3\)、batch size 16、训练 100 个 epoch、数值稳定常数 \(\epsilon=1e-9\)。
- **未明确说明**使用的 GPU 型号、GPU 数量、训练时长、总计算资源或能耗。因此无法从论文文本判断具体算力规模。

## 5. 实验数量与充分性

- **实验数量**：
  - 主实验覆盖 4 个数据集、约 7—8 个基线、3 个指标。
  - 消融实验覆盖 2 个数据集、4 个变体。
  - 超参数敏感性分析覆盖 3 个超参数。
  - 1 组事件预测可视化。
  - 论文称有统计检验，但完整结果在附录，正文未给出细节。
- **充分性**：
  - 整体较充分，覆盖专有与公开数据、多指标、消融和敏感性分析。
  - 但缺少重复运行方差、随机种子、置信区间、显著性检验细节，难以判断稳定性。
  - 专有 GTD 数据集不可公开复现；NJDTPP 在正文列为基线但表中缺失，影响完整性。
- **客观性与公平性**：
  - 使用公开基准和统一指标，比较对象涵盖传统与最新 TPP 方法，总体较客观。
  - 但未说明各基线是否经过同等调参，且部分指标上 METP 并非全部最优，说明仍有改进空间。

## 6. 主要结论与发现

- METP 在四个数据集上的平均 NLL、NMAE、NRMSE 最低，平均排名最好，整体优于现有方法。
- GTD 上 METP 在所有指标均最佳；Tianchi 上 NLL 和 NRMSE 最佳，NMAE 略逊于 RMTPP；Fault 上 NRMSE 略逊于 RMTPP；Earthquake 上 NLL 和 NMAE 最佳，NRMSE 略逊于 ITHP。
- 消融表明：
  - 去掉外部变量导致最大性能下降，说明环境感知建模最关键。
  - 去掉滞后权重、多尺度结构、周期结构均造成退化，证明各组件有效。
- 超参数分析表明：
  - \(\eta=10^{-3}\)—\(10^{-2}\) 较优；
  - 时间编码维度 \(d=64\)—128 较优；
  - 粒度数量 \(K=4\)—5 较优。
- 可视化显示 METP 对 2023 年 1
