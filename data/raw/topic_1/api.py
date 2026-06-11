"""
題目 1：零售 POS 銷售分析 — FastAPI API

啟動方式：
    cd data/raw/topic_1
    uvicorn api:app --reload --port 8000

需要先跑完 pipeline（starter 或 solution）產出 pipeline.db。

API 做什麼：
    把 SQLite 裡的分析結果包裝成 endpoint，讓前端（Streamlit）或其他人透過網址取得資料。
    這就是 DE 的做法：資料庫 → API → 前端，不是直接傳 CSV。
"""

from fastapi import FastAPI, HTTPException
import sqlite3
import pandas as pd
import os

DB_PATH = "pipeline.db"
app = FastAPI(title="零售銷售分析 API", version="1.0")


def get_conn():
    if not os.path.exists(DB_PATH):
        raise HTTPException(status_code=500, detail="pipeline.db 不存在，請先跑完 Notebook")
    return sqlite3.connect(DB_PATH)


@app.get("/health")
def health():
    """確認 API 和資料庫狀態"""
    conn = get_conn()
    tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
    conn.close()
    return {"status": "ok", "tables": tables["name"].tolist()}


@app.get("/stats/products")
def product_stats(limit: int = 20):
    """商品銷售排行"""
    conn = get_conn()
    df = pd.read_sql(f"""
        SELECT description, COUNT(*) as order_count,
               SUM(quantity) as total_qty,
               ROUND(SUM(total_amount), 2) as total_revenue
        FROM cleaned_orders
        GROUP BY description
        ORDER BY total_revenue DESC
        LIMIT {min(limit, 100)}
    """, conn)
    conn.close()
    return df.to_dict(orient="records")


@app.get("/stats/countries")
def country_stats():
    """各國銷售統計"""
    conn = get_conn()
    df = pd.read_sql("""
        SELECT country, COUNT(DISTINCT customer_id) as customers,
               COUNT(*) as orders, ROUND(SUM(total_amount), 2) as revenue
        FROM cleaned_orders
        GROUP BY country ORDER BY revenue DESC
    """, conn)
    conn.close()
    return df.to_dict(orient="records")


@app.get("/analyzed")
def get_analyzed(limit: int = 20):
    """LLM 品類分類結果"""
    conn = get_conn()
    df = pd.read_sql(f"""
        SELECT description, quantity, total_amount, category, llm_insight
        FROM analyzed_orders LIMIT {min(limit, 100)}
    """, conn)
    conn.close()
    return df.to_dict(orient="records")


@app.get("/summary")
def get_summary():
    """Pipeline 三表摘要"""
    conn = get_conn()
    result = {}
    for table in ["raw_orders", "cleaned_orders", "analyzed_orders"]:
        try:
            result[table] = int(pd.read_sql(f"SELECT COUNT(*) as n FROM {table}", conn)["n"][0])
        except Exception:
            result[table] = 0
    conn.close()
    return result


@app.get("/report")
def get_report():
    """讀取 output/pipeline_doc.md"""
    if not os.path.exists("output/pipeline_doc.md"):
        raise HTTPException(status_code=404, detail="pipeline_doc.md 不存在")
    with open("output/pipeline_doc.md") as f:
        return {"report": f.read()}
