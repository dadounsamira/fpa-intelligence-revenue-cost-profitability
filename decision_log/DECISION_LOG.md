# FP&A Intelligence — Decision Log

**Project:** Revenue, Cost & Profitability Forecasting
**Type:** Independent Finance & Data Science Portfolio Project
**Purpose:** Document important decisions, alternatives,
assumptions, evidence, and changes throughout the project.

---

## DEC-001 — Project Scope

**Date:** 2026-11-16
**Phase:** 1 — Project Strategy & Feasibility
**Status:** Accepted

### Decision
Develop an integrated FP&A analytics project covering
revenue forecasting, operating cost analysis, and
profitability assessment.

### Rationale
Demonstrate financial planning, financial analysis,
predictive modelling, and business decision support.

### Alternatives Considered
- Revenue forecasting only
- Cash flow forecasting and liquidity risk
- Profitability forecasting only
- Operating expense forecasting
- Financial benchmarking
- Capital expenditure analysis

### Limitations
The scope may need refinement after the data audit.
Refined by DEC-006 after the data audit.

---

## DEC-002 — Project Positioning

**Date:** 2026-11-16
**Phase:** 1 — Project Strategy & Feasibility
**Status:** Accepted

### Decision
Position FP&A Intelligence as an independent
professional portfolio project, not a university
assignment.

### Rationale
Build a project demonstrating practical finance,
analytics, and data science capabilities.

### Methodology
Follow five structured development phases inspired
by a rigorous academic capstone framework.

---

## DEC-003 — Primary Data Source

**Date:** 2026-11-16
**Phase:** 1 — Project Strategy & Feasibility
**Status:** Accepted

### Decision
Use Statistics Canada Table 33-10-0226-01
as the primary source of quarterly financial data.

### Source
https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3310022601

### Rationale
Use real, publicly documented Canadian financial data.

### Required Verification
- Manufacturing industry coverage
- Available financial statement variables
- Historical data coverage
- Missing or suppressed observations
- Suitability for revenue forecasting

### Verification Outcome (2026-11-17)
- Coverage: 55 industry groupings × 5 financial items × 26 quarters
  (Q1 2020 to Q2 2026); no missing quarters.
- Variables: revenue and operating profit are available; there is no
  cost column (see DEC-008).
- Missing data: 14 series are empty, all finance and insurance
  (see DEC-009).
- Limits: sample survey of incorporated enterprises; excludes
  government-controlled and not-for-profit corporations; history only
  from 2020; Statistics Canada may revise past values (note 5).
- Licence: Statistics Canada Open Licence; attribution to Statistics
  Canada and the table is required in the README.
- Suitability: suitable for the scope in DEC-006.

---

## DEC-004 — Forecasting Strategy

**Date:** 2026-11-16
**Phase:** 1 — Project Strategy & Feasibility
**Status:** Revised — see DEC-010

### Decision
Prioritize one-quarter-ahead revenue forecasting.

### Proposed Approach
Compare statistical and machine learning models
against a seasonal naive baseline.

### Evaluation
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Forecast bias
- Chronological validation

### Limitations
Model selection depends on available observations
and the quality of historical financial data.

### Revision (2026-11-17)
The table is seasonally adjusted, so the seasonal naive baseline is
replaced by naive and drift baselines. See DEC-010.

---

## DEC-005 — Development Environment

**Date:** 2026-11-16
**Phase:** 1 — Project Strategy & Feasibility
**Status:** Accepted

### Decision
Use PyCharm, Python, Git, and GitHub for project
development and version control.

### Supporting Tools
- SQL for data storage and querying
- Power BI for management dashboards
- Excel for financial validation and analysis

### Rationale
Create a reproducible, maintainable workflow
that reflects professional analytics practices.

---

## DEC-006 — Forecasting Scope: 9 Industries × 3 Measures

**Date:** 2026-11-17
**Phase:** 1 — Project Strategy & Feasibility
**Status:** Accepted

### Context
Table 33-10-0226-01 has 55 industry groupings. Forecasting all of
them is not realistic within the one-week project timeline.

