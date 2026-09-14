<div class="dpr-topic-result-actions"><button type="button" data-topic-copy="docs/starter-pack/20260914-e78bab55c0fb/papers.md">复制论文清单</button> <a href="docs/starter-pack/20260914-e78bab55c0fb/papers.md" download data-no-router>下载 Markdown</a> <a href="docs/starter-pack/20260914-e78bab55c0fb/papers.json" download data-no-router>下载 JSON</a> <button type="button" data-topic-continue="20260914-e78bab55c0fb">继续生成阅读内容</button></div>

# TPP-ES · 入门导读

> 本导读基于所列论文的标题、摘要和已有速览，不代表已阅读全部全文。近期窗口不是完整领域史；检索不保证覆盖全部相关论文。模型导读需结合原文核验。

检索窗口：arXiv &#91;2025-09-14, 2026-09-14&#41;；会议 &#91;2024-09-14, 2026-09-14&#41;（UTC，结束日不含）

## 方向概览

本导读聚焦连续时间异步事件序列的建模与预测，覆盖标记时间点过程、时空点过程、集合型事件序列、事件预测与生成等主题。基于输入论文可见，近期研究主要围绕以下问题展开：如何用神经或统计模型刻画事件的条件强度函数或累积强度；如何高效进行似然训练与采样；如何融合离散标记与连续时间动态；如何在时空域中建模背景强度与触发核；如何构造生成式（扩散、流匹配、签名）模型以支持无条件与条件生成；以及如何面向长时程预测、插补、异常检测与变化点检测等下游任务。评测方面，常见做法包括在合成与真实数据集上比较预测似然、下一事件类型与时间预测误差、拟合优度、生成质量与采样效率等。当前进展体现在表达力、计算效率、可解释性与生成灵活性上的持续改进；局限则包括评测协议不统一、标记不平衡、长时程误差累积、时空模型可扩展性与理论保证不足等。需要说明的是，本导读仅覆盖输入论文所反映的近期检索窗口，不构成完整领域史，也不补写未提供的经典文献、实验数字或外部链接。

依据：[Deep Continuous-Time State-Space Models for Marked Event Sequences](/conference/neurips-2025/openreview-neurips-2025-74sve2gzww-deep-continuous-time-state-space-models-for-marked-event-sequences)；[Long-range Modeling and Processing of Multimodal Event Sequences](/20250914-20260913/2602.01125v1)；[Edit-Based Flow Matching for Temporal Point Processes](/20250914-20260913/2510.06050v3)；[In-Context Learning of Temporal Point Processes with Foundation Inference Models](/20250914-20260913/2509.24762v3)；[Smooth Neural Point Processes via B-Splines](/20250914-20260913/2607.21098v1)；[ITPP: Learning Disentangled Event Dynamics in Marked Temporal Point Processes](/20250914-20260913/2511.06032v1)；[Residual TPP: A Unified Lightweight Approach for Event Stream Data Analysis](/conference/icml-2025/openreview-icml-2025-aukbfmtyus-residual-tpp-a-unified-lightweight-approach-for-event-stream-data-analysis)；[Speculative Sampling for Parametric Temporal Point Processes](/20250914-20260913/2510.20031v1)；[ExPERT: Modeling Human Behavior Under External Stimuli Aware Personalized MTPP](/conference/aaai-2025/aaai-2025-33960-expert-modeling-human-behavior-under-external-stimuli-aware-personalized-mtpp)；[Unlocking Point Processes through Point Set Diffusion](/conference/iclr-2025/openreview-iclr-2025-4anfphj0wf-unlocking-point-processes-through-point-set-diffusion)；[A Spatio-Temporal Point Process for Fine-Grained Modeling of Reading Behavior](/conference/acl-2025/anthology-2025acl-long1474-a-spatio-temporal-point-process-for-fine-grained-modeling-of-reading-behavior)；[Scaling-law-informed neural point processes for earthquake sequence forecasting](/20250914-20260913/2608.18791v1)；[Bridging Discrete Marks and Continuous Dynamics: Dual-Path Cross-Interaction for Marked Temporal Point Processes](/20250914-20260913/2603.11462v1)；[TPP-SD: Accelerating Transformer Point Process Sampling with Speculative Decoding](/conference/neurips-2025/openreview-neurips-2025-lkqk19tqgx-tpp-sd-accelerating-transformer-point-process-sampling-with-speculative-decoding)；[Product Depth for Temporal Point Processes Observed Only Up to the First k Events](/20250914-20260913/2511.19375v1)；[Efficient Temporal Point Processes via Monotone Alternating Splines](/20250914-20260913/2607.01752v1)；[Seahorse: A Unified Benchmarking Framework for Spatiotemporal Event Modeling](/20250914-20260913/2607.01022v1)；[Density-based Neural Temporal Point Processes for Heartbeat Dynamics](/20250914-20260913/2511.22096v1)；[Latent Block-Diffusion Temporal Point Processes: A Semi-Autoregressive Framework for Asynchronous Event Sequence Generation](/20250914-20260913/2606.24982v1)；[Transformers for Mixed-type Event Sequences](/conference/neurips-2025/openreview-neurips-2025-mtwsrjpzhf-transformers-for-mixed-type-event-sequences)

## 神经时间点过程的强度建模与高效似然训练

该子方向关注如何用神经网络参数化条件强度或累积条件强度，并在保持表达力的同时实现精确、可并行、低计算代价的负对数似然训练。输入论文中，S2P2 将现代深度状态空间模型与随机跳跃微分方程结合，构造基于强度的标记时间点过程，并用并行扫描获得线性复杂度；B 样条方法直接把条件强度参数化为非负 B 样条基组合，实现精确 NLL 评估并支持平滑正则；单调交替样条则针对累积条件强度建模，指出单调神经网络在凸性、饱和与建模要求上的结构性问题，并提出插值与外推分离的框架；SurF 利用时间重标度定理作为可学习双射，并给出多种累积强度参数化以扩展到长序列。这些工作共同体现了从自回归顺序计算向并行、精确、可扩展似然训练的演进。

依据：[Deep Continuous-Time State-Space Models for Marked Event Sequences](/conference/neurips-2025/openreview-neurips-2025-74sve2gzww-deep-continuous-time-state-space-models-for-marked-event-sequences)；[Smooth Neural Point Processes via B-Splines](/20250914-20260913/2607.21098v1)；[Efficient Temporal Point Processes via Monotone Alternating Splines](/20250914-20260913/2607.01752v1)；[SurF: A Generative Model for Multivariate Irregular Time Series Forecasting](/20250914-20260913/2605.14069v1)

