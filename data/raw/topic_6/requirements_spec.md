# 題目 6：求職媒合職缺洞察

## 情境

你是一家求職媒合平台的資料顧問。產品經理說：「我想知道現在市場上最缺什麼技能、哪些職缺最多、資料相關的職位通常要求什麼條件，這樣我們可以幫求職者推薦該補強什麼。」

## 你的角色

人資科技資料顧問

## 使用者

求職媒合平台產品經理——用分析結果設計「技能推薦」功能和「市場趨勢報告」。

## 資料來源

| 檔案 | 筆數 | 說明 | 來源 |
|------|------|------|------|
| `jobs.csv` | 2,000 | 資料科學相關職缺（含技能需求） | [Kaggle: Data Science Job Postings & Skills 2024](https://www.kaggle.com/datasets/asaniczka/data-science-job-postings-and-skills) |

### 欄位說明

| 欄位 | 型別 | 說明 |
|------|------|------|
| `job_title` | str | 職稱（Data Engineer, Data Scientist 等） |
| `company` | str | 公司名稱 |
| `job_location` | str | 工作地點 |
| `job_level` | str | 職級（Entry, Mid, Senior 等） |
| `job_type` | str | 類型（Full-time, Contract 等） |
| `job_skills` | str | 技能需求（逗號分隔的技能列表） |

## 今日 MVP Scope

### ETL（pandas 清洗 + 統計）

- 處理 job_skills 欄位（逗號分隔 → 展開成個別技能）
- 統計：技能出現頻率 Top 20、職稱分佈、職級分佈、地區分佈
- 交叉分析：不同職稱最常要求的技能差異
- 產出 `data/processed/skill_demand.csv`

### LLM（AI 加值分析）

- 對 Top 10 熱門技能，生成**技能補強建議**：「如果你想當 Data Engineer，最該先學什麼？」
- 對特定職缺描述，生成**職缺摘要**：一句話總結這個職缺在找什麼人
- 生成市場趨勢報告：「目前資料領域最搶手的是什麼角色？」

## 預期產出

- `data/processed/skill_demand.csv`：技能頻率 + 職稱交叉統計
- `output/report.md`：市場趨勢 + 技能建議報告

## 成功指標

- 能說出「資料領域最常被要求的 5 項技能是什麼」
- 技能建議具體、可行動（不是「多學習」這種空話）
