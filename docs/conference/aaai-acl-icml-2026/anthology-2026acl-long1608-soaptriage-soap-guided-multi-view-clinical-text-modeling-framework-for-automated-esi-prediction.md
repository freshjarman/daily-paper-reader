---
title: "SOAPTriage: SOAP-Guided Multi-View Clinical Text Modeling Framework for Automated ESI Prediction"
title_zh: SOAPTriage：面向自动ESI预测的SOAP引导多视图临床文本建模框架
authors: "Enming Wang, Jianlei Wang, Xueping Peng, Hongjiao Guan, Yinglong Wang, Sibo Wei, Jianbin Guo, Ruifeng Xu (徐睿峰), Wenpeng Lu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.acl-long.1608.pdf"
tags: ["query:ehr-es"]
score: 5.0
evidence: SOAP引导的多视图临床分诊文本建模用于ESI预测
tldr: 急诊科依赖分诊文本进行ESI病情分级，但自动ESI预测面临高质量分诊文本稀缺与缺乏临床理论框架两大挑战。本文受SOAP临床范式启发，提出SOAPTriage多视图临床文本建模框架，从主观、客观、评估与计划四个互补维度刻画分诊推理结构。实验表明其提升了ESI预测效果。该工作面向临床事件与文本序列建模，与EHR事件流建模相关但侧重文本模态。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1608/fig-001.webp\", \"caption\": \"\", \"page\": 23, \"index\": 1, \"width\": 1591, \"height\": 701}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1608/fig-002.webp\", \"caption\": \"\", \"page\": 24, \"index\": 2, \"width\": 1534, \"height\": 606}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1608/fig-003.webp\", \"caption\": \"\", \"page\": 24, \"index\": 3, \"width\": 1540, \"height\": 865}]"
motivation: 自动ESI预测受限于分诊文本稀缺，且缺乏能刻画多维分诊推理的临床理论框架。
method: 受SOAP临床范式启发，构建主观、客观、评估与计划四个互补视图的临床文本建模框架。
result: 在急诊分诊ESI预测任务上取得优于现有方法的性能。
conclusion: 为临床文本与事件序列的临床决策建模提供了理论引导的多视图方案。
---

## Abstract
Emergency departments (ED) rely on the Emergency Severity Index (ESI) to assess patient acuity and prioritize care, a process that is largely driven by clinical triage text. Despite recent progress in automated ESI prediction, two fundamental challenges remain: the scarcity of high-quality triage text data due to privacy and regulatory constraints and the lack of a clinically grounded triage framework capable of explicitly capturing the multidimensional structure of triage reasoning. To address these challenges, we draw inspiration from the clinically grounded SOAP paradigm, in which SOAP refers to Subjective, Objective, Assessment, and Plan and captures four complementary aspects of clinical reasoning. Building on this paradigm, we propose SOAPTriage, a SOAP-guided multi-view clinical text modeling framework for automated ESI prediction. To mitigate data scarcity, SOAPTriage introduces a Clinical Note Augmentation (CNA) module that generates natural-language triage notes from structured ED records, resulting in 15,393 augmented clinical notes derived from a real-world dataset. To incorporate clinical structure, SOAPTriage employs a SOAP-Guided Encoding (SGE) module that models patient conditions from four complementary SOAP perspectives, together with an adaptive SOAP-Aware Aggregation and Inference (SAAI) module that performs multi-view reasoning to infer ESI levels. Extensive experiments show that SOAPTriage consistently outperforms strong prompting-based, multi-agent, and encoder-based baselines, demonstrating the effectiveness of SOAP-guided multi-view clinical text modeling for automated emergency triage.

---

## 论文详细总结（自动生成）

# SOAPTriage 论文总结

## 1. 核心问题与整体含义

- **研究背景**：急诊科（ED）依赖急诊严重指数（ESI，1级最紧急至5级最不紧急）对患者病情紧急程度进行分级，以优先救治与分配资源。该过程目前仍高度依赖临床医生人工阅读分诊文本进行判断，随着就诊量上升，易导致医生疲劳、判断一致性下降、资源错配与危重救治延迟。
- **两大核心缺口**：
  - **Gap 1：高质量分诊文本数据严重稀缺**。受隐私保护与法规限制，真实临床分诊笔记难以公开，现有研究多依赖规模较小或质量不一致的数据集。
  - **Gap 2：缺乏临床理论支撑的分诊框架**。现有方法主要关注模型架构、提示工程或局部特征建模，未显式整合系统化的临床分诊理论，难以全面刻画患者的多维临床信息。
- **整体含义**：论文提出 SOAPTriage，将临床成熟的 SOAP（Subjective 主观、Objective 客观、Assessment 评估、Plan 计划）范式作为归纳偏置引入自动 ESI 预测，试图同时缓解数据稀缺与理论缺失两大问题，推动更可靠、更贴近临床推理的自动分诊。

