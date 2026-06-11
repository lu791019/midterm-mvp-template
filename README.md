# LLM × DE MVP Builder 實戰工作坊

> TibaMe 雲端資料工程師在職遠距班 — 期中實戰工作坊 Starter Repo
>
> 🚀 **現場速查卡**：[START_HERE.md](START_HERE.md)
> 📋 **學員手冊**：[_instructor/student_handbook.md](_instructor/student_handbook.md)

每位學員選一個題目，完成一條 **Mini Data Pipeline**：

```
CSV → pandas → SQLite (raw/cleaned/analyzed) → 統計分析 → LLM → Pipeline Documentation → FastAPI
```

---

## 快速開始

```bash
# 1. Clone（或下載 ZIP 解壓縮）
git clone https://github.com/lu791019/midterm-mvp-template.git
cd midterm-mvp-template

# 2. 選你的題目（1-6），打開對應的 Notebook
#    Colab：上傳 data/raw/topic_1/pipeline_starter.ipynb（Section 0 自動設定環境）
#    本地：jupyter notebook data/raw/topic_1/pipeline_starter.ipynb

# 3. 照著 Notebook 一格一格跑
```

---

## 三段實作

| 實作 | 時間 | Section | 做什麼 | 交付物 |
|------|------|---------|--------|--------|
| **實作 1** | 25 min | 0 | 環境 + 選題 + 討論 | Notebook 跑通、已選題 |
| **實作 2** | 45 min | 1-3 | Extract → raw 表 → Transform → cleaned 表 → 統計分析 | `pipeline.db`（raw + cleaned）、`processed/*.csv` |
| **實作 3** | 30 min | 4-8 | LLM → analyzed 表 → Pipeline Doc → FastAPI | `pipeline.db`（analyzed）、`output/pipeline_doc.md`、API 跑起來 |
| **回家** | 課後 | 9-10 | Dashboard | ipywidgets / Streamlit |

**Demo**：每組推派 1 人 × 3 分鐘

---

## 步驟導覽

### Step 1：選題

| # | 題目 | 資料 | 一句話 | 需求 |
|---|------|------|--------|------|
| 1 | 零售 POS 銷售分析 | 2,000 筆交易 | 找暢銷商品和高價值客戶 | [spec](data/raw/topic_1/requirements_spec.md) |
| 2 | B2C 電商競品比價 | 2,000 筆商品 | 跨平台價差分析 | [spec](data/raw/topic_2/requirements_spec.md) |
| 3 | 音樂串流趨勢分析 | 2,000 筆歌曲 | Spotify / YouTube / TikTok | [spec](data/raw/topic_3/requirements_spec.md) |
| 4 | 叫車服務交通熱點 | 2,000 筆行程 | 時段 × 地區（最複雜）| [spec](data/raw/topic_4/requirements_spec.md) |
| 5 | 求職媒合薪資洞察 | 2,000 筆職缺 | 資料領域薪資行情 | [spec](data/raw/topic_5/requirements_spec.md) |
| 6 | 不動產房價趨勢 | 2,000 筆登錄 | 台灣實價登錄（中文）| [spec](data/raw/topic_6/requirements_spec.md) |

> 資料來源詳情見 [docs/data_sources.md](docs/data_sources.md)

### Step 2：讀需求 → 開 Notebook

```
📂 data/raw/topic_N/
├── 📄 requirements_spec.md    ← 先讀：情境/角色/資料/MVP scope
├── 📊 xxx.csv                 ← 原始資料（2,000 筆）
└── 📓 pipeline_starter.ipynb  ← 從這裡開始做
```

### Step 3：照 Section 跑

每個 Section 開頭有 🎯 完成標準，告訴你「做到哪算完成」。

