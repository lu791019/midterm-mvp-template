"""題目 5：求職媒合薪資洞察 — Streamlit Dashboard"""
import streamlit as st
import pandas as pd
import sqlite3, os
st.set_page_config(page_title="求職薪資分析", layout="wide")
st.title("求職薪資分析 Dashboard")
DB_PATH = "pipeline.db"
if not os.path.exists(DB_PATH):
    st.error("❌ pipeline.db 不存在")
    st.stop()
conn = sqlite3.connect(DB_PATH)
st.subheader("Pipeline 狀態")
c1, c2, c3 = st.columns(3)
for col, t in zip([c1,c2,c3], ["raw_jobs","cleaned_jobs","analyzed_jobs"]):
    try: col.metric(t.split("_",1)[1], pd.read_sql(f"SELECT COUNT(*) as n FROM {t}", conn)["n"][0])
    except: col.metric(t, "N/A")
try:
    stats = pd.read_sql("""SELECT job_category, COUNT(*) as jobs, ROUND(AVG(salary_in_usd),0) as avg_salary FROM cleaned_jobs GROUP BY job_category ORDER BY avg_salary DESC""", conn)
    st.subheader("統計")
    st.dataframe(stats, use_container_width=True)
except Exception as e:
    st.warning(f"查詢失敗: {e}")
try:
    analyzed = pd.read_sql("SELECT * FROM analyzed_jobs", conn)
    st.subheader("LLM 分析")
    st.dataframe(analyzed.head(20), use_container_width=True)
except:
    st.info("尚未完成 LLM 分析")
if os.path.exists("output/pipeline_doc.md"):
    st.subheader("報告")
    with open("output/pipeline_doc.md") as f: st.markdown(f.read())
conn.close()
