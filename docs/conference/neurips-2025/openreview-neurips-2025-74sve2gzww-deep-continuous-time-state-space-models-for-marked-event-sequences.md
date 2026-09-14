---
title: Deep Continuous-Time State-Space Models for Marked Event Sequences
authors: "Yuxin Chang, Alex James Boyd, Cao Xiao, Taha Kass-Hout, Parminder Bhatia, Padhraic Smyth, Andrew Warrington"
date: 2025
pdf: "https://papers.neurips.cc/paper_files/paper/2025/file/ee39348acc798915d2d15a8bbbd417b8-Paper-Conference.pdf"
tags: ["query:TPP-ES"]
score: 10
source: NeurIPS-2025-Accepted
selection_source: long-range
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
id: openreview-neurips-2025-74sve2gzww
canonical_id: "work:50c3fa2ef5759f6032b5fe74"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: complete
title_zh: 用于标记事件序列的深度连续时间状态空间模型
tldr: "标记时序点过程用于建模不规则时间事件，但现有模型难以兼顾连续时间归纳偏置与表达力。本文提出S2P2，将随机跳跃微分方程与非线性交错，构建基于强度的深度状态空间点过程。方法支持并行扫描训练，具线性复杂度与亚线性扩展。在八个真实数据集上预测似然达最优，平均提升33%。"
motivation: 现有MTPP模型或缺乏连续时间归纳偏置，或依赖受限参数假设，难以兼顾表达力与效率。
method: 提出S2P2，受线性Hawkes启发，交错随机跳跃微分方程与非线性，构建无需受限强度假设的强度型MTPP。
result: "在八个真实数据集上取得最优预测似然，平均较最佳现有方法提升33%，训练与推理具线性复杂度。"
conclusion: S2P2为连续时间事件序列提供高效且表达力强的状态空间建模范式，拓展了深度SSM在MTPP中的应用。
evidence: 面向标记事件序列的连续时间状态空间点过程建模，属时序点过程专题。
reading_content_version: 1
reading_section: deep
---

## 摘要
标记时间点过程（MTPPs）对以不规则时间间隔发生的事件序列进行建模，在医疗、金融和社交网络等领域具有广泛应用。我们提出了状态空间点过程（S2P2）模型，这是一种新颖且性能优越的模型，它利用为现代深度状态空间模型（SSMs）开发的技术来克服现有MTPP模型的局限性，同时为连续时间事件序列注入其他离散序列模型（即RNNs、transformers）未能捕捉的强大归纳偏置。受经典线性Hawkes过程的启发，我们提出了一种架构，将随机跳跃微分方程与非线性交错，以创建高度表达性的基于强度的MTPP模型，而无需对强度进行限制性的参数假设。我们的方法通过并行扫描实现高效的训练和推理，带来线性复杂度和次线性缩放，同时保留对MTPPs的表达能力。在实证上，S2P2在八个真实世界数据集上实现了最先进的预测似然，比现有最佳方法平均提高了33%。

## Abstract
Marked temporal point processes (MTPPs) model sequences of events occurring at irregular time intervals, with wide-ranging applications in fields such as healthcare, finance and social networks. We propose the _state-space point process_ (S2P2) model, a novel and performant model that leverages techniques derived for modern deep state-space models (SSMs) to overcome limitations of existing MTPP models, while simultaneously imbuing strong inductive biases for continuous-time event sequences that other discrete sequence models (i.e., RNNs, transformers) do not capture. Inspired by the classical linear Hawkes processes, we propose an architecture that interleaves stochastic jump differential equations with nonlinearities to create a highly expressive intensity-based MTPP model, without the need for restrictive parametric assumptions for the intensity. Our approach enables efficient training and inference with a parallel scan, bringing linear complexity and sublinear scaling while retaining expressivity to MTPPs. Empirically, S2P2 achieves state-of-the-art predictive likelihoods across eight real-world datasets, delivering an average improvement of 33% over the best existing approaches.

## 专题评审

专题相关性评分：10/10。

该论文直接研究marked temporal point process建模，属于TPP-ES核心范围。

---

## 论文详细总结（自动生成）

# 论文深度总结：Deep Continuous-Time State-Space Models for Marked Event Sequences

## 1. 核心问题与整体含义

- **研究背景**：标记时间点过程（MTPPs）用于建模不规则时间间隔下发生的事件序列，每个事件带有类型标签（mark），广泛应用于医疗、金融、社交网络等领域。
- **核心问题**：现有MTPP模型存在三大瓶颈：
  - **RNN类模型**（如RMTPP、NHP）：具备连续时间归纳偏置，但序列计算导致O(N)复杂度，无法并行化，难以处理长序列。
  - **Transformer类模型**（如SAHP、THP、AttNHP）：可并行计算，但注意力机制带来O(N²)复杂度，长序列场景下内存和计算开销不可接受。
  - **强度自由类模型**（如IFTPP）：依赖参数化解码器，牺牲了灵活性。
