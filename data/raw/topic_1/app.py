"""
題目 1：零售 POS 銷售分析 — Streamlit Dashboard

啟動方式：
    cd data/raw/topic_1
    streamlit run app.py

app.py 做什麼：
    把你的分析結果變成互動式 Dashboard，這就是交給客戶看的東西。
    可以直接讀 SQLite（不需要 FastAPI），也可以透過 API。

需要先跑完 pipeline（starter 或 solution）產出 pipeline.db。
"""

import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="零售銷售分析", layout="wide")
st.title("🛒 零售 POS 銷售分析 Dashboard")

DB_PATH = "pipeline.db"

if not os.path.exists(DB_PATH):
    st.error("❌ pipeline.db 不存在，請先跑完 Notebook")
    st.stop()

conn = sqlite3.connect(DB_PATH)

# === Pipeline 狀態 ===
st.subheader("📊 Pipeline 狀態")
col1, col2, col3 = st.columns(3)
for col, table in zip([col1, col2, col3], ["raw_orders", "cleaned_orders", "analyzed_orders"]):
    try:
        n = pd.read_sql(f"SELECT COUNT(*) as n FROM {table}", conn)["n"][0]
        col.metric(table.replace("_orders", "").title(), n)
    except Exception:
        col.metric(table, "不存在")

# === 商品銷售排行 ===
st.subheader("📊 商品銷售額 Top 15")
try:
    products = pd.read_sql("""
        SELECT description, SUM(quantity) as qty, ROUND(SUM(total_amount), 2) as revenue
        FROM cleaned_orders GROUP BY description ORDER BY revenue DESC LIMIT 15
    """, conn)
    st.bar_chart(products.set_index("description")["revenue"])
    st.dataframe(products, use_container_width=True)
except Exception as e:
    st.warning(f"cleaned_orders 表不存在：{e}")

# === 各國銷售 ===
st.subheader("🌍 各國銷售額")
try:
    countries = pd.read_sql("""
        SELECT country, COUNT(DISTINCT customer_id) as customers, ROUND(SUM(total_amount), 2) as revenue
        FROM cleaned_orders GROUP BY country ORDER BY revenue DESC
    """, conn)
    st.bar_chart(countries.set_index("country")["revenue"])
    st.dataframe(countries, use_container_width=True)
except Exception as e:
    st.warning(f"查詢失敗：{e}")

# === LLM 品類分析 ===
try:
    analyzed = pd.read_sql("SELECT * FROM analyzed_orders", conn)
    st.subheader("🤖 LLM 品類分類結果")

    col1, col2 = st.columns(2)
    with col1:
        st.write("**品類分佈**")
        st.bar_chart(analyzed["category"].value_counts())
    with col2:
        st.write("**品類 × 銷售額**")
        cat_rev = analyzed.groupby("category")["total_amount"].sum().sort_values(ascending=False)
        st.bar_chart(cat_rev)

    st.write("**分析明細（前 20 筆）**")
    display = [c for c in ["description", "quantity", "total_amount", "category", "llm_insight"] if c in analyzed.columns]
    st.dataframe(analyzed[display].head(20), use_container_width=True)
except Exception:
    st.info("💡 尚未完成 LLM 分析（Notebook Section 4）")

# === 報告 ===
if os.path.exists("output/pipeline_doc.md"):
    st.subheader("📄 顧問報告")
    with open("output/pipeline_doc.md") as f:
        st.markdown(f.read())

conn.close()
