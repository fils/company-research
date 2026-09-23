#!/usr/bin/env python3
"""Daily update 2026-09-23: ARK Inc, Bulwark Dynamics, Marcura, HydroSurv."""
import json
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "2026-09-23"
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
        "name": "ARK Inc",
        "url": "https://www.ark.inc/en/",
        "sector": "Aquaculture",
        "tag": "aquaculture",
        "notes": (
            "Japanese modular closed RAS hardware + land-based seafood production ('let the ocean rest, create your own'). "
            "Series A ~$8.5M / ¥1.3B equity+loans (ann. 17 Sep 2026): UntroD Capital Japan, Beyond Next Ventures, BP Capital "
            "(Tokyo University of Agriculture and Technology Fund) lead equity; Resona Bank, Hokkoku Bank, Japan Finance Corporation loans. "
            "Global South expansion (UAE Abu Dhabi MOU, Indonesia pilots under METI co-creation subsidy); APAC base Malaysia Sep 2026; "
            "SoftBank Vision Fund founding member Yosuke Sasaki non-exec director. Species: grouper, whiteleg/kuruma prawn, research sea urchin/algae. "
            "Founded Dec 2020 Hiratsuka; CEO Yosuke Kurihara (London)."
        ),
        "description": (
            "Japanese modular closed RAS + land-based seafood (grouper/shrimp); ~$8.5M Series A Sep 2026; Global South UAE/Indonesia expansion."
        ),
        "raw": f"""# ARK Inc – Raw Web Extract
**Source:** https://www.ark.inc/en/
**Also:** https://www.ark.inc/en/company/
**Also:** https://www.ark.inc/en/news/
**Also:** https://thefishsite.com/articles/land-based-aquaculture-startup-ark-raises-8-5-million
**Extracted:** {DATE}

## Overview
ARK Inc (株式会社ARK) is a Japan-based R&D-driven land-based aquaculture company founded December 2020 in Hiratsuka, Kanagawa. Tagline: **"Let the ocean rest, create your own."** Dual business: (1) develop/manufacture/sell modular closed recirculating aquaculture systems (RAS), equipment, materials, and services; (2) produce and sell land-based farmed seafood via own farms, joint, and contract production, plus processing/distribution. Priority species: **groupers** (Malabar, longtooth×giant, tiger×giant hybrids) and **prawns** (kuruma, whiteleg); research on sea urchin and algae. Case deployments include Yamada Shokai (Aichi), Kyoritsu Kiko (Tochigi whiteleg shrimp), Ritsumeikan University (honmoroko), University of the Ryukyus (Malabar grouper).

## Business Model
- **Hardware + services**: modular closed RAS sold to operators starting land-based farms
- **Production**: own/joint/contract land-based seafood production and downstream sales
- Positioning: enable land-based aquaculture "anywhere," including harsh Global South climates
- International hubs: ARK WORLDWIDE LTD (London), ARK ASIA PACIFIC SDN. BHD. (Cyberjaya, Malaysia, est. Sep 2026)
- Policy tailwinds: Japan Growth Strategy (Jul 2026) lists food tech / land-based aquaculture as strategic; METI Global South co-creation subsidy operator (Jul 2026); Abu Dhabi fisheries MOU (Feb 2026)

## Funding
- **Series A ~US$8.5M / ~¥1.3B** announced **17 Sep 2026** (equity + loans)
- Equity leads: **UntroD Capital Japan**, **Beyond Next Ventures**, **BP Capital** (Tokyo University of Agriculture and Technology Fund) + three additional VC/corporate investors
- Loans: lead **Resona Bank**; **The Hokkoku Bank**; **Japan Finance Corporation**
- Use of proceeds: business foundation, RAS tech/product development, facility development, global talent for UAE/Indonesia and Global South expansion
- Governance: SoftBank Vision Fund founding member **Yosuke Sasaki** appointed non-executive director (11 Sep 2026)

## Key Technology
- Modular **closed recirculating aquaculture systems (RAS)** designed for harsh-environment resilience
- Species know-how centered on high-value **grouper** and prawn culture
- Multi-site Japan labs: Shonan R&D Studio, Hiratsuka Aquaculture Lab, Kansai, Okinawa

## Marine Data & Ops Needs
- Continuous RAS water-quality loops (temp, DO, pH, salinity, ammonia/nitrite/nitrate, CO₂, alkalinity)
- Biofilter health / microbiome state; feed conversion and growth curves by species/strain
- Energy/thermal budgets for modular plants; pathogen early warning in closed systems
- Site selection metocean only secondary (land-based) but coastal intake/discharge compliance where used
- Multi-country pilot telemetry for UAE/Indonesia METI demos

## Contacts
- https://www.ark.inc/en/
- CEO / Co-founder: Yosuke Kurihara
- COO: Isamu Yoshida; CTO: Takenoshita Koyo
- HQ: 57-7 Sengokukashi, Hiratsuka, Kanagawa, Japan
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "ARK Inc",
            "url": "https://www.ark.inc/en/",
            "description": "Japanese modular closed RAS systems and land-based seafood production focused on grouper and prawn; Global South expansion.",
            "sector": "Aquaculture",
            "foundingDate": "2020-12",
            "businessModel": "B2B modular RAS hardware/services + own/joint land-based seafood production and sales",
            "lastFundingRound": "Series A ~US$8.5M equity+loans (ann. 17 Sep 2026)",
            "totalFunding": "~US$8.5M Series A (equity + loans; full cumulative not fully disclosed)",
            "investors": [
                "UntroD Capital Japan",
                "Beyond Next Ventures",
                "BP Capital (Tokyo University of Agriculture and Technology Fund)",
                "Resona Bank (loan)",
                "The Hokkoku Bank (loan)",
                "Japan Finance Corporation (loan)",
            ],
            "employee": [
                {"@type": "Person", "name": "Yosuke Kurihara", "jobTitle": "Director & CEO / Co-founder"},
                {"@type": "Person", "name": "Isamu Yoshida", "jobTitle": "Director & COO / Co-founder"},
                {"@type": "Person", "name": "Takenoshita Koyo", "jobTitle": "Director & CTO / Co-founder"},
                {"@type": "Person", "name": "Yosuke Sasaki", "jobTitle": "Non-Executive Director"},
            ],
            "knowsAbout": [
                "Modular closed RAS",
                "Land-based aquaculture",
                "Grouper culture",
                "Prawn/shrimp RAS",
                "Global South food security",
            ],
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Hiratsuka",
                "addressRegion": "Kanagawa",
                "addressCountry": "JP",
            },
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "RAS water chemistry time series",
                    "Biofilter microbiome state",
                    "Growth/FCR and mortality",
                    "Energy and thermal plant telemetry",
                ],
                "keyParameters": [
                    "temperature",
                    "dissolved oxygen",
                    "pH",
                    "salinity",
                    "TAN/nitrite/nitrate",
                    "CO2",
                    "alkalinity",
                ],
                "observationPrograms": [
                    "On-site RAS sensor networks",
                    "Multi-lab pilot farms Japan",
                    "UAE/Indonesia METI demonstration telemetry",
                ],
                "knownGaps": [
                    "Cross-climate modular performance baselines",
                    "Pathogen early-warning integration in closed loops",
                    "Interoperable farm OS for Global South operators",
                ],
            },
        },
        "wiki_body": f"""# ARK Inc

