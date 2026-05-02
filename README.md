# Company Research Knowledge Graph

## About
Agent-managed repo for researching business models of companies in ocean carbon sequestration, climate risk, bioprospecting, aquaculture, and offshore energy sectors. Builds a personal knowledge graph (wiki) from sources, extracts funding, models, contacts, etc.

**Critical Note on URLs**: Every company entry in `sources/companies.json` contains an official homepage URL. Future workflow runs (Phases 2–4) must explicitly propagate this URL into:
- The first header of every `raw/*.md` file
- The `"url"` field in every `metadata/*.jsonld` file
- A clear **Official Site** line near the top of every wiki company profile

## Components

### sources/
JSON index of company sources (websites, APIs). Every record includes `url` (required).

### raw/
Scraped MD/HTML/JSON from web_extract/browser. **Each file now requires the source URL in the header**.

### wiki/
LLM-compiled `.md` articles on companies/sectors. **Every company profile must include the official homepage URL** near the top.

### metadata/
JSON-LD schema.org Dataset/DigitalObject for resources. **Must contain the company’s official URL**.

### PLAN.md
Daily workflow with explicit URL handling instructions.

## Workflow
Nightly cron runs Phases 1-5. All changes via branches/PRs to master.

**Last major revision**: 2026-05-01 (URL enforcement added to PLAN.md + templates)