# 題目 3：數位金融客訴效率分析

## 情境

你是一家數位金融公司的資料顧問。主管說：「客訴量一直在增加，客服團隊說忙不過來。我需要知道哪些類型的客訴最多、哪些最緊急、客服有沒有及時回應，還有客人到底在氣什麼。」

## 你的角色

金融業資料顧問

## 使用者

客服部門主管——每週看報告，決定人力分配和改善重點。

## 資料來源

| 檔案 | 筆數 | 說明 | 來源 |
|------|------|------|------|
| `complaints.csv` | 2,000 | 金融消費者客訴（含文字敘述） | [Kaggle: Consumer Complaint Dataset](https://www.kaggle.com/datasets/namigabbasov/consumer-complaint-dataset)（原始：[CFPB](https://www.consumerfinance.gov/data-research/consumer-complaints/)） |

### 欄位說明

| 欄位 | 型別 | 說明 |
|------|------|------|
| `narrative` | str | 客訴文字敘述（英文，關鍵欄位） |
| `Product` | str | 產品類別（Credit card、Mortgage 等） |
| `date` | str | 收到日期 |
| `Issue` | str | 問題類型 |
| `Sub-issue` | str | 問題子類型 |
| `Company` | str | 被投訴公司 |
| `State` | str | 州別 |
| `timely_response` | str | 是否及時回應（Yes/No） |

## 今日 MVP Scope

### ETL（pandas 清洗 + 統計）

- 日期轉 datetime，提取月份
- 統計：各 Product 客訴量、各 Issue 佔比、timely_response 比率
- 各公司被投訴次數排行
- 產出 `data/processed/complaint_stats.csv`

### LLM（AI 加值分析）

- 對 narrative 做**情緒分析**：憤怒 / 焦慮 / 失望 / 平靜
- 對 narrative 做**自動分類**（與 Issue 欄位交叉驗證）
- 對情緒最強烈的前 10 筆，生成**優先處理建議**：為什麼這筆最緊急？

## 預期產出

- `data/processed/complaint_stats.csv`：客訴類別統計
- `data/processed/complaints_analyzed.csv`：每筆客訴 + LLM 情緒/分類
- `output/report.md`：客訴分析與優先處理建議報告

## 成功指標

- 能說出「最常見的 3 種客訴類型，及時回應率各是多少」
- LLM 的情緒分析結果和人類直覺大致吻合
