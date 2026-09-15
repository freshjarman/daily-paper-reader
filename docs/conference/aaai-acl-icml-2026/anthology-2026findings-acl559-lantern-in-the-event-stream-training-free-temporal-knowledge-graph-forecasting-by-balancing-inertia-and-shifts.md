---
title: "LANTERN in the Event Stream: Training-Free Temporal Knowledge Graph Forecasting by Balancing Inertia and Shifts"
title_zh: 事件流中的LANTERN：通过平衡惯性与突变实现免训练时序知识图谱预测
authors: "Chengyuan Jin, Ao Chang, Daojian Zeng, Wenhao Teng, Xiangwen Liao, Kang Liu, Jun Zhao, Yubo Chen"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.findings-acl.559.pdf"
tags: ["query:tpp-es"]
score: 4.0
evidence: 事件流预测
tldr: 针对时序知识图谱预测中免训练大模型方法高度依赖提示所包含历史事件的问题，本文提出LANTERN框架，融合长窗口的稳定交互模式分数与短窗口的新颖变化分数，先过滤无用事件，再用帕累托贪心选择紧凑证据集，并加入结构感知分析。实验表明该方法在有限上下文预算下更准确地排序未来实体。该工作与事件序列预测相关，但面向知识图谱而非连续时间点过程强度建模。
source: ACL-2026-Findings
selection_source: conference_retrieval
motivation: 免训练大模型做时序知识图谱预测时，准确率严重依赖提示中选取的历史事件。
method: 提出LANTERN，结合长窗口稳定分与短窗口新颖分，用帕累托贪心选取紧凑证据。
result: 在有限上下文预算下提升了未来实体排序的准确性。
conclusion: 为事件流驱动的时序预测提供了免训练的证据选择方案。
---

## Abstract
Temporal knowledge graph forecasting(TKGF) asks a model to rank the mostplausible future entity for a query such as(s, r, ?, t) from historical events. Recenttraining-free methods use large languagemodels (LLMs) for this task, but their accuracydepends heavily on which past events areshown in the prompt under a tight contextbudget. We present LANTERN, a training-freeprompting framework that addresses thisbottleneck by combining two complementaryviews of history: a long-window strengthscore for stable interaction patterns anda short-window novelty score for suddenchanges. LANTERN first filters unhelpfulevents, then selects a compact evidence setwith Pareto-greedy selection, and finally addsone structure-aware analogical demonstration.Across ICEWS14, ICEWS05-15, ICEWS18,and GDELT, LANTERN consistently outperforms the state-of-the-art training-free baselineAnRe under the same backbone and 2-hopcandidate protocol, improving Hits@1 by upto 2.5 points and MRR by up to 1.2 points.

---

## 论文详细总结（自动生成）

# 论文总结：LANTERN —— 事件流中的免训练时序知识图谱预测

## 1. 核心问题与整体含义（研究动机与背景）

- **任务背景**：时序知识图谱预测（TKGF）要求模型基于历史事件序列（形如 `(s, r, o, t)`），对未来的查询 `(s_q, r_q, ?, t_q)` 排序出最可能的未来实体。
- **研究范式转变**：传统监督方法（如 RE-NET、CyGNet、TiRGN 等）需针对数据集训练，对分布漂移敏感；近期兴起的**免训练（training-free）**方法用大语言模型（LLM）通过上下文学习完成预测，无需参数更新。
- **核心瓶颈**：LLM 的预测精度**高度依赖提示（prompt）中选取了哪些历史事件**，而上下文预算严格受限。语义检索或简单时间近邻的选证据策略，往往陷入两种失效模式：
  - 被**陈旧、重复的历史模式（惯性 inertia）**主导；
  - 或被**近期噪声事件**干扰，无法识别真正有意义的变化。
- **核心洞察**：真实事件流同时具有**长期稳定的交互惯性**与**突发的机制突变（regime shift）**，二者构成一对互补信号，而现有方法未能显式建模这一张力。
- **整体含义**：论文提出 **LANTERN** 框架，将"惯性—突变"的权衡显式引入免训练 LLM 提示构建，在不增加训练成本的前提下提升预测精度与效率。

## 2. 方法论

### 2.1 核心思想
将证据选择建模为一个**双视角（long/short window）多目标选择问题**：长窗口刻画稳定偏好（Strength），短窗口捕捉突发变化（Novelty），再用**帕累托贪心**在固定预算下选出紧凑证据集，并配一个**结构感知的类比演示**引导 LLM 推理。

### 2.2 关键技术细节

- **查询中心有向历史构建**：
  - 收集涉及 `s_q` 的历史池 `H(s_q)`；
  - 引入逆关系 `r^{-1}`，统一转换为以 `s_q` 为源头的有向交互 `(s_q, r̃, v, t)`，保证方向一致性。
