# Autonomous Run — 2026-07-15

## Pre-run
- Working tree clean; last commit: f0e64e1 (Daily update 2026-07-14)
- Completeness check: 0 errors, 0 warnings (83 companies)
- 9 sectors tracked

## Phase 1 — Sources (Discovery)
- Discovery source: **NewMarketPitch.com Ocean Tech Funding Analysis (2026)** — comprehensive tracker of 23 disclosed ocean tech equity rounds Aug 2025–Jul 2026, $2.40B raised across 22 unique companies. This proved to be the richest single discovery source for this run.
- Additional searches: ocean tech startup funding 2026, ocean carbon removal funding 2026, aquaculture AI startup 2026, marine autonomous vehicle 2026, blue economy startup 2026, therobotreport.com maritime funding, ocean CDR alkalinity enhancement 2026
- High-signal finds (5 new companies):
  1. **Fleetzero** — $43M Series A (Jan 2026, Obvious Ventures + Maersk Growth + Breakthrough Energy Ventures + 8090 Ventures); marine energy & robotics — Leviathan modular marine battery systems (3.8 MWh per container, 25% footprint, double power/half price) + hybrid/electric propulsion + modular hull construction; AET partnership for world's longest-range hybrid-electric vessel; YC alumni; Houston TX; US Navy veterans team; price parity with fossil fuels (no green premium)
  2. **Hullbot** — $10.5M Series A (Nov 2025, Katapult Ocean lead); autonomous underwater robots for ship hull cleaning & inspection (proactive hull grooming); cloud robotics platform; works with all coatings; routine inspections without divers; UNSW-backed; Sydney, Australia; customers include Ultramar, NRMA Marine, FRS Clipper, Journey Beyond; as-a-service model (no upfront cost)
  3. **Ubotica** — $11M funding (Jun 2026); orbital AI / cognitive Earth observation for real-time maritime intelligence from space; SPACE:AI platform (11 missions flown, 30+ AI models); subscription-based predictive maritime surveillance (dark vessels, shadow fleets); Fugro partnership for space-to-seabed intelligence; NASA JPL collaboration (FAME autonomous satellite network); ESA partner; Dublin, Ireland
  4. **Kvasir Technologies** — €10M Series A (Jun 2026); climate-neutral drop-in marine biofuel from lignocellulosic biomass waste; DTU spinout; >96% GHG reduction; no engine modification needed; meets IMO 2030/2050 targets; Maersk as strategic investor-customer; Copenhagen, Denmark
  5. **AquaExchange** — $8M Series B (Mar 2026, NABVENTURES lead); full-stack IoT/AI platform for shrimp aquaculture; 20K devices, 80K acres, 4 countries; products include WaterMon (GPS water quality), Patholense (AI microscopy pathogen detection), FeedMon (acoustic demand-based feeding), AquaBot (automated feeding), NextFarm app; embedded finance + disease insurance + marketplace; Vijayawada, India; founded 2020
- Sector placement decisions:
  - Fleetzero → Offshore Energy (marine electrification/battery systems)
  - Hullbot → Marine Monitoring & Sensors (autonomous underwater robots for inspection)
  - Ubotica → Ocean Data & AI (satellite maritime AI intelligence — extends sector to space domain)
  - Kvasir Technologies → Offshore Energy (marine fuel decarbonization)
  - AquaExchange → Aquaculture (IoT/AI for shrimp farming)
- Net companies: 83 + 5 = **88**

## Phases 2–4
- Ingested homepages via web_extract for all 5 companies
- Wrote raw/, metadata/ JSON-LD, wiki/ profiles with Data & Measurement Needs sections
- Updated sector wiki pages:
  - wiki/offshore-energy.md: count 8→10, added Fleetzero + Kvasir Technologies entries with key insights
  - wiki/marine-monitoring-sensors.md: count 20→21, added Hullbot entry
  - wiki/ocean-data-ai.md: count 7→8, added Ubotica entry
  - wiki/aquaculture.md: count 16→17, added AquaExchange entry + 1 new cross-company pattern (full-stack IoT ecosystem)
- All wiki profiles include standardized Data & Measurement Needs sections

## Completeness
- ✅ COMPLETENESS CHECK PASSED — 0 errors, 0 warnings — 88 companies
- Sector breakdown: Aquaculture 17, Bioprospecting 1, Climate Risk 5, Coastal Risk 3, Marine Monitoring 21, Maritime Ops 7, Ocean Carbon 16, Ocean Data & AI 8, Offshore Energy 10

