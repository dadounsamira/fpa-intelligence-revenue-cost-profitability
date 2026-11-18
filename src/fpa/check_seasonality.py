import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

CSV_PATH = Path(__file__).resolve().parents[2] / "data" / "raw" / "33100226.csv"
INDUSTRY_COL = "North American Industry Classification System (NAICS)"
ITEM_COL = "Balance sheet and income statement selected seasonally adjusted components"
INDUSTRY = "Clothing, sporting goods, and general merchandise stores"
ITEM = "Total operating revenue, seasonally adjusted"

df = pd.read_csv(CSV_PATH, dtype={"REF_DATE": str})
series = df[(df[INDUSTRY_COL] == INDUSTRY) & (df[ITEM_COL] == ITEM)]
print(series[["REF_DATE", "VALUE"]])

plt.figure(figsize=(10, 4))
plt.plot(series["REF_DATE"], series["VALUE"], marker="o")
plt.xticks(rotation=90)
plt.title(INDUSTRY + "\n" + ITEM)
plt.ylabel("Millions of dollars")
plt.tight_layout()
plt.show()
