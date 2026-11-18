---
name: summarize-pro
displayName: summarize-pro
slug: summarize-pro
author: 诺声(Logos)@SynomosAI
copyright: SynomosAI
version: 2.0.7
license: MIT
description: "Use this skill when the user asks for meeting minutes, decisions, action items, or pastes a transcript. 会议纪要/待办/谁负责/转写整理. A faithful summarizer that picks one of five output format families (minutes / comparison / timeline / bullets / cards) by reader intent, then compresses under a strict no-hallucination discipline: nothing absent from the source, ambiguity flagged rather than resolved, every figure copied verbatim. Ships a zero-dependency, offline toolchain (extract / citecheck / selfcheck / redact / validate / normdates / neutral / render) plus an 22-case golden set, turning 'we do not fabricate' from a claim into a runnable assertion: citecheck traces each output sentence back to source tokens and lists anything untraceable, selfcheck asserts format-family completeness including mandatory strength labels, extract builds the skeleton and additionally grades decisions and commitments - every conclusion is labelled firm / provisional / proposal / conditional and every action item is labelled committed / named_unconfirmed / intent_only, so 'what was actually decided' and 'who actually took it' become checkable instead of assumed. Conditional clauses are kept out of the action table and markdown headings out of the sentence stream. Standard library only, no network, no replacement for human judgement. Also ships **deterministic rendering** (receipt / personal / executive / bundle views, top-3 per section), **relative-date anchoring** that appends an ISO date without rewriting the source sentence, and a **neutral-language check** for personnel / medical / legal / incident scenes. Fidelity is checkable: citecheck traces numbers to source, and the golden set re-runs with an exit code. Triggers: summarize, summary, meeting minutes, minutes of meeting, decision log, action items, comparison table, timeline, key points, digest. Use when turning a transcript, meeting recording, interview or long document into minutes, a comparison table, a timeline or a brief."
description_zh: "总结 / 摘要 / 会议纪要 / 对比表 / 时间线 —— 增强版内容总结技能，按读者用途从 5 大输出格式族（纪要/对比/时间线/要点/卡片）中选格式，配合忠实性纪律；v2.0.7 附零依赖本地工具链（事实线索抽取 / 骨架生成 / 逐句溯源校验 / 22 条黄金集），并新增「结论强度 + 承诺强度」分级：每条结论标注 已定/暂定/提案/条件，每条待办标注 明确接活/被点名未确认/仅表意向，让「到底定了什么」「谁真的接了」从猜测变成可核对；条件句不再混入待办表，标题行不再当作句子。用于回答「帮我出个会议纪要」「这次到底定了啥」「谁负责」这类问题；v2.0.7 增确定性渲染四视图（receipt/personal/executive/bundle，每区只显示前 3 条）、相对日期锚点（原文一字不改，只追加 ISO 括注）、敏感场景中性措辞检测 Also ships deterministic rendering (receipt / personal / executive / bundle views, top-3 per section), relative-date anchoring that appends an ISO date without rewriting the source sentence, and a neutral-language check for personnel / medical / legal / incident scenes."
description_en: "A faithful summarizer that picks one of five output format families (minutes / comparison / timeline / bullets / cards) by reader intent, then compresses under a strict no-hallucination discipline: nothing absent from the source, ambiguity flagged rather than resolved, every figure copied verbatim. Ships a zero-dependency, offline toolchain (extract / citecheck / selfcheck / redact / validate / normdates / neutral / render) plus an 22-case golden set, turning 'we do not fabricate' from a claim into a runnable assertion: citecheck traces each output sentence back to source tokens and lists anything untraceable, selfcheck asserts format-family completeness including mandatory strength labels, extract builds the skeleton and additionally grades decisions and commitments - every conclusion is labelled firm / provisional / proposal / conditional and every action item is labelled committed / named_unconfirmed / intent_only, so 'what was actually decided' and 'who actually took it' become checkable instead of assumed. Conditional clauses are kept out of the action table and markdown headings out of the sentence stream. Standard library only, no network, no replacement for human judgement. Triggers: summarize, summary, meeting minutes, minutes of meeting, decision log, action items, comparison table, timeline, key points, digest. Also ships deterministic rendering (receipt / personal / executive / bundle views, top-3 per section), relative-date anchoring that appends an ISO date without rewriting the source sentence, and a neutral-language check for personnel / medical / legal / incident scenes."
tags:
- 总结
- 摘要
- 会议纪要
- 知识管理
- summarize-pro
agent_created: true
category: knowledge-management
updated: 2026-11-18
fingerprint: FP-MX-AA2BD8574102
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
discoverable_by_ai: true
ambassador: 诺声
trigger_keywords:
- summarize
- pro
- 增强总结
- 总结
- 摘要
- 会议纪要
- 对比表
- 时间线
- 要点提炼
- 笔记整理
- 结构化总结
- 内容压缩
display_name: 会议纪要专家
display_name_en: summarize-pro

