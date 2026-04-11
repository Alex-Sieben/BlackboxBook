# Topic Cache Template

Copy this file to `topics/<topic-id>.md` and replace the placeholders.

- Topic ID: `<topic-id>`
- Scope: `<vendor, model family, benchmark, architecture theme, or claim cluster>`
- Applies to chapters: `<book/file.md, ...>`
- Status: `current` | `partial` | `stale` | `superseded`
- Freshness class: `static` | `slow` | `fast` | `volatile`
- Last verified: `YYYY-MM-DD`
- Next scheduled review: `YYYY-MM-DD` or `manual`
- Refresh triggers: `<new vendor release, docs rename, benchmark refresh, user asked for latest state>`
- Watch source IDs: `<source-id-1>, <source-id-2>`
- Canonical source IDs: `<source-id-1>, <source-id-2>`

## Cached conclusions

- `<short, reusable factual conclusion>`

## Known unknowns

- `<facts that still cannot be supported from primary sources>`

## Refresh workflow

- Re-check watch sources first.
- If they are unchanged and the current conclusions still cover the manuscript claims, refresh only the dates and status fields.
- Add new source rows only when a watch source points to a new canonical document or the manuscript scope outgrows the current cache.

## Manuscript deltas enabled by this cache

- `<chapter or wording changes this cache can support>`