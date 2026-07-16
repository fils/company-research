# Scripts

## `okf-lint.py` (daily gate)

OKF v0.1 conformance check for `wiki/`.

```bash
python3 scripts/okf-lint.py
python3 scripts/okf-lint.py --strict   # soft issues also fail
```

Hard-fails on: missing/unparseable frontmatter, missing `type`, residual `[[wikilinks]]` outside code.

Soft-checks: broken relative links, missing title/description, absolute `/...` links.

**Agents must run this after every wiki write day.** See `PLAN.md` Document format section.

## `convert-to-okf.py` (one-shot / re-run migrator)

Migrates concept pages to OKF: frontmatter, link normalization, indexes, local format concept.

```bash
python3 scripts/convert-to-okf.py --dry-run
python3 scripts/convert-to-okf.py
```

## `completeness-check.py` (domain gate)

Company-to-file cross-reference, sector counts, Data & Measurement Needs presence, etc. Complements OKF lint; does not replace it.

## Other dated generators

`generate-profiles*.py`, `daily-update-*.py` are one-off helpers. Prefer the Phase 1–5 loop in `PLAN.md` for ongoing work. Any page they write into `wiki/` must still satisfy OKF (`type` frontmatter + relative markdown links) and pass `okf-lint.py`.
