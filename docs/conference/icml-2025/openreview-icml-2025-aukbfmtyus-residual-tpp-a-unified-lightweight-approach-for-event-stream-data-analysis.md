---
title: "Residual TPP: A Unified Lightweight Approach for Event Stream Data Analysis"
authors: "Ruoxin Yuan, Guanhua Fang"
date: 2025-10-06
pdf: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25a/yuan25a.pdf"
tags: ["query:TPP-ES"]
score: 10
source: ICML-2025-Accepted
selection_source: long-range
publication_date: 2025-10-06
publication_date_precision: day
publication_date_source: "https://raw.githubusercontent.com/mlresearch/v267/gh-pages/_config.yml"
publication_date_kind: proceedings
id: openreview-icml-2025-aukbfmtyus
canonical_id: "work:43042cc1622684ab70cf51cb"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: complete
title_zh: 残差TPP：一种用于事件流数据分析的统一轻量级方法
tldr: 事件流数据建模中，简单统计TPP表达力有限，神经TPP计算开销大。本文提出Residual TPP，通过残差事件分解RED量化强度函数拟合质量，识别残差事件，再用Hawkes过程与任意神经TPP分工处理。实验表明其在多领域拟合与预测达SOTA，且计算优势显著。
motivation: 现有TPP方法难以兼顾简单统计模型的轻量与神经TPP的表达力，需统一高效方案。
method: 提出RED权重函数识别强度函数拟合差的残差事件，结合Hawkes过程与神经TPP分工建模。
result: 在多个领域取得一致最优的拟合优度与预测性能，并具备显著计算优势。
conclusion: Residual TPP为事件流分析提供统一、轻量、可插拔的TPP框架。
evidence: 面向事件流数据的轻量统一TPP建模，属TPP-ES专题。
reading_content_version: 1
reading_section: deep
---

## 摘要
这项工作介绍了残差TPP，一种新颖、统一且轻量级的事件流数据分析方法。它结合了简单统计TPP和表达性神经TPP的优势，以实现更优的性能。具体而言，我们提出了时间点过程中的残差事件分解（RED）技术，该技术定义了一个权重函数，用于量化强度函数对事件特征的捕捉程度。RED作为一个灵活、即插即用的模块，可以在广泛的任务中与任何TPP模型集成。它能够识别强度函数拟合较差的事件，称为残差事件。通过将RED与霍克斯过程结合，我们捕捉了数据的自激特性并识别残差事件。然后，采用任意神经TPP来处理残差事件。大量实验结果表明，残差TPP在多个领域中始终达到最先进的拟合优度和预测性能，并且还提供了显著的计算优势。

## Abstract
This work introduces Residual TPP, a novel, unified, and lightweight approach for analyzing event stream data. It leverages the strengths of both simple statistical TPPs and expressive neural TPPs to achieve superior performance. Specifically, we propose the Residual Events Decomposition (RED) technique in temporal point processes, which defines a weight function to quantify how well the intensity function captures the event characteristics. The RED serves as a flexible, plug-and-play module that can be integrated with any TPP model in a wide range of tasks. It enables the identification of events for which the intensity function provides a poor fit, referred to as residual events. By combining RED with a Hawkes process, we capture the self-exciting nature of the data and identify residual events. Then an arbitrary neural TPP is employed to take care of residual events. Extensive experimental results demonstrate that Residual TPP consistently achieves state-of-the-art goodness-of-fit and prediction performance in multiple domains and offers significant computational advantages as well.

## 专题评审

专题相关性评分：10/10。

论文直接提出时序点过程方法用于事件流数据分析。

---

## 论文详细总结（自动生成）

# Residual TPP 论文深度总结

## 1. 核心问题与整体含义

- **研究背景**：事件流数据广泛存在于金融交易、神经科学、社交媒体、自然灾害监测等领域，其特点是事件离散、时间间隔不规则、存在复杂的时间依赖关系。时序点过程（TPP）是建模此类数据的核心工具。
- **核心矛盾**：
  - **传统统计TPP**（如Poisson过程、Hawkes过程）计算简单、统计性质良好，但固定参数形式的强假设限制了其捕捉真实世界复杂动态的能力。
  - **神经TPP**（如RNN-based、Attention-based）表达能力强，但RNN难以捕捉长程依赖，Transformer计算开销大，且现有研究普遍忽视轻量化建模。
- **关键空白**：时间序列分析中已有成熟的季节性-趋势分解（STD）技术，但TPP领域尚无类似的分解方法。原因在于事件流数据的独特性——时间不规则、事件类型离散且高维稀疏，导致"残差"的定义本身就很困难。
- **整体含义**：本文提出Residual TPP，首次将分解思想引入TPP领域，通过残差事件分解（RED）技术，将简单统计TPP与神经TPP统一在一个轻量级框架中，兼顾表达力与计算效率。

## 2. 方法论

### 2.1 核心思想

