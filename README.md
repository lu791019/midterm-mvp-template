# LLM × DE Mini Data Pipeline 工作坊

> TibaMe 雲端資料工程師養成班 — 期中 MVP 工作坊 Starter Repo

每位學員選一個題目，完成 **Mini Data Pipeline**：

```
CSV → pandas 清洗 → SQLite (raw/cleaned/analyzed) → SQL 查詢 → LLM 分析 → FastAPI → Streamlit
```

## 快速開始

```bash
# 1. Clone（或下載 ZIP 解壓縮）
git clone https://github.com/lu791019/midterm-mvp-template.git
cd midterm-mvp-template

# 2. 選你的題目（1-8），打開對應的 Notebook
#    例如選題目 1：
#    → 用 Colab：上傳 data/raw/topic_1/pipeline.ipynb
#    → 用本地：jupyter notebook data/raw/topic_1/pipeline.ipynb

# 3. 照著 Notebook 一格一格跑
```

## 詳細步驟導覽

> 第一次用不知道去哪找東西？照下面走一遍。

### Step 1：選題

到下方「[你的題目](#你的題目)」表格，選一個你有興趣的題目（1-8）。
假設你選了 **題目 1（餐飲連鎖 POS 庫存優化）**。

### Step 2：看需求

打開你的題目資料夾，先讀需求規格書：

```
📂 data/raw/topic_1/
└── 📄 requirements_spec.md    ← 先讀這個！裡面有：
                                  - 你要扮演什麼角色
                                  - 客戶的問題是什麼
                                  - 資料有哪些欄位
                                  - 今天的 MVP 要做到什麼
```

### Step 3：開 Notebook 開始做

同一個資料夾裡有你的 Notebook：

```
📂 data/raw/topic_1/
├── 📄 requirements_spec.md    ← Step 2 讀過了
├── 📊 reviews.csv             ← 你的原始資料（2,000 筆）
└── 📓 pipeline.ipynb          ← 打開這個！照著一格一格跑
```

**用 Google Colab 開**：到 [colab.google](https://colab.research.google.com/) → 上傳 → 選 `pipeline.ipynb`
**用本地開**：`jupyter notebook data/raw/topic_1/pipeline.ipynb`

### Step 4：跑完後，產出在哪裡

Notebook 跑完後，你的成果會出現在：

```
📂 專案根目錄/
├── 🗄️ pipeline.db              ← 你的 SQLite 資料庫（自動產生）
│   ├── raw_reviews 表              原始資料
│   ├── cleaned_reviews 表          清洗後資料
│   └── analyzed_reviews 表         LLM 分析結果
│
├── 📂 data/processed/           ← 統計結果 CSV（自動產生）
│   └── restaurant_stats.csv
│
└── 📂 output/                   ← 顧問報告（自動產生）
    └── report.md
```

### Step 5：選做 — FastAPI + Streamlit

如果你還有時間，同一個資料夾裡有 API 和 Dashboard：

```
📂 data/raw/topic_1/
├── api.py     ← FastAPI API
└── app.py     ← Streamlit Dashboard
```

**`api.py` 是什麼？為什麼需要它？**

你在 Step 3 跑完 Notebook 後，分析結果都存在 `pipeline.db`（SQLite 資料庫）裡。
`api.py` 用 FastAPI 把資料庫裡的結果**包裝成 API endpoint**，讓別人（或前端）可以透過網址取得你的分析：

```
GET /stats      → 回傳各餐廳評分統計（從 cleaned 表查詢）
GET /analyzed   → 回傳 LLM 分析結果（從 analyzed 表查詢）
GET /summary    → 回傳 pipeline 三表的摘要統計
GET /report     → 回傳 output/report.md 的報告內容
GET /health     → 確認 API 和資料庫正常運作
```

這就是真實資料工程的做法：**資料存在資料庫 → API 提供存取 → 前端呈現**，而不是直接傳 CSV 給別人。

**`app.py` 是什麼？為什麼需要它？**

`app.py` 用 Streamlit 把你的分析結果**變成互動式 Dashboard**。
它可以直接讀 SQLite，也可以透過 `api.py` 的 API 拿資料（體驗「前後端分離」的架構）。
打開後你會看到：圖表、統計數字、LLM 分析明細、顧問報告——這就是你交給客戶看的東西。

**怎麼跑？**

```bash
# 啟動 API（先裝 uvicorn）
pip install fastapi uvicorn
uvicorn data.raw.topic_1.api:app --reload --port 8000

# 另開 terminal，啟動 Dashboard
pip install streamlit
streamlit run data/raw/topic_1/app.py
```

### Step 6：打包

跑完後，填寫以下兩份文件完成打包：

| 要填什麼 | 在哪裡 | 說明 |
|---------|--------|------|
| 後續升級計畫 | [docs/upgrade_plan.md](docs/upgrade_plan.md) | 寫下你打算怎麼用 Docker/Airflow/GCP 升級這個專案 |
| README | 用講師提供的模板 | 填完就是你的作品集說明文件 |

### 遇到問題？

| 狀況 | 去哪找幫助 |
|------|-----------|
| 不知道 pandas 語法怎麼寫 | [docs/ai_prompts.md](docs/ai_prompts.md) 有 prompt 模板，貼給 ChatGPT |
| 不知道 LLM prompt 怎麼設計 | [docs/ai_prompts.md](docs/ai_prompts.md) 的第 5、6 節 |
| 想知道資料從哪來的 | [docs/data_sources.md](docs/data_sources.md) |
| 想看其他題目的規格 | [docs/topic_catalog.md](docs/topic_catalog.md) |
| 想了解為什麼用 SQLite 不用 MySQL | [docs/tech_decision.md](docs/tech_decision.md) |

---

## Pipeline 流程

Notebook 會帶你走完以下 6 個 Section，每個 Section 對應 pipeline 的一個階段：

```mermaid
flowchart TD
    subgraph "Section 1：Extract"
        A[CSV 原始資料] -->|pd.read_csv| B[pandas DataFrame]
        B -->|df.to_sql| C[(SQLite: raw 表)]
    end

    subgraph "Section 2：Transform"
        C -->|pd.read_sql| D[pandas 清洗]
        D -->|dropna / 型別轉換 / 新增欄位| E[cleaned DataFrame]
        E -->|df.to_sql| F[(SQLite: cleaned 表)]
    end

    subgraph "Section 3：SQL 統計分析"
        F -->|SQL GROUP BY / ORDER BY| G[統計結果]
        G --> H[data/processed/*.csv]
    end

    subgraph "Section 4：LLM 加值分析"
        F -->|pd.read_sql| I[取出文字欄位]
        I -->|LLM API 或 fallback| J[情緒/分類/摘要]
        J -->|df.to_sql| K[(SQLite: analyzed 表)]
    end

    subgraph "Section 5：驗證"
        C -.- L{跨表查詢}
        F -.- L
        K -.- L
        L --> M[三表筆數一致 ✓]
    end

    subgraph "Section 6：產出報告"
        K --> N[output/report.md]
        H --> N
    end

    subgraph "選做：API + Dashboard"
        C -.-> O[FastAPI api.py]
        F -.-> O
        K -.-> O
        O -.-> P[Streamlit app.py]
    end

    style C fill:#e3f2fd
    style F fill:#e8f5e9
    style K fill:#fff3e0
    style O fill:#f3e5f5
    style P fill:#f3e5f5
```

| Section | 做什麼 | 產出 |
|---------|--------|------|
| 1. Extract | 讀 CSV → 寫入 SQLite `raw` 表 | `pipeline.db` 的 raw 表 |
| 2. Transform | 從 raw 表讀出 → pandas 清洗 → 寫入 `cleaned` 表 | cleaned 表 |
| 3. SQL 統計 | 從 cleaned 表用 SQL 查詢統計 | `data/processed/*.csv` |
| 4. LLM 分析 | 從 cleaned 表讀文字 → LLM 分析 → 寫入 `analyzed` 表 | analyzed 表 |
| 5. 驗證 | 跨表查詢確認三表一致（data lineage） | 驗證通過 ✓ |
| 6. 報告 | 整合統計 + LLM 結果 → 生成顧問報告 | `output/report.md` |
| 選做 | FastAPI 提供 API → Streamlit 顯示 Dashboard | API + Dashboard |

> 完整流程圖 Mermaid 原始檔：[docs/pipeline.mmd](docs/pipeline.mmd)

## Repo 結構

```
midterm-mvp-template/
│
├── README.md                    ← 📍 你在這裡
├── requirements.txt             ← Python 套件（pip install -r requirements.txt）
├── .env.example                 ← API Key 設定範例（複製成 .env 填入）
│
├── data/raw/                    ← 📂 8 個題目的資料與工具
│   ├── topic_1/                 ← 題目 1：餐飲連鎖 POS 庫存優化
│   │   ├── requirements_spec.md     需求規格書（情境/角色/資料/MVP scope）
│   │   ├── reviews.csv              2,000 筆餐廳評論資料
│   │   ├── pipeline.ipynb           📓 Notebook（從這裡開始做！）
│   │   ├── api.py                   ⭐ 選做：FastAPI API
│   │   └── app.py                   ⭐ 選做：Streamlit Dashboard
│   ├── topic_2/                 ← 題目 2：B2C 電商競品比價
│   │   ├── requirements_spec.md
│   │   └── products.csv
│   ├── topic_3/                 ← 題目 3：數位金融客訴效率
│   │   ├── requirements_spec.md
│   │   └── complaints.csv
│   ├── topic_4/                 ← 題目 4：音樂串流趨勢分析
│   │   ├── requirements_spec.md
│   │   └── tracks.csv
│   ├── topic_5/                 ← 題目 5：叫車服務交通熱點
│   │   ├── requirements_spec.md
│   │   ├── trips.csv
│   │   └── taxi_zone_lookup.csv     區域碼 → 地名對照表
│   ├── topic_6/                 ← 題目 6：求職媒合職缺洞察
│   │   ├── requirements_spec.md
│   │   └── jobs.csv
│   ├── topic_7/                 ← 題目 7：媒體業新聞輿情監測
│   │   ├── requirements_spec.md
│   │   └── news.csv
│   └── topic_8/                 ← 題目 8：不動產房價趨勢分析
│       ├── requirements_spec.md
│       └── real_estate.csv
│
├── data/processed/              ← 📂 你的清洗結果會存在這（跑完自動產生）
├── output/                      ← 📂 你的報告會存在這（跑完自動產生）
│
├── docs/                        ← 📂 參考文件（不需要改，需要時查閱）
│   ├── topic_catalog.md             8 題總覽：每題的 MVP 問題/資料/ETL/LLM 規格
│   ├── data_sources.md              資料來源說明：每題的 Kaggle/政府 URL + 欄位
│   ├── ai_prompts.md                AI prompt 模板：7 個可直接用的 prompt
│   ├── repo_format.md               Repo 格式說明：資料夾結構 + 最小交付標準
│   ├── tech_decision.md             工具選型紀錄（為什麼選 SQLite/pandas/etc.）
│   ├── pipeline.mmd                 Pipeline 流程圖（Mermaid 格式）
│   └── upgrade_plan.md              📝 後續升級計畫模板（你要填的！）
│
├── _advanced/                   ← 📂 進階升級用（期中不需要看，後續課程會用到）
│   ├── Dockerfile                   Docker 容器化模板
│   └── docker-compose.yml           Docker Compose 設定
│
└── _instructor/                 ← 📂 講師用（學員不需要看）
    ├── midterm_workshop_proposal.md  工作坊企劃書 v4.0
    └── midterm_workshop_slides.md    簡報原稿
```

## 你的題目

選一個，打開該資料夾的 `requirements_spec.md` 看需求，然後跑 `pipeline.ipynb`：

| # | 題目 | 資料 | LLM 做什麼 | 詳細需求 |
|---|------|------|-----------|---------|
| 1 | 餐飲連鎖 POS 庫存優化 | 2,000 筆餐廳評論 | 情緒分析 + 主題分類 | [requirements_spec.md](data/raw/topic_1/requirements_spec.md) |
| 2 | B2C 電商競品比價追蹤 | 2,000 筆跨平台商品價格 | 競品摘要 + 定價建議 | [requirements_spec.md](data/raw/topic_2/requirements_spec.md) |
| 3 | 數位金融客訴效率分析 | 2,000 筆金融客訴文字 | 情緒分析 + 自動分類 | [requirements_spec.md](data/raw/topic_3/requirements_spec.md) |
| 4 | 音樂串流趨勢分析 | 2,000 筆 Spotify 歌曲 | 聽眾洞察 + 推薦文案 | [requirements_spec.md](data/raw/topic_4/requirements_spec.md) |
| 5 | 叫車服務交通熱點分析 | 2,000 筆 NYC 計程車行程 | 交通模式解讀 + 調度建議 | [requirements_spec.md](data/raw/topic_5/requirements_spec.md) |
| 6 | 求職媒合職缺洞察 | 2,000 筆資料科學職缺 | 職缺摘要 + 技能建議 | [requirements_spec.md](data/raw/topic_6/requirements_spec.md) |
| 7 | 媒體業新聞輿情監測 | 2,000 筆新聞標題摘要 | 情緒分類 + 輿情重點 | [requirements_spec.md](data/raw/topic_7/requirements_spec.md) |
| 8 | 不動產房價趨勢分析 | 2,000 筆台灣實價登錄 | 區域分析建議書 | [requirements_spec.md](data/raw/topic_8/requirements_spec.md) |

> 資料來源詳情見 [docs/data_sources.md](docs/data_sources.md)

## 每人最低完成標準

- [ ] 跑完 `pipeline.ipynb` 的 Section 1-6
- [ ] `pipeline.db` 有 raw / cleaned / analyzed 三張表
- [ ] `data/processed/` 有統計結果 CSV
- [ ] `output/report.md` 有 LLM 分析報告
- [ ] 能用 3 分鐘說明：題目、資料、pipeline、output
- [ ] 填完 [docs/upgrade_plan.md](docs/upgrade_plan.md)

## AI 使用規範

本活動**允許並鼓勵**使用 AI，但要能說明你的 pipeline：

| 用法 | 是否允許 |
|------|---------|
| 用 ChatGPT/Claude 生成 pandas/SQL 草稿 | ✅ 允許 |
| 用 AI debug 錯誤訊息 | ✅ 允許 |
| 用 LLM API 做分類/摘要 | ✅ 允許 |
| 完全貼上不了解的程式碼 | ⚠️ 不建議（Demo 時要能說明） |

> 可直接用的 prompt 模板見 [docs/ai_prompts.md](docs/ai_prompts.md)

## 後續升級

這個 MVP 不是一次性練習。後續課程會持續升級這個專案：

| 階段 | 升級內容 |
|------|---------|
| 後續課程 | 回顧你的 MVP → 拆成正式 ETL 架構 |
| Docker | 容器化 pipeline（模板在 [_advanced/](\_advanced/)） |
| Airflow | run_pipeline 改成 Airflow 的程式碼流程(DAG) |
| MySQL / BigQuery | CSV 換成資料庫 |
| GCP | 部署到雲端 |

> 升級計畫模板：[docs/upgrade_plan.md](docs/upgrade_plan.md)
> Docker 模板參考：[_advanced/Dockerfile](_advanced/Dockerfile)

## 文件索引

| 文件 | 用途 | 什麼時候看 |
|------|------|-----------|
| [docs/topic_catalog.md](docs/topic_catalog.md) | 8 題的 MVP 問題、資料、ETL、LLM 規格 | 選題時 |
| [docs/data_sources.md](docs/data_sources.md) | 每題資料的 Kaggle/政府 URL、欄位、授權 | 想了解資料從哪來時 |
| [docs/ai_prompts.md](docs/ai_prompts.md) | 7 個 AI prompt 模板（需求釐清/pandas/debug/LLM/README） | 實作中需要 AI 幫忙時 |
| [docs/repo_format.md](docs/repo_format.md) | Repo 資料夾結構、最小交付標準、題目切換方式 | 想了解 repo 設計時 |
| [docs/tech_decision.md](docs/tech_decision.md) | 工具選型理由（為什麼 SQLite/pandas/Colab） | 想知道為什麼這樣選時 |
| [docs/pipeline.mmd](docs/pipeline.mmd) | Pipeline 流程圖（Mermaid） | 想看整體架構時 |
| [docs/upgrade_plan.md](docs/upgrade_plan.md) | 後續升級計畫模板 | **學員需要填的！**  |
