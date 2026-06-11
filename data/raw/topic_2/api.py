"""題目 2：B2C 電商競品比價 — FastAPI"""
from fastapi import FastAPI, HTTPException
import sqlite3, pandas as pd, os
DB_PATH = "pipeline.db"
app = FastAPI(title="B2C 電商競品比價 API")
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
    df = pd.read_sql("""SELECT title, amazon_price, flipkart_price, ROUND(price_diff,2) as diff FROM cleaned_products ORDER BY ABS(price_diff) DESC LIMIT 20""", conn)
    conn.close()
    return df.to_dict(orient="records")
@app.get("/analyzed")
def analyzed(limit: int = 20):
    conn = get_conn()
    df = pd.read_sql(f"""SELECT title, category, llm_insight FROM analyzed_products LIMIT {min(limit,100)}""", conn)
    conn.close()
    return df.to_dict(orient="records")
@app.get("/summary")
def summary():
    conn = get_conn()
    r = {}
    for t in ["raw_products","cleaned_products","analyzed_products"]:
        try: r[t] = int(pd.read_sql(f"SELECT COUNT(*) as n FROM {t}", conn)["n"][0])
        except: r[t] = 0
    conn.close()
    return r
@app.get("/report")
def report():
    if not os.path.exists("output/pipeline_doc.md"): raise HTTPException(404, "pipeline_doc.md 不存在")
    with open("output/pipeline_doc.md") as f: return {"report": f.read()}
