# {專案名稱}

> LLM × DE MVP Builder 實戰工作坊 — 個人作品

## 題目與目標

- **情境**：{一句話描述業務情境，例如「零售集團想從 10 萬筆交易中找出暢銷商品和高價值客戶」}
- **解決問題**：{客戶的具體痛點，例如「交易資料沒人分析，不知道哪些商品該補貨」}
- **使用者**：{誰會看產出，例如「營運經理，每週看報告決定進貨策略」}
- **你的角色**：資料解決方案顧問
- **資料來源**：{來源名稱 + URL}

## 資料說明

| 檔案 | 筆數 | 說明 | 來源 |
|------|------|------|------|
| {xxx.csv} | {N} 筆 | {主要欄位} | {Kaggle / 政府開放資料} |

### 主要欄位

| 欄位 | 型別 | 說明 |
|------|------|------|
| {欄位名} | {str/int/float} | {代表什麼} |

## Pipeline 架構（Medallion Architecture）

```
CSV → Extract → Bronze (raw 表) → Transform → Silver (cleaned 表) → LLM → Gold (analyzed 表)
                                                                       ↓
                                                       SQL 統計 → processed/*.csv
                                                       LLM 報告 → output/report.md
                                                       FastAPI  → API endpoint
                                                       Streamlit → Dashboard
```

### 各階段

| 階段 | 做了什麼 | Medallion 層 |
|------|---------|------------|
| **Extract** | {讀了什麼資料} | |
| **Load** | {寫入 SQLite raw 表} | Bronze |
| **Transform** | {清洗：去空值/轉日期/算新欄位/合併表} | Silver |
| **SQL 統計** | {GROUP BY / 排行 / 交叉分析} | Silver → 分析 |
| **LLM 分析** | {分類/摘要/建議，用什麼 prompt} | Gold |
| **報告** | {report.md 主要結論} | Gold → 產出 |
| **FastAPI** | {定義了哪些 endpoint} | Data Product |
| **Dashboard** | {呈現什麼圖表} | Data Product |

## Data Quality 處理

| 問題 | 處理方式 | 影響 |
|------|---------|------|
| {缺漏值} | {dropna(subset=[...])} | {刪除 N 筆} |
| {型別錯誤} | {pd.to_numeric(errors="coerce")} | {N 筆轉失敗} |

## 如何執行

```bash
cd data/raw/topic_{N}
jupyter notebook pipeline_starter.ipynb
# 或上傳到 Google Colab
```

### 選做：FastAPI + Streamlit

```bash
pip install fastapi uvicorn streamlit
uvicorn api:app --reload --port 8000    # Terminal 1
streamlit run app.py                     # Terminal 2
```

## 產出

| 產出 | 路徑 | 說明 |
|------|------|------|
| SQLite 資料庫 | `pipeline.db` | Bronze / Silver / Gold 三表 |
| 統計結果 | `processed/*.csv` | {列出 CSV} |
| 分析報告 | `output/report.md` | {主要結論} |
| API | `api.py` | {endpoint 列表} |
| Dashboard | `app.py` | {圖表說明} |

## 關鍵發現

1. {發現 1，附具體數字}
2. {發現 2，附具體數字}
3. {發現 3，附具體數字}

## LLM 使用紀錄

| 用途 | 模型 | Prompt 重點 | 結果品質 |
|------|------|-----------|---------|
| {品類分類} | {GPT-4o-mini / fallback} | {標籤選項} | {準確率} |

## 技術選型與取捨

| 決策 | 選了什麼 | 為什麼 | 升級後 |
|------|---------|--------|--------|
| 資料庫 | SQLite | 零安裝、Colab 內建 | BigQuery |
| 轉換 | pandas | 已學、直覺 | dbt |
| 排程 | 手動 | 期中先求能跑 | Airflow |
| 部署 | 本地 | 期中不要求 | Docker + GCP |

## 後續升級計畫

| 階段 | 升級內容 | 對應課程 | 業界工具 |
|------|---------|---------|---------|
| 後續進階課程 | 拆成正式 ETL 架構 | 帶狀課 | |
| Docker | 容器化 pipeline | Docker 模組 | Docker Compose |
| Airflow | 改成 DAG 排程 | Airflow 模組 | Dagster / Prefect |
| 資料庫 | SQLite → 正式 DB | 資料庫模組 | Snowflake / BigQuery |
| GCP | 雲端部署 | GCP 模組 | Cloud Run |

> 詳細：[docs/upgrade_plan.md](../../docs/upgrade_plan.md)

## 我學到什麼

- {例如「Medallion Architecture 讓資料分層管理，出問題可回到 Bronze 重跑」}
- {例如「LLM 做分類前要先跑 1 筆測試確認 prompt 有效」}
- {例如「SQL GROUP BY 比 pandas 更適合做聚合統計」}
- {其他}
