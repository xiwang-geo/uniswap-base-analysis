# Uniswap v3 on Base — Activity, Return & Concentration

**English** · [简体中文](README.zh-CN.md)


![Research cover](assets/cover.svg)

An evidence-backed analysis of **one WETH/USDC 1% pool**: who was active, whether first-observed addresses returned, and how much estimated amount came from the top addresses.

[Case study](reports/case-study.en.md) · [Report PDF](reports/report.pdf) · [English summary](reports/english-summary.md) · [Offline dashboard](app/dashboard.html)

> Open the downloaded dashboard HTML in a browser. GitHub file preview displays source rather than running the application.

## Questions and findings

- Latest complete week: **521 active origins**, up **59.82%**. The reappearing group increased by 104 of the net 195 addresses; this is an accounting decomposition, not marketing attribution.
- The **same six mature cohorts**: W1 return **154/806 = 19.11%**, W2 **149/806 = 18.49%**. Immature cells stay NA.
- Latest-week amount Top 1%: **6 addresses**, contributing **18.61%** of estimated USD. Both dynamic and fixed-head exclusion rules are reported.

## Scope

Base, Uniswap v3, pool `0x0b1c2dcbbfa744ebd3fc17ff1a96a1e1eb4b2d69`. Observation **[2026-07-27, 2026-10-19) UTC**, with a 28-day buffer before eight displayed weeks. Full population: **15,123 events, 14,300 transactions, 2,086 origins**.

Sources: public Base RPC logs and parent transactions; daily historical USDC prices. One full day and eight cross-week receipts were cross-checked; a second provider did not re-extract all 84 days.

## Reproduce

Python 3.10+; standard library only; no API key or network needed.

```bash
python scripts/reproduce.py
```

The script uses the included event database, rebuilds reviewed views **in memory**, checks eight weekly rows, the common mature cohort counts and latest head concentration. The original snapshot stays unchanged. This is local snapshot reproduction, not a fresh source acquisition.

## Repository map

| Path | Contents |
| --- | --- |
| `reports/` | Full report and English summary |
| `app/` | Portable dashboard HTML |
| `sql/` | Executed trend, grouping, cohort and concentration queries |
| `data/` | Event database and reviewed CSV results |
| `scripts/reproduce.py` | Read-only reproduction and reconciliation |
| `SOURCE-NOTES.md` | Source scope and snapshot checksums |

## Limits and operational next steps

Origins are address proxies, not people. USD is an estimated trading-leg amount, not revenue or net inflow. Pool absence does not establish protocol churn. Head exclusion does not simulate an actual exit. Recommendations concern monitoring and further research; no campaign, randomized experiment or measured lift is claimed.
