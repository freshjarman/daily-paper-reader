---
title: Causal Discovery from Interval-Based Event Sequences
title_zh: 基于区间事件序列的因果发现
authors: "Lénaïg Cornanguer, Joscha Cüppers, Jilles Vreeken"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39201/43162"
tags: ["query:tpp-es"]
score: 7.0
evidence: 基于区间事件序列的因果发现
tldr: 针对现有事件序列因果发现方法假设事件为瞬时点事件、忽略事件持续时间的问题，本文提出面向区间事件序列的因果模型，可刻画事件间交互以及依赖其他事件是否正在发生的因果机制。作者证明该模型在极限意义下可识别，并基于算法马尔可夫条件提出实用的因果发现算法Niagara。实验验证了方法的有效性，对医疗等带持续时间事件序列的因果分析具有价值。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 现有事件序列因果发现假设事件瞬时，忽略真实场景中事件的持续时间。
method: 提出区间事件序列因果模型，并基于算法马尔可夫条件给出Niagara算法。
result: 证明模型极限可识别，并通过实验验证实用因果发现效果。
conclusion: 为带持续时间的事件序列因果建模提供了可识别且实用的方法。
---

## Abstract
In this paper we address the problem of discovering causal relationships from observational event sequence data.
Existing methods typically assume that events are instantaneous point events, however in many real-world settings, events have duration.
For example, in healthcare, a patient's symptoms may persist over a time interval and influence clinical actions while ongoing.
To address this, we introduce a causal model for interval-based event sequences that captures rich causal structures, including interactions between events and causal mechanisms that depend on whether other events are ongoing.
We prove that our model is identifiable in the limit and present a practical causal discovery algorithm, Niagara, grounded in the algorithmic Markov condition.
To select among candidate models, we employ a minimum description length (MDL) criterion, enabling robust inference even with limited data.
We validate our approach on synthetic and real data and demonstrate its utility on a real-world medical case study, where it uncovers meaningful causal relationships from noisy, interval-based event data.

---

## 论文详细总结（自动生成）

# 论文总结：Causal Discovery from Interval-Based Event Sequences

## 1. 核心问题与整体含义

- **研究动机**：现有事件序列因果发现方法（如 Granger 因果、SHP、CAUSE、CASCADE 等）大多假设事件是**瞬时点事件**（instantaneous point events），仅关注事件的发生时刻，忽略了事件在真实世界中往往具有**持续时间**这一事实。
- **现实背景**：在医疗、经济、网络安全等领域，事件的持续性本身往往是关键。例如：患者症状可能持续一段时间并在持续期间影响临床决策；抗生素的持续给药会导致周期性的生命体征监测。仅看事件起点不足以解释重复给药等行为。
- **核心问题**：如何从**基于区间的事件序列**（interval-based event sequences）中，发现具有干预语义的真正因果关系，而非仅仅预测性关联。
- **整体意义**：论文填补了"事件持续时间"这一空白，提出了支持事件时长、多父节点交互、以及基于条件（conditioning）的因果机制的可识别因果模型，并给出了实用算法 NIAGARA。

## 2. 方法论

### 2.1 核心思想
- 每个事件 $e_i$ 由一组**独立的数据生成过程** $\Theta_i$ 生成，每个过程负责该事件的一部分发生实例（occurrences）。
- 每个事件至少有一个**背景过程**（齐次泊松过程），刻画无因果影响下的自发/噪声驱动发生。
- 因果影响分为两类：
  - **触发（Triggering）**：另一事件的发生在延迟后触发 $e_i$ 的发生。
  - **条件（Conditioning）**：一个或多个父事件的"正在进行（ongoing）"状态通过（a）调节泊松过程强度，或（b）对触发过程施加条件，影响 $e_i$ 的生成。

### 2.2 关键定义
- **事件发生实例**：$x = (t_s, t_e)$，即开始与结束时间。
- **因果机制** $\omega = (\varepsilon_\omega, F_\omega)$：
  - $\varepsilon_\omega$：可选的触发事件（可为空）。
  - $F_\omega$：关于谓词 $\mathrm{on}(e_j)$ 的命题逻辑公式（合取与否定），定义机制活跃的时间区间。
