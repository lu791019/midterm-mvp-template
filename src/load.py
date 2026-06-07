from pathlib import Path

import pandas as pd


PROCESSED_PATH = Path("data/processed/processed_reviews.csv")


def save_processed(df: pd.DataFrame, path: Path = PROCESSED_PATH) -> Path:
    """Persist processed data to CSV."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path
