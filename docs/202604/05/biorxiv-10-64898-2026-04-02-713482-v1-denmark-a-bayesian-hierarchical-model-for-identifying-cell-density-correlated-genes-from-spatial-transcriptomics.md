---
title: "DenMark: A Bayesian Hierarchical Model for Identifying Cell-Density Correlated Genes from Spatial Transcriptomics"
title_zh: DenMark：一种用于从空间转录组学中识别细胞密度相关基因的贝叶斯层次模型
authors: "Xu, M., Schmidt, A., Zhang, Q."
date: 2026-04-04
pdf: "https://www.biorxiv.org/content/10.64898/2026.04.02.713482v1.full.pdf"
tags: ["query:tpp-es"]
score: 9.0
evidence: 用于空间转录组学的密度依赖标记点过程框架
tldr: 单细胞分辨率空间转录组技术能保留细胞位置信息，但缺乏量化局部细胞密度与基因表达相关性的计算框架。为此，本研究提出了 DenMark（一种基于贝叶斯分层模型的密度依赖性标记点过程框架），它能联合建模细胞位置和基因表达，通过高效推断识别密度相关基因并提供不确定性量化。该模型在模拟和多种真实数据平台上验证有效，揭示了与组织微环境相关的生物学程序。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-04-02-713482-v1/fig-001.webp\", \"caption\": \"Table 1. Model comparison between DenMark and a nested setting.\", \"page\": 21, \"index\": 1, \"width\": 1002, \"height\": 917}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-04-02-713482-v1/fig-002.webp\", \"caption\": \"Figure 2. Results of the simulation studies. (A) Simulated cell counts and average gene expression per grid on 22 × 22 grids for an exemplary simulated dataset. (B) Spatial correlation functions of the latent spatial fields of cell density and gene expression, illustrating the decay of spatial correlation with increasing cell-cell distance (0 mm to the maximum observed distance). Black solid line, posterior mean; grey shaded region, 95% credible interval; red line, true correlation function. The horizontal dashed line (0.05) denotes a practical threshold below which correlation is considered negligible. (C) Comparison of the exact Gaussian process (GP) and Hilbert space Gaussian process (HSGP) approximations with different numbers of basis functions (2 × 2, 5 × 5, 10 × 10, and 25 × 25 over the two-dimensional spatial domain), together with corresponding computational time. (D) Comparison of exact GP and HSGP under varying boundary expansion factors (1.02, 1.05, and 1.5 applied to two spatial directions), with corresponding computational time. (E) Simulated marked point process (left), corresponding binned cell counts (middle), and average of gene expression per bin (right). (F) Estimation bias between fitted grid-level and simulated cell-level log-intensity surface across predefined grid resolutions (20×20, 30 × 30, 40 × 40 and 50 × 50).\", \"page\": 13, \"index\": 2, \"width\": 1025, \"height\": 515}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-04-02-713482-v1/fig-003.webp\", \"caption\": \"Figure 1. Workflow of DenMark. (A) Conceptual visualization of density-correlated genes. In regions of higher cell density, positively density-correlated genes show increased expression (upper panel), whereas negatively density-correlated genes show decreased expression (lower panel). (B) Data preparation: For each candidate gene, DenMark extracts cell location (point pattern) and cell-level gene expression measurements (gene expression pattern) from single-cell resolution ST data. These two spatial patterns are then discretized onto a set of predefined grids. (C) DenMark framework: The discretized grid-level cell counts and expression are fitted by the marked point process, facilitated by a low-rank approximation to enhance computation efficiency. (D) Output: For each gene, DenMark provides (1) posterior summaries of correlation between cell density and gene expression per cell; (2) the visualization of the latent field decomposition, where the gene-expression intensity is expressed as the weighted sum of a) a shared spatial component driven by the same latent field of cell density, and b) a residual component that reflects gene-specific spatial structure beyond what cell density accounts for; and (3) spatial correlation functions describing how correlations in cell density (or gene expression) decrease as a function of intercellular distance.\", \"page\": 12, \"index\": 3, \"width\": 913, \"height\": 705}]"
motivation: 当前缺乏严谨的计算框架来量化单细胞分辨率空间转录组数据中局部细胞密度与基因表达之间的相关性。
method: 该方法名为 DenMark，是一个贝叶斯分层模型，它联合建模局部细胞位置和基因表达数据，并利用希尔伯特空间高斯过程近似进行高效推断。
result: 在模拟和真实数据（如 MERFISH、10x Xenium）中，DenMark 能准确识别与细胞聚集相关的基因，并在脑组织和癌组织中揭示了与密度相关的生物学程序。
conclusion: DenMark 是一个强大的统计框架，能够从单细胞分辨率空间转录组数据中识别与细胞密度相关的基因，并揭示其背后的生物学程序。
---

