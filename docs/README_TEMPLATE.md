# {專案名稱}

> 期中 MVP 工作坊個人作品

## 題目與目標

- **情境**：{一句話描述你的題目，例如「分析零售交易資料，找出暢銷商品和高價值客戶」}
- **解決問題**：{客戶的痛點是什麼}
- **使用者**：{誰會看這個分析結果}
- **資料來源**：{資料從哪來，例如「Kaggle: Online Retail II UCI」}

## 資料說明

| 檔案 | 筆數 | 說明 |
|------|------|------|
| {xxx.csv} | {N} 筆 | {簡要說明} |

## Pipeline 架構

```
CSV → pandas 清洗 → SQLite (raw/cleaned/analyzed) → SQL 查詢 → LLM 分析 → 報告
```

### 各階段做了什麼

| 階段 | 做了什麼 |
|------|---------|
| **Extract** | {讀了什麼資料、寫入哪張 raw 表} |
| **Transform** | {做了什麼清洗：去空值？轉日期？算新欄位？} |
| **Load** | {寫入 SQLite 的 cleaned 表} |
| **SQL 統計** | {做了什麼查詢：排行？分組統計？} |
| **LLM 分析** | {LLM 做了什麼：分類？摘要？建議？} |
| **報告** | {output/report.md 的主要內容} |

## 如何執行

```bash
# 1. 進入題目資料夾
cd data/raw/topic_{N}

# 2. 開 Notebook
jupyter notebook pipeline_starter.ipynb
# 或上傳到 Google Colab

# 3. 照著 Notebook 一格一格跑
```

### 選做：FastAPI + Streamlit

```bash
# API
uvicorn api:app --reload --port 8000

# Dashboard
streamlit run app.py
```

## 產出

| 產出 | 路徑 | 說明 |
|------|------|------|
| SQLite 資料庫 | `pipeline.db` | 含 raw / cleaned / analyzed 三張表 |
| 統計結果 | `processed/*.csv` | {列出你產出的 CSV} |
| 分析報告 | `output/report.md` | {報告的主要結論} |

## 關鍵發現

1. {發現 1，附數字}
2. {發現 2，附數字}
3. {發現 3，附數字}

## 我學到什麼

- {學到的 1，例如「用 SQLite 存資料比 CSV 更適合被查詢」}
- {學到的 2，例如「LLM 做分類前要先測單筆確認品質」}
- {學到的 3}

## 後續升級計畫

| 階段 | 升級內容 | 對應課程 |
|------|---------|---------|
| EP01 | 回顧 MVP → 拆成正式 ETL 架構 | 帶狀課 |
| Docker | 容器化 pipeline + dashboard | Docker 模組 |
| Airflow | run_pipeline 改成 DAG 排程 | Airflow 模組 |
| MySQL / BigQuery | CSV 換成資料庫 | 資料庫模組 |
| GCP | 部署到 Cloud Run | GCP 模組 |

> 詳細升級計畫見 [docs/upgrade_plan.md](../../docs/upgrade_plan.md)
