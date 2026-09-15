---
title: "CURA: Clinical Uncertainty Risk Alignment for Language Model–Based Risk Prediction"
title_zh: CURA：面向语言模型风险预测的临床不确定性风险对齐
authors: "Sizhe Wang, Ziqi Xu, Claire Najjuuko, Charles Alba, Chenyang Lu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.acl-long.1567.pdf"
tags: ["query:ehr-es"]
score: 7.0
evidence: 临床风险预测的不确定性校准与误差对齐
tldr: 该工作针对临床语言模型在风险预测中不确定性估计校准差、临床可靠性不足的问题，提出临床不确定性风险对齐框架CURA。方法先微调领域临床模型获得患者嵌入，再以双层不确定性目标对多头分类器做不确定性微调，其中个体级校准项使预测不确定性对齐患者出错概率，队列级项对齐群体歧义。实验表明该方法改善了不确定性校准与临床可靠性。其为EHR相关预测的可信与不确定性量化提供了直接支撑。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1567/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 1078, \"height\": 1094}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1567/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 1076, \"height\": 1066}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1567/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 990, \"height\": 652}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1567/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1567/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1567/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1567/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 1024, \"height\": 1024}]"
motivation: 临床语言模型风险预测的不确定性估计校准差，临床可靠性不足。
method: 先微调临床模型得患者嵌入，再以双层不确定性目标做校准微调对齐个体与队列歧义。
result: 在临床风险预测上改善了不确定性校准与整体可靠性。
conclusion: 为EHR相关预测的可信性与不确定性量化提供了直接方法支撑。
---

## Abstract
Clinical language models (LMs) are increasingly applied to support clinical risk prediction from free-text notes, yet their uncertainty estimates often remain poorly calibrated and clinically unreliable. In this work, we propose Clinical Uncertainty Risk Alignment (CURA), a framework that aligns clinical LM-based risk estimates and uncertainty with both individual error likelihoods and cohort-level ambiguities. CURA first fine-tunes domain-specific clinical LMs to obtain task-adapted patient embeddings, and then performs uncertainty fine-tuning of a multi-head classifier using a bi-level uncertainty objective. Specifically, an individual-level calibration term aligns predictive uncertainty with each patient’s likelihood of error, while a cohort-aware regularizer pulls risk estimates toward event rates in their local neighborhoods in the embedding space and places extra weight on ambiguous cohorts near the decision boundary. We further show that this cohort-aware term can be interpreted as a cross-entropy loss with neighborhood-informed soft labels, providing a label-smoothing view of our method. Extensive experiments on MIMIC-IV clinical risk prediction tasks across various clinical LMs show that CURA consistently improves calibration metrics without substantially compromising discrimination. Further analysis illustrates that CURA reduces overconfident false reassurance and yields more trustworthy uncertainty estimates for downstream clinical decision support.

---

## 论文详细总结（自动生成）

# CURA：面向语言模型风险预测的临床不确定性风险对齐——论文总结

## 1. 核心问题与整体含义

- **研究背景**：临床语言模型（LMs）被广泛用于从自由文本临床笔记中支持风险预测（如死亡率、住院时长），但其不确定性估计往往**校准差、临床不可靠**。
- **核心痛点**：
  - 微调虽提升预测性能，却常**加剧过自信**，导致模型对高风险患者“高置信度却判断错误”（图1左侧示例）。
  - 通用集成方法（MC Dropout、Deep Ensembles）仅聚合多次预测，**未利用表示空间的语义结构**，只在孤立样本层面调整置信度，对边界队列仍可能校准不良。
  - 面向生成式LLM的校准方法多依赖**专家撰写的理由、高质量CoT标注或强教师模型**；而临床工作流中下游任务通常只有二值结局标签，缺乏大规模真实解释。
- **整体含义**：需要一种**直接作用于学习表示与二值标签、不依赖显式文本理由**的不确定性校准方法，使模型对正确决策保持高置信、对潜在错误给予更高不确定性，从而支持安全临床分诊。

## 2. 方法论

### 2.1 核心思想

CURA（Clinical Uncertainty Risk Alignment）是一个**双层（个体级 + 队列级）不确定性校准框架**，构建在微调后的临床LM之上，通过多头分类器与三个损失项联合优化，实现：
- 个体级：预测不确定性对齐每个患者的出错概率；
- 队列级：风险估计向嵌入空间中局部邻域的事件率靠拢，并对决策边界附近的模糊队列加权。

### 2.2 关键技术细节

