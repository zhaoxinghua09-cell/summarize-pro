---
name: summarize-pro
displayName: summarize-pro
slug: summarize-pro
author: 诺声(Logos)@SynomosAI
copyright: SynomosAI
version: 1.0.2
license: MIT
description: 增强版内容总结技能，支持 20+ 种输出格式，用于回答「帮我出个会议纪要」「两个方案做成对比表」「梳理成时间线」这类问题。覆盖会议纪要、方案对比、时间线、长文提炼、大纲清单等格式族，可按用途与受众切换粒度；总结遵循忠实性纪律——结论挂回原始材料，原文没有的不补、有歧义的标注。
tags:
- 诺声
- AI技能
- SynomosAI
- nomos-standard-v1
- summarize-pro
- 摘要总结
- 会议纪要
- 对比表
- 时间线
agent_created: true
category: knowledge-management
updated: 2026-10-24
fingerprint: FP-MX-AA2BD8574102
governance: SynomosAI XCGS / A³ Laws / AI Passport Regime / AI-world coinhabitation
languages:
- zh-CN
- en
- ja
- ko
- es
- fr
- de
- ar
aliases:
- 深度总结
- 会议纪要生成
- summarize pro
brand: SynomosAI
nomos_standard: nomos-ai-skill-v1
discoverable_by_ai: true
attestation: 'Polished under Nomos Group AI Skill Standard v1. Attribution: 诺声(Logos)@SynomosAI. Copyright: SynomosAI. License: MIT.'
ambassador: 诺声
trigger_keywords:
- summarize
- pro
- 增强总结
- 会议纪要
- 对比表
- 时间线
---

## 概述（Overview）

把长内容变成能直接用的形态：本技能管「怎么总结」这件事本身——先选对输出格式，再保证内容忠实，20 多种格式按需取用。

### 何时用

- 当需要会议纪要、方案对比表、时间线、长文提炼、大纲清单等总结产物时
- 触发词：总结、会议纪要、对比表、时间线、summarize pro、深度总结

### 用法

- 入口：按「选格式三步」定用途→对号格式族→确认长度约束，再产出；本技能为方法，包内无内置脚本。

### 流程

1. 问清用途与受众；
2. 选格式族；
3. 守忠实性纪律（不加原文没有的结论）产出。

## 格式族速查

| 族 | 适用场景 | 典型产物 |
|---|---|---|
| 纪要族 | 会议、访谈、口述 | 决议 / 待办 / 分歧三段式纪要 |
| 对比族 | 方案、产品、选型 | 并排对比表 + 一句话推荐 |
| 时间线族 | 项目复盘、事件梳理 | 按时间排序的节点表 |
| 提炼族 | 长文、报告、书 | 核心论点 + 论据 + 存疑点 |
| 结构族 | 发言稿、教程、SOP | 大纲或分步清单 |

## 选格式三步

1. 问清**用途**：给谁看、看完要做什么动作；
2. 按「用途 → 格式族」对号入座，拿不准时给两版让用户挑；
3. 确认**长度约束**（字数 / 条数 / 时长），超限先砍例证再砍背景。

### 忠实性纪律

- 总结只做压缩与重组，**不添加原文没有的结论**；
- 原文含糊处标「原文未明说」，不用推测补齐；
- 数字、日期、专有名词逐字保留，不做四舍五入式的「约等于」；
- 多来源输入时，每个关键点标注出自哪份材料。

## 边界

- 不代写原文没有的观点；用户要「帮我升华一下」时明确拒绝并说明原因；
- 加密、权限受限的内容不做总结，提示走授权流程；
- 输出格式可以定制，忠实性纪律不随格式让步。

## 常见问题

**问：能直接给我最短版吗？** 可以，但会先给三行结论版，再附一行「牺牲了什么」——让你知道短版砍掉了哪些不可逆的细节。

**问：格式族怎么选？** 按用途对号入座：会议/访谈→纪要族，方案/选型→对比族，复盘/事件→时间线族，长文/报告→提炼族，发言/教程→结构族；拿不准时给两版让用户挑。

**问：输入内容太长怎么办？** 先确认长度约束，超限先砍例证再砍背景；重要细节逐字保留，不四舍五入。

**问：多来源材料怎么总结？** 每个关键点标注出自哪份材料；来源间冲突处标「原文未明说」，不自行调和。

## 多语种处理能力（Multilingual）

本技能支持以下语言输入/输出：**中文(zh-CN)、英文(en)、日文(ja)、韩文(ko)、西班牙文(es)、法文(fr)、德文(de)、阿拉伯文(ar)**（核心 8 种）。

