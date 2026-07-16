# Company Research Knowledge Graph

## About

Agent-managed repo for researching business models of companies in ocean carbon sequestration, climate risk, bioprospecting, aquaculture, and offshore energy sectors. Builds a personal knowledge graph (wiki) from sources, extracts funding, models, contacts, etc.

**Document format:** `wiki/` is an [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) Knowledge Bundle. Local rules: [`wiki/concepts/okf-knowledge-bundle.md`](wiki/concepts/okf-knowledge-bundle.md). Conformance: `python3 scripts/okf-lint.py`.

**Critical Note on URLs**: Every company entry in `sources/companies.json` contains an official homepage URL. Future workflow runs (Phases 2–4) must explicitly propagate this URL into:
- The first header of every `raw/*.md` file
- The `"url"` field in every `metadata/*.jsonld` file
- The OKF `resource` frontmatter field and a clear **Official Site** line near the top of every wiki company profile

## Components

### sources/
JSON index of company sources (websites, APIs). Every record includes `url` (required).

### raw/
Scraped MD/HTML/JSON from web_extract/browser. **Each file now requires the source URL in the header**. Free-form notes allowed; do not copy non-OKF markup into `wiki/`.

### wiki/
OKF v0.1 Knowledge Bundle — LLM-compiled `.md` concepts (companies, sectors). Entry point: [`wiki/index.md`](wiki/index.md). Every concept has YAML frontmatter with required `type`. Cross-links use relative markdown only.

### metadata/
JSON-LD schema.org Dataset/DigitalObject for resources. **Must contain the company’s official URL**.

### scripts/
- `okf-lint.py` — daily OKF conformance gate (required after wiki writes)
- `convert-to-okf.py` — one-shot / re-run OKF migrator
- `completeness-check.py` — domain completeness (companies.json ↔ files)

### PLAN.md
Daily workflow with OKF format contract and URL handling instructions.

## Workflow

Nightly cron runs Phases 1–5. All changes via branches/PRs to master.

**Last major revision**: 2026-07-16 (OKF v0.1 migration of `wiki/`)
