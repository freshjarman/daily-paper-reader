---
title: "MedCPI: A Construct–Personalize–Integrate Framework for KG-enhanced Clinical Prediction"
title_zh: MedCPI：面向知识图谱增强临床预测的构建-个性化-整合框架
authors: "Hang Wang, Hang Dong, Lu Liu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.findings-acl.1215.pdf"
tags: ["query:ehr-es"]
score: 7.0
evidence: 基于纵向EHR证据的知识图谱增强临床预测
tldr: 电子健康记录为临床预测提供纵向证据，但数据稀疏、不完整且异质，限制了模型鲁棒性，已有知识图谱增强方法在知识选择与患者级个性化整合上存在不足。本文提出MedCPI的构建-个性化-整合框架，将异构EHR编码链接到共享医学概念，实现任务相关知识选择与面向纵向患者轨迹的个性化知识整合。该框架提升了临床预测的鲁棒性与个体化水平，为知识增强的EHR建模提供了新思路。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1215/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 4606, \"height\": 2736}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1215/fig-002.webp\", \"caption\": \"\", \"page\": 8, \"index\": 2, \"width\": 1150, \"height\": 1063}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1215/fig-003.webp\", \"caption\": \"\", \"page\": 8, \"index\": 3, \"width\": 1150, \"height\": 1063}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1215/fig-004.webp\", \"caption\": \"\", \"page\": 8, \"index\": 4, \"width\": 1121, \"height\": 1142}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1215/fig-005.webp\", \"caption\": \"\", \"page\": 8, \"index\": 5, \"width\": 1121, \"height\": 1142}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1215/fig-006.webp\", \"caption\": \"\", \"page\": 12, \"index\": 6, \"width\": 2507, \"height\": 1090}]"
motivation: EHR数据稀疏、不完整且异质，已有知识图谱增强方法在知识选择与患者级个性化整合上存在局限。
method: 提出MedCPI框架，将异构EHR编码链接到医学知识图谱概念，进行任务相关知识选择与纵向轨迹对齐的个性化整合。
result: 方法实现了受控的个性化与轨迹对齐的知识融合，提升了临床预测的鲁棒性。
conclusion: 该工作为知识图谱增强的纵向EHR临床预测提供了有效的整合范式。
---

## Abstract
Electronic health records (EHRs) provide longitudinal evidence for clinical prediction, but EHR data are sparse, incomplete, and heterogeneous, which can limit robustness. Medical knowledge graphs (MKGs) have therefore been incorporated to support KG-enhanced clinical prediction by linking heterogeneous EHR codes to shared medical concepts via structured relations. However, existing KG-enhanced approaches remain limited in two aspects: (i) task-specific knowledge selection when extracting knowledge from a large multi-source MKG; and (ii) patient-level personalization and knowledge integration, where personalization is often weakly controlled and knowledge integration is not sufficiently aligned with longitudinal patient trajectories. To address these issues, we propose MedCPI, a unified Construct–Personalize–Integrate framework. MedCPI first performs task-guided schema induction and KG normalization to build a task-specific Concept MKG as a denoised knowledge pool, then constructs controlled patient-level PKGs via local expansion and short path search, and finally integrates PKG representations with time-aware EHR representations via cross-attention for prediction. Experiments on MIMIC-III and MIMIC-IV across four clinical prediction tasks show consistent improvements over strong EHR-only and KG-enhanced baselines. Ablations and additional analyses further validate the contribution of each stage and illustrate how MedCPI utilizes structured medical knowledge.

---

## 论文详细总结（自动生成）

# MedCPI 论文深度总结

## 1. 核心问题与整体含义（研究动机与背景）

- **背景**：电子健康记录（EHR）通过诊断、手术、用药等事件刻画患者纵向轨迹，为临床预测（如院内死亡、再入院、疾病发作）提供细粒度证据。但 EHR 数据本身**稀疏、不完整、异质**，导致模型鲁棒性与可靠性受限。
- **已有对策**：引入医学知识图谱（MKG），将异构 EHR 编码经结构化关系链接到共享医学概念，用先验知识平滑数据稀疏性，形成"KG 增强的临床预测"。该方向经历了三代演进：
  - 早期利用医学本体的层级（父子/祖先）关系；
  - 中期引入多关系 MKG + 图神经网络提供全局关系上下文（如 GAMENet、DKEC）；
  - 近期为每位患者构造个性化知识图谱（PKG）并做图推理（如 KerPrint、KGxDP、GraphCare）。
