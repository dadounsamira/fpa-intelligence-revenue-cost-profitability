from common import INDUSTRIES, INDUSTRY_COL, ITEM_COL, load_table

ITEM = "Total operating revenue, seasonally adjusted"

df = load_table()
revenue = df[df[ITEM_COL] == ITEM]

wide = revenue.pivot(index="REF_DATE", columns=INDUSTRY_COL, values="VALUE")
changes = wide[INDUSTRIES].pct_change() * 100
print(changes.std().sort_values())
print(wide.shape)

print(changes.drop(["2020-04", "2020-07"]).std().sort_values())