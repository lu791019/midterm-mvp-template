"""題目 5：求職媒合薪資洞察 — FastAPI"""
from fastapi import FastAPI, HTTPException
import sqlite3, pandas as pd, os
DB_PATH = "pipeline.db"
app = FastAPI(title="求職媒合薪資洞察 API")
def get_conn():
    if not os.path.exists(DB_PATH): raise HTTPException(500, "pipeline.db 不存在")
    return sqlite3.connect(DB_PATH)
@app.get("/health")
def health():
    conn = get_conn()
    tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
    conn.close()
    return {"status": "ok", "tables": tables["name"].tolist()}
@app.get("/stats")
def stats():
    conn = get_conn()
    df = pd.read_sql("""SELECT job_category, COUNT(*) as jobs, ROUND(AVG(salary_in_usd),0) as avg_salary FROM cleaned_jobs GROUP BY job_category ORDER BY avg_salary DESC""", conn)
    conn.close()
    return df.to_dict(orient="records")
@app.get("/analyzed")
def analyzed(limit: int = 20):
    conn = get_conn()
    df = pd.read_sql(f"""SELECT job_title, field, llm_insight FROM analyzed_jobs LIMIT {{min(limit,100)}}""", conn)
    conn.close()
    return df.to_dict(orient="records")
@app.get("/summary")
def summary():
    conn = get_conn()
    r = {}
    for t in ["raw_jobs","cleaned_jobs","analyzed_jobs"]:
        try: r[t] = int(pd.read_sql(f"SELECT COUNT(*) as n FROM {t}", conn)["n"][0])
        except: r[t] = 0
    conn.close()
    return r
@app.get("/report")
def report():
    if not os.path.exists("output/report.md"): raise HTTPException(404, "report.md 不存在")
    with open("output/report.md") as f: return {"report": f.read()}
