"""
題目 1：餐飲連鎖 POS 庫存優化 — FastAPI API

啟動方式：
    uvicorn api:app --reload --port 8000

需要先跑完 pipeline.ipynb 產出 pipeline.db。
"""

from fastapi import FastAPI, HTTPException
import sqlite3
import pandas as pd
import os

DB_PATH = "pipeline.db"
app = FastAPI(title="餐飲顧客評論分析 API", version="1.0")


def get_conn():
    if not os.path.exists(DB_PATH):
        raise HTTPException(status_code=500, detail="pipeline.db 不存在，請先跑完 pipeline.ipynb")
    return sqlite3.connect(DB_PATH)


@app.get("/health")
def health():
    """確認 API 和資料庫狀態"""
    conn = get_conn()
    tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
    conn.close()
    return {
        "status": "ok",
        "db": DB_PATH,
        "tables": tables["name"].tolist()
    }


@app.get("/stats")
def get_stats():
    """各餐廳評分統計（從 cleaned_reviews 查詢）"""
    conn = get_conn()
    df = pd.read_sql("""
        SELECT
            Restaurant,
            COUNT(*) as review_count,
            ROUND(AVG(Rating), 2) as avg_rating,
            ROUND(AVG(is_negative) * 100, 1) as negative_pct
        FROM cleaned_reviews
        GROUP BY Restaurant
        HAVING review_count >= 3
        ORDER BY avg_rating ASC
    """, conn)
    conn.close()
    return df.to_dict(orient="records")


@app.get("/analyzed")
def get_analyzed(limit: int = 20):
    """LLM 分析結果（從 analyzed_reviews 查詢）"""
    conn = get_conn()
    df = pd.read_sql(f"""
        SELECT Restaurant, Rating, sentiment, topic, llm_summary
        FROM analyzed_reviews
        LIMIT {min(limit, 100)}
    """, conn)
    conn.close()
    return df.to_dict(orient="records")


@app.get("/summary")
def get_summary():
    """Pipeline 摘要統計"""
    conn = get_conn()
    result = {}
    for table in ["raw_reviews", "cleaned_reviews", "analyzed_reviews"]:
        try:
            count = pd.read_sql(f"SELECT COUNT(*) as n FROM {table}", conn)["n"][0]
            result[table] = count
        except Exception:
            result[table] = 0

    if result["analyzed_reviews"] > 0:
        topics = pd.read_sql("""
            SELECT topic, COUNT(*) as count
            FROM analyzed_reviews
            GROUP BY topic
            ORDER BY count DESC
        """, conn)
        result["topic_distribution"] = topics.to_dict(orient="records")

        sentiments = pd.read_sql("""
            SELECT sentiment, COUNT(*) as count
            FROM analyzed_reviews
            GROUP BY sentiment
            ORDER BY count DESC
        """, conn)
        result["sentiment_distribution"] = sentiments.to_dict(orient="records")

    conn.close()
    return result


@app.get("/report")
def get_report():
    """讀取 output/report.md"""
    report_path = "output/report.md"
    if not os.path.exists(report_path):
        raise HTTPException(status_code=404, detail="report.md 不存在，請先跑完 pipeline.ipynb")
    with open(report_path, "r") as f:
        content = f.read()
    return {"report": content}
