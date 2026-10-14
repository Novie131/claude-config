# claude-config

我的 Claude Code 個人設定（`~/.claude/`），以繁體中文為主。

| 檔案 | 用途 |
|---|---|
| `CLAUDE.md` | 全域偏好：一律繁體中文、工作方式、動電腦前先問、拷問規則、context 管理、何時委派子 agent |
| `settings.json` | 模型與 effort、自動壓縮門檻（183k，扣掉約 33k buffer 後實際約 150k 壓縮）、context 提醒 hook、狀態列、啟用的 plugin |
| `agents/Explore.md` | 覆蓋內建 Explore：改用 haiku、只給 Read/Grep/Glob |
| `agents/bulk.md` | 處理大量輸出（圖片、網頁、長 log）、只回傳結論的子 agent |
| `hooks/context-check.py` | `UserPromptSubmit` hook：context 超過 120k 時，要 Claude 先更新交接筆記，再依情況給一句可複製的指令（`/clear`、指定重點的 `/compact`、`/rewind` 局部摘要） |
| `hooks/statusline.py` | 狀態列：顯示 context 的絕對 token 數與提醒、壓縮門檻，依大小變色（不用 `used_percentage`，因為 1M 模型在 120k 時只顯示 12%） |
| `notes/toolchain.md` | 本機工具安裝原則（被 `CLAUDE.md` 引用） |

## 使用方式

直接 clone 到 `~/.claude` 會跟既有檔案衝突，建議只挑需要的檔案複製過去。
`settings.json` 裡的 hook 與狀態列路徑寫死為 `~/.claude/hooks/` 底下的檔案。

## 不在這裡的東西

`.gitignore` 採白名單，對話紀錄、專案記憶、`~/.claude.json`（登入資料）、shell 快照等一律不收錄。
