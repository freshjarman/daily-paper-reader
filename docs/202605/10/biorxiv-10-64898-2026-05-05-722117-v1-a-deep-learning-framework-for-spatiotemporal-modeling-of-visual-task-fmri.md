---
title: A Deep Learning Framework for Spatiotemporal Modeling of Visual Task fMRI
title_zh: 一种用于视觉任务fMRI时空建模的深度学习框架
authors: "Li, M., Chen, Y., Ning, C., Dang, X., Wu, D."
date: 2026-05-09
pdf: "https://www.biorxiv.org/content/10.64898/2026.05.05.722117v1.full.pdf"
tags: ["query:tpp-es"]
score: 6.5
evidence: 神经转移函数的时空建模
tldr: 传统fMRI分析侧重局部激活而忽视了脑区间的动态协调。本研究提出STREAM深度学习框架，通过学习任务态fMRI的神经转换函数来刻画有效连接和全脑信息流。基于1074名受试者的视觉处理数据，该模型不仅能重建激活图，还揭示了默认模式网络作为高层调节枢纽的主动作用，以及类别特异性通信源于信号模式的动态重构，为理解大脑灵活的功能架构提供了新范式。
source: biorxiv
selection_source: fresh_fetch
motivation: 传统fMRI分析难以揭示驱动局部激活的底层信息流和脑区间动态协调机制。
method: 提出名为STREAM的深度学习框架，通过学习神经转换函数来建模任务态fMRI中的有效连接。
result: 发现传统激活区主要受输入信号驱动，而默认模式网络作为具有广泛输出影响的调节枢纽，且类别特异性通信依赖于信号模式的动态重构。
conclusion: 该研究建立了一种揭示任务态fMRI定向信号机制的新计算范式，阐明了大脑如何为复杂认知灵活重构功能架构。
---

## 摘要
刻画认知任务期间分布式脑区的动态协调仍然具有挑战性，因为传统的fMRI分析侧重于局部激活，而未能揭示驱动这些激活的潜在信息流。在此，我们提出了STREAM（用于有效连接分析的时空表示模型），这是一个深度学习框架，通过学习任务态fMRI中的神经转换函数来刻画有效连接和全脑信息流。应用于1074名参与者的视觉类别处理，STREAM在准确重建激活图的同时，进一步揭示了传统的激活区域主要由输入信号驱动。此外，默认模式网络作为一个具有广泛传出影响的高级调节枢纽，挑战了其被动特征的传统观点。此外，类别特异性通信源于关键枢纽之间信号模式的动态重构，而非静态路径。这些发现建立了一种新的计算范式，揭示了驱动任务态fMRI局部动力学的定向信号机制，展示了大脑如何灵活地重构功能架构以实现复杂的认知。

## Abstract
Characterizing the dynamic coordination of distributed brain regions during cognitive tasks remains challenging, as traditional fMRI analysis focuses on localized activations without revealing the underlying information flow that drives them. Here, we propose STREAM (Spatiotemporal Representation for Effective connectivity Analysis Model), a deep-learning framework that learns neural transition functions in task-fMRI to characterize effective connectivity and whole-brain information flow. Applied to visual category processing in 1074 participants, STREAM accurately reconstructs activation maps while further revealing that traditional activation regions are primarily driven by incoming signals. Moreover, the Default Mode Network acts as a high-level regulatory hub with extensive outgoing influence, challenging its passive characterization. Additionally, category-specific communication emerges from dynamic reconfiguration of signaling patterns among key hubs rather than static pathways. These findings establish a novel computational paradigm that uncovers directional signaling mechanisms driving local dynamics in task-fMRI, revealing how the brain flexibly reconfigures functional architecture for complex cognition.