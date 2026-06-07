# Midterm MVP Starter Repo Format

> 目的：讓學員 clone / 下載後，能依照固定步驟完成自己的期中 MVP。期中先求可跑、可展示、可在 EP01 回收；GitHub、Docker、正式 package 化會在後續課程細教。

## 使用流程

```bash
git clone <repo-url>
cd midterm-mvp-template
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.run_pipeline
streamlit run app.py
```

如果尚未學 Git / GitHub，也可以直接下載 zip，解壓縮後照同樣步驟執行。

## 標準資料夾

```text
midterm-mvp-template/
├── README.md
├── requirements.txt
├── .env.example
├── Dockerfile                    # 加分項，期中不要求理解
├── docker-compose.yml            # 加分項，期中不要求理解
├── app.py                        # Streamlit demo
├── data/
│   ├── raw/                      # 原始資料
│   └── processed/                # 清洗後資料
├── docs/
│   ├── requirements_spec.md      # 關卡 1：需求與 MVP scope
│   ├── data_source.md            # 資料來源與欄位說明
│   ├── pipeline.mmd              # 資料流程圖
│   ├── tech_decision.md          # 工具選型與取捨
│   ├── upgrade_plan.md           # 後續升級路線
│   ├── topic_catalog.md          # 題庫與資料來源
│   ├── ai_prompts.md             # AI prompt 範本
│   └── repo_format.md            # 本文件
├── output/
│   └── report.md                 # LLM 分析或顧問報告
└── src/
    ├── extract.py
    ├── transform.py
    ├── load.py
    ├── llm_analyze.py
    └── run_pipeline.py
```

## 學員當天最小交付

| 必交 | 說明 |
|---|---|
| `docs/requirements_spec.md` | 題目、使用者、資料來源、MVP scope、成功指標 |
| `processed/*` | 至少一份處理後資料 |
| `output/report.md` | LLM 分析結果、摘要、分類或顧問建議 |
| `docs/upgrade_plan.md` | 後續如何升級成 GitHub / Docker / Airflow / GCP 版本 |
| demo 素材 | 截圖、Notebook output、Streamlit 畫面或 1 分鐘口頭 demo |

## 程式檔案責任

| 檔案 | 負責內容 |
|---|---|
| `src/extract.py` | 讀取 CSV / JSON / API / RSS，產生 raw dataframe |
| `src/transform.py` | 清理缺值、欄位轉換、基本統計、產生 processed dataframe |
| `src/llm_analyze.py` | 呼叫 LLM 或 fallback 規則，產生分類 / 摘要 / 洞察 |
| `src/load.py` | 輸出 CSV / markdown report / dashboard input |
| `src/run_pipeline.py` | 串起 extract → transform → LLM analyze → load |
| `app.py` | 用 Streamlit 展示輸出結果 |

## 題目切換方式

期中最簡單做法是每題共用同一套檔案名稱，只替換資料與邏輯：

1. 在 `docs/requirements_spec.md` 寫清楚自己選的題目。
2. 把題目資料放入 `data/raw/`。
3. 修改 `src/extract.py` 讀取該題資料。
4. 修改 `src/transform.py` 清洗欄位。
5. 修改 `src/llm_analyze.py` 的 prompt 或 fallback 規則。
6. 執行 `python -m src.run_pipeline`。
7. 用 `streamlit run app.py` 或截圖 / 報告 demo。

## AI 使用紀錄

學員可以使用 AI Coding，但要能說明產出。建議把關鍵 prompt 與修正結果記錄在：

- `docs/requirements_spec.md`
- `docs/tech_decision.md`
- `output/report.md`

可用 prompt 範本見 `docs/ai_prompts.md`。
