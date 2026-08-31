---
title: Synthetic Longitudinal Tabular Data Generation via Copula
title_zh: 基于 Copula 的纵向表格数据合成生成
authors: "Cai, H., Yu, W., Lu, R., Chattopadhyay, I., Zhang, X., Liu, J."
date: 2026-08-07
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.03.742474v1.full.pdf"
tags: ["query:ehr-es"]
score: 9.0
evidence: 基于copula的纵向表格数据合成与电子病历生成模型及患者轨迹生成相关
tldr: 合成纵向表格数据需保留受试者内依赖，但现有生成方法如GAN易过拟合且依赖结构难解释。基于eCDF-copula的统计方法通过经验分布与copula建模，结合多重插补处理缺失数据，同时保留访问内外依赖。在两种不同规模临床数据上，该方法相似性与实用性超越四种先进方法，隐私保护相当。为纵向数据共享提供可解释、稳健的生成方案。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-03-742474-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1644, \"height\": 939, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-03-742474-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1646, \"height\": 1109, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-03-742474-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1641, \"height\": 406, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-03-742474-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1660, \"height\": 513, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-03-742474-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1160, \"height\": 638, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-03-742474-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1590, \"height\": 984, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-03-742474-v1/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1649, \"height\": 690, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-08-03-742474-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1658, \"height\": 454, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-08-03-742474-v1/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1662, \"height\": 313, \"label\": \"Table\"}]"
motivation: 纵向健康数据的合成需保留重复测量依赖，但GAN等方法易过拟合且缺乏可解释性。
method: 采用eCDF-copula建模，结合多重插补两阶段处理缺失数据，并量化复制变异性。
result: 在两种规模（n=120和n=3612）的临床数据上，eCDF-copula在相似性和实用性上超过四种对比方法，隐私相当。
conclusion: eCDF-copula提供可解释、稳健的纵向数据合成方案，兼顾隐私与效用。
---

## 摘要
合成数据生成越来越被用于在保护参与者隐私的同时实现数据共享和二次分析，特别是在纵向表格健康数据中，每个受试者的重复测量会产生受试者内部的依赖性，而大多数合成数据方法并非旨在保留这种依赖性。现有的生成方法，特别是基于生成对抗网络（GAN）的方法，可以建模复杂分布，但其估计的依赖结构往往难以解释，并且在中型数据集中性能可能不稳定或容易过拟合。在这里，我们展示了 eCDF-copula——一种使用经验累积分布函数（eCDF）和 copula 建模的统计基础方法——能够保留访问内和访问间的依赖结构。为了处理普遍的缺失数据，我们提出了一种两阶段策略，将多重插补与基于 copula 的合成相结合，从而实现方差分解，以量化不同方法间的复制变异性。我们在两个样本量差异显著（n = 120 与 n = 3,612）的纵向临床数据集上，将所提出的方法与四种既有方法进行了基准测试。eCDF-copula 的相似性和实用性均超过了最先进的合成数据方法，同时保持了相当的隐私性。

## Abstract
Synthetic data generation is increasingly used to enable data sharing and secondary analysis while protecting participant privacy, particularly for longitudinal tabular health data, where repeated measures per subject create within-subject dependence that most synthetic data methods are not designed to preserve. Existing generative methods, particularly generative adversarial network (GAN)-based approaches, can model complex distributions, but their estimated dependence structures are often difficult to interpret and their performance may be unstable or prone to overfitting in modestly sized datasets. Here we show that eCDF-copula, a statistically rooted approach using the empirical cumulative distribution function (eCDF) and copula modeling, preserves within- and between-visit dependence structure. To handle pervasive missing data, we propose a two-stage strategy combining multiple imputation with copula-based synthesis, enabling a variance decomposition that quantifies replication variability across methods. We benchmarked the proposed approach against four established methods on two longitudinal clinical datasets spanning markedly different sample sizes (n = 120 vs. n = 3, 612). eCDF-copula achieved resemblance and utility exceeding those of state-of-the-art synthetic data methods, while maintaining comparable privacy.

