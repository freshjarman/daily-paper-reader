---
title: "RePrompT: Recurrent Prompt Tuning for Integrating Structured EHR Encoders with Large Language Models"
title_zh: RePrompT：融合结构化EHR编码器与大语言模型的递归提示调优
authors: "Arya Hadizadeh Moghaddam, Drew Ross, Mohsen Nayebi Kerdabadi, Dongjie Wang, Zijun Yao"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.findings-acl.1334.pdf"
tags: ["query:ehr-es"]
score: 8.0
evidence: 结合LLM的EHR序列建模与患者轨迹表示
tldr: 该工作针对将时间戳EHR序列转为文本会丢失时序结构与编码身份、且LLM逐病例孤立推理缺乏共享表示空间的问题，提出RePrompT递归提示调优框架，将结构化EHR编码器与大语言模型集成。方法在保留编码共现与纵向规律的同时学习跨患者的任务对齐表示。实验表明其在纵向临床信息建模与患者轨迹相关任务上优于常规提示方式。该框架为结构化EHR序列建模与基础模型结合提供了可行路径。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1334/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 2219, \"height\": 1030}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1334/fig-002.webp\", \"caption\": \"\", \"page\": 3, \"index\": 2, \"width\": 2586, \"height\": 962}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1334/fig-003.webp\", \"caption\": \"\", \"page\": 3, \"index\": 3, \"width\": 2430, \"height\": 2004}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1334/fig-004.webp\", \"caption\": \"\", \"page\": 7, \"index\": 4, \"width\": 3575, \"height\": 1751}]"
motivation: 将时间戳EHR序列转文本会掩盖时序结构与编码身份，且LLM逐病例推理缺乏共享表示。
method: 提出递归提示调优框架，将结构化EHR编码器与LLM集成以保留编码共现与纵向规律。
result: 在纵向临床信息建模上改善了患者轨迹表示并优于常规提示推理方式。
conclusion: 为结构化EHR序列建模与基础模型的结合提供了有效且可迁移的方案。
---

## Abstract
Large Language Models (LLMs) have shown strong promise for mining Electronic Health Records (EHRs) by reasoning over longitudinal clinical information to capture context-rich patient trajectories. However, leveraging LLMs for structured EHRs (e.g., standardized diagnosis and medication codes) presents two key challenges. First, translating time-stamped EHR sequences into plain text can obscure both temporal structure and code identities, weakening the ability to capture code co-occurrence and longitudinal regularities. Second, unlike cohort-trained predictive models that learn a shared, task-aligned representation space across patients, LLMs are often applied in a case-isolated inference setting where each patient is processed independently without leveraging population-level patterns. To address these challenges, we introduce RePrompT, a time-aware LLM framework that integrates structured EHR encoders through prompt tuning, without modifying underlying architectures. Specifically, RePrompT recurrently incorporates latent states from prior visits to preserve longitudinal information, and injects population-level information through trainable prompt tokens derived from a cohort-trained, task-aligned EHR encoder. Experiments on MIMIC-III and MIMIC-IV demonstrate that RePrompT consistently outperforms both EHR-based and LLM-based baselines across multiple clinical prediction tasks.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：电子健康记录（EHR）包含患者跨多次就诊的诊断、用药、手术等结构化编码，以及出院记录等文本。LLM 在 EHR 挖掘上具有潜力，但直接用于结构化 EHR 存在明显障碍。
- **核心问题一：时序结构弱化**。将带时间戳的多次就诊序列线性化为纯文本，会掩盖就诊间的时间依赖和医学编码的离散身份，不利于建模编码共现与纵向规律。
- **核心问题二：缺乏群体级共享表示**。传统队列训练模型可在全体患者上学习任务对齐的共享表示空间；而 LLM 常以“逐病例孤立推理”方式处理单个患者，难以利用跨患者的人口级模式。
- **整体含义**：论文提出 RePrompT，希望在**不修改 LLM 基础架构**的前提下，把结构化 EHR 编码器通过提示调优接入 LLM，同时保留纵向时序信息与队列级任务对齐表示。

