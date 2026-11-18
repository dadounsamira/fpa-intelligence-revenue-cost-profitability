# Data Biography and Ethics Check

## Who collected the data
Statistics Canada, through the Quarterly Survey of Financial Statements
(survey 2501). It is a sample survey of incorporated enterprises in
Canada. Aggregate estimates combine survey responses, administrative
data and publicly available information. The survey excludes
government-controlled and not-for-profit corporations.

## Why it is collected
The data are used to prepare industry financial statements for the
Canadian business sector and are an input to gross domestic product,
the national balance sheet and Canada's international investment
position.

## How it reached this project
- Table: 33-10-0226-01, Quarterly balance sheet and income statement,
  by industry, seasonally adjusted (x 1,000,000).
- Page: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310022601
- Downloaded: 2026-11-17, with `src/fpa/ingest.py`.
- Files: `33100226-eng.zip`, unpacked to `33100226.csv` and
  `33100226_MetaData.csv` in `data/raw/` (git-ignored).

## Licence and terms of use
Statistics Canada Open Licence: use, copy, share and redistribute,
commercially or not, with attribution. The licence gives two notices:

- Notice (a), for data shown unchanged, as published: "Source:
  Statistics Canada, name of product, reference date. Reproduced and
  distributed on an 'as is' basis with the permission of Statistics
  Canada."
- Notice (b), for a value-added product: "Adapted from Statistics
  Canada, name of product, reference date. This does not constitute an
  endorsement by Statistics Canada of this product."

This project derives cost and margin and adds forecasts, so it is a
value-added product and uses notice (b):

Adapted from Statistics Canada, Table 33-10-0226-01, Quarterly balance
sheet and income statement, by industry, seasonally adjusted
(x 1,000,000), 2026-08-24. This does not constitute an endorsement by
Statistics Canada of this product.

Charts of an unmodified series use notice (a).

## Known limits
- **Revisions:** Statistics Canada can revise past values (note 5).
- **Empty series:** 14 of 275 series are empty, all finance and
  insurance sales (DEC-009).
- **Definition changes:** the survey has changed since Q1 2020, and
  operating revenue, expenses and operating profit are derived from
  other variables (note 6). Insurance has an IFRS 17 break between
  Q4 2022 and Q1 2023 (note 7).
- **Coverage:** incorporated enterprises only; government-controlled
  and not-for-profit corporations are excluded, which leaves out most
  public health care.
- **Government support:** 2020 and 2021 amounts include programs such
  as the Canada Emergency Wage Subsidy, counted as revenue.
- **Units:** millions of dollars, treated as nominal.

## Ethics check
- **Personal information:** none. The data are published industry
  aggregates, not individual people or named companies.
- **Licence:** the Open Licence permits this use (an independent
  portfolio project), with attribution.
- **Appropriate use:** the forecasts are statistical projections from
  26 quarters of industry-level data. They are not financial advice
  and should not be applied to a single company, because an industry
  aggregate hides differences between firms. Forecast errors are
  expected to be larger around shocks such as 2020, and the models
  cannot anticipate events that are absent from the history.