| Section | 做什麼 | 交付物 |
|---------|--------|--------|
| 0 | 環境設定（Colab 自動 clone） | 套件載入成功 |
| 1 | Extract — 讀 CSV → 寫入 **raw 表** | `pipeline.db` 的 raw 表 |
| 2 | Transform — 清洗 → 寫入 **cleaned 表** | cleaned 表 |
| 3 | 統計分析（pandas / SQL）| `processed/*.csv` |
| 4 | LLM / fallback → 寫入 **analyzed 表** + 三表驗證 | analyzed 表 |
| 6 | Pipeline Documentation | `output/pipeline_doc.md` |
| 7 | Next Step 規劃 | `docs/upgrade_plan.md` |
| 8 | FastAPI | API `/health` 回 200 |
| 9-10 | Dashboard（回家作業）| ipywidgets / Streamlit |

### Step 4：跑完後，你的資料夾

```
📂 data/raw/topic_N/
├── 🗄️ pipeline.db                ← 自動產生
│   ├── raw_* 表                     原始資料（Bronze）
│   ├── cleaned_* 表                 清洗後（Silver）
│   └── analyzed_* 表                LLM 分析（Gold）
├── 📂 processed/                  ← 統計 CSV
├── 📂 output/
│   └── pipeline_doc.md            ← Pipeline Documentation
├── api.py                         ← FastAPI
└── app.py                         ← Dashboard（回家作業）
```

### Step 5：FastAPI

```bash
cd data/raw/topic_N
pip install fastapi uvicorn
uvicorn api:app --reload --port 8000
# 開瀏覽器 http://localhost:8000/health
```

| Endpoint | 說明 |
|----------|------|
| `GET /health` | 確認 API + DB 狀態 |
| `GET /stats/...` | 統計結果 |
| `GET /analyzed` | LLM 分析結果 |
| `GET /summary` | 三表摘要 |

### Step 6：課後 — Push 到你的 GitHub

1. 把整個 topic 資料夾 push 到你自己的 GitHub repo
2. 用 `output/pipeline_doc.md` 的內容整理成 repo 的 `README.md`
3. 填完 `docs/upgrade_plan.md`

> 💡 用 [docs/ai_prompts.md](docs/ai_prompts.md) 的 Prompt #7，貼 notebook 資訊給 AI，自動產出 Pipeline Documentation 草稿。

**目的**：你的 GitHub repo 就是作品集。Pipeline Documentation 當 README，面試官打開就看得懂你做了什麼。

---

