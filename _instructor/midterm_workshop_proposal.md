> ⚠️ **歷史文件**：本企劃書為早期規劃版本（全天 8 題），僅供參考。
> 正式版本請看：
> - 時間表 → `mvp_builder_slides.html`（Slide 7）
> - 講師手冊 → `facilitator_guide.md`
> - 學員手冊 → `student_handbook.md`
> - 題目：6 題（topic_1 ~ topic_6）

---

# 雲端資料工程師期中活動企劃書：AI × 資料工程挑戰賽

> **版本**：v4.0
> **日期**：2026-06-07
> **提案人**：Dex
> **狀態**：待確認

---

## 1. 背景與動機

### 1.1 課程脈絡

本工作坊為 **TibaMe 雲端資料工程師養成班** 的 **期中實戰活動**。學員在此時間點已完成：

- Python 與 pandas 基礎操作
- SQL 與資料庫查詢
- API request / response 基礎概念（若已學 FastAPI，可作為延伸理解）
- 基礎 ETL 流程概念與實作
- 「資料專案模擬室」活動（95 min）：透過分組討論與流程圖設計，建立資料處理流程概念與團隊角色分工認知

**尚未學習**：Docker、Airflow 排程、GCP 雲端部署。

本工作坊的定位是 **「用已學能力跑完一個粗版 MVP ＋ AI 首次體驗」**——上次畫了流程圖，今天先用 Python、pandas、SQL、Colab / Notebook 或講師模板把它做成能跑的原型，並首次體驗 AI/LLM 如何融入資料工程流程。

**核心設計**：工作坊產出的專案不是一次性練習，而是一個 **隨課程進度持續升級的長期作品**：

```
期初活動              工作坊（期中）              後續進階課程 與後續課程升級
──────────────       ──────────────           ──────────────
紙筆流程圖        →   個人 LLM x DE 粗 MVP →   後續進階課程 拆成 ETL 架構
業務需求草稿      →   可跑 pipeline        →   WSL / VS Code / GitHub 整理
工具選型討論      →   demo + 升級草稿      →   Docker / Airflow / GCP 升級

同一個專案，從期中原型開始，後續進階課程 正式回收，每學一個新技術就升級一次
```

完整整合藍圖見 `LLM_DE_MVP_INTEGRATION_PLAN.md`。本工作坊的定位是產出 **v0-v2 的個人 MVP 種子**；後續進階課程 會回收成果，產出 `mvp_review.md`、`etl_mapping.md`、`mvp_upgrade_plan.md`，後續課程再逐步升級到 GitHub / Docker / Airflow / GCP。

### 1.2 為什麼需要這個工作坊

| 痛點 | 解決方式 |
|------|---------|
| 學了 Python 但不知道怎麼用在資料工程場景 | 以產業情境驅動，讓技術落地 |
| 對 AI/LLM 在資料工程中的角色感到模糊 | 實際操作 ChatGPT + LLM API，體驗具體用法 |
| 上次活動只停在「討論」層面，缺乏動手成就感 | 每人產出可跑、可展示、可被 後續進階課程 回收的 MVP 原型 |
| 轉職者缺乏「我做得到」的信心 | 闖關制 + Starter Code 降低門檻，保障完成率 |
| 沒有可展示的作品集 | 每人帶走作品素材，後續進階課程 後逐步整理成正式 repo 與作品集 |

### 1.3 活動定位：工作坊骨架 × 黑客松調味

本活動刻意採用 **「引導式挑戰賽」** 的混合定位，而非純工作坊或純黑客松：

| 維度 | 純工作坊 | 純黑客松 | **本活動（引導式挑戰賽）** |
|------|---------|---------|------------------------|
| 氛圍 | 安全、跟著做 | 競賽壓力、自己衝 | **有引導的挑戰感** |
| 講師角色 | 老師帶著走 | 裁判，退到後面 | **前半引導、後半放手** |
| 完成率 | 高（但缺挑戰） | 低（做不完正常） | **用 Starter Code 保底，用進階任務拉高** |
| 學員心態 | 「我在學東西」 | 「我在打仗」 | **「我在解決一個真實問題」** |

**為什麼不做純黑客松？**
學員是轉職者 + 初學者，期中階段信心仍在建立中。純黑客松的高壓環境可能適得其反，打擊學習動機。

