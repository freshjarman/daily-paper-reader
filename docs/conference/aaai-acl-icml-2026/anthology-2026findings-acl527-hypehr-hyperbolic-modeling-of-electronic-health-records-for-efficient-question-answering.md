---
title: "HypEHR: Hyperbolic Modeling of Electronic Health Records for Efficient Question Answering"
title_zh: HypEHR：面向高效问答的电子健康记录双曲建模
authors: "Yuyu Liu, Sarang Rajendra Patil, Mengjia Xu, Tengfei Ma"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.findings-acl.527.pdf"
tags: ["query:ehr-es"]
score: 7.0
evidence: EHR序列建模与下次就诊诊断预测
tldr: 针对电子健康记录问答依赖昂贵大模型流程且未利用临床数据层级结构的问题，本文提出HypEHR，利用医疗本体与患者轨迹的双曲几何特性，将编码、就诊与问题嵌入双曲空间，并通过几何一致交叉注意力与类型化指针头作答。模型以下次就诊诊断预测和层级正则进行预训练。实验表明其在MIMIC-IV基准上以远少参数逼近大模型方法，推动了高效EHR序列建模与诊断预测。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl527/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 1378, \"height\": 736}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl527/fig-002.webp\", \"caption\": \"\", \"page\": 3, \"index\": 2, \"width\": 1523, \"height\": 825}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl527/fig-003.webp\", \"caption\": \"\", \"page\": 4, \"index\": 3, \"width\": 1220, \"height\": 911}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl527/fig-004.webp\", \"caption\": \"\", \"page\": 4, \"index\": 4, \"width\": 560, \"height\": 360}]"
motivation: EHR问答依赖昂贵大模型流程且忽视临床数据的层级结构。
method: 提出HypEHR，将编码、就诊与问题嵌入双曲空间并做几何一致交叉注意力。
result: 在MIMIC-IV问答基准上以远少参数逼近大模型方法。
conclusion: 为高效且结构感知的EHR序列建模与诊断预测提供了新方案。
---

## Abstract
Electronic health record (EHR) question answering is often handled by LLM-based pipelines that are costly to deploy and do not explicitly leverage the hierarchical structure of clinical data. Motivated by evidence that medical ontologies and patient trajectories exhibit hyperbolic geometry, we propose HypEHR, a compact Lorentzian model that embeds codes, visits, and questions in hyperbolic space and answers queries via geometry-consistent cross-attention with type-specific pointer heads. HypEHR is pretrained with next-visit diagnosis prediction and hierarchy-aware regularization to align representations with the ICD ontology. On two MIMIC-IV-based EHR-QA benchmarks, HypEHR approaches LLM-based methods while using far fewer parameters. Our code is publicly available at https://github.com/yuyuliu11037/HypEHR .

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究背景**：电子健康记录问答（EHR-QA）要求模型根据患者纵向就诊记录回答自然语言临床问题，例如“患者首次住院是否进入急诊室”“本次住院血培养是否有微生物学检测结果”等。
- **现有方法的问题**：
  - 基于大语言模型（LLM）的检索增强或生成式流程虽然准确，但部署成本高、隐私约束下难以本地化，且通常没有显式利用 EHR 的层级结构。
  - 文本到 SQL、图语义解析等方法同样依赖大规模预训练模型。
  - 传统 EHR 表示学习虽能编码时序和异质结构，但大多在欧氏空间中建模，难以低失真地表示医学本体和患者轨迹中的树状层级。
- **核心动机**：医学本体（如 ICD 编码）和患者就诊轨迹具有层级性，更接近双曲几何。欧氏嵌入会扭曲树状结构，而双曲空间可以用任意低失真嵌入层级。论文因此提出一个核心问题：**一个显式对齐 EHR 内在几何的紧凑模型，能否在复杂问答中与十亿/万亿参数级 LLM 竞争？**
- **整体含义**：论文提出 **HypEHR**，一个基于 Lorentz 双曲空间的紧凑 EHR-QA 框架，参数约 22M，目标是在隐私敏感的本地临床环境中，以远少参数逼近 LLM 方法，同时显式利用医学编码层级。

## 2. 方法论

### 2.1 总体框架

- HypEHR 分为两个阶段：
  1. **患者编码器预训练**：学习双曲患者编码器，联合优化“下一次就诊诊断预测”和“层级感知正则化”。
  2. **问答训练**：冻结患者编码器，训练按答案类型区分的预测头。
- 问题定义：给定自然语言问题 \(q\) 和患者就诊历史 \(H_p=\{v_1,\dots,v_T\}\)，模型需要定位正确就诊、找到正确科室/概念，并返回答案。
- 答案类型分为四类：布尔值、概念、数值、整数计数；还包括无答案情况。

