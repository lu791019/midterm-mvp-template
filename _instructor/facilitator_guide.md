# LLM × DE MVP Builder 實戰工作坊｜講師引導手冊

> 給主講師 + TA 用：照著這份跑就能完成下午 3 小時活動。

---

## 活動概覽

| 項目 | 內容 |
|------|------|
| 名稱 | LLM × DE MVP Builder 實戰工作坊 |
| 時長 | 13:30-16:30（下午 3 小時） |
| 規模 | 13 人 × 3 組智囊團 |
| 講師人力 | 主講 1 + TA 1-2 |
| 形式 | 個人實作 + 組內互助 |
| 上午 | 10:30-12:00 各組專題報告（與本手冊無關） |

## 活動目標

每位學員完成一條 Mini Data Pipeline：

```
CSV → pandas → SQLite (raw/cleaned/analyzed) → SQL → LLM → FastAPI
```

Dashboard（Section 9-10）為回家作業。

## 事前準備清單

### T-1 週

- [ ] 確認場地 Wi-Fi 可支援 15+ 裝置同時連線
- [ ] 確認共用 LLM API Key 額度
- [ ] 學員事前通知（帳號準備、Colab 測試、上午專題報告準備）
- [ ] 列印題目卡 ×6（各題情境 + 資料說明）

### 當天出門前

- [ ] 確認 repo 最新版可正常 clone
- [ ] 準備備用 API Key
- [ ] 帶延長線

### 到場後（上午）

- [ ] 測試投影
- [ ] 測試 Wi-Fi
- [ ] 上午引導各組專題報告（10:30-12:00）

### 午休後（13:15 就位）

- [ ] 確認分組（3 組，每組 4-5 人）
- [ ] 每組桌上放題目卡
- [ ] 投影切換到工作坊簡報

---

## 時間表（詳細版）

| 時段 | 分鐘 | 內容 | 講師做什麼 | 學員做什麼 | Notebook |
|------|------|------|-----------|-----------|---------|
| 13:30-13:50 | 20 | 開場講解 | 投影 demo pipeline + 概念 + 題目導覽 | 聽、看 | |
| **13:50-14:15** | **25** | **實作 1** | 巡場、解答環境問題 | clone → 環境 → 選題 | Section 0 |
| 14:15-14:20 | 5 | 交流 1 | 走動聽 | 組員互問：看 requirements_spec 的交流引導 | |
| 14:20-14:30 | 10 | ETL 講解 | 清洗重點 + 各題難點 | 聽 | |
| **14:30-15:15** | **45** | **實作 2** | 巡場 | ETL：raw → cleaned → SQL 統計 | Section 1-3 |
| 15:15-15:25 | 10 | LLM + API 講解 | demo prompt + fallback + API | 聽 | |
| **15:25-15:55** | **30** | **實作 3** | 巡場 | LLM → report → FastAPI | Section 4-8 |
| 15:55-16:05 | 10 | 交流 2：閃電秀預演 | 走動聽、給回饋 | 每組派 2~3 人 × 3 min 向組員預演 Demo | |
| **16:05-16:20** | **15** | **Demo** | 計時 + 點評 | 每組推派 1 人 × 3 min | |
| 16:20-16:30 | 10 | 收尾 | 升級路線 + Next Step + Q&A | | |

---

## 開場逐字稿（20 min 版，可精簡）

> 「歡迎大家。上午各組報告了專題方向，下午我們換個模式——**每個人獨立做出一條 Mini Data Pipeline**。
>
> 目標：從 CSV 到 API，在 3 小時內做出一條完整的資料管線。
>
> 我先 demo 一遍——
>
> （投影跑題 1 的 solution：讀 CSV → 寫入 SQLite → SQL 查詢 → LLM 分析 → 產出報告 → FastAPI）
>
> 你等等要做的就是這件事。Notebook 裡有步驟提示，前面幾格還附了參考程式碼。
>
> 有 6 個題目可以選，每題都有 2,000 筆真實資料。
>
> 規則：
> 1. 每人選一題，整條 pipeline 自己做
> 2. 同組可以互相討論、debug
> 3. 可以用 AI，但 Demo 時要能說明你的 pipeline
> 4. 做不完沒關係，repo 帶走課後繼續
>
> 最後每組推派 1 人上台 Demo 3 分鐘。show Notebook 或截圖就好。
>
> 現在選題、開環境。」

---

## 巡場引導重點

### 實作 1（ETL，45 min — Section 0-3）

**T+10（開始 10 分鐘）**
- 觀察：有沒有人還卡在環境（Colab 開不了、CSV 讀不到）
- 介入時機：超過 10 分鐘還沒讀到資料 → 幫他看路徑

