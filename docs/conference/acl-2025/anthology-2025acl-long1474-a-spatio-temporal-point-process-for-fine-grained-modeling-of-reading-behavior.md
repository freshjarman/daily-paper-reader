---
title: A Spatio-Temporal Point Process for Fine-Grained Modeling of Reading Behavior
authors: "Francesco Ignazio Re, Andreas Opedal, Glib Manaiev, Mario Giulianelli, Ryan Cotterell"
date: 2025
pdf: "https://aclanthology.org/2025.acl-long.1474.pdf"
tags: ["query:TPP-ES"]
score: 10
source: ACL-2025-Long
selection_source: long-range
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
id: anthology-2025.acl-long.1474
canonical_id: "work:023166ccf93667172aafbf4f"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: complete
title_zh: 用于阅读行为细粒度建模的时空点过程
tldr: 阅读行为在空间与时间上交替发生注视与眼跳，但传统建模多依赖聚合眼动指标并施加强假设，忽略细粒度时空动态。本文提出基于标记时空点过程的阅读行为概率模型，用Hawkes过程刻画眼跳的时空激发，并将注视时长建模为跨时间卷积的预测因子以捕捉溢出效应。实验显示该模型对人类眼跳拟合优于基线，而引入上下文惊奇度仅带来边际预测提升。
motivation: 传统阅读眼动建模依赖聚合测量与强假设，忽略注视与眼跳的细粒度时空动态。
method: 提出标记时空点过程，用Hawkes过程建模眼跳激发，注视时长由跨时间卷积预测因子建模。
result: Hawkes模型对人类眼跳拟合优于基线；上下文惊奇度对注视时长预测仅边际提升。
conclusion: 惊奇度理论难以解释细粒度眼动，需更一般的时空点过程刻画阅读行为。
evidence: 面向时空点过程与眼动阅读建模交叉专题，提出Hawkes过程细粒度建模阅读行为。
reading_content_version: 1
reading_section: deep
---

## 摘要
阅读是一个在空间和时间中展开的过程，在注视与眼跳之间交替：注视时读者聚焦于空间中的某个特定点，眼跳时读者迅速将焦点转移到新的点。心理语言学的一个假设是，对读者的注视和眼跳进行建模可以揭示其在线句子加工过程。然而，此类建模的标准方法依赖于聚合的眼动测量数据和施加了强假设的模型，忽略了阅读过程中发生的大部分时空动态。在本文中，我们提出了一种更通用的阅读行为概率模型，基于带标记的时空点过程，不仅捕捉注视持续多长时间，还捕捉它们在空间中落在何处以及在时间中何时发生。眼跳使用霍克斯过程建模，该过程捕捉每一次注视如何激发在其时间和空间附近发生新注视的概率。注视事件的持续时间被建模为注视特异性预测因子在时间上卷积的函数，从而捕捉溢出效应。在实证上，我们的霍克斯过程模型对人类眼跳的拟合优于基线。关于注视持续时间，我们观察到将上下文惊奇度作为预测因子仅使模型的预测准确性有边际提升。这一发现表明，惊奇度理论难以解释细粒度的眼动。

## Abstract
Reading is a process that unfolds across space and time, alternating between fixations where a reader focuses on a specific point in space, and saccades where a reader rapidly shifts their focus to a new point. An ansatz of psycholinguistics is that modeling a reader's fixations and saccades yields insight into their online sentence processing. However, standard approaches to such modeling rely on aggregated eye-tracking measurements and models that impose strong assumptions, ignoring much of the spatio-temporal dynamics that occur during reading. In this paper, we propose a more general probabilistic model of reading behavior, based on a marked spatio-temporal point process, that captures not only how long fixations last, but also where they land in space and when they take place in time. The saccades are modeled using a Hawkes process, which captures how each fixation excites the probability of a new fixation occurring near it in time and space. The duration time of fixation events is modeled as a function of fixation-specific predictors convolved across time, thus capturing spillover effects. Empirically, our Hawkes process model exhibits a better fit to human saccades than baselines. With respect to fixation durations, we observe that incorporating contextual surprisal as a predictor results in only a marginal improvement in the model's predictive accuracy. This finding suggests that surprisal theory struggles to explain fine-grained eye movements.

