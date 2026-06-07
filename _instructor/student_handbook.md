# LLM × DE MVP Builder 實戰營｜學員手冊

> 給你（學員）的：今天要做什麼、怎麼做、產出什麼。

---

## 活動是什麼

**情境**：你是「資料解決方案顧問」，要用已學的 Python / pandas / SQL 做出一條 Mini Data Pipeline。

**目標**：每人選一個題目，在半天內完成一條可跑的 pipeline，帶走一個作品集。

**時長**：約 4.5 小時（10:00-16:00，含午休）

**形式**：個人實作 + 3 組智囊團互相討論

---

## 你要做什麼

選一個題目，照著 Notebook 跑完整條 pipeline：

```
CSV → pandas 清洗 → SQLite（raw/cleaned/analyzed 三表）→ SQL 查詢 → LLM 分析 → 報告
```

### 6 個題目

| # | 題目 | 適合誰 |
|---|------|--------|
| 1 | 零售 POS 銷售分析 | 想看銷售排行、客戶分析 |
| 2 | B2C 電商競品比價 | 想做跨平台價格比較 |
| 3 | 音樂串流趨勢分析 | 想分析 Spotify / YouTube / TikTok |
| 4 | 叫車服務交通熱點 | 想做地理 + 時間分析（最複雜） |
| 5 | 求職媒合薪資洞察 | 想看資料領域薪資行情 |
| 6 | 不動產房價趨勢 | 想分析台灣房價（中文資料） |

> 每題都有 2,000 筆真實資料、需求規格書、Notebook、API、Dashboard。
> 詳細規格見各題的 `requirements_spec.md`。

---

## 活動流程

| 時段 | 做什麼 |
|------|--------|
| 10:00-10:40 | 聽開場：活動目標、repo 導覽、完整 pipeline demo |
| 10:40-10:45 | 休息 |
| 10:45-11:05 | 聽講解：資料清洗重點 + pandas 常見坑 |
| 11:05-11:55 | **實作**：選題 → 開環境 → ETL 清洗 → 產出 processed data |
| 11:55-12:00 | 休息 |
| 12:00-13:30 | 午休（想繼續做也可以） |
| 13:30-13:50 | 聽講解：LLM API demo + prompt 設計 |
| 13:50-14:40 | **實作**：LLM 分析 → 產出 report.md |
| 14:40-14:45 | 休息 |
| 14:45-15:00 | 聽講解：打包教學（README + Demo 怎麼講） |
| 15:00-15:15 | **實作**：填 README + upgrade_plan + 準備 demo |
| 15:15-16:00 | **閃電秀**：每人 3 分鐘 Demo |

---

## Step by Step

### Step 1：環境準備

```bash
git clone https://github.com/lu791019/midterm-mvp-template.git
cd midterm-mvp-template
```

或下載 ZIP 解壓縮。

### Step 2：選題

看上面的題目表，選一個。打開 `data/raw/topic_{N}/requirements_spec.md` 看需求。

### Step 3：開 Notebook

打開 `data/raw/topic_{N}/pipeline_starter.ipynb`：
- **Colab**：到 colab.google → 上傳 → 選檔案
- **本地**：`jupyter notebook data/raw/topic_{N}/pipeline_starter.ipynb`

### Step 4：照著做

Notebook 裡有 10 個 Section，標記如下：
- `TODO 🟢`：簡單，有相關程式碼可參考
- `TODO 🟡`：中等，有別的情境範例教語法
- `TODO 🔴`：較難，有骨架填空
- `（不需要改）`：直接跑

### Step 5：打包

跑完後，填寫：
- `docs/upgrade_plan.md`：後續升級計畫
- README：用 `docs/README_TEMPLATE.md` 模板

### Step 6：Demo

3 分鐘閃電秀：
1. 30s — 題目解決什麼問題
2. 30s — 資料從哪來、怎麼清
3. 30s — LLM 做了什麼
4. 30s — show output
5. 30s — 下一步怎麼升級
6. 30s — 快問快答

---

## AI 使用規範

| 用法 | 是否允許 |
|------|---------|
| 用 ChatGPT/Claude 生成 pandas/SQL | ✅ 允許 |
| 用 AI debug 錯誤 | ✅ 允許 |
| 用 LLM API 做分類/摘要 | ✅ 鼓勵 |
| 完全貼上不懂的程式碼 | ⚠️ 不建議（Demo 時要能說明） |

> prompt 模板見 `docs/ai_prompts.md`

---

## 遇到問題？

| 狀況 | 怎麼辦 |
|------|--------|
| 不會 pandas 語法 | 看 Notebook 裡的範例提示，或問 ChatGPT |
| 不知道 SQL 怎麼寫 | 看 Notebook Section 3 的範例 |
| API Key 沒有 | 沒關係，LLM 有 fallback 規則版 |
| 跑不起來 | 找同組的人討論，或舉手問 TA |
| 做不完 | 沒關係！完成到哪就 Demo 到哪，repo 帶走課後繼續 |

---

## 你會帶走什麼

- 一個完整的 **pipeline.db**（SQLite 資料庫，含三張表）
- 一份 **分析報告**（output/report.md）
- 一個 **GitHub repo**（後續課程持續升級）
- 一段 **3 分鐘 Demo 經驗**

> 這不是練習題，是放進履歷的作品集起點。