### Decision
Forecast 9 industries: total non-financial industries; clothing,
sporting goods and general merchandise stores; other wholesalers;
construction; oil and gas extraction and support services; food and
soft drink and ice manufacturing; professional, scientific and
technical services; real estate; and telecommunications.
For each, forecast revenue, cost and operating profit: 27 series of
26 quarters each (Q1 2020 to Q2 2026).

### Alternatives Considered
- All 55 industries
- A single industry (for example manufacturing only)
- The largest industries by revenue only
- Including a health care industry (not possible, see Evidence)

### Rationale
The mix covers steady series (telecommunications, professional
services) and volatile series (oil and gas), so models cannot look
good by being tested only on easy series. All 9 industries have
complete data for all 26 quarters.

### Evidence
- Oil and gas quarterly change: standard deviation about 18.1% with
  2020 included, about 11.0% without.
- Telecommunications and professional services are the steadiest.
- Health care cannot be isolated: the table reports it only inside
  "Educational, health care and social assistance services" (about 2%
  of non-financial revenue in 2026-04).

### Risks and Limitations
- The other 46 groupings are out of scope, including the 14 finance
  and insurance groupings (see DEC-009).
- The survey excludes government-controlled and not-for-profit
  corporations, which cover most public health care.
- Results describe these 9 private-sector industries, not the whole
  Canadian economy.
- The total and its component industries are forecast separately, so
  their forecasts may not sum; reconciliation is out of scope.

### Next Action
Apply the same scope in `common.py` and all scripts.

---

## DEC-007 — Flag the 2020 Shock; Do Not Delete It

**Date:** 2026-11-17
**Phase:** 1 — Project Strategy & Feasibility
**Status:** Accepted

### Context
The 2020-04 drop affected many industries at once and could distort
model training and scoring.

### Decision
Add a shock flag to quarters 2020-04 and 2020-07. Keep them in the
data and score the models on later quarters.

### Alternatives Considered
- Delete the two quarters
- Ignore the shock and treat all quarters equally
- Start the history after 2020 (not possible: the table starts in 2020)

### Rationale
The shock affects industries unevenly, so a score that includes it
would mostly measure how a model handled a one-off event. Deleting
the quarters would hide a real event.

### Evidence
- Oil and gas volatility falls from about 18.1% to about 11.0% when
  2020-04 and 2020-07 are removed.
- Telecommunications and professional services change little.
- Amounts in 2020-21 include government support (for example CEWS)
  counted as revenue.

### Risks and Limitations
- The flag adds a modelling step.
- Scoring on later quarters leaves fewer test points.

### Next Action
Create the flag column during feature engineering.

---

## DEC-008 — Derive Cost as Revenue Minus Operating Profit

**Date:** 2026-11-17
**Phase:** 1 — Project Strategy & Feasibility
**Status:** Accepted

### Context
The table has no operating cost column.

### Decision
Cost = total operating revenue − operating profit or loss.
Margin = profit ÷ revenue. Use total operating revenue as the revenue
measure for every industry.

### Alternatives Considered
- Forecast revenue and profit only, without cost
- Use a separate source for expenses (none available in this table)

### Rationale
Statistics Canada's note 6 says that since Q1 2020, operating
revenue, expenses and operating profit are all derived from other
variables, so the subtraction is consistent with how the numbers are
built.

### Evidence
Non-financial total, 2026-04 (million dollars): revenue 1,472,376,
profit 126,571, cost 1,345,805, margin 8.60%.

### Risks and Limitations
- Derived cost has no independent check; an error in profit passes
  straight into cost.
- Values are nominal dollars, so part of the growth is price inflation.

### Next Action
Compute cost and margin for all 9 industries in a shared function.

---

## DEC-009 — Exclude Finance and Insurance

**Date:** 2026-11-17
**Phase:** 1 — Project Strategy & Feasibility
**Status:** Accepted

### Context
The 14 finance and insurance groupings have no "Sales of goods and
services" values, and insurance has an accounting break in 2023.