- **整体含义**：论文提出**S2P2（State-Space Point Process）**，首次将深度状态空间模型（SSM）技术系统性地引入MTPP建模，在保持连续时间归纳偏置的同时，实现线性复杂度、亚线性并行扩展和高度表达力，在八个真实数据集上取得最优预测似然，平均提升33%。

---

## 2. 方法论

### 2.1 核心思想

- 受经典**线性Hawkes过程（LHP）** 启发，将LHP的强度递推方程与深度SSM的状态方程进行类比融合：
  - LHP强度 λ_t 类比于SSM隐状态 x(t)；
  - LHP衰减率 β 类比于SSM状态矩阵 A；
  - LHP背景强度 ν_t 类比于SSM输入信号 Bu(t)；
  - LHP的脉冲项 αdN_t 是SSM所缺失的关键组件，用于捕捉事件的突变影响。
- 提出**潜在线性Hawkes层（LLH层）**，作为S2P2的核心递推单元。

### 2.2 关键技术细节

**（1）LLH层的连续时间随机跳跃微分方程**：

```
dx_t = -A x_{t-} dt + A B u_{t-} dt + E α dN_t    (隐状态演化)
y_t = C x_t + D u_t                                (输出)
```

- 其中 α ∈ R^{R×K} 为低秩标记嵌入，E ∈ R^{P×R} 为层特定投影，R为嵌入秩。
- 相比原始LHP，LLH在潜在空间R^P中操作，且A为一般动力学矩阵，表达力大幅增强。

**（2）对角化与离散化**：

- 对 -A 进行对角化分解 VΛV⁻¹，将矩阵指数运算转化为逐元素指数运算。
- 采用**零阶保持（ZOH）** 假设，在无事件区间内输入信号视为常数，得到闭式更新规则：

```
x̃_{t'} = Λ̄ x̃_t + (Λ̄ - I) B̃ u_{t'-}          (无事件)
x̃_{t'} = Λ̄ x̃_t + (Λ̄ - I) B̃ u_{t'-} + Ẽα_k   (有类型k事件)
```

