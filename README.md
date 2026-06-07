# LLM × DE Mini Data Pipeline 工作坊

> TibaMe 雲端資料工程師養成班 — 期中 MVP 工作坊 Starter Repo

每位學員選一個題目，在半天內完成一條 **Mini Data Pipeline**：

```
CSV → pandas 清洗 → SQLite (raw/cleaned/analyzed) → SQL 查詢 → LLM 分析 → FastAPI → Streamlit
```

## 快速開始

```bash
# 1. Clone
git clone https://github.com/lu791019/midterm-mvp-template.git
cd midterm-mvp-template

# 2. 選你的題目（1-8），打開對應的 Notebook
#    例如選題目 1：
#    → 用 Colab：上傳 data/raw/topic_1/pipeline.ipynb
#    → 用本地：jupyter notebook data/raw/topic_1/pipeline.ipynb

# 3. 照著 Notebook 一格一格跑
```

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
├── _advanced/                   ← 📂 進階升級用（期中不需要看）
│   ├── src/                         模組化 Python 腳本版本（EP01 後從 Notebook 拆出）
│   │   ├── extract.py
│   │   ├── transform.py
│   │   ├── load.py
│   │   ├── llm_analyze.py
│   │   └── run_pipeline.py
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

## Pipeline 流程

```
Section 1：Extract
  → 讀 CSV → 寫入 SQLite raw 表

Section 2：Transform
  → 從 raw 表讀出 → pandas 清洗 → 寫入 cleaned 表

Section 3：SQL 統計分析
  → 從 cleaned 表查詢（GROUP BY, ORDER BY）

Section 4：LLM 加值分析
  → 從 cleaned 表讀文字 → LLM 分析 → 寫入 analyzed 表

Section 5：驗證
  → 跨表查詢確認三表一致（data lineage）

Section 6：產出報告
  → output/report.md

選做：FastAPI + Streamlit
  → api.py 提供 API → app.py 讀 API 顯示 Dashboard
```

> 流程圖見 [docs/pipeline.mmd](docs/pipeline.mmd)

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
| 用 LLM API 做分類/摘要 | ✅ 鼓勵 |
| 完全貼上不了解的程式碼 | ⚠️ 不建議（Demo 時要能說明） |

> 可直接用的 prompt 模板見 [docs/ai_prompts.md](docs/ai_prompts.md)

## 後續升級

這個 MVP 不是一次性練習。後續課程會持續升級這個專案：

| 階段 | 升級內容 |
|------|---------|
| EP01 | 回顧 MVP → 拆成正式 ETL 架構 |
| Docker | 容器化 pipeline（模板在 [_advanced/](\_advanced/)） |
| Airflow | run_pipeline 改成 DAG |
| MySQL / BigQuery | CSV 換成資料庫 |
| GCP | 部署到 Cloud Run |
| 期末團專 | 擴充為團隊完整系統 |

> 升級計畫模板：[docs/upgrade_plan.md](docs/upgrade_plan.md)
> 模組化腳本參考：[_advanced/src/](_advanced/src/)
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
| [docs/upgrade_plan.md](docs/upgrade_plan.md) | 後續升級計畫模板 | **你要填的！** 打包時 |
