from pathlib import Path

import pandas as pd


REPORT_PATH = Path("output/report.md")


def analyze_text(text: str) -> dict[str, str]:
    """Fallback analyzer for workshop use without an API key.

    Replace this with an LLM API call after the basic pipeline works.
    """
    negative_keywords = ["慢", "破損", "困惑", "不清楚", "等"]
    positive_keywords = ["快", "合理", "好", "不錯", "還會"]

    if any(keyword in text for keyword in negative_keywords):
        sentiment = "negative"
    elif any(keyword in text for keyword in positive_keywords):
        sentiment = "positive"
    else:
        sentiment = "neutral"

    if "客服" in text:
        topic = "customer_service"
    elif "價格" in text or "商品" in text:
        topic = "product_value"
    elif "頁面" in text or "結帳" in text:
        topic = "user_experience"
    elif "外送" in text or "包裝" in text:
        topic = "delivery"
    else:
        topic = "general"

    return {"sentiment": sentiment, "topic": topic}


def add_llm_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Add AI analysis columns to processed rows."""
    analyzed = df.copy()
    results = analyzed["text"].apply(analyze_text)
    analyzed["sentiment"] = results.apply(lambda item: item["sentiment"])
    analyzed["topic"] = results.apply(lambda item: item["topic"])
    return analyzed


def write_report(df: pd.DataFrame, path: Path = REPORT_PATH) -> Path:
    """Write a short markdown report for demo."""
    path.parent.mkdir(parents=True, exist_ok=True)
    sentiment_counts = df["sentiment"].value_counts().to_dict()
    topic_counts = df["topic"].value_counts().to_dict()

    report = [
        "# MVP Analysis Report",
        "",
        "## Summary",
        f"- Total rows: {len(df)}",
        f"- Sentiment counts: {sentiment_counts}",
        f"- Topic counts: {topic_counts}",
        "",
        "## Next Questions",
        "- 哪些負面主題最值得優先處理？",
        "- 這些洞察要如何轉成 dashboard 指標？",
        "- 學完 Airflow 後，這條 pipeline 要多久跑一次？",
    ]
    path.write_text("\n".join(report), encoding="utf-8")
    return path
