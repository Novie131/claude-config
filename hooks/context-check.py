#!/usr/bin/env python3
"""UserPromptSubmit hook：對話 context 超過門檻時，讓 Claude 提醒使用者 /clear。

只在跨過門檻、或之後每多 STEP 個 token 時提醒一次，避免每輪都提醒。
門檻可用環境變數 CONTEXT_REMIND_TOKENS 覆寫（測試時可設低一點）。
"""
import json, os, sys

THRESHOLD = int(os.environ.get("CONTEXT_REMIND_TOKENS", "120000"))
STEP = 40000


def context_sizes(path):
    """依序回傳主對話中每次 API 呼叫的 context 大小（同一則訊息只算一次）。"""
    sizes, seen = [], set()
    with open(path, errors="ignore") as f:
        for line in f:
            try:
                d = json.loads(line)
            except ValueError:
                continue
            m = d.get("message")
            if d.get("type") != "assistant" or d.get("isSidechain") or not isinstance(m, dict):
                continue
            u = m.get("usage")
            if not u or m.get("id") in seen:
                continue
            seen.add(m.get("id"))
            sizes.append(u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
                         + u.get("cache_read_input_tokens", 0))
    return sizes


def bucket(n):
    return -1 if n < THRESHOLD else (n - THRESHOLD) // STEP


def main():
    try:
        path = json.load(sys.stdin).get("transcript_path")
        sizes = context_sizes(path) if path else []
    except Exception:
        return  # 任何錯誤都不擋使用者的訊息
    if not sizes:
        return
    now = sizes[-1]
    prev = sizes[-2] if len(sizes) > 1 else 0
    if bucket(now) < 0 or bucket(now) <= bucket(prev):
        return
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": (
            f"目前對話的 context 約為 {now // 1000}k tokens，已超過 {THRESHOLD // 1000}k 的提醒門檻。"
            "依使用者的 CLAUDE.md 規則，此時應先更新 handoff.md（不論使用者是否 /clear），"
            "並在回答結尾提醒使用者：若手上這件事已告一段落，可以執行 /clear。"
        ),
    }}, ensure_ascii=False))


if __name__ == "__main__":
    main()
