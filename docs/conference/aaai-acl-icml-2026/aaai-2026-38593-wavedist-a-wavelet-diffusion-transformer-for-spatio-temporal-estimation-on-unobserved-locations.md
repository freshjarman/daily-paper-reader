---
title: "WaveDiST: A Wavelet Diffusion Transformer for Spatio-Temporal Estimation on Unobserved Locations"
title_zh: WaveDiST：面向未观测位置时空估计的小波扩散Transformer
authors: "Huiling Qin, Yuanxun Li, Weijia Jia"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38593/42555"
tags: ["query:tpp-es"]
score: 5.0
evidence: 面向时空估计的扩散点过程
tldr: 该工作针对缺乏历史参考的新颖或未观测位置状态难以估计的问题，这些区域只能借助地理空间中相似节点推断。作者在高频空间引入扩散点过程，构建鲁棒的时空扩散Transformer用于城市级估计。方法突破了简单的点或区块插补，实现跨空间节点的状态估计。其贡献在于将点过程与扩散生成结合用于时空估计，与时空点过程建模主题存在方法关联。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 新颖或未观测位置缺乏历史数据，只能依靠地理空间相似节点推断，简单插补方法难以胜任。
method: 在高频空间引入扩散点过程，构建小波扩散Transformer进行鲁棒的时空状态估计。
result: 方法实现超越点或区块插补的时空估计，支持城市级时空感知与未观测节点状态推断。
conclusion: 将扩散点过程用于时空估计，为时空点过程相关任务提供了可迁移的生成式方法。
---

## Abstract
Spatio-temporal estimation plays a vital role in numerous scientific and engineering tasks, particularly for novel or unobserved locations lacking historical references. Many areas remain unobserved by sensors due to their non-core location or pending development status. The states of these areas can only be estimated through similar nodes in the geospace, rather than through historical data with temporal trends. Estimating these unobserved node states is crucial for city-wide spatio-temporal sensing and urban development, extending beyond simple point or block data imputation. In this study, we introduce a diffusion point process in high-frequency space to develop a robust spatio-temporal diffusion transformer for urban estimation where partial historical reference data is lacking. Our approach decomposes spatio-temporal data into high and low-frequency components through wavelet transform, and trains a diffusion model of spatial temporal data with a transformer that operates on high frequency signals. We incorporate low-frequency signals as diffusion conditions in the transformer architecture to capture overall spatio-temporal profiles and gradual trends. To enhance the learning of each step, we design an diffusion model featuring a spatio-temporal attention module that adaptively captures interdependencies between time and space. Extensive experiments across diverse domains including traffic, economics, and environment demonstrate that our method significantly outperforms state-of-the-art baselines.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义（研究动机与背景）

- **研究问题**：如何估计**未观测位置**的时空状态，尤其是这些位置缺乏历史参考数据、无法利用传统时间趋势插补的情况。
- **背景动机**：
  - 城市传感器部署成本高，只能覆盖主要路段或核心区域，导致大量区域“未观测”。
  - 这些区域的状态只能借助地理空间中相似或相邻节点推断，而不是依赖自身历史序列。
  - 该任务对城市交通管理、商业选址、环境监测等具有重要意义，超越普通点/块缺失值插补。
- **核心挑战**：
  - **数据稀疏**：观测节点少，空间覆盖有限。
  - **采样噪声**：传感器数据受人为、通信等因素干扰，方差大。
  - **缺乏历史参考**：未观测区域没有历史序列，不能直接建模时间趋势。
  - **复杂时空模式**：城市节律、人类活动和发展模式带来高度异质时空依赖。
- **整体含义**：论文试图把“未观测位置估计”建模为基于部分观测时空图的条件生成/重建问题，并强调从稀疏、噪声数据中恢复城市级完整时空状态。

## 2. 方法论：核心思想与关键技术

### 核心思想
- 通过**小波变换**将时空信号分解为多个高频分量和一个低频分量。
- 在高频空间进行**条件扩散建模**，因为噪声通常集中在高频；低频分量作为条件，提供整体趋势和稳定约束。
- 使用**时空扩散 Transformer**，在反向去噪过程中同时建模时间依赖和空间依赖，并直接估计原始时空数据而非只估计噪声。

### 关键技术细节

