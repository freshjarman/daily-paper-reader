---
title: "ST-TPP: Learning Semi-Transductive Temporal Point Processes with Gromov-Wasserstein Barycentric Regularization"
title_zh: ST-TPP：基于Gromov-Wasserstein重心正则化的半转导时间点过程学习
authors: "Qingmei Wang, Tianyu Huang, Yujie Long, Yuxin Wu, Fanmeng Wang, Xi Sun, Junchi Yan, Hongteng Xu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39850/43811"
tags: ["query:tpp-es"]
score: 9.0
evidence: 半转导神经时间点过程结合聚类正则化进行事件序列预测
tldr: 真实事件序列的生成机制常呈异质性并蕴含聚类结构，但多数时间点过程模型独立处理每条序列，未利用聚类信息。本文提出半转导时间点过程ST-TPP，在最大化序列似然的同时学习序列聚类中心，并引入基于Gromov-Wasserstein重心正则化的数据核矩阵。实验显示协同训练序列簇能显著提升事件预测性能，为利用群组结构的时间点过程建模提供了新思路。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 真实事件序列生成机制异质并含聚类结构，而现有时间点过程模型独立处理序列，未利用该结构。
method: 提出半转导时间点过程，联合学习神经TPP与序列聚类中心，并用Gromov-Wasserstein重心正则化约束。
result: 协同训练序列簇后事件预测性能明显提升。
conclusion: 利用聚类结构的半转导建模为时间点过程预测提供了有效增强。
---

## Abstract
The generative mechanisms behind real-world event sequences are often heterogeneous, leading to data that possesses inherent clustering structures.
However, most existing temporal point processes (TPPs) treat different event sequences independently, without leveraging the clustering structures when predicting events.
In this study, we design and learn a novel semi-transductive temporal point process (ST-TPP), which explicitly improves prediction performance by co-training sequence clusters. 
In particular, given a set of event sequences, our method learns a neural TPP together with cluster centers of the sequences.
Besides maximizing the likelihood of the event sequences, we leverage a data-based kernel matrix and prior knowledge to regularize the sequence embeddings, leading to a Gromov-Wasserstein barycentric (GWB) regularizer.
Based on the optimal transport plans associated with the GWB regularizer, we derive the cluster centers by the push-forward of the sequence embeddings.
When a new sequence comes, the learned model first assigns a cluster center to the sequence and then jointly encodes the sequence and the cluster center to predict future events, leading to a semi-transductive prediction scheme.
Experiments demonstrate that ST-TPP achieves competitive sequence clustering results and strong prediction performance.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：真实世界事件序列（如患者入院、员工跳槽、用户行为）通常由异质生成机制产生，数据本身蕴含聚类结构。然而，绝大多数时间点过程（TPP）模型将不同事件序列独立处理，预测事件时未利用序列间的聚类信息。
- **核心问题**：如何将序列聚类结构有效融入事件预测，而非仅做转导式聚类或训练多个TPP混合模型？
- **现有方法局限**：
  - 谱聚类等转导方法不建模生成机制，无法用于事件预测。
  - TPP混合模型复杂度随聚类数线性增长，且需学习多个TPP，易过拟合；预测时退化为单TPP，未充分利用聚类信息。
- **论文含义**：提出半转导时间点过程（ST-TPP），在最大化序列似然的同时学习序列聚类中心，并通过Gromov-Wasserstein重心（GWB）正则化约束序列嵌入，使预测同时利用目标序列的归纳嵌入与训练集的转导聚类信息。

## 2. 方法论

### 2.1 核心思想
- ST-TPP由**序列编码器**和**神经强度预测器**组成，并维护 \(K\) 个可学习的聚类中心。
- 训练时：联合优化MLE损失与GWB正则项，基于最优传输计划通过推前操作得到聚类中心。
- 测试时：新序列先分配最近聚类中心，再联合事件级、序列级、聚类级嵌入预测未来事件，形成半转导预测范式。

### 2.2 关键技术细节