## 摘要
单细胞分辨率空间转录组学的最新进展使得在保留单个细胞精确位置的同时分析基因表达成为可能，从而能够定量研究细胞组织结构如何与分子状态相关联。组织结构中一个基本但尚未被充分建模的方面是局部细胞密度，它在不同微环境中存在差异，并且可能与转录程序相关。然而，目前仍缺乏严谨的计算框架来量化密度与表达之间的相关性。为此，我们提出了DenMark（密度依赖性标记点过程框架），这是一个统一的统计框架，能够联合建模单细胞分辨率空间转录组数据中的局部细胞位置和基因表达，从而在识别密度相关基因的同时自然地提供不确定性量化。为了扩展推理规模，DenMark利用了希尔伯特空间高斯过程近似方法。在模拟实验中，DenMark提供了准确且校准良好的密度-表达关联估计。在包括MERFISH和10x Xenium在内的多种单细胞空间转录组平台以及脑组织和癌组织中，DenMark识别出了其表达与细胞聚类相关的基因，并揭示了与密度相关的生物学程序。

## Abstract
Recent advances in single-cell-resolution spatial transcriptomics enable the profiling of gene expression while preserving the precise locations of individual cells, enabling quantitative investigation of how cellular organization relates to molecular state. A fundamental yet under-modeled aspect of organization is local cell density, which varies across microenvironments and can be linked to transcriptional programs. However, rigorous computational frameworks to quantify density-expression correlations remain lacking. Here, we present DenMark (Density-dependent Marked point process framework), a unified statistical framework that jointly models local cell locations and gene expression in single-cell-resolution ST data, enabling identification of density-correlated genes while naturally providing uncertainty quantification. To scale inference, DenMark leverages a Hilbert space Gaussian process approximation. In simulations, DenMark provides an accurate and well-calibrated estimate of density-expression association. Across single-cell ST platforms, including MERFISH and 10x Xenium, and across brain and cancer tissues, DenMark identifies genes whose expression is associated with cellular clustering and reveals density-related biological programs.

---

## 论文详细总结（自动生成）

# DenMark 论文分析总结

## 1. 核心问题与整体含义
*   **研究动机与背景**：
    *   **技术背景**：单细胞分辨率空间转录组学（ST）技术（如 MERFISH、10x Xenium）的发展，使得在保留细胞精确空间位置的同时测量其基因表达成为可能。
    *   **科学问题**：组织的空间结构（如局部细胞密度）如何影响或关联细胞的分子状态（基因表达），是一个基础但未被充分建模的生物学问题。局部细胞密度在不同组织微环境中存在差异，可能与特定的转录程序相关。
    *   **方法学缺口**：尽管数据已具备，但当前缺乏一个严谨、统一的统计计算框架来量化局部细胞密度与基因表达之间的相关性，并对此相关性进行可靠的统计推断和不确定性评估。

## 2. 提出的方法论
*   **核心思想**：提出 **DenMark**（Density-dependent Marked point process framework），一个贝叶斯分层模型框架。它将每个细胞的“位置”（点过程）和“基因表达值”（标记）进行联合建模，从而直接推断细胞密度场与基因表达场之间的相关性。
*   **关键技术细节**：
    1.  **数据预处理与离散化**：将连续空间中的细胞位置和基因表达数据，离散化到预先定义的规则网格上。每个网格记录细胞计数（代表局部密度）和该网格内细胞的平均基因表达水平。
    2.  **分层建模结构**：
        *   底层是两个潜在的空间高斯过程随机场，分别驱动“细胞密度强度”和“基因表达强度”。
        *   模型的核心参数是这两个潜在场之间的相关系数 `ρ`。`ρ > 0` 表示正密度相关基因（高密度区高表达），`ρ < 0` 表示负密度相关基因（高密度区低表达）。
        *   观测到的网格级细胞计数和平均表达值被建模为这些潜在强度场的泊松分布和高斯分布的实现。
    3.  **高效推断与计算优化**：
        *   为了应对高斯过程在大规模空间数据上的计算瓶颈，DenMark采用了 **希尔伯特空间高斯过程近似方法**。该方法通过一组有限的基础函数来近似无限维的高斯过程，显著提升了计算效率。
        *   论文探讨了不同基础函数数量 (`m`) 和边界扩展因子对近似精度与计算时间的影响（见图2C, D）。