- **两大关键局限**（论文切入的问题）：
  - **(a) 从大型多源 MKG 中提取知识时缺乏任务特定选择**：多源图谱关系粒度不一、模式存在冗余与语义重叠，产生"模式级噪声"；已有方法缺少显式任务相关筛选，邻域扩展会**过度检索**弱相关节点/关系，稀释任务证据（如 T2DM 预测更依赖 `has_risk_factor`、`diagnosed_by`）。
  - **(b) 患者级个性化与知识整合不足**：PKG 常通过无约束邻域扩展或检索式拼装构造，**个性化控制弱**、易引入弱相关节点；知识整合与患者**纵向轨迹对齐不充分**，难以反映跨访视演变的病情。
- **整体含义**：论文提出统一的 **Construct–Personalize–Integrate（构建–个性化–整合）** 框架 MedCPI，把"任务引导的知识构建、患者级个性化、EHR–PKG 整合"纳入结构化流水线，为 KG 增强临床预测提供系统化范式。

## 2. 方法论：核心思想与关键技术细节

**核心思想**：先"净化"出一个任务相关、语义一致的知识池，再据此为每位患者构造受控的个性化图谱，最后用时间感知的交叉注意力把结构化知识与纵向 EHR 融合。

### （1）Construct：任务特定 Concept MKG
- **任务引导的模式归纳（Task-Guided Schema Induction）**：
  - 对每个关系 r，用其名称 + 最多 S=5 条代表性三元组构成短文 `xr`，经 SapBERT 编码；
  - 用**余弦距离 + 平均链接的凝聚聚类**（阈值 0.15）得到跨任务共享的语义簇 `{Ki}`；
  - 对每个任务描述 `Tτ` 与每个簇摘要 `si`，用指令微调 LLM（GPT-5）判定相关性并赋予规范关系名（保持 snake_case、动词式、≤4 词），不相关则输出 `IGNORE`；
  - 归一化命名并合并同名簇以消解跨簇不一致，得到规范关系集 `Rτ` 与映射 **`fτ : R → Rτ ∪ {IGNORE}`**。
- **KG 归一化**：按 `fτ` 重写三元组，丢弃映射为 IGNORE 者，得到任务归一化图谱 `Gτ = (V, Rτ, Eτ)`，三元组集 `Eτ = {(h, fτ(r), t)}`。
- **Concept MKG 抽取（全局 1-hop）**：仅用**训练集**出现的 EHR 概念作锚点，在 `Gτ` 上做全局 1-hop 扩展，仅保留端点属于临床有意义语义类型 `Smed`（UMLS 的 Disorders、Procedures、Chemicals & Drugs 三大语义组）的三元组，去重后得到 `Gconcept_τ`。

### （2）Personalize：PKG 构造与编码
- **PKG 构造**：对患者 p 的概念集 `Cp`，附接其在 `Gconcept_τ` 中的 1-hop 邻域，并在 `Gτ` 中为**共现概念对**插入短知识路径（2-hop）；通过邻居上限 `Knbr=30`、每对锚点路径上限 `Kpath=2` 控制图谱规模；结果为 `Gpkg_{p,τ} = (V, Rτ ∪ Rehr, E)`，同时含患者临床事件与任务知识。
- **PKG 编码器**：多层**关系图卷积网络（R-GCN）**，节点经关系特定变换与自环变换、归一化常数 `cv,r` 与激活 σ 逐层更新：
  `h^(l+1)_v = σ( Σ_r Σ_{u∈Nr(v)} (1/c_{v,r}) W^(l)_r h^(l)_u + W^(l)_0 h^(l)_v )`，L 层后输出节点表示。

