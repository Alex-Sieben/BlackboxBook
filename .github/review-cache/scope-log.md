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