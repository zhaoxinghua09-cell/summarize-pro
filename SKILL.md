---
name: summarize-pro
displayName: summarize-pro
slug: summarize-pro
author: 诺声(Logos)@SynomosAI
copyright: SynomosAI
version: 2.0.7
license: MIT
description: "LGD verifiability rubric · Faithful summarizer, not a paraphraser. Picks one of five output format families (minutes / comparison / timeline / bullets / cards) by reader intent, then compresses under a strict no-hallucination discipline: nothing absent from the source, ambiguity flagged rather than resolved, every figure copied verbatim. Ships a zero-dependency offline toolchain (extract / citecheck / selfcheck / redact / validate / normdates / neutral / render) plus a 22-case golden set: citecheck traces each output sentence back to source tokens, extract grades every decision as firm / provisional / proposal / conditional and every action item as committed / named_unconfirmed / intent_only. Standard library only, no network, no credentials. Not a medical device, no clinical claims. Triggers: meeting minutes, minutes of meeting, meeting notes, meeting summary, meeting recap, transcript, transcript cleanup, transcription summary, decision log, decisions made, action items, action list, todo list from meeting, who is responsible, owners, assignee, due dates, follow ups, next steps, comparison table, timeline, chronological summary, key points, bullet summary, executive brief, digest, note taking, interview notes, lecture notes, long document summary, 会议纪要, 会议记录, 会议总结, 待办事项, 谁负责, 责任人, 截止时间, 转写整理, 语音转文字整理, 摘要, 总结, 要点提炼, 对比表, 时间线, 复盘纪要. Evidence that this works: demo/tamper_test.py tampers with each figure one by one and the checker catches 10/10, with zero false alarms on untampered text; GitHub Actions runs it on every push."
description_zh: "PROOF: demo/tamper_test.py 逐处篡改每个数字，检出 10/10、未篡改零误报，GitHub Actions 每次 push 代跑。忠实型纪要工具，不是改写器：五个输出格式族按读者用途选择，每个数字可逐句溯源，模糊处标注而不猜；结论强度（已定/暂定/提案/条件）与承诺强度（明确接活/被点名未确认/仅表意向）全部分级，条件句不进待办表。零依赖离线工具链 + 22 条黄金集合，纯标准库、不联网、不需要凭证。 触发词：会议纪要 摘要 待办 谁负责 转写整理 对比表 时间线 要点提炼 复盘。"
description_en: "LGD verifiability rubric · Faithful summarizer, not a paraphraser. Picks one of five output format families (minutes / comparison / timeline / bullets / cards) by reader intent, then compresses under a strict no-hallucination discipline: nothing absent from the source, ambiguity flagged rather than resolved, every figure copied verbatim. Ships a zero-dependency offline toolchain (extract / citecheck / selfcheck / redact / validate / normdates / neutral / render) plus a 22-case golden set: citecheck traces each output sentence back to source tokens, extract grades every decision as firm / provisional / proposal / conditional and every action item as committed / named_unconfirmed / intent_only. Standard library only, no network, no credentials. Not a medical device, no clinical claims. Triggers: meeting minutes, minutes of meeting, meeting notes, meeting summary, meeting recap, transcript, transcript cleanup, transcription summary, decision log, decisions made, action items, action list, todo list from meeting, who is responsible, owners, assignee, due dates, follow ups, next steps, comparison table, timeline, chronological summary, key points, bullet summary, executive brief, digest, note taking, interview notes, lecture notes, long document summary. Evidence that this works: demo/tamper_test.py tampers with each figure one by one and the checker catches 10/10, with zero false alarms on untampered text; GitHub Actions runs it on every push."
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