**為什麼不做純工作坊？**
上次 95 min 活動已經是引導式的了。這次需要升級——透過情境抽籤、計時、Demo 發表、獎項等黑客松元素，製造投入感和成就感。

**最終定位**：名稱用「挑戰賽」而非「黑客松」——既有挑戰的興奮感，又不會讓初學者覺得「我不夠格參加」。

---

## 2. 工作坊概要

| 項目 | 內容 |
|------|------|
| **名稱** | AI × 資料工程挑戰賽 |
| **副標** | 「上次你們畫了流程圖，今天把它做出來——用 AI 加速」 |
| **時長** | 10:00-16:00；中間午休 1.5 小時；有效活動約 4-5 小時；每小時附近安排 10 分鐘休息（詳細議程待確認） |
| **對象** | TibaMe 雲端資料工程師養成班學員（轉職者、初學者） |
| **前提** | 已學 Python / pandas / SQL 基礎，已完成「資料專案模擬室」活動；API / GitHub / Docker 可作為概念或加分，不作為當天硬門檻 |
| **人數** | 以實際班級人數為準；建議分成 **3 組智囊團** |
| **形式** | **每人一題一個 MVP、組內互助討論** — 每位學員從題庫選一題獨立完成完整 pipeline；同組成員可選不同題，藉由互相討論接觸不同資料來源、處理策略與 AI 加值方法 |

---

## 3. 核心設計理念

### 3.1 「個人實作、團隊智囊」模式

```
討論層：三組各自形成智囊團，同組討論策略、互相除錯、交流 prompt 技巧
         │
實作層：每人從題庫選一題，獨立跑完完整 4 關 pipeline
         │
成果層：每人帶走自己的 MVP 原型（Notebook / script + output + demo 素材 + 升級計畫草稿）
```

- 每人都做完整的 4 個關卡（不分工切段）
- 全班分成 3 組智囊團；每位學員選一個情境做自己的 MVP，不採分工制
- 同組可以有不同題目 → 討論時能看見不同資料來源、不同清洗策略、不同 AI 加值方式
- 卡關時先問組員，再問 TA → 自然形成 peer learning，也培養期末團專默契
- Demo 時可展示「不同題目如何共用同一套 pipeline 方法」→ 更貼近資料工程通用能力

### 3.2 與初階活動的升級對比

| | 初階：資料專案模擬室（95 min） | 進階：AI 資料工程挑戰賽（10:00-16:00） |
|---|---|---|
| 執行單位 | 組 | 個人（組內互助，跨題討論） |
| 產出 | 一張流程圖（組） | 可跑 MVP 原型（個人） |
| 動手程度 | 畫圖 + 討論 | 寫 code + 跑 AI + 接 Dashboard |
| 帶走什麼 | 概念理解 | 可展示作品素材，後續進階課程 後整理成作品集 |
| 團隊價值 | 分工協作 | 同儕學習 + 解題互助 + 團隊默契 |

### 3.3 設計原則

| 原則 | 說明 |
|------|------|
| **低門檻、高天花板** | Starter Code + 模板降低起步難度；Dashboard 部署讓強者不無聊 |
| **傳統 vs AI 對比** | 每關都有「手動做法」和「AI 做法」的體驗，學員切身感受效率差異 |
| **做不完沒關係** | 帶走的模板資料夾裡素材都在，後續進階課程 後可繼續整理 |
| **成果可延伸** | 工作坊產出會在 後續進階課程 回收，後續再對接 GitHub、Docker、排程自動化、雲端部署 |

### 3.4 MVP 版本階梯

| 版本 | 名稱 | 工作坊中做到什麼 | 後續怎麼升級 |
|---|---|---|---|
| **v0** | Notebook Prototype | Colab / Notebook 手動跑 ETL + LLM 分析 | 拆成 `.py` script |
| **v1** | Local Folder / Starter Repo | 本地資料夾或講師模板，能保留程式與輸出 | 後續進階課程 後整理成 GitHub repo、README、架構圖 |
| **v2** | Runnable Tool | `run_pipeline.py` / Streamlit 本地展示 | 補測試與設定管理 |
| **v3** | Dockerized MVP | 使用講師模板嘗試 `docker compose up`，只體驗價值 | 學完 Docker 後自行改寫 |
| **v4** | Scheduled Pipeline | 手動執行或簡單 Python schedule | 學完 Airflow 後改 DAG |
| **v5** | Data Engineering MVP | CSV / SQLite | 升級 MySQL / BigQuery |
| **v6** | Cloud Demo | 本地 demo | 部署到 GCP |