## 2. 方法论

- **核心思想**：将结构化 EHR 编码器学到的患者表示注入 LLM 的软提示中，并让 LLM 在逐次就诊处理时递归传递历史隐藏状态，从而同时实现“时间感知”和“群体感知”的临床预测。
- **问题形式化**：
  - 患者 \(i\) 的就诊序列为 \(\{V_{i,t}\}_{t=1}^{T_i}\)，每次就诊包含医学编码集合和出院记录文本。
  - 目标是基于截至第 \(T_i\) 次就诊的信息，预测第 \(T_i+1\) 次就诊的二分类或多标签临床结局，如再入院、死亡率或用药推荐。
- **三大模块**：
  - **Clinical Records Synthesis**：使用 DeepSeek-V3 对历史出院记录和结构化编码进行去噪、摘要，生成简洁的患者文本摘要 \(\hat{C}_{i,t}\)，作为硬提示输入 LLM。
  - **State-Recurrent Prompt Tuning**：LLM 每次只处理一次就诊，取最后一层 token 隐藏状态并平均池化，得到就诊级隐藏状态 \(\hat{H}_{i,t}\)；再经线性变换生成下一就诊的软提示 \(G_{i,t+1}\)，实现跨就诊的纵向信息传递。
  - **Struct-Encoded Prompt Tuning**：采用 RETAIN 作为结构化 EHR 编码器，对医学编码序列进行双层次注意力建模，得到患者表示 \(S_{i,t}\)，作为另一组软提示注入 LLM。
- **LLM 输入与输出**：
  - 输入提示由三部分拼接：状态递归软提示 \(G_{i,t}\)、结构化编码软提示 \(S_{i,t}\)、患者摘要 token 嵌入。
  - 使用 Llama 3.1 1B + LLM2Vec 提取高质量嵌入，LLaMA 主干冻结。
  - 最终就诊隐藏状态接入线性分类头，经阈值得到预测；训练使用 Adam 和二元交叉熵损失。
- **可训练组件**：RETAIN 编码器、状态递归的线性变换层、输出分类层；LLM 本身不更新。

## 3. 实验设计

- **数据集**：
  - **MIMIC-III**：重症监护入院记录，论文聚焦多次就诊患者。
  - **MIMIC-IV**：更大规模、模块化结构更清晰的 EHR 数据集。
  - 两者均公开、去标识化，在 PhysioNet 许可协议下使用。
- **任务与指标**：
  - 主要任务：再入院预测、死亡率预测。
  - 指标：AUROC、PRAUC。
  - 附录任务：药物推荐，使用 F1 与 Jaccard 相似度。
- **Benchmark 与对比方法**：
  - **EHR 深度模型基线**：Deepr、RETAIN、GRAM、GRASP、AdaCare、StageNet、Adore、ARCI。
  - **LLM 基线**：GPT-5 零样本提示、Prompt-Tuning、COCONUT。
  - 消融：去除两个模块、去除 State-Recurrent、去除 Struct-Encoded、去除 DeepSeek 摘要。
  - 编码器替换实验：RETAIN、LSTM、Transformer Encoder。
- **实验设置**：
  - 随机 70% 训练、30% 测试，报告三次运行均值。
  - 贪心搜索超参数；软提示数量设为 \(P=10\)；RETAIN 隐藏维度 256。
  - 排除仅有一次就诊的患者，以满足纵向预测需求。

## 4. 资源与算力

- **硬件**：使用一台高性能服务器，配备 **3 块 NVIDIA A6000 GPU、256 GB RAM、48 核 CPU**。
- **框架**：PyTorch、PyHealth、Hugging Face。
- **计算时间**：附录报告处理 8 名患者批次时，RePrompT 推理约 **1.44 秒**，高于多数传统深度模型基线，但作者认为仍可支持现实临床场景。
- **未明确说明**：论文未报告总训练时长、GPU 小时数、能耗、碳排或完整训练成本。