- **固定计数窗口（fixed-count window）**：
  - 用**事件数量**而非时间跨度定义窗口，避免高密度时段淹没信号，并使 token 用量稳定；
  - 长窗口 `N_ℓ = 100`，短窗口 `N_s = 10`（`N_s ≪ N_ℓ`）。
- **Strength（强度/惯性）**：用对称 Dirichlet 先验的后验均值建模稳态偏好分布：
  - `Str(s_q, r̃, v) = (c_ℓ(v) + α₀) / (C_ℓ + α₀·|V_{q,r̃}|)`
- **Novelty（新颖性/突变）**：用 **Beta-Binomial** 模型量化短窗口计数 `c_s(v)` 在长期基线下的"惊讶度"，定义为**负对数生存概率** `Nov = -log Pr(X ≥ c_s(v))`，其中先验参数由 Strength 导出。
  - 该分数随短窗口计数上升而增、随先验强度上升而减，符合"机制突变"直觉；
  - 相比 z-score 能处理事件流的**过度离散（overdispersion）**。
- **LLM 有用性门控（usefulness gate）**：
  - 按时间分位分 K=4 个 bin，每 bin 预筛至多 `M_use=25` 条；
  - 让 LLM 对每条事件打分（label-token 概率的 softmax），并用**动态阈值** `c_j` 过滤（越旧的事件阈值越严）。
- **帕累托贪心选择（Pareto-greedy）**：
  - 对 (Novelty, Strength) 双目标做**帕累托分层**（迭代剥离非支配前沿），避免线性加权超参；
  - 在预算 `B=100` 内贪心选择，同时施加三类确定性约束：**时间覆盖**（每 bin 上限 25）、**关系多样性**（每关系上限 ⌈ρ_rel·B⌉）、**反冗余**（同 (r̃, v) 重复上限 3）。
- **结构感知类比演示（analogical demonstration）**：
  - 默认只用 1 个演示（`m=1`，与 AnRe 结论一致）；
  - 相似度 = **语义相似度**（BERT [CLS] 余弦）+ **结构相似度**（基于 (Str, Nov) 的低维惯性—突变画像余弦）；
  - 权重 β 用**自适应移位 sigmoid**，由数据集结构规则度 `R_struct` 决定；
  - 让 LLM 生成**过程解释 p_a**，演示为四元组 `(G_a, q_a, o_a, p_a)`，实现"类比重放（analogical replay）"。
- **推理**：最终提示 = 1 个类比演示 + 证据集 `G_q` + 查询与候选列表（映射为数字标签），按 label-token 似然排序。

### 2.3 可选组件
- **关系级层次回退（backoff）**：查询历史极稀疏时，混合关系级先验；
- **漂移感知的长窗收缩**：用 KL 散度检测漂移，检测到则收缩长窗有效长度。

## 3. 实验设计

- **数据集（4 个标准 TKGF benchmark）**：
  - ICEWS14、ICEWS05-15、ICEWS18、GDELT（均源自政治事件流）。
- **评测指标**：MRR 与 Hits@1/3/10，采用标准**时间感知过滤协议**（过滤同一时间戳的其他真实事实）。
- **候选协议**：统一使用 **2-hop 历史邻居**协议（1-hop 作对照），候选上限 `C_max=100`。
- **LLM 骨干**：默认 **InternLM2-7B**；泛化实验另用 Mistral-7B、Qwen2.5-7B-Instruct、Llama-3.1-8B-Instruct、Gemma-2-9B-It。
- **对比方法**：
  - **免训练 LLM 基线**：ICL、CoH、ONSEP、AnRe（1-hop 与 2-hop）；
  - **监督基线（参考）**：RE-NET、CyGNet、xERTE、TITer、TiRGN、DiffuTKG、GenTKG。
- **默认超参**：`N_ℓ=100, N_s=10, α₀=1.0, B=100, K=4, ϕ=2.0` 等，四数据集共享同一配置。

## 4. 资源与算力

- 论文仅在附录 D.1 提到：**所有实验在 NVIDIA RTX 3090 GPU 上完成**。
- **未明确说明 GPU 数量、总训练时长或推理总时长**——这与方法本身"免训练"（无需参数更新）的定位一致，主要成本为 LLM 推理。
- 效率相关数据：最终排序提示 token 从 AnRe 的约 5,100 降至约 3,200（**减少约 37%**），但端到端吞吐（it/s）因多阶段门控而降低（0.9 vs AnRe 1.5）。

## 5. 实验数量与充分性

- **主实验**：4 个数据集 × (MRR + 3 档 Hits@k) × 多类基线，规模完整。
- **消融实验**：在 ICEWS18（突变为主）与 ICEWS14（稳定为主）上分别做：
  - 去掉有用性门控、去掉 Novelty、去掉 Strength；
  - 用频率比 / z-score 替换 Novelty；
  - 演示策略：β=1.0（纯语义）、β=0.0（纯结构）、β=0.5（固定混合）；
  - 去掉时间覆盖约束。
