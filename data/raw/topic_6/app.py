"""題目 6：不動產房價趨勢 — Streamlit Dashboard"""
import streamlit as st
import pandas as pd
import sqlite3, os
st.set_page_config(page_title="不動產房價分析", layout="wide")
st.title("不動產房價分析 Dashboard")
DB_PATH = "pipeline.db"
if not os.path.exists(DB_PATH):
    st.error("❌ pipeline.db 不存在")
    st.stop()
conn = sqlite3.connect(DB_PATH)
st.subheader("Pipeline 狀態")
c1, c2, c3 = st.columns(3)
for col, t in zip([c1,c2,c3], ["raw_realestate","cleaned_realestate","analyzed_realestate"]):
    try: col.metric(t.split("_",1)[1], pd.read_sql(f"SELECT COUNT(*) as n FROM {t}", conn)["n"][0])
    except: col.metric(t, "N/A")
try:
    stats = pd.read_sql("""SELECT 縣市, COUNT(*) as 交易量, ROUND(AVG(總價萬),1) as 均價萬 FROM cleaned_realestate GROUP BY 縣市 ORDER BY 均價萬 DESC""", conn)
    st.subheader("統計")
    st.dataframe(stats, use_container_width=True)
except Exception as e:
    st.warning(f"查詢失敗: {e}")
try:
    analyzed = pd.read_sql("SELECT * FROM analyzed_realestate", conn)
    st.subheader("LLM 分析")
    st.dataframe(analyzed.head(20), use_container_width=True)
except:
    st.info("尚未完成 LLM 分析")
if os.path.exists("output/report.md"):
    st.subheader("報告")
    with open("output/report.md") as f: st.markdown(f.read())
conn.close()
