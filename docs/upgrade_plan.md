# Upgrade Plan

## Current Version

- 手動執行 `python -m src.run_pipeline`
- CSV 儲存
- fallback 規則版分析
- Streamlit 本地展示

## EP01 Review

- [ ] 我能用 3 句話說明自己的 MVP 解決什麼問題
- [ ] 我能說明資料來源是什麼，以及目前怎麼取得資料
- [ ] 我能把目前程式拆成 Extract / Transform / Load / LLM 加值
- [ ] 我能指出目前最脆弱、最需要後續課程升級的一段
- [ ] 我能把後續想升級的項目寫成 `mvp_upgrade_plan.md`

## After Docker

- [ ] 改善 Dockerfile
- [ ] 用 docker-compose 同時啟動 pipeline + dashboard
- [ ] 加入 volume 保存輸出資料

## After Database

- [ ] 把 CSV 換成 SQLite / MySQL
- [ ] 補資料表 schema
- [ ] 補 SQL 指標查詢

## After Airflow

- [ ] 把 `run_pipeline.py` 拆成 DAG tasks
- [ ] 設定每日或每週排程
- [ ] 加入失敗重跑與 log

## After GCP

- [ ] 把資料放進 BigQuery
- [ ] 把 dashboard 部署到 Cloud Run 或其他服務
- [ ] 把 API key 放進 Secret Manager
