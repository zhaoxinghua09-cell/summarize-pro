#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""打假自测：对一份人工写对的纪要逐处篡改，验证「溯源核对」能不能抓住每一处。

用法（在技能包根目录）：
    python demo/tamper_test.py

它给出可复核的三组数字：
  1. 基线：未经篡改的纪要 → 必须 PASS
  2. 篡改：逐处改动一个数字/日期 → 每一处都必须被检出（召回率）
  3. 对照：把一处改成原文里确实存在的另一个事实 → 必须仍 PASS（不误报）

退出码 0 = 三组都成立；非 0 = 有漏检或误报，说明忠实性证明在该样本上不成立。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import summarize_pro as sp  # noqa: E402

SRC = os.path.join(HERE, "sample_transcript.md")
EXPECTED = os.path.join(HERE, "expected_minutes.md")
MAX_CASES = 10

NUM = re.compile(r"\d+(?:\.\d+)?%?|1[01] 月 \d{1,2} 日|\d{1,2} 月 \d{1,2} (?:日|号)")


def perturb(token):
    """把 token 变成原文里不存在的相似值。"""
    m = re.match(r"^(\d+)(\.\d+)?(%)?$", token)
    if m:
        n = int(m.group(1))
        return "%d%s%s" % (n + 7 if n < 7 else n - 3, m.group(2) or "", m.group(3) or "")
    m = re.match(r"^(\d{1,2}) 月 (\d{1,2}) (日|号)$", token)
    if m:
        return "%s 月 %d %s" % (m.group(1), int(m.group(2)) + 3, m.group(3))
    return token + "9"


def check(text, src_text):
    return sp.citecheck(text, src_text)


def main():
    src = open(SRC, encoding="utf-8").read()
    exp = open(EXPECTED, encoding="utf-8").read()

    # 1) 基线
    base = check(exp, src)
    print("[1] 基线（未篡改）：%s  核对 %d 个 token，不可溯源 %d 个"
          % (base["verdict"], base["checked"], len(base["missing"])))
    if base["verdict"] != "PASS":
        print("    基线就不通过，后面无从谈起。")
        sys.exit(1)

    # 2) 逐处篡改
    candidates = [t for t in NUM.findall(exp) if t in src]
    pairs = []
    for tok in candidates:
        bad = perturb(tok)
        if bad != tok and bad not in src and exp.count(tok) >= 1:
            pairs.append((tok, bad))
        if len(pairs) >= MAX_CASES:
            break
    cases = pairs
    caught, missed = 0, []
    print("\n[2] 逐处篡改（每处改一个事实，必须被检出）")
    for i, (tok, bad) in enumerate(cases, 1):
        tampered = exp.replace(tok, bad, 1)
        r = check(tampered, src)
        hit = r["verdict"] == "FAIL"
        caught += 1 if hit else 0
        if not hit:
            missed.append((tok, bad))
        print("    %02d %-14s -> %-14s %s" % (i, tok, bad, "检出" if hit else "漏检 ⚠"))

    # 3) 对照：改成原文里存在的另一个事实，不应误报
    print("\n[3] 对照组（改成原文里真实存在的另一个事实，不应误报）")
    others = [t for t in candidates if exp.count(t) >= 1]
    control_ok = True
    if len(others) >= 2:
        a, b = others[0], others[-1]
        if a != b and b in src:
            r = check(exp.replace(a, b, 1), src)
            control_ok = r["verdict"] == "PASS"
            print("    %-14s -> %-14s %s" % (a, b, "未误报" if control_ok else "误报 ⚠"))
    else:
        print("    样本里没有两个可互换的事实，跳过（不算失败）")

    recall = caught / len(cases) if cases else 0
    print("\n结果：篡改召回 %d/%d（%.0f%%）｜基线 PASS｜对照 %s"
          % (caught, len(cases), recall * 100, "未误报" if control_ok else "误报"))
    all_ok = recall == 1.0 and control_ok
    print("结论：%s" % ("忠实性可被机器证明（且不误伤真事实）" if all_ok else "存在漏检或误报，证明不成立"))
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()

