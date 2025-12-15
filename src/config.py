
MERCHANT_NORMALIZATION = {
    "WALMART": "Walmart",
    "Walmart Inc.": "Walmart",
    "UBER TRIP": "Uber",
    "UBER *TRIP": "Uber",
    "Uber B.V.": "Uber",
    "AMAZON": "Amazon",
    "Amazon Marketplace": "Amazon",
    "SWIGGY": "Swiggy",
    "ZOMATO": "Zomato",
}

CATEGORY_KEYWORDS = {
    "Groceries": ["walmart", "big bazaar", "dmart"],
    "Rideshare": ["uber", "ola"],
    "Food Delivery": ["swiggy", "zomato"],
    "Online Retail": ["amazon", "flipkart", "myntra"],
}

ANOMALY_THRESHOLD_PCT = 0.75
