# Market Data Guidance

Use this reference to keep financial analysis timely. The goal is not to use the most sources; it is to use the freshest reliable primary data for facts that can change quickly, and to label the timestamp of every market-sensitive number.

## Recency Gate

Before making a current investment view, capture:
- retrieval date and time, plus timezone when available
- market status: open, closed, pre-market, after-hours, suspended, or holiday
- latest price, currency, market cap, enterprise value if used, and data vendor
- current P/E and 5/10/20-year P/E percentile data when P/E is meaningful, plus the selected horizon and reason
- latest annual report period, latest interim/quarterly period, and filing or publication date
- latest company announcements since the last financial report
- latest earnings call, guidance update, dividend/buyback announcement, financing, M&A, litigation, or regulatory notice
- recent news window used: normally 30-90 days, shorter for fast-moving events and longer for structural/regulatory issues

If the user asks "now", "today", "latest", "recent", "还能买吗", "现在怎么看", or anything price-sensitive, verify current market data and recent announcements first. Do not rely on memorized prices, stale ratios, or old screenshots.

## Freshness Targets

| Data type | Freshness target | Notes |
| --- | --- | --- |
| Price, market cap, volume | Same trading day when possible | If delayed, state vendor delay or retrieval time. |
| Intraday or event-driven price moves | Minutes to same day | Use only when the user asks for current reaction or catalyst timing. |
| Valuation multiples | Same day or derived from same-day price | Label whether TTM, forward, GAAP, non-GAAP, or normalized. |
| P/E percentile | Same day or latest available market-data snapshot | State data vendor, P/E basis, history span used, and why 5, 10, or 20 years is the best fit. |
| Annual financials | Latest filed annual report | If a newer quarter exists, annual data alone is stale for current view. |
| Quarterly/interim financials | Latest filed period | State period end and filing date. |
| Guidance/earnings call | Latest company release or transcript | Check for updates after the financial statement date. |
| Company announcements | Since latest report, plus last 30-90 days | Primary filings beat media summaries. |
| News/catalysts | Last 30-90 days by default | Extend for lawsuits, regulation, product cycles, credit stress, and policy changes. |
| Macro rates, FX, commodities | Same day when material | Use only through company-specific exposure. |

## Source Priority By Data Type

Use primary sources for facts, market data vendors for live prices, and reputable media only for context or when primary confirmation is not yet available.

| Need | Preferred sources | Cross-check |
| --- | --- | --- |
| Filings and official announcements | SEC EDGAR, company IR, exchange filings, HKEXnews, Shanghai/Shenzhen exchange disclosure sites | Company press releases, transcripts |
| Current price and market cap | Exchange quote pages, Nasdaq/NYSE/HKEX pages, Yahoo Finance, TradingView, Koyfin-style market pages | A second market-data source when conclusion depends on price |
| P/E percentile | Market-data platforms with historical valuation bands, exchange/finance portals, Macrotrends/Koyfin/TradingView-style pages, or akshare-style datasets for A-shares | Recalculate from historical price and earnings data when practical; otherwise label vendor methodology limits. |
| Financial statements | Company reports, SEC XBRL, exchange filings, annual/interim reports | Finance portals and databases only after checking period/date |
| Earnings call and guidance | Company IR transcript/audio/presentation | Reputable transcript services or financial media |
| News and catalysts | Company/regulator/court filings first, then Reuters/Bloomberg/WSJ/FT/CNBC/official local media | Multiple outlets for unconfirmed or anonymous-source reports |
| Macro variables | Central banks, official statistics agencies, treasury/FX/commodity exchange sources | Reputable financial data vendors |

## US Stocks

Prefer:
- SEC EDGAR 10-K, 10-Q, 8-K, proxy statements, and Form 4/13D/13G when ownership matters
- company investor relations pages, earnings releases, presentations, and transcripts
- exchange or market-data pages for current price, market cap, volume, and trading status
- reputable financial news for recent catalysts and risk events

