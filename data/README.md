# Data: Statistics Canada Table 33-10-0226-01

Audit started 2026-11-16 (tracker steps 1.3.1 to 1.3.8). Items marked **Verified** were read from Statistics Canada pages. Items marked **To check** need the downloaded CSV; run `src/fpa/audit_table.py` on it (see the end of this file).

## What the table is

| Item | Finding | Status |
| --- | --- | --- |
| Title | Quarterly balance sheet and income statement, by industry, seasonally adjusted (x 1,000,000) | Verified |
| Table ID and DOI | 33-10-0226-01, DOI 10.25318/3310022601-eng | Verified |
| Source survey | Quarterly Survey of Financial Statements (survey 2501) | Verified |
| Coverage | Incorporated enterprises operating in Canada | Verified |
| Frequency and geography | Quarterly, Canada only | Verified |
| Seasonal adjustment | Seasonally adjusted | Verified |
| Units | Millions of dollars | Verified |
| Latest release | 2026-08-24 (page shows 2026-11-16 as date modified) | Verified |
| Industry list | Includes total, financial and non-financial industries; past releases cite manufacturing sub-industries from this table, for example primary metal and fabricated metal product and machinery manufacturing | Partly verified. Full list **to check** |
| Variables | Balance sheet and income statement items; releases cite operating revenue, operating profit and net income before taxes from this table | Partly verified. Full list **to check** |
| First and last quarter, number of quarters | Not shown on the page | **To check** |
| Footnotes, suppressed cells, symbols | The page refers to seven footnotes but their text did not load | **To check** |
| Licence | The page links to Statistics Canada's Terms and conditions; text not read yet | **To check** |

## What this means for the plan

1. **The series is already seasonally adjusted.** A seasonal naive baseline (same quarter last year) is a weak comparison on adjusted data because the seasonal pattern has been removed. Use the plain naive forecast (last quarter) as the main baseline and keep seasonal naive as a secondary one. DEC-004 needs this change.
2. **Not-seasonally-adjusted tables exist** for the same survey: 33-10-0224-01 (total all industries), 33-10-0225-01 (non-financial industries) and 33-10-0227-01 (financial industries). Switch to one of these only if the project needs to model seasonality itself. Compare which table gives the cost lines you need before deciding.
3. **The survey is a sample of larger corporations.** Statistics Canada says it covers corporations in Canada except government-controlled and not-for-profit ones. Results describe that population, not every business.
4. **2020 and 2021 amounts include government support** such as the Canada Emergency Wage Subsidy, which Statistics Canada counts as revenue for those businesses. Treat those quarters as a known structural break in the preprocessing spec.
5. **Industry level matters.** Decide in step 1.4 whether to model one industry (for example manufacturing) or the non-financial total. The CSV will show which cost lines exist at each level.

## Sources read

- Table page: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310022601
- The Daily, 2026-08-24, Quarterly financial statistics for enterprises, second quarter 2026: https://www150.statcan.gc.ca/n1/daily-quotidien/260824/dq260824a-eng.pdf
- The Daily, 2021-05-25 (manufacturing sub-industry cited from this table): https://www150.statcan.gc.ca/n1/daily-quotidien/210525/dq210525a-eng.pdf
- The Daily, 2021-02-24 (survey coverage and government-support note): https://www150.statcan.gc.ca/n1/daily-quotidien/210224/dq210224a-eng.htm
- Survey page: https://www150.statcan.gc.ca/n1/en/surveys/2501

## Finish the audit (about 10 minutes)

1. Open the table page above. Under Download options, choose the full table as CSV (displayed values) and save it as `data/raw/33100226-eng.csv`. The `data/raw/` folder is git-ignored, so record the download date here: ______
2. Run `python src/fpa/audit_table.py data/raw/33100226-eng.csv`.
3. Paste the printed output into this file under a new heading, "CSV audit results", and tick steps 1.3.2 to 1.3.7 in the tracker.
4. On the same page, read the footnotes and the Terms and conditions, and note the licence in `docs/data_biography.md`.
