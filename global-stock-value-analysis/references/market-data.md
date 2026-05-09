# Market Data Guidance

Use this reference to keep financial analysis timely. The goal is not to use the most sources; it is to use the freshest reliable primary data for facts that can change quickly, and to label the timestamp of every market-sensitive number.

## Recency Gate

Before making a current investment view, capture:
- retrieval date and time, plus timezone when available
- market status: open, closed, pre-market, after-hours, suspended, or holiday
- latest price, currency, market cap, enterprise value if used, and data vendor
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

## Data Hygiene

- Use the latest available price only after checking the current date and market status.
- Label financial data by fiscal year/quarter, period end, report date, and retrieval date.
- Use trailing and forward metrics carefully; say which one is used and whether it is consensus, company guidance, or your estimate.
- Reconcile big discrepancies across sources before drawing conclusions.
- Prefer primary sources for material claims: filings, exchange announcements, company releases, transcripts, regulator notices.
- Treat unsourced social-media rumors and promotional commentary as noise unless confirmed by primary or highly reputable sources.
- When news is fast-moving, include exact publication dates and distinguish confirmed facts from market speculation.
- If data is unavailable, stale, delayed, or blocked, continue only with a clearly marked limited analysis and reduce confidence.
