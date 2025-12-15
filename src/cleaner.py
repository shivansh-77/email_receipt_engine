
import pandas as pd
from dateutil import parser as date_parser
from .config import MERCHANT_NORMALIZATION

def normalize_merchant(name: str | None) -> str | None:
    if not isinstance(name, str):
        return None
    raw = name.strip()
    if raw in MERCHANT_NORMALIZATION:
        return MERCHANT_NORMALIZATION[raw]
    key = raw.upper()
    if key in MERCHANT_NORMALIZATION:
        return MERCHANT_NORMALIZATION[key]
    return raw.title()

def to_float_amount(value: str | None) -> float | None:
    if value is None:
        return None
    try:
        value = value.replace(",", ".")
        return float(value)
    except Exception:
        return None

def parse_date(value: str | None):
    if value is None:
        return None
    try:
        return date_parser.parse(value, dayfirst=False, fuzzy=True)
    except Exception:
        return None

def clean_parsed_receipts(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["merchant"] = df["raw_merchant"].apply(normalize_merchant)
    df["amount"] = df["raw_amount"].apply(to_float_amount)
    df["date"] = df["raw_date"].apply(parse_date)

    df = df.dropna(subset=["merchant", "amount", "date"])
    df["date"] = pd.to_datetime(df["date"]).dt.date

    df["currency"] = df["currency"].fillna("INR")

    return df