## 标记时间点过程中的类型解耦、不平衡与外部刺激建模

标记时间点过程需要同时刻画事件类型与到达时间。输入论文中，ITPP 指出通道混合会纠缠类型特定动态，提出通道独立架构与类型感知的倒置自注意力；针对标记分布高度不平衡的问题，有工作提出阈值化方法，按标记先验归一化后学习阈值，并采用先预测标记再预测时间的策略，同时避免数值积分；ExPERT 在 Transformer Hawkes 过程上引入外部刺激与基于语言模型的用户和事件描述表示，强调个性化与领域无关的外部刺激建模；Hawkes Attention 从多元 Hawkes 过程理论推导注意力算子，用可学习的逐类型神经核调制查询、键和值投影；超 Hawkes 过程通过潜在空间扩展与超网络获得时间与数据依赖动态，同时保留可解释的递归结构。

依据：[ITPP: Learning Disentangled Event Dynamics in Marked Temporal Point Processes](/20250914-20260913/2511.06032v1)；[Addressing Mark Imbalance in Integration-free Marked Temporal Point Processes](/conference/neurips-2025/openreview-neurips-2025-lutnvmiw3c-addressing-mark-imbalance-in-integration-free-marked-temporal-point-processes)；[Addressing Mark Imbalance in Integration-free Neural Marked Temporal Point Processes](/20250914-20260913/2510.20414v2)；[ExPERT: Modeling Human Behavior Under External Stimuli Aware Personalized MTPP](/conference/aaai-2025/aaai-2025-33960-expert-modeling-human-behavior-under-external-stimuli-aware-personalized-mtpp)；[From Hawkes Processes to Attention: Time-Modulated Mechanisms for Event Sequences](/20250914-20260913/2601.09220v2)；[Hyper Hawkes Processes: Interpretable Models of Marked Temporal Point Processes](/20250914-20260913/2511.01096v1)

## 离散标记与连续动态的融合及混合类型事件序列

事件序列常同时包含离散事件类型与连续测量值，且事件间存在连续演化。输入论文中，NEXTPP 提出双通道框架，用自注意力编码离散标记，同时用神经常微分方程演化潜在连续状态，并通过交叉注意力实现双向交互，再驱动神经 Hawkes 过程的条件强度；面向混合类型事件序列的 Transformer 框架使用离散与连续预测头，连续头采用归一化流建模连续事件属性，避免事件间时间的数值积分；ChronoSSM 则在自回归状态空间模型中联合建模事件与时间戳，比较联合训练与两阶段训练对时间信息可恢复性的影响；SOHET 面向异构事件流，结合事件类型特定的表格编码器与时间、类型嵌入，并引入自监督预训练目标。

依据：[Bridging Discrete Marks and Continuous Dynamics: Dual-Path Cross-Interaction for Marked Temporal Point Processes](/20250914-20260913/2603.11462v1)；[Transformers for Mixed-type Event Sequences](/conference/neurips-2025/openreview-neurips-2025-mtwsrjpzhf-transformers-for-mixed-type-event-sequences)；[ChronoSSM: Training for Temporally Aware Representations in Autoregressive State Space Models](/20250914-20260913/2608.10120v1)；[SOHET: Sequence Of Heterogeneous Events Transformer with Self-Supervised Pre-Training](/20250914-20260913/2606.21356v1)

## 时空点过程与时空 Hawkes 过程

时空点过程在连续时间和空间中建模事件，关注背景强度、触发核、空间局部性与可扩展性。输入论文中，点集扩散直接在一般度量空间上学习点集分布，不依赖强度函数，并支持并行采样与条件生成；GLIDE 面向下一事件建模，用多尺度历史图与双流架构编码时空拓扑，并引入先验引导的跳跃推断以降低反向采样成本；KSTPP 用空间高斯过程建模背景强度、用时空高斯过程建模影响核，并通过 Kronecker 结构协方差与张量积 Gauss-Legendre 求积实现可扩展训练；多变量时空神经 Hawkes 过程将空间信息融入潜在状态演化；时空 Hawkes 过程的统计推断与模拟工作统一了两种模拟技术与三种推断技术；关于时空 Hawkes 过程后验集中的工作在高斯过程先验下给出条件强度与参数的后验收缩率；此外还有面向阅读行为的标记时空点过程、地震序列预测的尺度律信息神经标记点过程，以及基于事件时空网络的复杂系统建模。

依据：[Unlocking Point Processes through Point Set Diffusion](/conference/iclr-2025/openreview-iclr-2025-4anfphj0wf-unlocking-point-processes-through-point-set-diffusion)；[GLIDE: Graph-guided Leap Inference for Diffusion Estimation of Spatio-Temporal Point Processes](/20250914-20260913/2606.01273v1)；[Kronecker-Structured Nonparametric Spatiotemporal Point Processes](/20250914-20260913/2603.23746v2)；[Multivariate Spatio-Temporal Neural Hawkes Processes](/20250914-20260913/2602.23629v2)；[Spatio-temporal Hawkes point processes: statistical inference and simulation strategies](/20250914-20260913/2511.14509v1)；[Posterior concentration in spatio-temporal Hawkes processes](/20250914-20260913/2601.03719v1)；[A Spatio-Temporal Point Process for Fine-Grained Modeling of Reading Behavior](/conference/acl-2025/anthology-2025acl-long1474-a-spatio-temporal-point-process-for-fine-grained-modeling-of-reading-behavior)；[Scaling-law-informed neural point processes for earthquake sequence forecasting](/20250914-20260913/2608.18791v1)；[Event-based spatiotemporal networks for modelling emergent phenomena in complex systems](/20250914-20260913/2605.15798v1)

## 生成式时间点过程：扩散、流匹配与签名方法

该子方向关注不依赖自回归逐事件采样、能够并行或半并行生成事件序列的模型。输入论文中，编辑流匹配将噪声到数据的传输定义为插入、删除、替换编辑操作，在连续时间马尔可夫链框架下学习瞬时编辑率；潜在块扩散时间点过程在潜在空间对事件块定义自回归分布并在块内做高斯扩散，兼顾变长输出与并行生成，并给出 Wasserstein 误差界；点集扩散直接对点集做随机插值，支持空间与时空点过程的无条件与条件生成；sigTPP 通过事件间到达嵌入把跳跃路径提升为有界变差连续路径，从而将粗糙路径签名方法扩展到事件序列，并给出三种分布差异度量；ReDiTT 使用检索增强的条件扩散 Transformer 在潜在空间预测下一事件间时间与类型，以稳定长时程预测；ARCH 提出分层流匹配框架，通过混合掩码支持任意条件，统一预测、逆推断与部分轨迹恢复。

