---
title: "Beyond Missing Data Imputation: Information-Theoretic Coupling of Missingness and Class Imbalance for Optimal Irregular Time Series Classification"
title_zh: 超越缺失值插补：面向最优不规则时间序列分类的缺失性与类别不平衡信息论耦合
authors: "Xin Qin, Mengna Liu, Wenjie Wang, Shuxin Li, Tianjiao Li, Xiufeng Liu, Xu Cheng"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39682/43643"
tags: ["query:tpp-es"]
score: 5.0
evidence: 面向不规则时间序列的缺失建模与插补感知分类
tldr: 不规则时间序列广泛存在，采样不均与缺失数据给深度特征建模带来挑战，且缺失模式与类别不平衡常被忽视。本文提出信息论框架，将缺失性结构与类别不平衡耦合建模，以缓解稀疏观测对少数类的表示损害。方法在不规则时间序列分类任务上提升了性能，为连续时间稀疏事件/观测的建模提供了可借鉴思路。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 不规则时间序列中采样不均和缺失严重，且缺失模式与类别不平衡常被忽略，导致分类偏差。
method: 提出信息论框架，耦合缺失性结构与类别不平衡以改进不规则时间序列分类的特征建模。
result: 实验表明该方法缓解了稀疏观测对少数类的损害并提升分类表现。
conclusion: 将缺失性纳入建模为不规则时间序列分类提供了有效途径。
---

## Abstract
Irregular time series (IRTS) are prevalent in real-world applications, where uneven sampling and missing data pose fundamental challenges to deep learning-based feature modeling. Although existing methods attempt to retain timestamp information, they often overlook the structured patterns embedded within the missingness itself, and tend to perform poorly when confronted with class imbalance exacerbated by data incompleteness. Specifically, temporal irregularity hinders the modeling of long-range dependencies
and local patterns, while sparse observations limit representational capacity, disproportionately impairing minority classes and leading to severe classification bias. To address these deeply coupled challenges, we propose SPECTRA (Structured Pattern and Enriched Context-aware Temporal Representation Architecture), a unified framework for robust IRTS classification. SPECTRA introduces a frequency-guided observation encoder that reconstructs temporal dependencies in a stable manner, mitigating spectral distortion and information corruption. Complementarily, a missingness pattern encoder explicitly captures the dynamic evolution of missing data and leverages it as a discriminative signal. In addition, a prototype-constrained classification paradigm directly optimizes the geometric structure of the feature space, enhancing intra-class compactness and alleviating generalization bottlenecks caused by class imbalance. Extensive experiments on three public IRTS datasets—P12, P19, and PAM—demonstrate the superior performance of SPECTRA under both missing and imbalanced conditions.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究动机**：不规则时间序列（IRTS）广泛存在于临床、可穿戴等场景，采样不均与缺失数据使深度特征建模困难；更关键的是，缺失往往与类别不平衡同时出现，少数类样本不仅更少，而且可能更不完整。
- **核心问题**：现有方法通常把“缺失值处理”和“类别不平衡处理”视为两个独立问题，忽略了缺失模式本身可能携带类别判别信息。论文提出并形式化 **Missing-Imbalance Coupling（缺失—不平衡耦合）**：在 MAR/MNAR 数据生成过程下，缺失模式 \(M\) 与类别标签 \(Y\) 之间存在非零互信息 \(I(Y;M)>0\)，且耦合强度 \(\kappa>0\)。
- **整体含义**：论文主张从“超越缺失值插补”的角度出发，不再仅把缺失当作噪声或待填补对象，而是把缺失结构作为显式信息源，与类别不平衡联合建模，从而提升 IRTS 分类的鲁棒性与判别性。
- **三大挑战**：论文将其归纳为：
  - **不可恢复的谱失真**：不规则采样导致频谱泄漏与混叠，且失真集中在少数类。
  - **少数类表示坍塌**：少数类缺失率更高，特征弱、信噪比低，易被多数类信号淹没。
  - **有偏优化动态**：少数类梯度稀少、不可靠、幅度小，模型易收敛到忽略少数类的退化解。

## 2. 方法论

- **总体框架**：提出 **SPECTRA**（Structured Pattern and Enriched Context-aware Temporal Representation Architecture），采用双流结构联合建模观测数据与缺失模式，包含三大模块：MAFF、MPE、CGFR。
- **问题定义**：数据集 \(D=\{(X^{(n)},M^{(n)},y^{(n)})\}\)，其中 \(X\in\mathbb{R}^{C\times L}\) 为多变量时间序列，\(M\in\{0,1\}^{C\times L}\) 为二值缺失掩码，\(y\) 为类别标签。
- **理论基础**：
  - 定义耦合强度 \(\kappa=\max_{i,j}|I(Y=i;M)-I(Y=j;M)|\)，并证明在类依赖观测概率下 \(\kappa>0\)。
  - 给出分类误差下界：  
    \(R^* \ge \frac{1}{2}\left(1-\sqrt{\frac{I(X,M;Y)-\kappa H(M)}{H(Y)}}\right)\)。
  - 理论框架连接耦合理论、谱—时对偶、信息几何学习，声称可达到信息论最优。
- **MAFF：缺失感知频率滤波模块**：
  - **SCSE（自校准谱增强）**：对输入做全局平均池化，经 MLP 与 Softmax 生成低/中/高频带注意力权重 \(\alpha_k\)；用固定频带掩码 \(M_k\) 加权合成自适应掩码 \(M_{\text{adapt}}=\sum_k \alpha_k M_k\)；再对频谱 \(F(X)\) 逐点滤波并逆变换得到增强表示 \(X'=F^{-1}(F(X)\odot M_{\text{adapt}})\)。
  - **AG-DRR（缺失引导动态感受野重构）**：根据每个时间步邻域缺失率 \(m_t\)，用元学习控制器生成动态权重 \(\beta_{t,k}\)，对并行膨胀卷积核输出加权求和。信息密集区域偏向低膨胀核，稀疏区域偏向高膨胀核，从而跨缺失段聚合信息。
- **MPE：缺失模式编码器**：
  - 用门控卷积提取局部缺失 motif：  
    \(H_{\text{local}}=\tanh(W_{\text{cand}}*M+b_{\text{cand}})\odot\sigma(W_{\text{gate}}*M+b_{\text{gate}})\)。
  - 再用 GRU 建模缺失模式的全局时间动态，输出 \(F_{\text{miss}}\)，作为缺失机制的高维语义表示。
- **CGFR：类别引导特征精炼**：
  - 将观测特征 \(F_{\text{data}}\) 与缺失特征 \(F_{\text{miss}}\) 自适应融合为 \(F_{\text{fused}}\)。
  - 在信息几何/黎曼流形视角下学习类原型 \(c_k\)，分类 logit 定义为负平方欧氏距离：  
    \(\text{logit}_k(z)=-\|z-c_k\|^2\)。
  - 总损失：  
    \(L_{\text{total}}=L_{\text{CE}}+\gamma L_{\text{center}}\)，  
    \(L_{\text{center
