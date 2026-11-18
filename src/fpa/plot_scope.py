import matplotlib.pyplot as plt
from common import INDUSTRIES, INDUSTRY_COL, ITEM_COL, load_table

ITEM = "Total operating revenue, seasonally adjusted"

df = load_table()
revenue = df[df[ITEM_COL] == ITEM]

for name in INDUSTRIES:
    one = revenue[revenue[INDUSTRY_COL] == name]
    print(len(one), name)

fig, axes = plt.subplots(3, 3, figsize=(14, 9), sharex=True)

for ax, name in zip(axes.flat, INDUSTRIES):
    one = revenue[revenue[INDUSTRY_COL] == name]
    ax.plot(one["REF_DATE"], one["VALUE"], marker="o")
    ax.set_title(name, fontsize=9)
    ax.tick_params(axis="x", rotation=90, labelsize=7)

plt.tight_layout()
plt.show()