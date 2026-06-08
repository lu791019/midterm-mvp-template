# LLM × DE MVP Builder 實戰工作坊 — 講稿

> 每張 slide 的講師講稿。建議時間標在每段開頭。
> 格式：`[Slide N] 標題 (建議秒數)` → 逐字稿（可精簡或展開）

---

## [Slide 1] 封面 (30s)

「歡迎大家來到期中實戰工作坊。上次期初活動你們用紙筆畫了流程圖，今天要把它變成真的跑得起來的程式。

今天結束時，每個人會帶走一條自己做的 Mini Data Pipeline。」

---

## [Slide 2] 今日目標 (60s)

「今天要做的一條線：從 CSV 讀資料進來，清洗，存進資料庫，用 SQL 查詢統計，再用 LLM 做 AI 加值分析，最後產出報告，甚至包裝成 API 和 Dashboard。

這裡要特別提一個概念：我們今天做的是 ELT，不是傳統的 ETL。差別是什麼？傳統做法是先轉換資料再存進資料庫。現代做法是先把原始資料存進去（保留原貌），再在資料庫裡面做轉換。為什麼？因為原始資料保留住了，之後隨時可以重新清洗，不用重新下載。Snowflake、BigQuery、Databricks 都是走這個路線。

你今天做的就是這件事。」

---

## [Slide 3] 三段旅程 (30s)

「課程有三場實體活動，從概念到實作到部署。期初畫流程圖是概念，今天做 pipeline 是實作，期末團專是完整系統。

今天做的東西後續課程每學一個新技術都會回來升級。」

---

## [Slide 4] Medallion Architecture — 業界 (90s)

「你們今天會建三張表：raw、cleaned、analyzed。在業界，這個做法有一個正式名稱，叫 Medallion Architecture，是 Databricks 提出的，被 Microsoft、Google、AWS 都廣泛採用。

三層分別是：

Bronze 層，就像你的 raw 表——把原始資料原封不動灌進來，不管它髒不髒、格式對不對。重點是保留原貌。

Silver 層，就像你的 cleaned 表——在這層做清洗、標準化、合併。去空值、轉型別、加新欄位，讓資料變成乾淨可查詢的狀態。業界叫這個 Enterprise View。

Gold 層，就像你的 analyzed 表——在這層做業務聚合、AI 加值。可以直接對接報表、API、機器學習模型。

為什麼要分三層？兩個原因：第一，Data Lineage，你知道每筆資料從哪來、經過什麼處理。第二，出問題時可以回到 Bronze 重跑，不用重新下載原始資料。

等等你做的時候，每次 to_sql 寫入一張表，就是在建這個架構。」

---

## [Slide 5] Modern Data Stack — 業界 (60s)

「你今天用的每個工具，在業界都有對應的正式版本。

read_csv 對應的是 Fivetran 或 Airbyte——專門做資料串接的工具。SQLite 對應的是 Snowflake 或 BigQuery——雲端資料倉儲。pandas 清洗對應的是 dbt——用 SQL 管理轉換邏輯。LLM API 對應的是 SageMaker 或 Vertex AI。FastAPI 加 Streamlit 對應的是 Looker 或 Metabase。

你不需要現在會這些工具，但要知道你今天做的事情跟業界在做的是同一件事，只是工具不同。後續課程學 Docker、Airflow、GCP 的時候，就是在把今天的工具一個一個換成業界版本。」

---

## [Slide 6] 我們今天的 Pipeline — 活動 (60s)

「回到我們今天的實際架構。

（指著流程圖）Extract 讀 CSV，Load 進 SQLite 的 Bronze 層，Transform 清洗寫入 Silver 層，SQL 做統計，LLM 做加值寫入 Gold 層，最後產出 CSV、報告、API、Dashboard。

你的 Notebook 有 10 個 Section，對應這條線的每一段。Section 0 是環境，1 是 Extract，2 是 Transform，3 是 SQL，4 是 LLM，5 是驗證，6 是報告，7 是打包，8 是 FastAPI，9 是 Dashboard，10 是本地部署指引。

必做是 Section 1 到 6，選做是 8 到 10。」

---

## [Slide 7] 時間表 (30s)

「今天的節奏是：每段先講 10 到 30 分鐘概念，然後你們實作 40 到 45 分鐘，每段之間有 5 分鐘交流時間。

