"""statusLine 指令：常駐顯示目前 context 的絕對 token 數，以及提醒、壓縮門檻。

不用 used_percentage：它以模型完整視窗計算，1M 模型在 12 萬時只顯示 12%，看起來很安全。
門檻要與 context-check.py 的 CONTEXT_REMIND_TOKENS 一致；COMPACT 是實際壓縮點，
= settings.json 的 autoCompactWindow（183000）減去 /context 顯示的 Autocompact buffer（約 33k）。
"""
import json
import os
import sys

REMIND = int(os.environ.get("CONTEXT_REMIND_TOKENS", "120000"))
COMPACT = 150000
GREEN, YELLOW, RED, RESET = "\033[32m", "\033[33m", "\033[31m", "\033[0m"


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    cw = data.get("context_window") or {}
    n = cw.get("total_input_tokens")
    if n is None:
        u = cw.get("current_usage") or {}
        n = sum(u.get(k) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))
    color = GREEN if n < 80000 else YELLOW if n < REMIND else RED
    model = (data.get("model") or {}).get("display_name", "")
    print(f"{model} │ {color}ctx {n // 1000}k{RESET} │ 提醒 {REMIND // 1000}k │ 壓縮 {COMPACT // 1000}k")


if __name__ == "__main__":
    main()
