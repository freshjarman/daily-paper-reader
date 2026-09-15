---
title: "Detecting the Future: All-at-Once Event Sequence Forecasting with Horizon Matching"
title_zh: 预测未来：基于时程匹配的一次性事件序列预测
authors: "Ivan Karpukhin, Andrey Savchenko"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39413/43374"
tags: ["query:tpp-es"]
score: 7.0
evidence: 基于匹配损失的长时程事件序列预测
tldr: 该工作针对事件序列预测中传统自回归多步策略易收敛为常量或重复输出、长时程效果差的问题。作者提出DEF方法，通过新颖的匹配损失在训练中让预测与真实事件最优对齐，实现对同一时程内多个未来事件的一次性同时预测。方法在零售、金融、医疗、社交网络等领域的长时程事件预测上取得新最优，显著提升准确性与多样性。其贡献在于为长时程事件序列预测提供了非自回归的高效建模范式。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 传统事件序列预测采用自回归多步策略，易收敛为常量或重复输出，长时程预测效果受限。
method: 提出DEF方法，用匹配损失在训练中让预测与真实事件对齐，实现同一时程内多事件的同时预测。
result: 在零售、金融、医疗、社交等领域的长时程事件预测上取得最优，显著提升准确性与多样性。
conclusion: 为长时程事件序列预测提供非自回归的高效范式，契合神经点过程长时程预测需求。
---

## Abstract
Long-horizon events forecasting is a crucial task across various domains, including retail, finance, healthcare, and social networks. Traditional models for event sequences often extend to forecasting on horizon using an autoregressive (recursive) multi-step strategy, which has limited effectiveness due to typical convergence to constant or repetitive outputs. To address this limitation, we introduce DEF, a novel approach for simultaneous forecasting of multiple future events on a horizon with high accuracy and diversity. Our method optimally aligns predictions with ground truth events during training by using a novel matching-based loss function. We establish a new state-of-the-art in long-horizon event prediction, achieving up to a 50% relative improvement over existing temporal point processes and event prediction models. Furthermore, we achieve state-of-the-art performance in next-event prediction tasks while demonstrating high computational efficiency during inference.

---

## 论文详细总结（自动生成）

# 论文总结：Detecting the Future: All-at-Once Event Sequence Forecasting with Horizon Matching

## 1. 核心问题与整体含义
- **研究背景**：事件序列广泛存在于零售、金融、医疗、社交网络等领域，其数据由带时间戳的事件类型/属性组成，具有不规则时间间隔和额外属性，区别于普通表格数据与规则时间序列。
- **核心任务**：长时程事件预测，即在给定最后观测事件后的时间窗口 \(H\) 内预测多个未来事件，而不仅是下一事件。
- **现有问题**：
  - 传统方法多采用自回归/递归多步预测，容易误差累积，并收敛为常量或重复输出。
  - 一次性预测多个未来事件的方法，如 GAN、Diffusion 等，常使用按位置对应的 pairwise loss，当预测与真实事件顺序/数量不一致时会产生错误匹配。
  - HYPRO 等长时程方法需要多次生成与筛选，训练和推理效率低。
- **论文含义**：作者提出 **DEF（Detection-based Event Forecasting）**，借鉴目标检测中的匹配思想，实现同一时程内多个未来事件的一次性、非自回归预测，在准确性与多样性上取得新 SOTA，同时保持较高推理效率。

## 2. 方法论
- **核心思想**：
  - 使用 backbone 提取历史事件嵌入，并通过 \(K\) 个预测头并行预测未来 \(K\) 个候选事件。
  - 训练时用 **horizon matching loss** 动态对齐预测事件与真实事件，而不是按固定位置强行对应。
  - 推理时根据事件发生概率过滤候选，再按预测时间排序输出。
