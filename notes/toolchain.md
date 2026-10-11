---
name: toolchain-install-policy
description: 本機安裝工具的分界原則：自帶更新器的應用不交給 Homebrew，函式庫才交給 brew
metadata:
  type: project
---

2026-09-22 定案的本機工具安裝原則：

- **自己會更新的應用**（Claude Code CLI、Claude.app、瀏覽器類）→ 用官方 native installer，讓它自己更新，不經過套件管理器。
- **不會自己更新的函式庫／CLI**（ffmpeg 及編解碼器、mlx、python、uv、sqlite、nvm）→ 交給 Homebrew。

**Why:** claude 原本用 `npm install -g` 裝在 `~/.nvm/versions/node/<版本>/` 底下，global 套件跟著 node 版本走，一旦 `nvm install` 換版就會消失；npm 12 的 allow-scripts 又會擋 postinstall，導致 native binary 連結不上。2026-09-02 的背景自動更新就是這樣失敗的。brew cask 雖然也能脫離 nvm，但官方明載不自動更新、stable 通道落後約一週，且是原地覆蓋而非原子性切換。

**How to apply:** Claude Code 現在裝在 `~/.local/bin/claude` →
`~/.local/share/claude/versions/`，PATH 由 `~/.zprofile` 提供。日後要裝新工具先問：它自己會不會更新？會就別包給 brew。`.zshrc` 的 brew 自動更新腳本維持只管 nvm，不要把 `brew upgrade claude-code` 加進去。

相關：[[ai-shorts-pipeline-decisions]]