- **数据生成过程** $\vartheta = (T_\vartheta, \varpi_\vartheta, \omega_\vartheta)$：过程类型、参数、因果机制。
- **四类过程**（对应图 1）：
  - (a) 背景泊松过程（无因果机制）；
  - (b) 触发过程（仅触发父节点）；
  - (c) 条件触发过程（触发 + 条件）；
  - (d) 条件泊松过程（仅条件）。
- **因果图** $G=(V,E)$：节点为事件，边表示父事件参与某因果机制。

### 2.3 数据建模（统一延迟视角）
- 所有情形都可归约为延迟序列 $\Delta_\vartheta$，并定义其概率密度 $\varrho(d|\varpi)$：
  - **背景泊松过程**：延迟服从指数分布 $p_{\exp}(d; \lambda_\vartheta)$。
  - **条件泊松过程**：强度为 $\lambda_\vartheta(t) = c_\vartheta$（若 $t \in I_\vartheta$）否则为 0，延迟基于活跃区间积分计算。
  - **（条件）触发过程**：父事件以概率 $\phi_\vartheta$ 触发子事件，延迟服从强度 $\lambda_\vartheta$ 的指数分布；未触发则 $d = \infty$，概率为 $1-\phi_\vartheta$。

### 2.4 可识别性
- **定理 1**：在（i）触发过程平均延迟严格为正、（ii）因果机制平稳、（iii）满足因果马尔可夫条件/忠实性/充分性 的条件下，区间事件序列的真实因果模型在极限意义下可识别。

### 2.5 MDL 评分
- 采用**两部分 MDL**（算法马尔可夫条件的近似），总代价：
  $$L(\mathcal{M}, D) = L(\mathcal{K}) + L(\Phi) + L(D|\Theta)$$
  - $L(\mathcal{K})$：编码所有因果机制（触发事件、参与 $F_\omega$ 的父节点子集及是否取反）。
  - $L(\Phi)$：参数编码，使用 Rissanen 整数编码 $L_R(v) = L_N(d) + L_N(\lceil v \cdot 10^d \rceil) + 1$。
  - $L(D|\Theta)$：数据负对数似然。
- 最优模型为最小化总代价者：$\mathcal{M}^* = \arg\min_{\mathcal{M}\in\mathcal{M}} L(\mathcal{M}, D)$。

### 2.6 NIAGARA 算法流程
1. **因果机制选择**：因存在父节点交互无法逐一识别父节点，采用贪心策略，按"集成该机制带来的代价增益"从高到低选择，并以无环约束作为安全网。
2. **事件发生实例划分**（Algorithm 1）：
   - 背景 vs 触发过程：迭代重分配，最小化全局负对数似然。
   - 多个泊松过程：利用非重叠活跃区间估计强度，重叠区间按强度比例分配。
3. **可选的因果超集估计**：用条件频率启发式（窗口长度 $w$、最大噪声比例 $\rho_{\max}$）计算四个统计量，筛选候选机制，大幅剪枝搜索空间。
4. **复杂度**：最坏情况 $O(|\mathcal{E}| \cdot n_{ch}^2)$，对发生实例数是多项式的（无界情形为事件数指数级）。

## 3. 实验设计

### 3.1 数据集 / 场景
- **合成数据**：按本文因果模型生成，变化参数包括：
  - 事件数（默认 $|\mathcal{E}|=10$）；
  - 观测周期（默认 $T=500{,}000$）；
  - 噪声比例（默认 $\rho_{\max}=0.05$）。
- **真实世界数据**：PCIC 2021 因果发现挑战赛的三个公开数据集（电信设备告警区间数据）：18V_55N_Wireless、24V_439N_Microwave、25V_474N_Microwave。
- **医疗案例研究**：MIMIC-III 数据库，聚焦脓毒症（sepsis）患者队列，共 1,184 名患者，提取服务转移、液体给药、医疗操作等条目，得到 532 个不同事件、477,491 个发生实例。

### 3.2 Benchmark 与对比方法
- **评价指标**：
  - SHD（结构汉明距离）；
  - SID（结构干预距离，仅对有向无环图，故排除 CAUSE）；
  - F1 分数（边级别精确率与召回率的调和平均）。
- **对比方法**：CAUSE、SHP（可建模父节点交互）、CASCADE（基于 AMC 的触发机制方法）。

## 4. 资源与算力

