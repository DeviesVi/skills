---
name: global-stock-value-analysis
description: Research business operations and value listed equities across US, China A-share, HK, and global markets using public evidence. Use for stock analysis, operating due diligence, screening, comparison, valuation, and thesis-relevant company news or risks.
---

# Global Stock Value Analysis

Analyze stocks as long-term ownership of businesses. Understand how the company wins customers, delivers products, earns money, and reinvests before valuing its securities. Connect operating evidence to durable earning power, cash generation, capital allocation, valuation, margin of safety, and permanent impairment risk.

## Scope And Completion

Infer the security, market, language, and research depth from the request and conversation. For a broad single-stock request, investigate the underlying operations and produce a Stock Note. A concise answer is a presentation choice, not permission to skip material research. Ask only when unresolved ambiguity would materially change the security or the answer; otherwise state a reasonable assumption and continue. Honor the user's requested scope and length; a narrow follow-up should stay focused.

Complete the requested research and give a supported conclusion, key uncertainties, and what would change the view. Missing optional data should lower confidence in the affected claim, not stop the whole report. Research does not authorize placing trades or changing accounts.

## Task And Reference Routing

Read only the references relevant to the task; reuse material already in context. The checklists guide analysis, not a mandatory sequence of tool calls.

| Task | Default output | Read when needed |
| --- | --- | --- |
| Broad single-stock analysis / 分析X、怎么看X | Stock Note | [Operating research](references/operating-research.md), [report templates](references/report-template.md), and relevant [framework](references/framework.md) checks |
| Deep dive / 完整报告、深度分析 | Full Investment Memo | Operating research, report templates, framework, and [investment philosophy](references/investment-philosophy.md) |
| Operating due diligence / 经营调研、产线、客户、供应链、竞争优势 | Operating Research Memo or focused answer | Operating research and report templates; research the mechanisms relevant to the question |
| Fair value or feasibility / 估值、值不值得买、能达到吗 | Valuation-Focused Note or focused answer | Framework's valuation guidance and operating research to test material forecast assumptions; reuse evidence already verified |
| Company news, earnings, catalysts / 最近发生什么 | News-Aware Value Memo | Report templates and [news and events](references/news-events.md) |
| Downside, accounting, governance / 风险、暴雷 | Risk Review | Report templates; framework or news guidance for the risks at issue |
| Peer comparison / 对比 | Comparison Output | Report templates; operating research for business differences and framework for comparable metrics |
| Screening / 筛选 | Screening Output | Report templates and framework; state the universe and filters |
| A focused follow-up, one metric, or a requested short answer | Direct answer | Only the reference needed to answer that question; do not restart a full report |

For current price, filings, valuation history, or cross-market data, use [market data](references/market-data.md). For owner earnings, moat durability, incentives, or an explicit Buffett/Munger/Duan view, use [investment philosophy](references/investment-philosophy.md). Combine relevant analysis for mixed requests without duplicating whole reports.

## Research And Evidence

For substantive company analysis, use the [operating research workflow](references/operating-research.md). Financial statements are one evidence stream. Investigate the material operating questions through accessible public information from the company and its products, customers, suppliers, competitors, industry bodies, regulators, and project records as relevant. Seek broad coverage and depth on the drivers that can change the conclusion; do not stop after finding a financial summary, management presentation, or a convenient source count.

Use filings and company, exchange, or regulator releases for material business facts; use reliable market-data sources for prices. Verify the quote timestamp, currency, latest available financial period and publication date, and subsequent material announcements before making a current valuation or investment judgment. Record retrieval time and timezone for price-sensitive answers. For historical as-of research, respect the information available at that date.

Trace decision-critical claims to their original source, test management claims against independent operating evidence where available, and distinguish repeated coverage of one announcement from corroboration. Record entity/project scope, dates, units, and whether a statement is an observed result, guidance, third-party estimate, or analytical assumption. Search explicitly for counterevidence and later changes to plans.

Retrieve independent facts together when tools permit, reconcile material conflicts, and calculate valuation outputs from identified inputs. Explore relevant alternative source types before declaring a material operating input unavailable. Finish when the key questions have evidence or clearly bounded gaps and further retrieval is unlikely to change the conclusion. Disclose material access limits and unresolved questions without claiming exhaustive coverage. Never substitute remembered prices, invented ratios, or arbitrary operating forecasts for unavailable data.

## Investment Judgment

For a company investment view, connect the relevant Buffett/Munger/Duan gates to evidence: circle of competence, durable business economics and moat, management integrity and culture, owner earnings or cash generation, inversion risk, and right price with margin of safety. These are analytical lenses, not quotations or endorsements by those investors. Mark a business as "too hard" when the evidence cannot support an informed valuation.

Choose valuation methods that fit the business and data. Use normalized earnings for cyclical or one-off-heavy results; distinguish reported figures, management adjustments, and analyst estimates. When P/E is meaningful, use a defensible 5-, 10-, or 20-year percentile horizon and explain the choice. Show the earnings basis and any material one-off adjustments. If comparable history is unavailable, say so and use another supported valuation anchor. Detailed method and horizon rules are in the framework and market-data references.

Support fair value ranges with assumptions and downside cases. For DCF/DDM, show normalized cash flow or dividends, discount rate, terminal assumptions, and sensitivity; reconcile enterprise value to equity value and the relevant share count when applicable. Normalize currencies, reporting periods, accounting bases, share classes, and ADR ratios for cross-market comparisons. A low historical multiple alone is not a margin of safety.

Build material forecasts from operating drivers and show the bridge into earnings and shareholder cash flow. Conditional valuation tables and reverse valuations identify requirements; they do not establish that those requirements are achievable. When asked whether a scenario can happen, investigate the required demand, capacity, pricing, costs, reinvestment, and cash ownership before judging feasibility. Separate a one-year result from a sustainable level and avoid assigning probabilities or a base case without supporting evidence.

## Deliver The Answer

Lead with the answer in the user's language. Use the report templates for substantive reports and retain their material coverage; a narrow follow-up can be a paragraph or small table. Explain the operating mechanism behind the conclusion, the strongest supporting and opposing evidence, and how they affect financial expectations. Keep facts, calculations/estimates, and judgment distinguishable. Link evidence beside material claims and label dates, units, and financial periods.

Before finishing, check the numbers and assumptions that drive the conclusion, material counterevidence, data freshness, and unresolved limitations. Match verification to those risks. If critical data cannot be verified, give a clearly limited assessment and explain which conclusion remains unsupported; do not manufacture a precise fair value, percentile, or confident buy/sell view.
