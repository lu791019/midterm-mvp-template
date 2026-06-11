# 期中 MVP 題庫

> 6 個題目都能在期中活動內完成最低版本：取得資料 → 清洗轉換 → 寫入 SQLite → SQL 查詢 → LLM 加值 → 輸出報告。

## 題目可行性標準

每個題目都已確認：

- 有講師預備的 2,000 筆 sample CSV，避免現場下載失敗
- 最低版本可在 50 分鐘內完成 ETL
- LLM 加值有明確的分類/摘要/洞察產出
- 有 fallback 規則版（不需 API Key 也能跑）
- 可在後續課程升級成 GitHub / Docker / Airflow / GCP 版本

## 6 題總覽

| # | 題目 | 資料 | 欄位 | 數值欄 | LLM 做什麼 |
|---|------|------|------|--------|-----------|
| 1 | 零售 POS 銷售分析 | orders.csv | 9 | 6 | 品類分類 + 客戶洞察 |
| 2 | B2C 電商競品比價 | products.csv | 7 | 5 | 書籍分類 + 定價建議 |
| 3 | 音樂串流趨勢分析 | tracks.csv | 29 | 12 | 曲風分類 + 推薦文案 |
| 4 | 叫車服務交通熱點 | trips.csv + lookup | 19 | 16 | 區域分類 + 調度建議 |
| 5 | 求職媒合薪資洞察 | jobs.csv | 12 | 3 | 職位分類 + 職涯建議 |
| 6 | 不動產房價趨勢 | real_estate.csv | 34 | 17 | 區域分類 + 分析建議書 |

## 題目 1：零售 POS 銷售分析

**MVP 問題**：哪些商品最暢銷？哪些客戶最有價值？各國市場表現如何？

**資料**：`orders.csv`（invoice_id, stock_code, description, quantity, invoice_date, unit_price, customer_id, country, total_amount）

**ETL**：日期轉換 + 時間特徵、缺漏值處理、銷售排行、各國統計

**LLM**：商品品類自動分類（家飾/禮品/餐具/季節商品/文具/其他）

## 題目 2：B2C 電商競品比價

**MVP 問題**：哪些書在兩平台價差最大？哪個平台整體比較便宜？

**資料**：`products.csv`（isbn, title, author, amazon_price, amazon_rating, flipkart_price, flipkart_rating）

**ETL**：價格轉數字、計算價差和百分比、標記哪平台便宜

**LLM**：書籍品類分類（科技/商業/文學/教育/生活/其他）

## 題目 3：音樂串流趨勢分析

**MVP 問題**：哪些歌 Spotify 最紅？跨平台（YouTube/TikTok）表現有差異嗎？

**資料**：`tracks.csv`（Track, Artist, Release Date, Spotify Streams, YouTube Views, TikTok Posts 等 29 欄）

**ETL**：數值欄位去逗號轉數字、日期轉換、播放量排行、跨平台比較

**LLM**：曲風分類（流行/嘻哈/搖滾/電子/其他）+ 推薦歌單文案

## 題目 4：叫車服務交通熱點

**MVP 問題**：哪些時段、哪些地區叫車最多？怎麼調度司機？

**資料**：`trips.csv`（pickup/dropoff datetime, trip_distance, PULocationID, fare_amount, tip_amount 等 19 欄）+ `taxi_zone_lookup.csv`

**ETL**：日期轉換 + 時間特徵、計算行程時間、合併地名（merge）、過濾異常值

**LLM**：區域分類（商業區/住宅區/交通樞紐/觀光區/其他）+ 調度建議

**難點**：需要 merge 兩張表，是 6 題中 ETL 最複雜的

## 題目 5：求職媒合薪資洞察

**MVP 問題**：資料領域薪資行情如何？Remote 是否影響薪資？哪些職稱最搶手？

**資料**：`jobs.csv`（work_year, experience_level, job_title, salary_in_usd, work_setting, company_size, job_category 等 12 欄）

**ETL**：薪資轉數字、各類別/等級/模式的統計分析

**LLM**：職位分類（工程/分析/科學/管理/其他）+ 職涯建議

## 題目 6：不動產房價趨勢

**MVP 問題**：各縣市房價差多少？什麼類型的房子最多？區域交易量如何？

**資料**：`real_estate.csv`（縣市, 鄉鎮市區, 交易年月日, 建物型態, 總價元, 單價元平方公尺 等 34 欄）

**ETL**：民國年轉西元年、面積轉坪、總價轉萬元、各縣市/區域統計

**LLM**：區域分類（蛋黃區/蛋白區/郊區/新興區/其他）+ 區域分析建議書

**難點**：中文欄位 + 民國年轉換

## Demo 最低格式

每題最後至少要能回答：

1. 我的題目解決什麼問題？
2. 我的資料從哪裡來？
3. 我做了哪些清洗與轉換？
4. LLM 在 pipeline 中做了什麼？
5. 最後輸出什麼？（pipeline.db + processed CSV + pipeline_doc.md）
6. 下一步要如何用 Docker / Airflow / GCP 升級？
