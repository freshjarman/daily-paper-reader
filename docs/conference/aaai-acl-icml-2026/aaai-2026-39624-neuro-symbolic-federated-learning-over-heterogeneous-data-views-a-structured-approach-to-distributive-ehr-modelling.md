---
title: "Neuro-Symbolic Federated Learning over Heterogeneous Data-Views: A Structured Approach to Distributive EHR Modelling"
title_zh: 异构数据视图上的神经符号联邦学习：面向分布式EHR建模的结构化方法
authors: "Soheila Molaei, Bahareh Fatemi, Anshul Thakur, Andrew Soltan, Fazle Rabbi, Andreas L. Opdahl, Kim Branson, Patrick Schwab, Danielle Belgrave, David A. Clifton"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39624/43585"
tags: ["query:ehr-es"]
score: 7.0
evidence: 面向分布式电子健康记录建模的神经符号联邦学习框架
tldr: 联邦学习可在分布式电子健康记录上实现隐私保护训练，但机构间数据视图异构导致难以部署，现有方法要么强求对齐而丢失特征，要么投影到共享隐空间而牺牲可解释性。本文提出从向量化输入转向符号化、关系中心的建模范式，将每个客户的EHR组织为结构化类型感知关系图进行神经符号建模。方法在保留可解释性的同时支持异构EHR协同建模，为分布式临床数据学习提供了新思路。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 联邦学习受限于机构间EHR数据视图异构，现有对齐或投影方法或丢失特征或牺牲可解释性。
method: 提出符号化、关系中心的神经符号联邦框架，将每个客户EHR组织为类型感知的关系图。
result: 方法在保留可解释性的同时支持异构EHR的协同建模。
conclusion: 关系中心的神经符号建模为分布式EHR学习提供了兼顾隐私与解释的途径。
---

## Abstract
Federated learning (FL) enables privacy-preserving model training across distributed Electronic Health Records (EHRs), but its deployment remains limited by data-view heterogeneity, where institutions maintain incompatible local schemas. Most existing methods address this by enforcing flat, aligned data views, which require extensive cross-site preprocessing and manual harmonisation that often discards client-specific features, or by projecting inputs into a shared latent space, which sacrifices interpretability. We propose a modelling shift from conventional FL with vectorised inputs to a symbolic, relation-centric framework, where each client organises its EHR data as a structured, type-aware relational graph. This enables client-specific inference without requiring schema alignment and supports FL across heterogeneous data views. To model over these symbolic structures, we introduce an architecture that combines relation-aware message passing with a learnable feature relevance mechanism, jointly enabling accurate local predictions and client-specific interpretability while supporting parameter sharing across clients. Beyond strong performance on three real-world EHR datasets exhibiting data-view heterogeneity, we further show that our framework supports multimodal FL under modality-level heterogeneity. Using MC-MED, a publicly available multimodal emergency department dataset, we demonstrate that our method accommodates clients with partially missing modalities, highlighting its robustness and scalability in real-world clinical settings.

---

## 论文详细总结（自动生成）

# 论文总结：异构数据视图上的神经符号联邦学习

## 1. 核心问题与整体含义

- **研究背景**：电子健康记录（EHR）蕴含丰富临床信息，但因隐私法规和数据治理限制，数据通常分散在各机构，难以集中训练。联邦学习（FL）可在数据不出本地的前提下协同训练模型，是临床 AI 的重要路径。
- **核心问题**：临床 FL 面临显著的 **数据视图异构性（data-view heterogeneity）**，即不同机构的本地 schema、可用特征、编码标准、测量单位等不一致，导致输入空间不兼容。
- **现有方法局限**：
  - 手动对齐特征空间：需大量跨站点预处理，且常丢弃部分站点独有特征，造成信息损失。
  - 投影到共享隐空间：虽可绕过 schema 对齐，但牺牲可解释性，且本地表示可能不一致。
  - 插补/数据增强：可能引入人工噪声，扭曲临床信号。
- **论文含义**：作者主张从“向量化输入”的 FL 转向“符号化、关系中心”的建模框架，将每个客户端的 EHR 表示为结构化、类型感知的关系图，在共享本体下实现异构数据视图乃至模态级异构下的联邦学习，并保留客户端级可解释性。

## 2. 方法论

### 核心思想

- 每个客户端将本地 EHR 数据组织为异质知识图 \(G_k=(V_k,E_k)\)。
- 节点分为患者节点和临床特征节点；边为类型化语义关系。
- 所有客户端共享同一套实体/关系本体，但各自图拓扑可因本地数据不同而不同，从而无需 schema 对齐。
- 在图上使用关系感知消息传递与可学习特征相关性机制，实现本地预测、联邦参数共享和客户端特定解释。

### 关键细节

- **符号化数据建模**：
  - 患者节点初始表示：随机向量 \(\epsilon_p \sim N(0,I)\)。
  - 特征节点初始表示：\(h^{(0)}_{v_f}=m_f \cdot \text{Emb}(f)\)，其中 \(m_f\in[0,1]\) 为可学习标量掩码，\(\text{Emb}(f)\) 来自共享嵌入表。
  - 三类核心关系：
    - `has feature`：患者具有某特征，边权对应观测值。
    - `of patient`：反向边，支持双向信息流。
    - `similar to`：基于 kNN 连接相似患者，边权反映相似度。
- **关系感知图处理**：
  - 使用两层异质图神经网络，结合异质注意力机制。
  - 每层对节点 \(u\) 按关系类型 \(r\) 聚合邻居信息，并使用关系特定变换矩阵 \(W^{(r)}\)。
  - 注意力权重通过 LeakyReLU 和 softmax 计算，衡量关系类型与具体边的重要性。
  - 患者节点最终嵌入经线性层和 sigmoid 输出预测。
