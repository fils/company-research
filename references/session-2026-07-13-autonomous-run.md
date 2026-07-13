# Autonomous Run — 2026-07-13

## Pre-run
- Working tree clean; last commit: 5f12dea (Daily update 2026-07-12)
- Completeness check: 0 errors, 0 warnings (77 companies)
- Sectors: Aquaculture 15, Bioprospecting 1, Climate Risk 5, Coastal Risk 3, Marine Monitoring 18, Maritime Ops 4, Ocean Carbon 16, Ocean Data & AI 7, Offshore Energy 8

## Phase 1 — Sources
- Discovery searches across: ocean AI startups, blue economy AI, maritime AI, NOAA/Copernicus AI partnerships, mCDR funding, a16z American Dynamism portfolio
- VentureWell OEA Spring 2026 exhausted — weighted defense-tech press, TechCrunch, ESG Dive, Carbon Herald, Tracxn, Dealroom
- High-signal finds:
  1. **Orca AI** — $72.5M Series B (May 2025, Brighton Park Capital lead); total $111M; AI computer vision for maritime navigation safety + collision avoidance; 1,500+ vessels deployed; world's largest marine visual dataset (80M+ nm); Tel Aviv, Israel; founded 2018; Samsung Heavy Industries partnership (Apr 2026); Lloyd's Register assessment (Apr 2026); $100K fuel savings/vessel/yr
  2. **Sea Machines Robotics** — ~$42M total funding; autonomous control & navigation systems for commercial + defense vessels; 200+ deliveries worldwide; US Navy MASC program; GPS-denied operations; Boston MA; DRS Counter-UAS partnership (Apr 2026); Shintoa Japan expansion (Apr 2026); record year of bookings 2026
- Funding updates for existing companies:
  3. **Captura** — $12.5M Series B (Jun 2026, Equinor Ventures lead); total now ~$57.5M; expanding Pasadena manufacturing; first lithium extraction market orders; CEO Steve Oldham
  4. **Vycarb** — Detailed $5M seed (Oct 2025, Twynam lead; Shell, Hatch Blue, Singapore govt); Tomco Systems + atdepth partnerships; industrial gas integration; East River NYC pilot 1+ yr; founded 2022 by Garrett Boudinot
- Net companies: 77 + 2 = **79**

## Phases 2–4
- Ingested homepages and press for Orca AI and Sea Machines via web_extract
- Wrote raw/, metadata/ JSON-LD, wiki/ profiles with Data & Measurement Needs
- Updated sector pages:
  - wiki/maritime-operations-analytics.md: count 4→6, added Orca AI + Sea Machines Robotics, expanded cross-company patterns (marine computer vision moat, autonomous shipping infrastructure, GPS-denied operations, voyage optimization ROI)
- Updated existing profiles:
  - wiki/captura.md: Series B $12.5M, total ~$57.5M, Equinor Ventures lead, Pasadena manufacturing, lithium extraction expansion
  - wiki/vycarb.md: $5M seed details (Twynam, Shell, Hatch Blue, Singapore govt), Tomco + atdepth partnerships, industrial gas integration, East River pilot 1+ yr

## Completeness
- ✅ COMPLETENESS CHECK PASSED — 0 errors, 0 warnings
- 79 companies across 9 sectors

## Focus themes
- **Business models**: SaaS + hardware (Orca AI), dual-use hardware + software (Sea Machines), industrial CO2 integration (Vycarb-Tomco)
- **Funding**: $111M (Orca AI, largest maritime AI raise), ~$42M (Sea Machines, dual-use autonomy), $12.5M Series B (Captura, Equinor-led), $5M seed (Vycarb, Shell-backed)
- **Marine data needs**:
  - Orca AI: world's largest marine visual dataset (80M+ nm); needs AIS augmentation, weather routing, ocean current data for voyage optimization
  - Sea Machines: GPS-denied navigation requiring alternative nav sources (inertial, visual); needs hydrographic charts, satellite comms for BLOS USV control
  - Captura: real-time seawater chemistry (pH, DIC, alkalinity), MRV verification, ecosystem monitoring at discharge points
  - Vycarb: real-time carbonate chemistry, CO2 flux, independent MRV via atdepth ocean monitoring

## Cross-company marine data patterns
- **Orca AI + Sea Machines**: marine computer vision as network-effect data moat; proprietary visual datasets create barriers to entry; more vessels = more data = better models
- **Orca AI + Sea Machines + Quartermaster + Sofar Ocean**: autonomous maritime infrastructure convergence — navigation, sensing, and data networks maturing simultaneously
- **Captura + Vycarb + Ebb Carbon + Equatic**: ocean CDR companies entering commercial execution phase, all with intensive MRV carbonate chemistry data needs
- **Vycarb + atdepth partnership**: model for independent third-party MRV verification — MIT spinout ocean monitoring company validates CDR impact; pattern may spread across mCDR sector
