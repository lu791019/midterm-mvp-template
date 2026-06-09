# LLM × DE MVP Builder 實戰工作坊 — 講稿

> 下午 3 小時版（13:30-16:30）。每張 slide 的講師講稿。
> 格式：`[Slide N] 標題 (建議秒數)` → 逐字稿

---

## Part 1：開場講解（13:30-13:55，25 分鐘）

### [Slide 1] 封面 (30s)

「歡迎大家來到期中實戰工作坊。上午各組報告了專題方向，下午我們換個模式——每個人獨立做出一條 Mini Data Pipeline。

今天結束時，每個人會帶走一條自己做的 pipeline。」

---

### [Slide 2] 今日目標 (45s)

「今天要做的一條線：從 CSV 讀資料進來，清洗，存進資料庫，用 SQL 查詢統計，再用 LLM 做 AI 加值分析，最後產出報告和 API。

這裡要提一個概念：我們今天做的是 ELT，不是傳統的 ETL。差別是什麼？傳統做法是先轉換資料再存進資料庫。現代做法是先把原始資料存進去（保留原貌），再在資料庫裡面做轉換。為什麼？因為原始資料保留住了，之後隨時可以重新清洗，不用重新下載。Snowflake、BigQuery、Databricks 都是走這個路線。」

---

### [Slide 3] 三段旅程 (20s)

「三場實體活動：期初畫流程圖是概念，今天做 pipeline 是實作，期末團專是完整系統。今天做的東西後續課程每學一個新技術都會回來升級。」

---

### [Slide 4] Medallion Architecture — 業界 (60s)

「你們今天會建三張表：raw、cleaned、analyzed。在業界叫 Medallion Architecture，Databricks 提出的。

三層：Bronze 層就是 raw 表——原始資料原封灌入。Silver 層就是 cleaned 表——清洗、標準化。Gold 層就是 analyzed 表——業務聚合、AI 加值。

為什麼分三層？Data Lineage，知道資料從哪來；出問題可以回 Bronze 重跑。

等等做的時候，每次 to_sql 寫入一張表，就是在建這個架構。」

---

### [Slide 5] Modern Data Stack — 業界 (45s)

「你今天用的每個工具，業界都有對應版本。read_csv 對應 Fivetran、SQLite 對應 BigQuery、pandas 對應 dbt、LLM API 對應 Vertex AI、FastAPI 對應 Looker。

不需要現在會這些，知道你做的跟業界是同一件事就好。後續課程學 Docker、Airflow、GCP 時會一個一個換成業界版本。」

---

### [Slide 6] 我們今天的 Pipeline — 活動 (45s)

「（指著流程圖）Extract 讀 CSV → Load 進 Bronze → Transform 清洗存入 Silver → SQL 統計 → LLM 加值存入 Gold → 產出報告和 API。

Notebook 有 10 個 Section。今天做 Section 0-8，Dashboard（Section 9-10）是回家作業。」

---

### [Slide 7] 時間表 (30s)

「下午 3 小時的節奏：先 25 分鐘講解，然後 45 分鐘實作 ETL。交流 5 分鐘後，10 分鐘講 LLM 和 API，再 45 分鐘實作。最後 30 分鐘 Demo。

（指表格）兩段實作各 45 分鐘，佔了大部分時間。重點是動手做。」

---

### [Slide 8] 規則 (20s)

「可以用 AI，但 Demo 時要能說明你的 pipeline 每一步。做不完帶走繼續，完成到哪就 Demo 到哪。Prompt 模板在 docs/ai_prompts.md。」

---

### [Slide 9] DE 角色定位 — 業界 (60s)

「今天你扮演的是資料解決方案顧問。懂業務——把需求翻譯成技術規格。有技術——Python / SQL / API 落地。建架構——ETL + 資料庫分層 + API。能導入——從原型到部署。

DE、DA、DS 的差別：DE 建管線管資料流，DA 分析資料做報表，DS 建模型做預測。今天你同時體驗三者。」

---

### [Slide 10] 6 題情境 — 活動 (45s)

「6 個題目，每個都是真實的業務情境。

（快速帶過）題 1 零售 POS、題 2 電商比價、題 3 音樂串流跨平台比較、題 4 叫車交通——這題最複雜要 merge 兩張表、題 5 求職薪資、題 6 不動產——台灣實價登錄中文資料。

每題也標了 Pipeline Pattern，面試會用到。選一個有興趣的。」

---

### [Slide 11] Repo 導覽 — 活動 (30s)