## 2. 方法论

- **核心思想**：以 SOAP 四视角对分诊文本进行多视图建模，通过自适应聚合与级联推理输出 ESI 等级；同时用结构化急诊记录合成自然语言分诊笔记以扩充数据。
- **任务定义**：给定一条自然语言分诊笔记 $v_i$，学习映射到 ESI 标签 $y_i \in \{1,\dots,5\}$，值越小越紧急。

### 模块一：临床笔记增强（CNA）

- **Templating（模板填充）**：将 MIMIC-IV 结构化字段（年龄、性别、族裔、主诉、来院方式、体温、心率、呼吸频率、血氧、血压、疼痛评分、既往病史、过敏史）填入统一模板，得到忠实但风格僵硬的初始文本。
- **Retrieval（检索）**：用 `bge-large-en-v1.5` 编码模板文本与真实笔记语料（来自 TRIAGEAGENT 数据），检索 top-K=3 最相似的真实临床笔记作为风格范例。
- **Generation（生成）**：由 LLM 进行检索增强改写，将模板文本润色为自然、多样且保留原始临床信息的急诊分诊笔记。
- **产出**：从 MIMIC-IV 生成 **15,393 条**临床分诊笔记（另在 NHAMCS 生成 16,596 条）。

### 模块二：SOAP 引导编码（SGE）

- 使用**冻结的 LLM**（Qwen3-8B，36 层），为每条笔记构造四个 SOAP 视角的对话式提示（系统提示定义任务与视角 + 用户提示含笔记与指令），分别独立编码。
- 提取**中间层（第 18–22 层）**的 token 隐藏状态，经层混合、均值池化与 L2 归一化，得到每个视角的定长嵌入 $f_{i,c} \in \mathbb{R}^d$（$c \in \{S,O,A,P\}$）。
- 选择中层而非末层，理由是中层表示语义更丰富、更具迁移性，末层更偏向预训练目标。

### 模块三：SOAP 感知聚合与推理（SAAI）

- **自适应加权聚合**：拼接四视角嵌入得 $x_i \in \mathbb{R}^{4d}$，经两层 MLP（ReLU）与 softmax 得到权重 $w_i = \mathrm{softmax}(\mathrm{MLP}(x_i))$，加权求和得统一表示 $z_i = \sum_{c \in C} w_{i,c} f_{i,c}$，模拟临床医生按情境与风险动态调整各维度关注度。
- **两阶段级联推理**：
  - 粗粒度阶段：轻量二分类器区分高风险/低风险，仅用于路由。
  - 细粒度阶段：根据路由结果，使用对应的高风险或低风险序数预测头确定最终 ESI 等级；两个头共享聚合表示但参数独立，以适配不同紧急程度区间。
- **序数预测实现**：对阈值 logits 施加 sigmoid，通过统计超过 0.5 的阈值数量确定等级；训练中采用自适应类别加权缓解类别不平衡。

## 3. 实验设计

- **数据集 / 场景**：
  - **MIMIC-IV**（整合 MIMIC-IV、MIMIC-IV-ED、MIMIC-IV-Note）：15,393 条增强分诊笔记，训练/验证/测试按 **8:1:1** 划分并保持标签分布。
  - **NHAMCS**：16,596 条记录，采用 IMMEDR（IR）分级，用于分布偏移下的域内验证。
  - **真实世界临床笔记**：384 条来自真实临床环境的笔记（TRIAGEAGENT 数据），用于跨数据集零样本迁移测试。
- **Benchmark 与评价指标**：
  - 主指标 **Total Discordance**（预测与真实 ESI 不一致比例，越低越好）。
  - 辅助指标：**UnderTriage、OverTriage、Significant UnderTriage、Significant OverTriage**（后者关注危重欠分诊与低级过度分诊等高风险的严重错误）。
- **对比方法**：
  - **提示类 LLM 基线**：Standard Prompting、Prompt-RAG、CoT、Self-Consistency（SCons）、Self-Contrast（SCtr）、Exchange-of-Thought（EoT）、KEA、TAIT-LoRA。
  - **多智能体方法**：TRIAGEAGENT。
  - **编码器分类模型**：BERT、TCM-BERT、BioBERT、KATE-BERT。
- **人类专家评估**：3 位医学领域专家对生成笔记从 5 个维度（临床一致性、事实正确性、叙述自然度、信息完整性、可读性）评分，并做字段级幻觉评估与 IMMEDR–ESI 映射一致性检验（Fleiss' kappa = 0.7435，显示高度一致）。

## 4. 资源与算力

