# 題目 4：叫車服務交通熱點分析

## 情境

你是一家叫車服務公司的資料顧問。營運主管說：「我想知道哪些時段、哪些地區叫車需求最高，這樣我們可以提前調度司機。還想知道有沒有什麼營運模式值得注意的。」

## 你的角色

交通服務資料顧問

## 使用者

叫車服務營運主管——每天看調度報告，決定司機排班和熱點部署。

## 資料來源

| 檔案 | 筆數 | 說明 | 來源 |
|------|------|------|------|
| `trips.csv` | 2,000 | 紐約市黃色計程車行程（2024 年 1 月取樣） | [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)（官方公開資料） |
| `taxi_zone_lookup.csv` | 265 | 區域碼 → 地名對照表 | 同上 |

### trips.csv 主要欄位

| 欄位 | 型別 | 說明 |
|------|------|------|
| `tpep_pickup_datetime` | datetime | 上車時間 |
| `tpep_dropoff_datetime` | datetime | 下車時間 |
| `passenger_count` | float | 乘客數 |
| `trip_distance` | float | 行程距離（英里） |
| `PULocationID` | int | 上車區域碼（需對照 taxi_zone_lookup） |
| `DOLocationID` | int | 下車區域碼 |
| `fare_amount` | float | 車資 |
| `tip_amount` | float | 小費 |
| `total_amount` | float | 總金額 |

### taxi_zone_lookup.csv 欄位

| 欄位 | 說明 |
|------|------|
| `LocationID` | 區域碼（對應 PU/DOLocationID） |
| `Borough` | 行政區（Manhattan, Brooklyn 等） |
| `Zone` | 地區名稱 |

## 今日 MVP Scope

### ETL（pandas 清洗 + 統計）

- 合併 trips + taxi_zone_lookup，把 LocationID 轉成地名
- 提取小時、星期幾
- 統計：上車熱點 Top 10、尖峰時段分佈、各行政區平均車資
- 計算行程時間（下車-上車）
- 產出 `data/processed/traffic_stats.csv`

### LLM（AI 加值分析）

- 對熱點區域 + 時段組合，生成**交通模式解讀**：為什麼這個地方在這個時段最忙？
- 生成**司機調度建議**：應該在幾點、在哪裡多部署司機？
- 分析小費模式：哪些區域/時段小費比率高？

## 預期產出

- `data/processed/traffic_stats.csv`：區域 × 時段統計
- `output/pipeline_doc.md`：交通模式分析 + 調度建議

## 成功指標

- 能說出「上車量最高的 3 個區域和 3 個尖峰時段」
- 調度建議有邏輯（不是空話）
