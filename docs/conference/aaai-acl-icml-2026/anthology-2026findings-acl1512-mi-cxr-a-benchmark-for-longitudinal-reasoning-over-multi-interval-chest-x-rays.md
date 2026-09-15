---
title: "MI-CXR: A Benchmark for Longitudinal Reasoning over Multi-Interval Chest X-rays"
title_zh: MI-CXR：多区间胸片的纵向推理基准
authors: "Sunghwan Steve Cho, Yunseok Han, Jaeyoung Do"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.findings-acl.1512.pdf"
tags: ["query:ehr-es"]
score: 4.0
evidence: 面向多访次患者时间线序列的纵向推理基准
tldr: 纵向胸片解读需要跨多次就诊推理疾病演变，但现有医学VQA基准多聚焦单图或短时图像对。本文提出MI-CXR基准，基于五次就诊的患者时间线构造多选问答，涵盖时序事件定位、区间变化推理与全局轨迹总结三类任务。评测14个模型揭示纵向视觉推理的不足，为患者轨迹层面的时间推理评估提供了标准化平台。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1512/fig-001.webp\", \"caption\": \"\", \"page\": 21, \"index\": 1, \"width\": 1488, \"height\": 1238}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1512/fig-002.webp\", \"caption\": \"\", \"page\": 21, \"index\": 2, \"width\": 1031, \"height\": 1238}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1512/fig-003.webp\", \"caption\": \"\", \"page\": 21, \"index\": 3, \"width\": 1488, \"height\": 1238}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1512/fig-004.webp\", \"caption\": \"\", \"page\": 21, \"index\": 4, \"width\": 1488, \"height\": 1238}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1512/fig-005.webp\", \"caption\": \"\", \"page\": 21, \"index\": 5, \"width\": 1488, \"height\": 1238}]"
motivation: 纵向胸片解读需跨多次就诊推理疾病演变，而现有医学VQA基准多限于单图或短时图像对。
method: 构建MI-CXR基准，基于五访次患者时间线设计时序事件定位、区间变化推理与轨迹总结任务。
result: 对14个模型的评测揭示了纵向视觉推理能力的不足。
conclusion: 该基准为患者轨迹层面的时间推理评估提供了标准化手段。
---

## Abstract
Longitudinal chest X-ray (CXR) interpretation requires reasoning over disease evolution across multiple patient visits, yet most existing medical VQA benchmarks focus on single images or short-horizon image pairs. We introduce **MI-CXR**, a benchmark for standardized evaluation of **M**ulti-**I**nterval longitudinal reasoning over multi-visit **CXR** sequences, without requiring free-form report generation or additional clinical context. MI-CXR comprises five-way multiple-choice questions over five-visit patient timelines and instantiates three complementary task families: Temporal Event Localization, Interval-wise Change Reasoning, and Global Trajectory Summarization, which assess clinically grounded visual reasoning over time. Evaluating 14 state-of-the-art vision–language models (VLMs) shows low overall performance (29.3% accuracy), only modestly above random guessing. Using stage-wise diagnostic probing, we find that models often produce locally plausible interval descriptions but fail to enforce temporal constraints or compose evidence into globally consistent decisions over the full timeline. These findings reveal key limitations of current VLMs and establish MI-CXR as a principled benchmark for longitudinal medical reasoning. The benchmark is available at: https://github.com/AIDASLab/MI-CXR

---

## 论文详细总结（自动生成）

论文：**MI-CXR: A Benchmark for Longitudinal Reasoning over Multi-Interval Chest X-rays**（ACL 2026 Findings）。以下按要点总结。

## 1. 核心问题与整体含义
- **研究动机**：纵向胸片解读需要跨多次就诊推理疾病发生、进展、缓解、复发与治疗反应，但现有医学 VQA 基准多聚焦单图识别或双图短期比较，无法评估长时程、多访次的临床时间推理。
- **核心问题**：当前 VLM 能否在多次就诊的胸片序列上进行结构化纵向推理，而不仅是描述局部图像变化？
- **整体含义**：作者提出 **MI-CXR**，将纵向医学 VQA 形式化为多区间、多访次时间线上的全局推理问题，并揭示当前模型的主要瓶颈不仅是视觉感知，更是时间决策与全局证据整合。

## 2. 方法论
- **核心思想**：基于五次就诊患者时间线构造五选一多选题，要求正确答案必须聚合多个访次的信息，不能依赖单图或单对图像。
- **任务族**：
  - **Temporal Event Localization, TEL**：定位异常出现、消失、复发等事件发生在哪个区间，包括 Single E/R、Multiple E/R、E→R / R→E。
  - **Interval-wise Change Reasoning, ICR**：推理相邻访次间的变化，但相关区间不预先给出，需先定位再解释。
  - **Global Trajectory Summarization, GTS**：整合所有访次证据，总结单异常或多异常的全局轨迹。
- **数据构建**：
  - 使用 **MIMIC-CXR-JPG** 图像与 **MIMIC-Ext-CXR-QBA** 结构化注释。
  - 保留至少 5 次有效就诊的患者，构造 5 访次、4 个连续区间的窗口；窗口大小 5，步长 1。
  - 基于质量属性过滤，只保留高置信、明确标注 present/absent 的疾病相关观察。
- **QA 生成**：
  - 正确答案由注释重组为时间一致陈述；干扰项通过受控事实翻转生成，保持医学上合理但确定错误。
  - LLM 仅用于表层语言实现，不决定时间顺序、异常存在性或答案正确性。
  - 最终保留 **5,311** 个高质量五选一实例；答案位置均匀分布，异常类型按频率采样。
- **评估协议**：
  - 主实验为零样本提示，确定性解码，输出 A–E，规则提取，精确匹配计分。
  - 另有阶段式诊断：第一阶段生成区间级描述，第二阶段仅基于描述作答，以分离局部证据表达与最终决策。

## 3. 实验设计
- **数据集 / 场景**：基于 MIMIC-CXR 的多次就诊胸片时间线；每个实例包含 5 次访次图像、自然语言问题和 5 个选项。
- **Benchmark**：MI-CXR，含 TEL、ICR、GTS 三类任务；另构造 **ICR Variant**（400 题），明确指定目标区间，用于隔离区间定位与变化解释。
- **对比方法**：评估 14 个 SOTA VLM，分为三类：
  - 闭源通用：Claude Sonnet 4.5、Gemini 3.0 Pro、GPT-5.2。
  - 开源通用：InternVL3.5-8B/14B/38B、QwenVL3-8B/32B、DeepSeek-VL-16B、IDEFICS2-8B。
  - 医学专用：Lingshu-7B/32B、MedGemma-4B/27B。
- **补充实验**：
  - 温度 0.7 敏感性分析。
  - ICR Variant
