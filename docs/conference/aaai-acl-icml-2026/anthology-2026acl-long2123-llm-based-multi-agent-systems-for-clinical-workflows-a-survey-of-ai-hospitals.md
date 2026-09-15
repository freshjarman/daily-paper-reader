---
title: "LLM-Based Multi-Agent Systems for Clinical Workflows: A Survey of AI Hospitals"
title_zh: 面向临床工作流的LLM多智能体系统：AI医院综述
authors: "Zonghai Yao, Hong Yu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://aclanthology.org/2026.acl-long.2123.pdf"
tags: ["query:ehr-es"]
score: 4.0
evidence: 临床工作流多智能体与EHR决策支持
tldr: 临床工作流中的决策支持需要协调多角色、共享状态与EHR证据。本文综述LLM多智能体系统，提出以工作流层级（角色与交接、记忆与证据、工具与安全审计）组织AI医院相关研究。作者主张按工作流而非单一模型组件比较系统，为临床多智能体系统的评估与设计提供统一框架。
source: ACL-2026-Long
selection_source: conference_retrieval
motivation: 临床决策支持系统缺乏在工作流层面统一比较的框架。
method: 综述LLM多智能体系统，提出角色、记忆、工具、安全门等维度的分类体系。
result: 归纳出应以状态转移与交接来衡量临床智能体系统。
conclusion: 主张从工作流层级评估AI医院系统的行动、证据与问责。
---

## Abstract
This survey reviews LLM-based multi-agent systems for clinical and healthcare workflows, including diagnosis, triage, consultation, discharge, mental health, and EHR-linked decision support. We define AI hospitals as workflow-level clinical systems in which agents take explicit roles, hand off shared state, use EHR- or guideline-grounded tools, and operate with safety gates and audit-ready logs. We argue that these systems should be compared at the workflow level, rather than only by model components or end-task accuracy, because clinical action, evidence, and accountability are expressed through state transitions and handoffs. We organize the literature through a workflow-level taxonomy covering roles and handoffs, memory and evidence, tools, and reasoning, control, and escalation. We further synthesize major workflow settings and task families, introduce a four-layer evaluation stack spanning safety, process, outcome, and operations, and connect model capabilities to workflow observables relevant to deployment. Finally, we present Integration Readiness Levels (IRL1-IRL6), task-level instrumentation requirements, and recurring workflow failure modes as a practical framework for comparing, evaluating, and deploying clinical LLM agents and AI hospitals.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究动机**：LLM 正从孤立文本生成走向临床工作流中的智能体化作业。医学领域的评估也逐渐从考试式、静态 QA 基准转向交互式患者任务、对话诊断和虚拟 EHR 环境。
- **关键缺口**：近期综述仍发现前瞻性证据有限、操作层报告稀疏，且基准性能提升与真实临床工作流结果之间联系薄弱。问题不再是“模型能否回答问题”，而是“系统能否在分诊、咨询、出院等阶段之间传递病例而不丢失状态、证据与问责”。
- **核心主张**：应以**工作流层级**而非仅模型组件或最终任务准确率来比较临床 LLM 多智能体系统。临床行动、证据与问责体现在**状态转移与交接**中。
- **AI 医院定义**：工作流级多智能体临床模拟或部署系统，具备明确角色、跨交接共享状态、基于 EHR 或指南的工具、安全门和可审计日志。其最低条件包括：跨角色与阶段组织行动、持久上下文、显式问责、审计就绪日志。
- **范围边界**：纳入多智能体模拟器和跨分诊、咨询、出院、床位管理、护理过渡、培训病房等阶段协调的临床系统；排除单智能体聊天机器人、无持久工作流状态的通用角色扮演、单轮 QA、缺乏安全规则/纵向记忆/交接结构的工具。
- **组织问题**：什么算 AI 医院？如何描述其设计选择？什么证据能支持更强自主性？

## 2. 方法论：核心思想与关键框架

