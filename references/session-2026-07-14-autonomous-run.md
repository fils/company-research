# Autonomous Run — 2026-07-14

## Pre-run
- Working tree clean; last commit: b99e5e7 (Daily update 2026-07-13)
- Completeness check: 0 errors, 0 warnings (79 companies)

## Phase 1 — Sources (Discovery)
- Discovery searches: ocean tech startup funding 2026, ocean carbon removal funding, maritime AI autonomous vessel, aquaculture AI startup
- High-signal finds (4 new companies):
  1. **Blue Water Autonomy** — $50M Series A (Aug 2025, GV lead) + $14M seed = ~$64M total; autonomous warships (Liberty-class 190-ft USV) for US Navy; founded 2024 Boston; repeat entrepreneurs (Rylan Hamilton CEO, ex-Navy/Amazon Robotics/6 River Systems $450M Shopify exit; Scott Miller CTO, ex-iRobot VP Eng/Roomba; Austin Gray CSO, ex-Navy intel/Ukraine drone factory); full-stack autonomy from keel up; Pentagon $2.1B MUSV funding; China 200x US shipbuilding capacity
  2. **Maritime Robotics** — €28M growth investment (Jun 2026, MS+PARTNERS lead) + $12M (2024); Norwegian USV pioneer since 2005 (Trondheim); SEACONTROL autonomous nav system + Mariner X/Otter USVs + mine countermeasures USV; revenue 5x in 5 years, 2x in 2 years; hundreds of systems delivered; dual-use commercial+defense
  3. **SEA.AI** — €3M Series A; Austrian maritime machine vision for safety (founded 2018, formerly OSCAR); 45 employees across Austria/France/Portugal/USA; optical+thermal camera fusion detects objects escaping radar/AIS; counter-USV detection for defense; NVIDIA edge AI partner; Robosys partnership for autonomous collision avoidance; products: Watchkeeper, Sentry, Brain (retrofit), Competition
  4. **BiOceanOr** — ~€2.5M funding (€2M Yield Lab Europe + €500K convertible; BlueInvest-supported); French aquaculture AI water quality forecasting; AquaCHECK/AquaFORECAST (12h oxygen forecast 0.5 mg/L accuracy)/AquaLYTICS; 10M+ data points/mo; 10+ countries (Chilean salmon PREDIMAR, Norway); CEO Samuel Dupont; biology+AI combination as moat
- Sector placement decisions:
  - Blue Water Autonomy → Marine Monitoring & Sensors (defense ASV prime, like Saronic)
  - Maritime Robotics → Marine Monitoring & Sensors (USV sensor/data platform, dual-use)
  - SEA.AI → Maritime Operations & Analytics (maritime AI vision/nav safety, like Orca AI)
  - BiOceanOr → Aquaculture (water quality AI forecasting)
- Net companies: 79 + 4 = **83**

## Phases 2–4
- Ingested homepages via web_extract for all 4 companies
- Wrote raw/, metadata/ JSON-LD, wiki/ profiles with Data & Measurement Needs sections
- Updated sector wiki pages:
  - wiki/marine-monitoring-sensors.md: count 18→20, added Blue Water Autonomy + Maritime Robotics entries
  - wiki/maritime-operations-analytics.md: count 6→7, added SEA.AI entry + 2 new cross-company patterns (Radar/AIS gap filling, camera retrofit business model)
  - wiki/aquaculture.md: count 15→16, added BiOceanOr entry + 1 new cross-company pattern (biology+AI water quality forecasting)
- All wiki profiles include standardized Data & Measurement Needs sections (primary data types, key measurements, observation platforms, known gaps, interest in external data services)

## Completeness
- ✅ COMPLETENESS CHECK PASSED — 0 errors, 0 warnings — 83 companies
- Sector breakdown: Aquaculture 16, Bioprospecting 1, Climate Risk 5, Coastal Risk 3, Marine Monitoring 20, Maritime Ops 7, Ocean Carbon 16, Ocean Data & AI 7, Offshore Energy 8

