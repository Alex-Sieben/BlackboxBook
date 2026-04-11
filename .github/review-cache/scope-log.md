# Scope Log

Use one row per reviewed scope so future runs know what was already checked and which topic caches were used.

## Scope Kinds

- `full-book`: whole-manuscript audits.
- `chapter`: one chapter file.
- `section`: one section-bounded slice of a chapter.
- `cross-book-topic`: terminology, naming, or other cross-chapter review.
- `follow-up-fix`: incremental correction after a previous review.
- `structure`: rename, move, delete, or navigation repair work.

## Column Guide

- `Scope ID`: stable identifier for the reviewed slice.
- `Scope kind`: one of the kinds above.
- `Files`: affected files or chapters.
- `Topic IDs`: reusable topic caches consulted or updated.
- `Last reviewed`: date of the latest pass.
- `Review mode`: `full`, `incremental`, `research-only`, `edit-follow-up`, `structure`, or similar.
- `Cache result`: short status such as `reused`, `partial-refresh`, `new-topic`, `stale-pending`.
- `Next action`: what still needs a refresh or follow-up.
- `Notes`: concise summary of why this row exists.

| Scope ID | Scope kind | Files | Topic IDs | Last reviewed | Review mode | Cache result | Next action | Notes |
|---|---|---|---|---|---|---|---|---|
| fbr-2026-04-11 | full-book | book/00–25, readme.md | anthropic-claude-family, openai-gpt5-family, google-gemini-gemma, alibaba-qwen, deepseek-family, xai-grok, meta-llama, zhipu-glm, minimax-m27, mcp-ecosystem, slm-edge, hybrid-architectures | 2026-04-11 | full | new-topic (all 12 topics created) | Refresh fast-class topics by 2026-05-11 | First full-book review. 8 research passes, 5 fact-check passes, 4 synthesis briefs, 4 editor passes, 1 structure pass. ~64 actionable findings, ~56 resolved. Validation clean. |
| ta-muse-spark-2026-04-11 | section | book/24_ландшафт_2026.md | meta-llama | 2026-04-11 | topic-addition | partial-refresh | Revisit when Meta publishes Muse Spark architecture/benchmarks | Added Meta Muse Spark (closed multimodal LLM, MSL, April 2026) to Ch.24 text. No table entry — no quantitative data available. Source: about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/ |