工作坊最低完成目標是 **v0 + 可展示輸出**；推薦做到 **v1 / v2**；GitHub、VS Code、WSL、Docker 在工作坊中只作為可選路線或模板化加分項，不要求學員理解完整原理。

---

## 4. 學習目標

工作坊結束時，學員應能夠：

1. **說明 AI/LLM 在資料工程 pipeline 中的 3-5 個具體應用場景**
   - 需求釐清、非結構化資料清洗、自動分類、Text-to-SQL、報告生成
2. **獨立完成一個 mini data pipeline**
   - 從資料取得 → 清洗轉換 → AI 加值分析 → 成果展示
3. **帶走一份可展示、可升級的個人 MVP 原型**
   - 包含程式碼或 Notebook、分析結果、demo 素材、升級計畫草稿
4. **體驗「用 AI 當工作夥伴」的協作模式**
   - 用 prompt 追問需求、生成程式碼、解讀分析結果

---

## 5. 議程總覽

> 10:00-16:00，午休 12:00-13:30。有效活動約 **4.5 小時**（270 min）。
> 設計原則：第一段 40 分鐘完整講解＋跑完一次 demo pipeline；後續每段 15-20 分鐘講解 + 30-50 分鐘實作。休息採自由制（實作時段可自行離席），正式休息每小時 5 分鐘。

| 時段 | 分鐘 | 模式 | 內容 |
|------|------|------|------|
| 10:00-10:40 | 40 | 講解 | 開場：活動目標、repo 結構導覽、完整 pipeline demo（用題目 1 從頭跑到尾）、8 題選題說明 |
| 10:40-10:45 | 5 | 休息 | |
| 10:45-11:05 | 20 | 講解 | 資料清洗重點＋pandas 常見坑（用 2-3 題的資料結構舉例）、LLM 呼叫預告 |
| 11:05-11:55 | 50 | 實作 | **選題 → 開環境 → 讀資料 → ETL 清洗 → 產出 processed data**（每題已附 `requirements_spec.md`，學員不需自己從零釐清需求） |
| 11:55-12:00 | 5 | 休息 | |
| 12:00-13:30 | 90 | 午休 | 想繼續做的可以做 |
| 13:30-13:50 | 20 | 講解 | LLM API demo：prompt 設計、batch 分析、fallback 機制、常見錯誤處理 |
| 13:50-14:40 | 50 | 實作 | **LLM 分析 → 產出 report.md → 接 Streamlit（進階）** |
| 14:40-14:45 | 5 | 休息 | |
| 14:45-15:00 | 15 | 講解 | 打包教學：README 模板怎麼填、upgrade_plan、Demo 3 分鐘怎麼講、GitHub push 流程 |
| 15:00-15:15 | 15 | 實作 | **填 README + upgrade_plan + 準備 demo** |
| 15:15-16:00 | 45 | Demo | **閃電秀 13 人 × 3 分鐘**（含講師穿插點評）；詳見附錄 A |

### 時間分配摘要

| 類型 | 總時長 | 佔比 |
|------|--------|------|
| 講解 | 95 min | 35% |
| 實作 | 115 min | 43% |
| Demo | 45 min | 17% |
| 休息 | 15 min | 5% |

### 每段實作的「最低完成線」與「進階挑戰」

| 實作段 | 最低完成線 | 進階挑戰 |
|--------|-----------|---------|
| 上午 50 min ETL | `pd.read_csv` 成功 + 基礎清洗 + processed data 產出 | 完整清洗 + 統計摘要 + 多檔案合併 |
| 下午 50 min LLM | LLM 至少分析 5 筆資料 + `report.md` 有內容 | 全量分析 + prompt 調優 + Streamlit 接上 |
| 打包 15 min | README 填完 + upgrade_plan 填完 | GitHub push + Streamlit 部署 |

---

