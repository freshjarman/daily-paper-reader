---
title: "Data integration with uneven spatiotemporal coverage: A point-process approach for dynamic species distribution models"
title_zh: 时空覆盖不均匀的数据集成：一种用于动态物种分布模型的点过程方法
authors: "Klaassen, M., Fernandez, M., Lindgren, F., Morera-Pujol, V., Thomas, L., Oliveira, N., Castro, J., Martinho, F., Magalhaes, S., Rodrigues, A., Martins, M., Alves, F., Marques, T. A."
date: 2026-06-29
pdf: "https://www.biorxiv.org/content/10.1101/2025.11.07.687170v3.full.pdf"
tags: ["query:tpp-es"]
score: 9.0
evidence: 点过程方法用于时空物种分布模型
tldr: "物种分布建模常面临数据时空覆盖不均的问题：设计调查时间短但空间结构好，公民科学数据时间频繁但空间偏差大。本文提出基于对数高斯Cox过程和集成嵌套拉普拉斯近似的多源数据集成框架，通过源特定观测模型（检测函数和空间约束）统一不同数据。模拟显示集成模型恢复分布模式中位数相关达0.91，月丰度平均误差+10.7%，显著优于单源模型；案例研究提升空间精度。该框架在数据互补时最能提升预测能力，可推广至其他物种和数据组合。"
source: biorxiv
selection_source: fresh_fetch
motivation: 解决设计调查与公民科学数据时空覆盖不均导致的模型局限性，融合两种数据优势以改进动态物种分布预测。
method: 基于对数高斯Cox过程和INLA构建框架，为调查数据设计检测函数，为机会数据添加空间约束，共享时空强度场。
result: "模拟中集成模型分布恢复相关中位数0.91，月丰度平均误差+10.7%；案例研究提升空间精度，但时间变化受弱协变量限制。"
conclusion: 当两种数据分别解决空间和时间维度时，集成价值最大；框架通用可扩展至其他分类群和数据组合。
---

## 摘要
物种分布模型（SDMs）被广泛用于预测物种出现的地点和时间，但用于拟合模型的数据往往在空间和时间上分辨率不均。设计性调查，如样线-距离采样调查，提供了结构化的空间覆盖和估计可探测性所需的检测信息，但后勤和资金限制通常使其局限于短期、不频繁的时段。机会性记录或公民科学记录在全年中更频繁地收集，但来自受观察者可达性和兴趣影响的区域，而非调查设计，且通常缺乏可比较的检测信息。因此，仅基于单一数据源构建的模型往往能很好地捕捉空间结构或时间动态，但不能同时兼顾，限制了动态环境中移动物种的预测。本文提出了一个基于对数高斯Cox过程（LGCP）的通用框架，通过集成嵌套拉普拉斯近似（INLA）进行拟合，该框架通过特定于数据源的观测模型将多个数据源与共享的物种密度时空度量联系起来：调查样线的探测函数，以及反映机会性努力足迹的空间约束。我们将该框架应用于鲸类样线调查和观鲸记录。在模拟中，使用一个月的调查数据和十二个月的机会性数据，集成模型很好地恢复了时空分布模式（与真实模式的中位相关系数为0.91），并以平均误差+10.7%估计了月度丰度，优于单源模型。在葡萄牙近海普通海豚（Delphinus delphis）的案例研究中，集成提高了预测的空间准确性，尽管较弱的协变量效应限制了模型能够解析的时间变化。这些结果表明，当两个数据源解析分布的互补方面时（例如，调查提供的广泛空间结构和观鲸提供的时间重复），集成带来的价值最大，而当协变量携带的季度信号较弱时，时间预测仍然有限。该框架具有通用性，可通过替换相关的观测模型扩展到其他分类群、系统以及结构化和机会性数据的组合。