- **小波分解与去噪依据**：
  - 对时空序列做 J 级小波分解，得到高频分量 \(x^{h_1},...,x^{h_J}\) 和低频分量 \(x^l\)。
  - 论文引用小波去噪理论：白噪声能量更多分布在高频子带，信号趋势主要保留在低频，因此在高频空间扩散有助于去噪。

- **高频空间条件扩散**：
  - 前向过程只对高频分量加噪，低频分量不参与加噪。
  - 前向公式可理解为：\(x_k^{h_j} = \sqrt{\bar{\alpha}_k}x_0^{h_j} + \sqrt{1-\bar{\alpha}_k}\epsilon\)。
  - 反向过程以噪声高频状态和低频条件 \(x^l\) 为条件，学习 \(p_\theta(\hat{X}_{k-1}|\tilde{x}^h_k,x^l)\)。
  - 与常规扩散不同，模型直接估计干净的原始时空数据 \(\hat{X}\)，而不是估计高斯噪声，因为任务本质是重建/估计。
  - 低频条件的作用：保持整体趋势、加速收敛、降低重建方差。

- **WaveDiST 架构**：
  - **输入编码**：高频分量经维度变换对齐到原序列长度，拼接为通道；加入时间正弦位置编码和空间可学习位置编码。
  - **条件编码**：去噪步 \(k\) 经正弦嵌入和 MLP 编码；低频分量 \(x^l\) 经 MLP 映射；二者相加形成条件嵌入。
  - **时空注意力模块**：
    - **时间注意力**：对每个节点在时间维度做自注意力，学习城市状态随时间演化。
    - **空间注意力**：引入图注意力，邻接矩阵 \(A\) 定义信息流向，并屏蔽无效连接；用于未观测节点借助相邻节点推断。
    - **融合**：将时间注意力和空间注意力输出通过可学习投影融合为时空表示。
  - **条件扩散 Transformer 块**：
    - 采用类似 DiT 的 adaLN-Zero 机制。
    - 条件不仅包括去噪步 \(t\)，还包括低频信号 \(x^l\)。
    - 由 \([t;x^l]\) 生成自适应 LayerNorm 参数 \(\gamma,\beta\) 和缩放参数 \(\alpha\)，用于残差连接前调制。
  - **估计流程**：
    - 训练时随机丢弃一部分已观测节点，构造监督样本。
    - 损失只在原始观测节点和人工丢弃节点上计算：
      \[
      L=M\odot\|X-\hat{X}\|_2^2+M_{drop}\odot\|X-\hat{X}\|_2^2
      \]
    - 评估用的真实缺失点不参与监督，避免信息泄漏。

## 3. 实验设计

- **数据集/场景**：5 个跨领域基准数据集：
  - **Jinan Taxi**：交通。
  - **Jinhua Sales**：经济/销售。
  - **Beijing Air**：环境/空气质量。
  - **METR-LA**：交通。
  - **PEMS08**：交通。
- **任务设定**：部分观测时空数据估计，通过随机屏蔽空间节点模拟未观测位置；指标为 **MAE** 和 **RMSE**。
- **对比方法**：
  - 时间序列类：Transformer、TimeMixer、TimesNet、CSDI、SAITS。
  - 时空类：ImputeFormer、FreTS、STEMGNN。
  - 表中还包含 GPVAE。
- **消融与变体**：
  - w/o diffusion：去掉扩散过程。
  - w/o encoder：仅用 decoder-only 架构。
  - w/o wavelet：不进行小波分解，直接对原始数据扩散。
  - w/o condition：去掉反向扩散中的条件。
  - 小波基比较：db1、db2、db4。
- **鲁棒性实验**：
  - 在 Jinan Taxi 和 Beijing Air 上测试 30%–70% 缺失率。
  - 对比 SAITS、ImputeFormer、TimeMixer。
- **时空案例分析**：
  - 济南交通速度空间估计与真实值对比。
  - 北京 PM2.5 两个月时间序列估计。
  - 济南出租车速度一周时间序列估计，观察去噪和平滑效果。

## 4. 资源与算力

- **论文未明确说明**使用的 GPU 型号、GPU 数量、训练时长、参数量或推理成本。
- 致谢中提到北京师范大学珠海校区“Interdisciplinary Intelligence Super Computer Center”，但未给出具体算力配置。
- 因此，无法从正文判断
