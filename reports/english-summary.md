# Uniswap v3 on Base: Single-Pool Activity, Address Return and Concentration

Observation period: 27 July to 19 October 2026 (UTC, end exclusive). Report date: 25 October 2026.

## Scope and question

Analyze activity, exact-week address return and trading-leg concentration in the WETH/USDC 1% pool on Base, Uniswap v3 (0x0b1c2dcbbfa744ebd3fc17ff1a96a1e1eb4b2d69). This is a complete single-pool population, not a protocol-wide sample or a count of people. Observation: [27 July, 19 October 2026), UTC; a 28-day buffer precedes eight complete reporting weeks.

## Evidence

The 84-day export contains 15,123 Swap events, 14,300 distinct transactions and 2,086 transaction-origin addresses. Public RPC logs cover 3,696 contiguous block segments; parent transaction.from is available for every transaction. Daily boundaries were verified. One complete day (302 events) matches an independent provider, and eight cross-week receipts were checked. No claim is made that a second provider re-extracted all 84 days.

Estimated USD equals the absolute USDC-side quantity times its daily historical price. Duplicate event keys, missing origins and missing accepted prices are all zero. Estimates are not Dune amount_usd, revenue or net inflows; no bot or wash-trading filter is claimed.

## Three findings

In the week starting 12 October, active addresses rose from 326 to 521 (+59.82%), while distinct transactions rose from 689 to 1,612 (+133.96%) and estimated trading-leg USD rose 32.51%. The reappearing group increased by 104 of the net 195 addresses. This is an accounting decomposition, not marketing attribution.
For the same six W2-mature first-observed cohorts (N=806), W1 return was 154/806=19.11% and W2 was 149/806=18.49%. W2 does not require W1 activity. Three immature cells remain NA. Window-first-observed does not mean a genuinely new protocol user.
In the latest week, ceil(1% × 521) = 6 addresses contributed 18.61% of estimated USD; the Top 10 contributed 22.58%. The latest USD change was +32.51% before exclusions, +33.66% after excluding each week’s own Top 1%, and +46.24% after excluding the preceding week’s Top 1% from both weeks. These answer different sensitivity questions and do not predict an actual exit scenario.

## Operational implications

Track first-observed, continuing and reappearing activity alongside mature return cohorts and both amount- and transaction-based concentration. Investigate cross-pool routing before calling an address’s absence protocol churn. Obtain authorized product funnel, exposure and user-level evidence before proposing causal experience or marketing improvements. These are proposals for monitoring and further research; causal effects have not been evaluated.

## Methods and limitations

UTC Monday weeks; distinct tx_from at each grain; first observation computed over all 84 days; one activity flag per address-week. Concentration uses positive-priced valid origins, USD descending/address ascending ties, and ceil(.01N). Transaction concentration ranks independently. Both exclusion rules and all seven weekly comparisons are reported. Raw-event set calculations reconcile with SQL; integer USDC values match exactly and USD uses a predeclared absolute tolerance of 1e-6.

Addresses may represent intermediaries, multiple users or multiple wallets per person. Limited historical lookback, single-pool routing and daily valuation restrict interpretation. The project supports descriptive analysis within its scope, not protocol-wide retention, verified people, investment outcomes or causal claims.

## Deliverables

Offline three-view HTML dashboard; Chinese report; English summary; seven static figures; CSV tables; executed SQL and reproducible scripts; raw request evidence and SHA256 manifests. Source records, query parameters and checksums accompany the results.
