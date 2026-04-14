# 2-2 建立全新的 Next.js 專案

## 核心內容

重點：**建立 Next.js 專案時，優先依照官方文件操作**。
官方文件不只提供最新安裝方式，也能避免照著過期教學做出錯誤設定。

流程：

1. 先確認系統需求，至少要有可用的 Node.js 環境。
2. 到 Next.js 官方文件的安裝頁面，直接使用推薦方式建立專案。
3. 推薦透過 `create-next-app` 建立新專案，因為它會自動幫你完成基礎設定。
4. 理解 `npm` 與 `npx` 的差別：
   - `npm`：安裝套件
   - `npx`：直接執行一次性 CLI 工具，不需要手動全域安裝
5. 建立專案時，會依序回答一些初始化問題，例如：
   - 是否使用 TypeScript
   - 是否使用 ESLint
   - 是否使用 Tailwind CSS
   - 是否使用 `src/` 目錄
   - 是否使用 App Router
   - 是否自訂 import alias

背後傳達的核心概念：**不要只會把專案生出來，還要知道每個初始化選項在做什麼。**

## 開發上可採取的行動步驟

### 1. 先養成「先看官方文件」的習慣

每次開始新技術或新專案前，先確認：

- 官方安裝方式
- 系統需求
- 推薦專案結構
- 目前官方推薦的 routing / styling / linting 方案

對 Next.js 來說，建立專案前至少要先看：

- Installation
- Create Next App
- Routing
- Project Structure

### 2. 在本機建立專案前先檢查環境

實際可執行：

```bash
node -v
npm -v
npx -v
```

檢查重點：

- Node.js 版本是否符合 Next.js 需求
- `npm` / `npx` 是否可正常使用

### 3. 用官方推薦方式建立新專案

可直接使用：

```bash
npx create-next-app@latest my-app
```

這樣做的好處：

- 使用官方維護的初始化流程
- 省去手動安裝與設定
- 能直接拿到較合理的預設值

### 4. 初始化專案時，不要無腦按 Enter

建立專案時，每個選項都應該有意識地決定：

- `TypeScript`
  - 若是正式專案，通常建議開啟
  - 若是教學練習或剛入門，可先不用
- `ESLint`
  - 建議開啟，能提早發現問題
- `Tailwind CSS`
  - 若你預期會快速建 UI，建議開啟
- `src/ directory`
  - 純屬結構偏好，重點是團隊一致
- `App Router`
  - 新版 Next.js 開發通常應優先採用
- `import alias`
  - 專案大一點時很好用，但先用預設也可以

### 5. 為自己建立一份「新專案預設模板決策」

你可以固定一套自己的初始化標準，例如：

- 預設使用 TypeScript
- 預設開 ESLint
- 預設開 Tailwind CSS
- 預設使用 App Router
- `src/` 是否使用，固定成同一種風格
- alias 固定使用 `@/*`

這能降低每次開新專案時的決策成本，也讓專案風格更一致。

### 6. 把 CLI 工具分清楚

開發上至少要記住：

- `npm install <package>`：把套件裝進專案
- `npx <tool>`：執行一次性工具

實務上你會常見：

```bash
npx create-next-app@latest my-app
```

這代表你只是借用這個工具來建立專案，不是把它永久裝在系統上。

## 我可以立刻採取的實作清單

- 建立新 Next.js 專案前，先打開官方文件確認最新版流程
- 在終端機先檢查 `node`、`npm`、`npx` 版本
- 用 `npx create-next-app@latest` 建立專案
- 對每個初始化選項做明確決定，不要全部用預設
- 為自己的專案整理一份固定初始化規格
- 之後每次新專案都沿用同一套規則

## 可直接使用的提示詞

直接這樣問：

### 1. 環境檢查

```text
請根據 Next.js 官方文件，告訴我建立新專案前需要先檢查哪些環境條件。
```

### 2. 理解 npm 與 npx

```text
請用初學者能懂的方式說明 npm 與 npx 的差別，並舉 Next.js 建專案的例子。
```

### 3. 理解 create-next-app 初始化選項

```text
我準備用 create-next-app 建立 Next.js 專案，請逐一說明 TypeScript、ESLint、Tailwind CSS、src directory、App Router、import alias 這些選項的用途與適合的選擇。
```

### 4. 推薦一組初始化設定

```text
如果我是做練習專案，請幫我推薦一組 create-next-app 的初始化選項，並說明原因。
```

### 5. 整理成可執行步驟

```text
請把建立一個新的 Next.js 專案的流程，整理成我可以直接照做的終端機步驟。
```

### 6. 驗證是否安裝成功

```text
我已經建立完 Next.js 專案，請告訴我如何驗證它是否成功安裝並能正常啟動。
```

### 7. 一次問完整套內容

```text
請根據 Next.js 官方文件，幫我完成「建立全新的 Next.js 專案」這個學習目標。
請用初學者角度整理：
1. 建立前要先檢查哪些環境
2. npm 與 npx 的差別
3. create-next-app 各個初始化選項的用途
4. 練習專案建議怎麼選
5. 完整操作步驟
6. 如何確認專案建立成功
```

## 依官方文件在目前目錄初始化 Next.js 專案

如果我目前已經在想要當成專案根目錄的資料夾中，也可以直接用 `.` 當成專案名稱，也就是把「目前目錄」直接初始化成 Next.js 專案。

以這次需求為例：

- TypeScript：`yes`
- ESLint：`yes`
- Tailwind CSS：`yes`
- `src/` directory：`yes`
- App Router：`yes`
- import alias：`yes`
- alias：`@/*`

可直接使用：

```bash
npx create-next-app@latest . \
  --ts \
  --eslint \
  --tailwind \
  --src-dir \
  --app \
  --turbopack \
  --import-alias "@/*" \
  --use-npm
```

### 為什麼可以用 `.`

因為 `.` 代表目前目錄，所以這條指令的意思是：

- 不新建一個額外的資料夾
- 直接把目前所在目錄當成 Next.js 專案根目錄

### 互動式做法

如果不用完整參數，也可以輸入：

```bash
npx create-next-app@latest .
```

然後依序選：

- `TypeScript`: `Yes`
- `Which linter`: `ESLint`
- `React Compiler`: `No` 或依需求決定
- `Tailwind CSS`: `Yes`
- `src/ directory`: `Yes`
- `App Router`: `Yes`
- `customize import alias`: `Yes`
- alias: `@/*`

### 注意事項

- 不建議這次直接用 `--yes`，因為 `--yes` 會套用預設值或已保存偏好；雖然官方文件提到預設會開啟 TypeScript、Tailwind CSS、ESLint、App Router、import alias，但不適合拿來精準控制這次每個選項。

### 對應提示詞

```text
請根據 Next.js 官方文件，告訴我如何在「目前目錄」初始化一個新的 Next.js 專案，並使用以下設定：
- TypeScript: yes
- ESLint: yes
- Tailwind CSS: yes
- src directory: yes
- App Router: yes
- import alias: @/*

請給我：
1. 可直接執行的 create-next-app 指令
2. 每個選項對應的 CLI 參數
3. 如果用互動式安裝，應該怎麼回答每個 prompt
4. 初始化後如何啟動並驗證專案成功
```

也可以用短版：

```text
請用 Next.js 官方文件的最新做法，幫我生成一條在目前目錄初始化 Next.js 專案的指令，需求是 ts/eslint/tailwind/src/app router/import alias 全開，alias 用 @/*，套件管理器用 npm。
```