*   **输出结果**：对于每个候选基因，DenMark提供：
    *   密度-表达相关系数 `ρ` 的后验估计（均值、可信区间）。
    *   潜在场的可视化分解：将基因表达强度分解为“由细胞密度共享的组分”和“基因特异的残差空间组分”。
    *   空间相关函数：描述细胞密度或基因表达的空间自相关性如何随细胞间距离衰减。

## 3. 实验设计
*   **数据集/场景**：
    1.  **模拟数据**：用于验证方法的准确性和校准性。通过控制不同的空间相关结构和相关系数 `ρ` 来生成数据。
    2.  **真实数据**：
        *   **平台多样性验证**：使用了来自不同技术平台的数据，包括成像技术的 **MERFISH** (小鼠下丘脑) 和基于测序的 **10x Xenium** (人类乳腺癌)。
        *   **组织多样性验证**：涵盖了脑组织 (小鼠下丘脑) 和癌组织 (人类乳腺癌、人类胶质母细胞瘤)。
*   **Benchmark与对比方法**：
    *   DenMark将自己与其一个简化版本进行了比较。
    *   Table1展示了模型比较结果。从提供的元数据看，文中提到的是“Model comparison between DenMark and a nested setting”，这表明主要对比可能是在完整模型与其某个嵌套/简化设定之间进行，而非与其他独立的外部方法进行广泛对比。

## 4. 资源与算力
*   论文中未明确说明具体使用的硬件配置（如GPU型号、数量）、软件依赖的详细版本或模型训练/推断所需的具体时长。
*   ***总结***：文中未提供具体的算力消耗信息。

## 5. 实验数量与充分性
*   **实验组别概览**：
    1.  **模拟研究 (多组)**：系统测试了HSGP近似的精度-效率权衡、不同网格分辨率对估计偏差的影响、以及模型在不同预设 `ρ`值下的恢复能力和校准度。
    2.  **真实数据分析 (多数据集)**：在至少三个不同的真实数据集上应用DenMark，识别出正/负密度相关基因，并进行下游生物学通路分析。
*   **充分性与客观性评估**：
    *   ***优点***：
        1.  模拟实验设计系统，有效验证了方法的核心统计属性（无偏性、校准性）和计算方案的可行性。
        2.  在多个独立的技术平台和组织类型上验证了方法的适用性和稳健性。
        3.  对关键超参数进行了敏感性分析。
    *   ***局限性***：
        1.  缺乏与其他现有空间分析方法（如基于共定位分析、基于邻域图的方法等）的定量性能比较。这使得评估DenMark相对于现有方案的绝对优势较为困难。
        2. “对比方法”部分可能主要限于自身模型的变体，而非独立的基准方法。

##6 .主要结论与发现
*   DenMark是一个有效的贝叶斯框架，能够从单细胞分辨率ST数据中可靠地识别出与局部细胞密度显著相关的基因。
*   在模拟中，该方法能准确估计密度-表达相关性并提供良好校准的不确定性量化。
*   在真实组织中发现了具有生物学意义的密度相关基因。例如在小鼠下丘脑中鉴定出富集于特定神经元亚型的正相关基因；在乳腺癌中发现正相关基因富集于增殖和应激反应通路，而负相关基因则与免疫应答相关。

