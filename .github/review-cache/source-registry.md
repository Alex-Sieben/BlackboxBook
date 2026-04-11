# Source Registry

Use one row per canonical primary source that has already been fetched during review work.

## Column Guide

- `Source ID`: stable identifier used from topic files and findings.
- `URL`: canonical source URL.
- `Type`: `docs`, `blog`, `paper`, `repo`, `benchmark`, or similar.
- `Owner`: vendor, lab, or organization.
- `Topics`: comma-separated `Topic ID`s that reuse this source.
- `First seen`: first date this source entered the cache.
- `Last checked`: last date the source was explicitly re-verified.
- `Freshness class`: `static`, `slow`, `fast`, or `volatile`.
- `Status`: `current`, `stale`, `superseded`, `historical`.
- `Notes`: short note about why this source matters or what superseded it.

| Source ID | URL | Type | Owner | Topics | First seen | Last checked | Freshness class | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|