采用"分而治之"策略：先用简单统计TPP（Hawkes过程）捕捉数据的主要统计特征（周期性、自激性），再通过RED技术识别Hawkes过程拟合不佳的"残差事件"，最后仅用神经TPP处理这些残差事件，从而大幅降低神经TPP的计算负担。

### 2.2 三步算法流程

**Step 1 — 统计模式建模**：用Hawkes过程拟合原始事件序列，强度函数为：
$$\lambda_k^{(1)}(t) = \mu_k(t) + \sum_{i:t_i<t} \alpha_{k,k_i} g_{k,k_i}(t-t_i)$$
其中基线强度 $\mu_k(t)$ 可捕捉周期性，衰减函数 $g(\cdot)$ 捕捉自激性。

**Step 2 — 残差事件分解（RED）**：为每个事件定义权重函数：
$$W_i(S;\theta) = \phi'_{\rho_1,\rho_2}\left(\int_{t_{i-1}}^{t_i}\sum_{k=1}^K \lambda_k^{(1)}(u)du - 1\right)$$
- 核心直觉：基于时间变换理论，若事件由强度 $\lambda^*(t)$ 生成，则 $\int_{t_{i-1}}^{t_i}\lambda^*(u)du \sim \text{Exp}(1)$。当积分接近1时权重接近1（拟合好），偏离1时权重趋近0（拟合差）。
- 影响函数 $\phi'(x)$ 经过精心设计，在 $x=0$ 处取最大值，具有紧支撑，且满足"无偏性"性质：当 $X\sim\text{Exp}(1)$ 时，$E[(X-1)\cdot\phi'(X-1)]=0$。
- 通过阈值 $w$ 筛选残差事件集：$S'_w = \{(t_i,k_i): W_i(S;\theta)\leq w\}$。

**Step 3 — 残差建模与组合**：在残差序列 $S'_w$ 上训练任意神经TPP，得到 $\lambda_k^{(2)}(t)$。最终强度函数为：
$$\lambda_k(t) = (1-\alpha)\lambda_k^{(1)}(t) + \lambda_k^{(2)}(t)$$
其中 $\alpha = |S'_w|/|S|$ 为残差事件比例。当 $w=0$ 时退化为纯Hawkes过程，$w=1$ 时退化为纯神经TPP。

### 2.3 理论保证