---

## 论文详细总结（自动生成）

# 基于 Copula 的纵向表格数据合成生成——论文详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：合成数据生成是保护患者隐私、促进数据共享与二次分析的重要技术。然而，**纵向健康数据**中每个受试者包含多次重复测量，形成了**受试者内部的时序依赖**（即“访问内”和“访问间”的依赖结构），大多数现有合成数据方法并未针对这种依赖进行设计，导致生成的合成数据在统计保真度上存在根本缺陷。
- **现有方法的不足**：以生成对抗网络（GAN）为代表的深度生成方法能够建模复杂分布，但其估计出的依赖结构**难以解释**，且在中型数据集（modest sample size）上**性能不稳定、容易过拟合**。这限制了其在临床纵向数据中的可靠应用。
- **整体含义**：论文主张一种统计学根基更扎实的替代方案——**eCDF-copula**（经验累积分布函数 + copula 模型），它既能显式保留访问内/访问间的依赖结构，又具有可解释性，同时在不同规模的数据集上都能稳健地平衡数据效用与隐私保护。该工作为纵向临床数据的可共享生成提供了一条新的、可解释的、非深度学习的路线。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：将“边缘分布建模”与“依赖结构建模”分离。使用**经验累积分布函数（eCDF）** 对每个变量的边缘分布进行非参数拟合，使用 **copula** 对变量间的依赖结构进行建模，从而生成与原始数据在单变量分布和多变量相关性上均高度相似的合成数据。
- **关键技术：两阶段缺失数据处理策略**（处理纵向数据中普遍存在的缺失值）：
  1. **第一阶段——多重插补（Multiple Imputation, MI）**：对原始缺失数据执行多次插补，生成多个完整的插补数据集。
  2. **第二阶段——基于 copula 的合成**：对每个插补完成的数据集分别拟合 eCDF-copula 模型并生成合成数据。
  3. **方差分解**：通过比较同一方法在不同插补数据集上生成的合成数据之间的差异，对**复制变异性**（replication variability）进行量化分解——即区分“插补导致的不确定性”与“合成过程本身的随机性”。
- **算法流程（文字说明）**：
  ① 输入原始纵向数据（含缺失）→ ② 执行多重插补（m 次）获得 m 个完整数据集 → ③ 对每个完整数据集估计边际 eCDF 及 copula 参数 → ④ 从拟合的 copula 中抽样并逆变换生成合成数据 → ⑤ 汇总多次插补/合成的结果，计算效用、相似性、隐私及变异性的评估指标。
- **注意**：论文摘要未提供具体公式符号（如 copula 类型、参数估计方法），但核心思路明确：eCDF 保证单变量分布的保真度，copula 保证多变量/时序依赖的保真度。

## 3. 实验设计：数据集 / 场景 / benchmark / 对比方法

- **数据集**：两个**纵向临床数据集**，样本量差异显著：
  - **小型数据集**：n = 120（受试者数量），样本量较小，更易产生过拟合。
  - **大型数据集**：n = 3,612，样本量较大，可检验方法的可扩展性。
- **Benchmark / 评估维度**：
  - **相似性（Resemblance）**：合成数据与原始数据的分布/依赖结构相似程度。
  - **实用性（Utility）**：在合成数据上训练模型后，在真实测试数据上的表现（或等效的下游任务效度）。
  - **隐私性（Privacy）**：合成数据对原始数据受试者的隐私保护程度（如成员推理攻击抵抗能力、最近邻距离等）。
- **对比方法**：论文将 eCDF-copula 与**四种既有合成数据方法**进行了对比（摘要未列出具体方法名称，但按引言推断应包含至少一种 GAN 类方法与若干传统合成方法），涵盖了从基于统计到基于深度学习的代表性基线。

