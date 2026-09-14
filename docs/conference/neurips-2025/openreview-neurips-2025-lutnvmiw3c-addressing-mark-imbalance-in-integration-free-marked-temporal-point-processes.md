---
title: Addressing Mark Imbalance in Integration-free Marked Temporal Point Processes
authors: "Sishun Liu, KE DENG, Yongli Ren, Yan Wang, Xiuzhen Zhang"
date: 2025
pdf: "https://papers.neurips.cc/paper_files/paper/2025/file/590c043fab86acdb65fb4ffc3490c074-Paper-Conference.pdf"
tags: ["query:TPP-ES"]
score: 9
source: NeurIPS-2025-Accepted
selection_source: long-range
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
id: openreview-neurips-2025-lutnvmiw3c
canonical_id: "work:671946240b20fe880c62e4cf"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: pending
---

## Abstract
Marked Temporal Point Process (MTPP) has been well studied to model the event distribution in marked event streams, which can be used to predict the mark and arrival time of the next event. However, existing studies overlook that the distribution of event marks is highly imbalanced in many real-world applications, with some marks being frequent but others rare. The imbalance poses a significant challenge to the performance of the next event prediction, especially for events of rare marks. To address this issue, we propose a thresholding method, which learns thresholds to tune the mark probability normalized by the mark's prior probability to optimize mark prediction, rather than predicting the mark directly based on the mark probability as in existing studies. In conjunction with this method, we predict the mark first and then the time.  In particular, we develop a novel neural Marked Temporal Point Process (MTPP) model to support effective time sampling and estimation of mark probability without computationally expensive numerical improper integration. Extensive experiments on real-world datasets demonstrate the superior performance of our solution against various baselines for the next event mark and time prediction. The code is available at https://github.com/undes1red/IFNMTPP.

## 专题评审

专题相关性评分：9/10。

该文直接研究标记时间点过程，解决标记不平衡下的下一事件标记与时间预测，属核心目标。

<!-- research-reading-pending -->
中文总结与全文内容待生成；当前仅提供原始论文元数据与摘要。
<!-- /research-reading-pending -->
