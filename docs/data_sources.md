# 期中 MVP 資料來源說明

> 每題的 sample CSV 由講師從原始來源預先下載並取樣，放在 `data/raw/topic_{N}/` 供學員直接使用。
> 學員不需自行下載原始資料，Colab 直接讀 repo 內的 CSV 即可。

---

## 題目 1：餐飲連鎖 POS 庫存優化

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_1/reviews.csv` |
| **筆數** | 2,000 筆（從 10,000 筆取樣） |
| **來源** | Kaggle — [10000 Restaurant Reviews](https://www.kaggle.com/datasets/joebeachcapital/restaurant-reviews) |
| **授權** | CC0: Public Domain |
| **欄位** | `Restaurant`（餐廳名）, `Reviewer`（評論者）, `Review`（評論文字）, `Rating`（評分）, `Time`（時間） |
| **ETL 用途** | 評分統計、餐廳排行、時間趨勢 |
| **LLM 用途** | 評論主題分類（服務/餐點/價格/環境）、情緒分析、營運建議摘要 |

---

## 題目 2：B2C 電商競品比價追蹤

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_2/products.csv` |
| **筆數** | 4,386 筆（Amazon × Flipkart 用 ISBN 合併） |
| **來源** | Kaggle — [Amazon vs Flipkart Book Prices](https://www.kaggle.com/datasets/mandan/amazon-vs-flipkart-book-prices) |
| **授權** | CC BY 4.0 |
| **欄位** | `isbn`, `title`（書名）, `author`（作者）, `amazon_price`, `amazon_rating`, `flipkart_price`, `flipkart_rating` |
| **ETL 用途** | 跨平台價差計算、品類統計、異常價差偵測 |
| **LLM 用途** | 競品摘要生成、價差原因分析、商品賣點比較 |

---

## 題目 3：數位金融客訴效率分析

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_3/complaints.csv` |
| **筆數** | 2,000 筆（從 690 萬筆取樣，僅含有文字敘述的客訴） |
| **來源** | Kaggle — [Consumer Complaint Dataset](https://www.kaggle.com/datasets/namigabbasov/consumer-complaint-dataset)（原始資料來自 [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)） |
| **授權** | 美國政府公開資料 |
| **欄位** | `narrative`（客訴文字）, `Product`（產品類別）, `date`（日期）, `Issue`（問題類型）, `Sub-issue`, `Company`（公司）, `State`（州）, `timely_response`（是否及時回應） |
| **ETL 用途** | 客訴類別統計、處理時間分析、各公司/州別比較 |
| **LLM 用途** | 情緒分析、自動分類、優先排序理由生成 |

---

## 題目 4：音樂串流趨勢分析

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_4/tracks.csv` |
| **筆數** | 4,600 筆 |
| **來源** | Kaggle — [Most Streamed Spotify Songs 2024](https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024) |
| **授權** | CC0: Public Domain |
| **欄位** | `Track`（歌名）, `Album Name`, `Artist`（藝人）, `Release Date`, `All Time Rank`, `Track Score`, `Spotify Streams`（播放量）, `Spotify Playlist Count`, `YouTube Views`, `TikTok Posts` 等 30 欄 |
| **ETL 用途** | 播放量排行、藝人/曲風統計、跨平台比較 |
| **LLM 用途** | 聽眾洞察生成、推薦歌單文案、趨勢摘要 |

---

## 題目 5：叫車服務交通熱點分析

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_5/trips.csv` + `taxi_zone_lookup.csv` |
| **筆數** | 2,000 筆（從 296 萬筆取樣，2024 年 1 月） |
| **來源** | [NYC TLC Yellow Taxi Trip Records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)（官方公開資料，不需註冊） |
| **授權** | 美國政府公開資料 |
| **trips.csv 欄位** | `VendorID`, `tpep_pickup_datetime`（上車時間）, `tpep_dropoff_datetime`（下車時間）, `passenger_count`, `trip_distance`（里程）, `PULocationID`（上車區域碼）, `DOLocationID`（下車區域碼）, `fare_amount`（車資）, `tip_amount`（小費）, `total_amount` 等 19 欄 |
| **taxi_zone_lookup.csv** | `LocationID` → `Borough`（行政區）+ `Zone`（地區名）對照表 |
| **ETL 用途** | 熱點區域統計、尖峰時段分析、平均車資/里程 |
| **LLM 用途** | 交通模式解讀、司機調度建議生成 |

---

## 題目 6：求職媒合職缺洞察

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_6/jobs.csv` |
| **筆數** | 2,000 筆（從 12,217 筆合併取樣） |
| **來源** | Kaggle — [Data Science Job Postings & Skills 2024](https://www.kaggle.com/datasets/asaniczka/data-science-job-postings-and-skills) |
| **授權** | CC BY 4.0 |
| **欄位** | `job_title`（職稱）, `company`（公司）, `job_location`（地點）, `job_level`（等級）, `job_type`（類型）, `job_skills`（技能需求） |
| **ETL 用途** | 技能出現頻率、職缺分類統計、地區/等級分佈 |
| **LLM 用途** | 職缺摘要生成、技能補強建議、履歷匹配分析 |

---

## 題目 7：媒體業新聞輿情監測

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_7/news.csv` |
| **筆數** | 2,000 筆（從 209,527 筆取樣） |
| **來源** | Kaggle — [News Category Dataset](https://www.kaggle.com/datasets/rmisra/news-category-dataset)（HuffPost 新聞，2012-2022） |
| **授權** | CC BY 4.0 |
| **欄位** | `headline`（標題）, `category`（類別，42 種）, `short_description`（摘要）, `authors`（作者）, `date`（日期）, `link`（連結） |
| **ETL 用途** | 類別分佈統計、來源/時間趨勢、關鍵字頻率 |
| **LLM 用途** | 新聞摘要生成、情緒/立場分類、輿情重點整理 |

---

## 題目 8：不動產房價趨勢分析

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_8/real_estate.csv` |
| **筆數** | 2,000 筆（合併台北/新北/台中/高雄/桃園/新竹縣市取樣） |
| **來源** | [內政部不動產成交案件實際資訊資料供應系統](https://plvr.land.moi.gov.tw/DownloadOpenData) + [政府資料開放平臺](https://data.gov.tw/dataset/25119)（不需註冊，直接下載） |
| **授權** | 政府資料開放授權條款 |
| **欄位** | `鄉鎮市區`, `交易標的`, `土地位置建物門牌`, `交易年月日`（民國年格式）, `建物型態`, `總樓層數`, `建物移轉總面積平方公尺`, `總價元`, `單價元平方公尺`, `建築完成年月`, `縣市` 等 33 欄 |
| **ETL 用途** | 區域均價統計、交易量趨勢、屋齡/類型分析（注意：日期為民國年格式需轉換） |
| **LLM 用途** | 區域分析建議書生成、買方提醒、資料限制說明 |

---

## 注意事項

1. **所有 sample CSV 由講師預先處理**：學員直接 `pd.read_csv()` 即可使用
2. **Kaggle 來源**：需 Kaggle 帳號才能從原始連結下載完整資料；本 repo 已附 sample，學員不需另外下載
3. **大資料集已取樣**：題 3（690 萬→2,000）、題 5（296 萬→2,000）、題 7（21 萬→2,000）、題 8（5,578→2,000）
4. **題 8 日期格式**：民國年（如 `1130101` = 民國 113 年 1 月 1 日），需轉換成西元年
5. **題 5 區域碼**：`PULocationID` / `DOLocationID` 需搭配 `taxi_zone_lookup.csv` 對照地名