**Sector**: Aquaculture
**Official Site**: https://www.ark.inc/en/

## Overview
**ARK Inc** (株式会社ARK) builds **modular closed recirculating aquaculture systems (RAS)** and operates/partners on **land-based seafood production** under the motto *"Let the ocean rest, create your own."* Founded **Dec 2020** in Hiratsuka, Kanagawa, with R&D and farm labs across Japan plus **London** and **Malaysia (Cyberjaya)** offices. Commercial focus: high-value **grouper** and **prawn/shrimp** culture transferable to harsh **Global South** climates (UAE Abu Dhabi MOU; Indonesia pilots under METI subsidy).

## Business Model
- **B2B RAS stack**: develop, manufacture, sell land-based aquaculture tech, equipment, materials, and services
- **Production & sales**: own farms, joint ventures, and contract production of land-based seafood; processing/distribution
- Expansion thesis: modular RAS resilient in harsh environments + grouper expertise as food-security hub along IMEEC corridor (Abu Dhabi)
- Policy alignment: Japan Growth Strategy food-tech priority; METI Global South co-creation project operator

## Funding
- **Series A ~US$8.5M / ~¥1.3B** (announced **17 Sep 2026**) combining equity and loans
- Equity leads: **UntroD Capital Japan**, **Beyond Next Ventures**, **BP Capital** (TUAT fund) + additional VC/corporate investors
- Debt: **Resona Bank** (lead), **Hokkoku Bank**, **Japan Finance Corporation**
- SoftBank Vision Fund founding member **Yosuke Sasaki** joined as non-executive director (Sep 2026)

## Key Technology
- Modular **closed RAS** hardware for distributed land-based farms
- Species programs: Malabar/hybrid **groupers**, kuruma & whiteleg **prawns**; research sea urchin/algae
- Multi-site Japan demonstration network (Shonan R&D, Hiratsuka lab, Kansai, Okinawa)

## Data & Measurement Needs
- **Primary data types**: Continuous RAS water-quality streams; biofilter/microbiome state; growth, FCR, mortality; plant energy/thermal telemetry; multi-country pilot datasets
- **Key measurements/parameters**: Temperature, DO, pH, salinity, TAN/NO₂/NO₃, CO₂, alkalinity; species-specific growth curves; pathogen indicators in closed loops
- **Observation platforms/programs**: On-site sensor networks at modular plants; Japan lab farms; UAE/Indonesia METI FS/demo telemetry
- **Known data gaps**: Cross-climate performance baselines for modular RAS; standardized pathogen early-warning in closed systems; interoperable farm OS for new Global South operators; intake/discharge compliance data where coastal water is used
- **Interest in external data services**: RAS AI control stacks ([ReelData AI](reeldata-ai.md), [Oceanloop](oceanloop.md)); hypoxia/WQ forecasting patterns ([BiOceanOr](bioceanor.md)); molecular biosecurity ([Nucleic Sensing Systems](nucleic-sensing-systems.md), [Esox Biologics](esox-biologics.md)); on-site O₂ infrastructure ([Nernst Electric](nernst-electric.md))

