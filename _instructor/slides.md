# LLM × DE MVP Builder 實戰營 — 簡報

> **活動名稱**：LLM × DE MVP Builder 實戰營
> **講師**：Dex（專題老師）
> **時間**：10:00-16:00（有效 4.5 小時）
> **規模**：13 人 × 3 組智囊團
> **總張數**：25 張
> **投影時機**：對照講師手冊 `facilitator_guide.md` 的時間表

---

## Slide 1 — 封面

### LLM × DE
### MVP Builder 實戰營

| 項目 | 內容 |
|---|---|
| 副標 | 上次你畫了流程圖，今天把它做出來 |
| 時長 | 10:00-16:00（半天） |
| 規模 | 13 人 × 3 組智囊團 |
| 講師 | Dex |
| 形式 | 個人實作 + 組內互助 + 閃電秀 Demo |

> 每人選一個題目，做出一條 **Mini Data Pipeline**，帶走一個作品。

---

## Slide 2 — 今日目標

### 你今天要完成的一條線

```
CSV → pandas 清洗 → SQLite (raw/cleaned/analyzed) → SQL 查詢 → LLM 分析 → 報告
         ↓                    ↓                         ↓              ↓
      Transform            Load                      Query          AI 加值
```

### 帶走什麼

| 產出 | 說明 |
|------|------|
| **pipeline.db** | SQLite 資料庫（含 raw / cleaned / analyzed 三張表） |
| **processed/*.csv** | SQL 統計結果 |
| **output/report.md** | LLM 分析的顧問報告 |
| **GitHub Repo** | 後續課程持續升級的作品集 |

> 這不是練習題，是**放進履歷的第一條 Data Pipeline**。

---

## Slide 3 — 從期初到期末

### 三場實體活動，同一個專案持續升級

```
期初活動（紙筆畫流程）          ← 已完成
    ↓
期中 MVP Builder（今天）        ← 你在這
    ↓
期末團專（團隊完整系統）        ← 下一站
```

### 每階段疊加能力

| 階段 | 做什麼 | 產出 |
|------|--------|------|
| 期初 | 紙筆畫流程圖 | 概念理解 |
| **期中** | **個人寫程式跑 pipeline** | **可跑的 MVP 作品** |
| 期末 | 團隊整合完整系統 | 可部署的系統 |

> 今天做的東西，期末會回來用。**不要做完就丟。**

---

## Slide 4 — Pipeline 架構圖

### 你的 Mini Data Pipeline 長這樣

```
┌─────────────┐     ┌──────────────┐     ┌────────────────────────┐
│  CSV 資料   │────▶│ pandas 清洗  │────▶│  SQLite 資料庫         │
│ (2000 筆)   │     │ (Transform)  │     │  ├── raw 表（原始）    │
└─────────────┘     └──────────────┘     │  ├── cleaned 表（清洗）│
                                          │  └── analyzed 表（AI） │
                                          └────────┬───────────────┘
                                                   │
                              ┌─────────────┐      │      ┌──────────────┐
                              │ SQL 查詢    │◀─────┤      │ LLM 分析     │
                              │ (統計分析)  │      └─────▶│ (分類/摘要)  │
                              └──────┬──────┘             └──────┬───────┘
                                     │                           │
                              ┌──────▼──────┐             ┌──────▼───────┐
                              │ CSV 統計    │             │ report.md    │
                              └─────────────┘             └──────────────┘
                                                                │
                              ┌──────────────────────────────────┘
                              ▼ （選做）
                        FastAPI API → Streamlit Dashboard
```

> **必做**：CSV → SQLite 三表 → SQL → LLM → 報告
> **選做**：FastAPI + Streamlit

---

## Slide 5 — 半天時間表

| 時段 | 分鐘 | 做什麼 |
|------|------|--------|
| **10:00-10:40** | 40 | 開場 + Pipeline Demo + 選題 |
| 10:40-10:45 | 5 | 休息 |
| **10:45-11:05** | 20 | ETL 講解：清洗重點 + pandas 常見坑 |
| **11:05-11:55** | 50 | 🔧 **實作 1**：選題 → 開環境 → ETL |
| 11:55-12:00 | 5 | 休息 |
| 12:00-13:30 | 90 | 午休 |
| **13:30-13:50** | 20 | LLM 講解：prompt 設計 + API vs fallback |
| **13:50-14:40** | 50 | 🔧 **實作 2**：LLM 分析 → 報告 |
| 14:40-14:45 | 5 | 休息 |
| **14:45-15:00** | 15 | 打包講解：README + Demo 怎麼講 |
| **15:00-15:15** | 15 | 🔧 **實作 3**：打包 |
| **15:15-16:00** | 45 | 🎤 **閃電秀**：每人 3 分鐘 |

> 講解 95 min + 實作 115 min + Demo 45 min + 休息 15 min

---

## Slide 6 — 活動規則

### 可以做

- ✅ 用 ChatGPT / Claude 生成 pandas / SQL 語法
- ✅ 用 AI debug 錯誤訊息
- ✅ 用 LLM API 做分類、摘要、洞察
- ✅ 同組互相討論、互相 debug

### 不建議

- ⚠️ 完全貼上不了解的程式碼（Demo 時要能說明）

### 做不完沒關係

- Notebook 帶走，課後可以繼續
- 完成到哪就 Demo 到哪
- 後續課程會回來升級

> **AI 是你的工具，不是你的替身。**

---

## Slide 7 — 6 個題目

### 選一個你有興趣的

| # | 題目 | 資料 | LLM 做什麼 | 適合誰 |
|---|------|------|-----------|--------|
| 1 | 零售 POS 銷售分析 | 2,000 筆交易 | 品類分類 + 客戶洞察 | 想看銷售排行 |
| 2 | B2C 電商競品比價 | 2,000 筆跨平台價格 | 書籍分類 + 定價建議 | 想做價格比較 |
| 3 | 音樂串流趨勢分析 | 2,000 筆 Spotify（29 欄） | 曲風分類 + 推薦文案 | 想分析串流 |
| 4 | 叫車服務交通熱點 | 2,000 筆 NYC 計程車 | 區域分類 + 調度建議 | 想做地理分析（最複雜） |
| 5 | 求職媒合薪資洞察 | 2,000 筆職缺與薪資 | 職位分類 + 職涯建議 | 想看薪資行情 |
| 6 | 不動產房價趨勢 | 2,000 筆台灣實價登錄 | 區域分類 + 建議書 | 想分析房價（中文資料） |

> 每題都有真實資料、需求規格書、Notebook、API、Dashboard。

---

## Slide 8 — 題目情境卡

### 你扮演的角色

| # | 情境 |
|---|------|
| 1 | 你是**零售集團資料顧問**。老闆想知道哪些商品最暢銷、哪些客戶最有價值。 |
| 2 | 你是**電商平台資料顧問**。老闆想知道同一本書在兩個平台價差多大。 |
| 3 | 你是**音樂串流平台資料顧問**。產品經理想知道哪些歌最紅、跨平台表現差異。 |
| 4 | 你是**叫車公司資料顧問**。營運主管想知道哪些時段地區叫車最多。 |
| 5 | 你是**求職平台資料顧問**。產品經理想知道資料領域薪資行情。 |
| 6 | 你是**不動產業者資料顧問**。業務主管想知道各縣市房價差異。 |

> 詳細需求見各題的 `requirements_spec.md`。

---

## Slide 9 — Repo 導覽

### Clone 下來後，去哪找什麼

```
midterm-mvp-template/
├── data/raw/topic_1/         ← 你的題目資料夾
│   ├── requirements_spec.md      先讀這個（需求）
│   ├── orders.csv                你的資料
│   ├── pipeline_starter.ipynb    打開這個（Notebook）
│   ├── api.py                    選做（FastAPI）
│   ├── app.py                    選做（Streamlit）
│   ├── processed/                跑完產出（統計 CSV）
│   └── output/                   跑完產出（報告）
│
├── docs/                     ← 參考文件
│   ├── ai_prompts.md             AI prompt 模板
│   ├── README_TEMPLATE.md        打包用的 README 模板
│   └── upgrade_plan.md           你要填的升級計畫
```

> 你的東西都在 `data/raw/topic_{N}/` 裡，不會跟別人的混在一起。

---

## Slide 10 — Notebook 怎麼用

### 打開 `pipeline_starter.ipynb`

Notebook 有 10 個 Section、約 60 格 cell。標記如下：

| 標記 | 意思 | 你要做什麼 |
|------|------|-----------|
| `TODO 🟢 簡單` | 有相關程式碼可參考 | 取消註解、改欄位名 |
| `TODO 🟡 中等` | 有別的情境範例教語法 | 看範例，翻譯到你的欄位 |
| `TODO 🔴 較難` | 有骨架，填關鍵處 | 填入 SQL / 欄位名 |
| `（不需要改）` | 直接跑 | Shift + Enter |

### 循序漸進

```
前 4 格：🟢 有相關程式碼（手把手帶）
中間：  🟡 有範例但要自己翻譯（放手）
後面：  🔴 有骨架填空（挑戰）
```

---

## Slide 11 — Section 1：Extract

> 投影時機：10:45-11:05 ETL 講解

### 資料怎麼進入系統

```
CSV 檔案 → pd.read_csv() → DataFrame → df.to_sql() → SQLite raw 表
```

### 為什麼寫入資料庫？

- 真實 DE 工作中，資料不會一直是 CSV
- 寫入資料庫 → 可以用 SQL 查詢 → 可以被 API 存取
- 今天用 SQLite（零安裝），後續升級到 MySQL / BigQuery

### 你要做的

1. `pd.read_csv("檔名.csv")` 讀資料
2. 檢查資料品質：`.dtypes` / `.isnull().sum()` / `.describe()`
3. `df.to_sql("raw_xxx", conn)` 寫入 SQLite
4. `pd.read_sql("SELECT COUNT(*) FROM raw_xxx", conn)` 驗證

---

## Slide 12 — Section 2：Transform

### 清洗重點

| 常見問題 | 怎麼處理 | pandas 方法 |
|---------|---------|-------------|
| 缺漏值 | 刪掉或填值 | `df.dropna()` / `df.fillna()` |
| 型別錯誤 | 字串轉數字 | `pd.to_numeric(df["欄位"], errors="coerce")` |
| 日期字串 | 轉 datetime | `pd.to_datetime(df["欄位"])` |
| 異常值 | 過濾掉 | `df = df[df["欄位"] > 0]` |

### 各題的清洗難點

| 題 | 難點 |
|---|------|
| 1 | invoice_date 轉日期，提取年月時 |
| 2 | 價格欄位有字串，要轉數字 |
| 3 | Spotify Streams 有逗號，要去逗號轉數字 |
| 4 | **merge 兩張表**（trips + zone lookup）← 最難 |
| 5 | 比較簡單，salary 轉數字就好 |
| 6 | **民國年轉西元年**（1130101 → 2024-01）← 最難 |

---

## Slide 13 — SQLite 三表設計

### 同一份資料，三種狀態

```
raw_xxx 表        cleaned_xxx 表      analyzed_xxx 表
（原始資料）      （清洗後）          （LLM 分析後）
  2000 筆     →     ~1950 筆     →      50 筆
  有缺漏值          型別正確            有 AI 標籤
  格式混亂          新增欄位            有洞察摘要
```

### 為什麼分三張表？

- **Data Lineage**：追蹤資料從哪來、經過什麼處理
- 這就是 Data Warehouse 分層的雛形：raw → staging → mart
- 出問題時可以回到 raw 重跑，不用重新下載

---

## Slide 14 — 實作 1 開始

> 投影時機：11:05

### 你現在要做：Section 1-3（50 分鐘）

```
✅ Section 1：讀 CSV → 寫入 SQLite raw 表
✅ Section 2：清洗 → 寫入 cleaned 表
✅ Section 3：SQL 查詢統計
```

### 提醒

- 前 4 格有 `# 相關程式碼`，取消註解就能跑
- 遇到問題 → 看 Notebook 裡的提示 → 問同組 → 問 ChatGPT → 舉手問 TA
- **卡太久就跳過，先把 raw + cleaned 表建好**

> ⏱ 50 分鐘後回來。

---

## Slide 15 — Section 4：LLM 加值

> 投影時機：13:30-13:50 LLM 講解

### 從「聊天」到「自動化」

```
手動方式：開 ChatGPT → 貼一筆資料 → 看回應 → 再貼下一筆...
    ↓
自動化：寫程式 → 呼叫 API → 批次處理 2000 筆 → 結果存回資料庫
```

### 每題的 LLM 應用

| 題 | LLM 做什麼 |
|---|-----------|
| 1 | 商品品類分類（家飾/禮品/餐具/季節商品/文具） |
| 2 | 書籍品類分類（科技/商業/文學/教育/生活） |
| 3 | 曲風分類（流行/嘻哈/搖滾/電子） |
| 4 | 區域分類（商業區/住宅區/交通樞紐/觀光區） |
| 5 | 職位分類（工程/分析/科學/管理） |
| 6 | 區域分類（蛋黃區/蛋白區/郊區/新興區） |

---

## Slide 16 — Prompt 設計技巧

### 三個原則

1. **給明確的標籤選項**（不要開放式）

```
❌ 「請分析這段文字」
✅ 「請分類為以下其中一個：家飾/禮品/餐具/季節商品/文具/其他」
```

2. **要求 JSON 格式回傳**

```
✅ 請回傳 JSON：{"category": "...", "insight": "..."}
```

3. **加上「不確定就選最接近的」避免拒答**

> Prompt 模板在 `docs/ai_prompts.md`，可以直接用。

---

## Slide 17 — API vs Fallback

### 有 API Key → 呼叫 OpenAI

```python
result = llm_analyze(text, api_key)  # 呼叫 GPT-4o-mini
```

### 沒有 API Key → 用規則版（也能完成！）

```python
result = llm_analyze(text, None)  # 用關鍵字規則判斷
```

### Fallback 怎麼運作

```python
if "christmas" in text.lower():
    category = "季節商品"
elif "cup" in text.lower():
    category = "餐具"
```

> **兩個版本都能產出結果**。沒 API Key 不影響完成度。

---

## Slide 18 — 實作 2 開始

> 投影時機：13:50

### 你現在要做：Section 4-6（50 分鐘）

```
✅ Section 4：LLM 分析 → 寫入 analyzed 表
✅ Section 5：跨表驗證（data lineage）
✅ Section 6：產出 report.md
```

### 提醒

- **先跑 1 筆測試**，確認 prompt 有效再跑批次
- 批次先用 50 筆，確認品質後可以改大
- API 太慢？改 `BATCH_SIZE = 20` 先看結果
- **LLM 結果不完美沒關係**，重點是體驗「程式 × AI API」

> ⏱ 50 分鐘後回來。

---

## Slide 19 — 打包教學

> 投影時機：14:45-15:00

### 你要填兩份文件

| 文件 | 在哪 | 填什麼 |
|------|------|--------|
| **README** | `docs/README_TEMPLATE.md` | 題目、流程、產出、學到什麼 |
| **升級計畫** | `docs/upgrade_plan.md` | 後續要用 Docker/Airflow/GCP 做什麼 |

### README 模板長這樣

```markdown
# {專案名稱}
## 題目與目標
## Pipeline 架構
## 如何執行
## 產出
## 關鍵發現
## 我學到什麼
## 後續升級計畫
```

> 填完就是你的**作品集說明文件**。

---

## Slide 20 — 最低完成標準

### 打勾確認

- [ ] 跑完 Notebook Section 1-6
- [ ] `pipeline.db` 有 raw / cleaned / analyzed 三張表
- [ ] `processed/` 有統計結果 CSV
- [ ] `output/report.md` 有 LLM 分析報告
- [ ] 填完 `docs/upgrade_plan.md`
- [ ] 能用 3 分鐘說明你的 pipeline

> 全部打勾 = 你的 MVP 完成了。

---

## Slide 21 — 閃電秀

> 投影時機：15:15

### 每人 3 分鐘，嚴格計時

| 時間 | 講什麼 |
|------|--------|
| 0:00-0:30 | 我的題目解決什麼問題 |
| 0:30-1:00 | 資料從哪來、做了什麼清洗 |
| 1:00-1:30 | LLM 在 pipeline 裡做了什麼 |
| 1:30-2:00 | show output（report / 截圖 / dashboard） |
| 2:00-2:30 | 下一步怎麼升級 |
| 2:30-3:00 | 快問快答 |

### 展示方式

- Notebook 直接 show output cell
- 截圖投影
- Streamlit Dashboard（進階）

> **重點不是做得多完美，是你能不能講清楚。**

---

## Slide 22 — 選做預告

### 如果你還有時間

| Section | 做什麼 | 在哪 |
|---------|--------|------|
| 8 | FastAPI — 把分析結果變成 API | Notebook 裡 or `api.py` |
| 9 | Dashboard — ipywidgets 互動圖表 | Notebook 裡 or `app.py` |
| 10 | 本地部署 — 回家跑 FastAPI + Streamlit | Notebook 裡有指引 |

### 完整架構

```
Notebook → pipeline.db → api.py（API）→ app.py（Dashboard）
```

> 今天做不完沒關係，Notebook 帶走回家做。

---

## Slide 23 — 後續升級路線

### 同一個專案，每學一個新技術就升級一次

```
今天（期中）                    後續課程
──────────────────────────────────────────
Colab Notebook 手動跑       →   EP01 拆成 ETL 架構
SQLite                      →   MySQL / BigQuery
CSV 檔案                    →   資料庫
手動觸發 pipeline           →   Airflow DAG 排程
本地 Streamlit              →   Docker 容器化
本地開發                    →   GCP 雲端部署
個人 MVP                    →   期末團隊完整系統
```

> 最終放進履歷的不是練習題，而是一個**歷經多次迭代的完整作品**。

---

## Slide 24 — 你會帶走什麼

### 四件具體產出

| 產出 | 證明什麼 |
|------|---------|
| **pipeline.db** | 你能建一條完整的 ETL pipeline |
| **report.md** | 你能用 AI 做資料分析 |
| **GitHub Repo** | 你會作品集打包 |
| **3 分鐘 Demo 經驗** | 你能講清楚你做的東西 |

### 對團隊的意義

- 今天不同題目的同學 = 互相學習的夥伴
- 期末團專時，你們就是有「做過 pipeline」經驗的隊友

---

## Slide 25 — 結尾

### 三件事

1. **今天的 Notebook + pipeline.db + 報告帶走**（不要做完就丟）
2. **課後把 repo push 到你自己的 GitHub**
3. **後續課程會回來升級這個專案**

### 一句話

> **「這是你履歷上的第一條 Data Pipeline。」**

── Q&A ──
