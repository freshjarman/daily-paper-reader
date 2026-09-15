---
title: "Toward Better EHR Reasoning in LLMs: Reinforcement Learning with Expert Attention Guidance"
title_zh: 面向更优EHR推理的大语言模型：基于专家注意力引导的强化学习
authors: "Yue Fang, Yuxin Guo, Jiaran Gao, Hongxin Ding, Xinke Jiang, Weibin Liao, Yongxin Xu, Yinghao Zhu, Zhibang Yang, Liantao Ma, Junfeng Zhao, Yasha Wang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40325/44286"
tags: ["query:ehr-es"]
score: 7.0
evidence: 通过强化学习增强大模型对时序结构化EHR的推理
tldr: 大语言模型擅长医学文本理解，却因难以建模时序结构化、高维的电子健康记录而在EHR预测任务上表现欠佳。现有混合范式仅把大模型当作冻结的先验检索器，无法提升其内在推理能力。本文提出EAG-RL两阶段训练框架，利用专家注意力引导从本质上增强大模型的EHR推理能力。实验表明其提升了临床预测的准确性与泛化性，为EHR序列的基础模型建模提供新思路。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 大模型难以建模时序结构化高维EHR，现有混合范式无法提升其内在临床推理能力。
method: 提出EAG-RL两阶段训练框架，利用专家注意力引导通过强化学习增强大模型的EHR推理。
result: 在EHR预测任务上提升了准确性与跨场景泛化能力。
conclusion: 为以基础模型建模EHR事件序列并支撑临床预测提供了新的训练范式。
---

## Abstract
Improving large language models (LLMs) for electronic health record (EHR) reasoning is essential for enabling accurate and generalizable clinical predictions. While LLMs excel at medical text understanding, they underperform on EHR-based prediction tasks due to challenges in modeling temporally structured, high-dimensional data. Existing approaches often rely on hybrid paradigms, where LLMs serve merely as frozen prior retrievers while downstream deep learning (DL) models handle prediction, failing to improve the LLM’s intrinsic reasoning capacity and inheriting the generalization limitations of DL models. To this end, we propose EAG-RL, a novel two-stage training framework designed to intrinsically enhance LLMs’ EHR reasoning ability through expert attention guidance, where expert EHR models refer to task-specific DL models trained on EHR data. Concretely, EAG-RL first constructs high-quality, stepwise reasoning trajectories using expert-guided Monte Carlo Tree Search to effectively initialize the LLM’s policy. Then, EAG-RL further optimizes the policy via reinforcement learning by aligning the LLM’s attention with clinically salient features identified by expert EHR models. Extensive experiments on two real-world EHR datasets show that EAG-RL improves the intrinsic EHR reasoning ability of LLMs by an average of 14.62%, while also enhancing robustness to feature perturbations and generalization to unseen clinical domains. These results demonstrate the practical potential of EAG-RL for real-world deployment in clinical prediction tasks.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究背景**：大语言模型（LLM）在医学文本理解任务中表现较强，但在基于电子健康记录（EHR）的临床预测任务上明显不足。EHR 具有时序结构化、高维、异构等特点，LLM 难以直接建模。
- **核心问题**：现有方法多采用“混合范式”，即 LLM 仅作为冻结的先验检索器，真正预测由下游深度学习模型完成。这种方式没有提升 LLM 自身的 EHR 推理能力，也继承了传统 DL 模型对输入模式、特征顺序和编码方式的脆弱性。
- **研究动机**：
  - 临床预测类似“假设-演绎”过程，医生会逐步提出诊断子问题并整合证据。
  - 专家 EHR 模型（如 Concare）的注意力可反映临床显著特征，可作为 LLM 的辅助监督信号。
- **整体含义**：论文提出 **EAG-RL**，一个两阶段训练框架，试图通过专家注意力引导的强化学习，从本质上增强 LLM 的 EHR 推理能力，而不是仅把 LLM 当作外挂检索器。

## 2. 论文提出的方法论

### 2.1 核心思想

EAG-RL 采用两阶段训练：

1. **Stage 1：Expert-Guided Trajectory Distillation**  
   用专家引导的 Monte Carlo Tree Search 构造高质量、逐步推理轨迹，再通过轨迹级 SFT 初始化 LLM 策略。
2. **Stage 2：Attention-Aligned Policy Optimization**  
   用强化学习进一步优化策略，奖励同时考虑预测正确性和与专家 EHR 模型注意力的对齐程度，并引入熵感知自适应上裁剪以鼓励探索。

### 2.2 Stage 1：专家引导轨迹蒸馏

- **问题分解 Prompt**：  
  引导 LLM 将复杂 EHR 预测分解为多个 `<Subquestion>` 和 `<Answer>`，最后输出 `<Final subquestion>`、`<Important Features>` 和 `<Final Answer>`。一条推理轨迹表示为 `τ = {(q1,a1),...,(qT,aT)}`。

- **Expert-Guided MCTS**：
  - 节点表示部分推理轨迹状态，边表示新增子问题-答案对。
  - **Selection**：用 UCT 平衡探索与利用，选择下一个子问题。
  - **Expansion**：生成多个候选子问题及答案，若终止则输出预测 `(y,C)`。
  - **Simulation**：单步 rollout，用局部奖励评估候选子问题是否有用。
  - **Backpropagation**：回传累计奖励。

- **奖励设计**：
  - **分类奖励 `R_cls`**：结合预测概率、真实标签和阈值 margin bonus。
  - **注意力对齐奖励 `R_att`**：用 Jaccard 相似度衡量 LLM 提取的重要特征集合 `C` 与专家模型高亮特征 `C_exp` 的重合度：  
    `R_att = |C ∩ C_exp| / |C ∪ C_exp|`。
  - 总奖励：`R = λ·R_cls + (1-λ)·R_att`。

