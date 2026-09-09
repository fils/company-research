# Autonomous Run — 2026-09-09

## Context
Scheduled company-research daily cron (Phases 1–5). Workdir `~/projects/company-research`. Pre-run: clean git, completeness PASS at 111 companies.

## Discovery blockers
- `web_search` / `web_extract` failed: Nous Tool Gateway not entitled/unreachable.
- Browser Use CDP unavailable.
- Fallback stack that worked: `urllib` DuckDuckGo HTML + direct homepage/TechCrunch fetches; X `search_posts_all` / `search_news`; VentureRadar Ocean funding list.

## Phase 1 — New / updated sources
| Company | Sector | Signal | URL |
|---------|--------|--------|-----|
| Bluecore Energy | Offshore Energy | $50M seed (Silverton, Sep 8 2026) + $10M pre-seed ≈ $60M; floating 10 MWe barge SMRs; Port of Long Beach; NRC+USCG | https://www.bluecore.energy/ |
| Newlight Marine | Offshore Energy | $9M seed (Sep 1 2026); H2-hybrid diesel retrofit; 24% fuel / 28% CO₂ on 8,500 nm Lomar voyage | https://www.newlightmarine.com/ |
| Coast 4C | Aquaculture | $2.5M seed (Aug 2026); regenerative smallholder seaweed + GROW + iMPAs; ZSL spinout | https://www.coast4c.com/ |
| Oshen (update) | Offshore Energy | £3.65M / ~$5M (Aug 2026, Lunar Ventures) to triple C-Star manufacturing | https://www.oshendata.com/ |

Deferred without clean homepage: Alteon ($2.5M dynamic-soaring maritime aircraft, Lachy Groom) — VentureRadar hit only.

## Phases 2–4
- Generated `raw/`, `metadata/*.jsonld`, OKF `wiki/` via `scripts/generate-profiles-2026-09-09.py`
- Updated sector pages (Offshore Energy 15→17, Aquaculture 23→24), `wiki/index.md` (111→114), `wiki/log.md`, Oshen profile

## Business model patterns surfaced
1. **Floating barge nuclear for port/AI shore-power** (Bluecore) — mobile baseload from water side; distinct from vessel propulsion and subsea geothermal
2. **H2 injection retrofit as fifth fleet decarbonization path** (Newlight) — alongside Fleetzero batteries, Kvasir biofuel, Aloft wind, Voltai motion harvest
3. **Smallholder regenerative seaweed + community iMPA stack** (Coast 4C) — livelihood/distribution layer vs genetics/biomaterials plays
4. **Ocean-robot manufacturing bottleneck** (Oshen) — sensing proven; factory throughput is the product

## Marine data needs (cross-cutting)
- Port MW demand + metocean for barge nuclear station-keeping / radiological baselines (Bluecore)
- High-frequency engine + H2 flow telemetry and bunkering maps (Newlight)
- Plot-scale SST/nutrients, ice-ice disease, regenerative MRV, iMPA ecology (Coast 4C)
- Swarm-density metocean manufacturing + constellation uplink (Oshen)

## Gates
- `python3 scripts/completeness-check.py`
- `python3 scripts/okf-lint.py`
