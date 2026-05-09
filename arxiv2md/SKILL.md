---
name: arxiv2md
description: Convert arXiv papers to clean Markdown using the online arxiv2md REST API plus a light cleanup pass. Use when the user wants to read, fetch, convert, inspect, or summarize an arXiv paper without local pandoc, PDFs, source downloads, or a local arxiv2md CLI.
---

# arxiv2md

Convert arXiv papers to LLM-ready Markdown through the online service at `https://arxiv2md.org`. The service parses arXiv's native HTML, not PDFs. Do not install or use the local `arxiv2md` CLI for this skill.

## Standard Workflow

1. Create an output directory for the arXiv ID.
2. Call the online Markdown endpoint with:
   - `frontmatter=true`
   - `remove_refs=false`
   - `remove_citations=false`
   - `remove_toc=true`
3. Save the raw API result as `<arxiv-id>.md`.
4. Run `scripts/clean_arxiv2md_markdown.py` to produce `<arxiv-id>.cleaned.md`.
5. Return both paths and note remaining conversion artifacts.

Prefer keeping citations. `remove_citations=true` can leave awkward empty text such as `Shor , Steane , and Knill`.

## REST API

Base URL: `https://arxiv2md.org`

No auth required. Rate limit: 30 requests/minute.

### Recommended Markdown Request

```bash
curl "https://arxiv2md.org/api/markdown?url=2501.11120&frontmatter=true&remove_refs=false&remove_citations=false&remove_toc=true"
```

Returns raw Markdown as plain text.

### JSON Metadata

```bash
curl "https://arxiv2md.org/api/json?url=2501.11120"
```

Returns `{ "arxiv_id", "title", "source_url", "content" }`.

## Cleanup Script

Use the bundled cleanup script after saving API output:

```powershell
uv run python <skill-dir>\scripts\clean_arxiv2md_markdown.py .\1708.02246.md -o .\1708.02246.cleaned.md
```

When arxiv2md frontmatter mixes affiliations into the author list, pass corrected values:

```powershell
uv run python <skill-dir>\scripts\clean_arxiv2md_markdown.py .\1708.02246.md -o .\1708.02246.cleaned.md --author "Christopher Chamberland" --author "Michael E. Beverland" --affiliation "Institute for Quantum Computing and Department of Physics and Astronomy, University of Waterloo" --affiliation "Station Q Quantum Architectures and Computation Group, Microsoft Research"
```

The cleanup pass handles common arxiv2md/ar5iv artifacts:

- Removes the generated TOC, where math alt-text is often noisy.
- Fixes duplicated `Abstract` text.
- Corrects common ar5iv visual math alt-text around simple inline formulas, including duplicated variables such as `v 𝑣 v`, hyphenated variables such as `distance- d 𝑑 d`, and one-variable numeric expressions such as `d + 1 𝑑 1 d+1` or `d = 5 𝑑 5 d=5`.
- Normalizes ar5iv delimiter fragments that many KaTeX renderers reject, such as `\big{(}`, `\big{)}`, `\big{\{}`, and `\big{|}`.
- Converts `Figure: ...` plus `Refer to caption: URL` blocks into Markdown images.
- Repairs double-wrapped display math such as `$$ $\displaystyle ...$ (1) $$`.
- Tidies theorem-like headings such as `Definition 1 .`.
- Converts definition/proof markers from Markdown headings into bold paragraphs, and removes empty duplicate definition anchors emitted by ar5iv.

## Parameters

Use these query parameters for both endpoints unless noted:

| Param | Recommended | Description |
| --- | --- | --- |
| `url` | required | arXiv URL or ID, such as `2501.11120v1` or `https://arxiv.org/abs/2501.11120` |
| `remove_refs` | `false` | Keep bibliography/references section |
| `remove_toc` | `true` | Remove generated table of contents |
| `remove_citations` | `false` | Keep inline citation text |
| `frontmatter` | `true` | Prepend YAML metadata, `/api/markdown` only |

## Notes

- The online service may still emit ar5iv artifacts in figure captions, footnotes, or complex math. Preserve the raw file beside the cleaned file for comparison.
- The cleanup script intentionally handles only conservative formula artifacts. For complex formulas, inspect the cleaned Markdown against the raw file or arXiv HTML before making semantic corrections.
- If a paper has broken or missing arXiv HTML, report the API failure and do not fall back to pandoc unless the user asks.