## 专题评审

专题相关性评分：10/10。

论文直接构建标记时空点过程建模阅读行为事件。

---

## 论文详细总结（自动生成）

# 论文总结：A Spatio-Temporal Point Process for Fine-Grained Modeling of Reading Behavior

## 1. 核心问题与整体含义

- **研究动机**：阅读是认知复杂的过程，眼睛在**注视**（fixation，短暂停留以感知和处理语言材料）与**眼跳**（saccade，快速移动焦点）之间交替。心理语言学长期假设，对注视和眼跳建模可以揭示语言理解的认知过程。
- **核心问题**：传统眼动建模方法存在两大缺陷：
  - **聚合损失信息**：将原始扫视路径（scanpath）聚合为词级指标（如首次注视时长、凝视时长、总注视时长），在时间和空间维度上均丢失细粒度信息。例如，总注视时长混合了首次注视与回视，而聚合依赖预定义的兴趣区（通常为词级），无法研究音节、词素等更小单位。
  - **强假设与认知/眼动控制混淆**：标准线性模型或GAM施加了强假设，且聚合指标倾向于混淆认知加工（如词汇通达）与眼动控制（如生理延迟）两类过程。
- **整体含义**：作者主张采用**统一的概率框架**，同时建模注视的**何时发生、落在何处、持续多久**，以更忠实地刻画阅读的时空动态，并重新审视惊奇度理论（surprisal theory）在细粒度眼动层面的解释力。

## 2. 方法论

### 2.1 核心思想
- 将阅读行为建模为**带标记的时空点过程**（marked spatio-temporal point process），交替生成眼跳与注视。
- 扫视路径定义为注视三元组序列 \( \mathcal{T} = \{(t_n, s_n, d_n)\}_{n=1}^N \)，分别对应起始时间、空间位置和持续时间。
- 模型分两个组件：
  - **时空点过程** \( f(t_n, s_n \mid \mathcal{H}_{n-1}) \)：建模注视的起始时间与空间位置。
  - **持续时间分布** \( g(d_n \mid \mathcal{H}_{n-1}, t_n) \)：建模注视时长（标记）。
- 采样流程迭代三步：(a) 采样注视起始时间与位置；(b) 采样注视时长；(c) 更新历史，直至达到预设阅读时间范围。

### 2.2 关键技术细节

**（1）眼跳建模：时空霍克斯过程**
- 强度函数为：
  \[
  \lambda(t_n, s_n; \mathcal{H}_{n-1}) = \nu + \sum_{m=1}^{n-1} \phi_m(t_n - t_m - \delta(n,m)) \, \psi_m(s_n)
  \]
  其中 \(\nu\) 为基础强度，\(\phi_m\) 为时间衰减核，\(\psi_m\) 为空间密度，\(\delta(n,m)\) 为累积注视时长（确保核只捕捉眼跳间隔）。
- **时间核**：指数衰减形式 \(\phi_m(\Delta) = h(x_m^\top \alpha)\exp(-h(x_m^\top \beta)\cdot \Delta)\)，其中 \(h\) 为非负函数（如ReLU）。\(h(x_m^\top \alpha)\) 表示激发强度，\(h(x_m^\top \beta)\) 表示衰减速率，二者均可依赖注视特异性预测因子。
- **空间密度**：以变换后的位置 \(\mu_m(s_m)\) 为中心的二元球面高斯：
  \[
  \psi_m(s_n) = \frac{1}{2\pi\sigma^2}\exp\left(-\frac{\|s_n - \mu_m(s_m)\|^2}{2\sigma^2}\right)
  \]
- **变换函数 \(\mu_m\) 的三种选择**：
  - 恒等函数（基线）；
  - 仿射变换 \(\mu_m^a(s) = As + b\)（捕捉恒定空间位移，如从左到右的阅读倾向）；
  - 完全参数化 \(\mu_m^f(s) = \mu_m^a(s) + Cx_m\)（引入预测因子效应）。
- 密度函数由强度函数与积分项 \(\Lambda(t_n;\mathcal{H}_{n-1})\) 共同定义，并含指示函数确保不向前分配概率质量。

