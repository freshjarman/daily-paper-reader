---
title: "DenMark: A Bayesian Hierarchical Model for Identifying Cell-Density Correlated Genes from Spatial Transcriptomics"
title_zh: DenMark：一种用于从空间转录组学中识别细胞密度相关基因的贝叶斯分层模型
authors: "Xu, M., Schmidt, A., Zhang, Q."
date: 2026-04-04
pdf: "https://www.biorxiv.org/content/10.64898/2026.04.02.713482v1.full.pdf"
tags: ["query:tpp-es"]
score: 10.0
evidence: 密度依赖的标记点过程框架 (DenMark)
tldr: 本研究针对单细胞分辨率空间转录组数据，开发了DenMark贝叶斯分层模型，用于识别细胞密度相关基因。该框架通过联合建模细胞位置和基因表达，利用高斯过程近似实现高效推断，在模拟和MERFISH、10x Xenium等平台数据中验证了其准确性和生物学发现能力。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-04-02-713482-v1/fig-001.webp\", \"caption\": \"Table 1. Model comparison between DenMark and a nested setting.\", \"page\": 21, \"index\": 1, \"width\": 1002, \"height\": 917}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-04-02-713482-v1/fig-002.webp\", \"caption\": \"Figure 2. Results of the simulation studies. (A) Simulated cell counts and average gene expression per grid on 22 × 22 grids for an exemplary simulated dataset. (B) Spatial correlation functions of the latent spatial fields of cell density and gene expression, illustrating the decay of spatial correlation with increasing cell-cell distance (0 mm to the maximum observed distance). Black solid line, posterior mean; grey shaded region, 95% credible interval; red line, true correlation function. The horizontal dashed line (0.05) denotes a practical threshold below which correlation is considered negligible. (C) Comparison of the exact Gaussian process (GP) and Hilbert space Gaussian process (HSGP) approximations with different numbers of basis functions (2 × 2, 5 × 5, 10 × 10, and 25 × 25 over the two-dimensional spatial domain), together with corresponding computational time. (D) Comparison of exact GP and HSGP under varying boundary expansion factors (1.02, 1.05, and 1.5 applied to two spatial directions), with corresponding computational time. (E) Simulated marked point process (left), corresponding binned cell counts (middle), and average of gene expression per bin (right). (F) Estimation bias between fitted grid-level and simulated cell-level log-intensity surface across predefined grid resolutions (20×20, 30 × 30, 40 × 40 and 50 × 50).\", \"page\": 13, \"index\": 2, \"width\": 1025, \"height\": 515}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-04-02-713482-v1/fig-003.webp\", \"caption\": \"Figure 1. Workflow of DenMark. (A) Conceptual visualization of density-correlated genes. In regions of higher cell density, positively density-correlated genes show increased expression (upper panel), whereas negatively density-correlated genes show decreased expression (lower panel). (B) Data preparation: For each candidate gene, DenMark extracts cell location (point pattern) and cell-level gene expression measurements (gene expression pattern) from single-cell resolution ST data. These two spatial patterns are then discretized onto a set of predefined grids. (C) DenMark framework: The discretized grid-level cell counts and expression are fitted by the marked point process, facilitated by a low-rank approximation to enhance computation efficiency. (D) Output: For each gene, DenMark provides (1) posterior summaries of correlation between cell density and gene expression per cell; (2) the visualization of the latent field decomposition, where the gene-expression intensity is expressed as the weighted sum of a) a shared spatial component driven by the same latent field of cell density, and b) a residual component that reflects gene-specific spatial structure beyond what cell density accounts for; and (3) spatial correlation functions describing how correlations in cell density (or gene expression) decrease as a function of intercellular distance.\", \"page\": 12, \"index\": 3, \"width\": 913, \"height\": 705}]"
motivation: 现有方法缺乏量化细胞密度与基因表达关联的严谨计算框架。
method: 采用贝叶斯分层模型和希尔伯特空间高斯过程近似进行联合建模与推断。
result: 在模拟和真实数据中准确识别出与细胞密度相关的基因及生物学程序。
conclusion: DenMark为空间转录组学中细胞密度与基因表达关联的研究提供了可靠的计算框架。
---