### （3）Integrate：EHR–PKG 融合与预测
- **EHR 编码器 HTT（Hierarchical Time-aware Transformer，受 HiTANet 启发）**：访视内概念聚合 → 跨访视的时间感知 Transformer（编码访视顺序与时间间隔）。
  - 患者级任务：对访视做注意力池化得 `z_ehr_p = Σ_t α_{p,t} h_{p,t}`；
  - 访视级任务：直接以 `h_{p,t}` 作为该实例上下文。
- **交叉注意力融合**：以 EHR 上下文 `qi` 为 query，PKG 节点表示为 key/value，得知识摘要 `ci = CrossAttn(qi, {h^(L)_v})`；融合表示 `z_fuse_i = ϕ([qi; ci])`（两层 MLP）。访视级任务构造 PKG 时**只用截至该访视的概念**，避免未来信息泄漏。
- **预测与训练**：二分类 `ŷi = σ(w_τ^T z_fuse_i + b_τ)`，损失为逐实例二元交叉熵（`BCEWithLogitsLoss`）。

## 3. 实验设计

- **数据集**：MIMIC-III（过滤后 7,537 患者 / 19,993 访视）与 MIMIC-IV（100,163 患者 / 422,739 访视），保留 ≥2 次访视的患者；患者级 8:1:1 划分且不重叠。
- **四个预测任务**：
  - 通用型（访视级）：**院内死亡**、**30 天再入院**；
  - 疾病型（患者级，12 个月观察窗 + 12 个月预测窗，排除既往患病者）：**T2DM 发作**、**CAD 发作**。
- **指标**：AUROC 与 AUPRC，报告 5 个随机种子的均值 ± 标准差。
- **对比方法（三类基准）**：
  - EHR-only：GRU、Transformer、RETAIN、HiTANet；
  - 静态 KG 增强：GRAM、KAME；
  - PKG 推理：KerPrint、KGxDP、GraphCare。
- **消融变体**：w/o Construct、w/o Personalize、w/o Integrate（PKG-only）、w/o Integrate（EHR-only）。
- **附加分析**：PKG 最大路径长度敏感性（1–5）；交叉注意力在各关系类型上的分布；模式归纳鲁棒性（换用 GPT-4o / Llama 3.1-70B / Qwen2.5-72B 及两种非 LLM 基线）；替代融合策略（Late fusion、Gated fusion、FiLM 调制）。

## 4. 资源与算力

- 文中明确提到实验在 **NVIDIA GH200 GPU** 上进行，并致谢英国 **Isambard-AI** 国家级 AI 研究资源（由布里斯托大学运营）。
- **未说明**：GPU 具体数量、训练时长、总计算量、单模型训练成本等均未给出。
- 其他工程细节：每对"数据集–任务"训练独立模型；AdamW 优化，早停（patience 10，最多 30 轮）；超参在验证集上按 AUROC 调优（表 9 给出搜索空间，含嵌入/隐藏维度、HTT 与 R-GCN 层数、学习率、权重衰减、dropout、batch size、最大路径长度）。
- 补充：模式归纳使用 **GPT-5** 离线完成（另测试 GPT-4o、Llama 3.1-70B、Qwen2.5-72B），这部分调用成本与能耗同样未量化。

## 5. 实验数量与充分性

- **规模**：2 个数据集 × 4 个任务 = 8 个"数据集–任务"组合；每个组合 5 个随机种子；消融在全部任务上展开（正文表 4 + 附录表 10）；另含路径长度、注意力分布、模式归纳鲁棒性、融合策略四类附加分析。总体实验量较充分。
- **客观性与公平性**：
  - 采用标准公开数据集与代表性基线，评价指标（AUROC/AUPRC）规范，报告均值±方差；
  - 严格患者级划分，避免患者重叠；任务输入只用预测时点前的记录，防标签泄漏；
  - 超参在验证集调优，PKG 路径长度亦在验证集选择，减少测试集调参风险；
  - 附录补充了模式归纳与融合策略的对照，增强可复现性与稳健性论证。
- **可改进处**：未报告统计显著性检验（如配对 t 检验/置信区间）；部分任务类别极不平衡（如死亡率 AUPRC 普遍偏低），AUPRC 的绝对差异解释力有限；疾病型任务训练实例较少（MIMIC-III T2DM 仅 1,419），可能放大方差。

