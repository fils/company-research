# Autonomous Run — 2026-07-29

## Pre-run
- Working tree clean; last commit: 7161b3c (OKF migration after 2026-07-16 daily)
- Completeness check: 0 errors, 0 warnings (93 companies)
- Date gap since last research run: ~13 days (2026-07-16 → 2026-07-29)
- 9 sectors tracked

## Phase 1 — Sources (Discovery)
- **Primary discovery**: The Robot Report maritime, TechCrunch climate, Climate Tech deal tables, company press, Kraken/Saildrone/Endurance/XOCEAN official sites
- web_extract unavailable (Firecrawl not configured) → curl text extraction + browser_navigate fallback
- High-signal finds (4 new companies; all funding >> $5M priority bar):
  1. **Endurance Energy** — $54M Series A (Jun 2026, Founders Fund); subsea geothermal baseload; Adélie OOI Axial Seamount pilot; Tonga partnership → **Offshore Energy**
  2. **Kraken Technology** — $175M Series B @ $1B (9 Jul 2026, DTCP); UK defence USV/USSV (K3/K4/K5); Anduril/Rheinmetall/Davie mfg; USSOCOM $49M OTA; NOT Kraken Robotics → **Marine Monitoring & Sensors**
  3. **XOCEAN** — €115M (~$118M) growth (Jan 2025); turnkey USV ocean data; Ørsted/Shell/bp; 48.6+ GW OSW → **Ocean Data & AI**
  4. **Saildrone** — >$345M total; $60M EIFO (May 2025) + $50M Lockheed (Oct 2025); Spectre ASW USV; 2.5M nm → **Marine Monitoring & Sensors**

### Considered but not added
- **EyeROV** — still deferred (inconsistent funding signal; India ROV)
- **Gigablue $20M Q2 2026** — already tracked
- **Panthalassa $140M** — already tracked
- **cAI / HavocAI $85M** — HavocAI already tracked
- Defense ASV sub-sector split still deferred (now 8+ funded primes including Kraken + Saildrone) — flag for next structural pass

## Phases 2–4
- Ingested homepages via curl HTML text extract + browser snapshots (Endurance, Kraken+funding PR, XOCEAN, Saildrone/about, TechCrunch Endurance)
- Wrote raw/, metadata/ JSON-LD, OKF wiki/ profiles with Data & Measurement Needs
- Updated sector pages + index.md + log.md
- Counts: Offshore Energy 12→13, Marine Monitoring 23→25, Ocean Data & AI 8→9; total 93→97

## Completeness / OKF
- `python3 scripts/completeness-check.py` — PASS (97 companies, 0 errors)
- `python3 scripts/okf-lint.py` — PASS (0 hard failures)

## New business model patterns
1. **Subsea geothermal baseload** (Endurance): Modular seafloor plants at ridge/volcanic heat for 24/7 power with zero surface footprint — new Offshore Energy pathway vs wind/wave/tidal/storage/vessel harvest
2. **NATO multi-nation USV manufacturing** (Kraken): Localized co-production (Rheinmetall DE, Anduril US, Davie CA) + airdrop insertion vs single-country shipyard bets
3. **Turnkey USV data + library** (XOCEAN): Fixed-price campaign + reusable data library licensing; carbon-neutral survey displacement of crewed vessels
4. **Science→defense continuum USV** (Saildrone): METOC heritage fleet monetzed as fully managed ISR/ASW with prime effector integration (Lockheed)

## Cross-company marine data patterns
- **Defense ASV/USV stack now multi-architecture**: full-size warship (Blue Water/Saronic) + high-speed modular (Kraken) + sail-endurance ISR/ASW (Saildrone) + swarm C2 (HavocAI) + micro (Seasats/Clear)
- **Offshore baseload thesis expands**: Endurance subsea geothermal joins Sizable LDES and Panthalassa wave-compute as non-intermittent ocean energy plays pulling hard on seafloor heat flux, cabled observatories (OOI), and benthic MRV
- **Ocean data delivery stratification**: Sofar (drifter weather network) vs XOCEAN (geophysical survey USV campaigns+library) vs Saildrone (managed long-endurance METOC/ISR) vs Ubotica (orbital edge AI)
- **Prime partnerships as maturation signal**: Lockheed→Saildrone, Anduril→Kraken, Rheinmetall→Kraken — defense primes integrating startup USV fleets

## Discovery source quality
- **The Robot Report**: Highest yield this cycle (Kraken Series B day-of coverage)
- **TechCrunch Climate**: Endurance Series A detail (Founders Fund, SpaceX alumni thesis)
- **Company sites**: Best for platform specs and partner lists when Firecrawl unavailable
- **NewMarketPitch**: JS/Shopify paywall-heavy; skipped deep table harvest this run

## Commit
- Pending after final gate