### 2.2 双曲临床序列编码器

- 每个医学概念 \(c\) 被嵌入到 \(d\) 维 Lorentz 双曲流形 \(\mathbb{H}^d_L\)，得到 \(e_c\in\mathbb{H}^d_L\)。
- 在一次就诊内，使用双曲注意力聚合编码嵌入，得到就诊表示 \(h_t\in\mathbb{H}^d_L\)。
- 就诊序列 \(\{h_t\}_{t=1}^T\) 输入多层 **Lorentz Transformer 编码器**，其自注意力、残差连接和归一化均适配 Lorentz 流形，输出上下文就诊状态 \(\{z_t\}_{t=1}^T\) 和全局摘要 \(z_{[CLS]}\in\mathbb{H}^d_L\)。
- 全局摘要用于下一次就诊诊断预测，损失为 \(L_{diag}\)（二元交叉熵）。
- 层级感知正则化：
  - 使用 ICD 编码树：章节 → 块 → 类别 → 子类别。
  - 鼓励共享祖先的编码在双曲距离上更近。
  - 总损失：
    \[
    L = L_{diag} + \lambda L_{hier}
    \]
    \[
    L_{hier} = L_{rad} + \mu L_{rel}
    \]
  - **径向层级项** \(L_{rad}\)：对父–子对 \((p,c)\)，约束父节点双曲半径小于子节点：
    \[
    \max(0,\|e_p\|_H-\|e_c\|_H+\beta)
    \]
    其中 \(\|e\|_H:=d_H(e,o)\)，\(o\) 为 Lorentz 双曲面原点。
  - **相对层级项** \(L_{rel}\)：对三元组 \((a,a^+,a^-)\)，使 \(a\) 与祖先相关节点 \(a^+\) 的距离小于与非祖先节点 \(a^-\) 的距离：
    \[
    \max(0,d_H(e_a,e_{a^+})-d_H(e_a,e_{a^-})+\alpha)
    \]
  - \(\alpha,\beta>0\) 为 margin，\(\lambda,\mu>0\) 平衡损失。

### 2.3 双曲 EHR-QA 模型

- 问题 \(q\) 先由生物医学预训练语言编码器编码为欧氏向量 \(u_q\in\mathbb{R}^{d_e}\)。
- 通过仿射映射和原点处的指数映射投影到双曲流形：
  \[
  \tilde u_i=Wu_i+b,\quad z_{q_i}=\exp_o(\tilde u_i)\in\mathbb{H}^d_L
  \]
- 对就诊状态做双曲交叉注意力：
  \[
  s_t=-\gamma d_H(z_q,z_t)
  \]
  \[
  \alpha_t=\mathrm{softmax}(s_t)
  \]
  \[
  z^{visit}_{p|q}=\mathrm{HypAgg}(\{\alpha_t,z_t\}_{t=1}^T)
  \]
  HypAgg 实现为加权对数映射平均后再指数映射，近似 Lorentz 流形上的 Fréchet 均值。
- 对 top-k 关注就诊内的编码嵌入再做第二阶段双曲注意力，得到编码级理由向量 \(z^{code}_{p|q}\in\mathbb{H}^d_L\)。
- 不同答案类型使用专门预测头，输入 \((z_q,z^{visit}_{p|q},z^{code}_{p|q})\)，并用交叉熵训练：
  - **布尔/存在头**：拼接切空间表示，MLP 输出二分类。
  - **概念头**：在患者候选概念集 \(C_p\) 上做指针选择，包含可学习的“无答案”伪概念 \(c_{null}\)。
  - **浮点值头**：在候选数值事件集 \(E\) 上做指针选择，包含可学习的空事件 \(e_{null}\)，使用多正例 log-loss。
  - **计数头**：将计数离散化为 \(\{0,1,\dots,K_{max}\}\)，做分类交叉熵。
- 推理时，将双曲向量通过对数映射映回原点切空间，再输入欧氏 MLP。

## 3. 实验设计

### 3.1 数据集与任务

- **EHR-QA 基准**：
  - **MIMIC-IV-Ext-Instr**：使用 Schema Alignment 子集，训练/验证/测试划分跟随 Llemr。
  - **EHRXQA**：使用 tabular 子集，将问题按答案类型分为 Boolean Value、Count、Float Value、Concept。
- **临床预测任务**：在 MIMIC-IV 上评估四个任务：
  - 死亡率预测（MT）
  - 再入院预测（RA）
  - 住院时长预测（LOS）
  - 表型预测（Pheno）
  - 评价指标为 AUPRC。
