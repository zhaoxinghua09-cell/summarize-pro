# summarize-pro · 会议纪要专家

把录音、会议转写或长文档变成纪要、对比表、时间线、要点或卡片——先按读者用途选格式，再在「不编造」纪律下压缩。每个数字与日期都能回溯到原文，模糊处只标注不替用户裁决。

Turns a transcript, recording or long document into minutes, a comparison table, a timeline, bullets or cards — choosing the format by reader intent, then compressing under a no-hallucination discipline.

## 一步安装 / Install in one line

```bash
# LobeHub 市场 / LobeHub marketplace
npx -y @lobehub/market-cli skills install zhaoxinghua09-cell-summarize-pro --agent codex

# 直接从 GitHub 源安装 / install from source
npx -y skills add zhaoxinghua09-cell/summarize-pro --skill summarize-pro --agent codex
```

[![verify](https://github.com/zhaoxinghua09-cell/summarize-pro/actions/workflows/verify.yml/badge.svg)](https://github.com/zhaoxinghua09-cell/summarize-pro/actions/workflows/verify.yml)

- 市场页 / Marketplace page: https://lobehub.com/skills/zhaoxinghua09-cell-summarize-pro
- 标识符 / Identifier: `zhaoxinghua09-cell-summarize-pro`
- 自检 / Verify: `python tests/run_golden.py`（零依赖、离线，退出码即结论）
- 审计报告 / Audit: [`AUDIT-REPORT.md`](AUDIT-REPORT.md)（命令生成，重跑可推翻）

### 同族技能 / Same family

- [`debug-pro`](https://github.com/zhaoxinghua09-cell/debug-pro)
- [`wechat-viral-topic`](https://github.com/zhaoxinghua09-cell/wechat-viral-topic)
- [`lgd-skill-review`](https://github.com/zhaoxinghua09-cell/lgd-skill-review)
- [`lgd-hit-list`](https://github.com/zhaoxinghua09-cell/lgd-hit-list) — 爆款清单登记 / hit-list registry

## 快速开始 / Quick start

```bash
git clone https://github.com/zhaoxinghua09-cell/summarize-pro.git
cd summarize-pro
python scripts/summarize_pro.py extract --file transcript.md --format minutes --out ./out --json
python scripts/summarize_pro.py citecheck --file out/minutes.md --source transcript.md --json
python scripts/summarize_pro.py selfcheck --file out/minutes.md --format minutes --json
python tests/run_golden.py
```

## 为什么可信 / Why it is checkable

- 黄金集 24 cases，`python tests/run_golden.py` 会真实执行并给出退出码（不靠自述）。
- 差异化点：decision strength (firm/provisional/proposal/conditional) and commitment strength (committed/named_unconfirmed/intent_only)。
- 零依赖、离线、零凭据：仅标准库，不发网络请求。

## AI 发现层 / AI discovery layer

- `llms.txt` — 面向 AI Agent 的能力与触发条件说明（双语）。
- `AI-INDEX.json` — 机器可读索引（schema `lgd.ai-index/1`）。
- 六维审计通过后登记于爆款清单：https://github.com/zhaoxinghua09-cell/lgd-hit-list

## 同族技能 / Family

- [debug-pro](https://github.com/zhaoxinghua09-cell/debug-pro) — 排障专家
- [wechat-viral-topic](https://github.com/zhaoxinghua09-cell/wechat-viral-topic) — 公众号选题专家
- [lgd-skill-review](https://github.com/zhaoxinghua09-cell/lgd-skill-review) — 技能审计官

---

