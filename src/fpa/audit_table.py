"""Audit a Statistics Canada full-table CSV.

Usage:
    python src/fpa/audit_table.py data/raw/33100226-eng.csv

Prints what the tracker steps 1.3.2 to 1.3.7 ask for: the quarters covered,
the members of every dimension (industry, financial statement item, and so
on), units, missing and flagged values, and how many quarters each series has.
It reads the file only; it changes nothing.
"""

import sys

import pandas as pd

# Columns that every Statistics Canada full-table CSV carries besides its
# dimensions. Everything else is treated as a dimension (industry, item...).
STANDARD_COLUMNS = {
    "REF_DATE", "GEO", "DGUID", "UOM", "UOM_ID", "SCALAR_FACTOR", "SCALAR_ID",
    "VECTOR", "COORDINATE", "VALUE", "STATUS", "SYMBOL", "TERMINATED", "DECIMALS",
}


def load_table(path):
    """Read the CSV with the date as text so odd period labels are not lost."""
    return pd.read_csv(path, dtype={"REF_DATE": str}, low_memory=False)


def find_dimensions(df):
    """Return the dimension columns: those that are not standard metadata."""
    return [c for c in df.columns if c not in STANDARD_COLUMNS]


def describe_periods(df):
    """Print first and last period and how many distinct quarters exist."""
    periods = sorted(df["REF_DATE"].dropna().unique())
    print(f"Periods: {len(periods)} distinct, first {periods[0]}, last {periods[-1]}")
    # A quarterly table should have no gaps; list any quarter that is missing.
    dates = pd.PeriodIndex(pd.to_datetime(periods, errors="coerce"), freq="Q")
    full = pd.period_range(dates.min(), dates.max(), freq="Q")
    missing = [str(p) for p in full.difference(dates)]
    print(f"Missing quarters between first and last: {missing if missing else 'none'}")


def describe_dimensions(df, dimensions):
    """Print every member of every dimension."""
    for col in dimensions:
        members = df[col].dropna().unique()
        print(f"\n{col}: {len(members)} members")
        for m in sorted(members):
            print(f"  - {m}")


def describe_quality(df):
    """Print units, empty values and the flags Statistics Canada attaches."""
    if "UOM" in df and "SCALAR_FACTOR" in df:
        print("\nUnits:", df[["UOM", "SCALAR_FACTOR"]].drop_duplicates().to_dict("records"))
    empty = df["VALUE"].isna().sum()
    print(f"\nEmpty VALUE cells: {empty} of {len(df)} ({empty / len(df):.1%})")
    for col in ("STATUS", "SYMBOL"):
        if col in df:
            counts = df[col].value_counts(dropna=True)
            print(f"{col} flags:", counts.to_dict() if len(counts) else "none")


def describe_series_length(df, dimensions):
    """Print how many quarters each series (one combination of members) has."""
    if not dimensions:
        return
    counts = df.dropna(subset=["VALUE"]).groupby(dimensions)["REF_DATE"].nunique()
    print(f"\nSeries: {len(counts)}; quarters per series: "
          f"min {counts.min()}, median {int(counts.median())}, max {counts.max()}")
    print("Series with fewer than 60 quarters:", int((counts < 60).sum()))


def main(path):
    df = load_table(path)
    print(f"Rows: {len(df)}; columns: {list(df.columns)}")
    dims = find_dimensions(df)
    describe_periods(df)
    describe_dimensions(df, dims)
    describe_quality(df)
    describe_series_length(df, dims)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