- **预测头设计**：
  - 每个事件预测三部分：
    - 发生概率 \(\hat{o}\)：sigmoid 输出。
    - 标签分布 \(\hat{p}(l)\)：softmax 输出。
    - 时间偏移 \(\hat{t}\)：采用单位尺度 Laplace 分布，\(P(t)=\frac{1}{2}e^{-|t-\hat{t}|}\)，等价于 MAE 的概率解释。
  - 条件预测头架构：使用单个共享前馈网络，对 \(K\) 个可训练 query 向量与上下文向量拼接后生成 \(K\) 个输出，减少参数量、加速收敛并提升预测质量。
- **Horizon Matching Loss**：
  - 设预测序列为 \(\{\hat{y}_i\}_{i=1}^K\)，真实时程内事件为 \(\{y_i\}_{i=1}^T\)，\(T\) 可变。
  - 在所有可能对齐 \(\sigma\) 中寻找最小匹配代价：
    \[
    L_{\text{matching}}(y,\hat{y})=\min_{\sigma\in A}\left[\sum_{i=1}^T L_{\text{pair}}(y_i,\hat{y}_{\sigma(i)})+L_{\text{BCE}}(\sigma,\hat{y})\right]
    \]
  - 匹配使用 Hungarian 算法，计算复杂度为序列长度的三次方。
  - 成对损失：
    \[
    L_{\text{pair}}(y_i,\hat{y}_{\sigma(i)})=|t_i-\hat{t}_{\sigma(i)}|-\log \hat{p}_{\sigma(i)}(l_i)
    \]
  - 发生概率损失：
    \[
    L_{\text{BCE}}(\sigma,\hat{y})=-\sum_{i\in\sigma}\log\hat{o}_i-\sum_{i\notin\sigma}\log(1-\hat{o}_i)
    \]
  - 最终训练目标加入首头下一事件预测损失：
    \[
    L_{\text{DEF}}(y,\hat{y})=L_{\text{matching}}(y,\hat{y})+\lambda\left[|t_1-\hat{t}_1|-\log\hat{p}_1(l_1)\right]
    \]
    实验中 \(\lambda=4\)。
- **校准与推理**：
  - 由于发生概率 \(\hat{o}\) 偏向匹配频率，通常低于 0.5，模型会预测过少事件。
  - 训练时在线跟踪匹配频率并计算分位数，为各预测头确定阈值，使预测率与匹配概率对齐。
  - 推理步骤为：按 \(\hat{o}\) 过滤，再按预测时间排序。
- **关键超参数**：
  - \(K\) 通常设为时程内平均序列长度的约 4 倍，实验中取 32 到 64。
  - \(L_{\text{BCE}}\) 权重通常约为标签损失和时间损失的 8 倍；Retweet 等大时间步数据集需降低 MAE 损失权重。

## 3. 实验设计
- **Benchmark**：使用 **HoTPP benchmark** 评估长时程事件预测。
- **数据集**：5 个跨领域数据集：
  - StackOverflow、Amazon、Retweet、MIMIC-IV、Transactions。
  - 覆盖社交网络、医疗、金融等场景；序列数从 2k 到 120k，事件数从 138k 到 43.7M，类别数 3 到 203，平均长度 19.7 到 875。
- **评估指标**：
  - 长时程预测：**OTD**（越低越好）与 **T-mAP**（越高越好）。
  - 下一事件预测：时间 MAE 与类型错误率。
  - 预测多样性：预测标签分布熵。
  - 效率：训练与生成阶段的 Requests Per Second。
- **对比方法**：
  - IFTPP、IFTPP-T、RMTPP、NHP、AttNHP、ODE、HYPRO、Diffusion，以及本文 DEF。
  - DEF 使用 GRU 作为 backbone。
- **主要实验场景**：
  - 长时程预测：Table 2，5 个数据集上比较 OTD/T-mAP。
  - 下一事件预测：Fig. 5，比较时间 MAE 与类型错误率。
  - 预测多样性：Fig. 6，通过改变采样温度分析熵与 OTD 的权衡。
  - 计算效率：Fig. 7，比较训练与生成 RPS。
  - 扩展时程：Fig. 4，在 Transactions 上测试 DEF 的自回归扩展版本。

## 4. 资源与算力
- 论文正文脚注明确说明：实验在 **Nvidia RTX 4060 GPU** 上完成。
-