**（2）注视时长建模：卷积式对数正态分布**
- 假设注视时长服从对数正态分布：
  \[
  g(d_n \mid \mathcal{H}_{n-1}, t_n) = \frac{1}{d_n\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(\log d_n - \xi_n(t_n))^2}{2\sigma^2}\right)
  \]
- **条件对数均值** \(\xi_n(t_n)\) 采用卷积方式建模溢出效应：
  \[
  \xi_n^c(t_n) = x_n^\top w + \sum_{k\in K} w'_k \sum_{m=1}^{n-1} x_{mk}\,\gamma(t_n - t_m \mid \alpha_k, \beta_k, \theta_k)
  \]
  其中 \(\gamma\) 为移位伽马分布密度，用于捕捉时间上扩散的溢出效应。
- **马尔可夫溢出对照模型**：将伽马核替换为固定滞后权重，即
  \[
  \xi_n^M(t_n) = x_n^\top w + \sum_{k\in K}\sum_{m=n-l}^{n-1} x_{mk} w'_{mk}
  \]
  用于比较卷积模型与马尔可夫假设的拟合效果。

## 3. 实验设计

### 3.1 数据集
- 使用 **MECO语料库**（多语言眼动语料库）的**英语部分**，包含46名读者阅读12段Wikipedia短文的扫视路径。
- 原始数据共 **97,742个注视**。
- 通过Tesseract OCR识别字符及其边界框，并派生三个附加数据集：
  - **过滤扫视路径时长数据集**（46,511条）：移除词边界框外的注视，合并同一词上的连续注视；
  - **逐读者词级凝视时长数据集**（34,368条）；
  - **平均词级凝视时长数据集**（2,097条）。
- 预测因子包括：字符级惊奇度（GPT-2）、词级惊奇度（mGPT）、词长、一元惊奇度（词频，来自wordfreq）。

### 3.2 Benchmark与对比方法

**眼跳规划实验（§4.1）**：
- 基线模型：**泊松过程**（空间时间独立均匀）、**最后注视基线**（以上一次注视为中心的正态分布）、**标准霍克斯过程**（标量激发强度与衰减率、恒等空间变换）。
- 进阶模型：**恒定空间位移（CSS）模型**、**读者特异性效应（RSE）模型**、**加入预测因子的完全参数化模型**。
- 评估指标：每注视对数似然增益（相对于泊松基线或RSE模型），使用bootstrap重采样估计不确定性。

**注视时长实验（§4.2）**：
- 对比**卷积模型**（式16）与**线性马尔可夫模型**（式18，滞后 \(l=2\)）。
- 在完整扫视路径、过滤扫视路径及三种聚合数据集上分别评估。
- 基线包含读者特异性截距及过去注视时长的溢出效应（作为控制变量）。

## 4. 资源与算力

- 论文**未明确说明**所使用的GPU型号、数量或具体训练时长。
- 仅提及模型在 **PyTorch** 中实现，使用随机梯度下降（SGD）配合Nesterov动量训练，训练30个epoch，早停耐心值为5。
- 超参数网格搜索：眼跳模型搜索batch size {64, 128, 256}、学习率 {0.1, 0.01, 0.001}、权重衰减 {0, 10⁻⁴}，共18次运行/模型/数据集；时长卷积模型batch size固定128，搜索学习率 {0.01, 0.001, 0.0001} 和权重衰减 {0, 10⁻⁴}，并变化伽马分布初始参数。
- 采用**热启动**策略，从简单模型初始化复杂模型参数。

## 5. 实验数量与充分性

- **实验组数**：
  - 眼跳规划：约6种模型规格（泊松、最后注视、标准霍克斯、CSS、RSE、加预测因子）× 2种数据（完整/过滤）× 多种预测因子组合，另有扩展对比（图4）。
  - 注视时长：卷积模型与马尔可夫模型 × 4种数据集（完整、过滤、逐读者词级、平均词级）× 多组预测因子组合，共约数十组实验。
  - 分布选择：对6种候选分布（Rayleigh、指数、Weibull、正态、对数正态、伽马）进行10折交叉验证。