**T+25**
- 觀察：清洗進度、有沒有寫入 SQLite
- 介入時機：卡在 dropna 或日期轉換 → 指著 Notebook 的提示問「這段你看到了嗎？」

**T+40**
- 觀察：有沒有做完 SQL 統計
- 介入時機：還沒做到 → 建議跳過細節，先把 raw + cleaned 表建好再做 SQL

### 實作 2（LLM + API，45 min — Section 4-8）

**T+10**
- 觀察：單筆 LLM 測試有沒有成功
- 常見問題：API Key 沒設 → 用 fallback；JSON 解析錯 → 改 prompt

**T+25**
- 觀察：批次分析進度 + 有沒有開始打包
- 常見問題：跑太慢 → 改 BATCH_SIZE 成 20 先看結果

**T+35**
- 觀察：有沒有開始做 FastAPI
- 提醒：Section 8 的 api.py 已經寫好，改好路徑就能跑

### 常見卡關 + 引導句

| 卡關 | 引導句 |
|------|--------|
| CSV 路徑錯 | 「你現在在哪個資料夾？用 `os.getcwd()` 看看」 |
| 型別錯誤 | 「先用 `df.dtypes` 看看欄位是什麼型別」 |
| SQL 語法錯 | 「SQL 有沒有少了 GROUP BY 或 FROM？」 |
| LLM 回空的 | 「先跑 fallback 版確認流程對，API 之後再接」 |
| 做不完 | 「沒關係，先把 Section 1-6 跑完，FastAPI 回家做也行」 |
| FastAPI 跑不起來 | 「確認 pipeline.db 存在，然後在 topic_N 資料夾下跑 `uvicorn api:app --reload`」 |

---

## Demo 環節（15 min）

### 格式
- 每組推派 1 人，3 分鐘，嚴格計時
- 用手機計時器，2:30 時舉手提醒
- 閃電秀預演已在交流 2 完成，正式 Demo 應更精煉

### 講師點評模板（每人挑 1 句）
- 「你的 SQL 查詢很清楚，xxx 這個發現很有意思」
- 「如果資料量變 10 倍，你的 pipeline 會怎麼調整？」
- 「這個 LLM 分類結果你同意嗎？有沒有分錯的？」

### 評分（內部，不公開）

| 維度 | 權重 |
|------|------|
| Pipeline 完成度（ETL + SQLite 三表） | 30% |
| AI 應用品質（prompt + 結果） | 25% |
| 作品打包（README + upgrade_plan） | 20% |
| 洞察品質（有數字支撐的發現） | 15% |
| Demo 表達（3 分鐘講清楚） | 10% |

---

## 收尾（15 min）

> 「今天做的 pipeline，不要做完就丟。
>
> 後續課程學 Docker、Airflow、GCP 的時候，都會回來升級這個專案。
>
> 三件事帶走：
> 1. 你的 pipeline.db + 報告 + Notebook
> 2. 填完 upgrade_plan
> 3. 課後把 repo push 到你自己的 GitHub
>
> Dashboard 記得回家做（Section 9-10，app.py 已有 solution）。
>
> 這就是你履歷上的第一個 Data Pipeline 專案。」

---

## 備案

| 風險 | 應對 |
|------|------|
| Wi-Fi 不穩 | 資料都在 repo 裡，離線也能跑（SQLite 不需網路） |
| API Key 額度用完 | 全部切 fallback 規則版 |
| 有人完全做不出來 | 開 solution 帶著跑，確保至少有產出 |
| 時間不夠 Demo | 每組縮成 2 分鐘 |
| Colab 打不開 | 本地用 `jupyter notebook`，或直接用 VS Code |

---

## 物資清單

| 物資 | 數量 | 用途 |
|------|------|------|
| 題目卡（A4） | 6 張 | 各題情境 + 資料說明 |
| 延長線 | 3 條 | 每組 1 條 |
| 計時器 | 1 | Demo 計時 |
| 備用 API Key | 1 組 | 備案 |

---

## 檔案對照

| 用途 | 檔案 |
|------|------|
| 學員手冊 | `_instructor/student_handbook.md` |
| 講師手冊 | 本文件 |
| 講稿 | `_instructor/speaker_notes.md` |
| 簡報 | `_instructor/mvp_builder_slides.html` |
| 每題答案 | `_instructor/solutions/topic_N_solution.ipynb` |
| 學員 Notebook | `data/raw/topic_N/pipeline_starter.ipynb` |
| README 模板 | `docs/README_TEMPLATE.md` |
| AI prompt 模板 | `docs/ai_prompts.md` |
| 資料來源說明 | `docs/data_sources.md` |
