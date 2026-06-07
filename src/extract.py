from pathlib import Path

import pandas as pd


RAW_PATH = Path("data/raw/sample_reviews.csv")


def extract_reviews(path: Path = RAW_PATH) -> pd.DataFrame:
    """Load raw review data for the MVP pipeline."""
    if not path.exists():
        raise FileNotFoundError(f"Raw data not found: {path}")
    return pd.read_csv(path)