Useful searches:
- `<ticker> latest 10-Q 10-K revenue operating income free cash flow filing date`
- `<ticker> investor relations quarterly results earnings presentation transcript`
- `<ticker> latest 8-K guidance buyback dividend restructuring`
- `<ticker> current price market cap after hours premarket`
- `<ticker> latest news earnings guidance regulatory investigation last 30 days`

## China A-Shares

Prefer:
- Shanghai/Shenzhen/Beijing exchange disclosures and company announcements
- latest annual and quarterly reports, plus post-report announcements
- akshare or similar tools for market quotes and financial data when available, cross-checked against exchange/company filings for material claims
- CSRC, exchange inquiry letters, administrative penalties, and official policy releases when regulatory risk matters
- reputable Chinese financial media for context, not as the sole source for material facts

Typical metrics:
- PE, PB, PS, dividend yield, market cap, free-float market cap, turnover, trading suspension status
- ROE, ROA, gross margin, net margin
- asset-liability ratio, current ratio, quick ratio
- revenue/profit growth, operating cash flow quality, receivables and inventory movement

## HK Stocks And ADRs

Prefer:
- HKEXnews filings, company IR reports, announcements, and circulars
- home exchange filings for global issuers
- SEC filings for ADRs when applicable
- exchange or market-data pages for current price, market cap, currency, and ADR ratio

Normalize:
- reporting currency and trading currency
- fiscal year end
- accounting standards
- share classes, ADR ratio, and market cap basis
- Hong Kong lot size, liquidity, and trading suspension status when relevant

## Cross-Source Conflict Rules

When sources disagree:
- Prefer primary filings for financial statements and official events.
- Prefer exchange or reputable market-data vendors for current price and volume.
- Check whether ratios use TTM, forward estimates, adjusted earnings, different currencies, or stale share counts.
- Recalculate simple ratios directly when possible: market cap, EV, P/E, P/B, FCF yield, dividend yield.
- If a discrepancy remains material, show the range and state which source drives the conclusion.

## P/E Percentile Data

For each stock analysis where P/E is meaningful:
- Try to gather 5-year, 10-year, and 20-year P/E percentile data or enough historical P/E data to compute them.
- Select the primary horizon case by case and explain the reason in the final answer.
- Prefer 5 years when the company is newly listed, transformed, or has limited comparable public history.
- Prefer 10 years as the default for seasoned companies with comparable earnings across a full cycle.
- Prefer 20 years for mature, long-listed companies where older cycles remain relevant.
- State whether the percentile uses trailing, forward, GAAP, adjusted, or normalized P/E.
- Check whether the latest or historical EPS includes material non-recurring distortions such as tax provisions or benefits, impairments, litigation, restructuring, subsidies, asset disposals, or accounting changes. If so, compute or request an adjusted/normalized P/E percentile when possible.
- Warn the user when the reported P/E percentile is distorted by those items, and state whether the valuation view relies on adjusted earnings or treats P/E percentile as low-confidence evidence.
- If earnings are negative, near zero, distorted by one-offs, or structurally cyclical, say P/E percentile is low-quality evidence and use a better anchor.

## Data Hygiene

- Use the latest available price only after checking the current date and market status.
- Label financial data by fiscal year/quarter, period end, report date, and retrieval date.
- Use trailing and forward metrics carefully; say which one is used and whether it is consensus, company guidance, or your estimate.
- For P/E percentile, label the selected span, current percentile, vendor or calculation method, and the reason that span is reasonable for the specific company.
- Reconcile big discrepancies across sources before drawing conclusions.
- Prefer primary sources for material claims: filings, exchange announcements, company releases, transcripts, regulator notices.
- Treat unsourced social-media rumors and promotional commentary as noise unless confirmed by primary or highly reputable sources.
- When news is fast-moving, include exact publication dates and distinguish confirmed facts from market speculation.
- If data is unavailable, stale, delayed, or blocked, continue only with a clearly marked limited analysis and reduce confidence.