- **跨模型泛化**：5 种 LLM 架构对比。
- **机制突变鲁棒性**：按"真实答案长窗稀有度"分 Q1–Q5 分位，观察相对 AnRe 的 H@1 增益。
- **稀疏查询回退**：按历史密度分层（0–25% 最稀疏），对比有无 backoff。
- **效率与成本**：token/query、it/s、LLM 调用次数分解。
- **敏感性分析**：`N_s`、`α₀`、`ζ`、`ϕ` 的取值区间。
- **漂移策略对比**：无适配 / 硬收缩 / 软混合。
- **候选集分析**：hop 数与 Oracle Recall、token 成本的权衡。
- **案例研究**：ICEWS18 上一个法国—摩洛哥清洁能源的真实例子。
- **充分性与公平性评价**：
  - **较为充分**：覆盖多数据集、多基线、多维度消融与鲁棒性分析；
  - **公平性较好**：与基线在同一骨干、同一候选协议、同一证据预算（B=100）下对比，并报告配对 t 检验（p<0.05）；
  - **可改进点**：成本敏感的分析仅用 500 条分层抽样；监督基线数值多引用自前作而非复现；GDELT 上部分基线（CoH/ONSEP）缺数。

## 6. 主要结论与发现

- LANTERN 在四个 benchmark 上**一致优于最强的免训练基线 AnRe**（同骨干、同候选协议），**Hits@1 最高提升 2.5 个点、MRR 最高提升 1.2 个点**，且提升具统计显著性（p<0.05）。
- **惯性—突变的相对重要性随数据集变化**：
  - ICEWS18（突变重）：去掉 Novelty 使 H@1 从 0.285 掉到 0.235（-5.0 点）；
  - ICEWS14（惯性主导）：仅用 Strength 的变体在 MRR/H@1 上甚至略超完整模型。
- **增益集中在稀有/难预测查询**：按真实答案稀有度分桶，Q1 仅 +0.5 点，Q5 高达 **+4.8 点**。
- **演示需"主题相关 + 惯性—突变对齐"**：自适应混合优于纯语义或纯结构。
- **时间覆盖约束有效**：防止单一时间区域主导提示。
- **跨模型可迁移**：更强底座模型（Llama-3.1-8B、Gemma-2-9B）带来更大增益，方法模型无关。
- **效率优势**：在保持精度提升的同时，峰值提示 token 减少约 37%。
- **稀疏场景**：关系级 backoff 在历史最稀疏的 25% 查询上显著提升鲁棒性（MRR 0.310→0.335）。
- **漂移处理**：硬收缩优于软混合。

## 7. 优点（方法 / 实验设计亮点）

- **问题定位精准**：把"惯性 vs 突变"这一非平稳性核心张力显式形式化，弥补了以往语义检索/近期性策略的不足。
- **免训练、即插即用**：无需重训，可与更强候选检索模块解耦搭配。
- **无权重超参的多目标选择**：用帕累托分层替代线性加权，减少调参负担。
- **固定计数窗口设计巧妙**：同时稳定了统计样本量与提示 token 预算，适配免训练提示场景。
- **统计方法恰当**：用 Beta-Binomial 处理事件流的过度离散，比 z-score 更契合突发事件。
- **演示选择自适应**：用数据集结构规则度自动调节语义/结构权重，避免硬编码。
- **实验较全面**：多数据集、多基线、多消融、跨模型、稀有度分桶、稀疏回退、效率分析、案例研究齐备，且报告显著性检验。
- **效率与精度兼顾**：在提升精度的同时降低 token 成本，实用价值明确。

## 8. 不足与局限

- **窗口假设的局限**：固定计数窗口在**高度不规则时间间隔或连续时间动态**场景下可能次优，时间跨度窗口可能更合适（论文自述）。
- **有用性门控的偏差风险**：依赖 LLM 内部知识，可能**过度过滤长尾证据**，以牺牲召回换精度。
- **候选集天花板**：依赖 2-hop 邻居构造候选，无法恢复候选集外的真实答案；这是当前免训练协议的通病，非本方法独有。
- **领域覆盖有限**：仅在政治事件流（ICEWS、GDELT）上验证，未扩展到其他领域或低资源场景。
- **算力信息不完整**：未报告 GPU 数量与推理/训练时长，成本结论的可复现性略受限。
- **分析抽样成本限制**：部分成本敏感分析仅用 500 条查询的分层样本，统计稳健性有限。
- **监督基线非全部复现**：部分数值引自前作，且 GDELT 上部分基线缺失，横向对比完整度受限。
- **超参敏感性声明保守**：作者明确表示仅在 `α₀∈[0.5,2.0]`、`ζ∈[2.0,3.5]` 区间稳健，未主张更广范围的不敏感性。

（完）