## New business model patterns discovered
1. **Proactive hull grooming as-a-service** (Hullbot pattern): Shift from reactive cleaning (diminishing returns, intensive) to proactive grooming (prevents fouling before it occurs). No upfront cost to vessel operators — ongoing service relationship. Cloud robotics platform provides longitudinal fleet performance data. This is distinct from one-time cleaning services and creates a recurring revenue model tied to fuel savings.
2. **Space-to-seabed unified maritime intelligence** (Ubotica + Fugro pattern): Combining satellite edge AI (orbital processing, dark vessel detection) with Fugro's global ocean infrastructure (subsea sensors, USVs, UAVs, offshore vessels) creates the most comprehensive maritime intelligence stack in the knowledge graph. This is the first company to span the full vertical from space to seabed — previous Ocean Data & AI companies operated in either satellite (Amphitrite) or in-situ (Sofar Ocean) domains, not both.
3. **Price-parity electrification without green premium** (Fleetzero pattern): Marine battery systems achieving cost parity with fossil fuels — payback under 6 years, positive within 2 years for many projects. The "no green premium" positioning is distinct from other decarbonization approaches that require subsidies or premium pricing. Modular hull construction to lower shipyard costs is a secondary innovation addressing the shipbuilding capacity bottleneck.
4. **Drop-in biofuel as IMO compliance bridge** (Kvasir Technologies pattern): >96% GHG reduction with zero engine modification or infrastructure changes — enables the existing maritime fleet to meet IMO 2030/2050 targets without vessel replacement. This is a bridge solution distinct from electrification (Fleetzero) — it serves vessels that cannot be electrified and provides immediate compliance pathway while battery/hydrogen technologies mature.
5. **Full-stack aquaculture ecosystem with embedded finance** (AquaExchange pattern): Hardware + AI + finance + insurance + marketplace in one platform — addresses the entire farmer lifecycle (seed to harvest), not just monitoring. 20K devices across 4 countries with embedded finance and disease insurance. Acoustic demand-based feeding (FeedMon) is a novel modality beyond camera-based approaches. This is the most vertically integrated aquaculture company in the knowledge graph — previous companies focused on single product categories (sensors: Innovasea, vision: Aquabyte/Tidal, AI forecasting: BiOceanOr).

## Cross-company marine data patterns
- **Maritime decarbonization multi-pathway convergence**: Fleetzero (electrification), Kvasir Technologies (drop-in biofuel), and Hullbot (drag reduction via hull cleaning) now form a three-pathway decarbonization cluster in the knowledge graph. Each addresses a different lever: energy source, fuel type, and operational efficiency. All three have Maersk as a strategic connection (Maersk Growth invested in both Fleetzero and Kvasir). This signals that the shipping industry is pursuing parallel decarbonization strategies rather than betting on a single technology.
- **Space-to-seabed intelligence stack**: Ubotica extends Ocean Data & AI to the space domain. Combined with Sofar Ocean (2,500+ ocean drifters), Quartermaster (600+ vessel-mounted sensors), Coastal Measures (coastal sensor fabric), and Amphitrite (satellite data fusion), the knowledge graph now covers the full maritime intelligence stack from orbital AI to seafloor sensors. Ubotica's Fugro partnership is the first to explicitly bridge these layers.
- **Aquaculture vertical integration**: AquaExchange's full-stack approach (hardware + finance + insurance + marketplace) is the most vertically integrated model in the aquaculture sector. Previous companies were point solutions: Innovasea (sensors), Aquabyte/Tidal (vision), ReelData AI (land-based RAS AI), BiOceanOr (water quality forecasting). AquaExchange demonstrates that the market is maturing toward platform plays that capture more of the farmer lifecycle.
- **Ongoing defense ASV prime cluster**: With 6+ funded defense ASV primes (Saronic $2.6B, HavocAI $200M, Vatn Systems $60M, Ulysses $46M, Blue Water Autonomy $64M, Seasats $40M+), the defense marine autonomy sub-sector split threshold continues to be exceeded. No new defense ASV primes added this run, but the cluster remains a candidate for sub-sector split.

## Discovery source quality assessment
- **NewMarketPitch.com Ocean Tech Funding Analysis**: Excellent comprehensive tracker — 23 deals, 22 unique companies, covering Aug 2025–Jul 2026. Found 5 new high-signal companies in a single source. Should be checked monthly for updates.
- **The Robot Report**: Confirmed existing HavocAI ($85M + $100M) and Blue Water Autonomy ($50M) coverage — no new companies beyond what's already tracked.
- **Carbon Herald / cdr.fyi**: No new CDR companies discovered beyond existing coverage — the ocean CDR pipeline appears to be in a consolidation phase.

## Commit
- Git commit + push to origin/master