## 5. 实验数量与充分性

- **实验规模**：
  - 两个大规模数据集：MIMIC-III、MIMIC-IV。
  - 两个主任务：再入院、死亡率。
  - 一个附录任务：药物推荐。
  - 对比 8 个 EHR 基线、3 个 LLM 基线。
  - 多组消融：模块消融、输入摘要消融、不同 EHR 编码器消融。
  - 报告计算时间分析。
- **充分性评价**：
  - 覆盖多数据集、多任务、多基线、多消融，整体较充分。
  - 使用 AUROC/PRAUC 等阈值无关指标，并报告三次运行均值，具有一定客观性。
  - 但两个数据集均来自 MIMIC 体系，外部泛化验证有限。
  - 未报告置信区间、标准差或统计显著性检验，难以判断提升是否稳定显著。
  - 超参数搜索细节和基线调参公平性描述较简略。
  - LLM 基线中零样本使用 GPT-5，而本地模型为 Llama 3.1 1B，模型规模和访问条件不同，比较需谨慎解读。

## 6. 主要结论与发现

- RePrompT 在 MIMIC-III 和 MIMIC-IV 的再入院、死亡率预测上，整体优于传统 EHR 基线和 LLM 基线。
- 在 MIMIC-IV 再入院任务中，RePrompT AUROC 达 0.706、PRAUC 达 0.728，优于 RETAIN、StageNet 等强基线。
- 在死亡率预测中，RePrompT 也取得一致提升，说明时间感知提示与结构化编码器结合有效。
- 消融显示：**State-Recurrent 模块贡献更大**，说明显式建模就诊间时序依赖至关重要；Struct-Encoded 模块提供互补的群体级结构化信息。
- 去除 DeepSeek 摘要后性能仍优于 RETAIN 主干，表明提升不仅来自摘要，而来自整体框架；但去噪摘要仍有增益。
- 药物推荐附录中，RePrompT 在 F1 和 Jaccard 上表现较强，说明框架可扩展到多标签临床任务。

## 7. 优点

- **架构友好**：不修改 LLM 主干，仅训练软提示、EHR 编码器和分类头，参数高效、模块化强。
- **时间感知明确**：通过隐藏状态递归传递显式建模多次就诊间的纵向依赖，优于纯文本线性化。
- **群体级表示注入**：用队列训练的 RETAIN 编码器生成软提示，使 LLM 能利用跨患者共享模式。
- **硬提示与软提示结合**：既保留临床文本摘要的语义，又注入结构化 EHR 表示。
- **实验较全面**：覆盖两个 MIMIC 数据集、多个任务、多类基线和多组消融，并开源代码。
- **临床可迁移性**：与 PyHealth 兼容，便于后续在医疗预测工具链中复现和扩展。

## 8. 不足与局限

- **数据依赖与域偏移**：框架依赖 EHR 数据质量，换到其他医疗系统时可能受域偏移影响，泛化性未充分验证。
- **任务覆盖仍有限**：作者指出未来需扩展到更多临床预测任务；当前主要是再入院、死亡率和附录药物推荐。
- **外部验证不足**：仅使用 MIMIC-III/IV，二者来源相关，缺少独立医院或跨国数据验证。
- **统计严谨性有限**：未报告方差、置信区间或显著性检验，提升幅度是否统计显著不明确。
- **计算开销较高**：推理时间 1.44 秒/8 患者，虽可接受，但高于传统模型，实际部署需考虑延迟与成本。
- **训练成本未披露**：未说明训练时长、GPU 小时和能耗，影响可复现性与绿色 AI 评估。
- **隐私与伦理风险**：若使用未充分去标识化的 EHR 数据，存在患者隐私泄露风险，需遵守数据保护法规。
- **可解释性与公平性未深入评估**：未系统分析模型在不同人群、不同疾病亚组上的偏差或临床可解释性。

（完）
