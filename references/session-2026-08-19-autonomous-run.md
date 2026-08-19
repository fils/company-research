# Session 2026-08-19 — Autonomous Daily Company Research Run

**Date:** 2026-08-19 (cron)
**Workdir:** `~/projects/company-research`
**Prior state:** 101 companies (commit c015732, 2026-08-05); completeness clean

## Pre-run
- `git status`: clean except untracked `scripts/generate-profiles-2026-08-12.py`
- Completeness check: PASS (101/101)

## Phase 1 — Discovery
Sources consulted:
- Unmanned Systems Technology (BeeX $7.7M Series A Aug 2026 coverage)
- EU-Startups (Oceanloop up to €38.5M Aug 18 2026; Nernst Electric €1.7M Jul 2026)
- Omnes / SpaceNews (Unseenlabs €85M Series C / ~€120M total)
- Arctic Startup / TechCrunch (Spoor €8M Series A)
- Carbon Herald ocean CDR page (no new high-signal pure-play mCDR companies vs existing graph)
- Homepage extracts: beex.sg, unseenlabs.com, oceanloop.com, spoor.ai, nernstelectric.com

**Added (5):**
| Company | Sector | Signal |
|---------|--------|--------|
| BeeX | Marine Monitoring & Sensors | $7.7M Series A; Singapore AUV dual-use |
| Unseenlabs | Ocean Data & AI | €85M C / ~€120M; RF dark vessels |
| Oceanloop | Aquaculture | ≤€38.5M; Hatch Blue + Stolt + EIB |
| Spoor | Offshore Energy | €8M A; AI bird/bat wind monitoring |
| Nernst Electric | Aquaculture | €1.7M Hatch Blue Seed; OTM O2 |

## Phases 2–4
- Generated `raw/`, `metadata/`, `wiki/` for all 5 via `scripts/generate-profiles-2026-08-19.py`
- Updated sector pages + `wiki/index.md` + `wiki/log.md`
- Completeness + OKF lint gates

## Sector deltas
- Marine Monitoring: 27→28
- Aquaculture: 19→21
- Ocean Data & AI: 9→10
- Offshore Energy: 13→14
- **Total: 101→106**

## Marine data patterns (new)
1. Industrial dual-use AUV inspection (BeeX) — APAC WROV displacement
2. Space RF dark-vessel GEOINT (Unseenlabs) complements optical edge AI (Ubotica)
3. Industrial land-based marine RAS + Co-Pilot (Oceanloop)
4. Biodiversity compliance layer for wind (Spoor)
5. On-site oxygen infrastructure for remote farms (Nernst)

## Phase 5
- Commit + push; Discord report via cron auto-delivery
