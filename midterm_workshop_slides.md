# 期中工作坊｜AI × 資料工程顧問團挑戰賽 — 簡報

> **活動名稱**：期中工作坊 — AI × 資料工程顧問團挑戰賽
> **講師**：Dex（專題老師）
> **時間**：學期過半實體日（約 3h45m）
> **視覺風格**：科技感、藍紫色系（仿 `de-career-presentation-v3.html`）
> **總張數**：31 張
> **來源**：`workshop_proposal.md`

---

## Slide 1 — 封面

### AI × 資料工程顧問團
### 挑戰賽

| 項目 | 內容 |
|---|---|
| 副標 | 從紙筆架構 → 真的跑得起來的 pipeline |
| 時長 | 半天（約 3h45m） |
| 規模 | 13 人 × 同組智囊團 |
| 講師 | Dex |
| 形式 | 個人實作 + 同組討論 + 上台 Demo |

> 期初你畫了流程圖，今天**把它變成真的 pipeline**。

---

## Slide 2 — Agenda

| Part | 主題 |
|---|---|
| **1** | 為什麼有這場工作坊（脈絡 + 定位） |
| **2** | 議程總覽（半天時間表） |
| **3** | 四大關卡（MVP Scope → ETL → LLM 加值 → MVP 打包） |
| **4** | 個人 MVP 原型規格 |
| **5** | 與 TibaMe 課程的銜接 |
| **6** | 預期成果 + Q&A |

> 今天結束你會帶走一個**可升級的個人 LLM x DE MVP 原型**，EP01 會再整理成正式工程專案。

---

## Slide 3 — Part ① 為什麼有這場工作坊

### 脈絡：從期初到期中

```
期初工作坊（紙筆畫流程）
    ↓
期中工作坊（個人實作粗版 MVP）  ← 你在這
    ↓
EP01（回顧 MVP、拆成 ETL、規劃升級）
    ↓
期末團專（團隊交付完整系統）
```

### 動機

- 期初畫的流程圖**該動手實作了**
- 學了 Python / SQL / pandas，需要一場**整合演練**
- 體驗 **AI/LLM 在真實 pipeline 中怎麼用**

> 這是「把學的東西串起來」的關鍵節點。

---

## Slide 4 — 從期初到期中的升級邏輯

### 同一個流程，三層深度

```
期初：紙筆畫流程     →  概念理解（誰做什麼）
期中：個人寫程式     →  動手實作（用程式碼跑出來）  ← 你在這
EP01：工程化整理     →  ETL mapping + 升級計畫
期末：團隊整合系統   →  完整交付（含部署 + Demo）
```

### 每階段都會：
- 處理同樣 5 個環節：資料來源 → 截取 → 儲存 → 轉換 → 應用
- **能力疊加**：紙筆 → Notebook / script MVP → EP01 工程化整理 → Docker / Airflow / 雲端部署
- **視角擴大**：個人 → 隊友 → 客戶

> 期中是中繼站，**不是終點**。

---

## Slide 5 — 活動定位：引導式挑戰賽

### 什麼是「引導式挑戰賽」？

> **工作坊骨架 × 黑客松調味**
>
> 不是純黑客松（沒方向亂寫），也不是純工作坊（照本宣科）。

| 工作坊味道 | 黑客松味道 |
|---|---|
| 有 Starter Code 模板 | 你決定情境怎麼解 |
| 有時間引導 | 有 Demo 上台 |
| 有講師主控 | 有同儕競合 |

> **每個人都會跑完整條 pipeline**，作品都是自己的。

---

## Slide 6 — 執行模式：個人實作、團隊智囊

```
討論層：同組互相 debug、交流 prompt 技巧
         │
實作層：每人獨立跑完完整 4 關 pipeline
         │
成果層：每人帶走自己的 LLM x DE MVP 原型與升級素材
```

### 三條原則

- **每人都做完整 4 關卡**（不是分工拆開）
- **同組同情境 → 討論有共同語言**（不是 6 人組各做各的）
- **卡關時問組員比問 TA 快** → 自然 peer learning

> 不會出現英雄組長 + 路人組員。**你的作品就是你的**。

---

## Slide 7 — 期初 vs 期中升級對比

