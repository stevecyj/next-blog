# 3-9 渲染清單（Rendering Lists）

## 核心內容

實務上列表元件幾乎都來自陣列資料，透過 `Array.prototype.map()` 把每筆資料轉成 JSX。

- 用 `useState` 管理陣列資料，才能在修改時觸發重新渲染。
- `names.map((name) => <Card>{name}</Card>)` 會回傳一個 JSX 陣列，React 會依序渲染。
- 列表中每個**最外層**元素必須有唯一的 `key` prop，供 React 高效 diff。
  - `key` 只需在「該列表」中唯一，不需全域唯一。
  - 只要加在 map 回傳的最外層元素上，巢狀的子元件不需要再加。

### key 該用什麼？

- **首選**：資料本身穩定、唯一的 ID（例如後端回傳的 `id`、`uuid`、`slug`）。
- **次選**：確保不會重複的欄位（例如 email、SKU）。
- **最後手段**：陣列 index。僅當列表是「靜態、不會新增/刪除/重排」時才安全。
  - 若列表會變動用 index 當 key，React 會把舊元素的狀態「對到」新位置，造成畫面錯亂。
  - 課程影片中以 index 為 key 只是示範最低成本做法，實務應優先找穩定 ID。

### 修改狀態中的陣列

React 狀態要視為不可變（immutable），不能用 `push`、`splice`、`sort` 等會修改原陣列的方法。

```tsx
// 錯：直接 mutate
names.push('new element')

// 對：建立新陣列，透過 setter 交給 React
setNames([...names, 'new element'])
```

常見模式：

| 操作 | 寫法 |
| --- | --- |
| 新增到尾端 | `setNames([...names, newItem])` |
| 新增到開頭 | `setNames([newItem, ...names])` |
| 刪除某一筆 | `setNames(names.filter(n => n !== target))` |
| 更新某一筆 | `setNames(names.map(n => n.id === id ? { ...n, ...patch } : n))` |

## 開發上可採取的行動步驟

1. 把要渲染的清單資料用 `useState` 包起來，初始值給一個陣列。
2. 在 JSX 中用 `{items.map((item) => <Item key={item.id} ... />)}` 產生列表。
3. 為每個 map 回傳的最外層元素指定唯一的 `key`，優先用資料的穩定 ID。
4. 修改陣列狀態時一律回傳**新陣列**，用展開運算子或 `filter` / `map` 等不可變方法。
5. 若資料沒有 ID，考慮在新增時用 `crypto.randomUUID()` 或遞增計數器生成一個。

## 我可以立刻採取的實作清單

- [ ] 在 `app/page.tsx` 用 `useState` 放一個字串陣列 `names`，並用 `.map()` 渲染成多張 Card。
- [ ] 為每張 Card 加上 `key`，先用 index 看能不能跑，再換成自訂 ID 觀察差異。
- [ ] 加一顆「Add」按鈕，點擊後用 `setNames([...names, 'new element'])` 新增一筆。
- [ ] 加一顆「Delete」按鈕，用 `setNames(names.filter(...))` 刪除指定項目。
- [ ] 刻意在列表最前方插入一筆並把 `key` 設成 index，觀察各 Card 內部狀態（例如輸入框值）是否被錯誤搬移。

## 總結

渲染清單的三個關鍵：`useState` 管理陣列、`.map()` 把資料轉 JSX、為每個元素提供穩定唯一的 `key`。修改陣列狀態時永遠建立新陣列，不要 mutate 原本的值。

---

## 結構化提示詞指南

### 一、提示詞的五層結構

一個高效的提示詞 = **Context（上下文）+ Goal（目標）+ Constraints（限制）+ Steps（步驟）+ Verification（驗證）**。缺任何一層都會讓 AI 自己補洞，結果就不可預測。

| 層級 | 回答的問題 | 範例 |
| --- | --- | --- |
| Context | 檔案在哪？現在長怎樣？ | `app/page.tsx，目前用 useState 管 boolean isVisible` |
| Goal | 要完成什麼具體行為？ | `把寫死的 3 張 Card 改用 map 渲染` |
| Constraints | 不能動什麼？要遵守什麼？ | `不能用 push，必須不可變更新；沿用現有 Card 元件` |
| Steps | 要分幾步、按什麼順序？ | `1. 宣告 names 陣列 2. map 出 Card 3. 加 key` |
| Verification | 怎麼確認做對了？ | `點 Add 後 UI 多一張；console 確認舊陣列未被 mutate` |

### 二、分階段執行策略（Scaffold → Feature → Verify）

一次塞太多需求 AI 容易出錯。把功能拆成三個可獨立驗證的階段：

```
Stage 1 [Scaffold]：先把資料結構和 map 渲染跑起來
Stage 2 [Feature]：疊加互動功能（新增/刪除/更新）
Stage 3 [Verify]：刻意觸發邊界條件，確認 key/immutable 正確
```

每個階段的提示詞獨立送出，**驗證過關再進入下一階段**，而不是一次交付。

### 三、三階段提示詞範本

#### Stage 1：Scaffold — 建立 map 渲染骨架