## Cross-Sector Connections
- Direct peer to industrial land-based marine RAS ([Oceanloop](oceanloop.md)) with stronger **hardware export + Global South** angle and grouper specialty
- Complements RAS AI OS ([ReelData AI](reeldata-ai.md)) — ARK supplies physical plant; ReelData optimizes operations
- Species/welfare monitoring stack can plug CV and biomarker tools ([Tidal](tidal.md), [Aquabyte](aquabyte.md), [WellFish Tech](wellfish-tech.md))
- Sector home: [Aquaculture](aquaculture.md)

---
**Cross-links**: [Aquaculture](aquaculture.md) · [Oceanloop](oceanloop.md) · [ReelData AI](reeldata-ai.md) · [Nernst Electric](nernst-electric.md) · [BiOceanOr](bioceanor.md) · [WellFish Tech](wellfish-tech.md)

*Last Updated: {DATE}*
""",
    },
    {
        "name": "Bulwark Dynamics",
        "url": "https://bulwarkdynamics.com/",
        "sector": "Marine Monitoring & Sensors",
        "tag": "marine-monitoring-sensors",
        "notes": (
            "DefenseTech autonomous beach-landing resupply USV (CARAVEL) for contested Indo-Pacific logistics / EABO. "
            "$6.8M seed (Sep 2026) with Japanese shipyard Onomichi Dockyard as investor+build partner; Menlo Park prototype facility (Jan 2026); pre-seed Sep 2025. "
            "Specs: ~23,000 lb payload, ~1,100 nm range, JMIC/ISO containers, GPS-denied autonomy, autonomous beach/discharge/redeploy. "
            "CEO Nhat Lieu. Vertically integrated autonomy+hull production thesis vs software-only USV startups."
        ),
        "description": (
            "Autonomous beach-landing resupply USV (CARAVEL) for contested logistics; $6.8M seed Sep 2026 with Onomichi Dockyard; Menlo Park."
        ),
        "raw": f"""# Bulwark Dynamics – Raw Web Extract
**Source:** https://bulwarkdynamics.com/
**Also:** https://bulwarkdynamics.com/mission
**Also:** https://bulwarkdynamics.com/vessel
**Also:** https://maritime-executive.com/article/u-s-landing-drone-startup-gets-support-from-a-small-japanese-shipyard
**Extracted:** {DATE}

## Overview
Bulwark Dynamics (Menlo Park, CA) is a DefenseTech company building **CARAVEL**, an autonomous beach-landing resupply vessel for contested maritime logistics. Thesis: ports and fixed infrastructure are first targets; distributed Expeditionary Advanced Base Operations (EABO) across the Western Pacific need attritable, shallow-draft, port-independent connectors that beach, discharge cargo, and redeploy without shore crew. Positions outside classic Navy USV buckets (small patrol USVs vs medium USVs) into **landing-craft logistics drones**.

## Business Model
- Vertically integrated autonomous maritime logistics: autonomy + C2 + hull production + payload integration + expeditionary manufacturing
- Production partnership with Japanese FRP shipbuilding (Onomichi Dockyard investor + builder) to scale hundreds of hulls/year near First Island Chain
- Defense / allied military customer focus; attritable low-cost hulls vs legacy LCU/LCAC connectors ($32M+)
- KPI framed as production capacity, not demo autonomy alone

## Funding
- **$6.8M seed (September 2026)** including **Onomichi Dockyard** and VC participants — fuels prototype build/test of CARAVEL
- Prototype production facility opened **January 2026** (Menlo Park)
- **Pre-seed closed September 2025** for initial prototype development and field testing
- CEO/co-founder: **Nhat Lieu**

## Key Technology
- **CARAVEL** autonomous landing resupply vessel
  - Payload ~**23,000 lbs**; range ~**1,100 nm**
  - JMIC / ISO container compatible; self load/unload
  - **GPS-denied** navigation via sensor fusion + AI obstacle avoidance
  - Autonomous beach landing, bow-ramp discharge, redeploy — no port/shore crew
- Hybrid propulsion for multi-day contested missions
- Ukraine combat precedent cited for beach-landing drone craft (Kinburn Spit UGV delivery)

## Marine Data & Ops Needs
- Coastal bathymetry, reef/coral crest/rocky shore characterization for beachability
- Real-time sea state, surf-zone, current, and obstacle maps in littorals
- GPS-denied relative navigation (visual/radar/IMU/depth) datasets
- Distributed force logistics demand signals (tonnage/day across austere sites)
- Contested EW environment telemetry; blue-force tracking without exposing C2
- Manufacturing QA telemetry across US-Japan production lines