依据：[Edit-Based Flow Matching for Temporal Point Processes](/20250914-20260913/2510.06050v3)；[Latent Block-Diffusion Temporal Point Processes: A Semi-Autoregressive Framework for Asynchronous Event Sequence Generation](/20250914-20260913/2606.24982v1)；[Unlocking Point Processes through Point Set Diffusion](/conference/iclr-2025/openreview-iclr-2025-4anfphj0wf-unlocking-point-processes-through-point-set-diffusion)；[From Jumps to Signatures: a Generative Method for Temporal Point Processes](/20250914-20260913/2607.06652v1)；[ReDiTT: Retrieval Augmented Conditional Diffusion Transformers for Asynchronous Time Series](/20250914-20260913/2607.12391v1)；[Arbitrarily Conditioned Hierarchical Flows for Spatiotemporal Events](/20250914-20260913/2605.01226v1)

## 采样加速、并行生成与离散空间采样

时间点过程的自回归采样本质上是顺序的，限制了大规规模应用。输入论文中，参数化时间点过程的推测采样基于拒绝采样，在不改变架构或重训练的前提下并行精确采样多个未来值；TPP-SD 将 Transformer 时间点过程的细化算法与语言模型中的推测解码类比，用小型草稿模型生成候选事件再由大模型验证，保持输出分布不变并取得加速；采样于离散空间的工作构造多元时间点过程，使固定长度滑动窗口内的事件计数向量收敛到目标多元计数分布，并给出与出生死亡过程的比较。

依据：[Speculative Sampling for Parametric Temporal Point Processes](/20250914-20260913/2510.20031v1)；[TPP-SD: Accelerating Transformer Point Process Sampling with Speculative Decoding](/conference/neurips-2025/openreview-neurips-2025-lkqk19tqgx-tpp-sd-accelerating-transformer-point-process-sampling-with-speculative-decoding)；[Sampling on Discrete Spaces with Temporal Point Processes](/20250914-20260913/2603.09089v2)

## 基础模型、上下文学习与预训练

该子方向探索用大规模合成预训练获得可迁移的事件序列推断能力。输入论文中，FIM-PP 基于摊销推断与上下文学习，在大量 Hawkes 过程合成数据上预训练深度网络，使其无需额外训练即可从真实数据估计条件强度，或快速微调；面向科学发现的基础模型工作训练于数百万模拟事件序列，强调无需重训练即可分析新数据并支持快速微调；LAST SToP 面向异步时间序列设计大语言模型提示，利用事件描述的自然语言与随机软提示，把分析范围扩展到预测之外的异常检测与数据插补；TPP-TAL 则作为即插即用框架，在送入大语言模型前显式对齐时间动态与上下文语义，以增强时间感知。

依据：[In-Context Learning of Temporal Point Processes with Foundation Inference Models](/20250914-20260913/2509.24762v3)；[On Foundation Models for Temporal Point Processes to Accelerate Scientific Discovery](/20250914-20260913/2510.12640v2)；[LAST SToP for Modeling Asynchronous Time Series](/conference/icml-2025/openreview-icml-2025-tpp47eh1xg-last-stop-for-modeling-asynchronous-time-series)；[Enhancing Temporal Awareness in LLMs for Temporal Point Processes](/20250914-20260913/2601.00845v1)

## 长时程预测、插补与下游任务

输入论文覆盖了长时程预测、插补、异常检测、变化点检测与事件关系预测等任务。ReDiTT 通过检索增强条件扩散稳定长时程预测并提升样本多样性；LBDTPP 面向异步事件序列生成并强调变长输出；LAST SToP 将异步时间序列分析扩展到异常检测与数据插补；CADES 基于保形推断与时间重标度定理设计非一致性分数，在有限样本下控制假阳性率；时空点过程的基于分数的变化点检测与区域定位工作联合估计变化时间与连续空间中的变化区域；多变量非齐次 Poisson 过程的在线变化点检测使用低秩强度表示实现单遍、常数代价更新；此外还有面向时间知识图谱外推推理的组注意力神经 Hawkes 过程、面向演化超图方向关系预测的神经时间点过程、以及联合事件与时间预测的时间图统一框架。

依据：[ReDiTT: Retrieval Augmented Conditional Diffusion Transformers for Asynchronous Time Series](/20250914-20260913/2607.12391v1)；[Latent Block-Diffusion Temporal Point Processes: A Semi-Autoregressive Framework for Asynchronous Event Sequence Generation](/20250914-20260913/2606.24982v1)；[LAST SToP for Modeling Asynchronous Time Series](/conference/icml-2025/openreview-icml-2025-tpp47eh1xg-last-stop-for-modeling-asynchronous-time-series)；[Conformal Anomaly Detection in Event Sequences](/conference/icml-2025/openreview-icml-2025-cq7xu5tmp8-conformal-anomaly-detection-in-event-sequences)；[Score-Based Change-Point Detection and Region Localization for Spatio-Temporal Point Processes](/20250914-20260913/2602.04798v1)；[Online Change Point Detection for Multivariate Inhomogeneous Poisson Processes Time Series](/20250914-20260913/2601.20192v2)；[GAttNHP: Group Attention Neural Hawkes Process for Extrapolation Reasoning in Temporal Knowledge Graphs](/20250914-20260913/2607.14733v1)；[Neural Temporal Point Processes for Forecasting Directional Relations in Evolving Hypergraphs](/conference/aaai-2025/aaai-2025-33856-neural-temporal-point-processes-for-forecasting-directional-relations-in-evolving-hypergraphs)；[GTIN: A Unified Framework for Joint Event and Time Prediction in Temporal Graphs](/20250914-20260913/2607.23556v2)

## 评测、基准与拟合优度

评测协议与基准建设是该领域近期的重要关注点。输入论文中，SEAHORSE 提出时空事件建模的统一基准框架，形式化编码-演化-解码接口，在单一可执行协议下训练、调参与评估各模型族，并以原始坐标似然报告结果，同时提供合成压力测试套件以暴露不同模型族的归纳偏置；面向心跳动态的工作把经典点过程拟合优度框架适配到神经时间点过程，用于超参数优化与训练序列长度选择；残差时间点过程提出残差事件分解，定义权重函数量化强度函数对事件特征的拟合程度，识别残差事件，并可与任意时间点过程模型组合；此外，关于时间点过程乘积深度的工作面向仅观测到前 k 个事件的情形提出深度函数，用于中心性与排序分析。

