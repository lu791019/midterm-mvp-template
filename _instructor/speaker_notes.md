# LLM × DE MVP Builder 實戰工作坊 — 講稿

> 下午 3 小時版（13:30-16:30）。3 段實作 + 每組 Demo。

---

## Part 1：開場講解（13:30-13:50，20 分鐘）

### [Slide 1] 封面 (30s)

「歡迎大家來到期中實戰工作坊。上午各組報告了專題方向，下午我們換個模式——每個人獨立做出一條 Mini Data Pipeline。」

---

### [Slide 2] 今日目標 (30s)

「今天做一條線：CSV 進來、清洗、存進資料庫、SQL 統計、LLM 分析、產出報告、包成 API。今天結束時，每個人帶走一條自己做的 pipeline。」

---

### [Slide 3] 做到哪算完成 (45s)

「三段實作，做到哪就 Demo 到哪。

實作 1 是環境和選題。實作 2 是 ETL，花最多時間。實作 3 是 LLM 加 API。Dashboard 是回家作業。

最後每組推派 1 人 Demo 3 分鐘。」

---

### [Slide 4] 三段旅程 (20s)

「三場實體活動：期初畫流程圖，今天做 pipeline，期末團專是完整系統。」

---

### [Slide 5-6] Medallion + Modern Data Stack (60s)

（快速帶過）「你們今天會建三張表：raw、cleaned、analyzed。業界叫 Medallion Architecture——Bronze、Silver、Gold。每個工具業界都有對應版本，後續課程會換上去。」

---

### [Slide 7] Pipeline (30s)

「（指著流程圖）這就是今天要做的。Notebook 有 10 個 Section，Section 0-8 是現場做，9-10 回家。」

---

### [Slide 8] 時間表 (30s)

「三段實作：25 分鐘環境選題、45 分鐘 ETL（最多時間）、30 分鐘 LLM 加 API。最後 15 分鐘 Demo。」

---

### [Slide 9] 規則 (15s)

「可以用 AI，Demo 時要能說明。做不完帶走繼續。」

---

### [Slide 10-13] DE 角色 + 6 題 + Repo + Notebook (3 min)

（快速帶過題目、Repo 結構、Notebook 標記，讓學員知道等等去哪找東西。）

---

### [Slide 14] Data Quality + 清洗 (30s)

「清洗四維度：完整性、一致性、時效性、準確性。你等等做的 isnull、dtypes、describe 就是在檢查這些。各題難點：題 4 merge 兩表、題 6 民國年。」

---

### [Slide 15] 實作 1 Time (15s)

「現在開始實作 1，25 分鐘。clone repo、開 Notebook、跑 Section 0、選題、讀需求。

Checklist 在投影上——基礎完成就是環境跑通加選好題。進階是已經看過 CSV 欄位。

5 分鐘後交流：跟組員說你選了什麼題。開始。」

---

## Part 2：ETL 講解（14:20-14:30，10 分鐘）

### ETL 講解 (5 min)

「Extract 讀 CSV 存 raw 表、Transform 清洗存 cleaned 表、SQL 統計存 CSV。前 4 格有參考程式碼。」

### 各題清洗重點 (5 min)

「題 1 和 5 比較直覺。題 3 注意 Streams 有逗號。題 4 要 merge 兩張表。題 6 有民國年。看你的 Section 2 提示。」

---

### [Slide 16] 實作 2 Time (15s)

「實作 2，45 分鐘，今天最重要的一段。Section 1 到 3。

基礎完成：raw 表 + cleaned 表 + 統計 CSV + 一個能 Demo 講的數字。進階：多寫幾個 SQL、發現有趣規律。

Section 3 之後有『你還可以分析什麼』提示，做完必要的可以多探索。

開始。」

---

## Part 3：LLM + API 講解（15:20-15:25，5 分鐘）

### LLM + Prompt + API (5 min)

「LLM 要求回 JSON、給明確標籤選項。沒 API Key 就用 fallback。先 1 筆測試再批次。

報告寫到 output/report.md。FastAPI 的 api.py 已經是 solution，改好路徑就能跑。」

---

### [Slide 17-18] 實作 3 Time (15s)

「實作 3，30 分鐘。Section 4 到 8。LLM 分析、報告、FastAPI。

基礎完成：analyzed 表 + report.md + API 跑起來。先 LLM 再報告再 API。

準備 Demo：整理要 show 的畫面。開始。」

---

## Part 4：Demo + 收尾（16:00-16:30）

### Demo (15 min)

「每組推派 1 人上台，3 分鐘。結構：問題 → 清洗 → LLM → output → 升級方向。

用 Medallion 術語講：Bronze 存了什麼、Silver 清了什麼、Gold 分析了什麼。」

### 收尾 (15 min)

「三件事帶走：Notebook、pipeline.db、報告。課後 push 到 GitHub。Dashboard 回家做。

今天建的 pipeline 架構，就是後續每個技術模組的實作基礎。Q&A。」