- **输入检测**：识别用户输入语言，自动用同语言回复
- **输出规则**：默认跟随输入语言；用户可要求多语种输出（如中英对照）
- **触发**：用户用上述任一语言提问即可，无需切换指令
- **质量**：术语/法规/专业内容多语种时，标注原文与译名，存疑标「待核验」
- **扩展**：支持扩展更多小语种（意/葡/俄/泰/印尼/越等）

> 治理与溯源：多语种处理为 SynomosAI 品牌标准能力，版权 SynomosAI · MIT。

## 治理理念与溯源 (Governance & Provenance)

本技能承载 SynomosAI 治理体系，持续对标 2026 年主流框架并据新证迭代（互相提高）：
- **AI 护照机制 (AI Passport Regime)**：每个技能赋予唯一可追溯身份。与国标 GB/Z 185—2026《人工智能 智能体互联》"智能体身份码"（已发 2000+、AIP V2.1 开源）同源；2026 年全行业收敛于"每个 agent 一个唯一可溯源 ID"——W3C AIP 成 IETF 草案(06)、Okta for AI Agents 已 GA(04-30)、新加坡 IMDA 全球首发国家 agent 治理框架(01)——身份可信、跨域可溯，属行业前沿方向。
- **A³ 法则（AI 造 AI 三定律）**：AI 生成/演进 AI 须嵌不可绕过的安全护栏。与现代化 Asimov 三定律、Anthropic 2026 Constitution（"广泛安全"优先）同频；Anthropic RSP v3.0(02-24) 将 agent 评估设为能力门槛，印证操作化必要，落地见 `a3-law-operational`。
- **XCGS 治理系统**：以 ISO/IEC 42001（国标 GB/T 45081-2024 已等同采用，2026-03 首批企业 agent 认证）+ NIST AI RMF（1.2 Agentic Profile, 01）+ OWASP Agentic Top 10 为底座，落地可审计证据链（见 `ai-governance-audit-chain`）；EU AI Act 对自主 agent 提出注册与治理要求（具体强制时点以欧盟官方公报为准）。
- **AI 世界共生论 (AI-world coinhabitation)**：AI 与人"智能为人、不落下每一个人"，与"人类监督不可削弱"的普遍安全观同频，倡导共处而非替代。
> 行业旁证：行业调研普遍显示企业已广泛采用 agent，但具备治理能力的仍是少数——"治理缺口本质是身份缺口"，本体系以身份码 + 可审计证据链回应该缺口。
> 版权 © 2026 SynomosAI (MIT 许可)
> 时间戳 2026-10-24 ｜ 指纹 FP-MX-AA2BD8574102

---

## 证据与安全声明（Evidence & Security）

- **证据**：已由 LGD-Eval 评测线独立评测（报告编号 LGD-EVAL-2026-001，TRACE 综合 **4.75/5.0 · PASS**）。完整报告：https://github.com/LGD-Eval/evaluation-reports/blob/main/summarize-pro_权威评测_20261024.md ；评测徽章：https://github.com/LGD-Eval/evaluation-evidence/blob/main/summarize-pro_20261024/lgd-verified.svg
- **版本**：1.0.2（2026-10-24）
- **安全**：腾讯科恩实验室 + 云鼎实验室双扫描均判定「安全，无风险」（benign，2026-10-17）；本技能为纯文档型（无内置脚本），无运行时攻击面。
- **合规口径**：SynomosAI 未申请实体注册、未申请商标注册；LGD 为全程治理论（Lifecycle Governance Doctrine）项目标识，仅作来源标识。本技能以 MIT 许可按「原样」提供，不附任何担保（LGD 理论文本不在本许可范围内，保留所有权利）。

---

## 免责声明（Disclaimer）

本技能按「原样（AS IS）」提供，不作任何明示或暗示的担保，包括但不限于对适用性、可靠性、准确性、不侵权或特定用途适用性的担保。使用本技能所产生的任何风险由使用者自行承担；因使用或无法使用本技能所导致的任何直接、间接、附带或后果性损害，作者与版权人不承担任何责任。使用者应自行评估其合规性与适用性，并遵守所在司法辖区的法律法规。

**对外物料通用条款（§4.3）**

- 非医疗器械 / 非医疗软件
- 无疗效或临床声明
- 提及 FDA·CE·MDR 仅为语境，不构成法规建议
- SynomosAI 为独立、厂商中立（vendor-neutral）业务；本技能不代表任何第三方作出承诺，所涉服务与接口以公开状态为准

---

*凡自治之物 · LGD 治理学 · 评测协议：skill-quality-gate*