## 摘要
单细胞分辨率空间转录组学的最新进展使得能够在保留单个细胞精确位置的同时分析基因表达，从而定量研究细胞组织如何与分子状态相关联。组织中一个基本但未被充分建模的方面是局部细胞密度，它在微环境中存在差异，并可能与转录程序相关联。然而，目前仍缺乏量化密度-表达相关性的严谨计算框架。在此，我们提出DenMark（密度依赖性标记点过程框架），这是一个统一的统计框架，可联合建模单细胞分辨率空间转录组数据中的局部细胞位置和基因表达，从而在识别密度相关基因的同时自然地提供不确定性量化。为了扩展推断规模，DenMark利用了希尔伯特空间高斯过程近似方法。在模拟中，DenMark能提供准确且校准良好的密度-表达关联估计。在包括MERFISH和10x Xenium在内的多种单细胞空间转录组平台以及脑组织和癌组织中，DenMark识别出那些表达与细胞聚类相关的基因，并揭示了与密度相关的生物学程序。

## Abstract
Recent advances in single-cell-resolution spatial transcriptomics enable the profiling of gene expression while preserving the precise locations of individual cells, enabling quantitative investigation of how cellular organization relates to molecular state. A fundamental yet under-modeled aspect of organization is local cell density, which varies across microenvironments and can be linked to transcriptional programs. However, rigorous computational frameworks to quantify density-expression correlations remain lacking. Here, we present DenMark (Density-dependent Marked point process framework), a unified statistical framework that jointly models local cell locations and gene expression in single-cell-resolution ST data, enabling identification of density-correlated genes while naturally providing uncertainty quantification. To scale inference, DenMark leverages a Hilbert space Gaussian process approximation. In simulations, DenMark provides an accurate and well-calibrated estimate of density-expression association. Across single-cell ST platforms, including MERFISH and 10x Xenium, and across brain and cancer tissues, DenMark identifies genes whose expression is associated with cellular clustering and reveals density-related biological programs.

---

## 论文详细总结（自动生成）

好的，作为一名资深学术论文分析助手，我将对您提供的论文《DenMark: A Bayesian Hierarchical Model for Identifying Cell-Density Correlated Genes from Spatial Transcriptomics》进行结构化、深入且客观的总结。

---

### **论文总结：DenMark**

#### **1. 核心问题与整体含义**
*   **研究动机**：单细胞分辨率空间转录组学（ST）技术的发展，使得在保留细胞空间位置的同时测量其基因表达成为可能。细胞的空间组织（尤其是局部细胞密度）是影响细胞状态和功能的关键因素，但现有计算工具主要关注识别“空间可变基因”（SVG），即表达在空间中异质的基因，而缺乏一个严谨的统计框架来量化“密度相关基因”（DCG），即其表达水平与局部细胞密度存在统计关联的基因。
*   **整体含义**：本研究旨在填补这一空白，提出了一个名为DenMark的统一贝叶斯分层模型。该模型能够从单细胞分辨率ST数据中**联合建模细胞位置（点模式）和基因表达（标记）**，从而直接、定量地推断密度-表达相关性，并提供不确定性度量。这有助于揭示组织微环境中由细胞聚集程度驱动的转录程序。

#### **2. 方法论**
*   **核心思想**：将单细胞ST数据视为一个**标记点过程**。将组织区域离散化为网格后，每个网格内的细胞计数和基因表达总量被建模为两个平滑变化的空间过程。
*   **关键技术细节**：
    1.  **贝叶斯分层模型**：
        *   **第一层（密度过程）**：网格`i`中的细胞计数 `N_i` 服从泊松分布，其强度 `λ_1(g_i)` 的对数由一个截距项和一个高斯过程 `ω_1(g_i)` 构成。
        *   **第二层（表达过程）**：给定 `N_i`，网格`i`中的总基因表达量 `M_i` 服从泊松分布，其每个细胞的平均表达强度 `λ_2(g_i)` 的对数被分解为两部分：
            *   一个与密度过程共享的组分：`a_21 * ω_1(g_i)`。
            *   一个基因特异性的组分：`a_22 * ω_2(g_i)`。
        *   参数 `a_21` 决定了共享组分的权重和方向（正/负相关），其标准化值 `|a_21| / sqrt(a_21^2 + a_22^2)` 即为密度-表达的相关系数 `ρ`。
    2.  **可扩展性优化 - HSGP**：由于模型涉及两个高斯过程，直接计算在大规模网格上成本高昂。因此，作者采用了**希尔伯特空间高斯过程近似**来降低计算复杂度，在精度和效率之间取得平衡。
    3.  **推断与输出**：使用哈密顿蒙特卡洛进行贝叶斯后验采样。输出包括：
        *   密度-表达相关系数 `ρ` 的后验分布及可信区间。
        *   潜在场的分解可视化（共享 vs. 特异性组分）。
        *   空间相关性函数图。