| 維度 | 期初（95 min） | 期中（3.5 hr） |
|---|---|---|
| 執行單位 | 組 | **個人**（組內互助） |
| 產出 | 一張流程圖 | **可跑 MVP 原型** |
| 動手程度 | 畫圖 + 討論 | **寫 code + 跑 AI + 接 Dashboard** |
| 帶走什麼 | 概念理解 | **可持續升級的 MVP 種子** |
| 團隊價值 | 分工協作 | **同儕學習 + 解題互助** |

> 從紙筆到程式，從共識到作品。

---

## Slide 8 — 設計原則 4 條

| # | 原則 | 說明 |
|---|---|---|
| 1 | **低門檻、高天花板** | Starter Code 降低起步難度；Dashboard 部署讓強者不無聊 |
| 2 | **傳統 vs AI 對比** | 每關都有「手動做法」和「AI 做法」，切身感受效率差異 |
| 3 | **做不完沒關係** | 帶走的模板與輸出都在，EP01 會回來整理 |
| 4 | **成果可延伸** | 工作坊產出先對接 EP01，再對接 GitHub / Docker / Airflow / GCP |

### MVP 版本階梯

| 版本 | 工作坊狀態 | 後續升級 |
|---|---|---|
| v0 | Notebook 跑完 ETL + LLM | 拆成 `.py` |
| v1 | 本地資料夾 / starter repo | EP01 後整理成 GitHub + README |
| v2 | `run_pipeline.py` / Streamlit | 補測試與設定 |
| v3+ | Docker / Airflow / GCP | 後續課程升級 |

> 設計核心：**沒人會被卡死、沒人會無聊**。

---

## Slide 9 — 設計原則展開：AI vs 傳統對比

### 每一關都會體驗「兩種做法」

| 關卡 | 傳統做法 | AI 做法 |
|---|---|---|
| 需求拆解 | 自己想破頭 | **ChatGPT 扮演客戶**幫你釐清 |
| 資料清洗 | 手寫 pandas | **AI 生成 pandas 語法**加速 |
| 進階分析 | 自己跑模型 | **LLM API 直接做情緒分析** |
| 整合交付 | 手寫 README | **AI 生成 README + 摘要** |

> **AI 不是替代你，是讓你做更多**。

---

## Slide 10 — 設計原則展開：低門檻、高天花板 + 做不完沒關係

### 低門檻
- 可用 Google Colab 起步，也可用本地資料夾或講師 starter template
- Starter Code 模板（步驟提示 + helper 函式）
- 共用 LLM API Key（學員不用自己申請）

### 高天花板
- Streamlit Dashboard 模板（強者可上線部署）
- Docker 模板（加分，不要求當場理解完整原理）
- 自選路線（Demo / Dashboard / Docker 模板）
- AI 進階用法（多輪對話、自訂 prompt）

### 做不完沒關係
- 模板、輸出結果、demo 素材都會保留下來
- EP01 會回收並整理成正式工程化路線
- 後續課程會回來升級這個專案

---

## Slide 11 — 學習目標 4 條

工作坊結束時，你應該能：

| # | 能力 |
|---|---|
| 1 | **說明 AI/LLM 在資料工程 pipeline 中的 3-5 個具體應用場景**<br>（需求釐清、非結構化資料清洗、自動分類、Text-to-SQL、報告生成） |
| 2 | **獨立完成一個 mini data pipeline**<br>（資料取得 → 清洗轉換 → AI 加值分析 → 成果展示） |
| 3 | **帶走一份可展示的個人 MVP 原型**<br>（程式碼或 Notebook、分析結果、Dashboard 模板、升級計畫草稿） |
| 4 | **體驗「用 AI 當工作夥伴」的協作模式**<br>（用 prompt 追問需求、生成程式碼、解讀分析結果） |

---

## Slide 12 — Part ② 議程總覽（半天時間表）

| 時間 | 內容 |
|---|---|
| 00:00-00:20 | 開場 + 趨勢講座 + 環境檢查 |
| 00:20-00:45 | **關卡 1：MVP Scope（25 min）** |
| 00:45-01:25 | **關卡 2：建立可跑 ETL（40 min）** |
| 01:25-01:35 | 休息 + 組內互動 |
| 01:35-02:15 | **關卡 3：AI 加值分析（40 min）** |
| 02:15-02:40 | **關卡 4：整合交付（25 min）** |
| 02:40-03:20 | Demo 環節（每組代表上台） |
| 03:20-03:45 | 總結 + 引導打包 + Q&A |