## New business model patterns discovered
1. **Mass-production-first autonomous warship design** (Blue Water Autonomy pattern): Distinct from Saronic (multi-class ASV portfolio) — Blue Water focuses on perfecting a single platform class (Liberty) with full-stack hardware+software+AI integration from keel up. Founded by repeat hardware entrepreneurs (6 River Systems/Shopify $450M exit, iRobot/Roomba scaling). The mass-production philosophy directly counters China's 200x shipbuilding advantage — the bottleneck is not the autonomy AI but the shipyard throughput.
2. **Structural shift to fleet-level USV deployment** (Maritime Robotics pattern): A 20-year-old Norwegian USV pioneer with hundreds of systems delivered reports customers shifting from pilot projects to fleet-level deployment strategies — revenue 5x in 5 years. This signals sector-wide maturation: autonomous maritime systems are past the experimentation phase. The €28M growth investment (MS+PARTNERS, a growth PE firm not a VC) confirms this is a scaling-phase business, not early-stage R&D.
3. **Optical AI as radar/AIS gap filler** (SEA.AI pattern): Maritime machine vision that detects objects escaping both radar and AIS — unsignalled craft, debris, persons overboard. Distinct from Orca AI (fleet visual dataset for bridge awareness) and Sea Machines (full vessel autonomy), SEA.AI focuses specifically on the sensor gap that neither conventional system covers. The counter-USV use case is timely given drone boat threat proliferation in 2025-2026 naval conflicts.
4. **Camera retrofit business model** (SEA.AI Brain pattern): Upgrading existing thermal cameras with AI module — distinct from full-system sales, lowering adoption barriers for vessel operators who already have camera hardware. A go-to-market strategy that captures installed base without requiring full hardware replacement.
5. **Biology+AI water quality forecasting** (BiOceanOr pattern): 5-year R&D combining oceanographers/marine biologists with ML produces 12h oxygen forecasts at 0.5 mg/L accuracy — a concrete measurable performance benchmark. The biology+AI combination (20+ domain experts) is a moat vs pure-software competitors. Addresses shared critical risk (hypoxia, HABs) across ALL aquaculture operations, complementing sensor-hardware (Innovasea), computer vision (Aquabyte/Tidal), and synthetic data (NeuralX) approaches.

## Cross-company marine data patterns
- **Defense ASV prime cluster maturation**: Blue Water Autonomy ($64M) joins Saronic ($2.6B), HavocAI ($200M), Seasats ($40M+), Vatn Systems ($60M), Ulysses ($46M) — the defense autonomous surface vessel sector now has 6+ funded primes in the Marine Monitoring & Sensors category. The Marine Monitoring & Sensors sector at 20 companies is approaching a natural sub-sector split threshold (defense ASV primes vs sensor/AUV platforms).
- **Structural USV market maturation**: Maritime Robotics' "past the experimentation phase" and "fleet-level deployment" signals confirm the broader 2026 theme that autonomous maritime systems are entering commercial scaling. Revenue 5x in 5 years is a leading indicator for the sector.
- **Maritime AI vision consolidation**: Orca AI (80M+ nm), Sea Machines (AI-ris 4K), and SEA.AI (optical+thermal) now form a 3-company cluster in Maritime Ops. Each occupies a distinct niche: Orca = fleet visual dataset, Sea Machines = full autonomy, SEA.AI = radar/AIS gap filler + retrofit.
- **Aquaculture environmental forecasting**: BiOceanOr (water quality forecasting) joins ORCA (fisheries shock prediction) and Kurma AI (foundation models) in addressing environmental risk prediction — a shared critical need as climate variability intensifies. The 0.5 mg/L oxygen forecast accuracy is a measurable benchmark for the sector.

## Files changed
- sources/companies.json (+4 entries)
- raw/blue-water-autonomy.md, raw/maritime-robotics.md, raw/sea-ai.md, raw/bioceanor.md (NEW)
- metadata/blue-water-autonomy.jsonld, metadata/maritime-robotics.jsonld, metadata/sea-ai.jsonld, metadata/bioceanor.jsonld (NEW)
- wiki/blue-water-autonomy.md, wiki/maritime-robotics.md, wiki/sea-ai.md, wiki/bioceanor.md (NEW)
- wiki/marine-monitoring-sensors.md, wiki/maritime-operations-analytics.md, wiki/aquaculture.md (UPDATED)
- references/session-2026-07-14-autonomous-run.md (NEW)

## Commit
- (pending)
