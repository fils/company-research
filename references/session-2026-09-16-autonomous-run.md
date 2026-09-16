# Autonomous Run — 2026-09-16

## Context
Scheduled company-research daily cron (Phases 1–5). Workdir `~/projects/company-research`.
Pre-run: clean git, completeness PASS at 114 companies (last commit 1d683c3, 2026-09-09).

## Discovery blockers
- `web_search` / `web_extract`: Nous Tool Gateway not entitled/unreachable (same as 2026-09-09).
- Fallback: urllib DuckDuckGo HTML + The Fish Site article crawl + official homepages + X `search_news` / `search_posts_all`.
- DDG rate-limited after first queries; Fish Site startups feed was highest-yield source this run.

## Phase 1 — New sources
| Company | Sector | Signal | URL |
|---------|--------|--------|-----|
| WellFish Tech | Aquaculture | Oversubscribed interim financing (27 Aug 2026); WellFish Predict 28-day mortality from blood biomarkers; Series A planned 2027 | https://wellfishtech.com/ |
| WildTechDNA | Aquaculture | ORYA multi-pathogen ~15-min handheld DNA kit for salmon/shrimp (14 Sep 2026 launch); isothermal instrument-free | https://wildtechdna.com/ |
| Esox Biologics | Aquaculture | Detect metagenomics platform; first whole genome of sabellid worm for abalone water-based early warning (Sep 2026) | https://esoxbiologics.com/ |

### Already tracked (confirmed, no re-add)
- Oceanloop up to €38.5M (Hatch Blue, Stolt, EIB) — already in graph
- Nernst Electric Hatch Blue oxygen seed — already in graph
- AquaNab Nordic Foodtech VC — already in graph
- Kraken Technology $175M Series B unicorn — already in graph (Jul 2026 profile)

### Deferred
- Poseidon Aerospace $60M Series A autonomous cargo aircraft (seaplane variant mentioned) — aerospace logistics primary, weak marine-data fit
- Kelpi seaweed packaging FDA — materials/packaging edge case, lower MRV signal this cycle
- Entosystem insect protein carbon credits — aquafeed-adjacent only

## Phases 2–4
- Generated `raw/`, `metadata/*.jsonld`, OKF `wiki/` via `scripts/generate-profiles-2026-09-16.py`
- Updated `wiki/aquaculture.md` (24→27), `wiki/index.md` (114→117), `wiki/log.md`

## Business model / data patterns
1. **Host physiology biomarkers as production OS** (WellFish) — internal clinical chemistry + 28-day mortality forecast
2. **Point-of-care multi-pathogen DNA** (WildTechDNA ORYA) — speed/breadth/simplicity field kits
3. **Full-community metagenomic Detect + parasite genome moat** (Esox) — sabellid first genome; RAS/mollusc early warning
4. Layered biosecurity stack with existing Nucleic Sensing Systems eDNA hardware

## Marine data needs (cross-cutting)
- Longitudinal biomarker ↔ env/telemetry fusion (WellFish)
- On-site pathogen panel results + outbreak network sharing (WildTechDNA)
- Metagenome time series + water chemistry covariates + biofilter state (Esox)
- Interoperability across physiology / rapid PCR / metagenome / continuous eDNA layers

## Gates
- `python3 scripts/completeness-check.py`
- `python3 scripts/okf-lint.py`
