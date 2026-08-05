# Autonomous Run — 2026-08-05

## Pre-run
- Working tree clean; last commit: 706308e (Daily update 2026-07-29)
- Completeness check: 0 errors, 0 warnings (97 companies)
- Date gap since last research run: ~7 days (2026-07-29 → 2026-08-05)
- 9 sectors tracked

## Phase 1 — Sources (Discovery)
- **Primary discovery**: Tech.eu / WSense funding, Ace Aquatec / SeafoodSource / company PR, CREW Carbon Series A PR, The Bridge / NYK Oceanic Constellations, The Robot Report (Blue Water NAVOCEANO), StartUs Ocean Economy Report 2026
- web_extract unavailable (Firecrawl not configured) → curl text extraction + open_page fallback
- NewMarketPitch ocean-tech deal tables JS/paywall-gated (same as 07-29)
- High-signal finds (4 new companies; all funding >> $5M priority bar or strategic industrial capital):
  1. **WSense** — >€25M total; €10M pre-Series B (Oct 2025); IoUT underwater wireless mesh → **Marine Monitoring & Sensors**
  2. **Ace Aquatec** — £10M Stolt Ventures-led (May 2025); ~$23.4M total; welfare AI cameras + humane stunners → **Aquaculture**
  3. **CREW Carbon** — $25M Series A (May 2026, Burnt Island); $33M+ CDR offtakes; WWTP alkalinity CDR → **Ocean Carbon Sequestration**
  4. **Oceanic Constellations** — ¥2B Series B1 (Jan 2026); NYK/JAFCO/Globis; Japan USV swarm constellation → **Marine Monitoring & Sensors**

### Considered but not added / deferred
- **Skana Robotics** — ~$4.3M pre-seed only; below $5M priority bar for this cycle
- **ACUA Ocean** — hydrogen USV; funding signal mixed/lower than bar
- **Blusink / Fiora Mara** — early mCDR; weaker disclosed equity than CREW
- **Nauticus Robotics** — public company + $250M facility; different research track
- Defense ASV sub-sector split still deferred (now 8+ primes + APAC constellation) — flag for structural pass

### Existing company updates
- **Blue Water Autonomy**: NAVOCEANO multi-award IDIQ, $40M ceiling (Aug 4 2026 Robot Report) — deep-ocean survey path
- **HavocAI**: already reflected $100M Series A / ~$200M total from prior profile refresh

## Phases 2–4
- Ingested via curl HTML text extract + open_page on funding PRs and company sites
- Wrote raw/, metadata/ JSON-LD, OKF wiki/ profiles with Data & Measurement Needs
- Updated sector pages (aquaculture, ocean-carbon, marine-monitoring) + index.md + log.md
- Counts: Marine Monitoring 25→27, Aquaculture 18→19, Ocean Carbon 16→17; total 97→101

## Completeness / OKF
- `python3 scripts/completeness-check.py` — target PASS (101 companies)
- `python3 scripts/okf-lint.py` — target PASS

## New business model patterns
1. **Underwater IoT fabric / multi-vendor mesh** (WSense): Sells the comms layer AUV/ASV/sensor fleets lack — multi-hop acoustic+optical mesh + cloud APIs; shipbuilder/TSO integration (Fincantieri, Terna) as GTM
2. **Welfare-first full-lifecycle aqua hardware** (Ace Aquatec): Combines AI biomass/health CV with in-water electric humane stunners + sea lice pipeline — cage-to-harvest welfare, not just monitoring
3. **In-plant wastewater alkalinity CDR** (CREW): Dual WWTP process intensification + permanent bicarbonate CDR via CaCO₃ smart-dosing; offtake-grade MRV without marine vessels — extends Pronoe-style asset-light industrial CDR
4. **USV constellation / marine satellite swarm** (Oceanic Constellations): Mass-deploy small USVs as persistent sensor+comms constellation with shipyard mass-production (NYK/Keihin); 20+ swarm patents; APAC dual-use

## Cross-company marine data patterns
- **Underwater data plane gap**: WSense addresses multi-vendor underwater networking that every AUV/USV prime and mCDR MRV stack eventually needs
- **Asset-light CDR cluster matures**: CREW (in-plant WWTP) + Pronoe (outfall OAE) + Vycarb (water CO₂) share industrial-infrastructure GTM vs ship/plant-heavy OAE
- **Global USV stack now truly multi-region**: US primes + UK Kraken + Norway Maritime Robotics + **Japan Oceanic Constellations** swarm
- **Aquaculture welfare stack densifies**: Ace Aquatec joins Biosort/Aquabyte/Tidal/NeuralX with hardware-differentiated harvest + lice path

## Discovery source quality
- **Company Series A PRs + Tech.eu**: Best for European deep-tech (WSense)
- **SeafoodSource / Ace Aquatec PR**: Clean aquaculture funding detail
- **The Bridge + NYK IR**: Best for Japan ocean-tech (Oceanic Constellations)
- **The Robot Report**: Blue Water NAVOCEANO day-of coverage
- **NewMarketPitch**: Still JS-gated; limited yield this cycle

## Commit
- Pending after final gate
