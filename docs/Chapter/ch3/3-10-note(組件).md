---
title: 3-9 元件拆分與模組匯入
date: 2026-04-18
tags: [react, next.js, component, import, alias]
---

# 3-9 元件拆分與模組匯入

## 核心內容

- **一元件一檔案**是 React / Next.js 的標準慣例，便於維護與重用。
- 全域共用的 UI 元件放在 `src/components/` 目錄下。
- 元件要能被其他模組使用，必須加上 `export default`；否則只存在於該檔案內部。
- 匯入元件有兩種寫法：相對路徑與路徑別名（alias）。

### 相對路徑 vs. `@` 別名

| 寫法 | 範例 |
|------|------|
| 相對路徑 | `import Card from '../../components/card'` |
| `@` 別名 | `import Card from '@/components/card'` |

在本專案中，`tsconfig.json` 將 `@` 對應到 `./src/`，因此：

```ts
// tsconfig.json
"paths": {
  "@/*": ["./src/*"]
}
```

`@/components/card` 實際解析為 `src/components/card`。  
目錄越深時，`@` 別名能省去計算相對層數的麻煩。

## 開發上可採取的行動步驟

1. 在 `src/components/` 建立元件檔，每個元件獨立一個 `.tsx` 檔。
2. 元件函式定義後加上 `export default ComponentName`。
3. 在使用端以 `import ComponentName from '@/components/component-name'` 匯入；不需附副檔名。
4. 不確定別名對應路徑時，查看 `tsconfig.json` 的 `paths` 設定。

## 我可以立刻採取的實作清單

- [ ] 將目前 `app/page.tsx` 中的 inline 元件抽出到 `src/components/` 目錄
- [ ] 確認新檔案有 `export default`
- [ ] 在 `page.tsx` 改用 `@/components/...` 路徑匯入
- [ ] 儲存後確認 Next.js dev server 無報錯

## 總結

元件拆分的關鍵只有兩個動作：**export**（讓外部可見）與 **import**（在使用端引入）。路徑別名 `@` 讓匯入路徑保持一致，不受目錄深度影響，是中大型專案的實用習慣。