> **總計約 3h45m**。每關都有時間提示，超時自動切到下關。

---

## Slide 13 — 情境題庫（8 選 5，與期初共用）

| # | 情境 | 角色 | AI 切入點 | 難度 |
|---|---|---|---|---|
| 1 | 餐飲 POS 庫存優化 | 餐飲集團資料顧問 | LLM 分析非結構化評論 → 結構化標籤 | ★★ |
| 2 | B2C 電商競品比價 | 電商營運資料顧問 | LLM 自動生成競品分析摘要 | ★★ |
| 3 | 數位金融客訴效率 | 金融業資料顧問 | LLM 情緒分析 + 自動分類 + 優先排序 | ★★ |
| 4 | 音樂串流（Spotify） | 娛樂產業資料顧問 | LLM 生成聽眾洞察與推薦摘要 | ★★ |
| 5 | 叫車服務交通熱點 | 交通服務資料顧問 | LLM 生成交通模式洞察 | ★★★ |
| 6 | 求職媒合洞察 | 人資科技資料顧問 | LLM 履歷職缺匹配 + 摘要 | ★★ |
| 7 | 媒體業新聞輿情即時監測 | 媒體業資料顧問 | LLM 新聞摘要 + 情緒追蹤 | ★★★ |
| 8 | 不動產房價趨勢分析 | 不動產資料顧問 | LLM 生成區域分析建議書 | ★★ |

> **抽籤分配 5 個情境**，每組同情境同題目。**池子完整三層流程設計（業務 / 課程 / 進階）見 `course_project_guide.md` §5.4 工作坊情境題庫**（與期初共用同一池）。

---

## Slide 14 — Part ③ 四大關卡 概覽

```
關卡 1: MVP Scope（25 min）
    ↓ 從期初需求收斂成今天做得完的最小功能
關卡 2: 建立可跑 ETL（40 min）
    ↓ extract / transform / load，先用 CSV 或 SQLite
關卡 3: LLM 加值分析（40 min）
    ↓ llm_analyze.py：分類 / 摘要 / 洞察 / 報告
關卡 4: MVP 打包（25 min · 自選路線）
    ↓ README 草稿 / Streamlit / demo 素材 / Docker 模板 / upgrade_plan
```

> 每關都有 **Starter Code + 提示卡 + 講師示範**，跟著做就能完成。

---

## Slide 15 — 關卡 1：MVP Scope（25 min）

### 工具
**ChatGPT / Claude 網頁版**（不寫程式）

### 做法
- 拿出期初活動的流程圖與 5 個必答問題
- 用 prompt 讓 AI 扮演**虛擬客戶**，協助你收斂需求
- 追問清單：今天只做哪個功能？資料在哪？成功指標是什麼？最小輸出是什麼？

### 產出
- `docs/requirements_spec.md`（含資料來源、預期產出、關鍵指標、MVP scope）

### AI 學習點
> AI 不只能寫 code，**還能模擬角色幫你釐清思路**。

---

## Slide 16 — 關卡 2：建立可跑 ETL（40 min）

### 工具
**Google Colab / VS Code + pandas + SQL**

### 用到的已學技能
`pd.read_csv()`、pandas 清洗轉換、SQL 查詢

### 做法
- 使用 Starter Code 取得資料、清洗、輸出
- 資料來源：講師預備好的 CSV/JSON（模擬從系統匯出的原始資料）
- 部分情境搭配 SQL 查詢練習（從 SQLite 撈取）
- **遇到卡關時用 ChatGPT/Claude 生成 pandas / SQL 語句**

### 產出
- `src/extract.py` / `src/transform.py` / `src/load.py`
- `data/processed/` 裡的清洗後資料

### AI 學習點
> 用 AI 生成 SQL 查詢、加速 pandas 問題排除。

---

## Slide 17 — 關卡 3：AI 加值分析（40 min）

### 工具
**Google Colab + LLM API**（OpenAI / Anthropic）