- 其中 Λ̄ = exp(Λ(t'-t))，该更新规则无需矩阵指数运算。

**（3）并行扫描计算**：

- LLH递推可写为 z_{i+1} = R_i z_i + b_i 的标准形式，利用**并行扫描（Parallel Scan）** 实现O(log N)并行深度和O(N)工作量。
- 右极限 x_{t_i} 通过并行扫描计算，左极限 x_{t_i-} 通过减去脉冲项 Ẽα_k 直接获得。

**（4）输入依赖动力学**：

- 借鉴Mamba的设计，允许动力学矩阵随输入变化：

```
Λ_i = diag(softplus(W'u_{t_i} + b')) Λ
```

- 该设计条件线性于时间，仍可使用并行扫描。

**（5）S2P2整体架构**：

- 堆叠L层LLH层，层间插入GELU激活函数、残差连接和LayerNorm：

```
u^{(l+1)}_t = LayerNorm(σ(y^{(l)}_t) + u^{(l)}_t)
```

- 最终强度通过仿射投影+Softplus整流获得：λ_t = s ⊙ softplus((W u^{(L+1)}_{t-} + b) ⊙ s⁻¹)。
- 训练目标为最大化对数似然，积分项使用蒙特卡洛估计。

---

## 3. 实验设计

### 3.1 数据集

- **八个真实世界数据集**：
  - 五个EasyTPP基准数据集：Amazon、Retweet、Taxi、Taobao、StackOverflow；
  - 两个常用数据集：Last.fm、MIMIC-II；
  - 一个新构建的医疗事件数据集：**EHRSHOT**（668种标记，序列长度最长3955，规模远超EasyTPP数据集）。
- **合成数据集**：
  - 经典Hawkes过程和自校正过程；
  - 非齐次Poisson过程（方波强度函数）；
  - 长程依赖过程（触发-目标标记对，延迟约40个时间单位）；
  - 随机多变量Hawkes过程（K=3）。

### 3.2 Benchmark与对比方法

- **对比方法**（共8个基线）：
  - RMTPP（RNN类）、NHP（神经Hawkes过程）、SAHP（自注意力Hawkes）、THP（Transformer Hawkes）、AttNHP（注意力神经Hawkes）、IFTPP（强度自由TPP）、MHP（Mamba Hawkes过程）。
- **评估指标**（六类）：
  - 总对数似然（分解为时间似然和标记似然）；
  - 下一事件时间RMSE；
  - 下一标记分类准确率（EHRSHOT上使用top-10准确率）；
  - 时间校准（PCE）和标记校准（ECE）；
  - 综合排名（composite rank）。

### 3.3 主要实验结果

- S2P2在八个数据集上均取得最佳或次佳的对数似然，平均排名1.4（基线最佳为3.0）。
- 平均似然比提升1.33倍（33%），主要来自时间建模的改进。
- 下一事件时间RMSE平均排名2.3（最佳），下一标记分类平均排名1.9（最佳）。
- 校准性能在基于强度的方法中最佳，仅次于IFTPP。

---

## 4. 资源与算力

- **GPU型号与数量**：所有模型在**单张24GB NVIDIA A5000 GPU**上训练。
- **训练时长**：论文未明确报告具体训练时长，但提到模型在300个epoch内收敛。
- **其他资源**：使用EasyTPP库进行基线模型和S2P2的实现；S2P2还提供了JAX实现用于效率对比。
- **未明确说明**：总计算量（如GPU小时数）、能耗、超参数搜索的总计算开销等未详细披露。

---

## 5. 实验数量与充分性

### 5.1 实验数量

- **真实数据实验**：8个数据集 × 8个模型 × 5个随机种子 × 6类指标 ≈ 240组评估。
- **合成实验**：4类合成场景（Hawkes、自校正、非齐次Poisson、长程依赖、多变量Hawkes）。
- **消融实验**：2个维度（前向/后向ZOH × 输入依赖/非输入依赖）× 8个数据集。
- **效率实验**：序列长度从8到50万+，对比5种模型的运行时间。
- **校准实验**：8个数据集上的PCE和ECE评估及可靠性图。

### 5.2 充分性与公平性

- **充分性**：实验覆盖了预测精度、校准、效率、合成验证等多个维度，较为全面。
- **公平性**：
  - 所有基线使用EasyTPP库的统一实现；
  - 对每个模型/数据集组合进行网格搜索调参；
  - 报告5个随机种子的均值和标准差；
  - 在相同硬件条件下训练。
- **潜在问题**：
  - AttNHP在EHRSHOT上因内存不足无法训练（OOM），导致该数据集上缺少一个基线；
  - 部分数据集（如Last.fm、EHRSHOT）因规模较大，超参数搜索范围较小。

---

## 6. 主要结论与发现

1. **S2P2在八个真实数据集上取得最优或次优的预测似然**，平均排名1.4，显著优于所有基线。
2. **平均似然比提升33%**，主要驱动因素是对事件时间建模的改进。
3. **S2P2具有线性复杂度和O(log N)并行深度**，在长序列上效率显著优于Transformer类模型和RNN类模型。
4. **连续时间隐状态是关键优势**：与THP、MHP、IFTPP等离散隐状态模型相比，S2P2能更灵活地建模事件间强度演化。
5. **合成实验验证了S2P2的表达力**：能精确恢复Hawkes、自校正、非齐次Poisson等过程的真实强度函数，并捕捉长程依赖。
6. **校准性能良好**：在基于强度的方法中时间校准最佳，标记校准平均排名第二。
7. **输入依赖动力学和反向ZOH离散化**在多数数据集上带来性能提升。

---

## 7. 优点

- **方法创新性强**：首次将深度SSM技术系统性地引入MTPP建模，建立了LHP与SSM之间的理论联系。
- **计算效率高**：通过并行扫描实现O(N)工作量和O(log N)并行深度，兼顾表达力和可扩展性。
- **无需参数化解码器**：强度直接与连续演化的隐状态绑定，避免了THP/MHP等模型的参数化限制。
- **实验全面**：覆盖8个真实数据集、6类指标、5个随机种子，合成实验验证了表达力和长程依赖捕捉能力。
- **消融实验清晰**：对输入依赖动力学和ZOH方向选择进行了系统消融。
- **代码开源**：集成到EasyTPP库，便于复现和实际应用。
- **理论支撑**：引用深度SSM的通用逼近定理，论证了S2P2的表达力上限。

---

## 8. 不足与局限

- **可解释性丧失**：S2P2放弃了线性Hawkes过程的参数可解释性，不适用于需要解释底层系统的场景。
- **无法建模时间点质量**：基于强度的MTPP假设无并发事件，无法处理同一时刻多个事件的情况。
- **数值积分需求**：预测下一事件时间需要数值积分，增加了推理开销。
- **实验覆盖局限**：
  - 仅测试了离散标记空间，未涉及连续标记或更丰富的标记结构（如时空点过程）；
  - AttNHP在EHRSHOT上OOM，导致该数据集上基线不完整；
  - 未评估删失数据或对抗条件下的鲁棒性。
- **超参数敏感性**：部分数据集上输入依赖动力学反而损害性能，缺乏理论指导何时使用。
- **计算资源报告不完整**：未披露总训练时长、能耗等细节。
- **社会影响未讨论**：论文声称无社会影响，但医疗事件建模可能涉及隐私和公平性问题。
- **未来方向**：恢复LHP类可解释性、扩展到非分类标记、作为预训练骨干、处理删失和对抗条件等。

---

（完）