- **总体思路**：以“工作流状态转移”为基本分析单元，而非孤立答案。每个角色更新病例状态、附加证据，并在显式控制策略下把病例交给下一步。
- **运行示例**：分诊 → 咨询 → 出院。每一步反复出现四个问题：
  - 谁拥有下一步行动？
  - 什么状态必须跨交接存活？
  - 什么证据支持该步骤？
  - 什么门控可以阻止或升级推进？
- **核心设计空间**：
  - **角色与交接**：患者面向角色、临床专业角色、规划与编排角色、评判/批评/记录角色。多智能体结构仅在跨护理阶段、专科或审批边界时更有价值，因为所有权变化且下一角色必须继承显式状态。
  - **记忆、证据与工具**：长期记忆与外部证据源、动态更新、工作记忆与交接恢复；证据访问工具、执行与验证工具、多模态与研究工具。工具不是可选准确率增强器，而是把证据和行动转化为可审计工作流对象的机制。
  - **推理、控制与升级**：直接/单路径推理、多路径推理、反馈来源、控制策略与门控。关键不是推理看起来多复杂，而是什么政策治理行动：何时继续、何时索取缺失证据、何时弃权、何时升级。
- **评估栈**：四层——安全、过程、结果、运营。同一运行应支持回放、审计和运营分析，而非只报告最终分数。
- **能力到工作流可观察桥**：更强校准影响高风险步骤的延迟或升级；更好检索影响记录链接证据；长上下文影响交接完整性与回放；工具可靠性影响受监管动作的可执行性与回滚；多模态接地影响图像/传感器证据是否留在决策链中。
- **IRL1–IRL6 分阶段自主协议**：
  - IRL1：静态或脚本沙盒，提交前人工审查。
  - IRL2：噪声、缺失信息或对抗模拟，人工审查加安全网关。
  - IRL3：真实数据影子回放，无实时影响，模型提议、人类决定。
  - IRL4：有限人机协同试点，有限步骤自动建议，高风险步骤强制批准。
  - IRL5：有限推广与端到端监控，自动默认加例外审查。
  - IRL6：多站点或多语言部署，监督自主加定期审计。
- **失败模式路线图**：纵向漂移、容量盲规划、未门控偏差与弱升级、不可追踪动作链、漂移/越狱/成本冲击。每类失败对应最小释放测试、最小日志包、阻断阶段和设计响应。
- **合成数据定位**：用于训练和压力测试，不作为部署证据。可扩展覆盖、反事实压力测试和工作流扰动，但可能扭曲患病率、协调模式和错误表面；更强自主声明仍需真实数据回放或前瞻性证据。

## 3. 实验设计、场景与基准

- **重要说明**：本文是**综述（Survey）**，不是提出新模型的实验论文。因此没有作者自行设计的数据集、训练实验或方法对比实验。
- **归纳的工作流设置与任务家族**：
  - **直接临床影响的工作流**：
    - 端到端临床工作流模拟与虚拟病房：最接近分诊、咨询、出院示例，强调阶段级可见性。
    - 咨询、多学科协调与复杂决策：处理专科约束、持续不确定性、隐藏分歧、过早收敛和不充分承诺。
    - 分诊、路由、护理过渡与出院沟通：输入噪声大、审批边界常见，质量由交接完整性和下游可用性决定。
  - **纵向、护理邻近与研究型工作流**：
    - 纵向患者交互与心理健康：强调持久状态、风险跟踪、校准升级。
    - 护理邻近临床数据工作流：EHR 分析、工具构建、知识策展、临床试验匹配，需增加溯源、验证或交接价值。
    - 科学发现与研究流程：实验规划、证据合成、工具介导的科学协作。
- **评估与基准讨论**：
  - 提到 OSCE 风格交互考试、虚拟 EHR 基准、更广泛医学任务套件、早期前瞻性研究等，作为部署证据包的不同部分。
  - 强调基准不等于部署准备：基准问系统能否在设定任务下表现，部署准备问在回放、升级和运营证据共同检查后自主声明是否仍合理。