### Decision
Exclude finance and insurance. Use "Total, non-financial industries"
as the overall measure instead of "Total, all industries".

### Alternatives Considered
- Include them using a different revenue measure
- Use "Total, all industries" and accept the break

### Rationale
Including them would mix a missing measure and a structural break
into the results.

### Evidence
- 14 of 275 series are empty (364 empty cells).
- Note 7: IFRS 17 break between Q4 2022 and Q1 2023 in insurance
  industries; the non-financial total is not affected.

### Risks and Limitations
Finance and insurance is about 13% of total operating revenue
(222,100 of 1,694,476 in 2026-04), so results describe the
non-financial economy only.

### Next Action
Document the exclusion in `data/README.md`.

---

## DEC-010 — Baselines and Validation

**Date:** 2026-11-17
**Phase:** 1 — Project Strategy & Feasibility
**Status:** Accepted

### Context
The table is seasonally adjusted, so a seasonal naive baseline
(copying the same quarter last year) would be weak. This revises
DEC-004.

### Decision
Prioritize one-quarter-ahead forecasts of revenue, cost and operating
profit. Compare statistical and machine learning models against two
baselines: naive (next quarter equals the last quarter) and drift
(last value plus the average quarterly change). Evaluate with MAE,
RMSE and forecast bias, using expanding-window time-series validation
(roughly 16 quarters for training, 10 for testing).

### Alternatives Considered
- Seasonal naive baseline (original proposal in DEC-004)
- A single fixed train/test split

### Rationale
A model only counts if it beats naive and drift. An expanding window
uses the 26 quarters better than one fixed split.

### Evidence
Seasonality was checked: the series are labelled seasonally adjusted
in the table.

### Risks and Limitations
10 test quarters is a small test set, so scores will be noisy and
reported with that caveat.


## DEC-011 — Use Nominal Dollars (No Inflation Adjustment)

**Date:** 2026-11-17
**Phase:** 1 — Project Strategy & Feasibility
**Status:** Proposed

### Context
Table 33-10-0226-01 reports values in millions of current (nominal)
dollars. Part of any revenue or cost growth is therefore price
inflation, not volume growth.

### Decision
Forecast the values as published, in nominal dollars, without
adjusting for inflation.

### Alternatives Considered
- Deflate all series with the Consumer Price Index
- Forecast growth rates instead of levels

### Rationale
FP&A budgets and forecasts are normally stated in nominal dollars,
so the outputs match how the business would use them. Deflating adds
a second data source and a new assumption within a one-week project.
Margins (profit ÷ revenue) are ratios and are not distorted by
inflation.

### Evidence
- The table states its unit as millions of dollars, not chained
  dollars.
- The 2026-04 margin of 8.60% (DEC-008) is unaffected by the choice.

### Risks and Limitations
- Revenue and cost growth overstate real growth.
- Comparing quarters across years mixes volume and price effects.
- The README must state that all amounts are nominal.

### Next Action
State the unit and the nominal basis in `data/README.md` and in the
final report. Revisit with a CPI adjustment if time allows.

---

## DEC-012 — Shared Module for Common Code

**Date:** 2026-11-17
**Phase:** 1 — Project Strategy & Feasibility
**Status:** Accepted

### Context
Several scripts repeated the same setup: the path to the CSV, the two
long column names, the industry list, and the line that reads the
file. A change to any of them would have to be made in every script.

### Decision
Keep shared code in `src/fpa/common.py`: the constants, the
`INDUSTRIES` list and a `load_table()` function. Scripts import what
they need from it and keep only logic that belongs to them.

### Alternatives Considered
- Self-contained scripts that each repeat the setup
- Logic placed inside notebooks

### Rationale
Each fact (a path, a column name, the industry list) is written in
one place, so a change is made once. Scripts become shorter and easier
to read, and the shared code can be tested on its own.

### Evidence
- `build_cost.py`, `plot_scope.py` and `volatility.py` were refactored
  to import from `common.py`.
- Outputs were checked against the earlier versions: for
  `build_cost.py` the 2026-04 row is identical (revenue 1,472,376.0,
  profit 126,571.0, cost 1,345,805.0, margin 8.596378).