## 6. 主要结论与发现

- **整体性能**：MedCPI 在全部数据集与任务上均取得最优结果，一致优于 EHR-only、静态 KG 增强与已有 PKG 推理方法（例如 MIMIC-III 院内死亡 AUROC 0.713 / AUPRC 0.242；MIMIC-IV 30 天再入院 AUROC 0.744 / AUPRC 0.606；MIMIC-IV T2DM 发作 AUROC 0.763）。
- **三类方法对比观察**：
  - 强时序建模（如 HiTANet）在多个设定下可媲美甚至超过静态知识增强方法，说明纵向序列建模很重要；
  - 静态 KG 增强收益有限且不稳定；
  - PKG 推理整体更稳健，说明"按患者上下文选择并使用知识"比"固定注入知识"更有效。
- **消融结论**：移除任一阶段都会掉点——Construct 影响一致且明显；Personalize 在 T2DM 发作上掉点更显著；Integrate 的 PKG-only 与 EHR-only 都劣于全模型，说明结构化知识与纵向 EHR 建模互补、缺一不可。
- **路径长度**：从 1 增至 2 时性能提升，之后随路径变长逐渐下降，说明**短知识路径已足够**（最终取 2-hop）。
- **可解释性**：交叉注意力呈任务相关分布——死亡预测更关注 `has_complication`、`treated_by`；T2DM 发作更关注 `has_risk_factor`、`diagnosed_by`，表明模型选择性利用任务相关医学关系。
- **模式归纳鲁棒性**：GPT-5 与 GPT-4o 一致性高（Jaccard 分别 1.000 与 0.926），明显优于非 LLM 基线（0.655 / 0.542）。
- **融合策略**：交叉注意力优于 Late fusion、Gated fusion 与 FiLM 调制。

## 7. 优点

- **范式清晰、模块解耦**：Construct–Personalize–Integrate 三阶段各司其职，形成可复用的知识构建与使用流程。
- **任务引导的知识去噪**：用 LLM 做关系簇相关性判定与规范命名，配合 KG 归一化，显式缓解多源图谱的模式冗余与语义重叠，且模式可跨数据集共享。
- **可控的个性化**：以 1-hop 限制 + 共现锚点间的 2-hop 短路径 + 明确的规模上限（`Knbr`、`Kpath`）构造 PKG，兼顾信息量与效率、可解释性。
- **时间对齐的整合**：以时间感知 EHR 表示作为 cross-attention 的 query，使知识整合随患者轨迹演进；访视级任务只用截至预测点的概念，防止未来信息泄漏。
- **可解释性**：关系类型层面的注意力分布为"模型用了哪些医学知识"提供直观证据。
- **实验较严谨**：多数据集、多任务、多随机种子、患者级划分、验证集调参、消融 + 敏感性 + 鲁棒性 + 融合策略对照，并公开代码仓库。

## 8. 不足与局限

- **作者自述局限**：
  - 仅基于 MKG 中的**结构化关系**构造 Concept MKG 与 PKG，未纳入更多本体、人工整编资源或其他模式设计；
  - Personalize 采用**固定、可解释的约束**（非自适应），未来需发展兼顾可解释性与效率的自适应个性化策略；
  - 仅研究结构化 EHR + KG，**未纳入非结构化临床文本**等多模态信息；
  - 仅在 MIMIC-III/IV 上评估，跨数据集、跨护理场景与跨医疗系统的泛化性待验证。
- **方法层面的潜在风险**：
  - **对 LLM 的依赖**：模式归纳依赖 GPT-5（另测其他 LLM），带来复现性、成本与"LLM 判定偏差/幻觉"风险；非 LLM 基线表现明显更弱，也说明流程对 LLM 质量较敏感。
  - **任务描述驱动**：任务相关性的判定依赖任务描述文本质量，描述不当可能影响知识筛选。
- **实验覆盖与偏差**：
  - MIMIC 为单一（美国）重症监护来源、去标识化数据，可能存在**单中心与人群偏差**，影响临床推广；
  - 未报告算力开销（GPU 数量、训练时长）与推理成本，也**缺少统计显著性检验**；
  - 部分任务正例稀少（如死亡率），AU