## Contacts
- https://bulwarkdynamics.com/
- contact@bulwarkdynamics.com
- CEO: Nhat Lieu
- Menlo Park, CA
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Bulwark Dynamics",
            "url": "https://bulwarkdynamics.com/",
            "description": "DefenseTech builder of CARAVEL autonomous beach-landing resupply USVs for contested Indo-Pacific logistics.",
            "sector": "Marine Monitoring & Sensors",
            "businessModel": "Defense prime-style vertically integrated autonomous maritime logistics (hull + autonomy + production partnership)",
            "lastFundingRound": "$6.8M seed (Sep 2026) with Onomichi Dockyard + VCs",
            "totalFunding": "At least $6.8M seed + prior pre-seed (Sep 2025); cumulative not fully disclosed",
            "investors": ["Onomichi Dockyard", "Undisclosed VCs"],
            "employee": [
                {"@type": "Person", "name": "Nhat Lieu", "jobTitle": "Co-founder & CEO"}
            ],
            "knowsAbout": [
                "Autonomous landing craft",
                "Contested maritime logistics",
                "GPS-denied navigation",
                "Distributed maritime operations",
                "USV manufacturing",
            ],
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Menlo Park",
                "addressRegion": "CA",
                "addressCountry": "US",
            },
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Littoral bathymetry and beachability maps",
                    "Sea state and surf-zone observations",
                    "GPS-denied navigation sensor suites",
                    "Logistics demand / force disposition data",
                ],
                "keyParameters": [
                    "water depth",
                    "surf height",
                    "current",
                    "obstacle maps",
                    "payload mass",
                    "endurance nm",
                ],
                "observationPrograms": [
                    "Prototype sea trials",
                    "Beach landing autonomy tests",
                    "Partner shipyard production telemetry",
                ],
                "knownGaps": [
                    "High-resolution coral/reef shelf charts for Pacific littorals",
                    "EW-resilient C2 datasets",
                    "Standardized attritable logistics USV performance benchmarks",
                ],
            },
        },
        "wiki_body": f"""# Bulwark Dynamics

**Sector**: Marine Monitoring & Sensors
**Official Site**: https://bulwarkdynamics.com/

## Overview
**Bulwark Dynamics** (Menlo Park, CA) builds **CARAVEL**, an **autonomous beach-landing resupply vessel** for contested Indo-Pacific logistics. Unlike patrol USVs or medium USVs optimized for sensing/strike, CARAVEL is a **landing-craft logistics drone**: ship-to-shore cargo without ports or shore crews, aimed at Expeditionary Advanced Base Operations (EABO) and distributed maritime operations where fixed infrastructure is targetable.

## Business Model
- **Vertically integrated** autonomy + hull production + payload + in-theater sustainment — not software-only autonomy retrofit
- **Japan industrial partnership**: **Onomichi Dockyard** is investor and production partner (FRP throughput near First Island Chain)
- Defense/allied customers; attritable shallow-draft connectors vs legacy LCU/LCAC cost and vulnerability
- Production capacity framed as primary KPI (hundreds of hulls/year ambition)

## Funding
- **$6.8M seed (Sep 2026)** with **Onomichi Dockyard** + VCs — prototype build/test
- Menlo Park prototype production facility (**Jan 2026**)
- Pre-seed (**Sep 2025**)
- CEO/co-founder **Nhat Lieu**

## Key Technology
- **CARAVEL**: ~**23,000 lb** payload; ~**1,100 nm** range; JMIC/ISO containers; autonomous beach, discharge, redeploy
- **GPS-denied** navigation (sensor fusion + AI obstacle avoidance)
- Hybrid endurance propulsion for multi-day contested missions
- Category: logistics landing USV (distinct from multi-class ASV primes and survey USVs)

## Data & Measurement Needs
- **Primary data types**: Littoral bathymetry/beachability; surf-zone and sea-state streams; GPS-denied nav suites (vision/radar/IMU/depth); logistics demand signals across austere sites; EW/contested-comms telemetry
- **Key measurements/parameters**: Depth, reef/coral crest geometry, surf height, currents, obstacles, payload mass/CG, endurance, autonomy mission success rates
- **Observation platforms/programs**: Prototype sea trials; beach-landing test ranges; US–Japan production QA telemetry
- **Known data gaps**: High-res Pacific littoral charts for coral/rocky shores; standardized benchmarks for attritable logistics USVs; resilient C2 datasets under jamming
- **Interest in external data services**: Ocean survey USV data layers ([HydroSurv](hydrosurv.md), [Saildrone](saildrone.md), [XOCEAN](xocean.md)); defense ASV peers ([Saronic Technologies](saronic-technologies.md), [Blue Water Autonomy](blue-water-autonomy.md), [Seasats](seasats.md)); coastal risk basemaps ([Coastal Risk & Infrastructure](coastal-risk-infrastructure.md))

## Cross-Sector Connections
- Extends **defense marine autonomy** cluster with a **logistics landing** niche vs multi-class combat USVs ([Saronic Technologies](saronic-technologies.md), [Blue Water Autonomy](blue-water-autonomy.md), [HavocAI](havocai.md))
- Complements survey-first USVs ([HydroSurv](hydrosurv.md), [Saildrone](saildrone.md)) — different mission (cargo vs data) but shared autonomy/nav stack needs
- Japan shipyard co-production echoes mass-production-first warship patterns ([Blue Water Autonomy](blue-water-autonomy.md))
- Sector home: [Marine Monitoring & Sensors](marine-monitoring-sensors.md)

---
**Cross-links**: [Marine Monitoring & Sensors](marine-monitoring-sensors.md) · [HydroSurv](hydrosurv.md) · [Saronic Technologies](saronic-technologies.md) · [Blue Water Autonomy](blue-water-autonomy.md) · [Saildrone](saildrone.md) · [Seasats](seasats.md)

*Last Updated: {DATE}*
""",
    },
    {
        "name": "Marcura",
        "url": "https://marcura.com/",
        "sector": "Maritime Operations & Analytics",
        "tag": "maritime-operations-analytics",
        "notes": (
            "Maritime voyage/vessel/crew operating system + AI on one of industry's largest transaction networks. "
            "Brands: DA-Desk (port-call spend), VesselMan, MarTrust, ShipServ (procurement marketplace, acquired ~2023-4), Brightwell. "
            "CEO Henrik Hyldahn (ex-ShipServ CEO; Marcura Group CEO post-acquisition). AI for charterparty review, document automation, "
            "demurrage claims, AP automation — augment specialists. Acquisitions: Fairway Maritime (US demurrage), Shipdem (chemical tanker laytime). "
            "Established scaled platform (not early seed); high ops-data network effects."
        ),
        "description": (
            "AI + specialist execution platform for voyage spend, vessel ops, crew payroll & demurrage; ShipServ/DA-Desk network; CEO Henrik Hyldahn."
        ),
        "raw": f"""# Marcura – Raw Web Extract
**Source:** https://marcura.com/
**Also:** https://maritime-executive.com/podcast/podcast-marcura-ceo-henrik-hyldahn-on-ai-for-modern-vessel-operations
**Extracted:** {DATE}

## Overview
Marcura is a scaled maritime technology and services group providing solutions across **voyage** (port-call management, demurrage/laytime, port services), **vessel** (marine procurement, AP automation, drydocking, husbandry), and **finance & compliance** (crew payroll, vendor payments, KYB). Operates brands including **DA-Desk**, **VesselMan**, **MarTrust**, **ShipServ** (marine procurement marketplace acquired ~2023-4), and **Brightwell**. Positions on "one of maritime's largest operational networks" and intelligence from millions of maritime transactions; combines **AI with specialist execution**.

## Business Model
- B2B SaaS + managed services for shipowners, charterers, traders, operators
- Network-effect data moat from port calls, payments, claims, procurement searches
- M&A roll-up of domain specialists (ShipServ, Fairway Maritime US demurrage assets, Shipdem chemical tanker laytime)
- AI strategy (CEO Henrik Hyldahn): automate document creation and charterparty inconsistency checks in minutes; humans validate high-stakes voyage outcomes; capture institutional knowledge

## Funding / Corporate
- Mature private group (exact latest equity round not disclosed on homepage extract)
- Leadership: **Henrik Hyldahn** Group CEO (ex-Coca-Cola/Carlsberg; ShipServ CEO 2020; Marcura CEO after ShipServ acquisition); Jens Lorens Poulsen moved to Board Chair in prior transition
- Scale signal: multi-brand platform spanning port spend, procurement marketplace, crew payments

## Key Technology
- Port-call cost intelligence and disbursement control (DA-Desk)
- Laytime & demurrage claims automation and recovery
- Marine procurement marketplace (ShipServ) + AP invoice matching
- Crew payroll / e-wallet / FX (MarTrust, Brightwell)
- Generative/document AI for charterparties and voyage paperwork with human-in-the-loop

## Marine Data & Ops Needs
- Structured port-call cost lines, tariffs, and vendor performance globally
- Charterparty / fixture / SOF / NOR document corpora for AI training and audit
- AIS/voyage actuals vs planned for demurrage and performance claims
- Procurement SKU/price intelligence across vessel opex categories
- Crew compliance, welfare, and payment rails data
- Interoperability with fleet OS, class, and insurer systems

## Contacts
- https://marcura.com/
- CEO: Henrik Hyldahn
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Marcura",
            "url": "https://marcura.com/",
            "description": "Maritime technology group combining AI and specialist execution for voyage spend, vessel ops, demurrage, procurement, and crew payments.",
            "sector": "Maritime Operations & Analytics",
            "businessModel": "B2B multi-brand maritime SaaS + managed services with transaction-network data moat and AI automation",
            "lastFundingRound": "Not disclosed on primary sources this cycle; growth via product AI + M&A (ShipServ, Fairway, Shipdem)",
            "totalFunding": "Not disclosed",
            "investors": [],
            "employee": [
                {"@type": "Person", "name": "Henrik Hyldahn", "jobTitle": "Group CEO"},
                {"@type": "Person", "name": "Jens Lorens Poulsen", "jobTitle": "Chair of the Board"},
            ],
            "knowsAbout": [
                "Port call management",
                "Demurrage and laytime",
                "Marine procurement",
                "Crew payroll",
                "Maritime AI document automation",
            ],
            "brand": [
                "DA-Desk",
                "VesselMan",
                "MarTrust",
                "ShipServ",
                "Brightwell",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Port-call cost and disbursement records",
                    "Charterparty and voyage document corpora",
                    "Procurement price/SKU transactions",
                    "Crew payment and compliance data",
                    "AIS/voyage actuals",
                ],
                "keyParameters": [
                    "port tariffs",
                    "laytime events",
                    "demurrage exposure",
                    "invoice line items",
                    "vendor KYB status",
                ],
                "observationPrograms": [
                    "Global port-call network (DA-Desk)",
                    "ShipServ marketplace search/order graph",
                    "Claims processing pipelines",
                ],
                "knownGaps": [
                    "Standardized cross-carrier voyage event schemas",
                    "Ground-truth labels for charterparty clause risk",
                    "Integration with onboard fleet behavioral AI",
                ],
            },
        },
        "wiki_body": f"""# Marcura

**Sector**: Maritime Operations & Analytics
**Official Site**: https://marcura.com/

## Overview
**Marcura** is a scaled maritime technology group that closes cost and compliance gaps across **every port call, purchase, and payment**. It combines multi-brand specialist products — **DA-Desk** (port-call spend), **ShipServ** (procurement marketplace), **VesselMan**, **MarTrust**, **Brightwell** — with **AI + human specialist execution** on top of millions of maritime transactions. Group CEO **Henrik Hyldahn** (ex-ShipServ) frames AI as automation of paperwork and charterparty checks so professionals focus on high-stakes voyage decisions.

## Business Model
- **B2B SaaS + managed services** for owners, charterers, traders, operators
- **Network-effect data moat**: port calls, claims, payments, buyer searches
- **M&A expansion**: ShipServ acquisition; Fairway Maritime (US demurrage); Shipdem (chemical tanker laytime)
- AI GTM: minutes-scale document generation and inconsistency detection; human validation remains mandatory for voyage risk

## Funding
- Mature private platform; **latest equity round not disclosed** on primary public pages this cycle
- Growth evidenced by brand consolidation, AI product push, and bolt-on claims specialists rather than a single seed/Series headline

## Key Technology
- Port-call cost intelligence & disbursements (DA-Desk)
- Laytime/demurrage claim construction and recovery
- Marine procurement marketplace + AP invoice automation (ShipServ)
- Crew payroll, e-wallet, FX rails
- Document/charterparty AI with human-in-the-loop controls

## Data & Measurement Needs
- **Primary data types**: Global port-call cost lines; charterparty/SOF/NOR corpora; procurement SKU/price graphs; crew payment/compliance; AIS and voyage actuals vs plan
- **Key measurements/parameters**: Tariffs and surcharge variance; laytime events; demurrage exposure; invoice match rates; vendor KYB; workflow automation %
- **Observation platforms/programs**: DA-Desk port-call network; ShipServ marketplace graph; claims pipelines; multi-brand transaction lake
- **Known data gaps**: Cross-carrier standardized voyage event schemas; labeled charterparty risk clauses for AI; deep integration with onboard fleet behavioral/CV systems
- **Interest in external data services**: Fleet ops AI ([ShipIn Systems](shipin-systems.md), [Orca AI](orca-ai.md)); voyage weather/ocean routing ([Ocean Intelligence](ocean-intelligence.md), [Sofar Ocean](sofar-ocean.md)); compliance/GEOINT overlays ([Unseenlabs](unseenlabs.md))

## Cross-Sector Connections
- Complements **fleet behavioral AI** ([ShipIn Systems](shipin-systems.md)) and **bridge CV** ([Orca AI](orca-ai.md), [SEA.AI](seaai.md)) with **commercial voyage/spend OS**
- Distinct from pure vessel autonomy ([Sea Machines Robotics](sea-machines-robotics.md)) — Marcura owns transactions and claims, not helm control
- Sector home: [Maritime Operations & Analytics](maritime-operations-analytics.md)

---
**Cross-links**: [Maritime Operations & Analytics](maritime-operations-analytics.md) · [ShipIn Systems](shipin-systems.md) · [Orca AI](orca-ai.md) · [Sea Machines Robotics](sea-machines-robotics.md) · [Ocean Intelligence](ocean-intelligence.md)

*Last Updated: {DATE}*
""",
    },
    {
        "name": "HydroSurv",
        "url": "https://www.hydro-surv.com/",
        "sector": "Marine Monitoring & Sensors",
        "tag": "marine-monitoring-sensors",
        "notes": (
            "UK commercial USV OEM (Exeter) — REAV family (REAV-60 long endurance through REAV-25 inland). "
            "OWGP Development Funding for next-gen USV-first 3D sub-bottom profiler with GeoAcoustics + Tellus; Ocean Winds guidance; "
            "on-water trials targeted Oct 2026 on REAV-45 (UK MiniMASS MGN 705). First four REAV-47s in commercial service EU/West Africa 2025. "
            "Hike Metal Canada/US tech license; Subsea Fenix Italy delivery; Subnero underwater comms collab; BeyonC REAV-60+ROV Norway subsea survey. "
            "Founder/CEO David Hull; NED Mark Burnett. Commercial survey supply-chain focus (not defense-first)."
        ),
        "description": (
            "UK REAV USV OEM for hydrographic/geophysical survey; OWGP-funded USV-first 3D SBP with GeoAcoustics; global commercial deployments."
        ),
        "raw": f"""# HydroSurv – Raw Web Extract
**Source:** https://www.hydro-surv.com/
**Also:** https://www.hydro-surv.com/our-story/
**Also:** https://www.hydro-surv.com/news-case-studies/
**Also:** https://www.hydro-international.com/news/funding-boost-for-hydrosurv-s-next-generation-usv-first-3d-sbp-system
**Extracted:** {DATE}

## Overview
HydroSurv Unmanned Survey (UK) Ltd (Exeter) designs and delivers **Rapid Environmental Assessment Vessels (REAVs)** — commercial uncrewed surface vessels for hydrographic, geophysical, and oceanographic survey. Founded from a garage in **2018** to make affordable, workboat-standard USVs for commercial users (not only defense primes). Product line spans **REAV-60** (long endurance), **REAV-47/45** (nearshore; REAV-45 UK MiniMASS MGN 705 aligned), and inland **REAV-35/28/25**, plus customization, training, and support.

## Business Model
- USV hardware sales + customization + training/qualifications + technical support
- Technology licensing for regional manufacture (e.g., **Hike Metal** Canada/US agreement to manufacture/market/support full REAV portfolio)
- Integrated survey packages with sensor partners (Teledyne multibeam; GeoAcoustics SBP; Subnero underwater comms; BeyonC USV-ROV)
- Serves survey contractors and offshore wind developers needing lower-cost, lower-risk data collection

## Funding / Programs
- **Offshore Wind Growth Partnership (OWGP) Development Funding** (announced context Dec 2025 / active through 2026): next-generation **3D sub-bottom profiling** system built USV-first with **GeoAcoustics** and **Tellus Geoconsulting**; strategic guidance from **Ocean Winds**; follows 1st-place KTN Innovation Exchange geophysical survey win (2025)
- Field trials scheduled **October 2026** on REAV-45
- Commercial traction: first four **REAV-47** platforms delivered 2025 into routine service across **Europe and West Africa**
- Board: NED **Mark Burnett** appointed; Founder/CEO **David Hull**

## Key Technology
- REAV battery-hybrid USV family for inland to long-endurance nearshore/offshore survey
- USV-first **3D SBP**: multi-frequency architecture on GeoAcoustics GeoPulse 2; novel hydrophone arrangement + deploy/recover system for volumetric shallow sub-seafloor imaging (boulders, shallow gas, faults, UXO) for foundation and cable-route engineering
- Multibeam and ROV-capable configurations (Subsea Fenix Italy 5.7m hybrid USV delivery)
- Persistent ocean monitoring collab with Subnero underwater wireless networking

## Marine Data & Ops Needs
- High-resolution bathymetry and backscatter
- 3D sub-bottom / shallow geology volumes for OSW foundations and cables
- UXO and geohazard indicators; landfall/coastal survey in high-energy zones
- USV nav, endurance, sea-state operability envelopes; MiniMASS compliance evidence
- Multi-sensor timed data products (MBES + SBP + oceanographic)
- Customer fleet utilization and remote ops center telemetry

## Contacts
- https://www.hydro-surv.com/
- info@hydro-surv.com
- +44 (0) 333 772 9306
- Unit 5 Jardine Park, Bradman Way, Grace Road West, Marsh Barton, Exeter EX2 8PE, UK
- CEO: David Hull
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "HydroSurv",
            "legalName": "HydroSurv Unmanned Survey (UK) Ltd",
            "url": "https://www.hydro-surv.com/",
            "description": "UK commercial USV OEM (REAV family) for hydrographic and geophysical survey, advancing USV-first 3D sub-bottom profiling for offshore wind.",
            "sector": "Marine Monitoring & Sensors",
            "foundingDate": "2018",
            "businessModel": "USV hardware sales, customization, training, tech licensing, and integrated survey payloads for commercial survey supply chain",
            "lastFundingRound": "OWGP Development Funding for USV-first 3D SBP (with GeoAcoustics, Tellus; Ocean Winds guidance); equity totals not disclosed",
            "totalFunding": "Not fully disclosed (program grant + commercial revenue)",
            "investors": [
                "Offshore Wind Growth Partnership (OWGP Development Funding Programme)"
            ],
            "employee": [
                {"@type": "Person", "name": "David Hull", "jobTitle": "Founder & CEO"},
                {"@type": "Person", "name": "Mark Burnett", "jobTitle": "Non-Executive Director"},
            ],
            "knowsAbout": [
                "Uncrewed surface vessels",
                "Hydrographic survey",
                "Sub-bottom profiling",
                "Offshore wind geophysics",
                "USV training and MiniMASS compliance",
            ],
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Exeter",
                "addressCountry": "GB",
            },
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Multibeam bathymetry",
                    "3D sub-bottom volumes",
                    "Oceanographic casts",
                    "USV navigation and sea-state logs",
                ],
                "keyParameters": [
                    "depth",
                    "backscatter",
                    "sub-seafloor reflectivity",
                    "shallow gas indicators",
                    "boulder/UXO contacts",
                    "cable route geology",
                ],
                "observationPrograms": [
                    "Commercial REAV fleet ops EU/West Africa",
                    "OWGP 3D SBP field trials (Oct 2026 target)",
                    "Partner ROV/USV integrated missions",
                ],
                "knownGaps": [
                    "USV-motion-compensated 3D SBP validation datasets",
                    "Landfall survey benchmarks vs towed systems",
                    "Cross-OEM payload interface standards",
                ],
            },
        },
        "wiki_body": f"""# HydroSurv

**Sector**: Marine Monitoring & Sensors
**Official Site**: https://www.hydro-surv.com/

## Overview
**HydroSurv** (Exeter, UK; founded **2018**) builds the **REAV** family of commercial **uncrewed surface vessels** for hydrographic, geophysical, and oceanographic survey. The company targets the **survey supply chain** and offshore wind developers with affordable, workboat-standard USVs — inland **REAV-25/28/35**, nearshore **REAV-45/47**, and long-endurance **REAV-60** — plus training, support, and regional manufacturing licenses.

## Business Model
- **USV OEM sales** + customization + training/qualifications + technical support
- **Tech licensing**: e.g. **Hike Metal** (Canada) to manufacture/market/support REAVs across Canada/US
- Integrated payloads with sensor partners (**Teledyne**, **GeoAcoustics**, **Subnero**, **BeyonC** ROV packages)
- Commercial contractor deployments (e.g. **Subsea Fenix** Italy) rather than defense-first GTM

## Funding
- **OWGP Development Funding** for USV-first **3D sub-bottom profiler** with **GeoAcoustics** + **Tellus Geoconsulting**; guidance from **Ocean Winds**; follows KTN Innovation Exchange 1st place (2025)
- On-water validation targeted **Oct 2026** on **REAV-45** (UK **MGN 705 MiniMASS**-aligned)
- Equity totals not disclosed; commercial signal: first four **REAV-47** units in routine EU/West Africa service (2025)
- Leadership: Founder/CEO **David Hull**; NED **Mark Burnett**

## Key Technology
- Battery-hybrid **REAV** USV portfolio spanning inland to long-endurance missions
- Next-gen **3D SBP** on GeoPulse 2 architecture: novel hydrophone array + deploy/recover for volumetric shallow geology (gas, boulders, faults, UXO) supporting OSW foundations and cable routes
- Multibeam and USV-ROV integrated configurations
- Underwater wireless collaboration (**Subnero**) for persistent monitoring concepts

## Data & Measurement Needs
- **Primary data types**: MBES bathymetry/backscatter; 3D sub-bottom volumes; oceanographic time series; USV nav/sea-state operability logs; landfall/coastal corridor surveys
- **Key measurements/parameters**: Depth, reflectivity, shallow-gas indicators, boulder/UXO contacts, sediment layering for foundations/cables, endurance and motion limits
- **Observation platforms/programs**: Global REAV commercial fleet; OWGP 3D SBP trials (2026); partner contractor missions (Italy, Canada license build-out, Norway REAV-60+ROV)
- **Known data gaps**: Motion-compensated USV 3D SBP validation libraries; quantified cost/quality vs towed SBP at landfalls; standard payload interfaces across USV OEMs
- **Interest in external data services**: OSW metocean & bird/bat layers ([Spoor](spoor.md)); ocean data platforms ([XOCEAN](xocean.md), [Saildrone](saildrone.md), [Sofar Ocean](sofar-ocean.md)); defense logistics USVs are adjacent but different mission ([Bulwark Dynamics](bulwark-dynamics.md))

## Cross-Sector Connections
- **Commercial survey USV** complement to defense ASV primes ([Saronic Technologies](saronic-technologies.md), [Blue Water Autonomy](blue-water-autonomy.md), [Bulwark Dynamics](bulwark-dynamics.md))
- Enables [Offshore Energy](offshore-energy.md) geophysical derisking for foundations/cables
- Pairs with ocean data marketplaces and long-endurance platforms ([XOCEAN](xocean.md), [Saildrone](saildrone.md))
- Sector home: [Marine Monitoring & Sensors](marine-monitoring-sensors.md)

---
**Cross-links**: [Marine Monitoring & Sensors](marine-monitoring-sensors.md) · [Bulwark Dynamics](bulwark-dynamics.md) · [Saildrone](saildrone.md) · [XOCEAN](xocean.md) · [Offshore Energy](offshore-energy.md) · [Spoor](spoor.md)

*Last Updated: {DATE}*
""",
    },
]


