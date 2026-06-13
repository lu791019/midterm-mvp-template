# 題目 1：餐飲連鎖 POS 庫存優化

## 情境

你是一家零售連鎖集團的資料顧問。老闆說：「我們有大量的銷售交易紀錄，但沒人在分析。我想知道哪些商品最暢銷、哪些客戶最有價值、各國市場表現如何，還有庫存該怎麼調配。」

## 你的角色

零售集團資料顧問

## 使用者

零售連鎖集團營運經理——每週看報告，決定進貨策略和行銷重點。

## 資料來源

| 檔案 | 筆數 | 說明 | 來源 |
|------|------|------|------|
| `orders.csv` | 2,000 | 零售交易紀錄（含品項、數量、金額、客戶、國家） | [Kaggle: Online Retail II UCI](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci) |

### 欄位說明

| 欄位 | 型別 | 說明 |
|------|------|------|
| `invoice_id` | int | 發票編號 |
| `stock_code` | str | 商品代碼 |
| `description` | str | 商品描述（英文） |
| `quantity` | int | 購買數量 |
| `invoice_date` | str | 交易日期時間 |
| `unit_price` | float | 單價 |
| `customer_id` | float | 客戶編號 |
| `country` | str | 客戶所在國家 |
| `total_amount` | float | 總金額（quantity × unit_price） |

## 今日 MVP Scope

### ETL（pandas 清洗 + 統計）

- 日期轉 datetime，提取年、月、星期幾、小時
- 處理缺漏值（description 空值、customer_id 空值）
- 統計：商品銷售排行 Top 20、客戶消費金額排行、各國銷售佔比
- 時間趨勢：每月/每日銷售額、尖峰時段
- 產出 `data/processed/sales_stats.csv`

### LLM（AI 加值分析）

- 對商品 description 做**品類自動分類**（家飾/禮品/餐具/季節商品/其他）
- 對 Top 客戶生成**客戶洞察摘要**：「這位客戶偏好什麼品類？消費模式如何？」
- 生成顧問報告：「本月暢銷品類、庫存建議、高價值客戶維護策略」

## 預期產出

- `data/processed/sales_stats.csv`：銷售統計摘要
- `data/processed/orders_analyzed.csv`：每筆訂單 + LLM 品類分類
- `output/pipeline_doc.md`：銷售分析與庫存建議報告

## 成功指標

- 能說出「銷售額最高的 3 個品類和 3 個國家」
- 庫存建議有數據支撐（不是空話）

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
