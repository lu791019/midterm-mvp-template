"""題目 6：不動產房價趨勢 — FastAPI"""
from fastapi import FastAPI, HTTPException
import sqlite3, pandas as pd, os
DB_PATH = "pipeline.db"
app = FastAPI(title="不動產房價趨勢 API")
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
    df = pd.read_sql("""SELECT 縣市, COUNT(*) as 交易量, ROUND(AVG(總價萬),1) as 均價萬 FROM cleaned_realestate GROUP BY 縣市 ORDER BY 均價萬 DESC""", conn)
    conn.close()
    return df.to_dict(orient="records")
@app.get("/analyzed")
def analyzed(limit: int = 20):
    conn = get_conn()
    df = pd.read_sql(f"""SELECT 鄉鎮市區, area_character, llm_insight FROM analyzed_realestate LIMIT {min(limit,100)}""", conn)
    conn.close()
    return df.to_dict(orient="records")
@app.get("/summary")
def summary():
    conn = get_conn()
    r = {}
    for t in ["raw_realestate","cleaned_realestate","analyzed_realestate"]:
        try: r[t] = int(pd.read_sql(f"SELECT COUNT(*) as n FROM {t}", conn)["n"][0])
        except: r[t] = 0
    conn.close()
    return r
@app.get("/report")
def report():
    if not os.path.exists("output/report.md"): raise HTTPException(404, "report.md 不存在")
    with open("output/report.md") as f: return {"report": f.read()}
