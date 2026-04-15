# 2-3 認識 Next.js 專案結構

## 核心內容

- 建立「哪些東西是框架產物、哪些是你的應用程式、哪些是設定檔」。
- 以目前這個專案來看，最重要的三塊是：
  - `src/app/`：App Router 的主要應用程式入口，包含頁面、layout、全域樣式。
  - `public/`：靜態資源目錄，檔案會直接暴露在網站根路徑下。
  - 根目錄設定檔：`package.json`、`tsconfig.json`、`next.config.ts`、`eslint.config.mjs`、`.gitignore`。
- 不應手動維護的內容：
  - `.next/`：`next dev` / `next build` 產生的輸出。
  - `node_modules/`：套件安裝結果，遺失時可重裝。
- 字幕裡有幾個版本相關說法需要校正：
  - 現在的專案不是根目錄 `app/`，而是 `src/app/`。
  - 目前專案不是 `jsconfig.json`，而是 `tsconfig.json`。
  - 目前專案不是 `.eslintrc.json`，而是 `eslint.config.mjs`。
  - App Router 不是「Next.js 12 才引入 app folder」這種簡化說法；依目前本地 Next.js 文件，App Router 是新版主要路由系統，`create-next-app` 也會直接提供 App Router 選項。
- 目前專案實際可見的重要檔案如下：
  - `src/app/layout.tsx`
  - `src/app/page.tsx`
  - `src/app/globals.css`
  - `src/app/favicon.ico`
  - `public/next.svg`
  - `next.config.ts`
  - `eslint.config.mjs`
  - `tsconfig.json`
  - `package.json`

## 開發上可採取的行動步驟

### 1. 先用「會不會手改」來分專案

- 第一眼先把專案分成三類：
  - 框架輸出：`.next/`
  - 套件依賴：`node_modules/`
  - 真正要維護的程式與設定：`src/`、`public/`、各種 config 檔
- 這樣做的目的，是避免一開始就把注意力放到不該改的地方。

### 2. 先確認你的 App Router 放在哪裡

- 這個專案的主要程式碼在 `src/app/`，不是根目錄 `app/`。
- 所以看到教學提到 `app/page.tsx` 時，要主動映射成你專案裡的 `src/app/page.tsx`。
- 可先打開：
  - `src/app/page.tsx`
  - `src/app/layout.tsx`
  - `src/app/globals.css`

### 3. 用 `public/` 實際驗證靜態資源規則

- 啟動開發伺服器：

```bash
npm run dev
```

- 然後直接用瀏覽器打開：

```text
http://localhost:3000/next.svg
```

- 如果能直接看到圖片，就表示你理解了 `public/` 的規則：
  - 放進 `public/` 的檔案，不需要額外 route 設定
  - 會直接掛在網站根路徑下

### 4. 讀 `package.json` 時先看 scripts 與依賴分工

- 目前這個專案的 scripts 是：
  - `dev`
  - `build`
  - `start`
  - `lint`
- 目前執行期依賴是：
  - `next`
  - `react`
  - `react-dom`
- 目前開發期依賴包含：
  - `typescript`
  - `eslint`
  - `eslint-config-next`
  - `tailwindcss`
- 你要建立的理解是：
  - `dependencies` 決定 app 跑不跑得起來
  - `devDependencies` 決定開發體驗與工具鏈

### 5. 用 `tsconfig.json` 理解 alias 與型別環境

- 目前 `tsconfig.json` 裡有：

```json
"paths": {
  "@/*": ["./src/*"]
}
```

- 這代表 `@/` 會從 `src/` 開始找檔案。
- 之後你在匯入元件時，可以少寫很多層 `../../`。

### 6. 把設定檔當成「責任邊界」

- `next.config.ts`
  - 控制 Next.js 行為，目前還是空白預設配置。
- `eslint.config.mjs`
  - 控制 lint 規則，目前接了 `eslint-config-next` 的 `core-web-vitals` 與 TypeScript 設定。
- `.gitignore`
  - 控制哪些內容不要進版控，例如 `node_modules/`、`.next/`。
- 這種看法比死記檔名更有用，因為之後專案長大時，你會知道該去哪裡改哪一類問題。

## 我可以立刻採取的實作清單

- 打開專案根目錄，先把 `.next/`、`node_modules/`、`src/`、`public/` 分類清楚。
- 打開 `src/app/page.tsx`、`src/app/layout.tsx`、`src/app/globals.css`，確認首頁是怎麼被組起來的。
- 執行 `npm run dev`，直接測試 `/next.svg` 是否可被存取。
- 打開 `package.json`，說出 `dev`、`build`、`start`、`lint` 各自用途。
- 打開 `tsconfig.json`，確認 `@/*` 實際指向 `./src/*`。
- 打開 `eslint.config.mjs`，確認它不是舊版 `.eslintrc.json` 格式。
- 打開 `next.config.ts`，理解它是未來客製 Next.js 行為的入口。

## 使用過的提示詞

### 1. 從逐字稿抽出真正的學習目標

```text
請根據 docs/Chapter/ch2/2-3-vtt.md，整理這一節真正要學會的能力，而不是逐字摘要。

請用繁體中文回答：
1. 這節的核心概念
2. 讀完後我應該能立刻做什麼
```

### 2. 對照目前專案，找出字幕裡過時或不精準的說法

```text
請對照目前專案實際結構，檢查 docs/Chapter/ch2/2-3-vtt.md 裡哪些說法需要校正。

請特別檢查：
- app 或 src/app
- jsconfig.json 或 tsconfig.json
- .eslintrc.json 或 eslint.config.mjs
- package.json 的 scripts 與依賴
- public 資料夾的實際用途
```

### 3. 用本地 Next.js 文件驗證版本敏感內容

```text
請依照 node_modules/next/dist/docs/ 內的本地 Next.js 文件，
檢查這一節對 App Router、create-next-app 與專案結構的描述是否仍然成立。

請用繁體中文列出：
1. 哪些說法仍然成立
2. 哪些說法需要修正
3. 修正後我應該怎麼理解目前的 Next.js 專案結構
```

### 4. 產出一組 10 分鐘內能完成的理解練習

```text
請根據目前這個 Next.js 專案，設計一組 10 分鐘內可以完成的練習，目標是讓我真正理解：
- src/app 的角色
- public 的角色
- package.json scripts
- tsconfig.json 裡的 @/* alias

每一步都要包含：
1. 我要打開或執行什麼
2. 我要觀察什麼
3. 做完後我會理解什麼
```

### 5. 生成自我檢查題

```text
請根據這個 Next.js 專案目前的檔案結構，出 8 題自我檢查題，並附上簡短答案。

題目要涵蓋：
- .next
- node_modules
- src/app
- public
- package.json
- tsconfig.json
- next.config.ts
- eslint.config.mjs
```

## 本節一句話總結

- 拿到一個新的 Next.js 專案時，先分清楚框架產物、應用程式目錄與設定檔，再開始改程式，效率會高很多。