- **特征级可解释性**：
  - 特征掩码 \(m_f\) 在训练中优化，反映该特征在本地预测中的重要性。
  - 推理时可作为显著性图，提供客户端特定解释，无需事后解释方法。
- **时间序列扩展**：
  - 将每个时间步视为一个快照，形成符号图序列，以捕捉时间动态。
- **联邦训练协议**：
  - 采用 FedSGD。
  - 服务器初始化全局模型参数 \(\theta\) 和全局特征字典 \(F\)，为每个临床特征名分配唯一索引。
  - 每轮服务器下发 \(\theta^{(t)}\)；客户端本地训练多个 epoch，计算梯度更新 \(\Delta\theta_k=\theta^{(t)}-\theta'_k\)。
  - 服务器按客户端样本量加权聚合并更新全局模型。
- **理论分析**：
  - 定理 1：schema 不变性。对未观测特征添加孤立节点不改变前向预测和梯度，未观测特征梯度为 0。
  - 定理 2：在关系型数据生成过程下，符号图预测器的总体风险不高于扁平向量化模型。
  - 定理 3：特征掩码作为信息瓶颈，给出基于互信息的泛化误差界。

## 3. 实验设计

### 数据集与场景

- **CURIAL 数据集集合**：来自四个不同 NHS Trusts，各自作为联邦客户端，包含生命体征和血液检测结果，用于 COVID-19 预测。
- **eICU**：多中心 ICU 数据库，选取前 50 家医院模拟联邦客户端，用于 4 小时休克预测，使用时间序列数据。
- **MIMIC-III**：模拟 15 个具有异构数据 schema 的客户端，用于 48 小时 ICU 死亡率预测。
- **MC-MED**：公开多模态急诊数据集，划分为 3 个客户端，模态可用性不同，用于早期卒中预测：
  - Client 1：静态特征、生命体征时间序列、PPG 波形。
  - Client 2：缺少 PPG。
  - Client 3：仅有静态特征。
- 对于 MC-MED，数据视图异构是固有的；其余数据集通过随机丢弃部分客户端特征来模拟异构。

### Benchmark 与对比方法

- **评价指标**：AUROC 和 AUPRC，按客户端平均，重复 5 次并报告标准差。
- **评价场景**：
  - Standard：传统 FL 场景，特征空间对齐。
  - Data-view Heterogeneity：客户端拥有不同本地特征，测试无需手动协调的能力。
- **对比方法**：
  - Standalone DNN：各客户端独立训练，非协同参考。
  - FedAvg：手动对齐特征子集。
  - Hypernet、LG-FedAvg、AGAT、Knowledge Filtering：处理异构性的联邦方法。
  - 提出的 Neuro-Symbolic FL。

### 主要实验结果

- 在 CURIAL、eICU、MIMIC-III 上，提出方法在 Standard 场景中略优于基线；在 Data-View Heterogeneity 场景中保持接近 Standard 的性能。
- FedAvg 在异构场景中性能明显下降，甚至低于 standalone，说明手动对齐造成特征损失。
- 相比最强基线 Knowledge Filtering：
  - CURIAL：AUROC +1.5%，AUPRC +2.1%。
  - eICU：AUROC +5.0%，AUPRC +22.4%。
  - MIMIC-III：AUROC +1.2%，AUPRC +9.5%。
- MC-MED 模态异构下：
  - 平均 AUROC：提出方法 0.795，Knowledge Filtering 0.704，FedAvg 0.700。
  - 平均 AUPRC：提出方法 0.030，多数基线约 0.011–0.012。
  - 模态更少的客户端提升更明显：Client 2 AUROC 提升约 0.18，Client 3 提升约 0.09。
- 可解释性分析：CURIAL 上，氧输送装置、白细胞计数等特征在多个站点被一致识别为重要；不同客户端也呈现不同特征重要性模式，如 UHB 更重视碱性磷酸酶、氧饱和度和血细胞比容。
- 消融实验：比较提出方法、非可学习符号变体、同质图基线。提出方法在所有客户端 AUROC 最高；去除可学习特征相关性和关系权重会下降；同质图下降最大，说明保留符号异质性关键。

## 4. 资源与算力

- 论文中 **未明确说明** 使用的 GPU 型号、数量、训练时长、显存、能耗或具体算力资源。
- 也未报告训练轮数、超参数搜索范围、模型参数量等工程细节。
- 因此无法从论文中评估其计算成本、复现难度或实际部署资源需求。

## 5. 实验数量与充分性

- **实验规模**：
  - 4 个数据集/数据集集合：CURIAL、eICU、MIMIC-III、MC-MED。
  - 其中 CURIAL 含 4 个 NHS Trust 客户端；eICU 模拟 50 个客户端；MIMIC-III 模拟 15 个客户端；MC-MED 为 3 个模态异构客户端。
  - 2 个联邦评价场景：Standard 与 Data-view Heterogeneity。
  - 7 类方法对比：Standalone、FedAvg、Hypernet、LG-FedAvg、AGAT、Knowledge Filtering、Proposed。
  - 5 次重复运行并报告标准差。
  - 1 组图构造消融实验，覆盖 3 种图策略。
  - 1 组特征级可解释性案例。
- **充分性评价**：
  - 覆盖了特征视图异构、模态级异构、时间序列、多个真实/公开临床数据集，实验设计较系统。
  - 但部分异构场景是通过随机丢弃特征模拟的，可能无法完全反映真实机构间 schema 差异。
  - MC-MED 的 AUPRC 整体较低，反映严重类别不平衡
