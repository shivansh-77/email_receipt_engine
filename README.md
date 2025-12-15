
# Email Receipt Data Cleaning & Merchant Categorization Engine

This project demonstrates a realistic **Data QA / Data Cleaning pipeline** similar to what a Data QA Associate might do at a company like YipitData.

## What this project does

- Loads raw email receipt data from a CSV file.
- Extracts key fields using **regex and text parsing**:
  - Merchant name
  - Amount
  - Date
  - Currency (if present)
- Cleans and normalizes:
  - Merchant names (e.g., "WALMART", "Walmart Inc." → "Walmart")
  - Amounts and dates (to numeric / datetime)
- Categorizes each receipt into categories like **Groceries, Rideshare, Food Delivery, Online Retail, Other**.
- Performs basic **anomaly detection**:
  - Detects large spikes/drops in total daily amount per merchant.
- Writes:
  - A cleaned, structured CSV
  - A merchant-level summary
  - An anomaly report

## Project structure

```
email_receipt_engine/
├─ README.md
├─ requirements.txt
├─ src/
│  ├─ __init__.py
│  ├─ config.py
│  ├─ parser.py
│  ├─ cleaner.py
│  ├─ categorizer.py
│  ├─ anomaly.py
│  └─ main.py
└─ data/
   ├─ raw/
   │  └─ receipts_sample.csv
   ├─ processed/
   └─ reports/
```

## 1. Setup (step-by-step)

1. **Clone / Download the project**
   - Download this folder or clone it into your machine.
   - Make sure the folder structure stays the same.

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # on macOS / Linux
   venv\Scripts\activate   # on Windows
   ```

3. **Install dependencies**

   From inside the project folder:

   ```bash
   pip install -r requirements.txt
   ```

4. **Inspect the sample data**

   Open `data/raw/receipts_sample.csv` to see how raw email data looks:
   - `email_id`
   - `subject`
   - `body`

5. **Run the pipeline**

   From inside the project folder:

   ```bash
   python -m src.main
   ```

   This will:
   - Read `data/raw/receipts_sample.csv`
   - Process and clean the data
   - Save:
     - `data/processed/cleaned_receipts.csv`
     - `data/reports/merchant_summary.csv`
     - `data/reports/anomalies.csv`

6. **Customize for your own data**

   - Replace `data/raw/receipts_sample.csv` with your own email receipt export.
   - Keep the same columns (`email_id`, `subject`, `body`) or adjust the loader in `src/parser.py`.
   - Update `MERCHANT_NORMALIZATION` and `CATEGORY_KEYWORDS` in `src/config.py` to match your examples.