### 用到的已學技能
**FastAPI 概念**（理解 API 呼叫邏輯）、Python 函式呼叫

### 做法
- 用封裝好的 `llm_helper.py` 呼叫 LLM API
- 因為學過 FastAPI，串接 LLM API 是**自然延伸**（送 request → 收 response）
- 情緒分析 / 自動分類 / 摘要生成 / 異常偵測（依情境不同）
- 體驗「**從聊天升級到自動化**」

### 產出
- `src/llm_analyze.py`
- AI 加值後的分析結果（新欄位、分類標籤、洞察摘要）
- `output/report.md`

### AI 學習點
> 「**程式 × AI API**」的串接體驗（FastAPI 概念的實戰應用）。

---

## Slide 18 — 關卡 4：MVP 打包（25 min · 自選路線）

依進度和興趣選擇展示方式：

| 路線 | 適合誰 | 做什麼 | 完成度 |
|---|---|---|---|
| **A. Demo 簡報** | 時間緊 / 偏分析思維 | 整理成果截圖 + 口頭展示 pipeline | 工作坊內完成 |
| **B. Streamlit Dashboard** | 有餘裕 / 想挑戰 | 將資料接上預製 Dashboard 模板 | 工作坊內或課後完成 |
| **C. Docker 模板啟動** | 想先看工程化長相 | 用講師模板嘗試 `docker compose up` | 加分，只體驗 |
| **D. 全部都做** | 強者 | Dashboard + Docker + 上台 Demo | 高天花板挑戰 |

### 工具
Streamlit 模板（講師預先製作，學員只需接入自己的資料）

### AI 學習點
> 用 AI 快速生成 README、展示摘要。

### 必補文件
`docs/upgrade_plan.md`：寫下後續如何升級成 Docker / Airflow / GCP 版本。

---

## Slide 19 — AI 整合策略（橫跨四關）

```
關卡 1: ChatGPT/Claude 網頁版    →  概念與構想（虛擬客戶對話）
關卡 2: ChatGPT 輔助 + Colab/VS Code →  生成 pandas / SQL，debug 用
關卡 3: Colab/VS Code + LLM API      →  程式化呼叫（情緒分析 / 分類 / 摘要）
關卡 4: AI 生成 README / 摘要        →  MVP 打包加速
```

### 核心理念

- **概念用網頁版**（聊天式釐清）
- **實作用 API**（程式化批次處理）
- 把「**用 AI debug**」當作必修技能練起來

> AI 不是輔助，是**第二個大腦**。

---

## Slide 20 — Starter Code 結構（Notebook + Repo 模板）

```python
# === 關卡 1：MVP Scope ===
# （此段在 ChatGPT/Claude 網頁版完成）
# TODO: 貼上你的需求規格書摘要

# === 關卡 2：建立可跑 ETL ===
# Step 1: 取得資料
df = pd.read_csv('data/raw/source.csv')
# Step 2: 資料清洗
# TODO: 處理缺漏值
# TODO: 轉換資料型別
# TODO: 基礎統計摘要

# === 關卡 3：LLM 加值分析 ===
# Step 3: 用 LLM 分析資料
# TODO: 設計你的 prompt
# TODO: 對資料做 AI 加值分析（情緒/分類/摘要）

# === 關卡 4：MVP 打包 ===
# 路線 A: 截圖 + 口頭 Demo
# 路線 B: 接上 Streamlit Dashboard（見 app.py）
# 路線 C: 用 Docker 模板啟動
```

> **TODO 清單就是你的任務**。Starter Code 不是答案，是地圖。

---

## Slide 21 — Helper 函式設計（讓你少寫 boilerplate）

### 講師預備好的 helper 函式

| 函式 | 功能 |
|---|---|
| `load_data(scenario)` | 載入該情境的原始資料 |
| `clean_basic(df)` | 通用基礎清洗（缺漏 / 型別） |
| `llm_call(prompt, text)` | 一行呼叫 LLM API（含 retry） |
| `batch_analyze(df, col, prompt)` | 對某欄位批次跑 LLM 分析 |
| `save_output(df, name)` | 存到 `data/processed/` |

### 設計原則
- **學員專注業務邏輯**，不被 boilerplate 綁住
- **可改寫**：你想自己重寫也可以，helper 只是起點

