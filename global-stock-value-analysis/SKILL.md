---
name: global-stock-value-analysis
description: Research and value listed equities across US, China A-share, HK, and global markets. Use for stock analysis, screening, comparison, valuation, or company news and risks that affect an investment thesis.
---

# Global Stock Value Analysis

Analyze stocks as long-term ownership of businesses. Prioritize durable earning power, cash generation, capital allocation, valuation, margin of safety, and permanent impairment risk. Use news when it changes these judgments.

## Scope And Completion

Infer the security, market, language, and research depth from the request and conversation. For a broad single-stock request, produce a Quick Stock Note. Ask only when unresolved ambiguity would materially change the security or the answer; otherwise state a reasonable assumption and continue. Honor the user's requested format and length over the defaults below.

Complete the requested research and give a supported conclusion, key uncertainties, and what would change the view. Missing optional data should lower confidence in the affected claim, not stop the whole report. Research does not authorize placing trades or changing accounts.

## Task And Reference Routing

Read only the references relevant to the task; reuse material already in context. The checklists guide analysis, not a mandatory sequence of tool calls.

| Task | Default output | Read when needed |
| --- | --- | --- |
| Broad single-stock analysis / 分析X、怎么看X | Quick Stock Note | [Report templates](references/report-template.md); [framework](references/framework.md) for deeper business or financial analysis |
| Deep dive / 完整报告、深度分析 | Full Investment Memo | Report templates, framework, and [investment philosophy](references/investment-philosophy.md) |
| Fair value / 估值、值不值得买 | Valuation-Focused Note | Report templates and the framework's valuation guidance |
| Company news, earnings, catalysts / 最近发生什么 | News-Aware Value Memo | Report templates and [news and events](references/news-events.md) |
| Downside, accounting, governance / 风险、暴雷 | Risk Review | Report templates; framework or news guidance for the risks at issue |
| Peer comparison / 对比 | Comparison Output | Report templates; framework for comparable metrics or requested scoring |
| Screening / 筛选 | Screening Output | Report templates and framework; state the universe and filters |
| A focused follow-up, one metric, or a requested short answer | Direct answer | Only the reference needed to answer that question; do not restart a full report |

For current price, filings, valuation history, or cross-market data, use [market data](references/market-data.md). For owner earnings, moat durability, incentives, or an explicit Buffett/Munger/Duan view, use [investment philosophy](references/investment-philosophy.md). Combine relevant analysis for mixed requests without duplicating whole reports.

## Research And Evidence

Use filings and company, exchange, or regulator releases for material business facts; use reliable market-data sources for prices. Verify the quote timestamp, currency, latest available financial period and publication date, and subsequent material announcements before making a current valuation or investment judgment. Record retrieval time and timezone for price-sensitive answers. For historical as-of research, respect the information available at that date.

Collect evidence that can change the requested conclusion. Retrieve independent facts together when tools permit, reconcile material conflicts, and calculate valuation outputs from identified inputs. Do not turn every checklist item into a separate search. If a source is blocked or incomplete, try an appropriate alternative; stop when further retrieval is unlikely to change the answer, and disclose remaining gaps. Never substitute remembered prices or invented ratios for unavailable data.

## Investment Judgment

For a company investment view, connect the relevant Buffett/Munger/Duan gates to evidence: circle of competence, durable business economics and moat, management integrity and culture, owner earnings or cash generation, inversion risk, and right price with margin of safety. These are analytical lenses, not quotations or endorsements by those investors. Mark a business as "too hard" when the evidence cannot support an informed valuation.

Choose valuation methods that fit the business and data. Use normalized earnings for cyclical or one-off-heavy results; distinguish reported figures, management adjustments, and analyst estimates. When P/E is meaningful, use a defensible 5-, 10-, or 20-year percentile horizon and explain the choice. Show the earnings basis and any material one-off adjustments. If comparable history is unavailable, say so and use another supported valuation anchor. Detailed method and horizon rules are in the framework and market-data references.

Support fair value ranges with assumptions and downside cases. For DCF/DDM, show normalized cash flow or dividends, discount rate, terminal assumptions, and sensitivity; reconcile enterprise value to equity value and the relevant share count when applicable. Normalize currencies, reporting periods, accounting bases, share classes, and ADR ratios for cross-market comparisons. A low historical multiple alone is not a margin of safety.

## Deliver The Answer

Lead with the answer in the user's language. Use the report templates for substantive reports and retain their material coverage; a narrow follow-up can be a paragraph or small table. Keep facts, calculations/estimates, and judgment distinguishable. Link evidence beside material claims and label dates, units, and financial periods.

Before finishing, check the numbers and assumptions that drive the conclusion, material counterevidence, data freshness, and unresolved limitations. Match verification to those risks. If critical data cannot be verified, give a clearly limited assessment and explain which conclusion remains unsupported; do not manufacture a precise fair value, percentile, or confident buy/sell view.
