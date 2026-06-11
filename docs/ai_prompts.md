# AI Prompt Templates

> 期中活動允許使用 ChatGPT / Claude / AI Coding。原則是：可以請 AI 協助釐清、生成草稿、debug、改寫報告，但學員最後要能說明自己的 pipeline。

## 1. MVP Scope Prompt

```text
你現在扮演一位資料工程顧問的客戶。

我的題目是：「{題目名稱}」。
請用客戶角度連續追問我 5 個問題，幫我把需求收斂成今天 4 小時內可以完成的 MVP。

請特別追問：
1. 業務問題是什麼？
2. 使用者是誰？
3. 資料來源是什麼？
4. 今天最小可交付成果是什麼？
5. 怎麼判斷這個 MVP 有價值？

最後請幫我整理成：
- Problem
- User / Stakeholder
- Data Source
- MVP Scope
- Success Metric
```

## 2. Data Understanding Prompt

```text
我有一份資料，欄位如下：

{貼上欄位名稱與前 5 筆資料}

請幫我判斷：
1. 每個欄位可能代表什麼？
2. 哪些欄位適合拿來做分析？
3. 可能有哪些資料品質問題？
4. 我應該先做哪些清理？
5. 這份資料可以產出哪些 MVP 指標？

請用初學者看得懂的方式回答。
```

## 3. Pandas / SQL Coding Prompt

```text
我正在做一個資料工程 MVP，題目是：「{題目名稱}」。

資料欄位：
{欄位說明}

我想完成這個轉換：
{描述你要做的清洗或統計}

請幫我產生 Python pandas 程式碼。
要求：
1. 程式碼要有註解。
2. 不要使用太進階的寫法。
3. 請說明每一步在做什麼。
4. 如果有缺值或型別錯誤，請一起處理。
```

## 4. Debug Prompt

```text
我執行 Python 程式遇到錯誤。

錯誤訊息：
{貼上完整錯誤}

相關程式碼：
{貼上 20-40 行相關程式}

請幫我：
1. 用白話解釋錯誤原因。
2. 指出最可能出錯的那一行。
3. 給我一個最小修改版本。
4. 告訴我如何確認修好了。
```

## 5. LLM Analysis Prompt

```text
你是一位資料分析顧問。

請根據以下資料，產生一段可以放進 MVP 報告的分析。

題目：{題目名稱}
使用者：{使用者}
資料摘要：
{貼上統計表或前幾筆資料}

請輸出：
1. 三個重點洞察
2. 一個可能的業務建議
3. 一個後續值得追蹤的指標

限制：
- 不要捏造資料中沒有的事實。
- 如果資料不足，請明確說明限制。
- 用繁體中文回答。
```

## 6. Classification Prompt

```text
請把以下文字分類成固定標籤。

可用標籤：
{標籤列表}

文字：
{文字內容}

請只輸出 JSON：
{
  "label": "...",
  "confidence": 0.0,
  "reason": "..."
}
```

## 7. Pipeline Documentation Prompt（最重要！）

> 把你的 Notebook 跑完後的資訊貼進去，AI 幫你填完整份 Pipeline Documentation。

```text
你是一位資料工程師。請根據我提供的資訊，幫我填寫一份 Pipeline Documentation。

模板在最下方，請照格式輸出完整的 Markdown，把所有 {placeholder} 換成真實內容。

---

以下是我的 Pipeline 資訊：

【題目】
{貼上你的題目名稱和情境}

【原始資料欄位】（從 df.dtypes 或 df.head() 複製）
{貼上 df.dtypes 的輸出}

【清洗邏輯】（你在 Section 2 做了什麼）
{例如：dropna(subset=["description", "customer_id"])、quantity > 0、新增 total_amount}

【清洗前後筆數】
- raw: {N} 筆
- cleaned: {N} 筆
- analyzed: {N} 筆

【SQL 統計】（你在 Section 3 寫的 SQL 或 pandas 查詢）
{貼上你的 SQL 或 describe}

【LLM 分析】
- 用了什麼模型：{GPT-4o-mini / fallback}
- 輸入哪個欄位：{欄位名}
- 分類標籤：{標籤列表}
- 新增欄位：category, llm_insight

【API Endpoints】（從 api.py 看）
{貼上 api.py 的 @app.get 那幾行}

---

請用以下模板格式輸出（不要省略任何 section）：

# {專案名稱} — Pipeline Documentation

## 1. Overview
（表格：業務情境、Pipeline 目標、使用者、資料來源、資料量）

## 2. Architecture / Data Flow
（ASCII 流程圖 + 表格：每階段的輸入→處理→輸出）

## 3. Data Dictionary
（三張表各自的欄位定義，包含型別、說明、範例值）

## 4. Transform Logic
（表格：每步清洗的程式碼、理由、影響筆數）

## 5. Data Quality
（完整性、一致性、準確性的檢查結果）

## 6. LLM Integration
（模型、Prompt 策略、Fallback、處理筆數）

## 7. API Endpoints
（Method、Path、說明、回傳格式）

## 8. How to Run
（完整指令，從 cd 到 uvicorn）

## 9. Design Decisions
（每個技術選擇的理由和 trade-off）

## 10. Known Limitations & Next Steps
（目前限制 + 升級路線）

請用繁體中文，表格對齊，不要省略。
```

> 💡 **懶人版**：如果你不想一個一個貼，直接把整個 Notebook 的輸出截圖或文字複製給 AI，加一句「請根據以上 Notebook 內容，幫我填寫 docs/README_TEMPLATE.md 的所有 section」也行。

## 8. AI Coding 使用提醒

- 可以請 AI 產生草稿，但要自己讀懂後再貼進專案。
- 不要一次貼整個專案要求 AI 全部重寫。
- 優先問「這段錯在哪」「這個函式怎麼改」「這個欄位怎麼清」。
- Demo 時要能說明每一步：資料怎麼來、怎麼清、LLM 做了什麼、最後輸出什麼。