> 不是給你抄答案，是讓你**有更多時間思考、更少時間 debug**。

---

## Slide 22 — Part ④ 個人 MVP 原型規格

### 工作坊結束時每人帶走的 starter 結構

```
llm-de-mvp/
├── README.md                    ← AI 協助生成的專案說明草稿
├── requirements.txt             ← 套件依賴
├── .env.example                 ← API Key 範例，不放真實 key
├── Dockerfile                   ← 加分項 / 講師模板提供，後續 Docker 課再細教
├── docker-compose.yml           ← 加分項 / 講師模板提供，後續 Docker 課再細教
├── src/
│   ├── extract.py               ← 資料取得
│   ├── transform.py             ← 資料清洗
│   ├── load.py                  ← 資料輸出 / 入庫
│   ├── llm_analyze.py           ← LLM 加值分析
│   └── run_pipeline.py          ← 一鍵跑完整流程
├── notebooks/
│   └── pipeline.ipynb           ← 個人完整 Notebook（關卡 1-3）
├── data/
│   ├── raw/                     ← 原始資料
│   └── processed/               ← 清洗後資料
├── app.py                       ← Streamlit Dashboard 模板
└── docs/
    ├── requirements_spec.md     ← 關卡 1 產出的需求規格書
    ├── pipeline.mmd             ← 期初流程圖升級版，EP01 再正式整理
    ├── data_source.md           ← 資料來源說明
    ├── tech_decision.md         ← 工具選型理由
    └── upgrade_plan.md          ← Docker / Airflow / GCP 升級計畫
```

> 今天先求能跑、能展示、能討論。EP01 會把它整理成真正的工程專案。

---

## Slide 23 — 工作坊結束時每人帶走什麼

| 成果 | 說明 |
|---|---|
| **需求規格書** | 個人產出的客戶需求分析文件（關卡 1） |
| **完整 Pipeline** | Notebook 或 `.py` script，包含 ETL + AI 加值（關卡 2-3） |
| **Dashboard 模板** | 可接入資料即時展示的 Streamlit App（關卡 4） |
| **Starter 專案資料夾** | 整合以上所有產出的專案資料夾，可之後上傳 GitHub |
| **升級計畫** | 後續 Docker / Airflow / GCP 要怎麼改 |
| **EP01 回收素材** | `mvp_review.md`、`etl_mapping.md`、`mvp_upgrade_plan.md` 的內容來源 |

### 衡量指標（內部目標）
- 關卡 1-3 完成率 ≥ 80%
- Dashboard 接入率 ≥ 40%
- AI 工具使用率 = 100%（每人都至少體驗過 ChatGPT + LLM API）

---

## Slide 24 — 引導打包流程（10 min · 包含在總結環節）

### 三步驟，講師現場帶你做

| Step | 動作 |
|---|---|
| 1 | 將 Colab Notebook **下載 / 存到 Google Drive** |
| 2 | 下載或複製提供的 **starter 專案模板** |
| 3 | 套用 **README 草稿 + EP01 回收清單 + LinkedIn 貼文模板** |

> 今天先讓作品素材收好。GitHub 與正式 repo 整理會在 EP01 之後繼續補。

---

## Slide 25 — Demo 環節設計

### 展示形式
- **每組代表 1-2 人上台**（依時間調整）
- 每組 5-7 分鐘（含問答）
- 同情境的組互相比較解法

### 評分項目（內部評估，不公開排名）
| 項目 | 重點 |
|---|---|
| 技術完整性 | 4 關卡是否都跑完 |
| AI 整合品質 | prompt 設計、結果解讀 |
| 作品打包 | README 草稿、輸出結果、升級素材 |
| 報告表達 | 從用戶問題切入、邏輯清晰 |

---

## Slide 26 — 評分標準（內部評估）

| 評分項目 | 配比 | 評分標準 |
|---|---|---|
| **技術實現** | 50% | 4 關卡完成度、技術選擇合理性、Code 品質 |
| **AI 整合創意** | 25% | Prompt 設計、AI 應用情境的創意 |
| **作品打包** | 15% | README 草稿、輸出結果、文件完整度 |
| **展示表達** | 10% | 報告邏輯、問答應對 |

> 評分**不公開排名**。重點是**自己有沒有完成**。

