← BACK TO PORTFOLIO / SELECTED WORK

RESEARCH 01 · ONCHAIN PRODUCT ANALYTICS

# Activity rebounded. Who came back?

Study participation, first-observed address return and trading concentration in one Uniswap v3 WETH/USDC 1% pool on Base. Separate operational evidence from explanations that need more data.

2026.07.27 — 10.19 UTC / end exclusiveSQL · Python · Cohort AnalysisCompleted / 2026.10
[Report PDF · Chinese ↗](report.pdf) · [Dashboard · Chinese ↗](../app/dashboard.html) · [SQL & data ↗](https://github.com/xiwang-geo/uniswap-base-analysis)[English summary ↗](english-summary.md)

01 / QUESTION

## More participation, or more trading by a few origins?

Address counts, transaction counts and trading amounts can move differently. The study asks whether activity composition changed, whether first-observed origins returned in later calendar weeks, and how much estimated amount was concentrated among a few origins.

The 84-day population contains 15,123 Swap events, 14,300 distinct transactions and 2,086 transaction origins. A 28-day buffer precedes eight displayed full weeks. The parent transaction’s `from` field is an address proxy, not a verified person or website visitor.

02 / FINDINGS

## Three findings. Three different questions.

**+59.82%**

### Activity rebound

Latest full-week origins: 326 → 521. Reappearing origins increased by 104, or 53.33% of the net gain of 195.

**19.11%**

### Comparable W1 return

Same six mature cohorts: W1 154/806; W2 149/806, or 18.49%.

**18.61%**

### Top-origin amount share

Latest-week amount Top 1%, rounded up to six origins, contributed 18.61% of estimated USDC-leg USD.

03 / ACTIVITY

## Read addresses, transactions and amounts together.

![Eight-week source figure: latest week 521 active origins, 1612 transactions and USD 460443.59 in estimated trading-leg amount](../assets/01-八周趋势分面图.png)

Original Chinese source figure. Same pool and week boundaries; separate panels for different units. USD uses daily historical prices for the USDC leg.

Latest-week origins grew 59.82%, transactions 133.96% and estimated amount 32.51%. Splitting active origins into first-observed, continuously active and reappearing groups gives net changes of +17, +74 and +104.

Reappearance is a useful research lead. Membership changes each week, so this accounting decomposition does not establish successful reactivation marketing. Cross-pool activity, inter-trade intervals and actual contact evidence would be needed.

04 / ADDRESS RETURN

## Too little observation is not zero return.

![First-observed address cohort heatmap; three immature W1/W2 cells remain NA](../assets/04-首次观察地址回访热力图.png)

W1 and W2 mean the first and second subsequent calendar weeks. W2 does not require W1 activity. At most one activity flag per origin-week.

All mature W1 cohorts give 158/869; all mature W2 cohorts give 149/806. Their populations differ. Restricting both to the same 806 origins yields W1 19.11% and W2 18.49%. Do not compare inconsistent maturity populations or average cohort percentages without weighting.

First observation refers only to this pool and 84-day window. Absence from one pool is not protocol churn; an origin is not necessarily a person.

05 / CONCENTRATION

## Growth survives head removal. That is not an exit forecast.

Latest-week estimated amount grew 32.51%. Removing each week’s own amount Top 1% leaves 33.66% growth. Removing the same four prior-week head origins from both weeks leaves 46.24% growth.

![All seven adjacent-week comparisons showing original amount growth and dynamic versus fixed-head removal](../assets/07-两种剔除敏感性.png)

Dynamic and fixed sets answer different questions. Every adjacent comparison is retained. Exclusion does not model liquidity, price or routing feedback.

The independently ranked transaction-count Top 1% accounts for 24.88% of transactions. The six amount-ranked origins account for 21.96% of transactions. These sets are not interchangeable: always state the metric, population, rounding and ranking rule.

06 / IMPLICATIONS

## Turn observations into bounded next steps.

Include all three activity groups in weekly monitoring

Investigate reappearing origins’ trade intervals and routing context. Add cross-pool evidence before considering reactivation research. Composition differences are not channel attribution.

Distinguish pool absence from protocol departure

Check other pools, fees and failed transactions, then use an authorized product funnel to investigate experience. These address cohorts are not user-level seven-day product retention.

Monitor scale, address return and concentration together

Track activity, mature return cohorts and amount/count concentration, retaining both sensitivity rules. No operational experiment or measured causal improvement was established.

07 / METHOD & QUALITY

## Keep the calculation behind the conclusion.

- Collected events over 3,696 contiguous, non-overlapping block segments and completed every parent transaction origin.

- Deduplicated by UTC day and week. 370 transactions contain multiple same-pool events; event rows are not transaction counts.

- Independently recalculated from structured source events and reconciled SQL group, return and concentration results.

- Cross-checked one full day of 302 events with an independent provider and eight cross-week receipts; this is not a second extraction of all 84 days.

- Retained integer USDC units, allowed a USD 0.000001 absolute floating-point reconciliation tolerance, and preserved immature cells as NA.

Scope: Base Uniswap v3 WETH/USDC 1% pool. Amount is a trading-leg estimate, not revenue or net inflow. No identity resolution or verified bot/wash-trading exclusion is claimed.

08 / EXPLORE THE EVIDENCE

## Read the study. Inspect the numbers.

[8-page report · Chinese ↗](report.pdf) · [Three-view dashboard · Chinese ↗](../app/dashboard.html) · [GitHub · SQL, data & reproduction ↗](https://github.com/xiwang-geo/uniswap-base-analysis)[English executive summary ↗](english-summary.md)

Figures and results are unchanged copies from the archived analysis. The repository reproduces key metrics from the local structured snapshot; it does not freshly acquire all source data.

RESEARCH 02 / FINANCIAL PRODUCT

## Another question: how should same-index ETFs be compared?

Five funds, three windows: from fee and tracking evidence to an interactive fund-comparison tool.

[Read the ETF case ↗](https://github.com/xiwang-geo/csi300-etf-analysis)

DISCUSS THE WORK

## Let’s discuss the evidence and the decision.

[Email ↗](mailto:xiwang.geo@outlook.com)