- **轨迹级 SFT**：  
  选取 MCTS 中 top-k 高奖励轨迹，训练 LLM 从原始临床问题生成完整推理轨迹，损失为负对数似然。

### 2.3 Stage 2：注意力对齐策略优化

- **注意力对齐奖励建模**：  
  继续使用 `R_cls` 和 `R_att` 的组合奖励，引导 LLM 关注专家认为临床显著的特征。

- **熵感知自适应上裁剪**：
  - 计算轨迹中关键临床 token 的平均预测熵 `H̄(τ)`。
  - 将熵通过 min-max 归一化映射到轨迹特定上裁剪界 `ε(τ) ∈ [ε_min, ε_max]`。
  - 论文实现中取 `ε_min = 0.2`，`ε_max = 0.4`。
  - 对高熵、不确定但可能信息丰富的轨迹放大学习信号，对过度自信轨迹限制更新。

- **RL 训练**：  
  基于 GRPO 风格目标，采用非对称裁剪：下界固定为 `ε`，上界为轨迹自适应的 `ε(τ)`，优化 token 级重要性比率与优势的裁剪目标。

## 3. 实验设计

- **数据集**：
  - **MIMIC-IV**：ICU 去标识化 EHR 记录，2008–2019。
  - **TJH**：结构化住院数据，带临床注释。
  - 预处理包括时间聚合、LOCF 插补、患者级序列访问；至少两次访问，用最后一次访问预测。

- **任务 / Benchmark**：
  - **Mortality Prediction**：住院死亡预测。
  - **Readmission Prediction**：30 天再入院预测。
  - 评价指标：**AUROC** 和 **AUPRC**，尤其强调 AUPRC 在不平衡数据中的信息量。

- **对比方法**：
  - **Prompt-based**：Vanilla、Think then Answer、Question Decomposition。
  - **Training-based**：SFT、GRPO、DAPO；并与 EAG-RL 的 Stage-1 初始化做公平比较。
  - **开源 LLM / Backbone**：Qwen2.5-7B-Instruct、LLaMA3.1-8B-Instruct、Qwen2.5-3B-Instruct；并对比 HuatuoGPT-o1-7B、OpenBioLLM-8B、DeepSeek-R1-7B。
  - **专家模型 / 基线分析**：Concare、未训练 base 模型、Vanilla SFT 等用于鲁棒性和跨数据集分析。

## 4. 资源与算力

- 论文中**未明确说明**使用的 GPU 型号、数量、训练时长、显存、参数量或具体计算成本。
- 文中仅提供了代码链接：`https://github.com/devilran6/EAG-RL`。
- 因此无法从论文正文评估其训练开销、可复现性和实际部署成本。

## 5. 实验数量与充分性

- **主要实验**：
  - 表 1：在 TJH、MIMIC-IV 上对 3 个 backbone、3 类任务、多个基线进行 AUROC/AUPRC 比较。
  - 表 2：消融实验，包括 w/o Stage-1、w/o Stage-2、w/o `R_att`、w/o `ε(τ)`。
  - 表 3：与多个开源医学/推理 LLM 比较。
  - 图 3：特征顺序扰动鲁棒性实验，随机打乱 20%、40%、60%、100% 特征。
  - 图 4：MIMIC-IV 到 TJH 的跨数据集泛化实验。
- **充分性评价**：
  - 实验覆盖了多 backbone、多任务、消融、鲁棒性和 OOD 泛化，整体较充分。
  - 使用 bootstrap 100 次重采样报告均值和标准差，统计上较规范。
  - 在相同 Stage-1 初始化下比较 GRPO/DAPO，增强了 RL 阶段效果归因的公平性。
  - 但部分实验未说明随机种子数量、超参搜索范围和显著性检验；跨数据集泛化仅展示一个方向。

## 6. 论文的主要结论与发现

- EAG-RL 在多个 EHR 预测任务上平均提升 **14.62%**，在 AUPRC 上尤其明显。
- Stage-1 的专家引导 MCTS 轨迹初始化能有效提升 SFT 和后续 RL 表现。
- Stage-2 的注意力对齐 RL 和熵感知自适应上裁剪均带来显著增益；移除 Stage-2 的性能下降大于移除 Stage-1。
- 移除 `R_att` 后性能下降，说明专家注意力作为辅助监督有效。
- 移除 `ε(τ)` 后性能和鲁棒性下降，说明自适应探索机制重要。
- EAG-RL 对特征顺序扰动更鲁棒，并能从 MIMIC-IV 泛化到 TJH，优于 Concare、base 模型和 Vanilla SFT。
- 总体表明：LLM 可以通过专家注意力引导的 RL 学习更内在、可迁移的 EHR 推理策略。

## 7. 优点

- **方法创新性**：首次系统性地将专家 EHR 模型的注意力作为 LLM 的策略监督信号，用于增强 LLM 内在 EHR 推理。
- **两阶段设计合理**：先用专家引导 MCTS 构造高质量轨迹做 SFT 初始化，再用 RL 精调，缓解 RL 冷启动和样本效率问题。
- **奖励设计轻量且语义相关**：用 Jaccard 相似度对齐重要特征集合，避免直接对齐 LLM 注意力带来的计算开销和架构不匹配。
- **熵感知自适应裁剪**：根据轨迹不确定性动态调整上裁剪界，鼓励探索高熵但临床有意义路径，缓解熵崩塌。
- **实验较全面**：涵盖多数据集、多任务、多 backbone、消融、鲁棒性和跨域泛化。
- **公平比较意识**：RL 方法在相同 Stage-1 初始化下比较，较好隔离了强化学习阶段贡献。

##