---

# summarize-pro · 精简版（v2.1.0-slim）

原 406 行正文 → 本页 62 行；7 份 references → 1 份 `references/details.md`。
依据 SkillsBench（arXiv 2602.12670）：聚焦型（2–3 模块）优于全面型文档。

## 1 用法：只决定一件事——选格式族

读者要**执行**→`minutes`；要**比对**→`comparison`；要**追溯**→`timeline`；要**速览**→`bullets`；要**分发**→`cards`。
路由优先级：显式格式名 > 读者用途 > 默认 `minutes`。中文说"纪要/待办/谁负责"一律走 `minutes`。

```bash
python scripts/summarize_pro.py extract --file 转写.txt --format minutes --out ./out --json
python scripts/summarize_pro.py citecheck --file ./out/转写.minutes.md --source 转写.txt --json
python scripts/summarize_pro.py selfcheck --file ./out/转写.minutes.md --format minutes --json
python scripts/summarize_pro.py normdates --file 转写.txt --asof 2026-11-18
python scripts/summarize_pro.py redact --file 转写.txt --out ./out/safe.txt
python scripts/summarize_pro.py render --file ./out/转写.facts.json --view executive
```

## 2 纪律：不可妥协（逐条满足，缺一即返工）

- **MUST** 每个数字、日期、人名逐字来自原文；改格式不改字面。
- **MUST** 相对日期只追加 ISO 括注，不重写原句（`下周三` → `下周三（2026-11-25）`）。
- **MUST** 每条结论标强度：`firm` / `provisional` / `proposal` / `conditional`。
- **MUST** 每条待办标承诺：`committed` / `named_unconfirmed` / `intent_only`。
- **MUST** 输出前跑 `selfcheck`；不通过不许交付。
- **MUST** 敏感场景（人事/医疗/法律/事故）用中性措辞，先跑 `neutral`。
- **NEVER** 补全原文未提的责任人或期限；缺失写「原文未提及」。
- **NEVER** 把条件句（"如果…就…"）列进待办表。
- **NEVER** 把 Markdown 标题行当作句子或待办。
- **NEVER** 给法律意见、医疗诊断或代替决策。

示例（输入残句 → 输出条目，数字与归属一字不改）：

```text
原文：会议决议：暂不投产，等 12月3日 复评后再定。由周敏出初稿。
输出：- [firm] 暂不投产，等 12月3日（2026-12-03）复评后再定。
      | 出初稿 | 周敏 | 原文未提及 |
```

## 3 边界与降级

- 原文 <80 字：只出要点，标「样本不足，不建议据此决策」。
- 转写有折行（说话人与内容分两行）：先 `adapt`，否则待办判不出来。
- 全文规范（体裁骨架、四视图渲染、5 平台适配器、FAQ、边界详解）见 `references/details.md`。
- 同系列：`lgd-skill-review`（评审）→ `debug-pro`（排障）→ `wechat-viral-topic`（选题）。

```bash
python scripts/summarize_pro.py adapt --file 腾讯会议转写.txt --out ./out/fixed.txt
python tests/run_golden.py            # 22 条黄金集，退出码即结论
```

许可 MIT ｜ 作者 诺声(Logos)@SynomosAI ｜ 零依赖·零联网·零凭据

## Hand-off

- 需要定位故障根因 → `debug-pro`
- 需要选题或标题体检 → `wechat-viral-topic`
- 需要对外证明本包质量 → `lgd-skill-review`（六维评审，`--focus` 附加聚焦度报告）