### Risks and Limitations
- `check_seasonality.py` and `list_industries.py` still carry their
  own setup lines.
- `ingest.py` still uses a relative path for the raw data folder.

### Next Action
Refactor the remaining scripts and anchor the path in `ingest.py`
with `Path(__file__)`.

### Next Action
Build the baselines and the validation split.

## DEC-013 — Research Questions and Success Criterion

**Date:** 2026-11-18
**Phase:** 1 — Project Strategy & Feasibility
**Status:** Accepted

### Context
The project needs research questions that are connected, tied to a
real planning problem, and answerable with the audited data
(26 quarters, 9 industries, revenue and derived cost).

### Decision
Main questions:
- **RQ1 (forecasting):** For one-quarter-ahead forecasts of operating
  revenue in the 9 industries, do statistical and machine-learning
  models achieve a lower MAE than the naive and drift baselines, and
  in which industries do they fail to beat them?
- **RQ2 (cost behaviour):** By how much does operating cost change
  when revenue changes by 1% in each industry, and does this differ
  between steady industries (telecommunications) and volatile ones
  (oil and gas)?
- **RQ3 (risk):** If revenue falls by 5%, 10% or 20%, how many
  percentage points does operating margin fall in each industry, and
  which industries are most exposed?

Secondary questions (only if time allows):
- **S1:** Is it more accurate to forecast margin directly, or to
  forecast revenue and cost separately and subtract?
- **S2:** How much does keeping the 2020-04 and 2020-07 quarters in
  the training data change forecast accuracy? (tests DEC-007)
- **S3:** Which industries explain the rise in the non-financial
  margin in 2026-04? Descriptive only, and partial, because only 8
  component industries are in scope.

Success criterion (set before seeing results): a model counts as
better than the baselines when its MAE is lower than the better of
naive and drift over the test quarters. RMSE and forecast bias are
reported alongside. RQ2 and RQ3 have no pass or fail threshold; they
report estimates with their uncertainty.

Impact hypothesis: forecasts that beat the baselines, together with a
measured cost response to revenue, would let an FP&A team plan next
quarter's margin with smaller errors and see in advance which
industries lose most margin in a downturn.

### Alternatives Considered
- RQ2 as "which cost lines are fixed or variable" (not answerable:
  the table has no cost lines, see DEC-008)
- A percentage threshold such as "10% below naive" (too unstable with
  about 10 test quarters)
- Asking whether the 2026-04 margin rise is a trend (cannot be
  answered reliably with 26 quarters)

### Rationale
Each question builds on the previous one: RQ1 forecasts revenue, RQ2
measures how cost follows revenue, and RQ3 uses that response for
margin scenarios. All three use only data we have audited.

### Evidence
- RQ1: complete revenue series for all 9 industries, 26 quarters.
- RQ2: a first check on the 9 industries (excluding 2020-04 and
  2020-07) gave cost responses from about 0.55 (oil and gas) to about
  1.21 (telecommunications); the non-financial total was 0.87.
- RQ3: scenario arithmetic from the RQ2 estimates and current margins.

### Risks and Limitations
- About 10 test quarters make RQ1 results noisy.
- RQ2 estimates rest on about 24 quarterly changes and are rough,
  especially where revenue barely moves (telecommunications).
- RQ3 is a what-if calculation, not a forecast, and assumes the cost
  response stays stable.

### Next Action
Tick steps 1.7.1 to 1.7.6 in the tracker; use these questions in the
project design document and the data biography.

---

## Template — Future Decisions

### DEC-XXX — Decision Title

**Date:** YYYY-MM-DD
**Phase:**
**Status:** Proposed / Accepted / Revised / Rejected

### Context
What problem required a decision?

### Decision
What did we decide?

### Alternatives Considered
What other approaches were evaluated?

### Rationale
Why was this approach selected?

### Evidence
What data, documentation, or results support it?

### Risks and Limitations
What could go wrong?

### Next Action
What needs to happen next?