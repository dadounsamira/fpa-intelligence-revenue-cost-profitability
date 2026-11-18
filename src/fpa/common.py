import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parents[2] / "data" / "raw" / "33100226.csv"
INDUSTRY_COL = "North American Industry Classification System (NAICS)"
ITEM_COL = "Balance sheet and income statement selected seasonally adjusted components"

INDUSTRIES = [
    "Total, non-financial industries",
    "Clothing, sporting goods, and general merchandise stores",
    "Other wholesalers",
    "Construction [23]",
    "Oil and gas extraction and support services",
    "Food and soft drink and ice manufacturing",
    "Professional, scientific and technical services [54]",
    "Real estate [531]",
    "Telecommunications [517]",
]


def load_table():
    return pd.read_csv(CSV_PATH, dtype={"REF_DATE": str})