- **对比方法**：没有实验性方法对比。论文对比的是设计选择、工具类别、记忆设计、推理与控制策略，以表格形式呈现适配场景、成本、日志义务和失败信号，例如 Table 6–9。

## 4. 资源与算力

- 论文中**未提及**任何 GPU 型号、数量、训练时长、算力预算或实验资源。
- 作为综述论文，作者未开展模型训练或大规模实验，因此没有算力消耗报告。
- 文中涉及的 token 成本、延迟、控制器负担等属于对多智能体工作流运营成本的定性讨论，未给出具体量化资源数据。

## 5. 实验数量与充分性

- **实验数量**：作者未执行传统实验，因此可视为 **0 组作者自建实验**。论文的主要“工作”是文献综述、分类框架构建、评估栈和 IRL 协议提出。
- **文献覆盖**：优先覆盖主要 NLP 与 ML 会议（ACL、NeurIPS、ICLR、ICML、AAAI）以及部分医学期刊和近期预印本（arXiv、medRxiv、bioRxiv）。
- **充分性评价**：
  - 作为框架性综述，覆盖面较广，并提供了多个操作性表格：Table 1 运行示例、Table 2 能力到工作流桥、Table 3 集成任务仪器化、Table 4 IRL 阶梯、Table 5 失败路线图、Table 6 单/多智能体清单、Table 7 记忆设计、Table 8 工具栈、Table 9 设计权衡。
  - 但**没有对提出的 IRL 框架、评估栈或失败模式进行实证验证**，也没有系统定量元分析。
  - 作者在“Limitations”中承认：受篇幅限制，只按角色、记忆、工具和控制总结，未提供每个方法的完整实现细节；覆盖渠道外的工作可能遗漏；分类和比较需随部署实践、法规和临床整合标准更新。
- **公平性**：
  - 由于没有方法对比实验，不涉及实验公平性比较。
  - 但文献选择可能受渠道偏好影响，偏向 NLP/ML 主会，可能遗漏医学信息学、临床实施科学等领域的相关工作。

## 6. 主要结论与发现

- AI 医院应被理解为**工作流级 LLM 多智能体临床系统**，而不是孤立问答代理。
- 主要设计问题是：谁拥有每一步；什么状态和证据在每次交接中存活；什么控制政策管理继续、弃权与升级。
- 评估应聚焦安全、过程、结果、运营四个层面的工作流可观察量；部署应通过显式仪器化、审计就绪日志和分阶段 IRL 门控推进。
- 最可复用的输出不是单纯系统分类法，而是面向**部分可观测下有状态、证据接地、工具介导的临床工作流**的报告与门控框架。
- 未来路线：
  - 近期进展依赖工作流感知记忆、容量耦合规划、校准升级政策、可审计溯源和部署手册，而非增加更多讨论轮次。
  - 需要共享报告协议，共同报告工作流可观察量、最小日志、升级覆盖、回放证据和运营成本。
  - 长期看，AI 医院可视为医学世界模型的工作流级近似，但前提是部署证据被当作分阶段协议，而非基准增益的副产品。

## 7. 优点

- **视角创新**：从“模型能力”转向“工作流状态转移与交接”，更贴近临床行动、证据和问责的真实表达方式。
- **框架系统**：统一组织角色与交接、记忆与证据、工具、推理/控制/升级，覆盖设计、评估、部署全链条。
- **可操作性较强**：四层评估栈、能力到工作流可观察桥、IRL1–IRL6 阶梯、任务级仪器化表和失败路线图，均可直接用于比较和治理讨论。
- **强调审计与安全**：把安全门、证据链、回放、升级日志、PHI 泄漏、回滚状态等作为释放信号，而非事后补充。
- **失败模式具体**：将失败定位为纵向漂移、容量盲规划、未门控偏差、不可追踪动作链、漂移/越狱/成本冲击，并给出最小测试和日志包。
- **伦理与局限意识**：明确讨论合成数据不能替代部署证据、IRL 阈值需按任务风险和站点政策校准，以及公平性和治理问题。

## 8. 不足与局限

- **综述性质限制**：没有作者自建实验