- **第一阶段：临床LM微调**
  - 输入为去标识化临床笔记 \(x_i\)，标签 \(y_i \in \{0,1\}\)。
  - 在领域特定临床LM \(\pi_\theta\) 上接线性分类器，用**类加权二元交叉熵**联合优化。
  - 微调后**冻结LM**，作为特征提取器得到固定维患者嵌入 \(e_i = \pi_\theta(x_i)\)。

- **第二阶段：不确定性微调（多头分类器）**
  - 在冻结嵌入上构建 **M个独立随机初始化的轻量MLP头**，推理时取平均预测 \(\bar{p}(x_i) = \frac{1}{M}\sum_{m=1}^M p_m(e_i)\)。
  - **基础风险损失** \(L_{\text{base}}\)：集成平均预测与真实标签的类加权交叉熵，提供判别力锚点，防止退化解。

- **个体不确定性校准** \(L_{\text{ind}}\)
  - 定义正确性概率 \(a(x) = y\bar{p}(x) + (1-y)(1-\bar{p}(x))\)。
  - 用集成平均预测的熵 \(H(x)\) 衡量不确定性，归一化得 \(u(x) = H(x)/H_{\max} \in [0,1]\)。
  - 对齐不确定性与错误代理 \((1-a(x))\)，最小化：
    \[
    L_{\text{ind}} = \lambda_{\text{ind}} \mathbb{E}\left[-(1-a)\log u - a\log(1-u)\right]
    \]
  - 效果：正确且自信→小损失；自信但错误→大惩罚。

- **队列感知风险对齐** \(L_{\text{coh}}\)
  - 对每个样本 \(e_i\) 检索 **K近邻**，计算邻域事件率 \(q(x_i) = \frac{1}{K}\sum_{j \in N_K(e_i)} y_j\)。
  - 用邻域熵 \(\hat{H}(q(x_i))\) 衡量队列模糊性，自适应权重 \(w(x_i) = \lambda_{\text{coh}} \hat{H}(q(x_i))\)。
  - 损失：
    \[
    L_{\text{coh}} = \mathbb{E}_{x_i}\left[w(x_i)\,\text{CE}(\bar{p}(x_i), q(x_i))\right]
    \]
  - 将预测拉向邻域风险，并对高熵（边界模糊）队列加大权重。

- **总目标**
  \[
  L_{\text{total}} = L_{\text{base}} + L_{\text{ind}} + L_{\text{coh}}
  \]

- **理论解释（附录F）**：\(L_{\text{base}} + L_{\text{coh}}\) 可等价写为**带队列信息软标签的交叉熵**，软标签 \(t(x) = (1-\gamma(x))y + \gamma(x)q(x)\)，其中 \(\gamma(x)=w(x)/(1+w(x))\)，可视为**数据依赖的标签平滑**，高邻域熵队列获得更强正则化。

- **实现特点**：轻量级即插即用损失，无需架构改动，不引入额外骨干参数或额外前向传播。

## 3. 实验设计

- **数据集/场景**：MIMIC-IV 去标识化临床笔记（出院摘要），预测五个风险分层任务：
  1. 7天死亡率（正例率 0.88%）
  2. 30天死亡率（2.87%）
  3. 12小时内早期出院（0.74%）
  4. 院内死亡率（1.71%）
  5. ICU停留超过1天（2.50%）
  - 两个出院后死亡率任务约 **323K** 次就诊；其余三个约 **142K** 次就诊。

- **Benchmark**：与既往临床LM研究任务对齐，采用**五折交叉验证**。

- **对比方法**：
  - **Deep Ensembles**（M=5）
  - **MC Dropout**（p=0.5，T=10次随机前向）
  - **内部基线**：相同多头架构但仅优化类加权交叉熵
  - 所有基线共享相同微调骨干，差异仅来自不确定性机制。

- **评估指标**：
  - 区分度：AUROC、AUPRC
  - 校准与不确定性：Brier score、NLL、AURC

- **骨干模型**：BioGPT（主实验）、BioClinicalBERT、ClinicalBERT（附录B）。

## 4. 资源与算力

- **硬件**：主要在 **A40 GPU（48GB VRAM）** 上完成，来自 Research Infrastructure Services compute1 集群（经批准可处理受保护健康信息）。
- **模型规模**：BERT类模型约 **1.1亿参数**，BioGPT约 **3.47亿参数**。
- **运行时对比**（7天死亡率，BioGPT，单张NVIDIA A40，五折交叉验证总计）：
  - Baseline：1.03 GPU hours
  - Deep Ensemble：4.43 GPU hours
  - MC Dropout：1.08 GPU hours
  - **CURA：0.94 GPU hours**（含一次性K近邻预计算）
