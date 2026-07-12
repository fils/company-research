# Autonomous Run — 2026-07-12

## Pre-run
- Working tree clean; branch master up to date with origin
- Completeness check: 0 errors, 0 warnings (74 companies)
- Last commit: 8ef1217 (Daily update 2026-07-11)

## Phase 1 — Sources
- Discovery searches across: ocean tech funding 2026, marine AI startups, aquaculture AI, mCDR investment, a16z American Dynamism portfolio
- VentureWell OEA Spring 2026 exhausted — weighted defense-tech press, TechCrunch, ESG Dive, Tracxn, CB Insights
- High-signal finds:
  1. **Saronic Technologies** — $1.75B Series D at $9.25B valuation (Mar 2026), ~$2.6B total; autonomous surface vessels for defense; Austin TX; founded 2023
  2. **Sofar Ocean** — Largest privately-owned ocean sensor network (2,500+ Spotters, 1.5M obs/day); ~$75-78.5M funding; In-Q-Tel backed; NOAA/US Navy/NVIDIA partners
  3. **Tidal** (TidalX AI) — Alphabet/X spinout (Aug 2024); AI underwater vision for aquaculture; 300+ Orca cameras with Mowi; "fishal recognition"; TIME Best Inventions 2023
- Net companies: 74 + 3 = **77**

## Phases 2–4
- Ingested homepages and press for all three new companies via web_extract + web_search
- Wrote raw/, metadata/ JSON-LD, wiki/ profiles with Data & Measurement Needs
- Updated sector pages:
  - wiki/marine-monitoring-sensors.md: count 17→18, added Saronic Technologies
  - wiki/ocean-data-ai.md: count 5→7 (SeaDeep was added in prior run but sector count not updated; added Sofar Ocean; corrected count to 7)
  - wiki/aquaculture.md: count 14→15, added Tidal

## Completeness
- ✅ COMPLETENESS CHECK PASSED — 0 errors, 0 warnings
- 77 companies across 9 sectors

## Focus themes
- **Business models**: defense prime manufacturing (Saronic), platform + data network (Sofar Ocean), hardware-enabled SaaS with strategic customer-investors (Tidal)
- **Funding**: $2.6B (Saronic, largest defense marine autonomy raise), $75-78.5M (Sofar Ocean, In-Q-Tel backed), undisclosed (Tidal, salmon industry capital)
- **Marine data needs**: 
  - Saronic: METOC feeds, sea state/wave/current data for autonomous navigation in contested environments
  - Sofar Ocean: owns the data layer (2,500+ Spotter network); gaps in deep ocean, Arctic, Southern Hemisphere subsurface
  - Tidal: pen-level underwater vision data; gaps in open-ocean baselines, ecosystem-level monitoring

## Cross-company marine data patterns
- **Saronic + HavocAI + Vatn Systems + Ulysses**: defense marine autonomy sector maturing from R&D to fleet deployment; Saronic's $2.6B dwarfs all peers
- **Sofar Ocean + Quartermaster**: both own proprietary physical sensing networks (drifters vs vessel-mounted); network-effect data moats
- **Tidal + Aquabyte + NeuralX**: aquaculture AI convergence on computer vision; Tidal's "fishal recognition" (individual fish ID) is a step beyond population-level monitoring
