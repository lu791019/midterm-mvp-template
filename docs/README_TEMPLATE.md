# {專案名稱} — Pipeline Documentation

> LLM × DE MVP Builder 實戰工作坊 — 個人作品

---

## 1. Overview

| 項目 | 內容 |
|------|------|
| **業務情境** | {一句話，例如「零售集團需要從交易資料中自動產出商品分析」} |
| **Pipeline 目標** | {Pipeline 做什麼，例如「每日匯入交易 CSV → 清洗 → 統計 → LLM 分類 → API 供出去」} |
| **使用者** | {誰使用這條 Pipeline 的產出，例如「營運經理透過 API 查詢商品排行」} |
| **資料來源** | {來源名稱 + URL} |
| **資料量** | {N 筆，M 個欄位} |

---

## 2. Architecture / Data Flow

```
{資料來源} → Extract → [raw 表] → Transform → [cleaned 表] → LLM/Enrich → [analyzed 表]
                                                    ↓                            ↓
                                             統計 CSV (processed/)         report (output/)
                                                                               ↓
                                                                        FastAPI (api.py)
```

| 階段 | 輸入 | 處理 | 輸出 | 對應 Section |
|------|------|------|------|-------------|
| Extract | {CSV 檔名} | `pd.read_csv()` | `raw_*` 表 | Section 1 |
| Transform | `raw_*` 表 | {清洗邏輯摘要} | `cleaned_*` 表 | Section 2 |
| Statistics | `cleaned_*` 表 | {SQL / pandas 查詢} | `processed/*.csv` | Section 3 |
| LLM Enrich | `cleaned_*` 表 | {LLM API / fallback} | `analyzed_*` 表 | Section 4 |
| Serve | `pipeline.db` | FastAPI | REST API | Section 8 |

---

## 3. Data Dictionary

### raw_{表名}（Bronze）

> 原始資料，未做任何處理。

| # | 欄位 | 型別 | 說明 | 範例值 |
|---|------|------|------|--------|
| 1 | {欄位名} | {str/int/float/datetime} | {代表什麼} | {一個範例} |
| 2 | | | | |
| ... | | | | |

### cleaned_{表名}（Silver）

> 清洗後資料。

| # | 欄位 | 型別 | 說明 | 來自 | 備註 |
|---|------|------|------|------|------|
| 1 | {欄位名} | {型別} | {說明} | raw.{原欄位} | |
| N+1 | {新增欄位} | {型別} | {計算邏輯} | 計算產生 | {例如 total_amount = quantity × price} |

### analyzed_{表名}（Gold）

> LLM 或 fallback 分析結果。

| # | 欄位 | 型別 | 說明 | 產生方式 |
|---|------|------|------|---------|
| * | （繼承 cleaned 全部欄位） | | | |
| N+1 | category | str | {分類標籤} | LLM / fallback |
| N+2 | llm_insight | str | {分析洞察} | LLM / fallback |

---

## 4. Transform Logic

| 步驟 | 程式碼 | 理由 | 影響筆數 |
|------|--------|------|---------|
| 去缺值 | `df.dropna(subset=[{欄位}])` | {為什麼這些欄位不能為空} | -{N} 筆 |
| 型別轉換 | `pd.to_datetime({欄位})` | {為什麼要轉} | 0 |
| 過濾異常 | `df[df[{欄位}] > 0]` | {為什麼這些值不合理} | -{N} 筆 |
| 新增欄位 | `df[{新欄位}] = {計算}` | {業務邏輯} | 0 |

**筆數追蹤**：raw {N} 筆 → cleaned {N} 筆（清除 {N} 筆，{X}%）→ analyzed {N} 筆

---

## 5. Data Quality

| 維度 | 檢查方式 | 結果 |
|------|---------|------|
| 完整性 | `df.isnull().sum()` | {哪些欄位有缺，多少比例} |
| 一致性 | `df.dtypes` | {有沒有型別不一致} |
| 準確性 | `df.describe()` | {有沒有不合理的值} |

---

## 6. LLM Integration

| 項目 | 內容 |
|------|------|
| **模型** | {GPT-4o-mini / fallback 規則版} |
| **輸入** | {哪個欄位的文字} |
| **Prompt 策略** | {固定標籤 + JSON 回傳 + 不確定選最接近的} |
| **輸出欄位** | `category`（{標籤列表}）、`llm_insight` |
| **Fallback** | {關鍵字規則：如果含 X 就分類為 Y} |
| **處理筆數** | {N} 筆，耗時約 {M} 秒 |

---

## 7. API Endpoints

| Method | Path | 說明 | 回傳 |
|--------|------|------|------|
| GET | `/health` | 確認 API + DB 狀態 | `{status, tables}` |
| GET | `/stats/...` | {統計查詢} | `[{records}]` |
| GET | `/analyzed` | LLM 分析結果 | `[{records}]` |
| GET | `/summary` | 三表摘要統計 | `{table: count}` |
| GET | `/report` | Pipeline 文件 | `{report: text}` |

---

## 8. How to Run

```bash
# 1. 環境
cd data/raw/topic_{N}
pip install pandas fastapi uvicorn

# 2. 跑 Pipeline
jupyter notebook pipeline_starter.ipynb
# 或上傳到 Google Colab（Section 0 自動設定環境）

# 3. 驗證產出
ls pipeline.db processed/ output/

# 4. 跑 API
uvicorn api:app --reload --port 8000
# 開瀏覽器 http://localhost:8000/health
```

---

## 9. Design Decisions

| 決策 | 選了什麼 | 為什麼 | Trade-off | 升級方向 |
|------|---------|--------|-----------|---------|
| 儲存 | SQLite | 零安裝、Colab 內建 | 不支援並發寫入 | BigQuery |
| 轉換 | pandas | 已學、直覺 | 大資料量慢 | dbt |
| LLM | {API/fallback} | {理由} | {限制} | {升級} |
| 排程 | 手動 | MVP 先求能跑 | 不可重複執行 | Airflow |
| 部署 | 本地 | 期中不要求 | 只有自己能用 | Docker + GCP |

---

## 10. Known Limitations & Next Steps

**目前限制**：
- {例如「只處理前 50 筆 LLM 分析，完整版需跑全部」}
- {例如「API 只能本地跑，無法對外存取」}

**下一步**：
| 階段 | 升級內容 | 業界工具 |
|------|---------|---------|
| 帶狀課 | 拆成正式 ETL 架構 | Python module/package |
| Docker | 容器化 pipeline | Docker Compose |
| Airflow | 改成 DAG 排程 | Airflow / Dagster |
| 資料庫 | SQLite → 正式 DB | BigQuery / Cloud SQL |
| GCP | 雲端部署 | Cloud Run / Composer |