---

## Slide 27 — 獎項建議

| 獎項 | 規則 |
|---|---|
| **完成獎** | 完成 4 關卡 + 可展示輸出 |
| **AI 整合獎** | Prompt 設計最有創意 |
| **打包獎** | README 草稿 / 升級計畫最清晰 |
| **同儕推薦獎** | 組內互推（最會互助的那位） |

> 重點不是贏別人，是**證明自己有做完**。

---

## Slide 28 — Part ⑤ 與 TibaMe 課程的銜接：運用已學技能

### 工作坊運用已學技能

| 工作坊環節 | 對應已學課程模組 |
|---|---|
| 關卡 2：pandas 資料清洗 | Python / pandas 基礎 |
| 關卡 2：SQL 查詢載入資料 | SQL 與資料庫 |
| 關卡 3：呼叫 LLM API | API request/response 概念體驗 |
| 關卡 1-4：完整 MVP pipeline | 基礎 ETL 流程 |
| 關卡 4：Docker 模板啟動 | 後續 Docker 課程預告 |

### 為什麼這場工作坊放在學期過半？

```
學完 Python / pandas → 可以用了
學完 SQL → 可以查資料了
理解 API request/response → 可以體驗 LLM API 了
                ↓
            三件事「串起來」= mini data pipeline
                ↓
            加上 AI 加值 = 期中工作坊
```

> 今天會碰到一些後續工具的影子，但不要求當場精通。目標是先把點連成線。

---

## Slide 29 — 升級路徑：期中 → 期末 + 課後延伸

### 工作坊作品的持續升級路徑

```
期初                 期中（工作坊）                  EP01 與後續課程模組
──────────────────────────────────────────────────
紙筆流程圖        →   Notebook / script 手動執行    →   EP01 ETL mapping → Docker 容器化
需求草稿          →   Streamlit 本地 Dashboard      →   README / GitHub → docker-compose 部署
資料來源想像      →   CSV / SQLite                 →   MySQL / BigQuery
工具選型討論      →   手動觸發 pipeline            →   Airflow 排程自動化
團隊情境          →   個人 MVP 原型                →   GCP 雲端部署
```

### 課後 1 週的行動

- **EP01**：回顧 MVP、拆成 ETL、補升級計畫
- **GitHub 課程後**：上傳 GitHub（附教學文件，講師會給模板）
- **學 Docker / Airflow / GCP**：每學一個新技術就回來升級這個專案
- **結業專題**：擴充為完整作品集

> 最終放進履歷的不是練習題，而是一個**歷經多次迭代的完整作品**。**不要做完就丟**。

---

## Slide 30 — Part ⑥ 預期成果：4 件個人產出 + 對你的意義

### 你會帶走的 4 件具體產出

| 產出 | 用途 |
|---|---|
| **需求規格書** | 證明你能把模糊需求拆成具體任務 |
| **Pipeline MVP** | 證明你能跑完 ETL + AI 加值 |
| **Dashboard 模板** | 證明你能交付給客戶看的東西 |
| **升級計畫** | 證明你知道作品如何繼續工程化 |

### 4 個能力證據

```
「需求拆解能力」 + 「ETL 實作能力」 + 「AI 整合能力」 + 「作品升級能力」
                                   ↓
                          這就是 DE 履歷上要寫的東西
```

### 對團隊的意義

同情境同學變成你的**期末隊友**；互相 debug 累積的**默契與共同語言**；能對照不同解法**反思自己的選擇**。

---

## Slide 31 — 結尾 + Q&A

### 我們的目標

> **不是讓你「學完工作坊」，而是讓你「帶走一個能用的作品」。**

### 三個提醒

- **保留今天的輸出與專案資料夾**（EP01 會用到）
- **GitHub 會在後續正式整理**（不要今天卡在工具安裝）
- **後續課程會回來升級這個專案**（不要做完就丟）
- **同情境的組員是期末隊友**（保持聯絡）

### 完整內容指引

- 工作坊企劃書：`workshop_proposal.md`
- MVP 整合藍圖：`LLM_DE_MVP_INTEGRATION_PLAN.md`
- 學期專題機制總覽：`course_project_guide.md`

> **歡迎進入學期下半場。**
> ── Q&A ──
