
import pandas as pd
from .config import ANOMALY_THRESHOLD_PCT

def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    daily = (
        df.groupby(["merchant", "date"], as_index=False)
          .agg(total_amount=("amount", "sum"), tx_count=("amount", "size"))
    )

    daily = daily.sort_values(["merchant", "date"])
    daily["rolling_mean"] = (
        daily.groupby("merchant")["total_amount"]
             .transform(lambda s: s.rolling(window=7, min_periods=3).mean())
    )

    mask = daily["rolling_mean"] > 0
    daily.loc[mask, "pct_change_vs_mean"] = (
        (daily["total_amount"] - daily["rolling_mean"]) / daily["rolling_mean"]
    )
    daily.loc[~mask, "pct_change_vs_mean"] = 0.0

    anomalies = daily[daily["pct_change_vs_mean"].abs() >= ANOMALY_THRESHOLD_PCT].copy()
    anomalies["anomaly_type"] = anomalies["pct_change_vs_mean"].apply(
        lambda x: "Spike" if x > 0 else "Drop"
    )
    return anomalies
