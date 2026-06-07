# LLM x DE MVP Template

> 期中工作坊 starter repo。目標是在半天內完成一個可跑、可展示、後續可升級的個人資料工程 MVP。

這個模板是期中快速體驗用，不代表你現在要理解所有工程細節。GitHub、VS Code / WSL、Python package、Docker、部署方式會在後續帶狀課逐步拆解；期中先求能跑出結果、能展示、能在 EP01 回來整理。

活動方式是：**每人選一個題目做出自己的 MVP，組內可以互相討論與除錯**。你可以使用 ChatGPT / Claude / AI Coding，但最後要能說明自己的 pipeline。

## 專案目標

用一條最小 pipeline 完成：

```text
raw data -> transform -> LLM analyze -> report / dashboard
```

本模板預設用「評論文字分類」作為示範資料。學員可以替換成自己的期初情境資料。

題庫與資料來源規格見：

- [docs/topic_catalog.md](docs/topic_catalog.md)
- [docs/repo_format.md](docs/repo_format.md)
- [docs/ai_prompts.md](docs/ai_prompts.md)

## 快速開始

如果使用 GitHub：

```bash
git clone <repo-url>
cd midterm-mvp-template
```

如果還不熟 GitHub，也可以下載 zip 後解壓縮，再進入資料夾。

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.run_pipeline
```

成功後會產生：

```text
data/processed/processed_reviews.csv
output/report.md
```

## Streamlit 展示

```bash
streamlit run app.py
```

## Docker 模板啟動

Docker 是加分項，只用來先體驗「一鍵啟動」的價值。若你已經裝好 Docker，可以試：

```bash
docker compose up --build
```

## LLM API

工作坊當天可以先使用 fallback 規則版分析，不需要 API key 也能跑。

若要接 OpenAI，建立 `.env`：

```bash
cp .env.example .env
```

填入：

```text
OPENAI_API_KEY=你的_key
```

再自行改寫 `src/llm_analyze.py` 的 `analyze_text()`。

可用 prompt 範本見 [docs/ai_prompts.md](docs/ai_prompts.md)。

## 期中當天四關卡

| 關卡 | 要做什麼 | 產出 |
|---|---|---|
| 1. MVP Scope | 選題、釐清使用者、資料來源、最小交付 | `docs/requirements_spec.md` |
| 2. ETL | 讀資料、清資料、產出 processed data | `data/processed/*` |
| 3. LLM 加值 | 分類、摘要、洞察或報告生成 | `output/report.md` |
| 4. MVP 打包 | 準備 demo、README 草稿、升級計畫 | `docs/upgrade_plan.md` |

## 每人最低完成標準

- 能執行 `python -m src.run_pipeline`
- 有一份 processed data
- 有一份 LLM / fallback 分析結果
- 能用 1 分鐘說明自己的題目、資料、pipeline、輸出
- 完成 `docs/requirements_spec.md` 和 `docs/upgrade_plan.md`

## 後續升級

請先填寫 [docs/upgrade_plan.md](docs/upgrade_plan.md)。EP01 會回收這份文件，協助你把期中 MVP 拆成 ETL 架構與正式升級路線：

- EP01：回顧 MVP，拆成 Extract / Transform / Load / LLM 加值
- 學完 Docker：容器化 pipeline + dashboard
- 學完 Airflow：把 `run_pipeline.py` 改成 DAG
- 學完 MySQL / BigQuery：把 CSV 換成資料庫
- 學完 GCP：部署到雲端