##7 .优点
1.	统一建模框架:创新性地将标记点过程引入ST数据分析,为联合建模空间位置(点)和分子表型(标记)提供了一个严谨的概率学基础.
2	不确定性量化:作为贝叶斯方法,天然地提供参数估计的后验分布,包括相关系数的可信区间,增强了结果的可解释性和可靠性.
3	可扩展性:通过集成希尔伯特空间高斯过程近似,解决了传统高斯过程在大规模空间数据分析中的计算难题,使方法适用于实际规模的ST数据集.
4	生物学洞察丰富:不仅输出相关性系数,还能分解潜在的空间场并可视化,有助于深入理解驱动表达的潜在因素.

##8 .不足与局限
1	方法对比不充分:如前所述,缺乏与其他主流或专门用于分析空间依赖性的方法的全面性能比较.
2	离散化依赖:模型依赖于将连续点模式离散化为网格,网格大小的选择可能影响结果(尽管论文分析了此影响).这本质上是一种信息损失.
3	模型假设限制:假设观测噪声服从特定的分布(泊松/高斯),且底层关联结构通过线性相关系数描述;对于更复杂的非线性关系或非标准噪声模式可能捕捉不足.
4	应用范围限制:目前主要应用于单细胞分辨率的ST数据;对于spot-based的低分辨率ST数据可能需要调整或无法直接应用.
5	计算复杂度依然较高:尽管采用了HSGP优化,但贝叶斯层次模型的推断相比一些简单启发式方法仍然更耗时.

(完)

## 9. 潜在影响与未来方向
*   **对领域的影响**：
    1.  **方法论贡献**：DenMark 为空间组学领域提供了一个新的、基于概率生成模型的“工具箱”。它将经典的标记点过程理论与现代计算技术（HSGP）相结合，为解决“空间结构如何影响分子表型”这一核心问题提供了标准化、可推断的解决方案。
    2.  **生物学发现引擎**：该方法能够系统性地扫描全基因组，识别出与组织结构（如细胞密度）共变的基因模块。这有助于发现新的空间调控模式，例如鉴定在肿瘤边缘（高免疫细胞密度）或肿瘤核心（高肿瘤细胞密度）特异性激活的基因程序。
    3.  **促进因果探索**：虽然 DenMark 本身是相关性分析工具，但其提供的严谨关联证据可以作为生成生物学假说的起点，引导后续的实验验证（如扰动局部密度观察基因表达变化），向因果推断迈出第一步。
*   **可能的未来工作**：
    1.  **模型扩展**：
        *   **多标记联合建模**：当前模型针对单个基因。未来可扩展至同时建模多个基因或整个基因模块的表达，以研究共调控网络。
        *   **非线性关联**：引入更灵活的非线性关联函数（如通过高斯过程先验）来捕捉复杂的密度-表达关系。
        *   **整合细胞类型信息**：在模型中显式纳入已知的细胞类型标签，以区分是细胞类型组成变化驱动的关联，还是同一细胞类型内真实的密度依赖性表达。
    2.  **计算优化**：进一步探索更高效的高斯过程近似方案或变分推断方法，以处理超大规模数据集（如全脑或整个器官尺度）。
    3.  **应用拓展**：
        *   应用于亚细胞分辨率数据，研究细胞内分子分布与局部胞内环境密度的关系。
        *   适应 spot-based ST 数据，此时“点”变为捕获点，“标记”为混合表达谱，需要不同的观测模型。

## 10. 总结评价
DenMark 是一篇方法学扎实、动机清晰的论文。它成功地识别并填补了单细胞空间转录组数据分析中的一个重要缺口——量化局部微环境结构（以细胞密度为代表）与基因表达之间关联的统计框架。其核心优势在于提供了一个统一、严谨且可计算贝叶斯框架，能够进行联合建模和不确定性量化。

尽管在实验部分缺乏与外部方法的广泛横向对比是一个明显的短板，可能影响对其性能优势的绝对评估，但论文通过系统的模拟验证和在多个异质真实数据集上的成功应用，充分证明了方法的有效性、稳健性和生物学实用性。它输出的不仅仅是相关性 p 值，而是包含空间场分解在内的丰富中间结果，为生物学家提供了更深层次的洞察工具。

总体而言，DenMark 是一项有价值的贡献，推动了空间组学数据分析从描述性统计向更具模型驱动和推断性的方向发展。它为后续开发更复杂的空间多模态数据分析模型奠定了良好的基础。

（完）