- **数据预处理**：
  - MIMIC-IV 过滤少于两次就诊的患者，ICD-9-CM 通过 GEMs 映射到 ICD-10-CM。
  - 处理后：14,155 名患者，42,053 次就诊，平均 2.97 次/患者，最多 70 次，11,225 个唯一诊断，8,352 个唯一操作，196 个唯一药物。
- **评价指标**：EHR-QA 报告准确率，临床预测报告 AUPRC。

### 3.2 对比方法

- **文本到 SQL 方法**：
  - NeuralSQL：使用 GPT-5.2 作为 SQL 解析器。
  - NeuralSQL-l：轻量版，使用 code-smol2-text-to-sql。
- **LLM 方法**：
  - Llemr：指令微调 LLM 框架。
  - EHRAgent：带 Python 代码接口和工具调用的智能体。
  - Llama-3-8B：直接提示生成答案。
- **EHR 表示学习方法**：
  - RETAIN：传统患者序列编码器，替换 HypEHR 中的患者编码器作为基线。
- 结果报告 5 个随机种子的均值和标准差。

## 4. 资源与算力

- **GPU**：4 张 NVIDIA A100，每张 80GB 显存。
- **训练配置**：
  - batch size 48。
  - 优化器：`geoopt.optim.RiemannianAdam`。
  - 权重衰减 \(1\times10^{-2}\)，学习率 \(3\times10^{-4}\)，线性 warmup 前 10%，随后余弦衰减。
  - 梯度裁剪最大 \(\ell_2\) 范数 1.0，dropout 0.1。
  - 早停 patience 10 epoch。
  - 预训练最多 250 epoch，约 2 小时；QA 头训练最多 200 epoch，约 5 分钟。
- **模型规模**：
  - Lorentz Transformer 3 层，每层 6 个注意力头。
  - 双曲嵌入维度 390。
  - 总可训练参数约 22M，FP32 存储约 84MB。
- **实现细节**：
  - PyTorch + Geoopt，混合精度 FP16，NVIDIA Apex。
  - 文本编码器：Bio_ClinicalBERT。
- **未明确说明**：论文没有报告总 GPU 小时数、能耗、完整训练管线总成本等。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 两个 EHR-QA 数据集：EHRXQA、MIMIC-IV-Ext-Instr。
  - 每个数据集按四类问题报告准确率：Boolean、Count、Float、Concept。
  - 5 个随机种子重复训练，报告均值 ± 标准差。
  - 与 6 个代表性基线比较：RETAIN、NeuralSQL、NeuralSQL-l、Llama-3、Llemr、EHRAgent。
  - 消融实验：w/o \(L_{hier}\)、w/o pretraining、EucEHR（欧氏版本）、完整 HypEHR。
  - 四个临床预测任务：死亡率、再入院、住院时长、表型。
  - 几何分析：ICD 编码按树深度分组，比较欧氏范数与 Lorentz 双曲半径。
- **充分性评价**：
  - 实验覆盖了 QA、临床预测、消融和几何验证，整体较完整。
  - 5 个随机种子和标准差增强了结果可信度。
  - 超参数在验证集上搜索，训练/测试划分遵循已有工作，较客观。
- **公平性注意点**：
  - EHRXQA 本身以 SQL 查询形式表述，文本到 SQL 和 LLM 智能体方法天然占优。
  - 论文将 NeuralSQL 和 Llemr 分别视为 EHRXQA 和 MIMIC-Instr 的官方强基线，近似性能上界。
  - LLM 基线的提示、解码、模型版本等可能引入不可控差异。
  - 所有实验集中在 MIMIC-IV 相关数据，外部泛化性有限。

## 6. 主要结论与发现

- **EHR-QA 性能**：
  - EHRXQA 上 HypEHR 准确率 89.53%，优于 RETAIN 81.19%、Llama-3 82.88%、Llemr 87.25%、NeuralSQL-l 86.72%，但低于 NeuralSQL 95.97% 和 EHRAgent 93.06%。
  - MIMIC-IV-Ext-Instr 上 HypEHR 准确率 76.02%，优于 RETAIN 65.91%、NeuralSQL 75.17%、NeuralSQL-l 67.85%、Llama-3 70.90%、EHRAgent 74.16%，略低于 Llemr 77.53%。
  - 结论：在不依赖 LLM 框架的方法中，HypEHR 表现最佳，并接近 LLM 基线。
- **临床预测**：
  - 在再入院预测和表型预测上取得最佳性能。
  - 在其余任务上与 LLM 基线 Llemr 相当。
- **消融实验**：
  - 患者编码器预训练贡献最大：去掉预训练后 EHRXQA 降至 74.
