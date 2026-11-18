import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parents[2] / "data" / "raw" / "33100226.csv"
INDUSTRY_COL = "North American Industry Classification System (NAICS)"
ITEM_COL = "Balance sheet and income statement selected seasonally adjusted components"

df = pd.read_csv(CSV_PATH, dtype={"REF_DATE": str})
counts = df.groupby([ITEM_COL, INDUSTRY_COL])["VALUE"].count()
print(counts[counts < 26])

ITEM = "Total operating revenue, seasonally adjusted"
revenue = df[df[ITEM_COL] == ITEM]
latest = revenue[revenue["REF_DATE"] == "2026-04"]
print(latest[[INDUSTRY_COL, "VALUE"]].sort_values("VALUE", ascending=False))


from common import INDUSTRY_COL, load_table

df = load_table()
names = df[INDUSTRY_COL].unique()
print([name for name in names if "health" in name.lower() or "[62" in name])