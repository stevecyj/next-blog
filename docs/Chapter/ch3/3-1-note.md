# 3-1 為什麼學 Next.js 前要先懂 React

## 核心內容

- 這一節要建立的核心觀念是：**Next.js 的開發體驗建立在 React 之上**。
- 如果沒有 React 的基本理解，之後看到元件、props、state、事件處理、條件渲染、清單渲染時，會很容易只會照抄，卻不知道自己在改什麼。
- 以目前這個專案來看，雖然你主要會在 `src/app/` 裡寫 Next.js，但裡面的頁面與 layout 本質上仍然是 React 元件：
  - `src/app/page.tsx`
  - `src/app/layout.tsx`
- 依本地 Next.js 文件 `node_modules/next/dist/docs/01-app/index.md`，App Router 會直接使用 React 的能力，例如 Server Components、Suspense、Server Functions。這代表你會**透過 Next.js 實際使用 React**。
- 所以這章的學習定位很明確：
  - 先補到足以讀懂 Next.js 程式碼、能繼續往下學的 React 基礎

## 開發上可採取的行動步驟

### 1. 先把 React 元件視角建立起來

- 打開 `src/app/page.tsx`，先不要急著看 Next.js API，先問自己：
  - 這是不是一個 React function component？
  - JSX 是怎麼組出畫面的？
  - `Image` 元件為什麼可以像 HTML 標籤一樣被使用？
- 如果這三題答不順，表示你要先補 React 基礎，再往後學。

### 2. 先掌握繼續學 Next.js 最低限度需要的 React 概念

- 這一節之後至少要能理解：
  - 元件是什麼
  - JSX 怎麼寫
  - props 怎麼傳資料
  - `map()` 如何渲染清單
  - 條件渲染怎麼做
  - 事件處理怎麼綁定
  - `useState` 在互動元件中的角色
- 不用一開始就鑽很深，但至少要能自己看懂簡單元件。

### 3. 用目前專案做 React 基礎練習

- 可直接從 `src/app/page.tsx` 開始做小改動：
  - 改首頁標題文字
  - 多加一段說明文字
  - 把目前的連結按鈕改成你自己的文案
- 這樣你會同時練到：
  - JSX 編寫
  - 元件回傳結構
  - props 與元件匯入的閱讀方式

### 4. 分清楚 React 與 Next.js 各自解什麼問題

- React 主要處理：
  - 元件化 UI
  - 狀態與互動
  - 畫面組裝
- Next.js 主要在 React 之上補上：
  - 路由結構
  - 預設專案架構
  - 伺服器端能力
  - 建置與部署流程
- 這個分工一旦清楚，之後遇到問題時，你比較知道自己該查 React 還是查 Next.js。

## 我可以立刻採取的實作清單

- 打開 `src/app/page.tsx`，把它當 React 元件逐行讀一次。
- 嘗試說出 `page.tsx` 回傳的 JSX 結構在畫面上會長什麼樣子。
- 把首頁 `<h1>` 文案改成自己的句子，確認你能安全修改 JSX。
- 新增一個簡單陣列並用 `map()` 渲染成 3 個列表項目，練習 React 的清單渲染。
- 新增一個按鈕與 `onClick` 事件，哪怕只是 `console.log`，也先把事件處理接起來。
- 如果你對 `useState` 還不熟，先做一個最小互動元件，例如點擊按鈕切換一段文字。

## 總結

這一節是在幫你校正學習順序：**先有 React 的基本操作能力，再學 Next.js，才看得懂框架背後在做什麼**。對目前這個專案而言，你接下來最務實的做法，是直接從 `src/app/page.tsx` 開始做幾個小改動，把 React 元件、JSX 與互動流程先摸熟。
