---
title: Cortical encoding of probabilistic temporal predictions during speech perception
title_zh: 言语感知中概率性时间预测的皮层编码
authors: "Deyna, L., Albouy, P., Trebuchon, A., Schon, D., Morillon, B., Guilleminot, P. H."
date: 2026-08-20
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.16.745095v1.full.pdf"
tags: ["query:tpp-es"]
score: 9.0
evidence: 利用RNN与风险率模型预测语言单位起始时间的概率时间结构，属于连续时间事件预测与强度估计
tldr: 传统语音时间结构研究仅关注语言单位的平均发生速率，忽略了上下文相关的概率性时间结构。本文利用大型语料库训练RNN模型预测音素、音节和词的出现时刻，并记录53名患者颅内电生理活动。结果发现RNN预测优于均值率和风险率模型，且其连续概率显著解释神经活动，与语言内容编码分离。该工作确立了语音时间预测是动态、上下文依赖且可独立编码的概率过程。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 851, \"height\": 1120, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1150, \"height\": 1138, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1754, \"height\": 1178, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1626, \"height\": 1145, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1166, \"height\": 1149, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1399, \"height\": 1279, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1802, \"height\": 687, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 571, \"height\": 424, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 556, \"height\": 501, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 815, \"height\": 799, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1777, \"height\": 1015, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1799, \"height\": 793, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1723, \"height\": 1227, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1797, \"height\": 836, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1813, \"height\": 696, \"label\": \"Table\"}, {\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-08-16-745095-v1/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1886, \"height\": 858, \"label\": \"Table\"}]"
motivation: 传统研究仅关注语言单位的平均发生率，忽略了语音中上下文相关的概率性时间结构，未能揭示时间预测的神经基础。
method: 利用大型法语/英语语料库训练RNN预测音素、音节和词的起始时刻，并在53名患者颅内电生理数据中检验预测概率对神经活动的解释力。
result: RNN预测显著优于均值率和风险率模型；预测概率较强地解释神经活动，且与语言内容编码在通道群体上分离。
conclusion: 语音时间预测是动态、上下文依赖的概率过程，其皮层编码独立于语言内容，并涉及颞叶至额叶/感觉运动区的网络。
---

## 摘要
言语的时间结构传统上通过其典型语言单位（音素、音节、单词）的节奏性来表征，每个单位均以平均发生频率概括。虽然这一观点有效，但它忽略了言语是否携带更精细的、依赖于情境且具有概率性的时间结构，这种结构可能支持听觉过程中的时间预测编码。利用大型法语和英语语料库，我们训练了复杂度递增的模型来预测语言单位的起始时刻。递归神经网络（RNN）优于平均速率和风险率模型，表明这些速率周围的变异性并非噪声，而是一种由局部情境塑造、在音素、音节和单词层面均可统计预测的时间结构。通过记录53名神经外科患者聆听自然言语时的7,698个脑内电极信号，我们进一步证明，模型的输出（即即将到来的起始事件的连续概率“何时”）能够解释超越声学与语言内容（“什么”）特征的神经活动，且RNN的效应显著强于平均速率或风险率模型。这种关于“何时”发生起始事件的动态神经预测可与语言内容的编码相分离，依赖于显著不同的通道群体。时间预测涉及一个分布式的皮层网络，从双侧颞叶皮层延伸到左额叶和感觉运动区域。总之，这些结果确立了言语中的时间预测本质上是一个动态、依赖情境且具有概率性的过程。

## Abstract
The temporal structure of speech has traditionally been characterized by the rhythmicity of its canonical linguistic units (phonemes, syllables, words), each summarized by a mean occurrence rate. While valid, this view overlooks whether speech carries a finer, context-dependent and probabilistic temporal structure that could support temporal predictive coding during listening. Using large French and English speech corpora, we trained models of increasing complexity to predict the onsets of linguistic units. Recurrent neural networks (RNNs) outperform mean-rate and hazard-rate models, showing that the variability around these rates is not noise but a temporal structure shaped by local context, statistically predictable across phonemes, syllables and words. Recording from 7,698 intracerebral electrodes in 53 neurosurgical patients listening to natural speech, we next show that the models' output), the continuous probability of an upcoming onset (when), explains neural activity beyond acoustic and linguistic content (what) features, with markedly stronger effects for RNNs than for mean- or hazard-rate models. This dynamic neural prediction of when an onset will occur is dissociable from the encoding of linguistic content, relying on largely distinct channel populations. Temporal predictions engage a distributed cortical network extending from bilateral temporal cortex into left frontal and sensorimotor regions. Together, these results establish temporal prediction in speech as a dynamic, context-dependent and probabilistic process in its own right.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：传统言语时间结构研究以典型语言单位（音素、音节、单词）的**平均发生频率**（节奏性）来表征，默认发生速率附近的变异性是噪声。
- **核心问题**：言语是否携带更精细的、**上下文依赖且具有概率性**的时间结构？这种结构能否为听觉过程中的**时间预测编码**提供神经基础？
- **整体含义**：若得到证实，则言语时间预测本质上是一个**动态、情境依赖的概率过程**，可作为独立于语言内容的神经编码维度，这挑战了将时间结构仅视为节奏统计量的传统观点，并将时间预测确立为言语感知中的独立认知-神经过程。

## 2. 方法论

