---
title: Early Warning of Intraoperative Adverse Events via Transformer-Driven Multi-Label Learning
title_zh: 基于Transformer多标签学习的术中不良事件早期预警
authors: "Xueyao Wang, Xiuding Cai, Honglin Shang, Yaoyao Zhu, Yu Yao"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39870/43831"
tags: ["query:ehr-es"]
score: 6.0
evidence: 多标签临床不良事件预测
tldr: 术中不良事件预警对降低手术风险至关重要，但现有方法忽视事件依赖、未充分利用异构临床数据且受类别不平衡困扰。本文构建首个多标签不良事件数据集MuAE（覆盖六类事件），并提出基于Transformer的多标签学习框架IAENet，引入时间感知特征调制模块。实验表明其能有效利用异构临床数据并提升多事件预警性能。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 术中不良事件预警忽视事件依赖、异构数据利用不足与类别不平衡。
method: 构建MuAE数据集并提出融合时间感知调制的Transformer多标签框架IAENet。
result: 有效利用异构临床数据，提升多标签不良事件预警效果。
conclusion: 为临床多标签事件预警提供了数据集与建模方案。
---

## Abstract
Early warning of intraoperative adverse events plays a vital role in reducing surgical risk and  improving patient safety. While deep learning has shown promise in predicting the single adverse event, several key challenges remain: overlooking adverse event dependencies, underutilizing heterogeneous clinical data, and suffering from the class imbalance inherent in medical datasets. To address these issues, we construct the first Multi-label Adverse Events dataset (MuAE) for intraoperative adverse events prediction, covering six critical events. Next, we propose a novel Transformer-based multi-label learning framework (IAENet) that combines an improved Time-Aware Feature-wise Linear Modulation (TAFiLM) module for static covariates and dynamic variables robust fusion and complex temporal dependencies modeling. Furthermore, we introduce a Label-Constrained Reweighting Loss (LCRLoss) with co-occurrence regularization to effectively mitigate intra-event imbalance and enforce structured consistency among frequently co-occurring events. Extensive experiments demonstrate that IAENet consistently outperforms strong baselines on 5, 10, and 15-minute early warning tasks, achieving improvements of +5.05%, +2.82%, and +7.57% on average F1 score. These results highlight the potential of IAENet for supporting intelligent intraoperative decision-making in clinical practice.

---

## 论文详细总结（自动生成）

# 论文总结：基于Transformer多标签学习的术中不良事件早期预警

## 1. 核心问题与整体含义

- **研究背景**：全球每年实施超过3亿台手术，46–65%的医疗不良事件与手术相关，3–22%的手术患者出现并发症。术中不良事件（如低血压、低氧血症）若持续时间过长，会引发肺功能障碍、急性肾损伤、心血管事件等严重并发症，增加死亡风险。多数事件可通过及时干预预防，因此准确的早期预警系统至关重要。
- **核心问题**：现有AI预测方法主要聚焦于**单一不良事件**（如仅预测低血压或低氧血症），存在三大关键挑战：
  - **忽视不良事件间的依赖关系**：单一事件预测无法捕捉共现事件（如心动过缓常与低血压共现）的临床关联。
  - **异构临床数据利用不足**：静态协变量（年龄、体重等）与动态生命体征（血压、心率等）的直接拼接融合会引入特征冗余和噪声。
  - **类别极度不平衡**：不良事件仅占总样本的0.189%–2.531%，严重阻碍模型泛化。
- **整体含义**：本文构建了首个术中多标签不良事件数据集MuAE，并提出IAENet框架，将术中风险预测从单事件范式推进到多标签联合建模，为临床智能决策提供新方案。

## 2. 方法论：核心思想与关键技术细节

### 2.1 整体框架
- **核心思想**：基于Transformer编码器进行多标签时序分类，通过TAFiLM模块实现静态协变量与动态变量的早期融合，通过LCRLoss解决类别不平衡与标签依赖问题。
- **输入表示**：15个动态变量（药物输注参数、BIS、血压、体温、心率、SpO₂、ECG等）与5个静态协变量（年龄、体重、身高、性别、ASA分级）拼接为 $x \in \mathbb{R}^{W \times (D+S)}$。

