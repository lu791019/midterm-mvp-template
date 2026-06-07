"""
題目 1：餐飲連鎖 POS 庫存優化 — Streamlit Dashboard

啟動方式（二擇一）：

    方法 A：直接讀 SQLite（不需要 FastAPI）
        streamlit run app.py

    方法 B：透過 FastAPI（需要先啟動 api.py）
        1. uvicorn api:app --reload --port 8000
        2. streamlit run app.py -- --use-api

需要先跑完 pipeline.ipynb 產出 pipeline.db。
"""

import streamlit as st
import pandas as pd
import sqlite3
import os
import sys

st.set_page_config(page_title="餐飲評論分析 Dashboard", layout="wide")
st.title("🍽️ 餐飲連鎖顧客評論分析 Dashboard")

USE_API = "--use-api" in sys.argv
DB_PATH = "pipeline.db"


def load_from_db():
    """直接從 SQLite 讀取"""
    if not os.path.exists(DB_PATH):
        st.error("❌ pipeline.db 不存在，請先跑完 pipeline.ipynb")
        st.stop()
    conn = sqlite3.connect(DB_PATH)
    return conn


def load_from_api():
    """從 FastAPI 讀取"""
    import requests
    base_url = "http://localhost:8000"
    try:
        requests.get(f"{base_url}/health", timeout=3)
        return base_url
    except Exception:
        st.error("❌ FastAPI 未啟動，請先執行 uvicorn api:app --reload --port 8000")
        st.stop()


# === 載入資料 ===
if USE_API:
    import requests
    base_url = load_from_api()
    st.caption("📡 資料來源：FastAPI API")

    stats = pd.DataFrame(requests.get(f"{base_url}/stats").json())
    analyzed = pd.DataFrame(requests.get(f"{base_url}/analyzed?limit=100").json())
    summary = requests.get(f"{base_url}/summary").json()
else:
    conn = load_from_db()
    st.caption("📂 資料來源：SQLite pipeline.db")

    stats = pd.read_sql("""
        SELECT Restaurant, COUNT(*) as review_count,
               ROUND(AVG(Rating), 2) as avg_rating,
               ROUND(AVG(is_negative) * 100, 1) as negative_pct
        FROM cleaned_reviews
        GROUP BY Restaurant HAVING review_count >= 3
        ORDER BY avg_rating ASC
    """, conn)

    try:
        analyzed = pd.read_sql("SELECT * FROM analyzed_reviews", conn)
    except Exception:
        analyzed = pd.DataFrame()

    summary = {}
    for table in ["raw_reviews", "cleaned_reviews", "analyzed_reviews"]:
        try:
            summary[table] = pd.read_sql(f"SELECT COUNT(*) as n FROM {table}", conn)["n"][0]
        except Exception:
            summary[table] = 0

# === Pipeline 狀態 ===
st.subheader("📊 Pipeline 狀態")
col1, col2, col3 = st.columns(3)
col1.metric("Raw", summary.get("raw_reviews", 0))
col2.metric("Cleaned", summary.get("cleaned_reviews", 0))
col3.metric("Analyzed", summary.get("analyzed_reviews", 0))

# === 餐廳評分排行 ===
st.subheader("📊 餐廳評分排行（評分最低 → 最高）")
if not stats.empty:
    st.bar_chart(stats.head(15).set_index("Restaurant")["avg_rating"])
    st.dataframe(stats.head(15), use_container_width=True)

# === LLM 分析結果 ===
if not analyzed.empty:
    st.subheader("🤖 LLM 分析結果")

    col1, col2 = st.columns(2)
    with col1:
        st.write("**情緒分佈**")
        sentiment_counts = analyzed["sentiment"].value_counts()
        st.bar_chart(sentiment_counts)

    with col2:
        st.write("**主題分佈**")
        topic_counts = analyzed["topic"].value_counts()
        st.bar_chart(topic_counts)

    st.write("**分析明細（前 20 筆）**")
    display_cols = [c for c in ["Restaurant", "Rating", "sentiment", "topic", "llm_summary"] if c in analyzed.columns]
    st.dataframe(analyzed[display_cols].head(20), use_container_width=True)
else:
    st.info("💡 尚未完成 LLM 分析（pipeline.ipynb Section 4）")

# === 報告 ===
report_path = "output/report.md"
if os.path.exists(report_path):
    st.subheader("📄 顧問報告")
    with open(report_path, "r") as f:
        st.markdown(f.read())