- **充分性评估**：
  - **优点**：实验覆盖了模型组件消融（时间依赖、空间位移、读者效应）、数据粒度对比（完整vs过滤）、聚合策略对比（原始vs三种聚合），以及多种预测因子，设计较为系统。
  - **客观性与公平性**：使用固定训练/验证/测试划分（80/10/10），bootstrap估计不确定性，线性模型采用五折交叉验证，基线设置较为严格（包含过去时长作为控制变量）。
  - **潜在不足**：仅使用英语数据，未做跨语言验证；超参数搜索不能保证全局最优；字符级与词级惊奇度来自不同语言模型，性能差异不能完全归因于粒度。

## 6. 主要结论与发现

- **眼跳规划**：
  - 更表达性的模型（时间依赖、恒定空间位移、读者特异性效应）显著提升对留出数据的泛化能力。最佳模型（RSE）相对泊松基线平均每注视对数似然增益 **2.44 nats**（约1047%更高似然）。
  - 参数估计显示一致的**全局右移约10.61个字符**，符合英语从左到右的阅读习惯；存在自激发效应，但激发强度（12.64±2.69）低于衰减速率（16.24±3.44），表明影响衰减较快。
  - 加入词汇预测因子（词长、惊奇度等）仅带来**边际提升**（多数低于2%相对增益），词长效果最大（约4%）。
  - 在**完整扫视路径**上训练的模型优于过滤扫视路径，说明保留词外注视信息有价值。
- **注视时长**：
  - 卷积模型与线性马尔可夫模型拟合效果**相似**，表明马尔可夫假设在实践中足够，过去注视的影响可能是**有界的**。
  - 加入惊奇度等预测因子仅带来**极小且多不显著**的改进（平均效应量<0.004）。
  - **聚合数据**上的效应量（0.023–0.037）比**非聚合数据**（≤0.003）大一个数量级以上，说明文献中基于聚合指标的效应可能被**系统性放大**。
  - 包含过去时长作为基线控制变量时，效应量进一步降低，建议未来研究采用更严格的基线。
- **总体结论**：常用聚合与数据处理流程会实质性影响阅读时间分析结果；惊奇度理论难以解释细粒度眼动。

## 7. 优点

- **方法创新**：首次将带标记的时空霍克斯过程系统应用于阅读行为建模，同时捕捉注视的**时间、空间和持续时间**三个维度，突破传统聚合指标的局限。
- **建模灵活性**：时间核和空间变换函数均可依赖注视特异性预测因子，支持读者特异性效应和方向性眼跳倾向（如从左到右、回视、重注视）。
- **溢出效应处理**：采用卷积式伽马核对过去预测因子进行时间扩散建模，并与马尔可夫假设进行系统对比，提供了关于溢出效应有界性的实证证据。
- **实验严谨性**：使用bootstrap估计不确定性、五折交叉验证、严格基线（含过去时长控制），并系统比较多种聚合策略，增强了结论的可信度。
- **理论意义**：对惊奇度理论在细粒度眼动层面的解释力提出质疑，并揭示聚合策略对效应量的放大作用，对心理语言学研究方法有重要警示意义。
- **开源代码**：提供GitHub仓库，便于复现和后续研究。

## 8. 不足与局限

- **数据覆盖有限**：仅使用MECO英语部分，未验证其他10种语言（尤其是从右到左书写的语言），跨语言泛化性未知。
- **模型假设限制**：
  - 空间核假设**各向同性方差**，可能无法捕捉眼动的方向性偏差；作者建议未来采用各向异性核或非线性扭曲函数。
  - 预测因子与响应之间的关系被限制为**仿射**，可能过度简化认知过程与眼动的关系。
  - 行转换等结构化空间效应未能成功建模（梯度不稳定），未纳入最终结果。
- **实验偏差风险**：
  - 字符级与词级惊奇度来自不同语言模型（GPT-2 vs mGPT），性能差异不能纯粹归因于表示粒度。
  - 超参数网格搜索不能保证全局最优。
  - 标准霍克斯基线与最后注视基线性能相当，但后者未获得同等的空间增强，比较可能不完全平衡。
- **应用限制**：模型旨在提供数据驱动的描述性建模，**并非**对认知或眼动控制机制的机理解释；合成扫视路径的应用未在文中重点展开。
- **预处理差异**：与Siegelman et al. (2022)的注视-词映射方法不同，可能导致绝对效应量偏小，影响与先前研究的直接可比性。

（完）
