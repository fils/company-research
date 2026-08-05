#!/usr/bin/env python3
"""Generate profiles for 2026-08-05 autonomous run — 4 new high-signal companies."""
import json, os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = "2026-08-05"
TS = "2026-08-05T00:00:00Z"


def slugify(name):
    slug = name.lower()
    slug = slug.replace("ø", "o").replace("æ", "ae").replace("å", "a")
    slug = slug.replace("ü", "u").replace("é", "e").replace("è", "e")
    slug = re.sub(r"[^a-z0-9-]", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def sector_tag(sector):
    return slugify(sector)


def wiki_page(name, url, sector, body, description):
    tag = sector_tag(sector)
    return f"""---
type: Company
title: {name}
description: {description}
resource: {url}
tags:
- {tag}
timestamp: '{TS}'
date: '{TODAY}'
sector: {sector}
---

# {name}

**Sector**: {sector}
**Official Site**: {url}

{body.rstrip()}

*Last Updated: {TODAY}*
"""


COMPANIES = [
    {
        "name": "WSense",
        "url": "https://wsense.it/",
        "sector": "Marine Monitoring & Sensors",
        "notes": (
            "Italian Internet of Underwater Things (IoUT) deep-tech: patented multi-modal underwater wireless "
            "communications (acoustic/optical) + mesh networking enabling real-time high-density ocean data from "
            "multi-vendor sensors/AUVs/ASVs. Products: W·Node, W·Node Enhanced (deep + onboard AI), W·Mesh, "
            "W·Gateway, W·Edge, W·Cloud, W·Micro. €10M pre-Series B (Oct 2025) Indico Capital + SIMEST; prior "
            "€7.2M bridge (Apr 2025) and €9–11M Series A (SWEN Blue Ocean et al.); total funding >€25–29M. "
            "Investors: CDP Venture Capital, SWEN Blue Ocean, RunwayFBU, Axon, Fincantieri, Rypples, Indico, SIMEST. "
            "Partners: Fincantieri DEEP, Hub Ocean MoU, Terna. Use cases: smart cables/pipelines, asset integrity, "
            "defense AUV swarms, offshore energy, CCS, MPAs, seismic. CEO Chiara Petrioli (Sapienza). HQ Rome; "
            "offices Bergen, London; 80+ engineers. Contact: wsense@wsense.it."
        ),
        "description": "Internet of Underwater Things — underwater wireless mesh IoUT; >€25M raised; Fincantieri partner.",
        "raw": f"""# WSense – Raw Web Extract
**Source:** https://wsense.it/
**Also:** https://tech.eu/2025/10/23/wsense-raises-10m-to-scale-subsea-wi-fi-and-expand-underwater-iot-tech/
**Extracted:** {TODAY}

## Overview
WSense (Rome, Italy; founded 2017) builds the Internet of Underwater Things (IoUT) — end-to-end multi-modal secure wireless communications and networking among submerged and surface sensing and robotic platforms. Mission: enable large-scale, high-density, continuous real-time ocean data collection while caring for marine ecosystems. CEO Chiara Petrioli (Professor of Computer Engineering, Sapienza University of Rome; CEO since 2022). 80+ engineers/researchers; offices Italy, Norway (Bergen), UK (London); staff in France and UAE.

## Business Model
- Hardware + software IoUT platform sales and deployments for blue-economy operators
- End-to-end stack: underwater multi-sensor nodes, mesh networking, gateways, edge apps, cloud/API layer
- Markets: critical infrastructure (cables/pipelines), asset integrity, defense/AUV swarms, offshore energy, carbon capture & storage monitoring, marine protected areas, seismic/volcanic events
- Strategic OEM/integration partnerships (e.g. Fincantieri DEEP system integration)

## Funding
- **€10M pre-Series B** (Oct 2025) — new investors Indico Capital Partners, SIMEST; existing CDP Venture Capital, Blue Ocean by SWEN, RunwayFBU, Axon Partners Group, Fincantieri, Rypples
- Prior: €7.2M pre-Series B bridge (Apr 2025); Series A ~€9–11M (SWEN Blue Ocean et al. 2023)
- **Total funding: >€25M** (Tracxn ~$29.3M)
- Use of proceeds: scale subsea Wi-Fi / IoUT internationally for energy transition, infrastructure security, ocean protection

## Key Technology
- Patented multi-protocol underwater wireless mesh (acoustic + optical modalities)
- W·Node (shallow multi-sensor + acoustic modem); W·Node Enhanced (deep water + onboard AI)
- W·Mesh (reliability, interoperability, security-by-design networking)
- W·Gateway (underwater ↔ terrestrial bridge); W·Edge; W·Cloud (open data + API library)
- W·Micro miniaturized modem for small drones/divers; general-purpose real-time underwater module
- Multi-vendor interoperability across sensors and ASV/AUV fleets; multi-hop long-area monitoring

## Partners / Proof points
- Fincantieri integrates WSense into DEEP system; safer maritime infrastructures agreement
- Hub Ocean MoU for ocean sustainability and data sharing
- Terna (Italian TSO) IoUT collaboration for underwater infrastructure
- WEF Ocean Data Challenge winner (2023)

## Contacts
- HQ: Corso d'Italia 39, 00198 Rome, Italy
- Bergen: Thormøhlensgate 51, 5006 Bergen, Norway
- London: Norvin House, 45-55 Commercial Street, E1 6BD
- Email: wsense@wsense.it

## Marine Data Needs
- Underwater acoustic/optical channel characterization; multi-vendor sensor streams; AUV/ASV telemetry; cable/pipeline integrity telemetry; CCS leakage monitoring; MPA biodiversity baselines
""",
        "body": """## Overview
**WSense** (Rome; founded 2017) builds the **Internet of Underwater Things (IoUT)** — patented multi-modal underwater wireless communications and mesh networking that let multi-vendor sensors, AUVs, and ASVs exchange data in real time at scale. CEO **Chiara Petrioli** (Sapienza University). **>€25M** raised including a **€10M pre-Series B** (Oct 2025). Strategic partners include **Fincantieri**, **Hub Ocean**, and **Terna**.

## Business Model
- Sell/deploy end-to-end IoUT stack (nodes, mesh, gateway, edge, cloud/API) to energy, defense, infrastructure, and ocean-protection operators
- Integration partnerships with shipbuilders and TSOs (Fincantieri DEEP; Terna)
- Moat: patents on multi-protocol underwater mesh + multi-vendor interoperability + multi-hop long-area coverage

## Funding
| Round | Amount | Date | Notes |
|-------|--------|------|-------|
| Series A | ~€9–11M | ~2023 | SWEN Blue Ocean, CDP, Axon, Katapult Ocean et al. |
| Pre-B bridge | €7.2M | Apr 2025 | Existing Series A investors |
| Pre-Series B | **€10M** | Oct 2025 | **Indico Capital**, **SIMEST** join; total **>€25M** |

## Key Technology
- Acoustic + optical multi-modal underwater wireless; W·Node / W·Node Enhanced (deep + onboard AI)
- W·Mesh patented multi-protocol networking; W·Gateway surface bridge; W·Cloud open-data APIs
- W·Micro for small drones/divers; multi-hop mesh across multi-vendor AUV/ASV fleets

## Data & Measurement Needs
- **Primary data types**: Underwater acoustic/optical comms telemetry, multi-sensor node streams, AUV/ASV swarm C2, cable/pipeline integrity, CCS site monitoring, MPA biodiversity
- **Key measurements/parameters**: Acoustic channel quality, packet reliability, node localization, depth, temperature, integrity strain/leak indicators, biodiversity proxies
- **Observation platforms/programs**: W·Node networks, AUV/ASV fleets, smart cable/pipeline routes, offshore wind/CCS sites, Fincantieri DEEP integrations
- **Known data gaps**: Standardized multi-vendor underwater protocol interoperability at basin scale; labeled CCS leakage signatures; long-range shallow/noisy channel models
- **Interest in external data services**: Hub Ocean data sharing, satellite cueing for surface assets, offshore energy digital twins, navy/MDA underwater situational layers

## Cross-Sector Connections
- Complements AUV/USV primes ([Saildrone](saildrone.md), [Kraken Technology](kraken-technology.md), [Saronic Technologies](saronic-technologies.md)) with the **comms fabric** they need underwater
- Enables MRV telemetry for [Ocean Carbon Sequestration](ocean-carbon-sequestration.md) CCS/mCDR sites and [Offshore Energy](offshore-energy.md) asset integrity
- Data layer pairs with [Ocean Data & AI](ocean-data-ai.md) platforms (Sofar, XOCEAN, Hub Ocean MoU)
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "WSense",
            "legalName": "WSense S.r.l.",
            "url": "https://wsense.it/",
            "description": "Internet of Underwater Things platform — multi-modal underwater wireless mesh networking for real-time ocean data from multi-vendor sensors and autonomous vehicles.",
            "foundingDate": "2017",
            "founder": {"@type": "Person", "name": "Chiara Petrioli", "jobTitle": "CEO"},
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Corso d'Italia 39",
                "addressLocality": "Rome",
                "postalCode": "00198",
                "addressCountry": "IT",
            },
            "email": "wsense@wsense.it",
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "EUR",
                "value": 25000000,
                "description": ">€25M total incl. €10M pre-Series B (Oct 2025)",
            },
            "sector": "Marine Monitoring & Sensors",
            "businessModel": "IoUT hardware+software platform sales and integrations for critical marine infrastructure, defense, offshore energy, CCS, and MPAs",
            "lastFundingRound": "€10M pre-Series B (Oct 2025) — Indico Capital, SIMEST + existing",
            "totalFunding": ">€25M",
            "investors": [
                "Indico Capital Partners",
                "SIMEST",
                "CDP Venture Capital",
                "SWEN Blue Ocean",
                "RunwayFBU",
                "Axon Partners Group",
                "Fincantieri",
                "Rypples",
                "Katapult Ocean",
            ],
            "knowsAbout": [
                "Internet of Underwater Things",
                "Underwater wireless communications",
                "Acoustic and optical mesh networking",
                "AUV swarm communications",
                "Subsea infrastructure monitoring",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Underwater acoustic/optical telemetry",
                    "Multi-sensor node streams",
                    "AUV/ASV C2",
                    "Cable/pipeline integrity",
                    "CCS monitoring",
                ],
                "keyMeasurements": [
                    "Channel quality",
                    "Packet reliability",
                    "Node localization",
                    "Integrity/leak indicators",
                    "Depth and temperature",
                ],
                "observationPlatforms": [
                    "W·Node networks",
                    "Multi-vendor AUV/ASV fleets",
                    "Smart cable routes",
                    "Fincantieri DEEP",
                ],
                "knownGaps": [
                    "Basin-scale multi-vendor protocol standards",
                    "Labeled CCS leakage signatures",
                ],
                "interestInExternalDataServices": "Hub Ocean sharing, satellite surface cueing, offshore digital twins, MDA underwater layers",
            },
        },
    },
    {
        "name": "Ace Aquatec",
        "url": "https://aceaquatec.com/",
        "sector": "Aquaculture",
        "notes": (
            "Scotland welfare-first aquaculture tech: AI biomass/health cameras (multi-species individual tracking, "
            "wound/maturation detection), in-water electric humane stunners, emerging sea lice removal systems. "
            "£10M (~$11.3–13.9M) oversubscribed round (May 2025) led by Stolt Ventures with Scottish Enterprise and "
            "Aqua-Spark (£7.5M equity + £2.5M debt); total raised ~$23.4M (PitchBook). CEO Nathan Pyne-Carter; "
            "CFO Alan MacLeod; board Axel de Mégille (Stolt Ventures). Offices Dundee, Glasgow, Chile. Partners: "
            "JBT Marel preferred provider, Shrimp Welfare Project portable stunner. AI + sensors for full fish "
            "lifecycle welfare from cage to harvest. Contact via aceaquatec.com."
        ),
        "description": "Welfare-first aqua AI cameras + humane stunners — £10M Stolt Ventures round; ~$23M total.",
        "raw": f"""# Ace Aquatec – Raw Web Extract
**Source:** https://aceaquatec.com/
**Also:** https://aceaquatec.com/news-and-resources/news/ace-aquatec-secures-pound-10m-investment-accelerate-growth-and-expand-its-digital-technologies-internationally
**Also:** https://www.seafoodsource.com/news/business-finance/stolt-ventures-leads-usd-11-3-million-funding-round-for-ace-aquatec
**Extracted:** {TODAY}

## Overview
Ace Aquatec (Dundee, Scotland) is a welfare-first aquaculture technology company designing products across the full fish lifecycle: AI underwater biomass/health cameras and award-winning in-water electric humane stunners for farmed and wild fish. Expanding into sea lice removal systems using the same tech stack. CEO Nathan Pyne-Carter. Offices in Dundee, Glasgow, and Chile; global footprint (26 countries cited in SDI materials).

## Business Model
- Hardware + AI software for fish farmers: biomass cameras, health detection, individual tracking, humane slaughter systems
- Data-driven insights that improve welfare and farm profitability
- Strategic OEM/channel partnerships (JBT Marel preferred provider; Shrimp Welfare Project portable stunner)
- Expansion focus: Scotland + Chile/South America; AI talent hiring

## Funding
- **£10M investment round** (May 2025, announced 1 May) — oversubscribed; led by **Stolt Ventures** (Stolt-Nielsen); Scottish Enterprise; Aqua-Spark
- Structure: £7.5M equity + £2.5M debt facility (~USD 11.3M)
- PitchBook: later-stage VC / Series B ~$13.9M (21 May 2025 listing); **total funding ~$23.4M**; 16 investors
- Use of proceeds: 15 new roles (AI/sensors/ML) in Dundee, Glasgow, Chile; deepen data capabilities; commercialise sea lice systems
- Board: Axel de Mégille (Head of Stolt Ventures) joined as NED

## Key Technology
- AI cameras: non-invasive weight tracking, wound/maturation health detection, multi-species individual tracking
- In-water electric humane stunners (award-winning; farmed + wild)
- Sea lice removal systems in commercialisation pipeline (same tech family)
- Sensors + cameras + ML algorithms for real-time welfare insights cage-to-harvest

## Partners
- Stolt Ventures / Stolt Sea Farm strategic fit
- Aqua-Spark long-term shareholder
- JBT Marel strategic partnership (preferred provider)
- Shrimp Welfare Project portable in-water stunner

## Marine Data Needs
- Underwater video streams, biomass estimates, individual fish IDs, welfare/health labels, water quality context, sea lice counts, harvest process telemetry
""",
        "body": """## Overview
**Ace Aquatec** (Dundee, Scotland) is a **welfare-first aquaculture technology** company spanning AI underwater biomass/health cameras and award-winning **in-water electric humane stunners**, with sea lice removal systems entering commercialisation. CEO **Nathan Pyne-Carter**. Raised an oversubscribed **£10M** round led by **Stolt Ventures** (May 2025); PitchBook total funding **~$23.4M**.

## Business Model
- Sell AI camera systems + humane slaughter hardware into global fish farming
- Real-time data insights that improve welfare and operational performance
- Channel/OEM scale via **JBT Marel** preferred-provider partnership; shrimp welfare portable stunner with Shrimp Welfare Project
- Distinct angle: **welfare-first** full lifecycle (cage → harvest) vs pure biomass-CV peers

## Funding
| Round | Amount | Date | Notes |
|-------|--------|------|-------|
| Growth / Series B | **£10M** (~$11.3–13.9M) | May 2025 | **Stolt Ventures** lead; Scottish Enterprise; Aqua-Spark; £7.5M equity + £2.5M debt |
| **Total** | **~$23.4M** | | PitchBook; 16 investors |

## Key Technology
- AI cameras: non-invasive weights, wound/maturation detection, multi-species individual tracking
- In-water electric humane stunners (farmed + wild)
- Sea lice removal systems (commercialisation pipeline)
- Sensors + ML for cage-to-harvest welfare optimisation

## Data & Measurement Needs
- **Primary data types**: Underwater video, biomass estimates, individual fish tracks, welfare/health event labels, sea lice counts, harvest stun telemetry, farm environmental context
- **Key measurements/parameters**: Weight distributions, wound incidence, maturation signals, lice load, DO/temp/salinity co-variates, stun efficacy metrics
- **Observation platforms/programs**: Cage-mounted AI cameras, harvest-line stunners, multi-site deployments (Scotland, Chile, 26-country footprint)
- **Known data gaps**: Cross-species labeled welfare corpora; standardized lice-load ground truth at night/turbid conditions; RAS vs sea-cage domain transfer
- **Interest in external data services**: Farm environmental sensor feeds, satellite SST/bloom alerts, veterinary disease databases, insurer loss datasets

## Cross-Sector Connections
- Complements [Aquabyte](aquabyte.md), [Tidal](tidal.md), [NeuralX](neuralx.md), [Biosort](biosort.md) CV/AI stack with **welfare + humane harvest** hardware differentiation
- Sea lice pipeline overlaps [Biosort](biosort.md) individual FishID control thesis
- [BiOceanOr](bioceanor.md) water-quality forecasts are natural upstream inputs to Ace welfare models
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Ace Aquatec",
            "url": "https://aceaquatec.com/",
            "description": "Welfare-first aquaculture technology: AI biomass and health cameras plus in-water electric humane stunners and emerging sea lice systems.",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Dundee",
                "addressCountry": "GB",
            },
            "founder": {"@type": "Person", "name": "Nathan Pyne-Carter", "jobTitle": "CEO"},
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "GBP",
                "value": 10000000,
                "description": "£10M May 2025 Stolt Ventures-led round; ~$23.4M total funding",
            },
            "sector": "Aquaculture",
            "businessModel": "AI camera + humane stunner hardware/software sales to global fish farmers; OEM partnerships (JBT Marel)",
            "lastFundingRound": "£10M oversubscribed (May 2025) led by Stolt Ventures; Scottish Enterprise; Aqua-Spark",
            "totalFunding": "~$23.4M",
            "investors": [
                "Stolt Ventures",
                "Scottish Enterprise",
                "Aqua-Spark",
                "Seabird Ventures",
            ],
            "knowsAbout": [
                "Aquaculture AI computer vision",
                "Fish welfare monitoring",
                "Humane electric stunning",
                "Sea lice control systems",
                "Biomass estimation",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Underwater video",
                    "Biomass estimates",
                    "Individual fish tracks",
                    "Welfare/health labels",
                    "Sea lice counts",
                ],
                "keyMeasurements": [
                    "Weight distribution",
                    "Wound incidence",
                    "Maturation",
                    "Lice load",
                    "Stun efficacy",
                    "DO/temp/salinity",
                ],
                "observationPlatforms": [
                    "Cage AI cameras",
                    "Harvest stunners",
                    "Multi-country farm deployments",
                ],
                "knownGaps": [
                    "Cross-species welfare label corpora",
                    "Turbid/night lice ground truth",
                ],
                "interestInExternalDataServices": "Farm environmental feeds, SST/bloom alerts, disease databases, insurer loss data",
            },
        },
    },
    {
        "name": "CREW Carbon",
        "url": "https://crewcarbon.com/",
        "sector": "Ocean Carbon Sequestration",
        "notes": (
            "Yale Carbon Containment Lab spinout (2022): wastewater process intensification via smart-dosing of "
            "alkaline minerals (e.g. calcium carbonate) that improves WWTP performance AND permanently removes CO2 "
            "as bicarbonate — asset-light CDR on existing industrial/municipal infrastructure. $25M oversubscribed "
            "Series A (14 May 2026): $19M equity + $6M grants/non-dilutive; led by Burnt Island Ventures; AP Ventures, "
            "Sony Innovation Fund, Builders Vision, Kibo Invest, Idemitsu Ventures, New York Ventures + existing "
            "Counteract, ANIMO, Connecticut Innovations, Ponderosa, Echo River. Prior $5.3M seed; $2.35M Colorado "
            "Energy Office award (Feb 2026). ~10 WWTP deployments US/Europe (HRSD); $33M+ CDR offtakes (JP Morgan, "
            "Google, Autodesk, Stripe via Frontier); 2,000+ tCO2 removed. Proprietary MRV. HQ Brooklyn NY / New Haven CT. "
            "Contact: hello@crewcarbon.com / clare.bennett@crewcarbon.com."
        ),
        "description": "Wastewater alkalinity CDR + process intensification — $25M Series A (May 2026); $33M+ offtakes.",
        "raw": f"""# CREW Carbon – Raw Web Extract
**Source:** https://crewcarbon.com/
**Also:** https://crewcarbon.com/crew-raises-25m-of-funding-to-scale-wastewater-treatment-optimization-technology-as-climate-solution/
**Extracted:** {TODAY}

## Overview
CREW Carbon, Inc. (Brooklyn, NY / New Haven, CT) is a water-tech + CDR company spun out of Yale University's Carbon Containment Lab (founded 2022). Patented process uses smart-dosing of strategically sourced alkaline minerals (e.g. calcium carbonate) into wastewater treatment to optimize pH/alkalinity — improving pollutant removal, settleability, and capacity while permanently converting CO2 into dissolved bicarbonate for durable storage when effluent reaches receiving waters.

## Business Model
- Dual value: (1) sell process-intensification solutions to municipal/industrial WWTPs (lower opex/capex, defer plant upgrades); (2) generate high-MRV permanent carbon removal credits for corporate buyers
- Integrates into existing wastewater infrastructure — no dedicated marine vessels/plants; results in weeks
- Long-term utility RFPs + multi-year CDR offtakes
- Pattern: asset-light industrial co-location CDR (related to Pronoe industrial discharge OAE; distinct as wastewater reactor alkalinization with multi-pathway discharge)

## Funding
- **$25M oversubscribed Series A** (14 May 2026): $19M equity + $6M grant/non-dilutive
  - Lead: **Burnt Island Ventures**
  - New: AP Ventures, Sony Innovation Fund, Builders Vision, Kibo Invest, Idemitsu Ventures, New York Ventures, family offices
  - Existing: Counteract, ANIMO Ventures, Connecticut Innovations, Ponderosa Ventures, Echo River Capital
- Prior: $5.3M seed; $2.35M Colorado Energy Office Clean Air Program award (Feb 2026)
- Traction: ~10 WWTP deployments US/Europe (incl. HRSD); one utility considering deferring $350M capex; $33M+ CDR offtakes; 2,000+ tCO2 captured; buyers include JP Morgan, Google, Autodesk, Stripe via Frontier

## Key Technology
- Alkaline mineral smart-dosing in WWTP reactors
- Improves biological treatment + locks CO2/superpollutant emissions in measurable permanent form
- Proprietary MRV for high-confidence quantification
- Scalable analytics platform for WWTP operational insights (in development)

## Contacts
- hello@crewcarbon.com
- Media: clare.bennett@crewcarbon.com
- Offices: Brooklyn, NY; New Haven, CT

## Marine Data Needs
- Receiving-water carbonate chemistry (pH, DIC, alkalinity, TA), effluent chemistry, river/estuarine/coastal mixing, permanence/additionality MRV, ecosystem impact baselines at discharge points
""",
        "body": """## Overview
**CREW Carbon** (Brooklyn, NY; Yale Carbon Containment Lab spinout, 2022) delivers **wastewater process intensification** that simultaneously **permanently removes CO₂** via alkaline mineral smart-dosing (e.g. calcium carbonate) inside existing WWTP reactors. Oversubscribed **$25M Series A** (May 2026, Burnt Island Ventures lead); **$33M+** CDR offtakes (JP Morgan, Google, Autodesk, Stripe/Frontier).

## Business Model
- **Dual revenue**: WWTP performance/cost savings (pollutant removal, settleability, chemical reduction, capacity) + high-MRV durable CDR credits
- Asset-light integration into existing industrial/municipal infrastructure — no new marine plant or vessel required
- Distinct from ship-based OAE ([Calcarea](calcarea.md)), electrochemical plants ([Ebb Carbon](ebb-carbon.md), [Equatic](equatic.md)), and industrial-outfall OAE ([Pronoe](pronoe.md)): **reactor-side alkalinization** with multi-pathway discharge (rivers, estuaries, seawater)

## Funding
| Round | Amount | Date | Notes |
|-------|--------|------|-------|
| Seed | $5.3M | ~2024–25 | Oversubscribed |
| Grant | $2.35M | Feb 2026 | Colorado Energy Office Clean Air |
| Series A | **$25M** ($19M equity + $6M non-dilutive) | May 2026 | **Burnt Island Ventures** lead; AP Ventures, Sony Innovation Fund, Builders Vision, Kibo, Idemitsu, NY Ventures + existing |

## Key Technology
- Smart-dosing alkaline minerals to optimize WWTP pH/alkalinity
- Permanent CO₂ → bicarbonate conversion with proprietary MRV
- Analytics platform for WWTP ops insights (in development)
- ~10 commercial deployments US/Europe (incl. HRSD); 2,000+ tCO₂ removed

## Data & Measurement Needs
- **Primary data types**: WWTP process chemistry, effluent composition, receiving-water carbonate system, flow/mixing, credit MRV packages, ecosystem baselines
- **Key measurements/parameters**: pH, alkalinity/TA, DIC, DIC speciation, nutrient removal rates, settleability, CO₂ flux/ permanence, additionality
- **Observation platforms/programs**: In-plant sensors, discharge-point coastal/riverine monitoring, third-party verification, Frontier offtake MRV
- **Known data gaps**: Long-term estuarine/coastal permanence at scale; standardized cross-basin discharge chemistry protocols; open labeled WWTP–receiving-water paired datasets
- **Interest in external data services**: Coastal carbonate networks, USGS/EPA discharge data, satellite water-quality, independent MRV labs (cf. atdepth pattern)

## Cross-Sector Connections
- Extends asset-light industrial CDR cluster with [Pronoe](pronoe.md) (outfall OAE) — CREW is **in-plant** rather than outfall-only
- Offtake + MRV sophistication parallels [Planetary Technologies](planetary-technologies.md) / [Vycarb](vycarb.md) credit-buyer rigor
- Discharge-to-sea pathway creates demand for [Marine Monitoring & Sensors](marine-monitoring-sensors.md) coastal chemistry networks
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "CREW Carbon",
            "legalName": "CREW Carbon, Inc.",
            "url": "https://crewcarbon.com/",
            "description": "Wastewater treatment process intensification that permanently removes CO2 via alkaline mineral smart-dosing, with high-MRV carbon credits.",
            "foundingDate": "2022",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Brooklyn",
                "addressRegion": "NY",
                "addressCountry": "US",
            },
            "email": "hello@crewcarbon.com",
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "USD",
                "value": 25000000,
                "description": "$25M Series A (May 2026): $19M equity + $6M non-dilutive",
            },
            "sector": "Ocean Carbon Sequestration",
            "businessModel": "Dual: WWTP process-intensification services + permanent CDR credit sales via alkaline mineral dosing in existing infrastructure",
            "lastFundingRound": "$25M Series A (May 2026) led by Burnt Island Ventures",
            "totalFunding": ">$30M incl. seed + grants",
            "investors": [
                "Burnt Island Ventures",
                "AP Ventures",
                "Sony Innovation Fund",
                "Builders Vision",
                "Kibo Invest",
                "Idemitsu Ventures",
                "New York Ventures",
                "Counteract",
                "ANIMO Ventures",
                "Connecticut Innovations",
                "Ponderosa Ventures",
                "Echo River Capital",
            ],
            "knowsAbout": [
                "Wastewater alkalinity enhancement",
                "Ocean-relevant CDR via effluent bicarbonate",
                "MRV for engineered carbon removal",
                "Process intensification",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "WWTP process chemistry",
                    "Effluent composition",
                    "Receiving-water carbonate system",
                    "MRV packages",
                    "Ecosystem baselines",
                ],
                "keyMeasurements": [
                    "pH",
                    "Alkalinity/TA",
                    "DIC",
                    "Nutrient removal",
                    "Permanence metrics",
                ],
                "observationPlatforms": [
                    "In-plant sensors",
                    "Discharge monitoring",
                    "Third-party verification",
                    "Frontier offtake MRV",
                ],
                "knownGaps": [
                    "Long-term coastal permanence at scale",
                    "Cross-basin discharge chemistry standards",
                ],
                "interestInExternalDataServices": "Coastal carbonate networks, EPA/USGS discharge data, satellite water quality, independent MRV labs",
            },
        },
    },
    {
        "name": "Oceanic Constellations",
        "url": "https://www.oceanic-constellations.com/",
        "sector": "Marine Monitoring & Sensors",
        "notes": (
            "Japan (Kamakura) USV swarm 'Marine Satellite Cluster' — mass-deployed small waterborne drones forming "
            "sensor + communications constellation for persistent ocean monitoring, disaster prevention, resource "
            "development, illegal fishing, MDA. ¥2B (~$13M) Series B1 (Jan 2026) co-led JAFCO + Globis Capital; "
            "investors Nippon Yusen (NYK equity Feb 2026), DBJ Capital, Astart, Coral Capital, Green Coinvest. "
            "Total raised ~$24.7M (PitchBook). 20+ patents on marine swarm control. Partners: NYK/Keihin Dock mass "
            "production; Kamakura City + Shonan Fisheries Coop illegal fishing demo; offshore rocket recovery with NYK. "
            "First continuous night ops of domestic small USV; auto recovery with multi-sensor spatial recognition "
            "(Jun 2026). Commercialisation target 2027. Founded Nov 2023; CEO Takuma Honda."
        ),
        "description": "Japan USV swarm Marine Satellite Cluster — ¥2B Series B; NYK/JAFCO/Globis; 20+ swarm patents.",
        "raw": f"""# Oceanic Constellations – Raw Web Extract
**Source:** https://www.oceanic-constellations.com/
**Also:** https://thebridge.jp/en/2026/01/oceanic-constellations-developer-of-swarm-control-technology-for-small-waterborne-drone-vessels-raises-%C2%A52-billion-in-series-b1
**Also:** https://www.nyk.com/english/news/2026/20260206_02.html
**Extracted:** {TODAY}

## Overview
Oceanic Constellations Inc. (Kamakura, Japan; founded November 2023) develops and operates a "Marine Satellite Cluster™" — a constellation of numerous small unmanned surface vehicles (USVs / waterborne drones) that form a persistent sensor and communications network at sea. Swarm control integrates marine communication network control and energy management. CEO Takuma Honda. Multidisciplinary team from aerospace, IT, academia, and automotive.

## Business Model
- Build and operate USV constellations for constant ocean monitoring
- Applications: ocean monitoring, disaster prevention, resource development, illegal fishing prevention, maritime domain awareness, offshore rocket recovery support
- Mass-production path via shipyard partnership (Keihin Dock / NYK Group)
- Patent network strategy (20+ patents on marine swarm control) aimed at global market
- Commercialisation target: 2027

## Funding
- **¥2 billion Series B1** (announced mid-Jan 2026; related Series B coverage Feb 2026) — participants: Globis Capital Partners, JAFCO Group, Nippon Yusen (NYK), DBJ Capital, Astart, Coral Capital, Green Coinvest
- NYK equity investment via third-party allotment (5 Feb 2026) to support USV mass-production framework
- PitchBook: ~$13.1M Feb 2026 tranche; **total raised ~$24.7M**

## Key Technology
- Swarm control for small USV fleets — marine communications network + energy management
- Real-time sensing, monitoring, and data linking of marine infrastructure
- Marine digital twin technology + integrated autonomous vehicle development
- First continuous night operation of domestically produced small USV in Japan
- Jun 2026: first domestic long-endurance small USV auto-recovery demo using multi-sensor spatial recognition
- 20+ patents on marine swarm control essentials for USV constellations

## Partners
- Nippon Yusen (NYK) equity + offshore reusable rocket recovery collaboration
- Keihin Dock (NYK Group) joint demonstration for small USV mass production
- Kamakura City + Shonan Fisheries Cooperative Kamakura Branch + Saito Construction — comprehensive partnership for illegal fishing prevention tech demo (Dec 2025)

## Marine Data Needs
- Multi-USV swarm telemetry, surface METOC, AIS/non-AIS vessel detection, fisheries enforcement ISR, coastal disaster sensors, communications link budgets, energy budgets for persistent constellation ops
""",
        "body": """## Overview
**Oceanic Constellations** (Kamakura, Japan; founded Nov 2023) builds a **Marine Satellite Cluster™** — swarms of small USVs that form a persistent ocean sensor and communications constellation. **¥2B (~$13M) Series B1** (Jan 2026) with **JAFCO**, **Globis Capital**, and **Nippon Yusen (NYK)**; PitchBook total **~$24.7M**. **20+ patents** on marine swarm control. CEO **Takuma Honda**. Commercialisation target **2027**.

## Business Model
- Deploy and operate multi-USV constellations for continuous ocean monitoring and data linking
- Dual-use: ocean observation, disaster prevention, resource development, illegal fishing enforcement, MDA, offshore rocket recovery support
- Shipyard mass-production path via **Keihin Dock (NYK Group)**
- Moat: swarm control patent portfolio + integrated comms/energy management for constellation-scale USVs

## Funding
| Round | Amount | Date | Notes |
|-------|--------|------|-------|
| Series B1 | **¥2B (~$13M)** | Jan 2026 | Globis, **JAFCO**, **NYK**, DBJ Capital, Astart, Coral Capital, Green Coinvest |
| NYK equity | Undisclosed | Feb 2026 | Third-party allotment for mass-production framework |
| **Total** | **~$24.7M** | | PitchBook |

## Key Technology
- Swarm control integrating marine communication networks + energy management
- Small waterborne drone USVs as "marine satellites"
- Marine digital twin + multi-sensor spatial recognition auto-recovery (Jun 2026 demo)
- First continuous night ops of domestic small USV in Japan

## Data & Measurement Needs
- **Primary data types**: Multi-USV swarm telemetry, surface METOC, EO/IR/radar tracks, AIS + dark-vessel detection, fisheries enforcement ISR, coastal disaster sensors, mesh comms link budgets
- **Key measurements/parameters**: Swarm relative navigation, energy state, packet success, vessel contacts, illegal-gear signatures, wave/wind, position error
- **Observation platforms/programs**: Marine Satellite Cluster USV fleets; Kamakura/Shonan illegal-fishing demo; NYK offshore ops; Keihin Dock production units
- **Known data gaps**: Open labeled swarm coordination datasets; standardized multi-USV C2 interchange with allied MDA; long-endurance energy models under Kuroshio/typhoon regimes
- **Interest in external data services**: Satellite SAR/RF cueing, JMSDF/coast guard tracks, fisheries registries, metocean forecasts for constellation tasking

## Cross-Sector Connections
- Asia-Pacific counterpart to US/EU defense USV cluster ([Saronic Technologies](saronic-technologies.md), [HavocAI](havocai.md), [Kraken Technology](kraken-technology.md), [Seasats](seasats.md)) with **constellation/swarm-first** thesis
- Monitoring-as-network resonates with [Sofar Ocean](sofar-ocean.md) (drifter network) and [Quartermaster](quartermaster.md) (vessel-mounted sensing) — OC is **purpose-built USV constellation**
- NYK shipping strategic investor parallels Crowley/Saildrone and MOL/Sofar industrial partnerships
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Oceanic Constellations",
            "legalName": "Oceanic Constellations Inc.",
            "url": "https://www.oceanic-constellations.com/",
            "description": "Japanese developer of Marine Satellite Cluster USV swarms for persistent ocean monitoring, communications, and dual-use maritime missions.",
            "foundingDate": "2023",
            "founder": {"@type": "Person", "name": "Takuma Honda", "jobTitle": "CEO"},
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Kamakura",
                "addressCountry": "JP",
            },
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "JPY",
                "value": 2000000000,
                "description": "¥2B Series B1 (Jan 2026); ~$24.7M total raised (PitchBook)",
            },
            "sector": "Marine Monitoring & Sensors",
            "businessModel": "Build/operate small-USV constellations for persistent ocean sensing and dual-use maritime missions; mass-produce via shipyard partners",
            "lastFundingRound": "¥2B Series B1 (Jan 2026) — Globis, JAFCO, NYK et al.",
            "totalFunding": "~$24.7M",
            "investors": [
                "Globis Capital Partners",
                "JAFCO Group",
                "Nippon Yusen (NYK)",
                "DBJ Capital",
                "Astart",
                "Coral Capital",
                "Green Coinvest",
            ],
            "knowsAbout": [
                "USV swarm control",
                "Marine satellite constellation",
                "Ocean monitoring networks",
                "Illegal fishing enforcement USVs",
                "Offshore rocket recovery support",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Swarm telemetry",
                    "Surface METOC",
                    "Vessel ISR",
                    "Dark-vessel detection",
                    "Mesh comms metrics",
                ],
                "keyMeasurements": [
                    "Relative navigation",
                    "Energy state",
                    "Contact tracks",
                    "Wave/wind",
                    "Link budget",
                ],
                "observationPlatforms": [
                    "Marine Satellite Cluster USVs",
                    "Kamakura illegal-fishing demo",
                    "NYK/Keihin production units",
                ],
                "knownGaps": [
                    "Open swarm coordination datasets",
                    "Multi-USV C2 interchange standards",
                ],
                "interestInExternalDataServices": "Satellite SAR/RF cueing, coast guard tracks, fisheries registries, metocean forecasts",
            },
        },
    },
]


