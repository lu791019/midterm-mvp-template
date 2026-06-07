# 期中 MVP 資料來源說明

> 每題的 sample CSV 由講師從原始來源預先下載並取樣（各 2,000 筆），放在 `data/raw/topic_{N}/` 供學員直接使用。
> 學員不需自行下載原始資料，Colab 直接讀 repo 內的 CSV 即可。

---

## 題目 1：零售 POS 銷售分析

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_1/orders.csv` |
| **筆數** | 2,000 筆（從 106 萬筆取樣） |
| **來源** | [Kaggle: Online Retail II UCI](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci) |
| **授權** | CC BY 4.0 |
| **欄位** | `invoice_id`（發票編號）, `stock_code`（商品代碼）, `description`（商品描述）, `quantity`（數量）, `invoice_date`（交易日期）, `unit_price`（單價）, `customer_id`（客戶編號）, `country`（國家）, `total_amount`（總金額） |
| **ETL 用途** | 銷售排行、客戶分析、時間趨勢、各國比較 |
| **LLM 用途** | 商品品類自動分類、客戶洞察、庫存建議 |

---

## 題目 2：B2C 電商競品比價追蹤

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_2/products.csv` |
| **筆數** | 2,000 筆（從 4,386 筆取樣，Amazon × Flipkart 用 ISBN 合併） |
| **來源** | [Kaggle: Amazon vs Flipkart Book Prices](https://www.kaggle.com/datasets/mandan/amazon-vs-flipkart-book-prices) |
| **授權** | CC BY 4.0 |
| **欄位** | `isbn`, `title`（書名）, `author`（作者）, `amazon_price`, `amazon_rating`, `flipkart_price`, `flipkart_rating` |
| **ETL 用途** | 跨平台價差計算、異常價差偵測、品類統計 |
| **LLM 用途** | 書籍品類分類、競品摘要、定價建議 |

---

## 題目 3：音樂串流趨勢分析

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_3/tracks.csv` |
| **筆數** | 2,000 筆（從 4,600 筆取樣） |
| **來源** | [Kaggle: Most Streamed Spotify Songs 2024](https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024) |
| **授權** | CC0: Public Domain |
| **欄位** | `Track`（歌名）, `Artist`（藝人）, `Album Name`, `Release Date`, `All Time Rank`, `Spotify Streams`, `YouTube Views`, `TikTok Posts` 等 29 欄 |
| **ETL 用途** | 播放量排行、藝人統計、跨平台比較 |
| **LLM 用途** | 曲風分類、聽眾洞察、推薦歌單文案 |

---

## 題目 4：叫車服務交通熱點分析

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_4/trips.csv` + `taxi_zone_lookup.csv` |
| **筆數** | 2,000 筆（從 296 萬筆取樣，2024 年 1 月） |
| **來源** | [NYC TLC Yellow Taxi Trip Records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)（官方公開資料，不需註冊） |
| **授權** | 美國政府公開資料 |
| **trips.csv 欄位** | `tpep_pickup_datetime`（上車時間）, `tpep_dropoff_datetime`（下車時間）, `passenger_count`, `trip_distance`, `PULocationID`（上車區域碼）, `DOLocationID`, `fare_amount`, `tip_amount`, `total_amount` 等 19 欄 |
| **taxi_zone_lookup.csv** | `LocationID` → `Borough`（行政區）+ `Zone`（地區名）對照表 |
| **ETL 用途** | 熱點區域統計、尖峰時段分析、合併地名（merge） |
| **LLM 用途** | 區域分類、交通模式解讀、司機調度建議 |

---

## 題目 5：求職媒合薪資洞察

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_5/jobs.csv` |
| **筆數** | 2,000 筆（從 14,199 筆取樣） |
| **來源** | [Kaggle: Jobs and Salaries in Data Field 2024](https://www.kaggle.com/datasets/murilozangari/jobs-and-salaries-in-data-field-2024) |
| **授權** | CC BY 4.0 |
| **欄位** | `work_year`（年份）, `experience_level`, `employment_type`, `job_title`, `salary_in_usd`, `work_setting`（Remote/In-person/Hybrid）, `company_size`, `job_category` 等 12 欄 |
| **ETL 用途** | 薪資統計、經驗等級比較、工作模式分析 |
| **LLM 用途** | 職位分類、薪資洞察、職涯建議 |

---

## 題目 6：不動產房價趨勢分析

| 項目 | 說明 |
|------|------|
| **檔案** | `data/raw/topic_6/real_estate.csv` |
| **筆數** | 2,000 筆（合併台北/新北/台中/高雄/桃園/新竹取樣） |
| **來源** | [內政部實價登錄](https://plvr.land.moi.gov.tw/DownloadOpenData) + [政府資料開放平臺](https://data.gov.tw/dataset/25119)（不需註冊） |
| **授權** | 政府資料開放授權條款 |
| **欄位** | `縣市`, `鄉鎮市區`, `交易年月日`（民國年）, `建物型態`, `建物移轉總面積平方公尺`, `總價元`, `單價元平方公尺` 等 34 欄 |
| **ETL 用途** | 區域均價、交易量、屋齡分析（注意：民國年需轉換） |
| **LLM 用途** | 區域分類、分析建議書、買方提醒 |

---

## 注意事項

1. **所有 sample CSV 由講師預先處理**，學員直接 `pd.read_csv()` 即可
2. **Kaggle 來源**：需 Kaggle 帳號才能從原始連結下載完整資料；本 repo 已附 sample
3. **題 4 區域碼**：`PULocationID` 需搭配 `taxi_zone_lookup.csv` 對照地名
4. **題 6 日期格式**：民國年（如 `1130101` = 民國 113 年 1 月 1 日），需轉換成西元年
5. **題 3 數值欄位**：Spotify Streams 等欄位含逗號，需去逗號轉數字
