# Handoff — 期中活動 repo 接手文件

> 更新日期：2026-06-09
> GitHub: https://github.com/lu791019/midterm-mvp-template

## 活動結構變更（最新決定）

原本是全天活動，**已改成半天**：

| 時段 | 內容 |
|---|---|
| 10:30-12:00 | 3 組專題報告 + 討論（期末題目審查，每組 30 min） |
| 12:00-13:30 | 午休 |
| **13:30-16:30** | **黑客松（3 小時，MVP Builder 實作）** |
| 16:30 | 結束 |

## 黑客松 3 小時時程（已定案）

| 時段 | 分鐘 | 內容 | Notebook |
|---|---|---|---|
| 13:30-13:55 | 25 | 講解：開場 + Pipeline Demo + Medallion + 選題 | |
| **13:55-14:40** | **45** | **實作 1**：Extract & Load → Bronze → Transform → Silver → SQL | Section 0-3 |
| 14:40-14:45 | 5 | 交流 | |
| 14:45-14:55 | 10 | 講解：LLM + Prompt + API 概念 | |
| **14:55-15:40** | **45** | **實作 2**：LLM → Gold → 驗證 → 報告 → 打包 → FastAPI | Section 4-8 |
| 15:40-15:45 | 5 | 準備 Demo | |
| **15:45-16:15** | **30** | **Demo**：閃電秀 | |
| 16:15-16:30 | 15 | 收尾：升級路線 + Dashboard 回家做 | |

## 下個 session 要做的（優先順序）

### 🔴 必做

1. **簡報 HTML 重做**（`_instructor/mvp_builder_slides.html`）
   - 時程從全天改成 3 小時版
   - 26 張 → 壓縮到 ~15 張
   - 業界概念頁保留但精簡合併
   - 實作段從 4 段合併為 2 段
   - `/stats` 改成 `/stats/products`（配合 api.py 實際路徑）

2. **講稿重寫**（`_instructor/speaker_notes.md`）
   - 對齊新的 3 小時時程
   - 26 段 → ~13 段

3. **講師手冊更新**（`_instructor/facilitator_guide.md`）
   - 時間表對齊
   - 新增上午專題報告的引導（評估表、確認項目）

4. **學員手冊更新**（`_instructor/student_handbook.md`）
   - 時間表對齊
   - 新增上午報告準備事項

### 🟡 應做

5. **新增專題報告評估表**
   - 學員報告需涵蓋：動機、業務問題、資料來源、取得方式、資料樣貌、預期產出、技術可行性、分工、時程
   - 給講師的評估 checklist

6. **新增學員事前通知文件**
   - 上午報告要準備什麼（投影片 + 至少看過資料 + 試過取得方式）
   - 下午黑客松要準備什麼（GitHub 帳號 + 筆電 + Google 帳號）

### 🟢 可選

7. **README 更新**時間描述（目前寫全天）
8. **舊簡報清理**（`_instructor/midterm_workshop_slides.md` 可刪，已被 HTML 取代）
9. **Notebook 加術語**（Bronze/Silver/Gold 寫進 Markdown cell）

## 已完成且不需要改的

- ✅ 6 題資料（CSV 2,000 筆）
- ✅ 6 題 requirements_spec.md
- ✅ 6 題 pipeline_starter.ipynb（三級難度）
- ✅ 6 題 solution（驗證跑通）
- ✅ 6 題 api.py（已修 numpy.int64 bug，全部驗證通過）
- ✅ 6 題 app.py
- ✅ docs/（data_sources / topic_catalog / ai_prompts / repo_format / pipeline.mmd / README_TEMPLATE / upgrade_plan）
- ✅ 術語一致性（Bronze=Raw/Landing, Silver=Staging/ODS, Gold=Mart/Application）
- ✅ 無孤兒、無舊題號、無 EP01

## 關鍵設計決策（不要改）

- 活動名稱：**LLM × DE MVP Builder 實戰工作坊**
- 6 題（topic 1-6）：零售/電商/音樂/叫車/求職/房價
- Pipeline：CSV → SQLite(Bronze/Silver/Gold) → SQL → LLM → FastAPI
- Dashboard（Streamlit/ipywidgets）= 回家做，不在活動必做範圍
- Notebook 三級難度：🟢簡單 🟡中等 🔴較難
- 前 4 格有 `# 相關程式碼`（循序漸進）
- api.py 和 app.py 是 Section 8/9 的 solution
