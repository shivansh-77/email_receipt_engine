
import re
import pandas as pd

MERCHANT_PATTERNS = [
    r"Thank you for shopping at (?P<merchant>[A-Za-z0-9 &.'-]+)",
    r"from (?P<merchant>[A-Za-z0-9 &.'-]+)",
    r"at (?P<merchant>[A-Za-z0-9 &.'-]+)",
]

AMOUNT_PATTERN = re.compile(r"(?P<currency>USD|INR|Rs\.?|\$)?\s*(?P<amount>\d+[\.,]\d{2})")
DATE_PATTERN = re.compile(r"(?P<date>\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{1,2} [A-Za-z]{3,9} \d{4})")

def extract_merchant(text: str) -> str | None:
    if not isinstance(text, str):
        return None
    for pattern in MERCHANT_PATTERNS:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return match.group("merchant").strip()
    return None

def extract_amount_and_currency(text: str) -> tuple[str | None, str | None]:
    if not isinstance(text, str):
        return None, None
    match = AMOUNT_PATTERN.search(text)
    if not match:
        return None, None
    amount = match.group("amount")
    currency = match.group("currency")
    if currency:
        currency = currency.replace("Rs.", "INR").replace("Rs", "INR")
    return amount, currency

def extract_date(text: str) -> str | None:
    if not isinstance(text, str):
        return None
    match = DATE_PATTERN.search(text)
    if not match:
        return None
    return match.group("date")

def parse_raw_receipts(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    combined = (df["subject"].fillna("") + " " + df["body"].fillna("")).str.strip()

    df["raw_merchant"] = combined.apply(extract_merchant)
    df["raw_amount"], df["currency"] = zip(*combined.apply(extract_amount_and_currency))
    df["raw_date"] = combined.apply(extract_date)

    return df
