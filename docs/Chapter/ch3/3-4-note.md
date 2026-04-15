# 3-4 React 元件與 Props 基礎

## 核心內容

- 這一節的學習目標是理解 **React 元件的結構與命名規則**，以及如何透過 **props** 把資料從父元件傳遞給子元件。
- React 元件就是一個回傳 JSX 的 JavaScript 函式。元件把 HTML 結構、CSS 樣式、JavaScript 邏輯封裝在一起，成為可重複使用的 UI 單元。
- 元件命名必須以**大寫字母**開頭，React 用這個規則區分自訂元件和原生 HTML 標籤。
- 最佳慣例：**一個元件對應一個檔案**，用 `export default` 匯出，需要時再 `import` 使用。
- 在 JSX 裡使用元件時，把元件名稱當成 HTML 標籤寫，例如 `<Card />`。
- Props（properties 的縮寫）是父元件傳遞資料給子元件的機制：
  - 父元件透過 HTML 屬性的語法傳值，例如 `<Card text="Hello" />`。
  - 子元件的函式接收 `props` 參數，透過 `{props.text}` 在 JSX 中渲染。
- Tailwind CSS 在元件裡同樣透過 `className` 屬性套用，例如 `border rounded-md border-gray-600 p-4`。

## 開發上可採取的行動步驟

### 1. 建立第一個獨立元件檔案

- 在 `src/components/` 或 `src/app/` 下新增一個檔案，例如 `Card.tsx`。
- 確認命名以大寫字母開頭。
- 函式回傳 JSX，加上 `export default`。
- 操作範例：

  ```tsx
  export default function Card() {
    return (
      <div className="border rounded-md border-gray-600 p-4">
        Card component
      </div>
    );
  }
  ```

### 2. 在頁面中使用元件並驗證可重複使用性

- 在 `src/app/page.tsx` import 該元件，然後放置多次。
- 確認每個 `<Card />` 都能正常渲染，驗證元件是可複用的 UI 單元。

### 3. 加入 Props，讓元件接受外部資料

- 在元件函式加入 `props` 參數，並在 JSX 中用大括號插值渲染：

  ```tsx
  export default function Card(props: { text: string }) {
    return (
      <div className="border rounded-md border-gray-600 p-4">
        {props.text}
      </div>
    );
  }
  ```

- 在父元件傳入不同文字：

  ```tsx
  <Card text="第一張卡片" />
  <Card text="第二張卡片" />
  ```

### 4. 用解構語法讓 Props 更簡潔（實務常見寫法）

- 把 `props` 改成解構參數，讓程式碼更直接：

  ```tsx
  export default function Card({ text }: { text: string }) {
    return (
      <div className="border rounded-md border-gray-600 p-4">
        {text}
      </div>
    );
  }
  ```

## 我可以立刻採取的實作清單

- 在 `src/components/Card.tsx` 建立 Card 元件，回傳帶有 Tailwind 樣式的 div。
- 在 `src/app/page.tsx` 加入 `import Card from "@/components/Card"`。
- 放置三個 `<Card />` 並確認畫面出現三個相同的卡片。
- 為 Card 加入 `text` prop，分別傳入不同字串，確認每張卡片顯示不同內容。
- 把 `props` 改成解構參數寫法，確認功能不受影響。
- 確認所有樣式都透過 `className` 而非 `class` 屬性設定。

## 總結

這一節的核心是建立「**元件 = 可複用的 JSX 函式**」的概念，並透過 props 機制讓元件接受外部資料，成為真正靈活的 UI 單元。在目前 Next.js 專案中，建議養成一個元件一個檔案的習慣，放在 `src/components/` 下集中管理，並善用 TypeScript 型別標注 props，這樣在多人協作或元件數量增加時會更容易維護。
