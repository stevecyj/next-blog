# 4-2 Next.js 路由與頁面建立

## 核心內容

Next.js 採用**檔案系統路由**（File System Router）：資料夾結構即路由結構，無需額外設定。

- 路由由 `app/` 目錄下的資料夾層級決定，資料夾名稱對應 URL 路徑段
- 只有在資料夾內建立 `page.js`（或 `.tsx`）才會成為公開頁面；其他檔案放在同資料夾不影響路由
- 巢狀資料夾產生巢狀路徑，例如 `app/about/projects/page.tsx` → `/about/projects`
- 目前專案使用 **App Router**（非舊版 Pages Router），所有頁面預設為 Server Component，在伺服器端渲染
- 若頁面元件需要使用 `useState` 等客戶端狀態，必須在檔案頂端加上 `'use client'` 指令

## 開發上可採取的行動步驟

1. 確認路由需求：列出網站所需的 URL 路徑清單
2. 在 `app/` 下依路徑建立對應資料夾，巢狀資料夾對應巢狀路徑
3. 在每個要公開的資料夾內新增 `page.tsx`，並 export 一個 React 元件
4. 頁面元件命名慣例：以 `Page` 結尾（如 `AboutPage`、`ProjectsPage`），首字母大寫
5. 若頁面需要用戶端互動（state、event），在檔案頂端加 `'use client'`

## 我可以立刻採取的實作清單

- [ ] 在 `src/app/about/page.tsx` 建立 About 頁面，export `AboutPage` 元件
- [ ] 在 `src/app/about/projects/page.tsx` 建立 Projects 頁面，export `ProjectsPage` 元件
- [ ] 確認 `src/app/page.tsx`（主頁）是否需要 `'use client'`，僅在有 state 時才加

## 總結

App Router 的路由規則簡單直觀：資料夾 = 路徑，`page.tsx` = 公開頁面。建立新頁面就是建立資料夾加檔案，不需要任何路由設定檔。預設 Server Component 可提升效能，只在必要時才標記 `'use client'`。
