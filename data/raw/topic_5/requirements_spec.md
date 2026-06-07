# 題目 5：求職媒合薪資洞察

## 情境

你是一家求職媒合平台的資料顧問。產品經理說：「我想知道資料領域的薪資行情、不同經驗等級差多少、遠端 vs 進辦公室的薪資差異、哪些職稱最搶手，這樣我們可以幫求職者做職涯建議。」

## 你的角色

人資科技資料顧問

## 使用者

求職媒合平台產品經理——用分析結果設計「薪資參考」和「職涯建議」功能。

## 資料來源

| 檔案 | 筆數 | 說明 | 來源 |
|------|------|------|------|
| `jobs.csv` | 2,000 | 資料領域職缺與薪資（2020-2024，全球） | [Kaggle: Jobs and Salaries in Data Field 2024](https://www.kaggle.com/datasets/murilozangari/jobs-and-salaries-in-data-field-2024) |

### 欄位說明

| 欄位 | 型別 | 說明 |
|------|------|------|
| `work_year` | int | 年份（2020-2024） |
| `experience_level` | str | 經驗等級（Entry-level / Mid-level / Senior / Executive） |
| `employment_type` | str | 雇用類型（Full-time / Part-time / Contract / Freelance） |
| `job_title` | str | 職稱（Data Engineer / Data Scientist / ML Engineer 等） |
| `salary` | int | 原始幣別薪資 |
| `salary_currency` | str | 薪資幣別 |
| `salary_in_usd` | int | 換算成 USD 的年薪 |
| `employee_residence` | str | 員工居住國 |
| `work_setting` | str | 工作模式（Remote / In-person / Hybrid） |
| `company_location` | str | 公司所在國 |
| `company_size` | str | 公司規模（S / M / L） |
| `job_category` | str | 職位類別（Data Engineering / Data Science / ML 等） |

## 今日 MVP Scope

### ETL（pandas 清洗 + 統計）

- 統計：各 job_category 平均薪資、各 experience_level 薪資分佈
- 交叉分析：Remote vs In-person 薪資差異、公司規模 vs 薪資
- 趨勢：2020-2024 各年份薪資變化
- 職稱排行：最常見的 Top 20 職稱、最高薪的 Top 20 職稱
- 產出 `data/processed/salary_stats.csv`

### LLM（AI 加值分析）

- 對各 job_category 的統計結果，生成**薪資洞察**：「Data Engineer 的平均薪資、成長趨勢、競爭力分析」
- 生成**職涯建議**：「如果你是 Entry-level 想進 Data Engineering，應該瞄準什麼樣的公司和地區？」
- 跨維度摘要：「Remote 工作是否薪資較低？什麼類型的職位 Remote 比例最高？」

## 預期產出

- `data/processed/salary_stats.csv`：薪資 × 職稱 × 經驗 × 模式 統計
- `output/report.md`：薪資分析 + 職涯建議報告

## 成功指標

- 能說出「Data Engineer vs Data Scientist 的薪資差異，以及 Remote 是否影響薪資」
- 職涯建議具體、有數據支撐
