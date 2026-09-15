---
title: "EMSDialog: Synthetic Multi-person Emergency Medical Service Dialogue Generation from Electronic Patient Care Reports via Multi-LLM Agents"
title_zh: EMSDialog：基于电子患者护理报告的多LLM智能体合成多人急救对话生成
authors: "Xueren Ge, Sahil Murtaza, Anthony Cortez, Homa Alemzadeh"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.findings-acl.1751.pdf"
tags: ["query:ehr-es"]
score: 4.0
evidence: 基于患者护理报告合成临床对话
tldr: 会话式诊断预测需要模型跟踪流式临床对话中的证据，但现有医学对话语料多为双方且缺少多方流程标注。本文提出基于电子患者护理报告的主题流多智能体生成流程，迭代规划、生成并自检对话。由此构建了4414段带43种诊断与话题标注的合成急救对话数据集，为多方临床对话建模提供资源。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1751/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 849, \"height\": 427}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1751/fig-002.webp\", \"caption\": \"\", \"page\": 4, \"index\": 2, \"width\": 1671, \"height\": 779}]"
motivation: 现有医学对话语料缺乏多方工作流与细粒度标注。
method: 提出基于ePCR的主题流多智能体生成与自检流程构建EMSDialog。
result: 生成4414段多人急救对话，含43种诊断、角色与话题标注。
conclusion: 为会话式诊断预测提供了合成多方临床对话数据集。
---

## Abstract
Conversational diagnosis prediction requires models to track evolving evidence in streaming clinical conversations and decide when to commit to a diagnosis. Existing medical dialogue corpora are largely dyadic or lack the multi-party workflow and annotations needed for this setting. We introduce an ePCR-grounded, topic-flow-based multi-agent generation pipeline that iteratively plans, generates, and self-refines dialogues with rule-based factual and topic flow checks. The pipeline yields EMSDialog, a dataset of 4,414 synthetic multi-speaker EMS conversations based on a real-world ePCR dataset, annotated with 43 diagnoses, speaker roles, and turn-level topics. Human and LLM evaluations confirm high quality and realism of EMSDialog using both utterance- and conversation-level metrics. Results show that EMSDialog-augmented training improves accuracy, timeliness, and stability of EMS conversational diagnosis prediction. Our datasets and code are publicly available at https://uva-dsa.github.io/EMSDialog

---

## 论文详细总结（自动生成）

# EMSDialog 论文中文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **任务背景**：会话式诊断预测要求模型在流式临床对话中持续跟踪不断演化的证据，逐轮更新诊断信念，并决定何时“提交”诊断、何时“推迟”以收集更多信息。这对急救（EMS）等时间敏感场景尤其关键。
- **现有数据不足**：
  - 在线医患对话数据集多来自中文论坛，异步、双方对话，偏离真实临床工作流，诊断标签有限。
  - 基于 EHR 的人类角色扮演数据集虽更真实，但通常仍为双方对话，且缺少细粒度诊断标注。
  - 规则或 LLM 合成数据虽可扩展，但常忽视真实话题流、多参与方设置和下游任务所需标注。
- **EMS 场景特点**：急救过程天然多参与方，包括急救员、搭档、调度员、患者、旁观者等，不同角色提供不同证据（现场安全、主诉、用药、最后正常时间等），需要多方协作式对话数据。
- **零样本 LLM 的局限**：现有 LLM 作为会话诊断代理时，容易在证据稀疏时过早给出高置信错误判断，并随新信息到来频繁切换预测，稳定性差。
- **论文目标**：提出基于真实 ePCR（电子患者护理报告）的多智能体合成对话生成流程，构建 **EMSDialog** 数据集，用于训练和评估会话式诊断预测模型，提升预测准确性、及时性和稳定性。

## 2. 方法论：核心思想与关键技术细节

### 2.1 核心思想

- 以真实 ePCR 为事实 grounding，以官方 EMS 话题流为结构约束，采用多 LLM 智能体进行“规划—生成—自精炼”的迭代循环。
- 引入确定性规则检查器（概念检查、话题流检查）和 LLM 风格检查器，形成 **repeat-until-pass** 的硬约束闭环，只有通过检查才能进入下一阶段。
- 目标是在保证临床事实性和流程真实性的同时，生成自然、多说话人、带诊断和话题标注的 EMS 对话。

### 2.2 五个核心模块

- **Extractor（概念抽取）**：
  - 结构化字段用正则解析。
  - 非结构化 medic narrative 用 MedSpaCy + QuickUMLS 做临床 NER，并限定 UMLS 语义类型（TUIs）以减少噪声。
  - 用正则抽取 GCS 等控制话题流的关键特征。例如 GCS ≤ 8（昏迷）时从 Primary Assessment 开始；GCS > 8（清醒）时从 HPI / Pain
