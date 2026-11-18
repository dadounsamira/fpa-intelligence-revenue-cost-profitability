from common import INDUSTRY_COL, ITEM_COL, load_table

REVENUE = "Total operating revenue, seasonally adjusted"
PROFIT = "Operating profit or loss, seasonally adjusted"

df = load_table()

one = df[df[INDUSTRY_COL] == "Total, non-financial industries"]

table = one.pivot(index="REF_DATE", columns=ITEM_COL, values="VALUE")
table = table[[REVENUE, PROFIT]].rename(columns={REVENUE: "Revenue", PROFIT: "Profit"})
table["Cost"] = table["Revenue"] - table["Profit"]
table.columns.name = None
table["Margin %"] = table["Profit"] / table["Revenue"] * 100
print(table.tail(6))