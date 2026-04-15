# 3-3 JSX 基礎語法與在 Next.js 中的實際寫法

## 核心內容

- 這一節的學習目標是先看懂 **React 元件回傳的 JSX 到底在寫什麼**，以及哪些語法規則會直接影響你能不能正常渲染畫面。
- JSX 是把 JavaScript 與類 HTML 標記結合在一起的語法，讓你能在元件裡直接描述 UI 結構與要顯示的資料。
- 在目前這個專案裡，最直接的觀察點是 App Router 的頁面檔：
  - `src/app/page.tsx`
- 依本地 Next.js 文件 `node_modules/next/dist/docs/01-app/index.md` 與 `node_modules/next/dist/docs/01-app/01-getting-started/03-layouts-and-pages.md`，目前專案是 **App Router**，首頁通常由 `app/page.tsx` 或 `src/app/page.tsx` 這類檔案 default export React component 來產生畫面。
- JSX 幾個必懂規則：
  - 元件回傳時需要有單一根節點。
  - 如果不想多包一層 DOM，可以用 fragment。
  - JSX 標籤必須正確關閉。
  - 屬性名稱通常使用 camelCase，例如 `onClick`。
  - HTML 的 `class` 在 JSX 裡要改成 `className`。
  - 動態資料要放在大括號 `{}` 內。
- JSX 也是 React 宣告式渲染的入口。你描述「畫面應該長什麼樣子」，React 會依資料狀態更新 UI。
- 開發時如果 JSX 語法錯誤，Next.js 開發伺服器通常會立刻在頁面或終端顯示錯誤位置，這是你修正語法問題的第一個訊號。

## 開發上可採取的行動步驟

### 1. 用目前專案首頁練習辨識 JSX 結構

- 打開 `src/app/page.tsx`，先不要急著改功能，先辨認：
  - 最外層根節點是哪一個元素
  - 哪些內容是純文字
  - 哪些內容是動態插值或元件，例如 `Image`
- 這一步的目的，是先把「React component 回傳 JSX」這件事看成日常讀碼能力。

### 2. 先做一次最小可用的 JSX 簡化

- 你可以把 `src/app/page.tsx` 暫時改成最小版本，例如只保留一個 `<main>` 或 fragment，確認自己能安全改動 JSX 結構。
- 如果課程示範要你刪掉大段預設首頁內容，這在目前專案仍然可行，操作位置應該放在 `src/app/page.tsx`。

### 3. 刻意練習 JSX 的基本規則

- 練習新增一個清單：
  - `<ul>`
  - 多個 `<li>`
- 練習確認每個元素都有正確 closing tag，或在需要時使用 self-closing tag。
- 練習把 `className` 加到元素上，觀察 Tailwind class 是否有正確生效。
- 練習綁定一個 `onClick` 事件，熟悉 JSX 屬性命名規則。

### 4. 用變數插值理解動態內容

- 在元件內宣告簡單變數，例如 `const name = "John Doe"`。
- 在 JSX 中用 `{name}` 輸出，建立「資料進 JSX，React 幫你渲染」的直覺。
- 接著再把這個模式延伸到陣列 `map()`、條件渲染與事件處理，後面學 React 互動邏輯會更順。

### 5. 把錯誤訊息當成 JSX 學習工具

- 刻意觀察這些常見錯誤：
  - 少一個 closing tag
  - 回傳兩個根節點
  - 把 `className` 寫成 `class`
- 然後看 Next.js dev server 或瀏覽器錯誤覆蓋層指出哪一行有問題。這能幫你更快建立 JSX 語感。

## 我可以立刻採取的實作清單

- 打開 `src/app/page.tsx`，先指出目前 JSX 的根節點是哪個元素。
- 把首頁內容暫時改成：
  - 一個標題
  - 一段文字
  - 一個簡單清單
- 新增 `const name = "你的名字"`，並用 `{name}` 顯示在標題或段落中。
- 新增一個按鈕，綁定 `onClick={() => console.log("clicked")}`。
- 故意把某個標籤少寫 closing tag，觀察錯誤提示，再改回正確寫法。
- 檢查所有樣式屬性是否都使用 `className`，不要寫成 `class`。

## 總結

這一節真正要你學會的，是 **把 JSX 當成 React 元件的畫面描述語言**，並熟悉它和 HTML 相似但更嚴格的語法規則。對目前這個 Next.js 專案而言，最實際的練習位置就是 `src/app/page.tsx`；先在這裡熟悉根節點、`className`、`onClick`、大括號插值與標籤關閉規則，後面讀元件、props、事件與條件渲染時會順很多。
