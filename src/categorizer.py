
import pandas as pd
from .config import CATEGORY_KEYWORDS

def categorize_merchant(merchant: str | None) -> str:
    if not isinstance(merchant, str):
        return "Other"
    merchant_lower = merchant.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in merchant_lower:
                return category
    return "Other"

def add_categories(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["category"] = df["merchant"].apply(categorize_merchant)
    return df