## Abstract
Species distribution models (SDMs) are widely used to predict where and when species occur, but the data available to fit them often resolve space and time unevenly. Designed surveys, such as line-transect distance-sampling surveys, provide structured spatial coverage and the detection information needed to estimate detectability, but logistical and funding constraints often limit them to short, infrequent periods. Opportunistic or citizen-science records are collected more frequently across the year, but from areas shaped by observer access and interest rather than survey design, and usually without comparable detection information. As a result, models built from either source alone tend to capture spatial structure or temporal dynamics well, but not both, limiting predictions for mobile species in dynamic environments. Here, we present a general framework, based on a log-Gaussian Cox process (LGCP) fitted using integrated nested Laplace approximations (INLA), that links multiple data sources to a shared spatiotemporal measure of species density through source-specific observation models: a detection function for survey transects, and spatial constraints reflecting the footprint of opportunistic effort. We apply the framework to cetacean line-transect surveys and whale-watching records. In a simulation with one month of survey data and twelve months of opportunistic data, the integrated model recovered spatiotemporal distribution patterns well (median correlation with the true pattern = 0.91) and estimated monthly abundance with a mean error of +10.7%, outperforming single-source models. In a case study of common dolphins (Delphinus delphis) off mainland Portugal, integration improved the spatial accuracy of predictions, although weak covariate effects limited the temporal variation the model could resolve. These results show that integration adds the most value when the two data sources resolve complementary aspects of distribution, in this case broad spatial structure from the survey and temporal replication from whale-watching, while temporal predictions remain limited when covariates carry weak seasonal signal. The framework is general and can be extended to other taxa, systems, and combinations of structured and opportunistic data by substituting the relevant observation models.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **问题**：物种分布模型（SDMs）广泛用于预测物种出现的地点和时间，但用于拟合模型的数据往往在空间和时间分辨率上不均衡。设计性调查（如样线-距离采样调查）提供结构化空间覆盖和可检测性信息，但受限于短期、不频繁的时段；机会性记录（如公民科学数据）全年频率高，但空间分布受观察者可达性和兴趣影响，且缺乏检测信息。因此，单一数据源模型要么很好地捕捉空间结构，要么捕捉时间动态，但不能两者兼顾，限制了在动态环境中对移动物种的预测能力。
- **含义**：需要一种通用的数据集成框架，将不同时空覆盖特征的数据结合起来，同时利用各自的优势，以改进动态物种分布的预测。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：基于对数高斯Cox过程（Log-Gaussian Cox Process, LGCP），通过集成嵌套拉普拉斯近似（INLA）进行拟合。该框架通过**数据源特定的观测模型**将多个数据源与一个共享的物种密度时空度量联系起来。对于调查样线，使用**检测函数**（detection function）校正探测概率；对于机会性记录，使用**空间约束**（spatial constraints）反映机会性努力的空间足迹。
- **关键技术细节**：
  - 共享的时空强度场（intensity field）用对数高斯过程建模，分解为空间场、时间效应和协变量效应。
  - 调查数据用距离采样（distance sampling）的检测函数描述观测过程，将样线搜索中的探测概率与距离、环境变量等关联。
  - 机会性数据用泊松点过程模型，但添加空间约束（如基于“机会性努力足迹”的偏移量），以反映观测者更容易到达的区域（如海岸线、观鲸热点）。
  - 使用INLA进行贝叶斯推断，该框架可替换不同的观测模型以扩展到其他分类群和数据组合。
- **算法流程**（文字描述）：
  1. 定义共享的物种密度时空强度 λ(s,t)。
  2. 对调查数据：似然函数基于距离采样检测函数，即观测到的个体数量 = 真实数量 × 检测概率（与距离、协变量有关）。
  3. 对机会性数据：似然函数为泊松点过程，其强度为 λ(s,t) × 偏移量（反映机会性努力的空间分布）。
  4. 两个似然函数相乘得到联合似然，对共享的潜场和协变量参数进行先验设定。
  5. 使用INLA进行近似贝叶斯推断，获得后验分布。
  6. 预测时空密度和丰度。

## 3. 实验设计：使用了哪些数据集/场景、benchmark、对比方法