- **GPU**：全部实验在**单张 NVIDIA RTX 5090** 上完成。
- **训练配置**：AdamW 优化器，权重衰减 $5\times10^{-4}$，初始学习率 $3\times10^{-4}$，余弦退火调度；训练 **200 个 epoch**，batch size 128，梯度裁剪最大范数 5.0；冻结 LLM 解码温度设为 0；随机种子固定为 42。
- **骨干模型**：主实验用 Qwen3-8B；规模实验覆盖 0.6B/1.7B/4B/8B/14B；提示类基线与 TRIAGEAGENT 使用 DeepSeek-V3.2；检索编码器为 `bge-large-en-v1.5`。
- **未明确说明**：论文未报告具体训练时长、总 GPU 小时数或能耗成本，仅给出单卡型号与训练超参数。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 主对比实验：MIMIC-IV（表 2，14 个基线 + 本方法）。
  - 外部数据集：NHAMCS（表 9）。
  - 跨数据集迁移：真实世界 384 条笔记（表 8）。
  - 消融实验：w/o SGE、w/o SAAI-weight、w/o SAAI-fusion（图 3a）。
  - 骨干规模实验：0.6B、1.7B、4B、8B、14B 共 5 档（图 3b）。
  - 架构设置实验：单阶段 vs 两阶段、中层 vs 末层表示（表 3）。
  - 人类评估：临床质量 5 维度、幻觉评估、IMMEDR–ESI 映射。
  - 案例研究：3 个代表性病例（含 1 个失败案例）并分析各阶段 SOAP 权重。
- **充分性评价**：
  - **较充分**：覆盖多数据集、多类基线、消融、模型规模、架构与人类评估，并提供了跨域迁移验证与失败案例分析。
  - **客观性较好**：使用临床导向指标（区分欠/过度分诊及显著错误），而非仅报告准确率。
  - **公平性存疑之处**：提示类基线与多智能体方法使用 **DeepSeek-V3.2**，而本方法与需微调方法使用 **Qwen3-8B**，骨干不一致可能影响比较公平性；作者解释是为保证可复现性。
  - **跨域结果并非全面领先**：真实世界笔记上 Total Discordance 为 52.60%，高于 SCons 的 48.95%，作者将其归因于推理能力提升而非对合成笔记风格的适配。

## 6. 主要结论与发现

- **总体性能领先**：在 MIMIC-IV 上，SOAPTriage 的 Total Discordance 为 **35.99%**，优于次优基线 KATE-BERT（39.63%），并在欠分诊（17.99%）、显著欠分诊（10.39%）、过度分诊（18.00%）等指标上均为最优或接近最优。
- **编码器方法普遍优于提示类与多智能体方法**，说明通用 LLM 未经领域适配时，在复杂真实分诊场景中难以形成可靠分类决策。
- **消融结论**：
  - 移除 SGE 后各指标明显上升，说明 SOAP 结构化表示对分诊推理至关重要。
  - 移除 SAAI 加权会加剧显著过度分诊。
  - 移除多视图融合会显著增加欠分诊与总不一致率。
- **规模效应**：参数量越大性能越好，但综合性能与算力成本，**8B 模型性价比最优**。
- **架构结论**：两阶段级联优于单阶段直接预测；中层表示优于末层表示。
- **生成数据质量**：人类专家评估显示生成笔记在 5 个维度上接近真实笔记（MIMIC-IV 总体 93.25 vs 参考 92.47），字段级忠实度约 91–94 分，临床可信度较高。
- **跨域表现**：在真实世界笔记上优于 CoT、SCtr 与 BERT，且避免了 BERT 的严重过度分诊倾向，表明增益来自 ESI 推理能力而非仅适配合成数据风格。

## 7. 优点

- **临床理论驱动**：将 SOAP 范式显式作为归纳偏置引入表示学习与推理，而非仅依赖架构或提示工程，增强临床一致性与可解释路径。
- **数据稀缺的务实解法**：CNA 通过“模板 + 检索 + 生成”三阶段合成大规模自然语言分诊笔记，并经人类专家验证质量，具有可复用价值。
- **多视图自适应聚合设计合理**：门控网络模拟临床医生按情境动态调整关注维度；案例研究显示粗/细阶段权重分布会随决策目标合理迁移。
- **级联推理贴合临床实践**：先粗筛高风险再细判等级，与真实分诊流程一致。
- **中层表示利用有据可依**：引用中层语义更丰富的研究，实验也验证其优于末层。
- **评价体系临床导向**：引入显著欠/过度分诊等高风险错误指标，比单一准确率更能反映临床安全性。
- **验证较为立体**：涵盖域内、外部数据集、跨域迁移、消融、规模、架构与专家评估，并公开代码与数据以支持复现。

## 8. 不足与局限

- **语言与数据覆盖**：所有样本与生成内容均为英文，迁移到其他语言需额外语言特定预处理。
- **模型规模受限**：仅探索 0.6B–14B，未验证 30B–70B 等更大模型的效果。
