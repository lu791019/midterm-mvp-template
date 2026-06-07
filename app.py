from pathlib import Path

import pandas as pd
import streamlit as st


DATA_PATH = Path("data/processed/processed_reviews.csv")
REPORT_PATH = Path("output/report.md")


st.set_page_config(page_title="LLM x DE MVP", layout="wide")
st.title("LLM x DE MVP Dashboard")

if not DATA_PATH.exists():
    st.warning("Run `python -m src.run_pipeline` first.")
    st.stop()

df = pd.read_csv(DATA_PATH)

metric_cols = st.columns(3)
metric_cols[0].metric("Rows", len(df))
metric_cols[1].metric("Topics", df["topic"].nunique())
metric_cols[2].metric("Sentiments", df["sentiment"].nunique())

left, right = st.columns(2)
with left:
    st.subheader("Sentiment")
    st.bar_chart(df["sentiment"].value_counts())

with right:
    st.subheader("Topic")
    st.bar_chart(df["topic"].value_counts())

st.subheader("Processed Data")
st.dataframe(df, use_container_width=True)

if REPORT_PATH.exists():
    st.subheader("Report")
    st.markdown(REPORT_PATH.read_text(encoding="utf-8"))
