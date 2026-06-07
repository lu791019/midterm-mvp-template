import pandas as pd


def transform_reviews(df: pd.DataFrame) -> pd.DataFrame:
    """Clean raw review rows into a usable dataset."""
    required = {"id", "source", "text"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    cleaned = df.copy()
    cleaned["text"] = cleaned["text"].fillna("").astype(str).str.strip()
    cleaned = cleaned[cleaned["text"] != ""]
    cleaned["text_length"] = cleaned["text"].str.len()
    return cleaned