## 6. 情境題庫（各組抽籤選一，與期初工作坊共用同一池）

每個情境皆設計為可在工作坊內完成的 mini data pipeline，並自然嵌入 AI/LLM 應用。原則上 **8 個題目都可以開放選擇**，但每個題目都必須先確認「資料來源可取得、ETL 可完成、LLM 加值有明確輸出、Demo 可展示」。每位學員選一題做自己的版本，同組互相討論。**完整三層流程設計（業務 / 課程實作 / 進階展望）見 `course_project_guide.md` §5.4**。

| # | 情境主題 | 角色設定 | 資料來源 | AI 加值切入點 | 難度 |
|---|---------|---------|---------|-------------|------|
| 1 | 餐飲連鎖 POS 庫存優化 | 餐飲集團資料顧問 | Kaggle Restaurant Order Details / UCI Online Retail | LLM 分析非結構化評論 → 結構化標籤 | ★★ |
| 2 | B2C 電商競品比價追蹤 | 電商營運資料顧問 | 爬 momo / PChome / 蝦皮公開頁 / Kaggle e-commerce | LLM 自動生成競品分析摘要 | ★★ |
| 3 | 數位金融客訴效率分析 | 金融業資料顧問 | CFPB Complaint Database / Kaggle Bank Complaints | LLM 情緒分析 + 自動分類 + 優先排序 | ★★ |
| 4 | 音樂串流（Spotify）推薦優化 | 娛樂產業資料顧問 | Spotify Web API / Spotify Charts / Kaggle KKBOX | LLM 生成聽眾洞察與推薦摘要 | ★★ |
| 5 | 叫車服務交通熱點分析 | 交通服務資料顧問 | NYC TLC Trip Records / Uber Movement | LLM 解讀交通模式 | ★★★ |
| 6 | 求職媒合職缺洞察 | 人資科技資料顧問 | 爬 104 / CakeResume 公開頁 / 勞動部統計 | LLM 履歷職缺匹配 + 技能熱度摘要 | ★★ |
| 7 | 媒體業新聞輿情即時監測 | 媒體業資料顧問 | RSS / NewsAPI / Google News API | LLM 新聞摘要 + 情緒追蹤 | ★★★ |
| 8 | 不動產房價趨勢分析 | 不動產資料顧問 | 內政部實價登錄 / data.gov.tw | LLM 生成區域分析建議書 | ★★ |

### 6.1 題目分配方式（待討論）

目前建議採用 **每人選一題、三組智囊團討論、每人獨立完成**：

| 設計 | 說明 |
|---|---|
| 每人選一題 | 每位學員都能做出自己的 MVP，作品更有個人化 |
| 三組智囊團 | 組內不一定同題，但可以互相討論資料來源、清洗策略、prompt、錯誤排除 |
| 每人獨立完成 | 不分工切段，確保每位學員都跑過完整 ETL + LLM pipeline |
| 跨題互學 | 不同題目帶出不同資料型態與 AI 加值方式，更能培養團隊默契 |

題目開放前，每題都要通過以下檢查：

- 有講師預備資料或穩定公開資料來源
- 有明確的 raw data → processed data → LLM output
- 有 30 分鐘內能完成的最低版本
- 有可展示的最後產出，例如報告、表格、標籤、摘要或 dashboard
- 有 API / 網路失敗時的 fallback 資料

詳細題目可行性與資料來源規格見 `docs/topic_catalog.md`。

---

## 7. 三大關卡設計

> 舊版為四大關卡（需求釐清 → ETL → LLM → 打包）。v4.0 將「需求釐清」改為**講師直接提供**（每題預寫好 `requirements_spec.md`），省下初學者用 AI 對話釐清需求的不確定性時間，讓實作時間集中在 ETL 和 LLM。

### 關卡 1：建立可跑的 ETL（上午 50 min 實作）

- **工具**：Google Colab（Notebook）+ pandas
- **用到的已學技能**：`pd.read_csv()`、pandas 清洗轉換、基礎統計
- **起點**：每題已附 `requirements_spec.md`（題目、使用者、資料來源、MVP scope、成功指標），學員選題後直接動手
- **做法**：
  - 開 Colab → 讀取題目對應的真實資料 CSV
  - 用 Starter Notebook 的步驟提示做清洗（缺漏值、型別轉換、欄位篩選）
  - 卡關時可用 ChatGPT/Claude 生成 pandas 語法（體驗 AI 輔助寫 code）
