
import os
import pandas as pd
from . import parser, cleaner, categorizer, anomaly

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RAW_PATH = os.path.join(BASE_DIR, "data", "raw", "receipts_sample.csv")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
REPORTS_DIR = os.path.join(BASE_DIR, "data", "reports")

def main():
    print("Loading raw receipts from:", RAW_PATH)
    df_raw = pd.read_csv(RAW_PATH)

    print(f"Loaded {len(df_raw)} raw rows.")

    print("Parsing raw receipts...")
    df_parsed = parser.parse_raw_receipts(df_raw)
    print("Parsing complete.")

    print("Cleaning parsed receipts...")
    df_clean = cleaner.clean_parsed_receipts(df_parsed)
    print(f"After cleaning: {len(df_clean)} valid rows remain.")

    print("Adding categories...")
    df_cat = categorizer.add_categories(df_clean)

    os.makedirs(PROCESSED_DIR, exist_ok=True)
    processed_path = os.path.join(PROCESSED_DIR, "cleaned_receipts.csv")
    df_cat.to_csv(processed_path, index=False)
    print("Saved cleaned receipts to:", processed_path)

    print("Creating merchant summary...")
    merchant_summary = (
        df_cat.groupby(["merchant", "category"], as_index=False)
             .agg(
                 total_amount=("amount", "sum"),
                 tx_count=("amount", "size"),
                 first_date=("date", "min"),
                 last_date=("date", "max"),
             )
    )
    os.makedirs(REPORTS_DIR, exist_ok=True)
    summary_path = os.path.join(REPORTS_DIR, "merchant_summary.csv")
    merchant_summary.to_csv(summary_path, index=False)
    print("Saved merchant summary to:", summary_path)

    print("Detecting anomalies...")
    anomalies_df = anomaly.detect_anomalies(df_cat)
    os.makedirs(REPORTS_DIR, exist_ok=True)
    anomalies_path = os.path.join(REPORTS_DIR, "anomalies.csv")
    anomalies_df.to_csv(anomalies_path, index=False)
    print(f"Saved {len(anomalies_df)} anomalies to:", anomalies_path)

    print("Done.")

if __name__ == "__main__":
    main()
