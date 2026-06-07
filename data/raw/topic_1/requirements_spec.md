# 題目 1：餐飲連鎖 POS 庫存優化

## 情境

你是一家餐飲連鎖集團的資料顧問。老闆說：「我們有很多門店的顧客評論，但沒人在看。我想知道客人到底在抱怨什麼、哪些門店口碑最好、還有什麼趨勢我們該注意的。」

## 你的角色

餐飲集團資料顧問

## 使用者

餐飲連鎖集團營運經理——每週看一次報告，決定哪些門店要改善、哪些做法要推廣。

## 資料來源

| 檔案 | 筆數 | 說明 | 來源 |
|------|------|------|------|
| `reviews.csv` | 2,000 | 餐廳顧客評論（含評分、文字、時間） | [Kaggle: 10000 Restaurant Reviews](https://www.kaggle.com/datasets/joebeachcapital/restaurant-reviews) |

### 欄位說明

| 欄位 | 型別 | 說明 |
|------|------|------|
| `Restaurant` | str | 餐廳名稱 |
| `Reviewer` | str | 評論者名稱 |
| `Review` | str | 評論文字（英文） |
| `Rating` | int | 評分（1-5） |
| `Time` | str | 評論時間 |

## 今日 MVP Scope

### ETL（pandas 清洗 + 統計）

- 處理缺漏值（Rating 為空、Review 為空）
- 時間欄位轉成 datetime
- 統計：各餐廳平均評分、評論數、低評分（≤2）佔比
- 產出 `data/processed/restaurant_stats.csv`

### LLM（AI 加值分析）

- 對每筆 Review 文字做**主題分類**：服務 / 餐點 / 價格 / 環境 / 其他
- 對每筆 Review 做**情緒分析**：正面 / 負面 / 中性
- 生成顧問報告：「評分最低的餐廳，評論中反映的主要問題是什麼？建議優先改善什麼？」

## 預期產出

- `data/processed/restaurant_stats.csv`：各餐廳統計摘要
- `data/processed/reviews_analyzed.csv`：每筆評論 + LLM 分類結果
- `output/report.md`：顧問分析報告

## 成功指標

- 能說出「評分最低的 3 家餐廳，最常被提到的問題類別是什麼」
- LLM 分類結果可被人類理解且大致合理
