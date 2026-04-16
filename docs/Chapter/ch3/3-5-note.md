# 3-5 Props 進階：預設值、children 與元件組合

## 核心內容

- 這一節的學習目標是把 `props` 從「只是傳字串」提升到「設計元件 API」的層次，能正確處理預設值、巢狀內容與元件組合。
- `props` 不只可以傳字串，也可以傳 JavaScript 表達式、數字、布林值、函式，甚至 JSX。只要放在 `{}` 中，React 就會把它當成 JavaScript 值處理。
- 子元件收到的第一個參數本質上就是一個物件，因此可以直接用解構語法拿出需要的欄位，讓元件寫法更簡潔。
- 當某些 prop 不是必填時，可以在函式參數上設定預設值，讓元件在沒有收到資料時仍能安全渲染。
- `children` 是 React 提供的特殊 prop。當你用 `<Card>內容</Card>` 這種開關標籤寫法時，中間的內容就會被傳進 `children`。
- 在目前專案裡，`[src/app/layout.tsx](/Volumes/data/Projects-practice/next-blog/src/app/layout.tsx:21)` 已經是 `children` 的真實例子。`RootLayout` 接收 `children: React.ReactNode`，再把頁面內容渲染到 `<body>` 內。
- `children` 讓元件可以承接文字、HTML 結構，甚至另一個 React 元件，因此能做出 wrapper、section、card、layout 這類可組合的 UI。
- `props` 一律視為唯讀資料。子元件不應直接修改收到的 prop；如果需要改變畫面狀態，應該由父元件更新資料，再重新傳給子元件。

## 開發上可採取的行動步驟

### 1. 把展示型元件改成解構 props + 預設值

- 如果你要在這個專案延續前一節的例子，建議新增 `src/components/Card.tsx`，並直接使用 TypeScript 型別定義：

```tsx
type CardProps = {
  title?: string;
  children?: React.ReactNode;
};

export default function Card({
  title = "Untitled card",
  children,
}: CardProps) {
  return (
    <section className="rounded-lg border border-zinc-300 p-4">
      <h2 className="mb-2 text-lg font-semibold">{title}</h2>
      <div>{children}</div>
    </section>
  );
}
```

- 這種寫法比 `props.title` 更容易閱讀，也能在缺少資料時提供穩定輸出。

### 2. 在頁面中區分「簡單資料」與「可組合內容」

- 如果只是傳單一文字、狀態或設定值，用一般 prop，例如 `title="Welcome"`。
- 如果元件內部要放一段完整內容、按鈕、清單或其他元件，改用 `children` 更自然：

```tsx
<Card title="Welcome">
  <p>這裡可以放段落、按鈕，或另一個元件。</p>
</Card>
```

- 對目前專案來說，這個練習最適合放在 `[src/app/page.tsx](/Volumes/data/Projects-practice/next-blog/src/app/page.tsx:1)`。

### 3. 練習元件組合，而不是把所有內容寫死在同一個元件裡

- 你可以讓 `Card` 裡面再包另一個 `Card`、清單元件或 CTA 按鈕，觀察 UI 如何被一層一層組合出來。
- 這是 React 開發中很核心的能力，因為很多 reusable UI 都是靠 `children` 與組合關係建立起來的。

### 4. 維持單向資料流，避免在子元件內修改 props

- 如果子元件需要通知父元件某件事發生，傳入 callback prop，例如 `onSelect`、`onClose`、`onSubmit`。
- 由父元件處理狀態更新，再把新的值往下傳。這樣資料流向才清楚，也比較容易除錯。

## 我可以立刻採取的實作清單

- 在 `src/components/Card.tsx` 建立一個支援 `title` 與 `children` 的元件。
- 用解構參數取出 `title`、`children`，並為 `title` 設定預設值。
- 在 `src/app/page.tsx` 放入至少兩個 `<Card />`，一個只傳 `title`，一個改用 `children` 放段落內容。
- 觀察 `[src/app/layout.tsx](/Volumes/data/Projects-practice/next-blog/src/app/layout.tsx:21)` 的 `children` 型別與渲染方式，理解這和自製 `Card` 元件是同一種模式。
- 練習把一個元件包進另一個元件，例如在 `Card` 內再放一個按鈕或清單。
- 檢查自己是否有寫出像 `props.title = "new title"` 這種直接修改 prop 的程式碼；如果有，改成由父元件控制資料。
- 如果子元件需要互動，改用 callback prop 把事件往上傳，而不是在子元件內硬改外部資料。

## 總結

這一節真正要建立的是「**元件的輸入介面要怎麼設計**」的觀念。`props` 負責傳遞設定與資料，`children` 負責承接可組合的內容，而單向資料流保證每個元件的責任邊界清楚。對這個 Next.js 專案來說，先從 `src/app/layout.tsx` 理解 `children`，再把相同模式套用到 `src/components/Card.tsx`，會是最實際也最容易吸收的練習路徑。