- **核心思想**：用复杂度递增的统计/学习模型预测语言单位（音素、音节、单词）的起始时刻，将预测概率作为“何时（when）”发生的连续信号，检验其能否解释颅内神经活动，并与“什么（what）”（声学、语言内容）的编码分离。
- **关键技术细节**：
  - 训练**循环神经网络（RNN）**在大型法语和英语口语语料库上学习局部上下文→单位起始时间的映射。
  - 对比基线模型：**平均速率模型**（恒定速率泊松过程）和**风险率模型**（hazard-rate，基于全局间隔分布的条件瞬时速率）。
  - 模型输出为即将到来的起始事件的**连续概率**，即时间预测信号。
  - 颅内电生理记录：53名神经外科患者、7,698个脑内电极，聆听自然言语。
  - 统计验证：以模型输出作为回归量解释神经活动，并控制声学与语言内容特征。
- **算法流程（文字说明）**：
  1. 从语料库提取各语言单位起始时间标注。
  2. 用均值率/风险率模型计算基线预测概率。
  3. 用RNN学习基于上下文的一步预测概率分布。
  4. 对每位患者的每个电极建立编码模型，考察时间预测概率对高频神经活动的解释增量。
  5. 通过对比不同模型解释力、控制“what”类特征、比较通道群体重叠度来评估时间预测的独立性与特异性。

## 3. 实验设计

- **语料层面**：
  - 大型**法语和英语**口语语料库（来自自然语音），用于训练和评估预测模型。
- **神经数据层面**：
  - 53名神经外科癫痫患者植入的**7,698个颅内电极**，采集自然言语聆听时的电生理信号。
- **基准与对比**：
  - RNN vs. 平均速率模型 vs. 风险率模型
  - 时间预测信号 vs. 声学/语言内容特征（“what” vs. “when”）
  - 语言单位层面：音素、音节、词三类分别评估
- **分析维度**：
  - 模型预测性能比较（预测时间起始的准确性）
  - 神经编码模型（预测概率解释神经活动的增量方差）
  - 通道群体分离性分析（时间预测通道 vs. 内容编码通道）
  - 皮层网络分布图谱

## 4. 资源与算力

- 论文在提供的元数据与摘要文本中**未明确报告**所用GPU型号、数量、训练时长、参数规模等算力信息。
- 仅可推断：语料库规模为“大型”双语自然语料，RNN训练与7,698个电极的神经编码建模均属中等计算量任务，但具体算力细节缺失。

## 5. 实验数量与充分性

- **实验数量**：
  - 两个语言（法语、英语）的模型训练与评估。
  - 三种复杂度的模型对比（均值率、风险率、RNN）。
  - 三类语言单位（音素、音节、词）的预测与神经分析。
  - 大规模颅内验证（53名患者、7,698个电极）。
  - “what vs. when”分离性分析、通道群体重叠检验、皮层分布分析。
- **充分性与客观性**：
  - 样本量大、多语言、多粒度、多模型对比，设计较全面。
  - 控制声学与语言内容特征，验证了时间预测的**增量解释力**，具有较好的严谨性。
  - 客观性较好：颅内记录为直接神经证据，模型对比采用了统一基准。
  - 不足：缺乏消融实验细节（如RNN架构变体、训练数据量影响）、跨语言普适性仅覆盖两种印欧语系语言，且缺少行为实验佐证。

## 6. 主要结论与发现

- RNN**显著优于**平均速率与风险率模型，表明单位间隔的变异性**并非噪声**，而是由局部情境塑造的、可统计预测的**概率性时间结构**。
- 模型的“何时”预测信号能在**声学与语言内容之外**显著解释神经活动，且RNN的效应**显著强于**基线模型。
- 时间预测的神经编码与语言内容编码**可分离**，依赖于**显著不同的通道群体**。
- 时间预测涉及一个**分布式皮层网络**：从**双侧颞叶皮层**延伸至**左额叶与感觉运动区域**。
- 核心结论：言语中的时间预测是**动态、上下文依赖、概率性的独立神经过程**。

## 7. 优点

- **大规模高密度颅内记录**：7,698个电极、53名患者，统计功效高、空间覆盖广。
- **多语言验证**：法语+英语双语语料，提升结论普适性。
- **模型设计层次清晰**：均值率→风险率→RNN，由简到繁，直接回答“时间变异是否为可预测结构”的问题。
- **干净的“what vs. when”分离策略**：在控制内容特征后检验时间预测的增量解释力，逻辑严谨。
- **生态效度高**：使用自然言语而非人工刺激。
- **多粒度分析**：同时对音素、音节、词三个层级建模，结论具有跨层级一致性。

## 8. 不足与局限

- **算力与实现细节缺失**：未报告GPU、训练时间、模型结构超参数，复现难度较大。
- **语言覆盖有限**：仅法语、英语两种同语系语言，对非印欧语（如声调语言、节奏类型差异大的语言）普适性未知。
- **样本偏差**：颅内数据来自神经外科患者（多为药物难治性癫痫），大脑可能存在病理重塑性影响，需谨慎推广到健康人群。
- **语料偏差风险**：RNN预测依赖语料库统计特征，语料领域、口音、录音条件可能影响模型与后续神经分析。
- **缺乏行为验证**：未证明该时间预测信号与实际感知行为（如反应时、理解准确性）直接相关。
- **缺少因果性证据**：结果以编码模型相关性为主，未通过刺激操控或干预手段证明皮层活动对时间预测的因果必要性。
- **通道分离为统计层面的群体差异**，未提供解剖-功能连接上的机制解释。

（完）