### 2.2 TAFiLM模块（Time-Aware Feature-wise Linear Modulation）
- 受FiLM模块启发，针对时序数据改进。静态条件特征 $x_s \in \mathbb{R}^{B \times S}$ 经MLP条件网络生成时变缩放因子 $\gamma_s$ 和平移因子 $\beta_s \in \mathbb{R}^{B \times W \times D}$。
- 对动态特征进行仿射变换调制：
  $$\text{TAFiLM}(x_d) = ((\gamma_s + 1) \odot x_d + \beta_s)$$
  其中 $\odot$ 为Hadamard积。该设计以静态信息动态调制动态特征，减少直接拼接带来的冗余噪声。

### 2.3 Transformer编码器
- 采用倒置嵌入（inverted embedding），将每个变量作为独立token，捕捉多变量相关性。
- 输入序列反转以解决时间戳错位问题；每个变量独立进行LayerNorm以保持变量独立性；经多头自注意力和前馈网络后用于下游分类。

### 2.4 LCRLoss（Label-Constrained Reweighting Loss）
- **批内动态重加权**：按批内标签频率的平方根倒数缩放损失权重：
  $$q(y_i) = \begin{cases} \frac{1}{\sqrt{P_c/N}} & y_i=1 \\ \frac{1}{\sqrt{N_c/N}} & \text{otherwise} \end{cases}$$
- **共现正则化**：从训练集计算标签共现矩阵 $M = \sum_b (y^{(b)})^\top y^{(b)}$，归一化后作为权重，约束频繁共现标签的预测一致性：
  $$\mathcal{L}_{co} = \sum_{i,j} \text{co\_matrix}(y_i, y_j) \|\hat{y}_i - \hat{y}_j\|_2^2$$
- **总损失**：$\mathcal{L}_{LCR} = \mathcal{L}_{weight} + \lambda \mathcal{L}_{co}$，其中 $\lambda$ 经网格搜索设为0.02。

## 3. 实验设计

### 3.1 数据集与场景
- **MuAE数据集**：基于公开VitalDB数据集构建，原始包含6388例非心脏手术麻醉记录。经清洗（手术时长>2小时、排除儿童及ASA>6级），最终纳入**873例患者**。
- **事件定义**：6类不良事件——低血压（MAP<65 mmHg）、低麻醉深度（BIS<40）、心律失常（HR<60或>100 bpm）、低氧血症（SpO₂<90%）、低体温（BT<35°C）、低碳酸血症（EtCO₂<30 mmHg），均需持续至少1分钟。
- **预测任务**：分别进行**5分钟、10分钟、15分钟**提前预警，输入窗口30秒，滑动步长2秒，生成约4.88M/5.66M/5.55M样本。
- **数据划分**：按患者划分训练集70%、验证集10%、测试集20%。

### 3.2 Benchmark与对比方法
- **基线模型**（10种）：DLinear、SegRNN、iTransformer、PatchTST、FEDformer、Autoformer、Informer、TFT、Crossformer、Non-stationary Transformer。
- **损失函数对比**（7种）：LCRLoss、WBCE、BCE、Focal Loss、PolyLoss、ASL、SoftMarginLoss。
- **评估指标**：Micro F1、Macro AUC、Micro Precision、Micro Recall、Micro Accuracy、Hamming Loss，以F1和AUC为主。

## 4. 资源与算力

- **论文未明确说明**所使用的GPU型号、数量及训练时长。
- 仅提及实现细节：基于Time-Series-Library框架开发，使用RAdam优化器，初始学习率1e−3，批次大小64，训练10个epoch，早停耐心为3个epoch。λ经网格搜索在[0.001, 0.01, 0.02, 0.05, 0.1, 0.2]中确定为0.02。
- 这是论文在可复现性方面的一个明显信息缺口。

