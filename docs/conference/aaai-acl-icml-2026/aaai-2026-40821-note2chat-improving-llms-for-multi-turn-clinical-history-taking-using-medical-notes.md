---
title: "Note2Chat: Improving LLMs for Multi-Turn Clinical History Taking Using Medical Notes"
title_zh: Note2Chat：利用医疗病历提升大语言模型多轮临床病史采集能力
authors: "Yang Zhou, Zhenting Sheng, Mingrui Tan, Yuting Song, Jun Zhou, Yu Heng Kwan, Lian Leng Low, Yang Bai, Yong Liu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40821/44782"
tags: ["query:ehr-es"]
score: 4.0
evidence: 基于病历的临床问诊与诊断
tldr: 针对大模型在动态多轮临床问诊与诊断中表现不足、且对话数据稀缺敏感的问题，本文提出Note2Chat框架，用决策树引导的生成与精炼流程将真实医疗病历转化为高质量医患对话，并设计三阶段微调策略训练模型进行结构化问诊与诊断。实验表明该方法在临床病史采集与诊断任务上得到提升。该工作与临床事件与病历文本建模相关，但侧重对话式问诊而非EHR事件序列建模。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 大模型在动态多轮临床问诊与诊断中表现不足，且真实对话数据稀缺敏感。
method: 提出Note2Chat，用决策树流程将病历转为医患对话并做三阶段微调。
result: 在结构化病史采集与诊断任务上取得性能提升。
conclusion: 为基于病历训练临床问诊对话模型提供了可行路径。
---

## Abstract
Effective clinical history taking is a foundational yet underexplored component of clinical reasoning. While large language models (LLMs) have shown promise on static benchmarks, they often fall short in dynamic, multi-turn diagnostic settings that require iterative questioning and hypothesis refinement. To address this gap, we propose Note2Chat, a note-driven framework that trains LLMs to conduct structured history taking and diagnosis by learning from widely available medical notes. Instead of relying on scarce and sensitive dialogue data, we convert real-world medical notes into high-quality doctor-patient dialogues using a decision tree-guided generation and refinement pipeline. We then propose a three-stage fine-tuning strategy combining supervised learning, simulated data augmentation, and preference learning. Furthermore, we propose a novel single-turn reasoning paradigm that reframes history taking as a sequence of single-turn reasoning problems. This design enhances interpretability and enables local supervision, dynamic adaptation, and greater sample efficiency. Experimental results show that our method substantially improves clinical reasoning, achieving gains of +16.9 F1 and +21.0 Top-1 diagnostic accuracy over GPT-4o.

---

## 论文详细总结（自动生成）

# Note2Chat 论文中文总结

## 1. 核心问题与整体含义

- **研究动机**：临床病史采集（history taking）和鉴别诊断是临床推理的基础，但现有大语言模型（LLM）主要在静态、单轮医学基准上表现良好，在真实动态、多轮、需要主动提问和逐步修正假设的诊断场景中明显不足。
- **关键矛盾**：
  - 高质量医患对话数据稀缺、敏感、难获取；
  - 医学病历（medical notes）则广泛可得，且包含主诊断、现病史（HPI）、症状演变和临床推理结果；
  - 现有多轮临床对话研究多关注最终诊断准确率，忽视病史采集质量、阴性发现、症状语境和问诊效率。
- **整体含义**：论文提出 **Note2Chat**，一种以病历为监督信号的框架，把病历转化为高质量医患对话，训练 LLM 进行结构化多轮病史采集和鉴别诊断。其目标不是只优化诊断答案，而是让模型用更少问题获取更多临床相关信息，并自主决定何时停止提问、给出诊断。

## 2. 方法论

### 2.1 核心思想

- 将病史采集形式化为**部分可观察的序列决策过程**：医生 agent 在每轮观察状态 \(s_t=\{cc,h_t\}\)，其中 \(cc\) 是主诉，\(h_t\) 是已发生的问答历史。
- 动作空间包括：
  - 提问 \(a_t \in A_{\text{ask}}\)；
  - 给出诊断 \(a_t \in A_{\text{diagnose}}\)。
- 模拟患者基于真实病例 \(x=\{d_x,F,cc\}\) 回答，其中 \(d_x\) 是真诊断，\(F\) 是从 HPI 抽取的临床发现集合。
- 学习目标：训练策略 \(\pi_\theta(a_t|s_t)\)，最大化对话轨迹奖励，奖励同时衡量信息采集、诊断准确性和问诊效率。

### 2.2 数据构建：从病历到对话

- **来源**：MIMIC-IV 出院病历，使用 ICD-10 选择心衰、蜂窝织炎及相关疾病。
- **疾病范围**：10 类：Asthma、COPD、Cellulitis、Chronic venous insufficiency、Deep vein thrombosis、Erysipelas、Heart Failure、Necrotising Fasciitis、Pneumonia、Trauma/hematoma。
- **纳入条件**：有明确 HPI、主诊断、至少 100 词。
- **三步流程**：
  1. **Finding extraction**：从 HPI 提取临床发现，排除实验室、治疗、随访等问诊时不可知信息；
  2. **Decision tree-guided dialogue generation**：构建“发现—候选诊断”决策树，引导 LLM 生成贴近鉴别诊断流程的医患对话；
  3. **Critic and revision**：用 LLM critic 检查遗漏关键发现、上下文泄漏、医生过早推断未披露症状等问题，并补问或修正。
- **数据规模**：4,972 名