- **序列编码器**：
  - 对序列 \(s=\{(t_n,c_n)\}_{n=1}^N\) 得到事件级嵌入 \(\{h_n\}_{n=1}^N = g(s)\)。
  - 通过均值池化得到序列级嵌入 \(h(t)=\text{MeanPooling}(\{h_n\}_{t_n\le t})\)。
  - 聚类中心矩阵 \(A=[a_1,\dots,a_K]^\top\in\mathbb{R}^{K\times D}\)，对任意序列嵌入 \(h(t)\)，分配最近中心 \(a(t)=\arg\min_{a\in\{a_k\}}\|h(t)-a\|^2\)。

- **神经强度预测器**：
  - 联合三类嵌入与时间间隔建模强度：
    \[
    \lambda(t')=f(\text{Concat}(h_N,\underbrace{h(t')}_{\text{归纳}},\underbrace{a(t')}_{\text{转导}}),t'-t_N)
    \]
  - 其中 \(h_N\) 为最近事件嵌入，\(h(t')\) 捕捉长程依赖，\(a(t')\) 引入相似训练序列信息。
  - 事件类型预测：\(c^*=\arg\max_{c\in C}\lambda_c(t')\)。

- **Gromov-Wasserstein重心正则化（GWB）**：
  - 由序列嵌入构造高斯核矩阵 \(K\)，由序列距离构造数据核矩阵 \(\tilde K\)，并引入单位阵 \(I_K\) 作为聚类先验。
  - 正则项：
    \[
    \text{GWB}(K)=\underbrace{GW_2^2(K,\tilde K)}_{\text{数据驱动}}+\underbrace{GW_2^2(K,I_K)}_{\text{聚类先验}}
    \]
  - 第一项鼓励嵌入核继承序列距离相似性；第二项施加聚类结构先验，使嵌入趋向 \(K\) 类。
  - 最优 \(K\) 为 \(\tilde K\) 与 \(I_K\) 的GW重心。

- **推前操作得到聚类中心**：
  - 用近端梯度算法计算GW距离及最优传输计划 \(T_1^*,T_2^*\)。
  - 聚类中心由序列嵌入加权平均得到：
    \[
    A=(M T_2^*)^\top H
    \]
  - 权重矩阵元素可解释为给定聚类下序列的条件概率。
  - 为降低复杂度，按批次计算并平均：\(A\approx \frac{1}{I}\sum_i A^{(i)}\)。

- **学习算法**：
  - 总体目标：
    \[
    \min_{\theta=\{g,f,A\}} \left(-\sum_{m=1}^M \log L(s_m;\theta)+\tau \text{GWB}(K;\theta)\right)
    \]
  - 交替优化：每轮用SGD更新 \(\{g,f\}\)，再用推前操作更新 \(A\)。
  - 复杂度可控：批内GW相关开销约为 \(O(BL^2+B^2L+BK^2+B^2K)\)。

## 3. 实验设计

- **数据集**：
  - 合成数据：由Hawkes过程与In&Ex过程生成，含2个序列簇，共58,000条序列，最大50事件。
  - 真实数据：Taobao（17类，2000序列，最大64事件）、StackOverflow（22类，2200序列，最大100事件）、Taxi（10类，2000序列，最大38事件）、Amazon（16类，8300序列，最大94事件）。

- **Benchmark与对比方法**：
  - 单TPP的MLE学习。
  - 当前最优TPP混合模型（Zhang et al. 2022）。
  - Backbone包括：ODETPP、RMTPP、SAHP、THP、AttNHP。
  - 将半转导范式应用于各backbone，得到ST-ODETPP、ST-RMTPP、ST-SAHP、ST-THP、ST-AttNHP。

- **评价指标**：
  - 数据拟合：每事件对数似然（ELL）。
  - 事件类型预测：准确率（ACC）。
  - 聚类性能（仅合成数据有标签）：NMI、ARI。
  - 定性评估：序列级嵌入的t-SNE可视化。

- **主要实验组**：
  - 表2：5个数据集 × 5个backbone及其ST版本的预测与聚类对比。
  - 图3：THP vs ST-THP、RMTPP vs ST-RMTPP的t-SNE嵌入可视化。
  - 图4：GWB正则权重 \(\tau\) 的影响。
  - 表3：不同正则器组合（MLE+GWB+CE、MLE+GWB、MLE+CE、MLE）。
  - 表4：不同层级嵌入（事件+序列+聚类、事件+聚类、事件+序列、仅事件）的影响。
  - 图5：核矩阵采样率对运行时间和性能的影响。

## 4. 资源与算力

- 论文明确提到：“All experiments are run on a server with **two 3090 GPUs**”。
- 每个方法记录**三次试验的平均性能与标准差**。
- **未明确说明**：总训练时长、单次训练耗时、GPU小时数、模型参数量、能耗等细节。图5(a)给出了不同采样率下的每epoch运行时间趋势，但未给出绝对训练总时长。

## 5. 实验数量与充分性

- **实验数量**：
  - 主对比实验覆盖5个数据集、5种backbone及其ST变体，共约50组预测/聚类结果。
  - 消融实验包括：正则器组合4组、嵌入层级4组、\(\tau\) 影响多组、采样率4组、t-SNE可视化2组。
  - 整体实验规模较大，覆盖合成与真实场景。
- **充分性与公平性**：
  - 多backbone验证了方法的通用性；三次试验平均并报告标准差，增强了结果可信度。
  - 超参数基于EasyTPP默认设置，比较相对公平。
  - 合成数据有真实聚类标签，可定量评估聚类；真实数据无聚类标签，仅能定性展示t-SNE。
  - 合成数据仅含2个簇，聚类评估场景较简单；真实数据聚类性能缺乏定量指标。
  - 未与更多专门的事件序列聚类方法或半监督/转导TPP方法进行直接比较。

## 6. 主要结论与发现

- ST-TPP在所有数据集上均能提升各backbone的事件预测性能（ELL与ACC）。
- 在合成数据上，ST-TPP同时提升聚类指标NMI与ARI，说明GWB正则化有助于学习结构化序列嵌入。
- t-SNE显示ST-TPP的序列嵌入具有更清晰的簇分离结构，可解释性增强。
- GWB正则化与交叉熵（CE）正则化兼容，联合使用效果最佳；GWB更侧重提升聚类结构，CE更侧重预测。
- 序列级与聚类级嵌入均对预测有贡献，联合使用效果最好。
- 核矩阵采样率较小时仍能保持稳定性能，运行时间随核大小二次增长，验证了方法的可扩展性。

## 7. 优点

- **范式创新**：提出半转导TPP预测范式，将归纳式序列嵌入与转导式聚类信息结合，弥补现有TPP忽略聚类结构的空白。
- **正则化设计合理**：GWB正则化同时利用数据核与聚类先验，且通过GW距离避免核矩阵行列对齐问题，兼容SGD与批训练。
- **聚类中心可解释**：通过推前操作从最优传输计划导出聚类中心，权重具有条件概率解释。
- **通用性强**：可嵌入多种现有TPP backbone，实验验证了RMTPP、SAHP、THP、ODETPP、AttNHP等。
- **实验较全面**：多数据集、多backbone、多指标、消融与可视化结合，报告三次试验标准差。
- **计算可控**：通过批内计算与核采样近似，降低GW距离的高计算成本。

## 8. 不足与局限

- **聚类数 \(K\) 需预先设定**：真实场景中聚类数未知，论文仅在[5,10]经验范围内设定，缺乏自适应确定 \(K\) 的机制。
- **GW距离计算复杂度仍较高**：尽管批处理与采样缓解，但大规模序列下扩展性仍受限制；论文也指出未来需更高效算法。
- **真实数据聚类评估不足**：真实数据集无聚类标签，仅用t-SNE定性展示，无法定量验证聚类质量。
- **合成数据聚类场景简单**：仅含2个簇，难以充分反映复杂异质生成机制下的聚类能力。
- **预测任务覆盖有限**：主要评估事件类型预测（ACC）和似然（ELL），未单独评估事件时间预测或长期预测性能。
- **资源与效率报告不完整**：未给出总训练时长、GPU小时、参数量等，难以评估实际部署成本。
- **超参数敏感性**：带宽 \(\sigma\)、\(\tau\)、采样率 \(r\) 等对性能有影响，论文虽做了部分分析，但实际应用中调参成本可能较高。
- **公平性潜在偏差**：基线混合模型与ST-TPP使用不同训练策略，虽在默认设置下比较，但未必完全等价。

（完）