```
[Context]
檔案：app/page.tsx
目前狀況：手動寫了三個 <Card>Pyotr</Card> / <Card>John</Card> / <Card>Terry</Card>

[Goal]
改用資料驅動：用 useState 管理一個 names 陣列，再 .map() 渲染成多張 Card。

[Constraints]
- 只能修改 app/page.tsx，Card 元件本身不動
- 不新增第三方套件
- 每張 Card 的 key 必須是陣列元素本身（字串），不要用 index

[Steps]
1. import { useState } from 'react'
2. 宣告 const [names, setNames] = useState(['Pyotr', 'John', 'Terry'])
3. 在 JSX 中用 {names.map(name => <Card key={name}>{name}</Card>)}
4. 刪掉原本寫死的三個 Card

[Verification]
- 畫面渲染結果與修改前完全一致
- 指出你修改了哪幾行
- 說明為什麼這個情境下用字串當 key 安全
```

#### Stage 2：Feature — 疊加新增/刪除功能

```
[Context]
檔案：app/page.tsx
目前狀況：Stage 1 已完成，names 陣列用 map 渲染為多張 Card

[Goal]
新增「Add」和「Delete」兩個互動：
- Add 按鈕：在陣列尾端新增一筆（文字 'new element'）
- 每張 Card 旁：放一顆 Delete 按鈕，移除該筆資料

[Constraints]
- 禁用任何會 mutate 原陣列的方法（push / splice / pop / shift / sort / reverse）
- 必須透過 setNames 傳入新陣列
- Add 的 onClick handler 命名為 handleAdd；Delete 的命名為 handleDelete

[Steps]
1. 在元件內新增 handleAdd = () => setNames([...names, 'new element'])
2. 在元件內新增 handleDelete = (target: string) => setNames(names.filter(n => n !== target))
3. 在現有的 flex 容器中加一顆 Add 按鈕，onClick={handleAdd}
4. 在每張 Card 內（或旁邊）加一顆 Delete 按鈕，onClick={() => handleDelete(name)}

[Verification]
- 點 Add 三次：UI 依序多出三張 'new element' Card（會觸發 key 重複警告 → 進入 Stage 3 修正）
- 點任一 Delete：該張 Card 消失，其他不動
- 在 handleAdd 內加 console.log(names === newArray)，確認 false（是新陣列）
```

#### Stage 3：Verify — 用邊界條件驗證 key 的正確性

```
[Context]
檔案：app/page.tsx
目前狀況：Stage 2 的 Add 會造成 key 重複警告，因為 'new element' 會重名

[Goal]
把 names 的元素結構改成物件 { id, name }，用穩定 id 當 key，並親眼證明「用 index 當 key」在變動列表中會出 bug。

[Constraints]
- id 用 crypto.randomUUID() 產生（Next.js 環境支援）
- 不可用 Math.random()、Date.now() 作為唯一鍵的替代
- 為了示範 bug，Card 內要包一個 <input /> 讓 user 輸入文字

[Steps]
1. 把 names 型別改成 { id: string, name: string }[]
2. 初始值：三筆資料各給一個 uuid
3. handleAdd 改為 setNames([...names, { id: crypto.randomUUID(), name: 'new element' }])
4. 在 Card 內塞一個 <input defaultValue={name} />
5. 分別測試兩種 key 設定：
   - 實驗 A：key={index}
   - 實驗 B：key={item.id}

[Verification]
- 在多張 Card 的 input 各輸入不同文字
- 刪掉中間那張
- 實驗 A：觀察剩餘 input 的文字是否「錯位」到錯的 Card（證明 index 當 key 的 bug）
- 實驗 B：文字依然跟著原本的 Card（證明穩定 id 正確）
- 用一句話總結兩者差異
```

### 四、錯誤恢復提示詞（當 AI 產出不符預期時）

不要重打整段需求。用**最小修正**提示詞引導：

```
剛才的程式碼有以下問題：
1. [具體描述問題，引用行號]
2. [預期行為 vs 實際行為]

請只修改相關部分，其他保持不變。修改後列出 diff。
```

常見情境範例：

| 問題 | 修正提示 |
| --- | --- |
| 用了 `push` | `第 N 行用了 names.push()，改用 setNames([...names, item])` |
| key 用了 index | `把 key={index} 改成 key={item.id}，並解釋差異` |
| 直接賦值狀態 | `names = [...] 無效，必須用 setNames，請改寫` |
| 型別錯誤 | `TypeScript 錯誤：xxx，請修正型別定義而不是用 any` |

### 五、驗證檢查點清單（每階段結束必過）

每完成一個階段，用這份清單自我驗證再進入下一階段：

- [ ] **渲染正確**：頁面視覺與預期一致，無 React warning
- [ ] **key 合規**：打開 DevTools console 無 `Each child in a list should have a unique "key" prop` 警告
- [ ] **不可變性**：狀態更新都建立新陣列/物件，未使用 mutate 方法
- [ ] **型別一致**：TypeScript 無紅線，型別明確不用 `any`
- [ ] **互動可逆**：新增後可以刪除、切換後可以切回，狀態不殘留
- [ ] **邊界行為**：空陣列、單筆、大量資料都能正常渲染

### 六、通用提示詞模板（可複製貼上）

```
[Context]
檔案：<path>
目前狀況：<元件現在怎麼寫、用了哪些 state/props>

[Goal]
<一句話描述要完成的功能>

[Constraints]
- <不能動的檔案或 API>
- <必須遵守的規範，例如不可變更新>
- <命名或風格約束>

[Steps]
1. <步驟 1>
2. <步驟 2>
3. <步驟 3>

[Verification]
- <使用者視覺驗證>
- <console/devtools 驗證>
- <TypeScript/Lint 驗證>
```