- **產出**：清洗後的 `data/processed/*.csv` + 基礎統計摘要
- **組內互助**：不同題目的人互相比較資料結構、清洗策略、debug
- **AI 學習點**：用 AI 生成 pandas 語法、加速問題排除

### 關卡 2：加入 LLM 加值分析（下午 50 min 實作）

- **工具**：Google Colab + LLM API（OpenAI / Anthropic）
- **用到的已學技能**：API request / response 概念、Python 函式呼叫
- **做法**：
  - 用封裝好的 helper 函式呼叫 LLM API 對資料做進階分析
  - 情緒分析 / 自動分類 / 摘要生成 / 顧問報告生成（依題目不同）
  - 體驗「從手動 ChatGPT 對話 → 程式批次自動化」的升級
  - API 失敗時有 fallback 規則版（確保離線也能完成）
- **產出**：AI 加值後的分析結果（新欄位、分類標籤）+ `output/report.md`
- **組內互助**：交流 prompt 寫法、比較不同 prompt 的分析品質差異
- **AI 學習點**：「程式 × AI API」的串接體驗

### 關卡 3：MVP 打包 + Demo 準備（15 min 實作）

- **做法**：
  - 用講師提供的 README 填空模板完成專題文件（題目、目標、流程、執行方式、產出、升級計畫）
  - 填寫 `docs/upgrade_plan.md`（後續課程升級路徑，統一格式見下方）
  - 準備 3 分鐘 Demo（截圖 / Notebook output / Streamlit 畫面）
  - 進階：接 Streamlit Dashboard、push 到 GitHub
- **產出**：完整 README + upgrade_plan + demo 素材
- **AI 學習點**：用 AI 快速生成 README 草稿、展示摘要

### 後續升級計畫（統一格式）

`docs/upgrade_plan.md` 採統一格式，對應後續課程模組：

| 升級階段 | 對應課程 | 升級內容 |
|---------|---------|---------|
| 後續進階課程 | 帶狀課回收 | 回顧 MVP → 拆成正式 ETL 架構 → 產出 etl_mapping.md |
| Docker | 容器化模組 | 把 pipeline + Streamlit 容器化，`docker compose up` 一鍵啟動 |
| Airflow | 排程模組 | 把 `run_pipeline.py` 改成 DAG，定時自動跑 |
| MySQL / BigQuery | 資料庫模組 | 把 CSV 換成資料庫，SQL 查詢取代 `pd.read_csv` |
| GCP | 雲端部署模組 | 部署到 Cloud Run / Cloud Composer |
| 期末團專 | 結業專題 | 擴充為團隊完整系統，多人協作 + 完整 Demo |

### AI / LLM / AI Coding 使用規範

本活動允許並鼓勵使用 AI，但要求學員留下使用紀錄，讓 AI 成為可解釋的工作夥伴，而不是黑箱代寫。

| 用法 | 是否允許 | 要留下什麼 |
|---|---|---|
| 用 ChatGPT / Claude 釐清需求 | 允許 | 把關鍵 prompt 與收斂結果寫入 `docs/requirements_spec.md` |
| 用 AI 生成 pandas / SQL / Python 草稿 | 允許 | 自己讀懂後修改，並在註解或文件中寫下做了什麼 |
| 用 AI debug 錯誤訊息 | 允許 | 記錄錯誤與修正方式 |
| 用 LLM API 做分類 / 摘要 / 洞察 | 鼓勵 | 輸出 `output/report.md` 或 processed data 欄位 |
| 完全貼上不了解的程式碼 | 不建議 | Demo 時需要能說明 pipeline 每一步 |

可直接使用的 prompt 模板見 `docs/ai_prompts.md`。

---

## 8. 個人 MVP 原型規格

### 8.1 工作坊結束時每人帶走

