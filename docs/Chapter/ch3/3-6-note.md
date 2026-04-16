# 3-6 React 事件處理與 Client Component 邊界

## 核心內容

- 這一節的學習目標是學會在 React 中綁定事件，並理解在 Next.js App Router 專案裡，互動程式碼必須放在 client component。
- 在 JSX 中綁定事件時，屬性名稱使用 camelCase，例如 `onClick`、`onChange`、`onSubmit`。
- 事件處理器本質上是 JavaScript 函式。你可以先用 inline arrow function 快速驗證互動，再把它抽成元件內的命名函式，例如 `handleClick`。
- React 事件處理最常見的錯誤之一，是把函式「呼叫結果」塞進 `onClick`，像 `onClick={handleClick()}`。正確寫法是傳入函式本身：`onClick={handleClick}`。
- 事件處理函式可以接收事件物件，通常命名為 `event` 或 `e`。這讓你能讀取事件資訊，或呼叫 `event.preventDefault()` 攔截表單提交等預設行為。
- 目前這個專案的 `[src/app/page.tsx](/Volumes/data/Projects-practice/next-blog/src/app/page.tsx:3)` 仍是 App Router 預設的 server component。依照本地 Next 文件，頁面與 layout 預設都在 server 端執行，只有需要互動的部分才應切成 client component。
- 因此，課程裡「直接在檔案頂端加上 `'use client'`」雖然能讓事件跑起來，但實務上更好的做法通常是把按鈕、表單、切換器這類互動區塊抽到獨立的 client component，避免整個頁面都進入 client bundle。
- 本地 `use-client` 文件也提醒另一個重要限制：server component 傳給 client component 的 props 必須可序列化，所以不能把 server component 裡宣告的函式直接當成 `onClick` prop 傳下去。

## 開發上可採取的行動步驟

### 1. 先把互動區塊抽成最小 client component

- 目前專案還沒有 `src/components/` 目錄，這一節很適合從這裡開始建立可重用元件。
- 建議新增 `src/components/ClickButton.tsx`，把 `'use client'` 放在檔案最上方，讓互動只侷限在這個元件內。
- 範例：

```tsx
'use client';

export default function ClickButton() {
  function handleClick() {
    alert("Hello");
  }

  return (
    <button
      type="button"
      onClick={handleClick}
      className="rounded-md border border-zinc-300 px-4 py-2"
    >
      Click me
    </button>
  );
}
```

### 2. 由 `src/app/page.tsx` 匯入 client component，而不是整頁改成 client

- `[src/app/page.tsx](/Volumes/data/Projects-practice/next-blog/src/app/page.tsx:3)` 可以保持 server component，專心負責頁面結構。
- 把互動元件直接匯入頁面中使用：

```tsx
import ClickButton from "@/components/ClickButton";

export default function Home() {
  return (
    <main>
      <ClickButton />
    </main>
  );
}
```

- 這種拆法符合目前 Next.js 文件建議，也比較容易延伸到表單、搜尋框、modal 或 dropdown。

### 3. 養成事件命名與傳遞習慣

- 事件函式用 `handle...` 命名，例如 `handleClick`、`handleSubmit`、`handleToggle`，閱讀時一眼就知道責任。
- 如果事件邏輯很短，可以先用 inline function，例如 `onClick={() => console.log("clicked")}`。
- 一旦邏輯開始超過一行，或需要重複使用，立刻抽成獨立函式，避免 JSX 變得難讀。

### 4. 熟悉事件物件，為下一節表單處理做準備

- 在 `handleClick(event)` 或 `handleSubmit(event)` 中先 `console.log(event)` 看一次實際內容，理解 React 提供的是事件包裝物件。
- 練習使用 `event.currentTarget`、`event.target` 與 `event.preventDefault()`。
- 對表單來說，`preventDefault()` 幾乎是必備基礎，因為你通常不想讓瀏覽器直接用預設行為重新送出當前頁面。

### 5. 注意 client 邊界內外的資料限制

- 如果互動邏輯定義在 client component 內，就可以正常把函式傳給它的子元件。
- 如果父層是 server component，請傳資料值，不要傳函式。
- 想把 callback 往下傳時，代表那段父元件邏輯通常也應該位於 client 邊界內。

