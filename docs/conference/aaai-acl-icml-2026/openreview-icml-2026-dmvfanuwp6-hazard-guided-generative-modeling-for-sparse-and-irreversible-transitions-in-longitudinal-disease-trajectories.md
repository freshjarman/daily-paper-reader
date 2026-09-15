---
title: Hazard-Guided Generative Modeling for Sparse and Irreversible Transitions in Longitudinal Disease Trajectories
title_zh: 面向纵向疾病轨迹中稀疏且不可逆转移的风险引导生成建模
authors: "Hyuna Cho, Hayoung Ahn, Guorong Wu, Won Hwa Kim"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/3599eb97b3ebc4b3f9540fb5a4db23f920d6573a.pdf"
tags: ["query:ehr-es"]
score: 8.0
evidence: 面向疾病轨迹生成的神经ODE生成模型
tldr: 该工作针对纵向疾病进展数据稀疏、临床意义重大的不可逆状态转移稀缺且被欠表达，而现有生成模型忽视患者协变量与标签随时间演化的问题。作者提出NOHA，一种基于神经ODE的条件生成模型，并结合风险引导的轨迹采样策略来捕捉罕见转移。方法能够对疾病状态转移进行数据合成而非仅统计推断，生成更具临床意义的患者轨迹。其贡献在于将连续时间建模与生成式合成结合，服务于临床时间序列的轨迹生成。
source: ICML-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 纵向疾病进展数据稀疏，关键的不可逆状态转移罕见且被欠表达，现有生成模型还忽视协变量的时间演化。
method: 提出基于神经ODE的条件生成模型NOHA，采用风险引导的轨迹采样来建模并合成疾病状态转移。
result: 方法能够生成更具临床意义的疾病轨迹，优于将时间点一视同仁的传统生成与状态转移模型。
conclusion: 将连续时间生成建模用于患者轨迹合成，为临床时间序列生成提供了新范式。
---

## Abstract
Understanding longitudinal disease progression is challenging due to sparse and irregular data acquisition. Moreover, clinically meaningful disease-state transitions are rare and irreversible, leading to underrepresentation of critical progression events. Existing generative models often overlook such transitions by treating all time points uniformly, while traditional state-transition models focus on statistical inference rather than data synthesis. In addition, both paradigms disregard the temporal evolution of patient covariates and labels, treating them as static factors. To address these limitations, we propose a Neural ODE-based conditional generative model with Hazard-guided trajectory sampling (NOHA). By integrating continuous-time Markov chain with Neural ODE, NOHA effectively models time-varying transition risks and non-linear, irreversible disease dynamics. Our hazard-guided sampling strategy estimates temporal transition hazards to prioritize critical transition events during data synthesis. Moreover, NOHA jointly generates disease trajectories, labels, and patient attributes, ensuring clinically consistent temporal dynamics. Experimental results on four biomarkers from two neurodegenerative disease datasets demonstrate that NOHA generates high-fidelity, progression-aware trajectories that significantly improve downstream disease progression prediction.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
面向疾病轨迹生成的神经ODE生成模型。

### 2. 核心内容
该工作针对纵向疾病进展数据稀疏、临床意义重大的不可逆状态转移稀缺且被欠表达，而现有生成模型忽视患者协变量与标签随时间演化的问题。作者提出NOHA，一种基于神经ODE的条件生成模型，并结合风险引导的轨迹采样策略来捕捉罕见转移。方法能够对疾病状态转移进行数据合成而非仅统计推断，生成更具临床意义的患者轨迹。其贡献在于将连续时间建模与生成式合成结合，服务于临床时间序列的轨迹生成。

### 3. 对应检索需求
generative models for patient trajectory generation from clinical time series。

### 4. 来源与原文
- Source：ICML-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=dmVFANUWP6](https://openreview.net/forum?id=dmVFANUWP6)