```
my-data-project/
├── README.md                    ← AI 協助生成的專案說明
├── requirements.txt             ← 套件依賴
├── .env.example                 ← API Key 範例，不放真實 key
├── Dockerfile                   ← 加分項 / 講師模板提供
├── docker-compose.yml           ← 加分項 / 講師模板提供
├── src/
│   ├── extract.py               ← 資料取得
│   ├── transform.py             ← 資料清洗
│   ├── load.py                  ← 資料輸出 / 入庫
│   ├── llm_analyze.py           ← LLM 加值分析
│   └── run_pipeline.py          ← 一鍵跑完整流程
├── notebooks/
│   └── pipeline.ipynb           ← 個人完成的完整 Notebook
│                                  （關卡 1-3 的所有成果）
├── data/
│   ├── raw/                     ← 原始資料
│   └── processed/               ← 清洗後資料
├── app.py                       ← Streamlit Dashboard 模板
│                                  （已接好資料即可運行）
└── docs/
    ├── requirements_spec.md     ← 關卡 1 產出的需求規格書
    ├── pipeline.mmd             ← 期初流程圖升級版
    ├── data_source.md           ← 資料來源說明
    ├── tech_decision.md         ← 工具選型理由
    └── upgrade_plan.md          ← 後續 Docker / Airflow / GCP 升級計畫
```

### 8.2 工作坊結束時的引導打包流程（10 min，包含在總結環節中）

1. 講師帶學員將 Colab Notebook 下載 / 存到 Google Drive
2. 提供 GitHub Repo 模板連結（可當天 fork，也可 後續進階課程 後再整理）
3. 提供 README 模板 + 後續進階課程 回收清單 + LinkedIn 貼文模板

### 8.3 課後延伸路徑

工作坊產出將隨後續課程持續升級（詳見 §12.2）：

```
工作坊結束（每人帶走可跑 MVP 原型）
    │
    ├── 後續進階課程：回顧 MVP、拆成 ETL、補升級計畫
    │
    ├── 課後 / EP04：上傳 GitHub（附教學文件）
    │
    ├── 隨後續課程逐步升級 ─────────────────────
    │   ├── 學 Docker     →  容器化這個專案
    │   ├── 學 Airflow    →  加上排程自動化
    │   ├── 學 GCP        →  部署到雲端
    │   └── 結業專題      →  擴充為完整作品
    │
    └── 最終成果：一個歷經多次迭代的完整 Data Pipeline 專案
```

---

## 9. 預期成果與衡量指標

### 9.1 學員個人成果

| 成果 | 說明 |
|------|------|
| 需求規格書 | 個人產出的客戶需求分析文件 |
| 完整 Pipeline Notebook / script | 包含 ETL + AI 加值的 Colab Notebook 或 Python script |
| Dashboard 模板 | 可接入資料即時展示的 Streamlit App |
| MVP 升級素材 | `requirements_spec.md`、輸出結果、demo 截圖、`upgrade_plan.md` 草稿，供 後續進階課程 回收 |

### 9.2 衡量指標

| 指標 | 目標 |
|------|------|
| 關卡完成率（個人） | ≥ 80% 學員完成關卡 1-3 |
| Dashboard / Demo 完成率 | ≥ 80% 學員能用截圖、Notebook output、Streamlit 或口頭方式完成展示 |
| AI 工具使用率 | 100% 學員至少體驗過 ChatGPT + LLM API |
| 學員滿意度 | 活動後問卷 ≥ 4.2 / 5.0 |
| 後續進階課程 回收完成率 | ≥ 80% 學員能在 後續進階課程 補出 `mvp_review.md`、`etl_mapping.md`、`mvp_upgrade_plan.md` |

---

## 10. 所需資源

### 10.1 人力

| 角色 | 人數 | 職責 |
|------|------|------|
| 主講講師 | 1 | 開場、趨勢講座、關卡引導、總結 |
| 技術 TA | 2-3 | 巡場協助、環境問題排除、程式碼指導 |

### 10.2 場地與設備

| 項目 | 需求 |
|------|------|
| 場地 | 可容納 13 人的教室，桌椅可分 3 組排列 |
| 網路 | **穩定 Wi-Fi**（最關鍵，需支援 15+ 裝置同時連線） |
| 投影 | 投影機或大螢幕 × 1 |
| 電力 | 每組至少 1 條延長線 |

### 10.3 學員準備（事前通知）

