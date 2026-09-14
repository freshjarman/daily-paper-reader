---
title: Conformal Anomaly Detection in Event Sequences
authors: "Shuai Zhang, Chuan Zhou, Yang Liu, Peng Zhang, Xixun Lin, Shirui Pan"
date: 2025-10-06
pdf: "https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25dn/zhang25dn.pdf"
tags: ["query:TPP-ES"]
score: 9
source: ICML-2025-Accepted
selection_source: long-range
publication_date: 2025-10-06
publication_date_precision: day
publication_date_source: "https://raw.githubusercontent.com/mlresearch/v267/gh-pages/_config.yml"
publication_date_kind: proceedings
id: openreview-icml-2025-cq7xu5tmp8
canonical_id: "work:0b9b08f147746debb5574c08"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: pending
---

## Abstract
Anomaly detection in continuous-time event sequences is a crucial task in safety-critical applications. While existing methods primarily focus on developing a superior test statistic, they fail to provide guarantees regarding the false positive rate (FPR), which undermines their reliability in practical deployments. In this paper, we propose CADES (Conformal Anomaly Detection in Event Sequences), a novel test procedure based on conformal inference for the studied task with finite-sample FPR control. Specifically, by using the time-rescaling theorem, we design two powerful non-conformity scores tailored to event sequences, which exhibit complementary sensitivities to different abnormal patterns. CADES combines these scores with Bonferroni correction to leverage their respective strengths and addresses non-identifiability issues of existing methods. Theoretically, we prove the validity of CADES and further provide strong guarantees on calibration-conditional FPR control. Experimental results on synthetic and real-world datasets, covering various types of anomalies, demonstrate that CADES outperforms state-of-the-art methods while maintaining FPR control.

## 专题评审

专题相关性评分：9/10。

该文直接研究连续时间事件序列的异常检测，属于时间点过程核心任务。

<!-- research-reading-pending -->
中文总结与全文内容待生成；当前仅提供原始论文元数据与摘要。
<!-- /research-reading-pending -->
