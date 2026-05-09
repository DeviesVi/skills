---
name: global-stock-value-analysis
description: Unified value-investing and fundamental-analysis skill for global equities, especially US stocks and China A-shares, with market news and event analysis. Use for stock screening, single-stock research, peer comparison, valuation, financial health checks, news/catalyst review, risk review, and investment memo generation across markets such as AAPL, MSFT, NVDA, 600519, 000858, HK stocks, ADRs, or mixed portfolios.
---

# Global Stock Value Analysis

Unified workflow for value-investing oriented stock analysis across US stocks, China A-shares, HK stocks, ADRs, and mixed portfolios. The default lens is long-term business ownership: fundamentals, valuation, margin of safety, and risk first; market news is incorporated when it changes facts, probabilities, catalysts, or downside risk.

## When To Use

Use this skill when the user asks to:
- analyze a listed company or ticker
- screen stocks by value, quality, dividend, growth, or balance-sheet metrics
- compare several stocks or companies across the same or different markets
- estimate intrinsic value, fair value range, or margin of safety
- review fundamentals, financial health, accounting red flags, or business quality
- review market news, earnings events, regulatory changes, macro shocks, or company-specific catalysts
- produce an investment memo, watchlist, or portfolio-level research note

This skill is research support, not personalized financial advice. Use current data and state data dates clearly. For any current-market view, verify price, filings, and news recency before analysis; stale data must be labeled and should not drive a confident conclusion.

## Investment Philosophy

Prefer value-investing reasoning over short-term market commentary:
- Treat a stock as fractional ownership of a business.
- Start with durable earnings power, cash generation, balance-sheet resilience, and capital allocation.
- Require a margin of safety before calling valuation attractive.
- Use news to update the thesis, not to chase price action.
- Distinguish permanent impairment from temporary volatility.
- Admit uncertainty and show the assumptions that would change the conclusion.
- Stay inside the analyst's circle of competence. If the business, accounting, regulation, or technology is not understandable, mark it as "too hard" rather than forcing a view.
- Prefer great businesses with durable economics and fair prices over merely cheap businesses with weak economics.
- Apply Buffett-style owner earnings when reported earnings and free cash flow differ materially.
- Apply Munger-style inversion: ask what could permanently destroy the investment case, then test whether those failure modes are plausible.
- Apply Duan Yongping's lens: right business, right people, right price. Treat business model and corporate culture as primary, and price as the discipline that protects against overpaying.

## Market Routing

First classify the security and choose data sources:

| Market | Examples | Preferred data sources |
| --- | --- | --- |
| US stocks | AAPL, MSFT, NVDA, BRK.B | SEC filings, company IR, Yahoo Finance, Nasdaq, Macrotrends, Koyfin/TradingView pages, reputable financial news |
| China A-shares | 600519, 000858, 300750 | akshare, exchange filings, company announcements, financial statements, Chinese financial portals |
| HK stocks | 0700.HK, 9988.HK | HKEX filings, company IR, Yahoo Finance, exchange/company announcements |
| ADRs/global | BABA, TSM, ASML | Home-market filings, SEC ADR filings if applicable, company IR, exchange data |

If the market is ambiguous, infer from ticker format and company name. Ask one concise clarification only when ambiguity would materially change the analysis.

## Core Workflow

1. Define task type: screening, single-stock analysis, comparison, valuation, risk review, or full investment memo.
2. Gather current price, market cap, filings/financials, key ratios, segment/business context, recent news, and peer data.
3. Run the recency gate: timestamp market data, identify latest filing periods, check latest company announcements, and scan recent news before making valuation or risk claims.
4. Verify recency. Prefer latest annual report plus latest quarterly/interim report. Mention fiscal period, report date, source, and retrieval date.
5. Analyze business quality: moat, industry structure, unit economics, management/capital allocation, cyclicality, and regulation.
6. Analyze financials: revenue growth, margins, ROE/ROIC, cash conversion, free cash flow, leverage, liquidity, dilution, dividends/buybacks.
7. Apply the value-investor gate: circle of competence, business model quality, management/culture, moat durability, owner earnings, and margin of safety.
8. Analyze valuation: historical multiples, peer multiples, DCF/DDM where appropriate, owner earnings or FCF yield, and margin of safety.
9. Analyze news and events: classify each item as thesis-changing, catalyst, risk signal, sentiment/noise, or data point needing confirmation.
10. Check risks and red flags: accounting quality, debt maturity, customer concentration, governance, related-party transactions, regulatory exposure, cyclicality, and recent adverse news.
11. Produce a clear conclusion with thesis, key numbers, valuation range, watch items, and confidence level.

## References

Read only what is needed:
- `references/framework.md` for the unified value-investing checklist and scoring rubric.
- `references/investment-philosophy.md` for Buffett, Munger, and Duan Yongping principles translated into actionable analysis gates.
- `references/market-data.md` for market-specific data gathering guidance.
- `references/news-events.md` for market news, catalysts, and event triage.
- `references/report-template.md` for concise output structures.

## Output Rules

- Always separate facts, estimates, and judgment.
- Always include source dates for current market data and financial periods.
- For price-sensitive conclusions, include retrieval date/time and market status when available: open, closed, pre-market, after-hours, suspended, or holiday.
- If current price, filings, or material news cannot be verified, downgrade confidence and label the analysis as stale-data or limited-data.
- Always separate durable thesis items from short-term news flow.
- Avoid overprecision in valuation. Use ranges and key assumptions.
- For DCF/DDM, state discount rate, terminal growth, normalized FCF/dividend, and sensitivity.
- For cross-market comparisons, normalize currency, accounting standards, fiscal periods, and one-off items.
- If data is unavailable or stale, say so and continue with a clearly marked limited analysis.

