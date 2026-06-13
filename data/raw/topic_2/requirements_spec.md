# 題目 2：B2C 電商競品比價追蹤

## 情境

你是一家電商平台的資料顧問。老闆說：「我們想知道同一本書在 Amazon 和 Flipkart 的價差有多大，哪些書我們定價太高、哪些太低，還有對手的評分是不是比我們好。」

## 你的角色

電商營運資料顧問

## 使用者

電商平台定價經理——每週看一次比價報告，決定哪些商品要調價、哪些品類要重點追蹤。

## 資料來源

| 檔案 | 筆數 | 說明 | 來源 |
|------|------|------|------|
| `products.csv` | 2,000 | Amazon × Flipkart 書籍價格（已用 ISBN 合併） | [Kaggle: Amazon vs Flipkart Book Prices](https://www.kaggle.com/datasets/mandan/amazon-vs-flipkart-book-prices) |

### 欄位說明

| 欄位 | 型別 | 說明 |
|------|------|------|
| `isbn` | str | 國際書號（唯一識別碼） |
| `title` | str | 書名 |
| `author` | str | 作者 |
| `amazon_price` | float | Amazon 售價 |
| `amazon_rating` | float | Amazon 評分 |
| `flipkart_price` | float | Flipkart 售價 |
| `flipkart_rating` | str | Flipkart 評分（注意：可能有空值） |

## 今日 MVP Scope

### ETL（pandas 清洗 + 統計）

- 處理價格欄位（去除貨幣符號、轉數字）
- 處理 flipkart_rating 空值
- 計算價差：`price_diff = amazon_price - flipkart_price`
- 標記異常價差（價差 > 平均價差 2 倍）
- 統計：平均價差、價差最大的 Top 10、各平台評分比較
- 產出 `data/processed/price_comparison.csv`

### LLM（AI 加值分析）

- 對價差最大的 10 本書，生成**競品摘要**：為什麼可能有價差？可能的原因？
- 生成定價建議報告：「哪些書我們定價偏高、哪些偏低、建議調整方向」

## 預期產出

- `data/processed/price_comparison.csv`：含價差、異常標記的完整比較表
- `output/pipeline_doc.md`：競品分析與定價建議報告

## 成功指標

- 能說出「價差最大的 3 本書是什麼，價差多少」
- 能產出一份有商業邏輯的定價建議

---

## 交流引導

### 第一次交流（選題後，5 min）

組員會問你以下問題，看著上面的情境和欄位回答：

1. 你的資料有哪些欄位？哪個欄位你覺得最有分析價值？
2. 你打算怎麼清洗這份資料？預期會遇到什麼問題？
3. 如果只能做一個統計圖表給老闆看，你會做什麼？
4. 這份資料最大的限制是什麼？

### 第二次交流 — 閃電秀預演（準備 Demo 前）

每組派 2~3 人，每人 3 分鐘，向組員說明你等等要 Demo 的內容：

- 我的題目解決什麼問題？
- 我做了哪些清洗和分析？
- 最有趣的發現是什麼？（用數字說）
- LLM 在 pipeline 中做了什麼？

> 交流時可以比正式 Demo 更詳盡，組員給回饋幫你精煉重點。