- **模拟实验**：
  - 模拟一个具有真实时空分布的“物种”，产生一个月的设计调查数据（模拟样线）和十二个月的机会性数据（模拟观鲸记录，空间偏向海岸线）。
  - 对比方法：①仅使用调查数据的单一源模型；②仅使用机会性数据的单一源模型；③集成模型。
  - benchmark：恢复的时空分布与真实分布之间的相关系数（中位数0.91），以及月度丰度估计的平均误差（+10.7%）。
- **案例研究**：
  - 葡萄牙近海普通海豚（*Delphinus delphis*）的真实数据：来自鲸类样线设计调查和观鲸记录（机会性数据）。
  - 评估集成模型与单一源模型在空间预测精度上的差异。
  - 由于较弱的环境协变量效应（如海表温度季度信号弱），时间预测能力受限。

## 4. 资源与算力

- 论文中**未明确说明**所使用的GPU型号、数量或训练时长。根据方法（INLA拟合LGCP），通常这类贝叶斯空间模型在CPU上完成，不需要大规模GPU。故算力需求较低，属于传统统计计算范畴。

## 5. 实验数量与充分性

- **模拟实验**：1组（一个模拟场景），但详细报告了中位数相关系数和月度丰度误差。未提及多次重复或敏感性分析。
- **案例研究**：1组（普通海豚真实数据）。无消融实验（如改变数据比例、调整检测函数形式等）。
- **充分性评价**：实验数量较少，仅一个模拟和一个案例，未进行交叉验证或多次模拟重复。虽然结果积极，但缺乏统计稳健性验证（如置信区间、重抽样）。优点在于模拟和真实案例均对比了单源模型，展示了集成优势。总体而言，实验设计**不够充分**，但作为方法学论文，核心在于提出框架而非全面验证。

## 6. 论文的主要结论与发现

- **集成模型优于单源模型**：模拟中集成模型恢复时空分布的中位相关系数为0.91，月度丰度平均误差+10.7%；而单一调查模型因只覆盖一个月，无法反映季节变化；单一机会性模型空间偏差大。
- **集成价值在数据互补时最大**：当设计调查提供广泛空间结构，机会性数据提供时间重复性时，集成效果最佳。
- **时间预测受限于协变量**：案例研究中，由于环境协变量（如海表温度）携带的季度信号较弱，集成模型仍难以解析复杂的时间动态，说明仅靠数据集成并不能完全弥补协变量不足。
- **框架通用可扩展**：通过替换观测模型（如不同检测函数、不同的机会性努力约束），可应用于其他分类群和数据组合。

## 7. 优点：方法或实验设计上的亮点

- **方法创新**：将LGCP和INLA用于多源数据集成，统一处理不同观测偏差（检测概率和空间偏移），在生态学领域具有新颖性。
- **实用性强**：针对常见的“调查短而精，机会性长而偏”的生态数据困境，提供了可落地的解决方案。
- **贝叶斯框架**：提供不确定性量化（INLA近似后验），预测结果有置信区间。
- **模块化设计**：可灵活替换源特定的观测模型，易于推广。

## 8. 不足与局限

- **实验覆盖不足**：仅一个模拟和一个案例，未进行多物种、多区域或不同偏差模式的测试，缺乏消融实验和敏感性分析。
- **模拟设计简单**：模拟中机会性数据的空间偏差仅考虑了海岸线约束，未模拟更复杂的偏差模式（如观测者兴趣热点、地形影响）。
- **时间预测能力受限**：论文坦言当协变量信号弱时，集成也无法显著提升时间预测，说明框架依赖高质量协变量。
- **未评估计算效率**：未提供模型拟合时间、内存消耗等指标。
- **适用性假设**：机会性数据的空间约束需要预先估计（如通过历史观察者努力数据），这在实际应用中可能不容易获得，或引入额外误差。
- **未处理零膨胀或过分散**：机会性数据常存在过分散，模型仅用泊松过程可能不够鲁棒；未考虑观测者水平效应。

（完）
