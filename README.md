# claude-config

我的 Claude Code 個人設定（`~/.claude/`），以繁體中文為主。

| 檔案 | 用途 |
|---|---|
| `CLAUDE.md` | 全域偏好：一律繁體中文、工作方式、動電腦前先問、拷問規則、context 管理、何時委派子 agent |
| `settings.json` | 模型與 effort、自動壓縮門檻、context 提醒 hook、啟用的 plugin |
| `agents/Explore.md` | 覆蓋內建 Explore：改用 haiku、只給 Read/Grep/Glob |
| `agents/bulk.md` | 處理大量輸出（圖片、網頁、長 log）、只回傳結論的子 agent |
| `hooks/context-check.py` | `UserPromptSubmit` hook：context 超過 120k 時提醒更新交接筆記並 `/clear` |
| `notes/toolchain.md` | 本機工具安裝原則（被 `CLAUDE.md` 引用） |

## 使用方式

直接 clone 到 `~/.claude` 會跟既有檔案衝突，建議只挑需要的檔案複製過去。
`settings.json` 裡的 hook 路徑寫死為 `~/.claude/hooks/context-check.py`。

## 不在這裡的東西

`.gitignore` 採白名單，對話紀錄、專案記憶、`~/.claude.json`（登入資料）、shell 快照等一律不收錄。
