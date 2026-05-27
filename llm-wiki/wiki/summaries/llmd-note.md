# llm-d KV 缓存感知路由深度笔记

## Source

- Raw note: `raw/notes/llmd_note.md`
- Metadata: not available in note

## Compiled Summary

本文围绕 llm-d 项目的 KV 缓存感知路由展开，介绍了其设计原理、实现细节与实测效果。

## Evidence Notes

- llm-d 是一款面向容器编排生态的开源大语言模型推理框架，由 IBM、Google、Red Hat 及社区共同维护。
- 在分布式大语言模型推理场景中，即使底层模型服务器启用了前缀缓存，流量网关对 GPU 内存中的 KV 缓存状态仍然一无所知。这导致以下问题：
- 轮询或粘性会话策略无法根据实际缓存分布做智能调度；
- 高并发或共享上下文场景下出现大量重复前缀计算；
- GPU 内存与计算资源被冗余占用，延迟和成本双双上升。
- 本文要解决的问题是：如何在 Kubernetes 原生架构中构建一个全局、近实时的 KV 缓存状态感知与请求路由系统，使得新到达的提示词能够被导向缓存内容最充分的 pod，从而最大化前缀复用、降低首词元延迟并提升整体吞吐。
- ### 系统架构概览
llm-d 的 KV 缓存感知路由建立在三个云原生组件之上。
- 第一，**网关 API 推理扩展**：扩展标准 Kubernetes Gateway API，使其支持面向大语言模型推理的专用路由语义。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md)
- Entities: None identified