- **命题3.1**：影响函数满足无偏性——当 $X\sim\text{Exp}(1)$ 时，$E[(X-1)\cdot\phi'(X-1)]=0$。
- **定理3.2**：在正则条件下，加权梯度在真实参数处的期望为 $O(1/T)$，即随着 $T\to\infty$ 渐近无偏。这保证了RED筛选残差事件的安全性。

### 2.4 预测方式

- 下一事件时间预测：$\hat{t}_i = E[t_i|\mathcal{H}_{t_{i-1}}] = \int_{t_{i-1}}^\infty t p_i(t)dt$
- 下一事件类型预测：$\hat{k}_i = \arg\max_k \lambda_k(t_i)/\lambda(t_i)$

## 3. 实验设计

### 3.1 数据集

**六个真实世界基准数据集**：
| 数据集 | 领域 | 事件类型数 | 事件总数 |
|--------|------|-----------|---------|
| MIMIC-II | 医疗 | 75 | 2,419 |
| Retweet | 社交媒体 | 3 | 493,708 |
| Earthquake | 地震学 | 7 | 70,723 |
| StackOverflow | 用户行为 | 22 | 142,777 |
| Amazon | 电商 | 16 | 330,000 |
| Volcano | 火山学 | 1 | 9,127 |

**三个合成数据集**：
- Poisson-based：周期性非齐次Poisson + 齐次Poisson残差
- AttNHP-based：AttNHP + 齐次Poisson残差
- Poisson+AttNHP：周期性Poisson + AttNHP残差

### 3.2 对比方法（Baselines）

- **MHP**：多变量Hawkes过程（统计TPP基准）
- **RMTPP**：RNN-based
- **NHP**：连续时间LSTM-based
- **SAHP**：自注意力-based
- **THP**：Transformer-based
- **AttNHP**：注意力神经Hawkes过程
- **ODETPP**：神经ODE-based
- **FullyNN**：全神经网络强度（仅在附录中对比）

每个神经TPP基线均与其对应的Residual TPP版本（Res XXX）进行配对比较。

### 3.3 评估指标

- **拟合优度**：测试集对数似然（越高越好）
- **下一事件时间预测**：RMSE（越低越好）
- **下一事件类型预测**：错误率（越低越好）
- **计算效率**：端到端训练时间

## 4. 资源与算力

- 论文明确说明**所有实验均在CPU上执行**，使用PyTorch框架和Adam优化器。
- **未提及GPU型号、数量或具体训练时长**。
- 论文报告了各模型的端到端训练时间（秒），例如：MHP+RED在MIMIC-II上仅需1.42秒，而AttNHP需68.60秒；Res AttNHP降至52.92秒。
- 整体而言，论文强调的是方法的轻量性和CPU可运行性，而非大规模算力消耗。

## 5. 实验数量与充分性

### 实验规模

- **主实验**：6个真实数据集 × 7个基线模型 × 3个评估指标（拟合优度、时间预测、类型预测），共约126组对比。
- **合成实验**：3个合成数据集 × 7个基线模型，验证RED对真实数据生成过程的鲁棒性。
- **计算效率实验**：6个数据集上所有模型的训练时间对比。
- **消融/扩展实验**：
  - 不同基模型组合（MHP+RED+MHP、NHP+RED+神经TPP等）
  - 替代影响函数验证（附录C.4）
  - FullyNN及其Residual版本对比（附录E.2）
  - 权重分布分析（附录C.2）
  - 自激性统计验证（附录B）

### 充分性与公平性评估

- **充分性**：实验覆盖了医疗、社交、地质、电商等多个领域，包含真实和合成数据，进行了拟合、预测、效率多维度评估，整体较为充分。
- **客观性**：所有神经TPP基线使用EasyTPP库的统一实现，训练参数和流程保持一致，对比公平。
- **公平性**：Residual TPP与其对应基线使用相同的神经TPP架构和训练配置，仅数据不同（原始 vs. 残差），控制变量良好。
- **潜在不足**：未进行多次随机种子实验的方差报告；超参数搜索范围未详细说明。

## 6. 主要结论与发现

1. **拟合优度**：Residual TPP在所有6个真实数据集上均显著优于对应的神经TPP基线，对数似然提升明显（如MIMIC-II上RMTPP从-2.626提升至-2.045）。
2. **预测性能**：在下一事件时间预测和类型预测上均取得一致改进，多数指标达到SOTA。
3. **计算效率**：Residual TPP的训练时间普遍低于原始神经TPP，尤其对计算密集的注意力模型（如AttNHP从9475秒降至7195秒）。
4. **RED的鲁棒性**：即使真实数据生成过程不遵循Hawkes过程（合成实验），RED仍能有效识别残差并提升性能，说明其不依赖于真实模型假设。
5. **即插即用性**：RED可与任意TPP模型集成，包括统计TPP和神经TPP，具有广泛的适用性。
6. **理论保证**：加权梯度渐近无偏，为RED的合理性提供了数学基础。

## 7. 优点

### 方法亮点

- **首创性**：首次将分解思想引入TPP领域，填补了TPP与时间序列分析之间在方法论上的空白。
- **轻量高效**：通过RED筛选残差事件，大幅减少神经TPP的训练样本量，降低计算开销，适合资源受限场景。
- **即插即用**：RED作为独立模块，可与任意TPP模型组合，具有极强的通用性和扩展性。
- **理论支撑**：影响函数的设计有严格的无偏性证明，非纯启发式方法。
- **统一框架**：通过阈值 $w$ 和参数 $\alpha$ 灵活调节统计TPP与神经TPP的贡献，统一了两种范式。

### 实验亮点

- 覆盖6个真实领域 + 3个合成场景，验证充分。
- 配对实验设计（基线 vs. Residual版本）控制变量严谨。
- 同时报告拟合、预测、效率三类指标，评估全面。
- 附录中包含替代影响函数、不同基模型组合等扩展实验，增强了结论的可信度。

## 8. 不足与局限

### 方法局限

- **Hawkes过程的假设限制**：Step 1默认使用固定基线强度和指数衰减的Hawkes过程，未充分利用周期性建模能力（作者在结论中承认这一点，并列为未来工作）。
- **阈值 $w$ 的选择**：需要根据数据调整 $a$、$b$ 等参数以确保残差比例合理，增加了超参数调优负担。
- **残差事件的可解释性**：残差事件被视为"异常值"，但未深入分析其物理或统计含义。
- **组合权重的简化**：使用 $\alpha = |S'_w|/|S|$ 作为固定权重，而非可学习参数，可能不是最优组合方式。

### 实验局限

- **算力信息缺失**：未报告GPU使用情况，仅说明CPU训练，可能限制对大规模场景适用性的评估。
- **数据集规模有限**：最大数据集Retweet约49万事件，未在超大规模（百万级以上）事件流上验证。
- **方差报告缺失**：未报告多次实验的标准差或置信区间。
- **部分基线结果异常**：如SAHP在MIMIC-II上对数似然为-4.672，远差于其他模型，可能影响对比的全面性。
- **Volcano数据集仅单类型**：无法评估类型预测性能，限制了结论的普适性。

### 应用限制

- 方法依赖于Hawkes过程能较好地捕捉数据的主要统计特征；若数据的主导模式与Hawkes假设严重不符，RED的效果可能下降。
- 对于事件类型极多且稀疏的场景（如MIMIC-II的75类），神经TPP在残差上的训练可能仍面临数据不足问题。

（完）