- **论文未明确说明使用的 GPU 型号、数量或训练时长**。
- 仅在可扩展性实验中间接报告了**运行时间**：在 40 个事件时，NIAGARA 的中位运行时间为 8346 秒，而使用因果超集启发式后降至 793 秒。
- 这表明本文方法主要涉及统计推断与 MDL 搜索，而非深度学习训练，因此未报告 GPU 算力。

## 5. 实验数量与充分性

- **实验组数**（大致）：
  1. 合成数据上的可识别性实验（随观测周期 $T$ 变化）；
  2. 合成数据上的可扩展性实验（事件数 5–40）；
  3. 合成数据上的噪声鲁棒性实验（噪声比例 0.01–0.4）；
  4. 三个 PCIC 2021 真实数据集实验；
  5. MIMIC-III 医疗案例研究。
- **消融/变体**：NIAGARA 与 NIAGARA-heuristic（带因果超集估计）的对比，验证启发式在不损失性能的前提下加速。
- **充分性评价**：
  - 覆盖了数据规模、噪声、事件数等多维度，合成实验设计较为系统；
  - 与多个 SOTA 方法（CAUSE、SHP、CASCADE）对比，指标多维（SHD、SID、F1），较为客观；
  - 但真实数据集仅 PCIC 三个 + MIMIC-III 一个案例，真实场景覆盖仍有限；MIMIC-III 缺少检验结果与临床笔记，存在显著混淆，作者也承认这一点。

## 6. 主要结论与发现

- **可识别性**：NIAGARA 随观测周期增大能恢复真实因果图，验证了极限可识别性；在有限数据下表现仍接近最优。
- **可扩展性**：随事件数增加性能保持稳定；因果超集启发式显著降低运行时间而不损失性能。
- **噪声鲁棒性**：噪声比例 $\rho$ 直到 0.3 才开始明显下降。
- **真实数据表现**：PCIC 数据集 F1 分别为 0.57、0.35、0.36，与专门针对拓扑数据的方法相当，明显优于多数已有结果。
- **医疗案例发现**：
  - 抗生素给药常与葡萄糖（溶剂）共现，并以"无其他抗生素正在进行"为条件（如 Dextrose5%、PenicillinG → Vancomycin），反映抗生素通常单药使用。
  - 有创通气导致周期性滤器更换、肺特异性营养配方给药、肌肉松弛剂使用，甚至触发器官捐献服务通知（反映机构协议）。
  - 这些关系符合医学常识，且其他方法因无法表达父节点交互和事件持续时间而无法发现。

## 7. 优点

- **建模能力强**：首次在事件序列因果模型中同时支持事件持续时间、多父节点交互、以及基于"正在进行"状态的条件机制。
- **理论保证**：给出极限可识别性证明，并基于算法马尔可夫条件提供 MDL 评分，在有限数据下仍稳健。
- **算法实用**：NIAGARA 为多项式复杂度，并提供可选的因果超集估计启发式以加速；有确定性与局部收敛性保证。
- **统一框架**：通过延迟序列将背景泊松、条件泊松、触发、条件触发四类过程统一建模，理论优雅。
- **实验结合真实医疗场景**：MIMIC-III 案例发现的因果关系具有临床可解释性，验证了方法的实用价值。

## 8. 不足与局限

- **因果充分性假设**：与所有因果发现方法一样，依赖因果充分性（无隐混淆），MIMIC-III 案例中作者明确承认存在显著混淆（未纳入检验结果与临床笔记）。
- **划分算法无理论保证**：事件发生实例的划分（触发过程匹配、多泊松过程分离）可能收敛到局部最优，无法保证恢复真实划分；触发过程中因果匹配在早期原因产生晚于后期原因的效果时存在歧义。
- **泊松过程划分依赖条件**：需要低噪声和足够的非重叠活跃区间，条件不佳时近似会退化。
- **实验覆盖有限**：真实数据仅限 PCIC 三个数据集和 MIMIC-III 单一队列；合成数据虽系统但仍是模型内生成，可能有利于本方法。
- **算力信息缺失**：未报告 GPU 或训练资源，复现成本不透明。
- **超参数依赖**：因果超集估计需要设定窗口 $w$ 与最大噪声比例 $\rho_{\max}$，选择影响搜索严格性。
- **未来方向**：作者提出放松因果充分性假设、在事件序列中识别混淆是未来工作。

（完）