| 項目 | 說明 |
|------|------|
| 筆電 | 自備，已安裝 Chrome 瀏覽器 |
| Google 帳號 | 用於 Google Colab |
| ChatGPT / Claude 帳號 | 免費版即可（講師準備備用帳號） |
| GitHub 帳號 | 用於後續存放作品集（可課後或 EP04 前申請） |

### 10.4 講師端準備

| 項目 | 說明 |
|------|------|
| Starter Code Notebook | 各情境的 Colab Notebook 模板（含步驟提示 + 封裝好的 helper 函式） |
| 模擬資料集 | 各情境對應的 CSV / JSON 檔（確保離線也能使用） |
| Streamlit Dashboard 模板 | 各情境的 Dashboard 模板（學員接入資料即可運行） |
| GitHub / 本地資料夾模板 | `midterm-mvp-template/`，可一鍵 fork 或下載使用（含 README、目錄結構、Docker 模板） |
| LLM API Key | 共用 API Key（設定用量上限，避免超額） |
| 情境任務卡 | 各組的情境描述 + 任務說明 |
| 備案方案 | Wi-Fi 斷線 → 離線資料集；API 掛掉 → 預先生成的 LLM 回應範例 |

### 10.5 實體教具

| 項目 | 數量 | 用途 |
|------|------|------|
| 情境任務卡 | 8 題 | 每題的產業情境、資料來源、最低輸出、進階挑戰 |
| 提示卡 | 每組 1 組 | 各關卡的 prompt 範例與技術提示 |
| 便利貼 + 奇異筆 | 每組 1 組 | 需求拆解與討論用 |

---

## 11. 風險評估與應對

| 風險 | 影響 | 機率 | 應對方案 |
|------|------|------|---------|
| Wi-Fi 不穩 | 無法使用 Colab 和 API | 中 | 準備離線資料集 + 本地 Jupyter 備案 |
| LLM API 額度用完 | 關卡 3 無法完成 | 低 | 共用 Key 設用量上限 + 預備回應範例 |
| 個人進度差異大 | 部分人卡關、部分人太快 | 高 | Starter Code 分層（基礎提示 / 進階挑戰）；組內互助機制 |
| Dashboard 門檻太高 | 多數人做不完 | 中 | 關卡 4 設為自選路線，簡報 Demo 也是完整產出 |
| 時間不夠 | 來不及 Demo | 中 | 閃電秀每人 3 分鐘嚴格計時；若超時則縮為 2 分鐘 |
| 環境安裝問題 | 前期浪費時間 | 中 | 全面使用 Colab（零安裝）+ 事前測試連結 |

---

## 12. 與 TibaMe 課程的銜接

### 12.1 工作坊運用已學技能

| 工作坊環節 | 對應已學課程模組 | 後續升級課程 |
|-----------|----------------|----------------|
| 關卡 1：MVP Scope | 期初活動 / ETL 流程圖 | 期末需求規格 |
| 關卡 2：pandas 資料清洗 | Python / pandas 基礎 | MySQL / BigQuery |
| 關卡 2：SQL 查詢載入資料 | SQL 與資料庫 | 雲端資料倉儲 |
| 關卡 3：呼叫 LLM API | API request / response 概念體驗 | Secret Manager / LLM FinOps |
| 關卡 4：MVP 打包 | README 草稿 / Streamlit 模板 / demo 素材 | 後續進階課程 回顧、GitHub、Docker / Airflow / GCP |

### 12.2 工作坊作品的持續升級路徑

工作坊產出的 MVP 原型將先在 後續進階課程 被回收與拆解，再隨後續課程模組逐步升級，最終成為結業專題的基礎：

```
期初              期中（工作坊）                  後續進階課程 與後續課程模組
────────────────────────────────────────────────────────────
紙筆流程圖     →   Colab / Notebook 手動執行    →   後續進階課程 ETL mapping → Docker 容器化
需求草稿       →   Streamlit 本地 Dashboard     →   README / repo → docker-compose 部署
資料來源想像   →   CSV / SQLite                →   MySQL / BigQuery
工具選型討論   →   手動觸發 pipeline           →   Airflow 排程自動化
團隊情境       →   個人 MVP 原型               →   GCP 雲端部署
```