## Pipeline 架構

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

    subgraph "Section 3：統計分析"
        F -->|pandas / SQL| G[統計結果]
        G --> H[processed/*.csv]
    end

    subgraph "Section 4：LLM 加值"
        F -->|pd.read_sql| I[取出文字欄位]
        I -->|LLM API 或 fallback| J[分類 + 洞察]
        J -->|df.to_sql| K[(SQLite: analyzed 表)]
    end

    subgraph "Section 6：Pipeline Documentation"
        K --> N[output/pipeline_doc.md]
        H --> N
    end

    subgraph "Section 8：FastAPI"
        C -.-> O[api.py]
        F -.-> O
        K -.-> O
    end

    style C fill:#e3f2fd
    style F fill:#e8f5e9
    style K fill:#fff3e0
    style O fill:#f3e5f5
```

---

## Repo 結構

```
midterm-mvp-template/
├── README.md                          ← 📍 你在這裡
├── START_HERE.md                      ← 🚀 現場速查卡
├── requirements.txt
├── .env.example                       ← API Key 設定（複製成 .env）
│
├── data/raw/                          ← 📂 6 個題目
│   └── topic_N/
│       ├── requirements_spec.md           需求規格書
│       ├── xxx.csv                        原始資料（2,000 筆）
│       ├── pipeline_starter.ipynb         📓 Notebook（從這開始）
│       ├── api.py                         FastAPI（活動內容）
│       ├── app.py                         Dashboard（回家作業）
│       ├── processed/                     統計產出
│       └── output/                        pipeline_doc.md
│
├── docs/                              ← 📂 參考文件
│   ├── README_TEMPLATE.md                 Pipeline Documentation 模板
│   ├── ai_prompts.md                      AI prompt 模板（含自動填文件 prompt）
│   ├── upgrade_plan.md                    📝 後續升級計畫（要填！）
│   ├── topic_catalog.md                   6 題總覽
│   ├── data_sources.md                    資料來源
│   ├── pipeline.mmd                       Pipeline 流程圖（Mermaid）
│   ├── repo_format.md                     Repo 格式說明
│   └── tech_decision.md                   工具選型紀錄
│
├── _advanced/                         ← Docker 模板（後續課程用）
│   ├── Dockerfile
│   └── docker-compose.yml
│
└── _instructor/                       ← 講師用
    ├── mvp_builder_slides.html            簡報（24 張）
    ├── speaker_notes.md                   講稿
    ├── facilitator_guide.md               講師手冊
    ├── student_handbook.md                學員手冊
    ├── ta_briefing.md                     TA 行前 Brief
    ├── student_pre_event_notice.md        學員事前通知
    ├── student_pre_event_notice.pptx      事前通知（PPTX）
    ├── project_report_rubric.md           專題報告評估表
    ├── project_report_rubric.pptx         評估表（PPTX）
    ├── final_project_tracking.md          期末專題追蹤
    ├── midterm_workshop_proposal.md       ⚠️ 歷史文件
    └── solutions/                         6 題答案
```

---

## 完成標準

### 現場必做

- [ ] 跑完 Section 1-8
- [ ] `pipeline.db` 有 raw / cleaned / analyzed 三表
- [ ] `processed/` 有統計 CSV
- [ ] `output/pipeline_doc.md` 有 Pipeline Documentation
- [ ] FastAPI `/health` 回 200
- [ ] 每組推派 1 人 Demo 3 分鐘

### 課後

- [ ] Dashboard（Section 9-10）
- [ ] `pipeline_doc.md` 整理成你自己 repo 的 `README.md`
- [ ] Push 到你的 GitHub
- [ ] 填完 [docs/upgrade_plan.md](docs/upgrade_plan.md)

---

## AI 使用規範

| 用法 | 是否允許 |
|------|---------|
| 用 ChatGPT/Claude 生成 pandas/SQL | ✅ 允許 |
| 用 AI debug 錯誤 | ✅ 允許 |
| 用 LLM API 做分類/摘要 | ✅ 允許 |
| 用 AI prompt 產出 Pipeline Documentation | ✅ 鼓勵 |
| 完全貼上不了解的程式碼 | ⚠️ 不建議 |

> Prompt 模板見 [docs/ai_prompts.md](docs/ai_prompts.md)

---

## 後續升級

| 階段 | 升級內容 | 業界工具 |
|------|---------|---------|
| 帶狀課 | 拆成正式 ETL 架構 + Python package | module/package |
| Docker | 容器化 pipeline | Docker Compose |
| Airflow | 改成 DAG 排程 | Airflow / Dagster |
| 資料庫 | SQLite → 正式 DB | BigQuery / Cloud SQL |
| GCP | 雲端部署 | Cloud Run / Composer |

> 升級計畫模板：[docs/upgrade_plan.md](docs/upgrade_plan.md)
> Docker 模板：[_advanced/Dockerfile](_advanced/Dockerfile)

---

## 文件索引

| 文件 | 用途 | 什麼時候看 |
|------|------|-----------|
| [START_HERE.md](START_HERE.md) | 現場速查卡 | **活動當天第一個看** |
| [docs/README_TEMPLATE.md](docs/README_TEMPLATE.md) | Pipeline Documentation 模板 | **Section 6 填寫 + 課後整理成 README** |
| [docs/ai_prompts.md](docs/ai_prompts.md) | AI prompt（含自動填文件 Prompt #7）| 實作中 + 寫文件時 |
| [docs/upgrade_plan.md](docs/upgrade_plan.md) | 後續升級計畫 | **Section 7 填寫** |
| [docs/topic_catalog.md](docs/topic_catalog.md) | 6 題總覽 | 選題時 |
| [docs/data_sources.md](docs/data_sources.md) | 資料來源 | 想了解資料時 |
| [docs/pipeline.mmd](docs/pipeline.mmd) | Pipeline 流程圖 | 想看架構時 |
| [docs/tech_decision.md](docs/tech_decision.md) | 工具選型理由 | 寫 Design Decisions 時 |
