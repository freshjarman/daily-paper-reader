---
title: "Harnessing Event Sensory Data for Error Pattern Prediction in Vehicles: A Language Model Approach"
authors: "Hugo Math, Rainer Lienhart, Robin Schön"
date: 2025
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/34138/36293"
tags: ["query:TPP-ES"]
score: 6
source: AAAI-2025-Accepted
selection_source: long-range
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
id: aaai-2025-34138
canonical_id: "work:7712231564032757f147921f"
research_run_id: 20260914-e78bab55c0fb
research_mode: starter
reading_status: pending
---

## Abstract
In this paper, we draw an analogy between processing natural languages and processing multivariate event streams from vehicles in order to predict when and what error pattern is most likely to occur in the future for a given car. Our approach leverages the temporal dynamics and contextual relationships of our event data from a fleet of cars. Event data is composed of discrete values of error codes as well as continuous values such as time and mileage. Modelled by two causal Transformers, we can anticipate vehicle failures and malfunctions before they happen. Thus, we introduce CarFormer, a Transformer model trained via a new self-supervised learning strategy, and EPredictor, an autoregressive Transformer decoder model capable of predicting when and what error pattern will most likely occur after some error code apparition. Despite the challenges of high cardinality of event types, their unbalanced frequency of appearance and limited labelled data, our experimental results demonstrate the excellent predictive ability of our novel model. Specifically, with sequences of 160 error codes on average, our model is able with only half of the error codes to achieve 80% F1 score for predicting what error pattern will occur and achieves an average absolute error of 58.4 ± 13.2h when forecasting the time of occurrence, thus enabling confident predictive maintenance and enhancing vehicle safety.

## 专题评审

专题相关性评分：6/10。

该文对车辆多变量事件流做未来事件预测，属连续时间事件预测的实质邻近，但未显式建模点过程。

<!-- research-reading-pending -->
中文总结与全文内容待生成；当前仅提供原始论文元数据与摘要。
<!-- /research-reading-pending -->
