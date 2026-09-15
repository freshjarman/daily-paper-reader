---
title: "EHRStruct: A Comprehensive Benchmark Framework for Evaluating Large Language Models on Structured Electronic Health Record Tasks"
title_zh: EHRStruct：面向结构化电子健康记录任务的大模型综合评测基准
authors: "Xiao Yang, Xuejiao Zhao, Zhiqi Shen"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40731/44692"
tags: ["query:ehr-es"]
score: 8.0
evidence: 评估大模型在结构化电子健康记录任务上的基准
tldr: 结构化电子健康记录以关系表存储患者信息并在临床决策中居核心地位，近期研究尝试用大模型处理此类数据，但缺乏标准化评测框架与明确任务定义。本文提出EHRStruct基准，定义覆盖多种临床需求的11类任务并构建2200条测试样本，系统评估大模型在结构化EHR上的表现。该基准为EHR序列与结构化数据建模提供了统一评测基础。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 结构化EHR数据在临床决策中至关重要，但用大模型处理时缺乏标准化评测框架与明确任务定义。
method: 提出EHRStruct基准，定义11类代表性临床任务并构建2200条测试样本以评测大模型。
result: 基准系统揭示了大模型在结构化EHR任务上的能力与不足。
conclusion: 该基准为结构化EHR建模提供了统一可比的评测平台。
---

## Abstract
Structured Electronic Health Record (EHR) data stores patient information in relational tables and plays a central role in clinical decision-making. 
Recent advances have explored the use of large language models (LLMs) to process such data, showing promise across various clinical tasks.
However, the absence of standardized evaluation frameworks and clearly defined tasks makes it difficult to systematically assess and compare LLM performance on structured EHR data.
To address these evaluation challenges, we introduce EHRStruct, a benchmark specifically designed to evaluate LLMs on structured EHR tasks.
EHRStruct defines 11 representative tasks spanning diverse clinical needs and includes 2,200 task-specific evaluation samples derived from two widely used EHR datasets.
We use EHRStruct to evaluate 20 advanced and representative LLMs, covering both general and medical models.
We further analyze key factors influencing model performance, including input formats, few-shot generalisation, and finetuning strategies, and compare results with 11 state-of-the-art LLM-based enhancement
methods for structured data reasoning. 
Our results indicate that many structured EHR tasks place high demands on the understanding and reasoning capabilities of LLMs.
In response, we propose SEMaster, a code-augmented method that achieves state-of-the-art performance and offers practical insights  to guide future research.

---

## 论文详细总结（自动生成）

# EHRStruct 论文中文结构化总结

## 1. 核心问题与整体含义

- **研究背景**：结构化电子健康记录（EHR）以关系表形式存储患者诊断、用药、检验结果等信息，并常带时间戳，是临床决策的重要数据基础。传统上多依赖 SQL 查询等方法，而大语言模型（LLM）具备更强推理能力、自然语言交互能力和灵活性，因此被越来越多地用于结构化 EHR 建模。
- **核心问题**：现有研究在将 LLM 应用于结构化 EHR 时，缺乏统一的评测框架和明确的任务定义，导致：
  - 任务覆盖有限，多集中于疾病预测、死亡风险估计、信息抽取、表格算术推理等；
  - 同一任务常用不同数据集和评测协议，难以复现和公平比较；
  - 输入格式和实验设置不统一；
  - 评测指标解释性不足，难以判断模型成功或失败的具体推理能力。
- **整体含义**：论文提出 **EHRStruct**，一个面向结构化 EHR 任务的综合基准框架，旨在系统评估通用与医学 LLM 在结构化 EHR 上的能力，并进一步提出 **EHRMaster** 方法以提升结构化 EHR 推理表现。

## 2. 方法论：核心思想与关键技术细节

- **EHRStruct 基准设计**：
  - 定义 **11 个代表性任务**，归入 **6 个任务类别**：
    - 信息检索：D-U1、D-U2
    - 数据聚合：D-R1、D-R2、D-R3
    - 算术计算：D-R4、D-R5
    - 临床识别：K-U1
    - 诊断评估：K-R1、K-R2
    - 治疗规划：K-R3
  - 任务按两个正交维度分类：
    - **评估场景**：Data-Driven vs. Knowledge-Driven
    - **认知层级**：Understanding vs. Reasoning
  - 指标：数据驱动任务多用 Accuracy，知识驱动任务多用 AUC。
