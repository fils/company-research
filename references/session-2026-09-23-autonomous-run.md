# Autonomous Run — 2026-09-23

## Context
Scheduled company-research daily cron (Phases 1–5). Workdir `~/projects/company-research`.
Pre-run: clean git, completeness PASS at 117 companies (last commit a512fea, 2026-09-16).

## Discovery blockers
- `web_search` / `web_extract`: Nous Tool Gateway not entitled/unreachable (same as 2026-09-09/16).
- DDG HTML returned 0 result links this cycle.
- Fallback: urllib Fish Site + NewMarketPitch climate/ocean funding pages + Maritime Executive + Bing/Google News RSS + X `search_news` / `search_posts_all` + official homepages.

## Phase 1 — New sources
| Company | Sector | Signal | URL |
|---------|--------|--------|-----|
| ARK Inc | Aquaculture | ~$8.5M / ¥1.3B Series A (17 Sep 2026); modular closed RAS; Global South UAE/Indonesia; UntroD/Beyond Next/BP Capital + bank loans | https://www.ark.inc/en/ |
| Bulwark Dynamics | Marine Monitoring & Sensors | $6.8M seed (Sep 2026) + Onomichi Dockyard; CARAVEL autonomous beach-landing resupply USV | https://bulwarkdynamics.com/ |
| Marcura | Maritime Operations & Analytics | Scaled voyage/vessel/crew OS + AI; ShipServ/DA-Desk network; CEO Henrik Hyldahn | https://marcura.com/ |
| HydroSurv | Marine Monitoring & Sensors | UK REAV survey USVs; OWGP USV-first 3D SBP w/ GeoAcoustics; Hike Metal NA license | https://www.hydro-surv.com/ |

### Already tracked / noted
- Saildrone Danish flag registration for Voyager USVs (Sep 2026) — existing profile
- Seasats order traction — already tracked
- WellFish / WildTechDNA / Esox — prior week
- Entosystem insect carbon credits — aquafeed-adjacent, deferred again
- OoMee/Aqua Theon seaweed beverage — consumer CPG edge, lower MRV signal
- Marine Donut / Bluegreen — paywalled IntraFish; homepage refused connection this cycle

### Deferred
- Albatross Technology floating VAWT (~$2.6M) — homepage unresolved this cycle
- Manolin aquaculture AI — official site unresolved / 404s
- Kelpi seaweed coating commercial milestone — materials packaging edge

## Phases 2–4
- Generated `raw/`, `metadata/*.jsonld`, OKF `wiki/` via `scripts/generate-profiles-2026-09-23.py`
- Updated `wiki/aquaculture.md` (27→28), `wiki/marine-monitoring-sensors.md` (28→30), `wiki/maritime-operations-analytics.md` (8→9), `wiki/index.md` (117→121), `wiki/log.md`

## Business model / data patterns
1. **Modular RAS export for Global South** (ARK) — harsh-climate closed RAS + grouper specialty + METI/policy GTM
2. **Autonomous beach-landing logistics USV** (Bulwark) — landing-craft cargo niche vs patrol/survey USVs; allied shipyard co-production
3. **Transaction-network voyage OS** (Marcura) — port-call/procurement/claims data moat orthogonal to onboard CV
4. **Commercial survey USV + USV-first 3D SBP** (HydroSurv) — OSW foundation/cable geophysics via REAV + GeoAcoustics

## Marine data needs (cross-cutting)
- RAS multi-parameter water chemistry + biofilter state (ARK)
- Littoral bathymetry, beachability, GPS-denied nav (Bulwark)
- Port-call cost lines, charterparty corpora, AIS vs plan (Marcura)
- MBES + volumetric shallow sub-bottom + landfall survey (HydroSurv)
- Shared USV autonomy stack needs across defense logistics and commercial survey

## Gates
- `python3 scripts/completeness-check.py`
- `python3 scripts/okf-lint.py`
