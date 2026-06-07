# 題目 7：媒體業新聞輿情監測

## 情境

你是一家媒體公司的資料顧問。主編說：「我想知道最近什麼議題最熱、各類新聞的情緒走向如何、有沒有值得追蹤的趨勢，這樣我們可以決定下週的報導重點。」

## 你的角色

媒體業資料顧問

## 使用者

媒體公司主編——每週看輿情報告，決定報導方向和專題企劃。

## 資料來源

| 檔案 | 筆數 | 說明 | 來源 |
|------|------|------|------|
| `news.csv` | 2,000 | HuffPost 新聞標題與摘要（2012-2022，42 個類別） | [Kaggle: News Category Dataset](https://www.kaggle.com/datasets/rmisra/news-category-dataset) |

### 欄位說明

| 欄位 | 型別 | 說明 |
|------|------|------|
| `headline` | str | 新聞標題 |
| `short_description` | str | 新聞摘要 |
| `category` | str | 類別（POLITICS, ENTERTAINMENT, WELLNESS 等，共 42 種） |
| `authors` | str | 作者 |
| `date` | str | 發布日期 |
| `link` | str | 原文連結 |

## 今日 MVP Scope

### ETL（pandas 清洗 + 統計）

- 日期轉 datetime，提取年、月
- 統計：各 category 新聞數量排行、每月新聞量趨勢、作者產量 Top 10
- 標題長度分析（是否和 category 有關）
- 產出 `data/processed/news_stats.csv`

### LLM（AI 加值分析）

- 對每筆新聞做**情緒分類**：正面 / 負面 / 中性
- 對特定 category 的新聞做**摘要整理**：「本週 POLITICS 類的 5 大重點」
- 生成輿情報告：「哪些議題正面報導多、哪些負面居多」

## 預期產出

- `data/processed/news_stats.csv`：類別 × 時間統計
- `data/processed/news_analyzed.csv`：每筆新聞 + LLM 情緒標籤
- `output/report.md`：輿情分析 + 報導建議

## 成功指標

- 能說出「新聞量最多的 3 個類別，以及它們的情緒分佈」
- 輿情報告有助主編決定報導方向