#### **3. 实验设计**
*   **模拟实验 (Benchmark)**：
    *   **目的1 - HSGP有效性验证**：比较精确高斯过程和不同基函数数量的HSGP近似在参数估计精度和计算时间上的表现。结果表明HSGP能以可接受的精度损失大幅提升效率。
    *   **目的2 - 网格化敏感性分析**：评估不同网格分辨率对模型性能的影响。结果显示更精细的网格能提高近似精度。
*   **真实数据应用与验证 (Case Studies)**：
    1.  **MERFISH小鼠脑数据集 (Vizgen)**：
        *   **场景/目标群体**:聚焦于星形胶质细胞。
        *   **验证**:分析了已知与迁移、疾病相关的候选基因（如Aqp4, Cxcl12），证实了它们与密度的正相关性。
        *   **发现**:在全基因组范围内识别了DCGs (如Gprc5b)，并通过GO富集分析发现这些基因富集于神经系统发育等通路。同时指出DCGs与SPARK-X识别的SVGs重叠有限 (<20%) ，说明两者捕捉了不同的生物学信号。
    2.  **10x Xenium人类乳腺癌数据集 (10x Genomics)**：
        *   **场景/目标群体**:分别分析了导管原位癌(DCIS)区域、浸润性肿瘤区域以及CD8+ T细胞的微环境及全切片水平。
        *   **发现**:识别了不同肿瘤微环境中特异的DCGs；揭示了肿瘤区与免疫区之间存在“拮抗性”的密度-表达特征；富集分析显示浸润性肿瘤区的DCGs与免疫/炎症反应通路相关。

#### **4. 资源与算力**
*   论文中未明确提及具体使用的硬件配置（如GPU型号、数量）、训练时长或算力消耗等细节。方法的实现基于RStan库进行MCMC采样。

#### **5. 实验数量与充分性**
*   实验设计较为充分和客观：
    1.  **(模拟)基准测试全面**:系统评估了方法的核心近似技术(HSGP)和关键预处理步骤(网格化)的性能边界和敏感性。
    2.  **(真实数据)覆盖多平台多组织**:在两个主流单细胞ST平台(MERFISH, Xenium)和两种重要组织类型(脑、癌)上进行了验证和应用，证明了方法的通用性。
    3.  **(对比)概念清晰**:虽然没有与其他专门针对“密度相关”的方法进行头对头比较(因为此类方法缺乏)，但通过将结果与传统SVG检测工具(SPARK-X)的结果进行比较，清晰地界定了DenMark所解决的新问题及其发现的独特性。
    4. **(生物学解释深入):不仅提供统计显著性列表(DCGs)，还通过富集分析和已知生物学知识对结果进行了深入解读。

#### **6.主要结论与发现**
*   成功开发了一个名为DenMark的可扩展贝叶斯框架，能够从单细胞ST数据中稳健地量化并识别密度相关基因(DCGs)。
*   模拟研究表明该方法能准确估计参数并提供校准良好的不确定性量化；HSGP近似实现了效率与精度的有效权衡。
*   在脑组织和乳腺癌组织中均发现了具有生物学意义的DCGs谱系:
    *   在小鼠脑中,星形胶质细胞的DCGs参与蛋白结合、神经系统发育等过程.
    *   在乳腺癌中,揭示了肿瘤微环境内不同区域(如DCIS vs浸润癌 vs免疫区)特异的以及相互拮抗的密度-表达模式.