（指著表格）上午兩段、下午兩段、最後 Demo。實作佔超過一半的時間，講解只佔四分之一。重點是動手做。」

---

## [Slide 8] 規則 (30s)

「可以用 AI，但 Demo 時要能說明你的 pipeline 每一步。做不完帶走繼續，完成到哪就 Demo 到哪。

Prompt 模板在 docs/ai_prompts.md，直接用。」

---

## [Slide 9] DE 角色定位 — 業界 (90s)

「今天你扮演的角色是資料解決方案顧問。為什麼不叫工程師？因為在真實職場，DE 不只是寫 SQL 的人。

懂業務面——你要理解客戶的痛點，把模糊的需求翻譯成技術規格。
有技術能力——用 Python、SQL、API 把想法落地成系統。
能建立架構——設計 ETL pipeline、資料庫分層、API 服務。
能協助導入——從原型到部署，讓組織開始用資料做決策。

這四件事加在一起就是顧問。

再說一下 DE、DA、DS 的差別：DE 建管線管資料流，DA 分析資料做報表，DS 建模型做預測。今天你同時體驗三個角色——建管線是 DE，做統計是 DA，用 LLM 是 DS。」

---

## [Slide 10] 6 題情境 — 活動 (60s)

「6 個題目，每個都是真實的業務情境。

（快速帶過）題 1 零售 POS——10 萬筆交易找暢銷商品。題 2 電商比價——跨平台價差分析。題 3 音樂串流——Spotify、YouTube、TikTok 跨平台比較。題 4 叫車交通——時段加地區熱點分析，這題最複雜因為要 merge 兩張表。題 5 求職薪資——資料領域薪資行情和 Remote 影響。題 6 不動產——台灣實價登錄，中文資料加民國年轉換。

每題我也標了 Pipeline Pattern。比如題 4 是 Dimensional Join 加 Geospatial，題 2 是 Cross-source Join。這些是業界描述 pipeline 類型的術語，面試會用到。

選一個你有興趣的，等等實作時間開始就選。」

---

## [Slide 11] Repo 導覽 — 活動 (45s)

「clone 下來或下載 ZIP 後，你的東西都在 data/raw/topic_N 這個資料夾裡。

requirements_spec.md 是需求規格，先讀這個知道要做什麼。pipeline_starter.ipynb 是你的 Notebook，打開它開始做。api.py 和 app.py 是 Section 8 和 9 的 solution。processed 和 output 是跑完後的產出資料夾。

docs 資料夾有參考文件：ai_prompts.md 是 Prompt 模板，README_TEMPLATE.md 是打包用的 README 模板。」

---

## [Slide 12] Notebook 使用 — 活動 (45s)

「Notebook 大約 60 格 cell，標記系統是這樣：

綠色簡單——有相關程式碼在註解裡，取消註解改欄位名就能跑。前 4 格都是這種。

黃色中等——有別的情境範例教你語法，你要翻譯到自己的欄位。比如範例用學生名單教 read_csv，你要改成讀你的 orders.csv。

紅色較難——FastAPI 和 Dashboard 有骨架，填入 SQL 和欄位名。

灰色不需要改——環境設定、檢查點、LLM helper 函式，直接跑。

循序漸進，前面手把手，後面放手。」

---

## [Slide 13] 實作 1 Time (15s)

「現在開始實作 1，45 分鐘。

沒有 GitHub 帳號的先到 github.com 註冊，免費的。然後 clone 或下載 ZIP。選題、讀需求、開 Notebook、跑 Section 0 和開始 Section 1。

前 4 格有相關程式碼。5 分鐘後交流時間跟組員分享你選了什麼題。

開始。」

---

## [Slide 14] Data Quality — 業界 (60s)

「做清洗之前，先講一個概念：Data Quality。

業界評估資料品質有四個維度：完整性——缺漏值有多少？一致性——同一個欄位格式統一嗎？時效性——資料多新？準確性——數值合理嗎？

你等等在 Notebook 裡做的 isnull、dtypes、describe，就是在檢查這四個維度。

另一個概念是 Schema-on-Read：Bronze 層不強制格式，讀的時候再處理。這就是為什麼我們先灌原始資料進 raw 表，然後在 Transform 階段才做清洗。」

---

## [Slide 15] pandas 清洗 — 活動 (45s)