「clone 或下載 ZIP 後，你的東西在 data/raw/topic_N 裡。requirements_spec.md 先讀、pipeline_starter.ipynb 是你的 Notebook、api.py 是 FastAPI solution。docs 裡有 prompt 模板和 README 模板。」

---

### [Slide 12] Notebook 使用 — 活動 (30s)

「Notebook 大約 60 格 cell。綠色簡單有相關程式碼；黃色中等有別的情境範例；紅色較難是骨架填空；灰色直接跑不用改。前面手把手，後面放手。」

---

### [Slide 13] Data Quality + 清洗 — 業界+活動 (45s)

「清洗前先講 Data Quality。業界四維度：完整性、一致性、時效性、準確性。你等等做的 isnull、dtypes、describe 就是在檢查這些。

另一個概念 Schema-on-Read：Bronze 層不強制格式，讀的時候再處理。

清洗常用方法：dropna、to_numeric、to_datetime、merge。各題特殊難點：題 4 要 merge 兩張表，題 6 要民國年轉西元（+1911），題 3 的 Streams 有逗號要處理。」

---

### [Slide 14] 實作 1 Time (15s)

「現在開始實作 1，45 分鐘。

clone repo 或下載 ZIP、選題、讀需求、開 Notebook、跑 Section 0 到 Section 3。前 4 格有相關程式碼。

5 分鐘後交流時間跟組員分享你選了什麼題。開始。」

---

## Part 2：LLM + API 講解（14:45-14:55，10 分鐘）

### [Slide 15] LLM in Pipeline — 業界 (60s)

「LLM 在資料工程裡怎麼用？不是開 ChatGPT 聊天，是程式化呼叫。

關鍵概念 Structured Output——讓 LLM 回傳 JSON 格式，直接存進資料庫欄位。不是自由文字，是固定結構。

成本意識 LLM FinOps：GPT-4o-mini 處理 2000 筆大概 3 美分。業界做法是先跑 fallback baseline（規則版，零成本），再用 API 加值比較效果差異。」

---

### [Slide 16] Prompt 設計 — 活動 (45s)

「三個重點：第一，給明確標籤選項。第二，要求 JSON 格式回傳。第三，加上『不確定就選最接近的』。

API 掛了就用 fallback 規則版，兩個都能完成。

流程：先跑 1 筆測試確認 prompt 有效，再跑批次 50 筆，結果寫入 Gold 層。」

---

### [Slide 17] Data Product — 業界 (45s)

「Pipeline 做完但只有你能看到結果，那這條 pipeline 沒有價值。Data Product——pipeline 最終產出是給人用的產品。API 讓工程師串接、Dashboard 讓業務看圖表、報告讓主管做決策。

你的 pipeline.db 裡有完整資料，但老闆不會打開 .db 檔。FastAPI 把它包裝成 API endpoint。」

---

### [Slide 18] FastAPI + 打包 — 活動 (30s)

「Section 7 打包確認填 README。Section 8 做 FastAPI，api.py 是 solution，改好直接跑。

Dashboard 是回家作業，Section 9-10，app.py 已經有 solution。」

---

### [Slide 19] 實作 2 Time (15s)

「實作 2，45 分鐘。做 Section 4 到 8：LLM 分析、驗證、報告、打包、FastAPI。

先 1 筆確認 prompt 再批次。做完準備 Demo。開始。」

---

## Part 3：Demo + 收尾（15:45-16:30）

### [Slide 20] 完成標準 (15s)

「檢查一下：pipeline.db 有三表？processed 有 CSV？report.md 有報告？README 填了？能用 2 分鐘講清楚？全部打勾就完成了。」

---

### [Slide 21] 閃電秀 (15s)

「每人大約 2 分鐘。結構：20 秒說業務問題，20 秒說資料和清洗，20 秒說 LLM 做了什麼，20 秒 show output，20 秒升級方向，20 秒問答。

用 Bronze、Silver、Gold 這些術語來講。」

---

### [Slide 22] 後續升級 — 業界 (30s)

「你今天用的每個工具，後續課程都會換成業界版本。SQLite 換 BigQuery，pandas 換 dbt，手動跑換 Airflow DAG，本地換 Docker 部署到 GCP。這些加在一起就是 Modern Data Stack。」

---

### [Slide 23] 結尾 (30s)

「三件事：帶走你的 Notebook、pipeline.db 和報告。課後 push 到你的 GitHub。後續課程會持續升級這個專案。

Dashboard 記得回家做。

今天建的 pipeline 架構，就是後續每個技術模組的實作基礎。Q&A。」
