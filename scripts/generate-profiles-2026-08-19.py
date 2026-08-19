#!/usr/bin/env python3
"""Daily update 2026-08-19: BeeX, Unseenlabs, Oceanloop, Spoor, Nernst Electric."""
import json, os, re, copy
from datetime import datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "2026-08-19"
TS = f"{DATE}T00:00:00Z"

def slugify(name):
    slug = name.lower()
    for a, b in [("ø", "o"), ("æ", "ae"), ("å", "a"), ("ü", "u"), ("é", "e"), ("è", "e")]:
        slug = slug.replace(a, b)
    slug = re.sub(r"[^a-z0-9-]", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug

COMPANIES = [
    {
        "name": "BeeX",
        "url": "https://www.beex.sg/",
        "sector": "Marine Monitoring & Sensors",
        "tag": "marine-monitoring-sensors",
        "notes": (
            "Singapore autonomous underwater drones (A.IKANBILIS flagship + BETTA/CASPER/ALPHA fleet) + SAMbal software "
            "for end-to-end inspection planning→geo-referenced reporting. $7.7M Series A (Jun/Aug 2026) led by Monk's Hill "
            "Ventures; SEEDS/SG Growth Capital, ShipsFocus, OCTAVE Capital, NUS Technology Holdings. 700+ deployments APAC/Europe; "
            "18,000+ hours in water; 50% cost savings vs WROV+DP2. Commercial: offshore wind, O&G, subsea cables, coastal infra. "
            "Defense: Singapore MINDEF multi-million contract for mine countermeasures/base protection/ISR. Founders Grace Chia (CEO) "
            "& Goh Eng Wei (CTO). Dual-use AUV autonomy at industrial grade."
        ),
        "description": "Singapore AUV fleet + SAMbal inspection software; $7.7M Series A (Monk's Hill); dual-use commercial/defense.",
        "raw": f"""# BeeX – Raw Web Extract
**Source:** https://www.beex.sg/
**Also:** https://www.beex.sg/news/beex-closes-usd7-7m-series-a-to-scale-autonomous-underwater-operations
**Also:** https://www.unmannedsystemstechnology.com/2026/08/beex-raises-usd-7-7-million-to-expand-underwater-drone-operations/
**Extracted:** {DATE}

## Overview
BeeX (Singapore) builds true-autonomy underwater drones for commercial infrastructure inspection and defense. Flagship A.IKANBILIS plus BETTA, CASPER, ALPHA fleet; proprietary SAMbal software suite for planning → collection → near-real-time anomaly snapshots → geo-referenced reporting. Founded by Grace Chia (CEO) and Goh Eng Wei (CTO). Claims: 14 years proprietary underwater data, 7 operational drones worldwide, 18,000+ hours in water, 700+ deployments Europe/Asia, 50% cost savings vs WROV+DP2 vessel campaigns, 90% less operational risk via crewless ops.

## Business Model
- Autonomous underwater inspection as alternative to work-class ROV + DP2 support vessels
- Dual markets: (1) commercial offshore wind / O&G / subsea cables / coastal infrastructure; (2) defense ISR, minehunting, seabed intelligence, clearance diving, base protection
- SAMbal software monetizes end-to-end data workflow beyond hardware
- Fleet expansion and international commercial/defense reach post Series A

## Funding
- **$7.7M USD Series A** (announced ~Jun 29 / covered Aug 5 2026) — led by Monk's Hill Ventures
- Participants: SEEDS (SG Growth Capital / EDB + Enterprise Singapore), ShipsFocus, OCTAVE Capital, NUS Technology Holdings
- Use of proceeds: expand autonomous underwater drone fleet and operational reach; build more tech capabilities

## Key Technology
- Adaptive autonomy for high-variability underwater environments
- A.IKANBILIS flagship AUV; BETTA launched as most powerful autonomous underwater drone (Jun 2026)
- SAMbal: inspection planning, drone data collection, near real-time anomaly snapshots, full geo-referenced timestamped reporting
- Absolute positioning + stabilization for consistent data quality vs operator-skill-dependent ROVs
- Optionally tethered lightweight independent ops; X:1 drone-to-operator ratio

## Proof points
- Deployed for leading offshore asset owners across APAC and Europe
- Singapore Ministry of Defence multi-million-dollar national security contract
- Clients/partners logos include Shell and other offshore majors (homepage)

## Contacts
- HQ Singapore; site https://www.beex.sg/ ; contact form /get in touch
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "BeeX",
            "url": "https://www.beex.sg/",
            "description": "Singapore company building autonomous underwater drones and SAMbal inspection software for offshore energy asset integrity and defense MCM/ISR.",
            "foundingLocation": {"@type": "Place", "name": "Singapore"},
            "founder": [
                {"@type": "Person", "name": "Grace Chia", "jobTitle": "CEO"},
                {"@type": "Person", "name": "Goh Eng Wei", "jobTitle": "CTO"},
            ],
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "USD",
                "value": 7700000,
                "description": "$7.7M Series A (2026) led by Monk's Hill Ventures",
            },
            "sector": "Marine Monitoring & Sensors",
            "businessModel": "Dual-use AUV fleet + SAMbal software for commercial subsea inspection (RaaS-style scale) and defense MCM/ISR; displaces WROV+DP2 campaigns",
            "lastFundingRound": "$7.7M Series A (2026) — Monk's Hill Ventures lead; SEEDS, ShipsFocus, OCTAVE, NUS Tech Holdings",
            "totalFunding": "$7.7M+ (Series A disclosed)",
            "investors": [
                "Monk's Hill Ventures",
                "SEEDS / SG Growth Capital",
                "ShipsFocus",
                "OCTAVE Capital",
                "NUS Technology Holdings",
            ],
            "knowsAbout": [
                "Autonomous underwater vehicles",
                "Subsea inspection",
                "Mine countermeasures",
                "Offshore wind asset integrity",
                "Underwater autonomy software",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "High-res optical/sonar inspection imagery",
                    "Geo-referenced anomaly snapshots",
                    "Mooring and subsea structure maps",
                    "Mine/UXO detection imagery",
                    "Bathymetry and seabed intelligence",
                ],
                "keyMeasurements": [
                    "Structural integrity indicators",
                    "Anomaly location/timestamp",
                    "Absolute underwater position",
                    "Depth and current conditions",
                    "Mine/limpet signatures",
                ],
                "observationPlatforms": [
                    "A.IKANBILIS / BETTA / CASPER / ALPHA AUV fleet",
                    "SAMbal mission planning and reporting stack",
                    "Offshore wind farms",
                    "Subsea cable routes",
                    "Naval MCM ranges",
                ],
                "knownGaps": [
                    "Labeled multi-environment anomaly training sets",
                    "Standardized AUV inspection data interchange with operators' digital twins",
                    "Long-duration swarm C2 in contested/noisy acoustic channels",
                ],
                "interestInExternalDataServices": "Metocean for mission planning, satellite/AIS surface cueing, operator digital twins, navy MDA layers, cable GIS",
            },
        },
        "wiki_body": f"""# BeeX

**Sector**: Marine Monitoring & Sensors
**Official Site**: https://www.beex.sg/

## Overview
**BeeX** (Singapore) builds true-autonomy underwater drones and the **SAMbal** software suite for industrial-grade subsea inspection and defense. Flagship **A.IKANBILIS** plus **BETTA / CASPER / ALPHA**. Founders **Grace Chia** (CEO) and **Goh Eng Wei** (CTO). **$7.7M Series A** (2026) led by **Monk's Hill Ventures**. 700+ deployments, 18,000+ hours in water, ~50% cost vs classic WROV+DP2 campaigns. Singapore **MINDEF** multi-million contract validates defense path.

## Business Model
- Displace crewed WROV + DP2 vessel inspection with autonomous AUV fleets (X:1 drone-to-operator)
- Dual-use: commercial offshore wind / O&G / cables / ports + defense MCM, ISR, base protection
- Software layer (SAMbal) owns the full inspection→report workflow — not just vehicle sales
- Scale via fleet expansion across APAC and Europe after Series A

## Funding
| Round | Amount | Date | Notes |
|-------|--------|------|-------|
| Series A | **$7.7M** | 2026 | Monk's Hill lead; SEEDS/SG Growth Capital, ShipsFocus, OCTAVE, NUS Tech Holdings |

## Key Technology
- Adaptive autonomy for high-variability underwater environments
- A.IKANBILIS flagship; BETTA "most powerful" AUV launch (Jun 2026)
- SAMbal: planning, collection, near-real-time anomalies, geo-referenced reporting
- Absolute positioning + stabilization for operator-independent data quality

## Data & Measurement Needs
- **Primary data types**: Optical/sonar inspection streams, geo-referenced anomaly packages, mooring/structure maps, MCM imagery, seabed intelligence
- **Key measurements/parameters**: Integrity indicators, anomaly lat/lon/time, absolute underwater pose, depth/current, mine signatures
- **Observation platforms/programs**: BeeX AUV fleet, offshore wind farms, cable routes, naval MCM ranges, coastal terminals
- **Known data gaps**: Multi-environment labeled anomaly corpora; AUV↔operator digital-twin interchange standards; swarm C2 in noisy acoustics
- **Interest in external data services**: Metocean mission windows, satellite/AIS cueing, asset GIS/digital twins, navy MDA layers

## Cross-Sector Connections
- Complements [Marine Monitoring & Sensors](marine-monitoring-sensors.md) AUV peers ([Bedrock Ocean Exploration](bedrock-ocean-exploration.md), [Ulysses](ulysses.md), [Vatn Systems](vatn-systems.md), [Orpheus Ocean](orpheus-ocean.md)) with APAC dual-use industrial maturity
- Inspection backbone for [Offshore Energy](offshore-energy.md) (wind/O&G/cables) and pairs with underwater comms like [WSense](wsense.md)
- Defense path adjacent to [Saronic Technologies](saronic-technologies.md) / [Kraken Technology](kraken-technology.md) surface autonomy — BeeX is the subsea counterpart

*Last Updated: {DATE}*
""",
    },
    {
        "name": "Unseenlabs",
        "url": "https://unseenlabs.com/en/",
        "sector": "Ocean Data & AI",
        "tag": "ocean-data-ai",
        "notes": (
            "French space RF GEOINT leader for maritime domain awareness — detects/geolocates shipborne RF emitters from LEO "
            "to find dark vessels that evade AIS. €85M Series C (Feb 2024) led by Supernova Invest, ISALT Strategic Transition Fund, "
            "UNEXO; historical 360 Capital, OMNES, Bpifrance, Breizh Up/UI, S2G Ventures; total funding ~€120M. Constellation "
            "scaling toward ~20–25 nanosats for ~30-min revisit (from 4–6h). Serves governments, fisheries IUU, offshore facilities, "
            "marine insurers, shipowners, NGOs, trade intelligence. Gen-2 multi-domain RF (maritime/land/space) announced 2026. "
            "Founders Clément & Jonathan Galic (2015, Brittany)."
        ),
        "description": "Space-based RF maritime surveillance for dark vessels; €85M Series C; ~€120M total; French constellation.",
        "raw": f"""# Unseenlabs – Raw Web Extract
**Source:** https://unseenlabs.com/en/
**Also:** https://www.omnescapital.com/press-release/unseenlabs-announces-a-record-breaking-fundraising-of-e85-million
**Also:** https://spacenews.com/investors-inject-92-million-into-french-maritime-surveillance-constellation/
**Extracted:** {DATE}

## Overview
Unseenlabs (France; founded 2015 by Clément and Jonathan Galic) is a global leader in radio-frequency (RF) maritime surveillance from space. Proprietary RF payloads on nanosatellites detect, characterize, and geolocate shipborne RF emitters worldwide, day/night, any weather — enabling monitoring of uncooperative "dark vessels" that turn off AIS. ~35% of the time ship positions are unknown or inaccurate via traditional means. Delivers RF geolocation coordinates, timestamps, RF technical parameters, data-fusion analytics, and intelligence reports.

## Business Model
- RF GEOINT data products and intelligence services sold to governments and private sector
- Segments: territorial waters/EEZ control, fisheries IUU, offshore facility security, marine insurance, shipowners, NGOs, business/trade intelligence
- Expand constellation for lower age-of-information (revisit); grow US/Asia commercial presence
- Gen-2 satellites extend RF detection across maritime, land, and space domains (2026)

## Funding
- **€85M Series C** (Feb 27, 2024) — new: Supernova Invest, ISALT (Strategic Transition Fund), UNEXO; existing: 360 Capital, OMNES, Bpifrance, Breizh Up (UI Investissement), S2G Ventures
- Prior rounds 2018, 2021; **total funding ~€120M** since inception
- Banking pool (Crédit Agricole Ille-et-Vilaine coordinator) + Barclays advisory
- Use: private-sector consolidation, multi-sat launches, US/Asia presence, talent, new products

## Key Technology
- In-house RF payload for passive detection of ship radars and electronic systems
- LEO constellation historically ~11 sats at 500–600 km; plan to ~20–25 for ~30-min revisit (from 4–6 hours)
- BRO-series Breizh Reconnaissance Orbiter satellites; SpaceX rideshares
- Data fusion for dark-vessel identification; multi-domain Gen-2 RF awareness
- Competitors: HawkEye 360 (US), Horizon Space Technologies (UK)

## Contacts
- https://unseenlabs.com/en/ ; Brittany / France New Space
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Unseenlabs",
            "url": "https://unseenlabs.com/en/",
            "description": "French space company providing RF geolocation of maritime emitters from LEO for dark-vessel detection and maritime domain awareness.",
            "foundingDate": "2015",
            "founder": [
                {"@type": "Person", "name": "Clément Galic"},
                {"@type": "Person", "name": "Jonathan Galic"},
            ],
            "address": {
                "@type": "PostalAddress",
                "addressCountry": "FR",
                "addressRegion": "Brittany",
            },
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "EUR",
                "value": 120000000,
                "description": "~€120M total incl. €85M Series C (Feb 2024)",
            },
            "sector": "Ocean Data & AI",
            "businessModel": "Space RF GEOINT data products and intelligence reports for government MDA and private maritime risk/insurance/IUU markets",
            "lastFundingRound": "€85M Series C (Feb 2024) — Supernova Invest, ISALT, UNEXO + historical investors",
            "totalFunding": "~€120M",
            "investors": [
                "Supernova Invest",
                "ISALT",
                "UNEXO",
                "360 Capital",
                "OMNES",
                "Bpifrance",
                "Breizh Up / UI Investissement",
                "S2G Ventures",
            ],
            "knowsAbout": [
                "RF maritime surveillance",
                "Dark vessel detection",
                "Space-based SIGINT/GEOINT",
                "Maritime domain awareness",
                "IUU fishing monitoring",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Space-based RF emitter detections",
                    "Vessel geolocation time series",
                    "AIS fusion layers",
                    "SAR/optical corroboration",
                    "Intelligence reports",
                ],
                "keyMeasurements": [
                    "RF emitter geolocation accuracy",
                    "Timestamp / age of information",
                    "RF technical parameters",
                    "Revisit interval",
                    "Dark-vessel confidence scores",
                ],
                "observationPlatforms": [
                    "BRO nanosatellite constellation",
                    "Ground processing and fusion stack",
                    "Customer MDA systems",
                ],
                "knownGaps": [
                    "Sub-30-minute global revisit at full constellation scale",
                    "Multi-sensor fusion standards with AIS/SAR/optical providers",
                    "Labeled ground-truth for dark-vessel behavior libraries",
                ],
                "interestInExternalDataServices": "AIS networks, SAR/optical EO (e.g. Ubotica-class edge AI), in-situ coastal radar, fisheries VMS, insurance claims data",
            },
        },
        "wiki_body": f"""# Unseenlabs

**Sector**: Ocean Data & AI
**Official Site**: https://unseenlabs.com/en/

## Overview
**Unseenlabs** (Brittany, France; founded **2015** by **Clément & Jonathan Galic**) leads **space-based RF maritime surveillance**. Nanosatellites detect and geolocate shipborne RF emitters to track **dark vessels** that disable AIS — day/night, any weather. **€85M Series C** (Feb 2024); **~€120M** total raised. Constellation scaling toward ~20–25 sats and ~30-minute revisit. Serves governments, fisheries IUU enforcement, offshore facilities, insurers, shipowners, and NGOs. **Gen-2** multi-domain RF (maritime/land/space) announced 2026.

## Business Model
- Sell RF GEOINT data products, analytics, and intelligence reports (not just raw RF)
- Public-sector MDA (EEZ, piracy, seabed protection) + private (O&G, insurance, trade intel, fisheries)
- Moat: proprietary in-house RF payload + growing LEO constellation revisit advantage
- Expand US/Asia commercial footprint with Series C capital

## Funding
| Round | Amount | Date | Notes |
|-------|--------|------|-------|
| Early | — | 2018, 2021 | 360 Capital, OMNES, Bpifrance, Breizh Up, S2G et al. |
| Series C | **€85M (~$92M)** | Feb 2024 | Supernova Invest, ISALT, UNEXO + all historicals; total **~€120M** |

## Key Technology
- Passive RF detection of ship radars/electronics from LEO (500–600 km)
- Geolocation + characterization + data-fusion dark-vessel ID
- BRO constellation; SpaceX rideshares; path to ~30-min age-of-information
- Gen-2 multi-domain RF awareness beyond maritime-only

## Data & Measurement Needs
- **Primary data types**: RF emitter detections, vessel tracklets, AIS fusion, SAR/optical corroboration, intel reports
- **Key measurements/parameters**: Geolocation accuracy, timestamp/AoI, RF parameters, revisit, dark-vessel confidence
- **Observation platforms/programs**: BRO nanosats, ground fusion, customer MDA systems
- **Known data gaps**: Full global sub-30-min revisit; multi-sensor fusion standards; labeled dark-vessel ground truth
- **Interest in external data services**: AIS, SAR/optical EO ([Ubotica](ubotica.md)), coastal radar, VMS, insurance claims

## Cross-Sector Connections
- Extends [Ocean Data & AI](ocean-data-ai.md) space layer alongside [Ubotica](ubotica.md) (optical edge AI) — RF + optical is complementary dark-fleet stack
- Feeds [Maritime Operations & Analytics](maritime-operations-analytics.md) and defense USV primes needing over-the-horizon cueing
- IUU use cases link to [Aquaculture](aquaculture.md)/fisheries enforcement and offshore facility security in [Offshore Energy](offshore-energy.md)

*Last Updated: {DATE}*
""",
    },
    {
        "name": "Oceanloop",
        "url": "https://oceanloop.com/",
        "sector": "Aquaculture",
        "tag": "aquaculture",
        "notes": (
            "Munich software-driven land-based marine RAS (raceway platform) scaling Europe's first land-based Giant Grouper. "
            "Up to €38.5M financing (Aug 2026): equity from Hatch Blue Blue Revolution Fund + Stolt Ventures; €32M EIB venture-debt "
            "(facility Oct 2024, amended Jul 2026 for grouper). Modular Oceanloop 100/1,000/4,000 m³ systems; <0.5% water exchange, "
            "~60% recirculation energy savings vs conventional RAS, Co-Pilot digital tools (sensors + CV + lab analytics). "
            "CEO Dr. Fabian Riedel; decade+ ops with Sander Aqua; Kiel/Baltic pilot; Honest Catch sister distribution. "
            "Licensing + owned farms model for international rollout."
        ),
        "description": "Software-driven land-based marine RAS for Giant Grouper; up to €38.5M (Hatch Blue, Stolt Ventures, EIB).",
        "raw": f"""# Oceanloop – Raw Web Extract
**Source:** https://oceanloop.com/
**Also:** https://oceanloop.com/technology
**Also:** https://www.eu-startups.com/2026/08/munich-based-oceanloop-nets-up-to-e38-5-million-to-scale-its-land-based-aquaculture-technology/
**Extracted:** {DATE}

## Overview
Oceanloop (Munich / Kiel Baltic coast) builds software-driven, land-based marine recirculating aquaculture systems (RAS) for premium seafood — notably Europe's first land-based Giant Grouper (sashimi-grade, Ikejime processing). Founder/CEO Dr. Fabian Riedel. Decade+ development with Sander Aqua. Sister company Honest Catch for DACH distribution. Goal: scale owned farms and licensed partner projects internationally.

## Business Model
- Technology platform + own production of premium marine species (Giant Grouper) closer to EU consumers
- Modular product line: Oceanloop 100 (R&D 40–100 m³), 1,000 (first commercial), 4,000 (industrial)
- Wholesale via selected distributors + Honest Catch; technology partnerships/licensing for international farms
- Differentiator: low-head raceway modular design vs fixed round-tank conventional RAS

## Funding
- **Up to €38.5M** (Aug 2026 announcement): equity from Hatch Blue Blue Revolution Fund and Stolt Ventures + **€32M EIB venture-debt**
- EIB facility originally signed Oct 7, 2024; amended Jul 20, 2026 to include Giant Grouper farming
- Marks industrial scale-up phase

## Key Technology
- Low-head raceway RAS: ~60% recirculation energy savings; plug-flow 4–6 cm/s; 4×/hr high recirculation; <0.5% closed water cycle makeup
- Multi-batch stocking via movable flow-through walls (multiple size classes, year-round harvest)
- Water treatment: drum filtration, foam fractionation, nitrification/denitrification, degassing, O2 injection, buffer dosing, backwash recycling
- Oceanloop Co-Pilot: ops data + lab analytics + sensors + computer vision for biomass, welfare, water quality, predictive maintenance, energy optimization (ShrimpWiz, SEADEEP research lineage)

## Contacts
- https://oceanloop.com/ ; Munich HQ; Kiel pilot farm
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Oceanloop",
            "url": "https://oceanloop.com/",
            "description": "Munich company building software-driven land-based marine RAS platforms and producing premium Giant Grouper in Europe.",
            "founder": {"@type": "Person", "name": "Dr. Fabian Riedel", "jobTitle": "CEO"},
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Munich",
                "addressCountry": "DE",
            },
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "EUR",
                "value": 38500000,
                "description": "Up to €38.5M (2026) incl. €32M EIB venture debt + Hatch Blue / Stolt Ventures equity",
            },
            "sector": "Aquaculture",
            "businessModel": "Own premium land-based marine seafood production + modular RAS technology licensing/partnerships; Co-Pilot digital layer",
            "lastFundingRound": "Up to €38.5M (Aug 2026) — Hatch Blue Blue Revolution Fund, Stolt Ventures equity + €32M EIB venture debt",
            "totalFunding": "Up to €38.5M disclosed package (2026)",
            "investors": [
                "Hatch Blue Blue Revolution Fund",
                "Stolt Ventures",
                "European Investment Bank",
            ],
            "knowsAbout": [
                "Recirculating aquaculture systems",
                "Land-based marine aquaculture",
                "Giant Grouper farming",
                "Aquaculture computer vision",
                "Water quality management",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "RAS sensor streams",
                    "Computer vision biomass/welfare video",
                    "Laboratory water chemistry",
                    "Energy and recirculation telemetry",
                    "Growth and feed conversion records",
                ],
                "keyMeasurements": [
                    "Dissolved oxygen",
                    "Temperature",
                    "Salinity",
                    "pH/alkalinity",
                    "TAN/nitrite/nitrate",
                    "CO2",
                    "Turbidity/solids",
                    "Biomass and individual size",
                    "Welfare indicators",
                    "Energy per kg fish",
                ],
                "observationPlatforms": [
                    "Oceanloop raceway modules",
                    "Co-Pilot digital twin/decision support",
                    "Kiel Baltic pilot",
                    "Partner licensed farms",
                ],
                "knownGaps": [
                    "Species-specific grouper welfare CV models at industrial density",
                    "Cross-farm benchmarking standards for licensed network",
                    "Predictive disease early-warning labeled datasets",
                ],
                "interestInExternalDataServices": "Feed formulation data, genetics partners, market price signals, coastal intake water quality, energy grid carbon intensity",
            },
        },
        "wiki_body": f"""# Oceanloop

**Sector**: Aquaculture
**Official Site**: https://oceanloop.com/

## Overview
**Oceanloop** (Munich; Baltic pilot at Kiel) builds **software-driven land-based marine RAS** — modular low-head raceways for premium seafood, led by Europe's first land-based **Giant Grouper**. CEO **Dr. Fabian Riedel**; decade+ ops with Sander Aqua. **Up to €38.5M** (Aug 2026): **Hatch Blue** Blue Revolution Fund + **Stolt Ventures** equity and **€32M EIB** venture debt. Sister brand **Honest Catch** for DACH go-to-market. Path: own farms + licensed international partners.

## Business Model
- Produce and sell premium land-raised marine fish (grouper) near EU demand centers
- Sell/license modular RAS platforms (100 / 1,000 / 4,000 m³) for partner projects
- Co-Pilot software connects multi-farm ops data, CV, and lab analytics
- Distinct from open-ocean cage tech: closed seawater loop, industrial control, year-round harvest

## Funding
| Round | Amount | Date | Notes |
|-------|--------|------|-------|
| Scale package | **Up to €38.5M** | Aug 2026 | Hatch Blue + Stolt Ventures equity; €32M EIB VD (amended Jul 2026 for grouper) |

## Key Technology
- Low-head raceway RAS: ~60% recirculation energy savings; <0.5% water makeup; plug-flow multi-batch walls
- Full water treatment train (mechanical/biological/chemical) + O2 injection
- Oceanloop Co-Pilot: sensors + lab + computer vision for biomass, welfare, WQ, maintenance, energy
- Superior Taste Award 2026 recognition for product quality

## Data & Measurement Needs
- **Primary data types**: Continuous RAS telemetry, CV biomass/welfare video, lab chemistry, energy logs, FCR/growth
- **Key measurements/parameters**: DO, T, S, pH/alkalinity, N-species, CO2, solids, biomass, welfare scores, kWh/kg
- **Observation platforms/programs**: Raceway modules, Co-Pilot, Kiel pilot, licensed partner farms
- **Known data gaps**: Industrial-density grouper CV models; cross-farm licensee benchmarks; disease early-warning labels
- **Interest in external data services**: Genetics/feed partners, intake water quality, market prices, grid carbon intensity

## Cross-Sector Connections
- Land-based RAS peer to [ReelData AI](reeldata-ai.md) (AI OS for RAS) — Oceanloop owns full hardware+biology stack
- Investor overlap with [Ace Aquatec](ace-aquatec.md) via **Stolt Ventures**; Hatch Blue links to broader aqua portfolio incl. [Nernst Electric](nernst-electric.md)
- Complements CV welfare players ([Tidal](tidal.md), [Aquabyte](aquabyte.md), [Biosort](biosort.md)) inside controlled raceways

*Last Updated: {DATE}*
""",
    },
    {
        "name": "Spoor",
        "url": "https://www.spoor.ai/",
        "sector": "Offshore Energy",
        "tag": "offshore-energy",
        "notes": (
            "Oslo AI computer-vision platform for continuous bird/bat monitoring at onshore and offshore wind farms — "
            "Sky Intelligence Platform for EIA, permitting, curtailment reduction, collision risk. €8M Series A to scale "
            "biodiversity monitoring software. Buoy-mounted offshore camera systems (4,500+ daytime hours/year); ≥95% detection "
            "accuracy; 1M+ birds training data; detections to 1.5 km; day/night. Customers/partners: Ørsted (Borssele trial), "
            "RWE, Ocean Winds, BTO, The Biodiversity Consultancy. De-risks offshore wind permitting with regulator-ready "
            "species-level flight height/flux datasets."
        ),
        "description": "AI bird/bat monitoring for wind farms; €8M Series A; Sky Intelligence Platform; Ørsted/RWE/Ocean Winds.",
        "raw": f"""# Spoor – Raw Web Extract
**Source:** https://www.spoor.ai/
**Also:** https://arcticstartup.com/spoor-raises-e8-million-series-a/
**Also:** https://techcrunch.com/2025/12/11/interest-in-spoors-bird-monitoring-ai-software-is-soaring/
**Extracted:** {DATE}

## Overview
Spoor (Oslo, Norway) builds AI-powered computer vision software and the Sky Intelligence Platform to continuously detect, track, and classify birds and bats at wind projects — onshore and offshore. Mission: make industry and nature coexist by turning wildlife monitoring into permitting and operational decisions. Deployed on 4 continents. Trusted logos: RWE, Ocean Winds, BTO, The Biodiversity Consultancy; Ørsted Borssele bird-monitoring collaboration.

## Business Model
- SaaS / platform data products for wind developers, operators, and environmental consultancies
- Continuous monitoring across project lifecycle: pre-construction EIA, buffer-zone optimization, operational curtailment minimization, collision detection
- Offshore: buoy-mounted camera systems integrated with metocean/LiDAR campaigns
- Division of labor: Spoor processes/delivers validated data; consultancies analyze and report to regulators

## Funding
- **€8M Series A** (disclosed via Arctic Startup / Dealroom coverage) to scale AI wildlife monitoring for wind as biodiversity regulation tightens
- Prior growth and commercial traction with major European offshore wind developers

## Key Technology
- Computer vision trained on 1M+ birds; detections up to 1.5 km; ≥95% accuracy; night/low-light capable
- Species ID with human expert validation; flight height, direction, flux, tracks
- Sky Intelligence Platform: monitor → validate/contextualize (weather/radar/historical) → regulator-ready exports → improve curtailment models over time
- Claimed 96% precision / 100% recall with full-resolution timestamped video per detection event
- Offshore buoy package: 4,500+ hours annual daytime monitoring all-weather

## Contacts
- https://www.spoor.ai/ ; Oslo, Norway; demo via /contact
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Spoor",
            "url": "https://www.spoor.ai/",
            "description": "Norwegian AI company providing continuous bird and bat monitoring for onshore and offshore wind permitting and operations.",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Oslo",
                "addressCountry": "NO",
            },
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "EUR",
                "value": 8000000,
                "description": "€8M Series A for AI wildlife monitoring at wind farms",
            },
            "sector": "Offshore Energy",
            "businessModel": "Sky Intelligence Platform SaaS + offshore buoy camera deployments selling decision-ready biodiversity data to wind developers and environmental consultancies",
            "lastFundingRound": "€8M Series A",
            "totalFunding": "€8M+ Series A disclosed",
            "knowsAbout": [
                "AI bird monitoring",
                "Offshore wind EIA",
                "Collision risk modeling",
                "Biodiversity compliance",
                "Computer vision wildlife tracking",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Continuous video of bird/bat activity",
                    "Species classifications",
                    "Flight tracks and heights",
                    "Metocean/weather context",
                    "Radar correlation layers",
                ],
                "keyMeasurements": [
                    "Species ID",
                    "Flight height distribution",
                    "Flux rates",
                    "Migration timing",
                    "Collision/avoidance events",
                    "Curtailment triggers",
                ],
                "observationPlatforms": [
                    "Turbine- and buoy-mounted cameras",
                    "Sky Intelligence Platform",
                    "Metocean/LiDAR campaign integration",
                    "Offshore wind farms (e.g. Borssele)",
                ],
                "knownGaps": [
                    "Long-range night/poor-weather species libraries offshore",
                    "Standardized CRM input formats across regulators",
                    "Multi-farm longitudinal baselines for migratory corridors",
                ],
                "interestInExternalDataServices": "Metocean/LiDAR buoys, weather models, radar networks, historical ornithology atlases, regulator EIA schemas",
            },
        },
        "wiki_body": f"""# Spoor

**Sector**: Offshore Energy
**Official Site**: https://www.spoor.ai/

## Overview
**Spoor** (Oslo) builds **AI computer vision** and the **Sky Intelligence Platform** for continuous **bird and bat monitoring** at onshore and offshore wind farms. **€8M Series A**. Deployed across 4 continents; ≥95% detection accuracy; 1M+ bird training set. Customers/partners include **Ørsted** (Borssele campaign), **RWE**, **Ocean Winds**, BTO, and The Biodiversity Consultancy. Turns wildlife uncertainty into permitting evidence and lower curtailment.

## Business Model
- Platform/SaaS biodiversity intelligence for developers, operators, and environmental consultancies
- Lifecycle coverage: EIA surveys → buffer optimization → operational curtailment reduction → collision analytics
- Offshore buoy-mounted cameras integrated with metocean/LiDAR campaigns
- Data-as-product: Spoor delivers validated detections; consultants/regulators consume exports

## Funding
| Round | Amount | Date | Notes |
|-------|--------|------|-------|
| Series A | **€8M** | ~2025–26 | Scale AI wildlife monitoring as biodiversity rules tighten |

## Key Technology
- CV detection/tracking/classification day & night; range to ~1.5 km
- Human-validated species ID; flight height, flux, tracks, weather context
- Sky Intelligence Platform decision workflow + regulator-ready video evidence
- Offshore: 4,500+ hours/year daytime buoy monitoring package

## Data & Measurement Needs
- **Primary data types**: Continuous wildlife video, species labels, flight tracks/heights, metocean context, radar layers
- **Key measurements/parameters**: Species, height distributions, flux, migration peaks, collision/avoidance, curtailment events
- **Observation platforms/programs**: Turbine/buoy cameras, Sky Intelligence, metocean campaigns, live wind farms
- **Known data gaps**: Offshore night/poor-weather species libraries; CRM input standards; multi-farm migratory baselines
- **Interest in external data services**: Metocean/LiDAR, NWP weather, radar, ornithology atlases, EIA schemas

## Cross-Sector Connections
- Direct biodiversity layer for [Offshore Energy](offshore-energy.md) developers ([Ørsted](orsted.md), floating wind peers)
- Complements metocean/ocean data providers ([Sofar Ocean](sofar-ocean.md), [XOCEAN](xocean.md), [Oshen](oshen.md)) — Spoor owns the avian channel
- Climate/nature risk adjacency to [Climate Risk](climate-risk.md) analytics via permitting and operational risk reduction

*Last Updated: {DATE}*
""",
    },
    {
        "name": "Nernst Electric",
        "url": "https://www.nernstelectric.com/",
        "sector": "Aquaculture",
        "tag": "aquaculture",
        "notes": (
            "Irish startup: on-site high-purity oxygen generation via ceramic Oxygen Transport Membrane (OTM) + additive "
            "manufacturing — targets remote fish farms where liquid oxygen logistics fail. €1.7M Seed (Jul 2026) from Hatch Blue "
            "Blue Revolution Fund; prior Hatch Accelerator Fund II pre-seed (Jul 2025). Founders Nick Farandos & Chris Matson (2023). "
            "Claims: <200 kWh/t O2 possible (vs PSA >1000), 100% O2 selectivity, no moving parts, >10x turndown, scalable <1 kg to "
            ">100 t/day. Primary beachhead aquaculture; also water treatment, mining/metallurgy, steel. First aquaculture deployment "
            "post-seed."
        ),
        "description": "On-site ceramic OTM oxygen generators for fish farms; €1.7M Hatch Blue Seed; Ireland.",
        "raw": f"""# Nernst Electric – Raw Web Extract
**Source:** https://www.nernstelectric.com/
**Also:** https://www.eu-startups.com/2026/07/irelands-nernst-electric-raises-e1-7-million-to-advance-on-site-oxygen-generation-technology-for-aquaculture-and-heavy-industry/
**Extracted:** {DATE}

## Overview
Nernst Electric (Ireland; founded 2023 by Nick Farandos and Chris Matson) builds ultra-efficient on-site oxygen generation using ceramic Oxygen Transport Membrane (OTM) technology and additive manufacturing. Primary beachhead: aquaculture — oxygen is the productivity limiter at remote fish farms that cannot economically access liquid oxygen (LOx) markets and face climate-driven oxygen variability. Also targets water treatment, mining/metallurgy, and steel.

## Business Model
- Hardware: on-site oxygen generators sold/deployed to fish farms and industrial gas users
- Disrupts LOx trucking and energy-intensive PSA for remote/variable demand sites
- Massive turndown (>10x vs ~40% for PSA) matches biological demand swings
- Path from aquaculture first deployment to broader industrial O2 markets

## Funding
- **€1.7M Seed** (Jul 2026) — Hatch Blue Blue Revolution Fund
- Pre-seed / Hatch Accelerator Fund II (Jul 2025) + Hatch Blue accelerator programme
- Use: first aquaculture deployment; scale manufacturing concept to working systems

## Key Technology
- Ceramic OTM separates oxygen directly from air — electrolyte with 100% oxygen selectivity
- Additive manufacturing of reactors from low-cost abundant materials
- Efficiency target <200 kWh per ton O2 (vs PSA often >1000 kWh/t)
- No moving parts → minimal maintenance / low fatal downtime risk for fish stocks
- Scale range: <1 kg to >100 tons O2 per day; purity >99 vol% (vs PSA 85–92%)

## Contacts
- https://www.nernstelectric.com/ ; Ireland
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Nernst Electric",
            "url": "https://www.nernstelectric.com/",
            "description": "Irish company developing ceramic oxygen transport membrane generators for on-site high-purity oxygen, starting with aquaculture.",
            "foundingDate": "2023",
            "founder": [
                {"@type": "Person", "name": "Nick Farandos"},
                {"@type": "Person", "name": "Chris Matson"},
            ],
            "address": {
                "@type": "PostalAddress",
                "addressCountry": "IE",
            },
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "EUR",
                "value": 1700000,
                "description": "€1.7M Seed (Jul 2026) Hatch Blue Blue Revolution Fund",
            },
            "sector": "Aquaculture",
            "businessModel": "Sell/deploy on-site OTM oxygen generation hardware to remote aquaculture and industrial users as LOx/PSA alternative",
            "lastFundingRound": "€1.7M Seed (Jul 2026) — Hatch Blue Blue Revolution Fund",
            "totalFunding": "€1.7M+ (Seed; prior Hatch pre-seed)",
            "investors": [
                "Hatch Blue Blue Revolution Fund",
                "Hatch Accelerator Fund II",
            ],
            "knowsAbout": [
                "Oxygen transport membranes",
                "On-site oxygen generation",
                "Aquaculture oxygenation",
                "Solid oxide electrochemistry",
                "Additive manufacturing",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Dissolved oxygen time series",
                    "Stocking density and biomass",
                    "Water temperature",
                    "Feed and metabolism proxies",
                    "Generator O2 output/energy telemetry",
                ],
                "keyMeasurements": [
                    "DO mg/L",
                    "Temperature",
                    "O2 demand forecast",
                    "kWh per ton O2",
                    "Purity vol%",
                    "Turndown response time",
                ],
                "observationPlatforms": [
                    "Farm DO sensor networks",
                    "On-site OTM generators",
                    "Hatchery and grow-out sites",
                ],
                "knownGaps": [
                    "Site-specific DO demand models under marine heatwaves",
                    "Integration APIs with farm management platforms",
                    "Long-duration field reliability datasets in harsh marine climates",
                ],
                "interestInExternalDataServices": "Farm IoT platforms (Innovasea-class), weather/SST forecasts, RAS Co-Pilot systems (Oceanloop), grid power quality",
            },
        },
        "wiki_body": f"""# Nernst Electric

**Sector**: Aquaculture
**Official Site**: https://www.nernstelectric.com/

## Overview
**Nernst Electric** (Ireland; founded **2023** by **Nick Farandos** & **Chris Matson**) builds **on-site ceramic Oxygen Transport Membrane (OTM)** generators for high-purity oxygen — beachhead **remote fish farms** where liquid oxygen logistics fail. **€1.7M Seed** (Jul 2026) from **Hatch Blue** Blue Revolution Fund after Hatch accelerator pre-seed (2025). Targets <200 kWh/t O2, 100% selectivity, no moving parts, >10× turndown.

## Business Model
- Hardware deployment of modular on-site O2 generators (aquaculture first; water treatment, mining, steel next)
- Replaces LOx trucking and inefficient PSA at remote/variable-demand sites
- Reliability moat: no moving parts reduces fatal oxygenation downtime for stock
- Scale manufacturing from working prototype to multi-site farm deployments

## Funding
| Round | Amount | Date | Notes |
|-------|--------|------|-------|
| Pre-seed | Undisclosed | Jul 2025 | Hatch Accelerator Fund II + Hatch Blue programme |
| Seed | **€1.7M** | Jul 2026 | Hatch Blue Blue Revolution Fund — first aqua deployment |

## Key Technology
- Ceramic OTM air separation via solid-oxide electrochemistry + additive manufacturing
- Purity >99 vol%; efficiency path <200 kWh/t; scale <1 kg to >100 t/day
- Massive turndown matches biological oxygen demand swings better than PSA

## Data & Measurement Needs
- **Primary data types**: Farm DO streams, biomass/density, temperature, metabolism proxies, generator energy/output telemetry
- **Key measurements/parameters**: DO mg/L, T, O2 demand forecast, kWh/t, purity, turndown latency
- **Observation platforms/programs**: Farm sensor nets, OTM units, hatchery/grow-out sites
- **Known data gaps**: Heatwave DO demand models; farm-platform APIs; multi-season marine reliability data
- **Interest in external data services**: Aqua IoT ([Innovasea](innovasea.md)), SST/weather forecasts, RAS stacks ([Oceanloop](oceanloop.md), [ReelData AI](reeldata-ai.md))

## Cross-Sector Connections
- Critical input layer for [Aquaculture](aquaculture.md) welfare and RAS players — oxygen is the shared productivity bottleneck
- Hatch Blue co-portfolio with [Oceanloop](oceanloop.md); complements forecasting ([BiOceanOr](bioceanor.md)) that predicts hypoxia while Nernst supplies O2 response
- Industrial O2 path later overlaps heavy industry decarbonization outside core blue-economy graph

*Last Updated: {DATE}*
""",
    },
]


def write_profiles():
    for c in COMPANIES:
        slug = slugify(c["name"])
        # raw
        with open(os.path.join(REPO, "raw", f"{slug}.md"), "w") as f:
            f.write(c["raw"].rstrip() + "\n")
        # metadata
        with open(os.path.join(REPO, "metadata", f"{slug}.jsonld"), "w") as f:
            json.dump(c["metadata"], f, indent=2)
            f.write("\n")
        # wiki OKF
        fm = {
            "type": "Company",
            "title": c["name"],
            "description": c["description"],
            "resource": c["url"],
            "tags": [c["tag"]],
            "timestamp": TS,
            "date": DATE,
            "sector": c["sector"],
        }
        # manual frontmatter for stable formatting
        lines = ["---", f"type: Company", f"title: {c['name']}", f"description: {c['description']}", f"resource: {c['url']}", "tags:", f"- {c['tag']}", f"timestamp: '{TS}'", f"date: '{DATE}'", f"sector: {c['sector']}", "---", "", c["wiki_body"].lstrip()]
        with open(os.path.join(REPO, "wiki", f"{slug}.md"), "w") as f:
            f.write("\n".join(lines).rstrip() + "\n")
        print(f"Wrote {slug}")


def update_companies_json():
    path = os.path.join(REPO, "sources", "companies.json")
    with open(path) as f:
        data = json.load(f)
    existing = {x["name"].lower() for x in data}
    added = []
    for c in COMPANIES:
        if c["name"].lower() in existing:
            print(f"SKIP existing: {c['name']}")
            continue
        data.append(
            {
                "sector": c["sector"],
                "name": c["name"],
                "url": c["url"],
                "notes": c["notes"],
                "last_updated": DATE,
            }
        )
        added.append(c["name"])
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"companies.json now {len(data)}; added {added}")
    return added


if __name__ == "__main__":
    write_profiles()
    update_companies_json()
