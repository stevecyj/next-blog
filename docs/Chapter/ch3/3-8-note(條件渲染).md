# 3-8 條件渲染（Conditional Rendering）

## 核心內容

條件渲染讓元件依狀態決定哪些 JSX 要輸出，哪些不輸出。

- 狀態通常用 boolean 表示（如 `isVisible`），語意比用字串更清晰。
- **三元運算子**：適合依條件切換不同的值或文字。
  ```tsx
  {isVisible ? 'hide' : 'show'}
  ```
- **邏輯 AND 運算子**：適合條件為 false 時完全不渲染任何東西。
  ```tsx
  {isVisible && <Fragment>...內容...</Fragment>}
  ```
  當條件為 `false`，React 不渲染任何 DOM 節點。
- **JSX 指派給變數**：把條件渲染的結果存入變數，讓 JSX 本體更乾淨。
  ```tsx
  const cards = isVisible && <Fragment>...內容...</Fragment>
  // 在 return 中直接使用
  {cards}
  ```
- 多個相鄰元素需用 `<Fragment>` 或 `<>` 包裝，才能作為單一表達式回傳。

## 開發上可採取的行動步驟

1. 將控制顯示邏輯的狀態命名為 boolean（`isVisible`、`isOpen`、`isLoading`），而非字串。
2. 切換狀態時用函式型更新確保基於最新值：
   ```tsx
   setIsVisible(prev => !prev)
   ```
3. 依場景選擇寫法：
   - 只切換文字/樣式 → 三元運算子
   - 整塊內容顯示/隱藏 → `&&` 或 JSX 變數
4. 多個平行元素用 `<Fragment>` 包裝，避免多餘的 DOM 層級。
5. 當條件渲染邏輯變複雜，先抽成 JSX 變數，保持 `return` 內部易讀。

## 我可以立刻採取的實作清單

- [ ] 在現有元件中找一個用字串狀態控制按鈕文字的地方，改用 boolean `isVisible` 重寫。
- [ ] 用 `&&` 運算子實作一個可收合的區塊，按鈕點擊後整塊內容消失/出現。
- [ ] 將條件渲染的 JSX 抽出成 `const content = ...` 變數，確認 `return` 更簡潔。
- [ ] 在 `&&` 右側故意放數字 `0`，觀察 React 渲染 `0` 而非空白的行為，並用 `!!` 或明確比較修正。

## 總結

React 條件渲染有三種主要寫法：三元運算子（切換不同值）、邏輯 AND（有或無）、JSX 變數（抽出複雜邏輯）。選擇哪種取決於場景，核心原則是讓 `return` 內的 JSX 保持易讀。

---

## 結構化提示詞指南

### 提示詞結構原則

```
[目標檔案/元件] + [目前狀態描述] + [要完成的具體行為] + [驗證條件]
```

### 任務一：用三元運算子切換按鈕文字

```
在 [目標元件，例如 app/page.tsx] 中：
- 目前有一個 useState 管理字串 label（'show' / 'hide'）
- 把它改成 boolean isVisible（預設 true）
- 按鈕文字改用三元運算子：{isVisible ? 'hide' : 'show'}
- 點擊後呼叫 setIsVisible(prev => !prev)
請指出修改了哪幾行。
```

### 任務二：用 && 運算子顯示/隱藏區塊

```
在 [目標元件] 新增條件渲染：
- 用 isVisible && <Fragment>...</Fragment> 包裝現有的卡片列表
- 按鈕點擊時切換 isVisible
- 確認 isVisible 為 false 時 DOM 中完全沒有卡片節點
```

### 任務三：把條件渲染抽成 JSX 變數

```
在 [目標元件] 中：
- 找到用 && 寫的條件渲染 JSX
- 把它抽成 const cards = isVisible && <Fragment>...</Fragment>
- 在 return 中改用 {cards} 渲染
- 確認功能不變，並說明 return 內部行數的變化
```

### 通用提示詞模板

```
檔案：[path]
目前狀況：[元件現在怎麼寫的]
目標：[要加什麼或改什麼]
限制：[不能動的部分，或要遵守的規則]
驗證：[怎麼確認它正確運作]
```