## 5. 实验数量与充分性

- **主要实验**：
  - 3个预测时间窗（5/10/15分钟）× 11种模型（含IAENet）× 6类事件 × 6项指标的大规模对比实验。
  - 7种损失函数的对比实验。
  - 消融实验：在4个基线模型上分别加入LCRLoss、FiLM、TAFiLM模块（共12组）。
  - 重加权策略对比：全局/批内频率 × 4种方案（inverse、log inverse、sqrt inverse、cubic inverse）。
  - 批次大小（64/128/256）和λ系数（6个取值）的敏感性分析。
  - 梯度分析：对比BCE、FL、ASL、PolyLoss、LCRLoss的梯度曲线。
  - 共现矩阵可视化。
- **充分性与公平性评价**：
  - 实验覆盖较全面，包含多时间窗、多基线、多损失函数和系统消融，整体设计较为充分。
  - 对比方法均使用标准BCE损失，IAENet使用LCRLoss，但作者通过消融实验（Table 3）验证了各组件在统一设置下的增益，部分缓解了公平性顾虑。
  - 所有模型在同一数据划分下评估，指标选择合理（F1/AUC对类别不平衡鲁棒）。
  - 但数据集规模较小（873例），且仅来自单一医疗中心（首尔大学医院），外部泛化性验证不足。

## 6. 主要结论与发现

- IAENet在5、10、15分钟预警任务上均持续优于所有基线，平均F1分别提升**+5.05%、+2.82%、+7.57%**。
- 预测性能随预测时间窗延长而下降，说明事件发生前的近端窗口包含更多判别性特征。
- LCRLoss优于所有对比损失函数，相比最强替代ASL，平均F1提升0.49%，AUC提升1.02%。
- TAFiLM作为即插即用模块，在多个基线上均带来F1和AUC提升，且优于原始FiLM；TAFiLM略降精度但显著提升召回率，有利于减少临床漏诊。
- 批内频率平方根倒数重加权策略表现最佳，优于全局静态重加权。
- 梯度分析显示LCRLoss在高置信区域仍保持有效梯度，且能促进频繁共现事件（如心律失常与低麻醉深度、低体温）的预测一致性。

## 7. 优点

- **数据集贡献**：构建了首个术中多标签不良事件数据集MuAE，填补了该领域多事件联合预测的数据空白。
- **方法创新**：
  - TAFiLM模块将静态协变量作为条件对动态特征进行仿射调制，避免了直接拼接的冗余和噪声，融合方式优雅且有效。
  - LCRLoss同时解决类别不平衡（批内动态重加权）和标签依赖（共现正则化），设计具有针对性。
  - 采用倒置嵌入的Transformer编码器，天然捕捉多变量相关性。
- **实验扎实**：对比了10种主流时序模型和6种损失函数，消融实验覆盖组件、策略、超参数和梯度分析，论证链条完整。
- **临床意义明确**：以召回率为重（减少漏诊）的倾向符合医疗预警场景的实际需求。

## 8. 不足与局限

- **算力信息缺失**：未报告GPU型号、数量、训练时长，影响可复现性和资源评估。
- **数据集规模与来源局限**：仅873例患者，全部来自单一中心（首尔大学医院）的VitalDB，种族、地域、手术类型覆盖有限，外部泛化性未验证。
- **性能仍不理想**：部分事件（如低碳酸血症）在所有模型中F1均较低（15分钟时IAENet仅25.89%），受极端不平衡影响，实际临床可用性存疑。
- **预测窗口有限**：最长仅15分钟，未探索更长时间跨度的预警能力。
- **偏差风险**：数据清洗中排除儿童、低体重及ASA>6级患者，模型不适用于这些人群；标签定义依赖固定阈值，可能忽略临床个体差异。
- **未来方向**：作者提出将引入外部知识并扩展到更广泛的临床数据集和事件类型，但当前工作尚未涉及。

（完）
