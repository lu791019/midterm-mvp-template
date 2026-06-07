# Midterm MVP Topic Catalog

> 目標：8 個題目都能被學員選用。每題都要能在期中活動內完成最低版本：取得資料 → 清洗轉換 → LLM 加值 → 輸出報告或展示。

## 題目可行性標準

每個題目開放前都要符合：

- 有講師預備資料，避免現場 API / 網路失敗。
- 最低版本可在 30-60 分鐘內完成 ETL。
- LLM 加值不是硬湊，必須能產生分類、摘要、洞察或建議。
- 最後輸出可以用 `output/report.md`、processed CSV、Streamlit 或截圖展示。
- 可在 EP01 後升級成 GitHub / Docker / Airflow / GCP 版本。

## 8 題總覽

| # | 題目 | 建議資料來源 | 最低輸出 | LLM 加值 | 風險 |
|---|---|---|---|---|---|
| 1 | 餐飲連鎖 POS 庫存優化 | 模擬 POS CSV + 顧客評論；可參考 Kaggle / UCI Online Retail | 銷售排行、庫存風險表、評論分類 | 顧客評論主題 / 情緒標籤、補貨建議摘要 | 低 |
| 2 | B2C 電商競品比價追蹤 | 講師預備商品 CSV；公開頁爬取作進階 | 價格比較表、異常價差、品牌摘要 | 競品摘要、商品賣點比較 | 中 |
| 3 | 數位金融客訴效率分析 | 模擬客訴工單；可參考 CFPB / Kaggle complaint data | 客訴類別、優先級、處理時間統計 | 情緒分析、自動分類、優先排序理由 | 低 |
| 4 | 音樂串流趨勢分析 | Spotify Charts CSV、KKBOX / Kaggle 類似資料 | 熱門歌曲 / 藝人排行、趨勢摘要 | 聽眾洞察、推薦摘要、歌單說明 | 低-中 |
| 5 | 叫車服務交通熱點分析 | NYC TLC sample CSV、Uber Movement 參考資料 | 熱點區域、尖峰時段、平均車程 | 交通模式解讀、營運建議 | 中 |
| 6 | 求職媒合職缺洞察 | 模擬職缺 CSV；104 / CakeResume 公開頁作進階 | 技能需求排行、職缺分類、薪資區間 | 職缺摘要、技能熱度、履歷匹配建議 | 中 |
| 7 | 媒體業新聞輿情監測 | RSS / NewsAPI；講師預備新聞 CSV fallback | 新聞分類、來源統計、關鍵字排行 | 新聞摘要、情緒追蹤、輿情重點 | 中-高 |
| 8 | 不動產房價趨勢分析 | 實價登錄 sample CSV、data.gov.tw 資料 | 區域均價、交易量、物件類型統計 | 區域分析建議書、買方提醒 | 中 |

## 題目 1：餐飲連鎖 POS 庫存優化

**MVP 問題**：哪些商品可能熱賣但庫存不足？顧客評論透露哪些營運問題？

**資料**
- `orders.csv`：訂單、商品、數量、金額、日期
- `inventory.csv`：商品、目前庫存、安全庫存
- `reviews.csv`：顧客評論

**ETL**
- Extract：讀取訂單、庫存、評論 CSV
- Transform：計算銷售量、庫存風險、評論文字欄位
- Load：輸出 `processed_inventory_risk.csv` 與 `report.md`

**LLM 加值**
- 將評論分類為服務、餐點、價格、環境、其他
- 產生補貨與營運建議摘要

## 題目 2：B2C 電商競品比價追蹤

**MVP 問題**：哪些商品在競品平台有明顯價差？應優先追蹤哪些品類？

**資料**
- `products.csv`：商品名稱、品牌、品類、平台、價格、評分
- 進階可改成公開頁爬蟲，但期中最低版用講師 CSV

**ETL**
- Extract：讀取商品價格資料
- Transform：依商品 / 品牌比價，計算最低價、最高價、價差
- Load：輸出 `price_gap.csv` 與 `report.md`

**LLM 加值**
- 生成競品摘要
- 解釋價格差異可能代表的營運意義

## 題目 3：數位金融客訴效率分析

**MVP 問題**：哪些客訴最急？哪些問題最常出現？客服應優先處理什麼？

**資料**
- `complaints.csv`：客訴時間、產品、文字內容、狀態、處理天數

**ETL**
- Extract：讀取客訴資料
- Transform：計算類別統計、處理時間、未結案比例
- Load：輸出 `complaint_summary.csv` 與 `report.md`

**LLM 加值**
- 情緒分析
- 自動分類
- 優先級理由

## 題目 4：音樂串流趨勢分析

**MVP 問題**：近期熱門歌曲 / 藝人有哪些趨勢？可以如何生成推薦摘要？

**資料**
- `tracks.csv`：歌曲、藝人、播放量、排名、日期、曲風

**ETL**
- Extract：讀取排行榜資料
- Transform：排行變化、播放量統計、藝人 / 曲風聚合
- Load：輸出 `music_trends.csv` 與 `report.md`

**LLM 加值**
- 生成聽眾洞察
- 產出推薦歌單描述

## 題目 5：叫車服務交通熱點分析

**MVP 問題**：哪些時段與地區叫車需求最高？營運上可以如何調度？

**資料**
- `trips.csv`：上車區、下車區、時間、車程、費用

**ETL**
- Extract：讀取 trip sample
- Transform：依時段 / 區域統計需求量與平均費用
- Load：輸出 `traffic_hotspots.csv` 與 `report.md`

**LLM 加值**
- 解讀熱點與尖峰時段
- 生成司機調度建議

## 題目 6：求職媒合職缺洞察

**MVP 問題**：哪些技能最常被要求？求職者應該優先補強什麼？

**資料**
- `jobs.csv`：職稱、公司、技能、薪資區間、職缺描述

**ETL**
- Extract：讀取職缺資料
- Transform：技能拆分、技能出現頻率、職缺分類
- Load：輸出 `skill_demand.csv` 與 `report.md`

**LLM 加值**
- 摘要職缺需求
- 產生技能補強建議
- 進階：履歷與職缺匹配

## 題目 7：媒體業新聞輿情監測

**MVP 問題**：某議題近期新聞如何被報導？情緒與主題分布如何？

**資料**
- 最低版：講師預備 `news.csv`
- 進階版：RSS / NewsAPI

**ETL**
- Extract：讀取新聞標題、來源、日期、摘要
- Transform：來源統計、關鍵字、日期聚合
- Load：輸出 `news_monitor.csv` 與 `report.md`

**LLM 加值**
- 新聞摘要
- 情緒 / 立場分類
- 輿情重點整理

**風險**
- API key / RSS 連線不穩，因此必須準備 CSV fallback。

## 題目 8：不動產房價趨勢分析

**MVP 問題**：不同區域房價與交易量有什麼差異？可以給買方什麼提醒？

**資料**
- `real_estate.csv`：區域、交易年月、總價、坪數、單價、屋齡、建物型態

**ETL**
- Extract：讀取實價登錄 sample
- Transform：區域均價、交易量、屋齡 / 類型統計
- Load：輸出 `real_estate_summary.csv` 與 `report.md`

**LLM 加值**
- 生成區域分析建議書
- 指出資料限制與買方應再確認的資訊

## Demo 最低格式

每題最後至少要能回答：

1. 我的題目解決什麼問題？
2. 我的資料從哪裡來？
3. 我做了哪些清洗與轉換？
4. LLM 在 pipeline 中做了什麼？
5. 最後輸出什麼？
6. 下一步要如何用 Docker / Airflow / GCP 升級？
