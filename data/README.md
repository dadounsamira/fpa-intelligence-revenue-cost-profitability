# Data: Statistics Canada Table 33-10-0226-01

Audit completed 2026-11-17 (tracker steps 1.3.1 to 1.3.8). Findings below come from Statistics Canada's table page and metadata, and from running checks on the downloaded CSV.

## Source and attribution

- **Table:** 33-10-0226-01, Quarterly balance sheet and income statement, by industry, seasonally adjusted (x 1,000,000). DOI 10.25318/3310022601-eng.
- **Publisher:** Statistics Canada, Quarterly Survey of Financial Statements (survey 2501).
- **Page:** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310022601
- **Licence:** Statistics Canada Open Licence, which allows sharing and redistribution, commercial or not, with attribution.
- **Attribution:** Adapted from Statistics Canada, Table 33-10-0226-01, Quarterly balance sheet and income statement, by industry, seasonally adjusted. This does not constitute an endorsement by Statistics Canada of this product.
- **Downloaded:** 2026-11-17, with `src/fpa/ingest.py`.

## What the table is

| Item | Finding |
| --- | --- |
| Frequency and geography | Quarterly, Canada only, seasonally adjusted |
| Units | Millions of dollars |
| Coverage | Q1 2020 (`2020-01`) to Q2 2026 (`2026-04`): 26 quarters, none missing. History starts in 2020; earlier data sit in archived tables that are not used here. |
| Size | 55 industry groupings x 5 financial items x 26 quarters = 7,150 rows; 275 series |
| Latest release | 2026-08-24 |
| Items (5) | Total operating revenue; sales of goods and services; operating profit or loss; income or loss before income taxes; net income or loss. All are seasonally adjusted. |
| Hierarchy | Total, all industries splits into Total, non-financial industries and Total, finance and insurance industries. Totals add exactly (1,472,376 + 222,100 = 1,694,476 in 2026-04). |

A series is one industry and one item followed over 26 quarters.

## Known issues

| Issue | Detail | How the project handles it |
| --- | --- | --- |
| 14 empty series | All are "Sales of goods and services" for the 14 finance and insurance groupings (the total and 13 sub-industries): 364 empty cells, flagged `..`. The other 261 series are complete. | Finance and insurance are excluded (DEC-009). |
| No cost column | The table has revenue and operating profit but no cost. | Cost is derived as revenue minus operating profit (DEC-008). |
| Insurance accounting break | IFRS 17 changed insurance reporting between Q4 2022 and Q1 2023 (metadata note 7). The non-financial total is not affected. | Totals that include insurance are not used (DEC-009). |
| Derived variables | Since Q1 2020, operating revenue, expenses and operating profit are derived from other variables (note 6). This is consistent across all 26 quarters but would matter if older history were added. | Noted; no action needed for 2020 onward. |
| Revisions | Statistics Canada can revise past values (note 5). | The download date is recorded above; re-download to refresh. |
| Sample survey | Covers incorporated enterprises in Canada and excludes government-controlled and not-for-profit corporations. Each value is an industry aggregate, not a single company. | Results describe these private-sector industries (DEC-006). |
| Health care | It appears only inside "Educational, health care and social assistance services", and the excluded public and non-profit part is most of the sector. | Not forecast separately (DEC-006). |
| 2020 and 2021 government support | Amounts include support such as the Canada Emergency Wage Subsidy, counted as revenue. 2020-04 shows a shock across many industries. | The 2020-04 and 2020-07 quarters are flagged, not deleted (DEC-007). |
| Seasonally adjusted data | The seasonal pattern is already removed, so a seasonal naive baseline would be weak. Not-seasonally-adjusted versions exist (33-10-0224-01, 33-10-0225-01, 33-10-0227-01) but are not used. | Baselines are naive and drift (DEC-010). |
| Nominal dollars | The table gives no sign of inflation adjustment, so values are treated as nominal and part of any growth is price inflation. | Amounts are used as published (DEC-011). |

Symbols found in the data: only `..` (not available). The symbols `p` (preliminary), `r` (revised) and `E` (use with caution) do not appear.

## What the project uses

Nine industries and three measures (revenue, cost and operating profit), which makes 27 series (DEC-006): total non-financial industries; clothing, sporting goods and general merchandise stores; other wholesalers; construction; oil and gas extraction and support services; food and soft drink and ice manufacturing; professional, scientific and technical services; real estate; and telecommunications.

The reasoning behind each choice is in the decision log, in the `decision_log/` folder.

## Reproduce the data

1. Run `python src/fpa/ingest.py`. It downloads the full table and unpacks `33100226.csv` and `33100226_MetaData.csv` into `data/raw/`. If the download is refused (HTTP 403), download the full table as CSV from the table page under Download options and unpack it into `data/raw/`.
2. The `data/raw/` folder is git-ignored, so the raw files are not stored in the repository.
3. Run `python src/fpa/audit_table.py data/raw/33100226.csv` to repeat the audit.

## Other sources read

- The Daily, 2026-08-24, Quarterly financial statistics for enterprises, second quarter 2026: https://www150.statcan.gc.ca/n1/daily-quotidien/260824/dq260824a-eng.pdf
- The Daily, 2021-02-24 (survey coverage and government-support note): https://www150.statcan.gc.ca/n1/daily-quotidien/210224/dq210224a-eng.htm
- Survey page: https://www150.statcan.gc.ca/n1/en/surveys/2501