def main():
    sources_path = os.path.join(REPO, "sources", "companies.json")
    with open(sources_path) as f:
        companies = json.load(f)

    existing = {c["name"] for c in companies}
    added = []

    for c in COMPANIES:
        slug = slugify(c["name"])
        print(f"Processing {c['name']} -> {slug}")

        # raw
        raw_path = os.path.join(REPO, "raw", f"{slug}.md")
        with open(raw_path, "w") as f:
            f.write(c["raw"].strip() + "\n")

        # metadata
        meta_path = os.path.join(REPO, "metadata", f"{slug}.jsonld")
        with open(meta_path, "w") as f:
            json.dump(c["metadata"], f, indent=2)
            f.write("\n")

        # wiki
        wiki_path = os.path.join(REPO, "wiki", f"{slug}.md")
        with open(wiki_path, "w") as f:
            f.write(
                wiki_page(
                    c["name"], c["url"], c["sector"], c["body"], c["description"]
                )
            )

        if c["name"] not in existing:
            companies.append(
                {
                    "sector": c["sector"],
                    "name": c["name"],
                    "url": c["url"],
                    "notes": c["notes"],
                    "last_updated": TODAY,
                }
            )
            added.append(c["name"])
        else:
            for entry in companies:
                if entry["name"] == c["name"]:
                    entry["notes"] = c["notes"]
                    entry["url"] = c["url"]
                    entry["sector"] = c["sector"]
                    entry["last_updated"] = TODAY

    with open(sources_path, "w") as f:
        json.dump(companies, f, indent=2)
        f.write("\n")

    print(f"Done. Added: {added}. Total companies: {len(companies)}")


if __name__ == "__main__":
    main()