- **任务合成与样本构建**：
  - 由 CS 研究者从既有研究与建模范式中蒸馏任务，医学专家审核临床相关性。
  - 使用两个数据源：
    - **Synthea**：合成 EHR 数据，无隐私问题；
    - **eICU Collaborative Research Database**：真实世界 ICU 多中心结构化数据。
  - 每个任务每个数据集构建 100 条评测样本，共 **2,200 条**标注实例。
  - 使用 GPT-4o 根据任务定义、表结构和采样内容生成问答对，并进行两阶段验证：医学审阅者检查答案正确性与合理性，技术审阅者检查问题是否忠实于任务目标和输入语义。
- **输入格式设计**：
  - 4 种结构化数据转文本格式：
    - Plain Text Conversion
    - Special Character Separation
    - Graph-Structured Representation
    - Natural Language Description
- **EHRMaster 方法**：
  - 三阶段流程：
    1. **Solution Planning**：根据问题生成高层自然语言解题计划，分解推理步骤；
    2. **Concept Alignment**：将计划中的抽象概念映射到结构化 EHR 数据中的字段和表；
    3. **Adaptive Execution**：自适应选择“生成代码执行”或“直接语言推理”来检索证据并得出答案。
  - 示例：医院费用估计任务中，EHRMaster 生成 Python 代码按入院/出院时间过滤 billing entries 并计算总成本；在异质临床事件治疗效果评估中，则可能绕过代码，采用基于对齐数据的多步语言推理。
  - 注：正文称该方法为 **EHRMaster**；摘要中一处写作 **SEMaster**，疑为笔误。

## 3. 实验设计

- **数据集/场景**：
  - **Synthea**：合成结构化 EHR 数据；
  - **eICU**：真实世界 ICU 结构化数据。
  - 每个任务在每个数据集上 100 条样本，合计 2,200 条；主结果表展示 Synthea 上结果，eICU 结果在附录。
- **评测模型**：
  - 共评估 **20 个 LLM**：
    - 11 个通用模型：GPT-3.5 Turbo、GPT-4.1、Gemini 1.5、Gemini 2.0、Gemini 2.5、DeepSeek-V2.5、DeepSeek-V3、Qwen-7B/14B/32B/72B；
    - 9 个医学模型：Huatuo、HEAL、Meditron-7B、MedAlpaca-13B、JMLR、PMC LLaMA 13B、Med42-70B、Apollo、CancerLLM。
  - 参数规模覆盖 7B 到 685B，包含开源与商业闭源模型。
- **实验设置**：
  - 主要为零样本（zero-shot）；
  - 额外测试 1-shot、3-shot、5-shot；
  - 比较 4 种输入格式；
  - 进行单任务与多任务微调实验；
  - 复现并评估 **11 种 LLM-based 增强方法**：
    - 非医学 8 种：C.L.E.A.R.、TaT、TableMaster、TIDE、E5、GraphOTTER、H-STAR、Table-R1；
    - 医学 3 种：LLM4Healthcare、DeLLiriuM、EnsembleLLM；
  - 将 EHRMaster 与上述 SOTA 增强方法比较。
- **评测细节**：
  - 所有评测采用单轮生成，使用一致的解码参数（如 temperature、最大 token 限制）以保证公平比较。
  - 微调使用 Qwen-7B + LoRA，配置为：10% 验证集、学习率 0.0001、3 epochs、batch size 8、LoRA rank 8、alpha 32、dropout 0.05。

## 4. 资源与算力

- 论文中**未明确说明**使用的 GPU 型号、数量、训练时长或总计算资源。
- 仅披露了微调配置：
  - Qwen-7B；
  - LoRA 微调；
  - 10% 验证集；
  - 学习率 0.0001；
  - 3 epochs；
  - batch size 8；
  - LoRA rank 8、alpha 32、dropout 0.05。
- 因此，无法从论文文本判断其实际算力开销和训练环境。

## 5. 实验数量与充分性

- **实验规模**：
  - 20 个 LLM × 11 个任务 × 每任务 200 条样本，若全部运行，零样本评测规模约为 **44,000 次模型推理**；
  - 额外进行 few-shot 实验，至少覆盖 Gemini 1.5、Gemini 2.0、Gemini 2.5 在 K-R1、K-R2、K-R3 等知识驱动任务上的 0/1/3/5-shot 比较；
  - 输入格式实验覆盖 4 种格式；
  - 微调实验覆盖单任务与多任务策略；
  - 复现并比较 11 种增强方法；
  - EHRMaster 与 previous SOTA 在多个任务和 Gemini 系列模型上比较。