依据：[Seahorse: A Unified Benchmarking Framework for Spatiotemporal Event Modeling](/20250914-20260913/2607.01022v1)；[Density-based Neural Temporal Point Processes for Heartbeat Dynamics](/20250914-20260913/2511.22096v1)；[Residual TPP: A Unified Lightweight Approach for Event Stream Data Analysis](/conference/icml-2025/openreview-icml-2025-aukbfmtyus-residual-tpp-a-unified-lightweight-approach-for-event-stream-data-analysis)；[Product Depth for Temporal Point Processes Observed Only Up to the First k Events](/20250914-20260913/2511.19375v1)

## 可解释性、结构化关系发现与事件分支推断

在保持预测性能的同时揭示事件间结构化关系是重要方向。输入论文中，结构化神经标记点过程构造乘积形式神经影响核，由类型间有符号交互网络与延迟感知单调时间网络组成，可显式刻画激励、抑制与中性关系；KSTPP 通过高斯过程影响核支持事件级关系发现；BADMM 模块把事件分支推断形式化为稀疏低秩约束下的事件转移矩阵优化，可嵌入现有时间点过程模型或学习范式，为 Hawkes 过程的期望最大化提供结构化责任矩阵，为自注意力神经时间点过程提供低秩稀疏注意力图；超 Hawkes 过程保留分段条件线性递归结构，便于直接探查预测生成方式。

依据：[Structured Neural Marked Point Processes for Interpretable Event Interaction Modeling](/20250914-20260913/2605.17568v2)；[Kronecker-Structured Nonparametric Spatiotemporal Point Processes](/20250914-20260913/2603.23746v2)；[A Plug-and-Play Bregman ADMM Module for Inferring Event Branches in Temporal Point Processes](/conference/aaai-2025/aaai-2025-35420-a-plug-and-play-bregman-admm-module-for-inferring-event-branches-in-temporal-point-processes)；[Hyper Hawkes Processes: Interpretable Models of Marked Temporal Point Processes](/20250914-20260913/2511.01096v1)

## 统计推断、理论性质与稳健性

输入论文包含若干统计推断与理论工作。时空 Hawkes 过程的后验收缩率在高斯过程先验下给出条件强度与参数的理论保证；有限点过程的分数匹配工作通过 Janossy 测度建立形式化框架，指出分数匹配在非参数深度模型下不能唯一识别真实分布，并提出生存分类增强以获得完整、免积分训练目标；幂律强度长记忆马尔可夫链工作构造具有有限维马尔可夫状态表示的自激励点过程，并证明不可约性、非周期性、T 链性质与正 Harris recurrence；此外还有关于时空超阈值点过程渐近行为、退化空间点过程的位移与不完全检测、以及标记点过程多尺度拓扑推断的工作。

依据：[Posterior concentration in spatio-temporal Hawkes processes](/20250914-20260913/2601.03719v1)；[Score Matching for Estimating Finite Point Processes](/20250914-20260913/2512.04617v1)；[Long-memory Markov chains with power-law intensities](/20250914-20260913/2607.20838v1)；[Asymptotic behavior of spatio-temporal point processes of exceedances](/20250914-20260913/2604.11691v1)；[Analyzing spatial point processes degraded by displacement and imperfect detection](/20250914-20260913/2606.05374v1)；[Multiscale Topological Inference for Marked Point Processes via Euler Characteristic Envelopes](/20250914-20260913/2605.14647v1)

## 应用驱动的事件序列建模

输入论文展示了时间点过程在多个领域的应用。地震序列预测结合 ETAS 与 Gutenberg-Richter 律的神经标记点过程；心跳动态用密度型神经时间点过程建模；阅读行为用标记时空点过程建模注视与眼跳；车辆错误模式预测用因果 Transformer 与自回归解码器；网络流量模拟用多标记时间点过程联合建模到达时间与包头字段；体育事件用随机记忆自激励过程建模；等待人群用非齐次空间点过程建模；行人到达时间用多重分形分析；还有面向急诊医疗服务预测的 AlphaEarth 空间上下文增强、面向半导体故障与疾病爆发的 Lorentzian 傅里叶神经算子、以及面向车辆、金融、医疗等领域的其他应用。这些工作表明时间点过程已成为连接统计建模与深度学习的通用工具。

依据：[Scaling-law-informed neural point processes for earthquake sequence forecasting](/20250914-20260913/2608.18791v1)；[Density-based Neural Temporal Point Processes for Heartbeat Dynamics](/20250914-20260913/2511.22096v1)；[A Spatio-Temporal Point Process for Fine-Grained Modeling of Reading Behavior](/conference/acl-2025/anthology-2025acl-long1474-a-spatio-temporal-point-process-for-fine-grained-modeling-of-reading-behavior)；[Harnessing Event Sensory Data for Error Pattern Prediction in Vehicles: A Language Model Approach](/conference/aaai-2025/aaai-2025-34138-harnessing-event-sensory-data-for-error-pattern-prediction-in-vehicles-a-language-model-approach)；[TempoNet: Learning Realistic Communication and Timing Patterns for Network Traffic Simulation](/20250914-20260913/2601.15663v1)；[Modeling Event Dynamics by Self-Exciting Processes with Random Memory](/20250914-20260913/2601.07980v1)；[Modeling inhomogeneous spatial point configurations with applications to replicated patterns in waiting crowds](/20250914-20260913/2606.14532v1)；[The multi-fractal nature of pedestrian arrival times](/20250914-20260913/2605.05788v1)；[When Context Compensates for Sparse Event History: AlphaEarth for Spatio-Temporal Point-Process Forecasting](/20250914-20260913/2607.01082v1)；[L-FNO: Lorentzian Fourier Neural Operator for Stochastic Event Dynamics](/20250914-20260913/2608.13562v1)

## 建议阅读顺序

以下为建议学习顺序，不是公布时间排序。