> **對學員的價值**：同一個專案從期中原型跟到結業，後續進階課程 先整理成工程化路線，每學一個新技術就升級一次。最終放進履歷的不是一次性練習題，而是一個歷經多次迭代的完整作品。

---

## 13. 時程規劃（籌備）

| 階段 | 時間 | 工作項目 |
|------|------|---------|
| T-4 週 | 確認 | 確認場地、人數、日期、8 個情境題目的資料來源與最低可行輸出 |
| T-3 週 | 開發 | 製作 Starter Repo、題目卡 × 8、模擬資料集、共用 Streamlit 模板、本地 / GitHub Repo 模板 |
| T-2 週 | 測試 | 內部試跑（講師 + TA 走一遍完整流程，含 Dashboard） |
| T-1 週 | 通知 | 學員事前準備通知（帳號申請、Colab 測試連結） |
| T-3 天 | 驗證 | 場地 Wi-Fi 壓力測試、API Key 額度確認、備案方案確認 |
| 當天 | 執行 | 工作坊 |
| T+1 天 | 回饋 | 發送問卷 + 後續進階課程 回收清單 + 課後延伸教學文件（GitHub 上傳指引、Streamlit Cloud 部署教學） |

---

## 附錄 A：Demo 環節設計

### 展示形式：閃電秀（13 人 × 3 分鐘 ≈ 45 min）

每位學員都上台，嚴格計時 3 分鐘。建議結構：

| 時間 | 內容 |
|------|------|
| 30s | 我的題目解決什麼問題 |
| 30s | 資料從哪來、怎麼清 |
| 30s | LLM 在 pipeline 裡做了什麼 |
| 30s | show output（report / dashboard / 截圖） |
| 30s | 下一步怎麼升級 |
| 30s | 講師 / 同學快問快答 |

### 展示方式（擇一）

- Colab Notebook 直接 show output cell
- 截圖投影
- Streamlit Dashboard（進階）
- 口頭 + 白板（最低限度）

### 評分標準（內部評估，不公開排名）

| 維度 | 權重 | 說明 |
|------|------|------|
| Pipeline 完成度 | 30% | ETL + LLM 流程是否跑完 |
| AI 應用品質 | 25% | prompt 設計、LLM 輸出是否有用 |
| 作品打包 | 20% | README / upgrade_plan / repo 結構 |
| 洞察品質 | 15% | 分析結果是否有商業價值 |
| 展示表達 | 10% | 3 分鐘是否講清楚 |

### 獎項建議

| 獎項 | 說明 |
|------|------|
| 完成獎 | 三關卡都跑完 + README 填完 |
| 最佳 AI 應用 | Prompt 設計最有效 / LLM 輸出品質最好 |
| 最佳洞察 | 分析結果最有商業價值 |
| 同儕推薦獎 | 組內互推（最會互助的那位） |

## 附錄 B：Starter Code 技術規格

### Notebook 模板結構

```python
# === 關卡 1：MVP Scope ===
# （此段在 ChatGPT/Claude 網頁版完成，Notebook 中記錄結果）
# TODO: 貼上你的需求規格書摘要

# === 關卡 2：建立可跑 ETL ===
import pandas as pd
from utils.api_helper import fetch_data     # 封裝好的資料取得函式

# Step 1: 取得資料
raw_df = fetch_data("情境名稱")            # 一行搞定資料取得

# Step 2: 資料清洗
# TODO: 處理缺漏值
# TODO: 轉換資料型別
# TODO: 基礎統計摘要

# === 關卡 3：LLM 加值分析 ===
from utils.llm_helper import analyze_with_llm  # 封裝好的 LLM 呼叫

# Step 3: 用 LLM 分析資料
# TODO: 設計你的 prompt
# TODO: 對資料做 AI 加值分析（情緒/分類/摘要）

# === 關卡 4：MVP 打包 ===
# 路線 A: 截圖 + 口頭 Demo
# 路線 B: 接上 Streamlit Dashboard（見 app.py）
# 路線 C: 用 Docker 模板啟動
```

### Helper 函式設計原則

- `api_helper.py`：一行取得資料，內部處理 API 呼叫 / CSV 載入的細節
- `llm_helper.py`：一行呼叫 LLM，內部處理 API Key、retry、格式化
- 目的：**讓學員聚焦在「思考怎麼用」而非「怎麼接」**
