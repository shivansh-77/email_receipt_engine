# 📧 Email Receipt Data Cleaning & Merchant Categorization Engine

> A complete Python data-cleaning pipeline for extracting structured insights from unstructured email receipts.

---

## 🎯 Overview

This project simulates a **real-world Data QA / Data Processing pipeline** similar to what companies like YipitData perform.

The engine takes **raw email receipt text** (subjects + bodies), applies **regex-based extraction**, performs **data cleaning**, **merchant normalization**, **categorization**, and **anomaly detection**, and finally exports clean, analysis-ready CSV datasets.

### Skills Demonstrated

| Skill | Description |
|-------|-------------|
| 🧹 Data Cleaning | Quality checks, validation, normalization |
| 🔍 Regex Extraction | Pattern matching for text parsing |
| 🏷️ Data Labeling | Merchant categorization |
| 📈 Anomaly Detection | Trend analysis & spike detection |
| 🐍 Python Pipelines | Modular, maintainable code design |

---

## ⚡ What This Project Does

### 1️⃣ Loads Raw Email Receipts
Reads `data/raw/receipts_sample.csv` containing email subjects, bodies, and unique IDs.

### 2️⃣ Extracts Structured Fields Using Regex

| Raw Email Text | Extracted Fields |
|----------------|------------------|
| `"Thank you for shopping at WALMART..."` | Merchant = Walmart |
| `"Amount charged: Rs. 1,234.50"` | Amount = 1234.50, Currency = INR |
| `"on 2025-01-10"` | Date = 2025-01-10 |

### 3️⃣ Cleans & Normalizes Data
- Standardizes merchant names
- Converts amount → float
- Parses dates → date object
- Fills missing currencies
- Drops invalid rows

### 4️⃣ Categorizes Transactions

| Merchant | Category |
|----------|----------|
| Walmart | Groceries |
| Uber | Rideshare |
| Amazon | Online Retail |
| Swiggy | Food Delivery |

### 5️⃣ Generates Merchant Summary
Creates `merchant_summary.csv` with total spend, transaction count, date range, and category.

### 6️⃣ Detects Anomalies
- Computes 7-day rolling mean
- Flags deviations ≥ 75%
- Exports to `anomalies.csv`

---

## 📁 Project Structure

```
email_receipt_engine/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── config.py          # Configuration settings
│   ├── parser.py          # Regex-based extraction
│   ├── cleaner.py         # Data cleaning logic
│   ├── categorizer.py     # Merchant categorization
│   ├── anomaly.py         # Anomaly detection
│   └── main.py            # Pipeline entry point
│
└── data/
    ├── raw/               # Input email data
    │   └── receipts_sample.csv
    ├── processed/         # Cleaned output
    └── reports/           # Summary & anomaly reports
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/shivansh-77/email_receipt_engine.git
cd email_receipt_engine
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Pipeline

```bash
python -m src.main
```

This will:
1. Parse receipts
2. Clean the dataset
3. Categorize merchants
4. Detect anomalies
5. Export clean CSV outputs

---

## 📊 Output Files

| File | Location | Description |
|------|----------|-------------|
| Cleaned Data | `data/processed/cleaned_receipts.csv` | Processed & validated receipts |
| Merchant Summary | `data/reports/merchant_summary.csv` | Aggregated merchant statistics |
| Anomaly Report | `data/reports/anomalies.csv` | Flagged irregular transactions |

---

## 🧪 Sample Output

| email_id | merchant | amount  | date       | currency | category      |
|----------|----------|---------|------------|----------|---------------|
| 1        | Walmart  | 1234.50 | 2025-01-10 | INR      | Groceries     |
| 2        | Uber     | 250.00  | 2025-01-11 | INR      | Rideshare     |
| 3        | Amazon   | 45.99   | 2025-01-11 | USD      | Online Retail |

---

## 🛠️ Tech Stack

- **Python 3.12** - Core programming language
- **Pandas** - Data manipulation & analysis
- **python-dateutil** - Date parsing
- **Regex** - Pattern matching & extraction

---

## 🔮 Future Enhancements

- Add merchant alias matching (Fuzzy matching)
- Add visual dashboards (Plotly/Matplotlib)
- Build a Streamlit UI for interactive QA review
- Support larger datasets with multiprocessing

---

## 👨‍💻 Author

**Shivansh Bajpai**

Data QA Engineer • Python Developer

- GitHub: https://github.com/shivansh-77
- LinkedIn: https://linkedin.com/in/shivansh-bajpai-522965257/

---

## 📄 License

This project is open source and available for learning purposes.

---

⭐ **Star this repo if you found it useful!**
