import pandas as pd

CSV_PATH = "data/raw/33100226.csv"
INDUSTRY_COL = "North American Industry Classification System (NAICS)"
ITEM_COL = "Balance sheet and income statement selected seasonally adjusted components"
INDUSTRY = "Clothing, sporting goods, and general merchandise stores"
ITEM = "Total operating revenue, seasonally adjusted"

df = pd.read_csv(CSV_PATH, dtype={"REF_DATE": str})
series = df[(df[INDUSTRY_COL] == INDUSTRY) & (df[ITEM_COL] == ITEM)]
print(series[["REF_DATE", "VALUE"]])