### 6. 用固定結構寫提示詞，讓 AI 真的能把功能做完

- 如果你是用 AI 協助實作，不要只丟一句「幫我加一個按鈕」。提示太短，AI 很容易不知道要改哪些檔案、該不該新建元件、是否要保留 server component 邊界。
- 這一節最實用的提示詞結構可以固定成五段：
  - 任務目標：你要完成什麼功能。
  - 專案現況：目前有哪些檔案、哪些檔案仍是 server component。
  - 實作限制：例如不要把整個 `src/app/page.tsx` 改成 client component。
  - 交付內容：你希望新增哪些檔案、修改哪些檔案。
  - 驗證方式：你要 AI 檢查什麼，例如事件是否可點擊、匯入是否正確。
- 你可以直接套用下面這個模板：

```text
請在目前的 Next.js App Router 專案中完成一個最小互動功能。

任務目標：
- 新增一個可點擊按鈕，點擊後執行簡單事件處理。

專案現況：
- `src/app/page.tsx` 目前是 server component。
- 專案目前還沒有 `src/components/ClickButton.tsx`。

實作限制：
- 不要把整個 `src/app/page.tsx` 改成 client component。
- 請把互動邏輯放在獨立的 client component。
- 使用 TypeScript 與現有專案結構。

交付內容：
- 新增 `src/components/ClickButton.tsx`
- 修改 `src/app/page.tsx`，把按鈕匯入並渲染到頁面上

驗證方式：
- 檢查 `onClick` 是否傳入函式參考，而不是函式呼叫結果。
- 確認 `'use client'` 只出現在互動元件檔案頂端。
- 回報你修改了哪些檔案與原因。
```

- 如果你想讓 AI 一次就做得更準，可以再補上「先讀檔、再改檔、最後驗證」這種執行順序要求：

```text
先閱讀 `src/app/page.tsx` 的現況，再建立最小可用的 `ClickButton` client component。
完成後請檢查匯入路徑、事件綁定與 client boundary 是否正確，最後再摘要說明修改內容。
```

- 當功能變大時，不要一次丟太多需求。先讓 AI 完成「按鈕可點擊」，再下一輪要求它把 `alert` 改成 `console.log`、狀態更新、表單提交處理或 `preventDefault()`。這樣每一步都比較容易驗證。
- 最後一個實用原則是把「不要做什麼」寫清楚。對這節來說，最關鍵的限制通常就是：
  - 不要把整頁改成 client component。
  - 不要直接在 server component 傳函式給 client component。
  - 不要只輸出範例程式碼，請直接修改實際檔案。

## 我可以立刻採取的實作清單

- 建立 `src/components/ClickButton.tsx`，在檔案頂端加入 `'use client'`。
- 在按鈕上綁定 `onClick={handleClick}`，不要寫成 `onClick={handleClick()}`。
- 先讓 `handleClick` 做最簡單的事，例如 `alert("Hello")` 或 `console.log("clicked")`。
- 把 `ClickButton` 匯入 `[src/app/page.tsx](/Volumes/data/Projects-practice/next-blog/src/app/page.tsx:3)`，確認頁面仍可正常渲染。
- 觀察是否只有互動元件是 client component，而不是整個頁面檔案都加上 `'use client'`。
- 把 `handleClick` 改成接收 `event`，並在 console 中查看事件物件內容。
- 額外做一個表單或連結點擊的小練習，實際呼叫 `event.preventDefault()`。
- 用上面的五段式模板，寫一則提示詞請 AI 幫你完成 `ClickButton`。
- 在 AI 完成後，逐項檢查它是否遵守你的限制條件，而不是只看畫面有沒有跑起來。

## 總結

這一節真正要建立的是三層能力：第一層是 React 的事件綁定基礎，知道 `onClick` 要接函式參考、事件物件能做什麼；第二層是 Next.js App Router 的執行邊界，知道互動程式碼應該放在 client component，而且 client 範圍應盡量縮小；第三層是把需求寫成結構化提示詞，讓 AI 能根據檔案現況、限制與驗證條件穩定完成實作。對這個專案來說，最實用的做法就是讓 `src/app/page.tsx` 保持 server component，然後把按鈕、表單等互動區塊抽到 `src/components/` 裡的獨立 client component，再用固定模板描述要改的檔案與不能踩到的邊界。