「回到實際操作。清洗的常用方法：dropna 處理缺漏值、to_numeric 轉數字、to_datetime 轉日期、merge 合併表。

各題的難點：題 4 要 merge 兩張表把 LocationID 轉成地名，題 6 要把民國年 1130101 轉成西元年 2024。其他題相對直覺。」

---

## [Slide 16] 實作 2 Time (15s)

「實作 2，40 分鐘。做 Section 1 到 3：Extract 寫入 Bronze，Transform 寫入 Silver，SQL 查詢統計。

卡太久就先跳過細節把表建好。交流時間跟組員比較清洗策略和 SQL 寫法。

開始。」

---

## [Slide 17] LLM in Pipeline — 業界 (60s)

「LLM 在資料工程裡怎麼用？不是開 ChatGPT 聊天，是程式化呼叫。

關鍵概念是 Structured Output——讓 LLM 回傳 JSON 格式，直接存進資料庫欄位。不是自由文字，是固定結構。這樣才能程式化處理。

成本意識也很重要，業界叫 LLM FinOps。GPT-4o-mini 處理 2000 筆大概 3 美分。業界做法是先跑 fallback baseline（規則版，零成本），再用 API 加值比較效果差異。

你今天做的就是這個流程。」

---

## [Slide 18] Prompt 設計 — 活動 (45s)

「實際操作三個重點：第一，給明確標籤選項，不要開放式。第二，要求 JSON 格式回傳。第三，加上『不確定就選最接近的』避免拒答。

API 掛了就用 fallback 規則版。兩個都能產出結果。

流程是：先跑 1 筆測試確認 prompt 有效，再跑批次 50 筆，結果寫入 Gold 層。」

---

## [Slide 19] 實作 3 Time (15s)

「實作 3，45 分鐘。做 Section 4 到 6：LLM 分析寫入 Gold，跨表驗證 Data Lineage，產出報告。

先跑 1 筆確認再批次。交流時間分享 prompt 經驗和分類結果。

開始。」

---

## [Slide 20] Data Product — 業界 (60s)

「Pipeline 做完了，但如果只有你一個人能看到結果，那這條 pipeline 沒有價值。

業界有一個概念叫 Data Product——pipeline 的最終產出是給人用的產品。API 讓工程師串接，Dashboard 讓業務看圖表，報告讓主管做決策。

你的 pipeline.db 裡有完整的資料，但老闆不會打開 .db 檔。你需要包裝它。FastAPI 把資料庫包裝成 API endpoint，Streamlit 把它包裝成互動圖表。這就是 Data Product。」

---

## [Slide 21] FastAPI + Dashboard — 活動 (30s)

「實際操作：Section 7 打包確認，填 README 用 docs/README_TEMPLATE.md 模板。Section 8 做 FastAPI 定義 endpoint。Section 9 做 Dashboard 互動圖表。api.py 和 app.py 是 solution。」

---

## [Slide 22] 實作 4 Time (15s)

「實作 4，45 分鐘。重點是 FastAPI 和 Dashboard。也要填 README 和 upgrade_plan。

交流時間準備 Demo。開始。」

---

## [Slide 23] 完成標準 (15s)

「檢查一下：pipeline.db 有三表？processed 有 CSV？report.md 有報告？README 填了？能用 2 分鐘講清楚？全部打勾就完成了。」

---

## [Slide 24] 閃電秀 (15s)

「每人大約 2 分鐘。結構：20 秒說業務問題，20 秒說資料和清洗，20 秒說 LLM 做了什麼，20 秒 show output，20 秒升級方向，20 秒問答。

用 Bronze、Silver、Gold 這些術語來講。」

---

## [Slide 25] 後續升級 — 業界 (45s)

「最後看一下升級路線。你今天用的每個工具，後續課程都會換成業界版本。SQLite 換成 BigQuery，pandas 換成 dbt，手動跑換成 Airflow DAG，本地 Streamlit 換成 Docker 容器化部署到 GCP。

這些工具加在一起就是 Modern Data Stack。你今天做的是簡化版，但架構是一樣的。」

---

## [Slide 26] 結尾 (30s)

「三件事：帶走你的 Notebook、pipeline.db 和報告。課後 push 到你的 GitHub。後續課程會持續升級這個專案。

今天建的 pipeline 架構，就是後續每個技術模組的實作基礎。

Q&A。」