def write_profiles():
    sources_path = os.path.join(REPO, "sources", "companies.json")
    with open(sources_path) as f:
        companies = json.load(f)
    existing = {c["name"].lower() for c in companies}

    for c in COMPANIES:
        slug = slugify(c["name"])
        print(f"Writing {c['name']} -> {slug}")

        raw_path = os.path.join(REPO, "raw", f"{slug}.md")
        with open(raw_path, "w") as f:
            f.write(c["raw"].rstrip() + "\n")

        meta_path = os.path.join(REPO, "metadata", f"{slug}.jsonld")
        with open(meta_path, "w") as f:
            json.dump(c["metadata"], f, indent=2)
            f.write("\n")

        desc = c["description"].replace("\n", " ").strip()
        if len(desc) > 220:
            desc = desc[:217] + "..."
        wiki = (
            "---\n"
            f"type: Company\n"
            f"title: {c['name']}\n"
            f"description: {desc}\n"
            f"resource: {c['url']}\n"
            f"tags:\n"
            f"- {c['tag']}\n"
            f"timestamp: '{TS}'\n"
            f"date: '{DATE}'\n"
            f"sector: {c['sector']}\n"
            f"---\n\n"
            f"{c['wiki_body'].lstrip()}"
        )
        wiki_path = os.path.join(REPO, "wiki", f"{slug}.md")
        with open(wiki_path, "w") as f:
            f.write(wiki if wiki.endswith("\n") else wiki + "\n")

        if c["name"].lower() not in existing:
            companies.append(
                {
                    "sector": c["sector"],
                    "name": c["name"],
                    "url": c["url"],
                    "notes": c["notes"],
                    "last_updated": DATE,
                }
            )
            existing.add(c["name"].lower())
        else:
            print("  (already in companies.json)")

    with open(sources_path, "w") as f:
        json.dump(companies, f, indent=2)
        f.write("\n")
    print(f"companies.json now has {len(companies)} entries")


if __name__ == "__main__":
    write_profiles()
