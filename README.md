# FP&A Intelligence: Revenue, Cost & Profitability Forecasting

**Independent Financial Analytics & Data Science Project**

## Project Summary

This project develops an end-to-end financial planning and analysis (FP&A) framework that combines financial analytics, statistical modelling, machine learning and business intelligence to support data-driven financial decisions.

Using publicly available Canadian financial data, the project focuses on three interconnected areas:

1. **Revenue Forecasting:** Evaluate statistical and machine learning models to predict quarterly revenue and compare forecasting accuracy against simple baselines (naive and drift).
2. **Operating Cost Analysis:** Measure how operating cost responds to changes in revenue in each industry. Cost is derived as revenue minus operating profit, because the source table has no cost lines.
3. **Profitability Analysis:** Analyze operating margins, assess financial risks and develop scenario-based insights on how far margin falls when revenue drops.

## Business Objective

Build a reproducible FP&A decision-support solution that helps finance professionals improve revenue forecasts, monitor operating costs, evaluate profitability risks and communicate actionable insights to senior management.

**Intended Users:** FP&A Analysts, Finance Managers, Financial Controllers and CFOs.

## Research Questions

- **RQ1 (forecasting):** For one-quarter-ahead forecasts of operating revenue, do statistical and machine learning models achieve a lower MAE than the naive and drift baselines, and in which industries do they fail to beat them?
- **RQ2 (cost behaviour):** By how much does operating cost change when revenue changes by 1%, and does this differ between steady and volatile industries?
- **RQ3 (risk):** If revenue falls by 5%, 10% or 20%, how many percentage points does operating margin fall, and which industries are most exposed?

Secondary questions, if time allows: whether forecasting margin directly beats forecasting revenue and cost separately, how much the 2020 shock affects accuracy, and which industries explain the 2026-04 margin rise.

## Data

Statistics Canada, Table 33-10-0226-01, Quarterly balance sheet and income statement, by industry, seasonally adjusted. The audit is complete:

- 26 quarters, from Q1 2020 to Q2 2026, in millions of dollars.
- 9 industries and 3 measures (revenue, cost, operating profit), which makes 27 series.
- Finance and insurance are excluded, because their sales series are empty.

Full findings, known issues and reproduction steps are in [`data/README.md`](data/README.md).

## Project Approach

The project follows five structured development phases:

1. Project Strategy & Feasibility
2. Data Architecture & Quality Assessment
3. Financial Analytics & Predictive Modelling
4. Model Evaluation & Business Insights
5. Executive Dashboard & Final Presentation

## Project Status

**Phase 1 — Project Strategy & Feasibility: In Progress.** The data audit, scope decisions and research questions are done; the data biography, pipeline sketch and project design document are being completed.

## Repository Guide

- `decision_log/`: every project decision, with alternatives and evidence.
- `data/README.md`: the data audit.
- `docs/data_biography.md`: where the data come from, limits and ethics.
- `src/fpa/`: Python modules and scripts (shared setup in `common.py`).

## Attribution

Adapted from Statistics Canada, Table 33-10-0226-01, Quarterly balance sheet and income statement, by industry, seasonally adjusted (x 1,000,000), 2026-08-24. This does not constitute an endorsement by Statistics Canada of this product.