- **未明确说明**：具体使用的GPU数量、总训练时长、总能耗等未详细报告；仅给出单任务运行时对比。

## 5. 实验数量与充分性

- **主实验规模**：3个骨干模型 × 5个任务 = **15组主要结果**（BioGPT主文表1，BioClinicalBERT/ClinicalBERT附录B表3、表4）。
- **消融实验**：5个任务上分离 \(L_{\text{ind}}\) 与 \(L_{\text{coh}}\) 贡献（主文表2报告2个高利害任务，附录D表5报告其余3个）。
- **敏感性分析**：\(\lambda_{\text{ind}}\) 与 \(\lambda_{\text{coh}}\) 在两个高利害死亡率任务上的调参分析（附录E表6、表7）。
- **不确定性分析**（7天死亡率，BioGPT）：
  - 不确定性分布、分箱准确率、分箱正例率（图3）
  - 选择性部署：保留队列AUPRC vs 保留比例（图5）
  - 分诊工作负载–安全权衡：每1000患者漏诊事件数 vs 自动管理比例（图6）
  - 假安慰率：五个任务（图4），并在 \(\tau=0.05, 0.15\) 下做阈值敏感性（附录H图7、图8）
- **运行时对比**：附录I表8。
- **充分性与公平性**：
  - 五折交叉验证并报告标准差，统计较严谨。
  - 所有方法共享相同骨干与分类器架构，差异仅来自不确定性目标，比较公平。
  - 消融、敏感性、多种骨干验证较全面。
  - **局限**：仅单中心回顾性数据，未评估闭源API模型，未做多模态/纵向扩展。

## 6. 主要结论与发现

- CURA在五个临床任务上**持续改善校准指标**（Brier、NLL、AURC），同时**保持甚至略微提升区分度**（AUROC、AUPRC）。
- Deep Ensembles与MC Dropout在区分度上具竞争力，但校准改善有限，有时甚至略差。
- 消融显示 \(L_{\text{ind}}\) 与 \(L_{\text{coh}}\) 各自有效，**联合使用最佳**。
- CURA使不确定性分布**更分散**，将概率质量从过自信尖峰移至中高不确定性区域；每个不确定性分箱的准确率更高，且高不确定性分箱正例率显著富集。
- **降低假安慰率**：在5个任务中的4个取得最低假安慰率，7天/30天死亡率任务上降幅显著，减少高风险患者被自信误判为安全的情况。
- **改善分诊效率**：在相同安全阈值下可自动管理更大比例患者；相同工作负载下漏诊事件更少。
- 队列感知项可解释为**邻域信息软标签的标签平滑**，方法具有理论视角。
- 方法**模型无关**，在BioGPT、BioClinicalBERT、ClinicalBERT上一致有效。

## 7. 优点

- **双层校准思想新颖**：同时对齐个体错误概率与队列邻域风险，弥补了传统方法忽略表示空间结构的不足。
- **理论解释清晰**：将队列感知损失等价为带软标签的交叉熵，提供标签平滑视角，增强可解释性。
- **轻量即插即用**：不改变架构，不增加额外前向传播，运行时甚至略低于基线，远低于Deep Ensembles。
- **临床相关性强**：引入假安慰率、分诊工作负载–安全权衡等贴近部署场景的指标，分析深入。
- **实验严谨**：五折交叉验证、多骨干验证、消融与敏感性分析较完整，结果稳定。
- **不依赖外部解释**：仅需二值标签与学习表示，适合真实临床工作流。

## 8. 不足与局限

- **数据与场景限制**：仅使用MIMIC-IV**单中心回顾性**数据，未验证多中心、前瞻性场景；任务均为**二分类**风险分层。
- **模型覆盖有限**：未评估闭源API模型（因MIMIC-IV数据使用协议禁止共享患者数据给第三方平台）；仅涉及判别式LM，未与生成式模型的可解释推理结合。
- **公平性风险**：MIMIC数据反映系统性健康差异，CURA**不直接缓解**数据中的结构性偏差，可能传播原有不公平。
- **超参数依赖**：\(\lambda_{\text{ind}}\)、\(\lambda_{\text{coh}}\)、K近邻数K、阈值\(\tau\)等需调节；虽敏感性分析显示默认值稳定，但仍需针对新任务调参。
- **扩展性考虑**：K近邻需预计算，大规模数据或在线更新场景下的计算与维护成本未充分讨论。
- **解释性缺失**：方法输出标量风险与不确定性，不提供文本理由，临床医生难以直接理解“为何不确定”。
- **算力报告不完整**：仅报告单任务GPU小时，未说明总GPU数量、总训练时长与能耗。

（完）