1. [Deep Continuous-Time State-Space Models for Marked Event Sequences](/conference/neurips-2025/openreview-neurips-2025-74sve2gzww-deep-continuous-time-state-space-models-for-marked-event-sequences) · 入门
   - 阅读理由：以深度状态空间模型构造基于强度的标记时间点过程，兼顾表达力与线性复杂度，适合作为理解现代神经时间点过程建模的入口。
   - 公布时间：2025（年精度）
   - NeurIPS-2025-Accepted · 2025（年精度）：[官方论文集](https://papers.neurips.cc/paper_files/paper/2025/hash/ee39348acc798915d2d15a8bbbd417b8-Abstract-Conference.html) / [原文](https://openreview.net/forum?id=74SvE2GZwW)

2. [Smooth Neural Point Processes via B-Splines](/20250914-20260913/2607.21098v1) · 入门
   - 阅读理由：直接参数化条件强度为 B 样条基组合，清晰展示精确 NLL 评估与并行训练的设计思路。
   - 公布时间：2026-07-23（日精度）
   - arxiv · 2026-07-23（日精度）：[原文](https://arxiv.org/pdf/2607.21098v1) / [PDF](https://arxiv.org/pdf/2607.21098v1)

3. [Efficient Temporal Point Processes via Monotone Alternating Splines](/20250914-20260913/2607.01752v1) · 入门
   - 阅读理由：针对累积条件强度建模，指出单调神经网络的结构性问题并提出替代框架，有助于理解强度与累积强度参数化的取舍。
   - 公布时间：2026-07-02（日精度）
   - arxiv · 2026-07-02（日精度）：[原文](https://arxiv.org/pdf/2607.01752v1) / [PDF](https://arxiv.org/pdf/2607.01752v1)

4. [ITPP: Learning Disentangled Event Dynamics in Marked Temporal Point Processes](/20250914-20260913/2511.06032v1) · 入门
   - 阅读理由：讨论标记时间点过程中的类型解耦与通道独立架构，是理解类型特定动态建模的入门材料。
   - 公布时间：2025-11-08（日精度）
   - AAAI-2026-Accepted · 2026（年精度）：[原文](https://ojs.aaai.org/index.php/AAAI/article/view/40138) / [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/40138/44099)
   - arxiv · 2025-11-08（日精度）：[原文](https://arxiv.org/pdf/2511.06032v1) / [PDF](https://arxiv.org/pdf/2511.06032v1)

5. [Transformers for Mixed-type Event Sequences](/conference/neurips-2025/openreview-neurips-2025-mtwsrjpzhf-transformers-for-mixed-type-event-sequences) · 入门
   - 阅读理由：面向混合类型事件序列，使用离散与连续预测头及归一化流，适合了解异构事件序列的统一建模。
   - 公布时间：2025（年精度）
   - NeurIPS-2025-Accepted · 2025（年精度）：[官方论文集](https://papers.neurips.cc/paper_files/paper/2025/hash/a6c7515ac435277dc92b75a07bb2257c-Abstract-Conference.html) / [原文](https://openreview.net/forum?id=MtwsRjPZhf)

6. [Bridging Discrete Marks and Continuous Dynamics: Dual-Path Cross-Interaction for Marked Temporal Point Processes](/20250914-20260913/2603.11462v1) · 进阶
   - 阅读理由：融合离散标记自注意力与神经常微分方程连续演化，展示离散与连续表示的双向交互设计。
   - 公布时间：2026-03-12（日精度）
   - arxiv · 2026-03-12（日精度）：[原文](https://arxiv.org/pdf/2603.11462v1) / [PDF](https://arxiv.org/pdf/2603.11462v1)

7. [From Hawkes Processes to Attention: Time-Modulated Mechanisms for Event Sequences](/20250914-20260913/2601.09220v2) · 进阶
   - 阅读理由：从多元 Hawkes 过程理论推导 Hawkes Attention，连接经典点过程与 Transformer 注意力机制。
   - 公布时间：2026-01-14（日精度）
   - arxiv · 2026-01-14（日精度）：[原文](https://arxiv.org/pdf/2601.09220v2) / [PDF](https://arxiv.org/pdf/2601.09220v2)

8. [Hyper Hawkes Processes: Interpretable Models of Marked Temporal Point Processes](/20250914-20260913/2511.01096v1) · 进阶
   - 阅读理由：超 Hawkes 过程在保持可解释递归结构的同时提升表达力，适合理解可解释性与性能之间的平衡。
   - 公布时间：2025-11-02（日精度）
   - arxiv · 2025-11-02（日精度）：[原文](https://arxiv.org/pdf/2511.01096v1) / [PDF](https://arxiv.org/pdf/2511.01096v1)

9. [Residual TPP: A Unified Lightweight Approach for Event Stream Data Analysis](/conference/icml-2025/openreview-icml-2025-aukbfmtyus-residual-tpp-a-unified-lightweight-approach-for-event-stream-data-analysis) · 进阶
   - 阅读理由：残差事件分解作为即插即用模块，结合简单统计模型与神经模型，适合理解拟合优度与残差建模。
   - 公布时间：2025-10-06（日精度）
   - ICML-2025-Accepted · 2025-10-06（日精度）：[官方论文集](https://proceedings.mlr.press/v267/yuan25a.html) / [原文](https://openreview.net/forum?id=AUkBFMtyUs)

10. [A Plug-and-Play Bregman ADMM Module for Inferring Event Branches in Temporal Point Processes](/conference/aaai-2025/aaai-2025-35420-a-plug-and-play-bregman-admm-module-for-inferring-event-branches-in-temporal-point-processes) · 进阶
   - 阅读理由：BADMM 模块用于推断事件分支，展示稀疏低秩约束与结构化注意力图的可解释性。
   - 公布时间：2025（年精度）
   - AAAI-2025-Accepted · 2025（年精度）：[原文](https://ojs.aaai.org/index.php/AAAI/article/view/35420) / [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/35420/37575)

11. [Structured Neural Marked Point Processes for Interpretable Event Interaction Modeling](/20250914-20260913/2605.17568v2) · 进阶
   - 阅读理由：结构化神经标记点过程通过乘积形式影响核显式刻画类型间激励、抑制与中性关系。
   - 公布时间：2026-05-17（日精度）
   - arxiv · 2026-05-17（日精度）：[原文](https://arxiv.org/pdf/2605.17568v2) / [PDF](https://arxiv.org/pdf/2605.17568v2)

12. [Edit-Based Flow Matching for Temporal Point Processes](/20250914-20260913/2510.06050v3) · 进阶
   - 阅读理由：编辑流匹配将生成过程定义为插入、删除、替换操作，是理解非自回归时间点过程生成的重要工作。
   - 公布时间：2025-10-07（日精度）
   - ICLR-2026-Accepted · 2026（年精度）：[官方论文集](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b5a324fa48de6a2d7c593b1cf7ad10e1-Abstract-Conference.html) / [原文](https://openreview.net/forum?id=FNf9IV1P2L)
   - arxiv · 2025-10-07（日精度）：[原文](https://arxiv.org/pdf/2510.06050v3) / [PDF](https://arxiv.org/pdf/2510.06050v3)

13. [Latent Block-Diffusion Temporal Point Processes: A Semi-Autoregressive Framework for Asynchronous Event Sequence Generation](/20250914-20260913/2606.24982v1) · 进阶
   - 阅读理由：潜在块扩散时间点过程提出半自回归框架，兼顾变长输出与并行生成，并给出误差界。
   - 公布时间：2026-06-23（日精度）
   - arxiv · 2026-06-23（日精度）：[原文](https://arxiv.org/pdf/2606.24982v1) / [PDF](https://arxiv.org/pdf/2606.24982v1)

14. [Unlocking Point Processes through Point Set Diffusion](/conference/iclr-2025/openreview-iclr-2025-4anfphj0wf-unlocking-point-processes-through-point-set-diffusion) · 进阶
   - 阅读理由：点集扩散不依赖强度函数，直接在一般度量空间上建模点集分布，适合理解生成式点过程的新范式。
   - 公布时间：2025（年精度）
   - ICLR-2025-Accepted · 2025（年精度）：[官方论文集](https://proceedings.iclr.cc/paper_files/paper/2025/hash/cceb6b5d1781b6eb848f7e87bff5f74b-Abstract-Conference.html) / [原文](https://openreview.net/forum?id=4anfpHj0wf)

15. [From Jumps to Signatures: a Generative Method for Temporal Point Processes](/20250914-20260913/2607.06652v1) · 专题
   - 阅读理由：通过事件间到达嵌入把签名方法扩展到事件序列，并给出分布差异度量，适合关注生成模型评测的读者。
   - 公布时间：2026-07-07（日精度）
   - arxiv · 2026-07-07（日精度）：[原文](https://arxiv.org/pdf/2607.06652v1) / [PDF](https://arxiv.org/pdf/2607.06652v1)

16. [ReDiTT: Retrieval Augmented Conditional Diffusion Transformers for Asynchronous Time Series](/20250914-20260913/2607.12391v1) · 专题
   - 阅读理由：检索增强条件扩散 Transformer 面向异步时间序列的长时程预测，适合研究长时程与样本多样性的读者。
   - 公布时间：2026-07-14（日精度）
   - arxiv · 2026-07-14（日精度）：[原文](https://arxiv.org/pdf/2607.12391v1) / [PDF](https://arxiv.org/pdf/2607.12391v1)

17. [GLIDE: Graph-guided Leap Inference for Diffusion Estimation of Spatio-Temporal Point Processes](/20250914-20260913/2606.01273v1) · 专题
   - 阅读理由：GLIDE 结合多尺度历史图与先验引导跳跃推断，适合研究时空点过程扩散模型的读者。
   - 公布时间：2026-05-31（日精度）
   - arxiv · 2026-05-31（日精度）：[原文](https://arxiv.org/pdf/2606.01273v1) / [PDF](https://arxiv.org/pdf/2606.01273v1)

18. [Kronecker-Structured Nonparametric Spatiotemporal Point Processes](/20250914-20260913/2603.23746v2) · 专题
   - 阅读理由：KSTPP 用 Kronecker 结构高斯过程实现可扩展的时空点过程建模与关系发现。
   - 公布时间：2026-03-24（日精度）
   - arxiv · 2026-03-24（日精度）：[原文](https://arxiv.org/pdf/2603.23746v2) / [PDF](https://arxiv.org/pdf/2603.23746v2)

19. [Seahorse: A Unified Benchmarking Framework for Spatiotemporal Event Modeling](/20250914-20260913/2607.01022v1) · 专题
   - 阅读理由：SEAHORSE 提供统一时空事件建模基准框架与合成压力测试，适合关注评测协议与可复现性的读者。
   - 公布时间：2026-07-01（日精度）
   - arxiv · 2026-07-01（日精度）：[原文](https://arxiv.org/pdf/2607.01022v1) / [PDF](https://arxiv.org/pdf/2607.01022v1)

20. [In-Context Learning of Temporal Point Processes with Foundation Inference Models](/20250914-20260913/2509.24762v3) · 专题
   - 阅读理由：FIM-PP 通过摊销推断与上下文学习预训练基础推断模型，适合关注基础模型与零样本推断的读者。
   - 公布时间：2025-09-29（日精度）
   - arxiv · 2025-09-29（日精度）：[原文](https://arxiv.org/pdf/2509.24762v3) / [PDF](https://arxiv.org/pdf/2509.24762v3)
   - ICLR-2026-Accepted · 2026（年精度）：[官方论文集](https://proceedings.iclr.cc/paper_files/paper/2026/hash/325126ccbf5be6e8f285d2a61d33d8c2-Abstract-Conference.html) / [原文](https://openreview.net/forum?id=h9HwUAODFP)

任务：研究方向大礼包

固定窗口：arXiv &#91;2025-09-14, 2026-09-14&#41;；会议 &#91;2024-09-14, 2026-09-14&#41;（UTC，结束日不含）

本次候选评审上限 300，最终名单上限 100；本轮内容预算 10。

覆盖限制：仅检索配置范围内已有库存与预算内候选；向量/会议Top-k召回并非全库遍历，不保证找全相关论文。未核实录用、日期边界和缺失库存不能当作已覆盖。

缺失库存：eccv 2025、emnlp 2026、ijcai 2026、neurips 2026。

研究需求：查找temporal point process（包括marked tpp; stpp; set tpp; event forecast; continuous-time event prediction; asynchronous event sequence）相关工作

# TPP-ES

以下为本次固定最终名单，按相关性评分降序；不代表全部相关论文。

1. [Deep Continuous-Time State-Space Models for Marked Event Sequences](https://papers.neurips.cc/paper_files/paper/2025/hash/ee39348acc798915d2d15a8bbbd417b8-Abstract-Conference.html) · 分数 10
2. [Long-range Modeling and Processing of Multimodal Event Sequences](https://arxiv.org/abs/2602.01125v1) · 分数 10
3. [Edit-Based Flow Matching for Temporal Point Processes](https://arxiv.org/abs/2510.06050v3) · 分数 10
4. [In-Context Learning of Temporal Point Processes with Foundation Inference Models](https://arxiv.org/abs/2509.24762v3) · 分数 10
5. [Smooth Neural Point Processes via B-Splines](https://arxiv.org/abs/2607.21098v1) · 分数 10
6. [ITPP: Learning Disentangled Event Dynamics in Marked Temporal Point Processes](https://arxiv.org/abs/2511.06032v1) · 分数 10
7. [Residual TPP: A Unified Lightweight Approach for Event Stream Data Analysis](https://proceedings.mlr.press/v267/yuan25a.html) · 分数 10
8. [Speculative Sampling for Parametric Temporal Point Processes](https://arxiv.org/abs/2510.20031v1) · 分数 10
9. [ExPERT: Modeling Human Behavior Under External Stimuli Aware Personalized MTPP](https://ojs.aaai.org/index.php/AAAI/article/view/33960) · 分数 10
10. [Unlocking Point Processes through Point Set Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/hash/cceb6b5d1781b6eb848f7e87bff5f74b-Abstract-Conference.html) · 分数 10
11. [A Spatio-Temporal Point Process for Fine-Grained Modeling of Reading Behavior](https://aclanthology.org/2025.acl-long.1474/) · 分数 10
12. [Scaling-law-informed neural point processes for earthquake sequence forecasting](https://arxiv.org/abs/2608.18791v1) · 分数 10
13. [Bridging Discrete Marks and Continuous Dynamics: Dual-Path Cross-Interaction for Marked Temporal Point Processes](https://arxiv.org/abs/2603.11462v1) · 分数 9
14. [TPP-SD: Accelerating Transformer Point Process Sampling with Speculative Decoding](https://papers.neurips.cc/paper_files/paper/2025/hash/b0a844fbfd7f5840baeec02a8e7e406d-Abstract-Conference.html) · 分数 9
15. [Product Depth for Temporal Point Processes Observed Only Up to the First k Events](https://arxiv.org/abs/2511.19375v1) · 分数 9
16. [Efficient Temporal Point Processes via Monotone Alternating Splines](https://arxiv.org/abs/2607.01752v1) · 分数 9
17. [Seahorse: A Unified Benchmarking Framework for Spatiotemporal Event Modeling](https://arxiv.org/abs/2607.01022v1) · 分数 9
18. [Density-based Neural Temporal Point Processes for Heartbeat Dynamics](https://arxiv.org/abs/2511.22096v1) · 分数 9
19. [Latent Block-Diffusion Temporal Point Processes: A Semi-Autoregressive Framework for Asynchronous Event Sequence Generation](https://arxiv.org/abs/2606.24982v1) · 分数 9
20. [Transformers for Mixed-type Event Sequences](https://papers.neurips.cc/paper_files/paper/2025/hash/a6c7515ac435277dc92b75a07bb2257c-Abstract-Conference.html) · 分数 9
21. [Addressing Mark Imbalance in Integration-free Marked Temporal Point Processes](https://papers.neurips.cc/paper_files/paper/2025/hash/590c043fab86acdb65fb4ffc3490c074-Abstract-Conference.html) · 分数 9
22. [A Plug-and-Play Bregman ADMM Module for Inferring Event Branches in Temporal Point Processes](https://ojs.aaai.org/index.php/AAAI/article/view/35420) · 分数 9
23. [From Jumps to Signatures: a Generative Method for Temporal Point Processes](https://arxiv.org/abs/2607.06652v1) · 分数 9
24. [Addressing Mark Imbalance in Integration-free Neural Marked Temporal Point Processes](https://arxiv.org/abs/2510.20414v2) · 分数 9
25. [GLIDE: Graph-guided Leap Inference for Diffusion Estimation of Spatio-Temporal Point Processes](https://arxiv.org/abs/2606.01273v1) · 分数 9
26. [From Hawkes Processes to Attention: Time-Modulated Mechanisms for Event Sequences](https://arxiv.org/abs/2601.09220v2) · 分数 9
27. [Hyper Hawkes Processes: Interpretable Models of Marked Temporal Point Processes](https://arxiv.org/abs/2511.01096v1) · 分数 9
28. [Neural Temporal Point Processes for Forecasting Directional Relations in Evolving Hypergraphs](https://ojs.aaai.org/index.php/AAAI/article/view/33856) · 分数 9
29. [Kronecker-Structured Nonparametric Spatiotemporal Point Processes](https://arxiv.org/abs/2603.23746v2) · 分数 9
30. [Enhancing Temporal Awareness in LLMs for Temporal Point Processes](https://arxiv.org/abs/2601.00845v1) · 分数 9
31. [Score-Based Change-Point Detection and Region Localization for Spatio-Temporal Point Processes](https://arxiv.org/abs/2602.04798v1) · 分数 9
32. [On Foundation Models for Temporal Point Processes to Accelerate Scientific Discovery](https://arxiv.org/abs/2510.12640v2) · 分数 9
33. [Spatio-temporal Hawkes point processes: statistical inference and simulation strategies](https://arxiv.org/abs/2511.14509v1) · 分数 9
34. [Multivariate Spatio-Temporal Neural Hawkes Processes](https://arxiv.org/abs/2602.23629v2) · 分数 9
35. [Laplace Variational Inference for Dirichlet Process Mixtures of Marked Poisson Point Processes](https://arxiv.org/abs/2605.09562v1) · 分数 9
36. [Deep Representation Learning for Forecasting Recursive and Multi-Relational Events in Temporal Networks](https://ojs.aaai.org/index.php/AAAI/article/view/33857) · 分数 9
37. [Structured Neural Marked Point Processes for Interpretable Event Interaction Modeling](https://arxiv.org/abs/2605.17568v2) · 分数 9
38. [Learning Spatiotemporal Dynamical Systems from Point Process Observations](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b35df4ede4411f6831b94452bb98e43b-Abstract-Conference.html) · 分数 9
39. [When Context Compensates for Sparse Event History: AlphaEarth for Spatio-Temporal Point-Process Forecasting](https://arxiv.org/abs/2607.01082v1) · 分数 9
40. [Arbitrarily Conditioned Hierarchical Flows for Spatiotemporal Events](https://arxiv.org/abs/2605.01226v1) · 分数 9
41. [Neural Diffusion Intensity Models for Point Process Data](https://arxiv.org/abs/2602.24083v1) · 分数 9
42. [Posterior concentration in spatio-temporal Hawkes processes](https://arxiv.org/abs/2601.03719v1) · 分数 9
43. [ReDiTT: Retrieval Augmented Conditional Diffusion Transformers for Asynchronous Time Series](https://arxiv.org/abs/2607.12391v1) · 分数 9
44. [Long-memory Markov chains with power-law intensities](https://arxiv.org/abs/2607.20838v1) · 分数 9
45. [GAttNHP: Group Attention Neural Hawkes Process for Extrapolation Reasoning in Temporal Knowledge Graphs](https://arxiv.org/abs/2607.14733v1) · 分数 9
46. [L-FNO: Lorentzian Fourier Neural Operator for Stochastic Event Dynamics](https://arxiv.org/abs/2608.13562v1) · 分数 9
47. [TempoNet: Learning Realistic Communication and Timing Patterns for Network Traffic Simulation](https://arxiv.org/abs/2601.15663v1) · 分数 9
48. [Conformal Anomaly Detection in Event Sequences](https://proceedings.mlr.press/v267/zhang25dn.html) · 分数 9
49. [Modeling Event Dynamics by Self-Exciting Processes with Random Memory](https://arxiv.org/abs/2601.07980v1) · 分数 9
50. [Differentiable Adversarial Attacks for Marked Temporal Point Processes](https://ojs.aaai.org/index.php/AAAI/article/view/33724) · 分数 8
51. [Sampling on Discrete Spaces with Temporal Point Processes](https://arxiv.org/abs/2603.09089v2) · 分数 8
52. [SurF: A Generative Model for Multivariate Irregular Time Series Forecasting](https://arxiv.org/abs/2605.14069v1) · 分数 8
53. [Evolving Minds: Logic-Informed Inference from Temporal Action Patterns](https://proceedings.mlr.press/v267/yang25i.html) · 分数 8
54. [Stochastic Event Prediction via Temporal Motif Transitions](https://arxiv.org/abs/2603.05874v1) · 分数 8
55. [Trend and seasonality estimation for point-process time series](https://arxiv.org/abs/2605.21884v1) · 分数 8
56. [Asymptotic behavior of spatio-temporal point processes of exceedances](https://arxiv.org/abs/2604.11691v1) · 分数 8
57. [Receding-Horizon Maximum-Likelihood Estimation of Neural-ODE Dynamics and Thresholds from Event Cameras](https://arxiv.org/abs/2603.05011v2) · 分数 8
58. [LAST SToP for Modeling Asynchronous Time Series](https://proceedings.mlr.press/v267/gupta25a.html) · 分数 8
59. [ldmppr: Location Dependent Marked Point Processes in R](https://arxiv.org/abs/2605.19100v1) · 分数 8
60. [Score Matching for Estimating Finite Point Processes](https://arxiv.org/abs/2512.04617v1) · 分数 8
61. [SOHET: Sequence Of Heterogeneous Events Transformer with Self-Supervised Pre-Training](https://arxiv.org/abs/2606.21356v1) · 分数 8
62. [Multiscale Topological Inference for Marked Point Processes via Euler Characteristic Envelopes](https://arxiv.org/abs/2605.14647v1) · 分数 8
63. [GTIN: A Unified Framework for Joint Event and Time Prediction in Temporal Graphs](https://arxiv.org/abs/2607.23556v2) · 分数 8
64. [Event-based spatiotemporal networks for modelling emergent phenomena in complex systems](https://arxiv.org/abs/2605.15798v1) · 分数 8
65. [Online Change Point Detection for Multivariate Inhomogeneous Poisson Processes Time Series](https://arxiv.org/abs/2601.20192v2) · 分数 7
66. [Analyzing spatial point processes degraded by displacement and imperfect detection](https://arxiv.org/abs/2606.05374v1) · 分数 7
67. [Modeling non-Poissonian temporal hypergraphs by Markovian node dynamics](https://arxiv.org/abs/2604.07694v1) · 分数 7
68. [Generating Causal Temporal Interaction Graphs for Counterfactual Validation of Temporal Link Prediction](https://arxiv.org/abs/2602.02161v1) · 分数 7
69. [SPAN: Continuous Modeling of Suspicion Progression for Temporal Intention Localization](https://arxiv.org/abs/2510.20189v2) · 分数 7
70. [Temporal Tokenization Strategies for Event Sequence Modeling with Large Language Models](https://arxiv.org/abs/2512.13618v3) · 分数 7
71. [Existence-Field Diffusion Model for Spatial Point Processes with Variable Cardinality](https://arxiv.org/abs/2607.26428v1) · 分数 7
72. [NEST: Nested Event Stream Transformer for Sequences of Multisets](https://arxiv.org/abs/2602.00520v3) · 分数 7
73. [ChronoSSM: Training for Temporally Aware Representations in Autoregressive State Space Models](https://arxiv.org/abs/2608.10120v1) · 分数 7
74. [NeuroMemFPP: A recurrent neural approach for memory-aware parameter estimation in fractional Poisson process](https://arxiv.org/abs/2512.05893v1) · 分数 7
75. [NUM2EVENT: Interpretable Event Reasoning from Numerical time-series](https://arxiv.org/abs/2510.23630v1) · 分数 7
76. [A Deep Probabilistic Framework for Continuous Time Dynamic Graph Generation](https://ojs.aaai.org/index.php/AAAI/article/view/33896) · 分数 7
77. [Generating temporal networks with the Ascona model](https://arxiv.org/abs/2512.16972v2) · 分数 6
78. [Weighted Score-Oriented Losses for Temporally Localized Event Prediction](https://arxiv.org/abs/2606.23145v1) · 分数 6
79. [Estimating Mutual Information between Time Series and Temporal Event Sequences Across Diverse Analysis Tasks](https://arxiv.org/abs/2606.01602v3) · 分数 6
80. [Temporal connection probabilities in real networks](https://arxiv.org/abs/2604.23714v1) · 分数 6
81. [Modeling inhomogeneous spatial point configurations with applications to replicated patterns in waiting crowds](https://arxiv.org/abs/2606.14532v1) · 分数 6
82. [Fast Mining and Dynamic Time-to-Event Prediction over Multi-sensor Data Streams](https://arxiv.org/abs/2601.04741v2) · 分数 6
83. [HEPA: A Self-Supervised Horizon-Conditioned Event Predictive Architecture for Time Series](https://arxiv.org/abs/2605.11130v4) · 分数 6
84. [Structure-Aware Set Transformers: Temporal and Variable-Type Attention Biases for Asynchronous Clinical Time Series](https://arxiv.org/abs/2603.06605v2) · 分数 6
85. [SPOT-Trip: Dual-Preference Driven Out-of-Town Trip Recommendation](https://papers.neurips.cc/paper_files/paper/2025/hash/d32abef446ead79ac1e7f80419a7b82f-Abstract-Conference.html) · 分数 6
86. [SEDformer: Event-Synchronous Spiking Transformers for Irregular Telemetry Time Series Forecasting](https://arxiv.org/abs/2602.02230v2) · 分数 6
87. [The multi-fractal nature of pedestrian arrival times](https://arxiv.org/abs/2605.05788v1) · 分数 6
88. [Harnessing Event Sensory Data for Error Pattern Prediction in Vehicles: A Language Model Approach](https://ojs.aaai.org/index.php/AAAI/article/view/34138) · 分数 6

[按公布时间查看](#/starter-pack/20260914-e78bab55c0fb/dates)

阅读内容：已完成 10，待补充 78。