- **充分性**：
  - 任务覆盖较广，包含数据驱动与知识驱动、理解与推理，兼顾合成与真实 EHR 数据；
  - 模型数量多，覆盖通用/医学、开源/闭源、不同参数规模；
  - 对比方法较多，包括非医学和医学专用增强方法；
  - 实验设计整体较系统，具备一定可复现性，并提供了代码与项目页面。
- **公平性与客观性**：
  - 使用统一解码参数和任务特定样本，有利于公平比较；
  - 但 few-shot 主要集中于 Gemini 系列和部分知识驱动任务，未覆盖所有模型；
  - 微调只使用 Qwen-7B，结论外推需谨慎；
  - 商业闭源模型不可完全复现；
  - 问答样本由 GPT-4o 生成并经专家验证，但仍可能存在生成偏差或标注主观性。

## 6. 主要结论与发现

- **通用 LLM 优于医学 LLM**：通用模型在几乎所有结构化 EHR 任务上持续优于医学模型；医学模型在知识驱动任务中常无法输出有效结果，且没有任何医学模型进入任何任务前三。
- **闭源商业模型表现最佳**：尤其是 Gemini 系列，整体性能最高，说明广泛预训练可能间接支持结构化数据理解。
- **数据驱动任务优于知识驱动任务**：LLM 在数据驱动任务上表现更好；知识驱动任务对临床知识和复杂推理要求更高，模型普遍困难。
- **输入格式影响性能**：
  - 自然语言描述有利于数据驱动推理任务；
  - 图结构提示有利于数据驱动理解任务；
  - 知识驱动任务中没有一种格式能带来一致提升。
- **Few-shot 有益但非越多越好**：1-shot 和 3-shot 通常优于 5-shot；Gemini 2.0/2.5 对上下文示例更敏感。
- **多任务微调优于单任务微调**：两者都能提升性能，但联合训练有助于学习共享结构和推理模式。
- **增强方法具有场景特异性**：
  - 非医学方法在数据驱动任务上提升更大，但在知识驱动任务上有限；
  - 医学专用方法在知识驱动任务上更好，但难以泛化到数据驱动场景；
  - 现有方法无法在全谱结构化 EHR 任务上一致提升。
- **EHRMaster 表现**：
  - 在数据驱动任务上，尤其算术密集型 D-R4、D-R5，常达到 100% 准确率；
  - 在知识驱动任务如 K-R2、K-R3 上有明显提升，但增益因模型和任务而异；
  - 整体达到 SOTA 或竞争性表现，尤其在数据驱动结构化推理上优势显著。

## 7. 优点

- **任务体系清晰**：按场景和认知层级二维分类，增强评测解释性，便于分析模型能力边界。
- **数据来源互补**：同时使用合成数据 Synthea 和真实 ICU 数据 eICU，兼顾隐私安全与真实临床复杂性。
- **评测维度丰富**：覆盖 zero-shot、few-shot、输入格式、微调策略、增强方法比较，实验设计较全面。
- **模型覆盖广**：评估 20 个通用与医学 LLM，包含开源/闭源、不同规模，具有较强代表性。
- **方法创新**：EHRMaster 通过“规划—概念对齐—自适应执行”结合代码与语言推理，在结构化 EHR 任务上取得显著效果。
- **可复现性较好**：提供代码仓库、项目页面和扩展版本链接。
- **临床与工程结合**：任务由 CS 研究者与医学专家共同审核，兼顾技术可行性与临床相关性。

## 8. 不足与局限

- **算力信息缺失**：未报告 GPU 型号、数量、训练时长等，难以评估资源需求和可复现成本。
- **数据覆盖有限**：仅使用 Synthea 和 eICU 两个数据源；eICU 为 ICU 场景，向普通门诊或全科 EHR 泛化能力未知。
- **样本生成依赖 GPT-4o**：问答对由 GPT-4o 生成，虽经专家验证，但仍可能引入生成偏差、覆盖偏差或标注主观性。
- **Few-shot 实验不全面**：主要集中于 Gemini 系列和部分知识驱动任务，未覆盖所有模型和任务。
- **微调结论外推有限**：微调实验仅基于 Qwen-7B + LoRA，不同模型和规模上的结论可能不同。
- **闭源模型不可复现**：GPT、Gemini 等商业模型不可完全复现，可能影响长期可重复性。
- **增强方法复现风险**：11 种增强方法的复现质量、超参数调优和公平性未完全展开。
- **知识驱动任务仍困难**：即使 EHRMaster 在知识驱动任务上有提升，整体性能仍有限，说明临床知识融合和复杂推理仍是开放问题。
- **评测指标解释性仍可加强**：虽然任务分类提升了解释性，但对失败原因、错误类型和推理链质量的细粒度分析仍较少。

（完）