* DCGs在很大程度上不同于传统的SVGs,表明这是一种新的、补充性的数据分析视角.

####7.**优点**
*   ***问题定义新颖且重要***:首次系统性地提出了从单细胞ST数据中量化“密度-表达相关性”这一具体且有生物学意义的问题.
* ***模型框架统一且严谨***:采用标记点过程和共区域化矩阵的贝叶斯分层建模,理论根基扎实,能自然地进行不确定性量化.
* ***兼顾灵活性与可扩展性***:通过引入HSGP近似,使复杂的空间模型能够应用于大规模高分辨率数据.
* ***实验验证全面***:从模拟到真实数据,从方法学验证到生物学发现,形成了一个完整的证据链.

####8.**不足与局限**
* ***建模假设的限制***:
    1.**空间不变的相关性矩阵**:模型中连接密度场和表达场的系数(`a_{21}`)在整个区域内是恒定的,这可能无法捕捉某些情况下随空间变化的关联强度.
    2.**单基因独立分析**:每次只对一个基因进行分析,忽略了基因间的相互作用或共变模式.
    3.**忽略跨切片信息**:目前仅处理单个组织切片的数据.
* ***应用层面的挑战***:
    1.**需要足够的样本量/事件数**:对于非常稀疏或数量极少的稀有细胞类型,模型的推断可能不稳定.
    2.**先验选择和超参数设置**(如HSGP基函数数量、边界因子等)需要用户根据数据和计算资源进行调整.
    3.**计算成本依然较高**:尽管使用了HSGP,MCMC采样对于包含成千上万个细胞的整个切片进行分析仍然耗时较长.

**(完)**

好的，我将从您提供的总结末尾继续，补充一些更深入的讨论和总结性内容。

---

#### **9. 潜在影响与未来方向**
*   **对空间生物学的影响**：DenMark 为分析细胞密度与基因表达之间的功能联系提供了一个新的、严谨的计算透镜。它超越了传统的空间异质性分析，直接探究细胞聚集这一关键组织特征如何塑造转录组，有助于揭示由细胞-细胞物理邻近性驱动的信号通路和调控网络。
*   **方法学上的贡献**：该研究展示了将标记点过程理论与现代贝叶斯计算工具（如HSGP）相结合以解决新兴生物信息学问题的可行性。它为处理其他类型的“标记”（如蛋白质表达、染色质可及性）与空间点模式的关系提供了可扩展的建模框架。
*   **未来工作方向**：
    1.  **模型扩展**：开发能够处理多基因、多切片或允许相关性系数随空间变化的更复杂模型。
    2.  **整合多模态数据**：将DenMark的框架扩展到整合成像形态学特征或邻近细胞的表型信息，以构建更全面的微环境模型。
    3.  **下游分析工具**：开发基于DenMark识别出的DCGs进行细胞亚群细分、空间功能模块识别或轨迹推断的配套分析方法。
    4.  **计算效率优化**：探索变分推断等更快的近似后验推断方法，以进一步提升模型在大规模数据集上的可及性。

#### **10. 总体评价**
《DenMark》是一篇方法学扎实、问题驱动明确且具有重要生物学意义的优秀论文。它精准地定位了当前单细胞空间转录组数据分析中的一个空白领域——即系统性地量化细胞密度与基因表达之间的统计关联。作者提出的贝叶斯分层模型不仅在理论上优雅统一了空间点模式与标记数据的建模，而且通过巧妙的近似技术（HSGP）使其具备了处理现实世界大规模数据的实用性。

尽管模型存在一些固有的假设限制（如全局恒定的相关性、单基因分析），但作者通过详尽的模拟和在不同生物学场景（神经科学、肿瘤免疫）中的应用，充分证明了其方法的有效性、稳健性和独特的生物学发现能力。该工作不仅为领域提供了一个强大的新工具（DenMark），更重要的是，它定义并推动了一个新的分析范式，鼓励研究者从“密度相关”而不仅仅是“空间可变”的角度去解读复杂的组织微环境。其实验设计严谨，结论可靠，对未来研究具有明确的启发性和指导价值。

（完）
