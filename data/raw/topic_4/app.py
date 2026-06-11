"""題目 4：叫車服務交通熱點 — Streamlit Dashboard"""
import streamlit as st
import pandas as pd
import sqlite3, os
st.set_page_config(page_title="叫車交通分析", layout="wide")
st.title("叫車交通分析 Dashboard")
DB_PATH = "pipeline.db"
if not os.path.exists(DB_PATH):
    st.error("❌ pipeline.db 不存在")
    st.stop()
conn = sqlite3.connect(DB_PATH)
st.subheader("Pipeline 狀態")
c1, c2, c3 = st.columns(3)
for col, t in zip([c1,c2,c3], ["raw_trips","cleaned_trips","analyzed_trips"]):
    try: col.metric(t.split("_",1)[1], pd.read_sql(f"SELECT COUNT(*) as n FROM {t}", conn)["n"][0])
    except: col.metric(t, "N/A")
try:
    stats = pd.read_sql("""SELECT pickup_borough, pickup_zone, COUNT(*) as trips, ROUND(AVG(total_amount),2) as avg_fare FROM cleaned_trips GROUP BY pickup_borough, pickup_zone ORDER BY trips DESC LIMIT 20""", conn)
    st.subheader("統計")
    st.dataframe(stats, use_container_width=True)
except Exception as e:
    st.warning(f"查詢失敗: {e}")
try:
    analyzed = pd.read_sql("SELECT * FROM analyzed_trips", conn)
    st.subheader("LLM 分析")
    st.dataframe(analyzed.head(20), use_container_width=True)
except:
    st.info("尚未完成 LLM 分析")
if os.path.exists("output/pipeline_doc.md"):
    st.subheader("報告")
    with open("output/pipeline_doc.md") as f: st.markdown(f.read())
conn.close()