## 4. 资源与算力

- **论文明确说明情况**：摘要和元数据中**未提及任何 GPU 型号、数量、训练时长或计算资源的具体信息**。
- **推断**：由于 eCDF-copula 是统计方法（不涉及神经网络的反向传播或大规模矩阵迭代），其算力需求通常远低于 GAN 等深度生成模型，在普通 CPU 上即可运行。但论文未给出运行时间或硬件配置，属于信息缺失项。

## 5. 实验数量与充分性：是否充分、客观、公平

- **实验数量**：摘要显示共进行了两类数据集上的对比实验，并且每个数据集上均评估了相似性、实用性和隐私性三个维度。属于较全面的基础评估。
- **充分性评价**：
  - **充分之处**：两个数据集覆盖了“小样本”和“中等样本”两种常见临床场景，且对比了四种方法，评估维度多维，具有一定的说服力。
  - **不足之处**：摘要中未见明确的**消融实验**（如单独验证 eCDF 或 copula 的贡献）、未见对**缺失比例/缺失机制**的系统性变化分析、未见对**copula 类型/超参数敏感性**的分析。此外，对比的四种方法名称未列出，削弱了读者对公平性的直接判断能力。
  - **公平性**：在未列出具体基线参数调优细节的前提下，无法完全确认是否各基线均处于最优状态，但采用“四个基线 + 两数据集 + 三维度”的实验框架在主流提交中属于标准操作，整体客观性较好。

## 6. 论文的主要结论与发现

- **主要结论**：eCDF-copula 在两个规模迥异的纵向临床数据集上的**相似性（resemblance）和实用性（utility）均超过了四种最先进的合成数据方法**，同时保持了与基线**相当的隐私保护水平**。
- **附加发现**：
  - 提出的两阶段缺失数据处理策略（多重插补 + copula 合成）能够有效应对纵向数据中普遍的缺失值问题，并提供方差分解来量化复制变异性。
  - 统计基础的生成方法在中等规模临床数据上比 GAN 类方法更稳定、更可解释，且不牺牲隐私与效用。

## 7. 优点：方法或实验设计上的亮点

- **方法可解释性**：eCDF-copula 将边缘分布与依赖结构明确分离，依赖参数（copula）具有清晰的统计含义，克服了 GAN “黑箱”依赖结构的缺陷。
- **对纵向结构的显式建模**：通过 copula 自然捕获访问内（intra-visit）和访问间（between-visit）的依赖，这是许多现有方法忽略的关键特性。
- **稳健性**：在小样本（n=120）场景下表现出对过拟合的抵抗能力，优于以 GAN 为代表的深度方法。
- **科学的缺失数据处理**：将多重插补与合成结合并引入方差分解，提供了对不确定性的更完整刻画，而非简单丢弃或均值填充。
- **评估维度全面**：同时考察相似性、实用性、隐私性，三者缺一不可，有助于全面评价合成数据的实际可用性。

## 8. 不足与局限

- **实验覆盖有限**：仅有两个数据集，且均为临床纵向数据，未扩展到其他纵向领域（如金融、社交网络）；样本量最大为 3,612，未验证超高维/超大数据集上的表现。
- **基线信息不透明**：未在摘要中列出四种对比方法的具体名称，读者较难判断其是否包含最强基线（如最新的扩散模型或其他 SOTA 时序 GAN）。
- **缺失数据策略的边界未明确**：未说明多重插补次数 m 的敏感性、对高缺失率（如 >50%）的鲁棒性，以及 copula 结构对缺失机制（MCAR/MAR/MNAR）的假设敏感性。
- **依赖结构的表达范围**：copula 对复杂非线性、高阶交互或长时序依赖的建模能力弱于深度模型，论文未讨论这一理论边界。
- **可复现性信息缺失**：未提供代码链接、超参数设置、算力资源等，降低了对复现的友好程度。

（完）
