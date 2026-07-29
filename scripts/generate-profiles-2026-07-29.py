#!/usr/bin/env python3
"""Generate profiles for 2026-07-29 autonomous run — 4 new high-signal companies."""
import json, os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = "2026-07-29"
TS = "2026-07-29T00:00:00Z"


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
        "name": "Endurance Energy",
        "url": "https://www.enduranceenergy.com/",
        "sector": "Offshore Energy",
        "notes": (
            "Subsea geothermal power from mid-ocean ridge / Ring of Fire heat — modular seafloor plants for "
            "24/7 baseload renewable electricity (islands, industry, hyperscale AI data centers). "
            "$54M Series A (Jun 2026) led by Founders Fund; participants Ascend, Construct Capital, Felicis, "
            "First Round, Point72 Ventures, Riot Ventures, Voyager Ventures. Total raised ~$84M (PitchBook). "
            "Founded by ex-SpaceX engineer Andrew Redd (Dragon/Starship); ~25 staff, ~12 ex-SpaceX; VP Eng ex-Helion. "
            "Adélie: planned 100 kW subsea system for 1-year Axial Seamount caldera deployment tied to OOI Regional "
            "Cabled Array (Oregon coast, Sep 2026 target). Tonga government partnership for subsea geothermal test. "
            "Advantages claimed: weather-independent baseload, zero surface footprint (gen+tx on/under seafloor), "
            "GW-scale in months via factory modular units, O&G/geothermal tech heritage. Seattle HQ. "
            "Contact: info@enduranceenergy.com."
        ),
        "description": "Subsea geothermal baseload power — $54M Series A (Founders Fund); Adélie OOI pilot; Tonga partnership.",
        "raw": f"""# Endurance Energy – Raw Web Extract
**Source:** https://www.enduranceenergy.com/
**Also:** https://techcrunch.com/2026/06/11/endurance-energy-raises-54m-to-harness-a-massive-untapped-energy-source/
**Extracted:** {TODAY}

## Overview
Endurance Energy develops subsea geothermal systems that generate continuous electricity from Earth's heat at tectonic spreading centers and volcanic seafloor (Ring of Fire). Positioning: renewable, 24/7 baseload, rapidly deployable at tens–hundreds of GW potential vs slow nuclear build and intermittent wind/solar without storage.

## Business Model
- Develop and deploy modular subsea geothermal power plants
- Target customers: island nations (high fuel-import GDP share), industrial sites, hyperscale AI data centers facing projected US power shortfall
- Factory-built small modular units clusterable to GW scale; generation + transmission on/under seafloor (zero surface footprint)

## Funding
- **$54M Series A** (Jun 2026) — led by **Founders Fund**; Ascend, Construct Capital, Felicis Ventures, First Round Capital, Point72 Ventures, Riot Ventures, Voyager Ventures
- PitchBook total funding cited ~$84M (incl. prior seed)
- Use of proceeds: prototype → full-stack systems; scale offshore operational capability

## Key Technology / Projects
- Subsea geothermal at mid-ocean ridges / seafloor volcanic heat
- Leverages proven oil & gas and geothermal tech; ROV/robotic underwater ops; corrosion/pressure hardening
- **Adélie**: planned 100 kW subsea power system, 1-year operation inside Axial Seamount caldera, connection to OOI Regional Cabled Array (Oregon coast); target ~Sep 2026 deployment
- **Tonga**: Government of Tonga partnership — subsea geothermal test deployment announcement

## Team
- CEO/Founder: Andrew Redd (ex-SpaceX Dragon & Starship engineer)
- ~25 employees; ~12 ex-SpaceX; VP Engineering ex-Helion Energy
- HQ: Seattle, WA
- Contact: info@enduranceenergy.com

## Marine Data Needs
- Seafloor heat flux, bathymetry, tectonics, OOI cable array integration, ROV ops oceanography, environmental baselines for permitting
""",
        "body": """## Overview
Endurance Energy (Seattle) builds **subsea geothermal** power systems that tap Earth's internal heat at seafloor spreading centers and volcanic sites (Ring of Fire) for weather-independent, zero-surface-footprint baseload electricity. Founded by ex-SpaceX engineer **Andrew Redd** (Dragon/Starship), the company raised a **$54M Series A led by Founders Fund** (Jun 2026) amid surging demand from AI data centers, industry, and island grids.

## Business Model
- **Product**: Modular seafloor geothermal generation + undersea transmission, factory-built units clusterable to GW scale
- **Markets**: Island nations (fuel imports up to ~13% GDP), industrial power, hyperscale AI / data-center offtake
- **Differentiator vs land geothermal**: Access magma-proximal heat without multi-km land drilling far from load centers; vs nuclear: faster deploy; vs wind/solar: true 24/7 without batteries
- **Stage**: Prototype → full-stack; first ocean pilots (Adélie OOI, Tonga)

## Funding
- **$54M Series A** (Jun 2026) — **Founders Fund** lead; Ascend, Construct Capital, Felicis, First Round, Point72 Ventures, Riot Ventures, Voyager Ventures
- Prior seed; PitchBook cumulative ~**$84M**
- Team ~25 (≈12 ex-SpaceX); VP Eng from Helion fusion

## Key Technology
- Subsea closed-loop / modular geothermal at tectonic spreading & volcanic seafloor
- O&G-grade subsea engineering (pressure, corrosion, ROV installation)
- **Adélie (100 kW)**: 1-year deployment target inside **Axial Seamount** caldera tied to **OOI Regional Cabled Array** (Oregon)
- **Tonga** government partnership for island-nation test deployment
- Claims: GW-scale install in months; gen+tx fully subsea

## Data & Measurement Needs
- **Primary data types**: Seafloor heat flux and temperature fields; multibeam bathymetry; tectonic/volcanic hazard data; cabled observatory telemetry; ROV/AUV survey streams; metocean for install vessels
- **Key measurements/parameters**: Subsurface temperature gradients, hydrothermal chemistry, seafloor deformation/seismicity, ambient currents, corrosion rates, power output / cable integrity, benthic baseline ecology
- **Observation platforms/programs**: OOI Regional Cabled Array integration (Adélie); site characterization AUV/ROV campaigns; long-term seafloor sensor packages; island grid interconnection studies (Tonga)
- **Known data gaps**: High-resolution heat-flux maps at candidate ridge/volcanic sites; multi-year environmental baselines for permitting; real-time subsea plant health + ecological co-monitoring standards
- **Interest in external data services**: OOI/NSF cabled data; NOAA/USGS seafloor and seismic products; commercial AUV survey (e.g. Bedrock, XOCEAN-class); satellite SST/altimetry for regional context

## Cross-Sector Connections
- **Offshore Energy**: New baseload pathway beside floating wind (Ørsted/Principle Power), wave compute (Panthalassa), ocean LDES (Sizable Energy)
- **Marine Monitoring**: Heavy dependence on cabled observatories, AUVs, and benthic MRV — pull-through for sensor primes
- **Ocean Data & AI**: Long-duration seafloor telemetry fusion analogous to Sofar/XOCEAN surface networks
""",
        "jsonld": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Endurance Energy",
            "url": "https://www.enduranceenergy.com/",
            "description": "Subsea geothermal power systems delivering 24/7 baseload renewable electricity from seafloor heat sources.",
            "foundingDate": "2025",
            "founder": {"@type": "Person", "name": "Andrew Redd", "jobTitle": "CEO & Founder"},
            "email": "info@enduranceenergy.com",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Seattle",
                "addressRegion": "WA",
                "addressCountry": "US",
            },
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "USD",
                "value": 54000000,
                "description": "$54M Series A (Jun 2026) led by Founders Fund; cumulative ~$84M per PitchBook",
            },
            "sector": "Offshore Energy",
            "businessModel": "Modular subsea geothermal power plants for islands, industry, and AI data centers; factory units clusterable to GW scale",
            "lastFundingRound": "Series A — $54M (Jun 2026, Founders Fund lead)",
            "totalFunding": "~$54M Series A; ~$84M cumulative (PitchBook)",
            "investors": [
                "Founders Fund",
                "Ascend",
                "Construct Capital",
                "Felicis Ventures",
                "First Round Capital",
                "Point72 Ventures",
                "Riot Ventures",
                "Voyager Ventures",
            ],
            "knowsAbout": [
                "Subsea geothermal energy",
                "Mid-ocean ridge heat extraction",
                "Modular offshore power",
                "OOI cabled observatory integration",
                "Seafloor robotics installation",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Seafloor heat flux",
                    "Bathymetry",
                    "Cabled observatory telemetry",
                    "ROV/AUV survey data",
                    "Benthic ecology baselines",
                ],
                "keyMeasurements": [
                    "Temperature gradients",
                    "Hydrothermal chemistry",
                    "Seismicity/deformation",
                    "Currents",
                    "Power/cable integrity",
                ],
                "observationPlatforms": [
                    "OOI Regional Cabled Array",
                    "Adélie 100 kW pilot",
                    "AUV/ROV site characterization",
                ],
                "knownGaps": [
                    "High-resolution heat-flux maps at candidate sites",
                    "Multi-year environmental baselines for permitting",
                ],
                "interestInExternalDataServices": "OOI/NSF cabled data, NOAA/USGS seafloor products, commercial AUV survey fleets",
            },
        },
    },
    {
        "name": "Kraken Technology",
        "url": "https://krakentechnology.com/",
        "sector": "Marine Monitoring & Sensors",
        "notes": (
            "UK maritime defence USV/USSV prime (NOT Kraken Robotics). Modular uncrewed platforms: K3 SCOUT USV, "
            "K4 MANTA stealth USSV, K5 high-payload USV. $175M Series B at $1B valuation (9 Jul 2026) led by DTCP; "
            "British Business Bank, NATO Innovation Fund, Rheinmetall, Inocea, HICO, Thesiger, BOKA, Supernova Invest, "
            "Hakluyt; prior NIF/NSSIF/SmartCap/Notion/Speedinvest converted. Contracts: UK MoD, NATO partners, "
            "USSOCOM $49M OTA. Manufacturing: Rheinmetall Blohm+Voss (Hamburg K3 series), Anduril (US), Davie/Inocea (Canada). "
            "World-first USV airdrop (K3 SCOUT from A400M, Jul 2026). Founder/CEO Mal Crease; CTO Amelia Gould (Jul 2026); "
            "Kraken US CEO Justin Litko. Fareham/Segensworth UK. Dual-use path: defence, security, offshore wind/O&G survey."
        ),
        "description": "UK defence USV unicorn — $175M Series B at $1B; K3/K4/K5 platforms; Anduril/Rheinmetall/Davie manufacturing.",
        "raw": f"""# Kraken Technology – Raw Web Extract
**Source:** https://krakentechnology.com/
**Funding PR:** https://krakentechnology.com/articles/kraken-technology-group-raises-160m-at-1bn-valuation
**Extracted:** {TODAY}

## Overview
Kraken Technology Group (UK; Fareham/Segensworth) designs and builds autonomous surface and subsurface vessels for defence, security, infrastructure, commercial, and aid missions. Distinct from Canadian public company Kraken Robotics. Founded ~2020; racing-industry DNA; mission-first high-sea-state robotics.

## Platforms
- **K3 SCOUT** — modular uncrewed surface vessel (USV); series production at Rheinmetall Blohm+Voss Hamburg; airdrop-capable (A400M extracted-load demo Jul 2026 with Capewell)
- **K4 MANTA** — stealthy uncrewed subsurface vessel (USSV)
- **K5 Kraken** — high-payload USV
- Resilient at Sea State 5+

## Business Model
- Defence prime / platform OEM for NATO and allies
- Localized manufacturing partnerships (Germany Rheinmetall, US Anduril, Canada Davie/Inocea; ME + Indo-Pacific forthcoming)
- Dual-use: border/coast guard, offshore wind & O&G monitoring/survey, CNI protection, humanitarian/research

## Funding
- **$175M Series B at $1B valuation** (9 Jul 2026) — led by **DTCP** (Digital Transformation Capital Partners / DTCP Defence)
- Participants: British Business Bank, NATO Innovation Fund (NIF), Rheinmetall, Inocea Group, HICO, Thesiger Capital Group, BOKA Capital, Supernova Invest, Hakluyt Capital
- Earlier instruments converted: NIF, UK NSSIF, SmartCap, Notion Capital, Speedinvest
- **$49M OTA** from USSOCOM (May 2026)

## Contracts & Partnerships
- UK MoD, NATO European partners, USSOCOM — platforms deployed in support of multiple ongoing conflicts
- Anduril Industries — US domestic manufacturing and integration (Apr 2026)
- Rheinmetall — K3 Scout series production Hamburg (Apr 2026)
- Davie Shipbuilding (Inocea) — Canada autonomous vessel production (May 2026)
- Capewell — USV airdrop system

## Leadership
- Founder & CEO: Mal Crease
- CTO: Amelia Gould (appointed 28 Jul 2026)
- CEO Kraken US: Justin Litko (appointed 27 Jul 2026)
- Advisory: Rear Admiral James Parkin CB CBE (ex-RN)
- Contact: contact@krakentechnology.com

## Marine Data Needs
- High-sea-state autonomy perception, AIS/radar/EO fusion, bathymetry, metocean for contested littoral ops, ISR payload streams
""",
        "body": """## Overview
**Kraken Technology Group** (UK; Fareham) is a maritime defence OEM building modular uncrewed surface and subsurface vessels for NATO and allies. **Not** the Canadian public company Kraken Robotics. In July 2026 it closed a **$175M Series B at a $1B valuation** (DTCP-led), becoming a UK defence-tech unicorn with production partners Anduril (US), Rheinmetall (Germany), and Davie/Inocea (Canada).

## Business Model
- **Defence platform OEM**: sell/produce mission-ready USV/USSV fleets + payloads for navy, SOF, littoral, and joint force use
- **Localized manufacturing**: co-produce with primes in key markets rather than export-only from UK
- **Dual-use expansion**: maritime security, CNI/subsea infrastructure protection, offshore wind & O&G survey/monitoring, humanitarian/research
- **Mass / speed thesis**: affordable high-speed uncrewed vessels hardened for high sea state, delivered at tempo

## Funding
- **$175M Series B @ $1B** (9 Jul 2026) — **DTCP** lead; British Business Bank, **NATO Innovation Fund**, **Rheinmetall**, Inocea, HICO, Thesiger, BOKA, Supernova Invest, Hakluyt
- Converted earlier: NIF, UK **NSSIF**, SmartCap, Notion Capital, Speedinvest
- **$49M USSOCOM OTA** (May 2026)
- Advisor: PJT Partners; counsel Clifford Chance

## Key Technology
- **K3 SCOUT** modular USV — series production at Rheinmetall Blohm+Voss; **world-first USV airdrop** from A400M (Jul 2026, Capewell UMCADS)
- **K4 MANTA** stealth uncrewed subsurface vessel
- **K5** high-payload USV
- Autonomy stack for contested littorals; Sea State 5+ resilience; modular mission payloads (ISR → force protection / precision effects)

## Leadership & Partners
- CEO/Founder: **Mal Crease**; CTO **Amelia Gould**; Kraken US CEO **Justin Litko**
- Partners: Anduril Industries, Rheinmetall, Davie Shipbuilding, Capewell
- Customers: UK MoD, NATO partners, USSOCOM (deployed on multiple active conflicts per company)

## Data & Measurement Needs
- **Primary data types**: Multi-sensor autonomy perception (radar, EO/IR, AIS, acoustic), metocean for high-sea-state control, bathymetry/coastal charts, ISR full-motion video and tracks, GNSS-denied navigation aids
- **Key measurements/parameters**: Sea state, wave spectra, wind, current, contact classification confidence, acoustic signatures (ASW-adjacent), position integrity under jamming
- **Observation platforms/programs**: Onboard USV/USSV sensor suites; cooperative fleet C2; range/test instrumentation; partner shipyard sea trials
- **Known data gaps**: Contested-environment training data at scale; standardized NATO USV autonomy test metrics; persistent littoral oceanographic layers for swarm routing
- **Interest in external data services**: Metocean forecasts, satellite MDA, acoustic oceanography, chart/ENC updates, coalition track data services

## Cross-Sector Connections
- **Defense ASV cluster**: Joins Saronic, Blue Water Autonomy, HavocAI, Vatn, Ulysses, Seasats — European/NATO counterpart with unique airdrop + multi-nation mfg footprint
- **Anduril partnership**: US production bridge similar to other dual-use autonomy plays
- **Commercial survey adjacency**: Offshore wind/O&G monitoring overlaps XOCEAN/Maritime Robotics service models
""",
        "jsonld": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Kraken Technology",
            "legalName": "Kraken Technology Group Ltd",
            "alternateName": "Kraken Technology Group",
            "url": "https://krakentechnology.com/",
            "email": "contact@krakentechnology.com",
            "description": "UK maritime defence company designing modular autonomous surface and subsurface vessels (K3 SCOUT, K4 MANTA, K5) for NATO and allied missions.",
            "foundingDate": "2020",
            "founder": {"@type": "Person", "name": "Mal Crease", "jobTitle": "Founder & CEO"},
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Area 1, 5 Sopwith Park, Concorde Close",
                "addressLocality": "Fareham",
                "addressRegion": "Hampshire",
                "postalCode": "PO15 5RT",
                "addressCountry": "GB",
            },
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "USD",
                "value": 175000000,
                "description": "$175M Series B at $1B valuation (9 Jul 2026) led by DTCP",
            },
            "sector": "Marine Monitoring & Sensors",
            "businessModel": "Defence USV/USSV OEM with localized manufacturing partnerships (Rheinmetall, Anduril, Davie); dual-use security and offshore survey path",
            "lastFundingRound": "Series B — $175M at $1B (Jul 2026, DTCP lead)",
            "totalFunding": "$175M Series B disclosed; prior seed/strategic + $49M USSOCOM OTA",
            "investors": [
                "DTCP",
                "British Business Bank",
                "NATO Innovation Fund",
                "Rheinmetall",
                "Inocea Group",
                "HICO",
                "Thesiger Capital Group",
                "BOKA Capital",
                "Supernova Invest",
                "Hakluyt Capital",
                "NSSIF",
                "SmartCap",
                "Notion Capital",
                "Speedinvest",
            ],
            "knowsAbout": [
                "Unmanned surface vessels",
                "Unmanned subsurface vessels",
                "Maritime defence autonomy",
                "High sea state robotics",
                "USV airdrop deployment",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Autonomy perception sensor fusion",
                    "Metocean",
                    "Bathymetry",
                    "ISR video/tracks",
                    "Acoustic data",
                ],
                "keyMeasurements": [
                    "Sea state",
                    "Wave spectra",
                    "Contact classification",
                    "GNSS-denied navigation integrity",
                ],
                "observationPlatforms": ["K3/K4/K5 organic sensors", "Fleet C2", "Sea trials instrumentation"],
                "knownGaps": [
                    "Contested-environment training corpora",
                    "NATO-standard USV autonomy test metrics",
                ],
                "interestInExternalDataServices": "Metocean, satellite MDA, acoustic oceanography, ENC updates",
            },
        },
    },
    {
        "name": "XOCEAN",
        "url": "https://xocean.com/",
        "sector": "Ocean Data & AI",
        "notes": (
            "Ireland-based turnkey ocean data delivery via in-house USV fleet — geophysical, environmental, asset integrity, "
            "bathymetry, fisheries for offshore wind and civil hydrography. €115M (~$118M) growth investment (Jan 2025) "
            "via S2G Ventures structure; Climate Investment, Morgan Stanley 1GT, Crown Family CC Industries affiliate. "
            "Customers: Ørsted, Shell, bp, SSE, RWE, Vattenfall, EnBW, Eneco (5-year NL framework), governments in 23+ jurisdictions. "
            "4.9M+ GB data processed; 48.6+ GW offshore wind supported; fleet >1.2M km cumulative (Jul 2026). "
            "Sensors: MBES, SSS, SBP, magnetometer. Models: fixed-price turnkey campaigns + data library licensing. "
            "Offices: Ireland (Rathcor/Dundalk), UK, US, Canada, Norway, Australia (Melbourne), NL hub IJmuiden. Founded 2017. "
            "Carbon-neutral USV ocean data thesis."
        ),
        "description": "Turnkey ocean data via USV fleet — €115M raise; Ørsted/Shell/bp customers; 48.6+ GW offshore wind supported.",
        "raw": f"""# XOCEAN – Raw Web Extract
**Source:** https://xocean.com/
**Funding:** €115M investment (Jan 2025) — S2G, Climate Investment, Morgan Stanley 1GT, Crown Family CC Industries affiliate
**Extracted:** {TODAY}

## Overview
XOCEAN provides turnkey ocean data using Uncrewed Surface Vessels (USVs). From seabed mapping to environmental monitoring — safe, economic, carbon-neutral ocean data delivery for offshore energy and civil hydrography. Founded 2017; HQ Rathcor, Co. Louth, Ireland; global ops.

## Business Model
- **Direct / turnkey**: fixed-price fully inclusive campaigns — understand needs → USV acquisition → process/interpret → deliver report
- **Data Library**: license existing high-quality ocean datasets before new campaigns
- Value props: high safety, low impact, scalable, rapid, weather tolerant, carbon neutral

## Markets / Applications
- Offshore Wind, Geophysical, Environmental, Asset Integrity, Bathymetry, Fisheries
- Customers include major energy cos and government agencies (logos: Ørsted, Shell, bp, SSE, RWE, Vattenfall, EnBW, Shearwater, etc.)
- 23+ jurisdictions; Eneco 5-year framework (5 Dutch OWFs); Dogger Bank restoration support

## Scale (company-reported / press)
- €115M (~$118M) growth round (Jan 2025)
- 4.9M+ GB data collected/processed (Robot Report era stats)
- 48.6+ GW offshore wind development supported
- Fleet cumulative transit >1.2 million km (~30 global circumnavigations) as of Jul 2026

## Technology / Sensors
- In-house USV fleet remote-piloted from shore
- MBES (Multibeam Echosounder), SSS (Side-Scan Sonar), SBP (Sub-Bottom Profiler), MAG (Magnetometer)
- Data processing and interpretation in-house

## Presence
- Ireland (Rathcor Technical Centre; Dundalk Operations), UK, US, Canada, Norway, Australia (Melbourne), Netherlands hub (IJmuiden)
- Contact: info@xocean.com

## Marine Data Needs
- Multibeam/backscatter, sub-bottom, magnetics, metocean for USV ops, environmental baselines, cable/route geohazards
""",
        "body": """## Overview
**XOCEAN** (Ireland, founded 2017) delivers **turnkey ocean data** via an in-house fleet of uncrewed surface vessels — seabed mapping, geophysical, environmental, and asset-integrity surveys for offshore wind and civil hydrography. A **€115M (~$118M) growth investment** (Jan 2025; S2G-structured with Climate Investment, Morgan Stanley 1GT, Crown Family affiliate) funds global scale-out of a carbon-neutral USV data platform already supporting **48.6+ GW** of offshore wind and customers including **Ørsted, Shell, bp, SSE, RWE, Vattenfall**.

## Business Model
- **Turnkey fixed-price campaigns**: requirements → multi-USV acquisition → processing/interpretation → final deliverable
- **Data library licensing**: resell/reuse prior survey assets before mobilizing new collection
- **Service differentiation**: high safety (crew ashore), low carbon, weather-tolerant persistence, rapid scale-out vs crewed survey vessels
- **Stage**: Growth / multi-basin operations (Europe, N America, Australia)

## Funding
- **€115M (~$118M)** (Jan 2025) — structured with **S2G Ventures**; **Climate Investment**, **Morgan Stanley 1GT**, Crown Family **CC Industries** affiliate
- Use: geographic expansion, fleet and shore hubs, platform scale

## Key Technology & Operations
- Shore-piloted **USV fleet** for MBES, side-scan, sub-bottom profiler, magnetometer payloads
- In-house processing/analytics pipeline and multi-year data library
- Cumulative fleet distance **>1.2M km** (Jul 2026); **4.9M+ GB** ocean data processed (prior disclosed)
- Hubs: Rathcor/Dundalk (IE), Melbourne (AU), IJmuiden (NL) for Eneco framework; offices UK/US/CA/NO

## Customers & Contracts
- Energy: Ørsted, Shell, bp, SSE Renewables, RWE, Vattenfall, EnBW, Eneco (5-year Dutch OWF framework)
- Government/civil hydrography across 23+ jurisdictions
- Example value: early rock-outcrop detection on subsea cable routes → reroute before engineering lock-in

## Data & Measurement Needs
- **Primary data types**: Multibeam bathymetry/backscatter, side-scan imagery, sub-bottom stratigraphy, magnetics, water-column/environmental samples, metocean for USV ops
- **Key measurements/parameters**: Depth, seafloor texture, shallow geology, UXO/magnetic anomalies, cable/pipeline as-found position, habitat metrics, wave/wind/current for operability
- **Observation platforms/programs**: In-house USV fleet; shore ROC; repeat asset-integrity time series; data library productization
- **Known data gaps**: Coastline-to-EEZ seamless modern bathymetry; standardized environmental DNA + acoustic habitat layers co-collected with geophysics; real-time multi-vessel adaptive survey AI
- **Interest in external data services**: Satellite-derived bathymetry/SSCI cues, public hydrographic archives (EMODnet, NOAA), metocean forecasts, offshore wind developer GIS stacks

## Cross-Sector Connections
- **Ocean Data & AI**: Closest peer to Sofar (owned sensor network → data products) but survey-campaign + library model vs drifter weather network
- **Offshore Energy**: Primary demand pull from floating/fixed wind developers already in graph (Ørsted et al.)
- **Marine Monitoring**: USV hardware layer adjacent to Maritime Robotics, Clear Robotics, Seasats — XOCEAN monetizes data delivery more than platform sales
""",
        "jsonld": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "XOCEAN",
            "url": "https://xocean.com/",
            "email": "info@xocean.com",
            "description": "Turnkey ocean data delivery using uncrewed surface vessels for offshore wind, geophysical, environmental, and hydrographic customers.",
            "foundingDate": "2017",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Rathcor Technical Centre",
                "addressLocality": "Rathcor, Co. Louth",
                "postalCode": "A91 DVT0",
                "addressCountry": "IE",
            },
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "EUR",
                "value": 115000000,
                "description": "€115M growth investment (Jan 2025) via S2G; Climate Investment, Morgan Stanley 1GT, Crown Family affiliate",
            },
            "sector": "Ocean Data & AI",
            "businessModel": "Fixed-price turnkey USV ocean data campaigns + data library licensing; carbon-neutral survey alternative to crewed vessels",
            "lastFundingRound": "€115M growth (Jan 2025)",
            "totalFunding": "€115M disclosed growth round",
            "investors": [
                "S2G Ventures",
                "Climate Investment",
                "Morgan Stanley 1GT",
                "CC Industries (Crown Family affiliate)",
            ],
            "knowsAbout": [
                "Uncrewed surface vessels",
                "Multibeam bathymetry",
                "Offshore wind survey",
                "Ocean data services",
                "Subsea cable route survey",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "MBES bathymetry",
                    "Side-scan sonar",
                    "Sub-bottom profiler",
                    "Magnetometer",
                    "Environmental monitoring",
                ],
                "keyMeasurements": [
                    "Depth",
                    "Backscatter",
                    "Shallow geology",
                    "Magnetic anomalies",
                    "Habitat metrics",
                    "Metocean operability",
                ],
                "observationPlatforms": ["In-house USV fleet", "Shore remote operations centers", "Data library"],
                "knownGaps": [
                    "Seamless EEZ modern bathymetry",
                    "Co-collected eDNA/acoustic habitat standards",
                ],
                "interestInExternalDataServices": "Satellite bathymetry cues, EMODnet/NOAA archives, metocean forecasts",
            },
        },
    },
    {
        "name": "Saildrone",
        "url": "https://www.saildrone.com/",
        "sector": "Marine Monitoring & Sensors",
        "notes": (
            "Alameda CA autonomous USV leader for maritime defense & ocean intelligence. Wind+solar endurance platforms: "
            "Explorer (METOC), Voyager (MDA/coastal), Surveyor (deep-ocean mapping/ASW), Spectre (170-ft ASW/VLS-class, 2026). "
            "12+ years ops; 2.5M nm sailed; 65K days at sea. Funding: $60M (May 2025, EIFO lead + Lux/Crowley et al.); "
            "$50M Lockheed Martin strategic (Oct 2025) for JAGM launcher integration / live-fire 2026; prior $75M C-1 (2024), "
            "$100M Series C (2021 Bond); total >$345M. Investors: BOND, XN, Standard, Emerson Collective, Crowley, Capricorn, "
            "Lux, Social Capital, Tribe, Schmidt Family Foundation, Exor Seeds, Washington Harbor, Academy Securities, Pinegrove. "
            "Missions: MDA, ASW/undersea detection, ocean mapping, sub-bottom, METOC, kinetics/effectors; USCG BPA, Danish Armed "
            "Forces Baltic Voyagers, hurricane eye science. Fully managed data delivery (Mission Portal + API). CEO Richard Jenkins."
        ),
        "description": "Autonomous USV defence & ocean intelligence — $345M+ raised; Spectre ASW platform; Lockheed $50M; 2.5M nm sailed.",
        "raw": f"""# Saildrone – Raw Web Extract
**Source:** https://www.saildrone.com/ / https://www.saildrone.com/about
**Extracted:** {TODAY}

## Overview
Saildrone, Inc. (Alameda, CA; founded 2012 by Richard Jenkins) builds autonomous unmanned surface vehicles delivering persistent maritime intelligence, surveillance, reconnaissance, ocean mapping, and increasingly kinetic/effector payloads. 12+ years operations, 2.5M nautical miles sailed, 65K days at sea. European HQ Copenhagen (2025).

## Platforms
- **Explorer** — affordable persistent METOC / environmental sensing
- **Voyager** — multi-mission MDA, counter-narcotics, illegal immigration, EW, coastal mapping; Class-certified USV
- **Surveyor** — blue-water deep-ocean mapping, undersea detection; production at Austal USA
- **Spectre** (2026) — next-gen ~170-ft USV for ASW and VLS/strike; silent endurance + stealth configs; towed arrays / VDS; modular effectors
- Propulsion: wind wing + solar (+ engine assist on larger classes); extreme endurance months on station

## Business Model
- Fully managed autonomous maritime data/ISR service (Mission Portal + API)
- Platform programs for government/defense customers
- Science and commercial ocean mapping / METOC heritage evolving to defence-primary positioning ("Autonomous Maritime Defense & Ocean Intelligence")

## Funding (disclosed)
- **$50M strategic** — Lockheed Martin (Oct 2025) — JAGM Quad Launcher integration; live-fire demos targeted 2026
- **$60M** — May 2025 led by EIFO (Denmark) with Lux Capital, Washington Harbor Partners, Crowley, Academy Securities, Pinegrove — Europe expansion / Danish Armed Forces Voyagers
- **$75M Series C-1** (2024) at ~$575M post
- **$100M Series C** (2021) led by Bond at ~$600M post
- **Total funding >$345M** (Sacra / press aggregate)
- Other backers: XN, Standard Investments, Emerson Collective, Capricorn TIF, Social Capital, Tribe Capital, Schmidt Family Foundation, Exor Seeds, Horizons Ventures, Crowley Maritime

## Missions & Traction
- Maritime Domain Awareness, undersea detection/ASW, ocean & coastal mapping, sub-bottom profiling, METOC/hurricane monitoring, kinetics & effectors
- USCG missions; Danish Armed Forces Baltic deployment; GPS-denied Middle East ops; first video inside Cat-4 hurricane; Antarctic circumnavigation heritage
- USCG $37M BPA (press); Seabed 2030 collaboration heritage

## Leadership
- Founder & CEO: Richard Jenkins
- President: John Mustin; CGRO Tom Alexander; CFO Jen Betz; European MD Robert Kleist

## Marine Data Needs
- Multibeam/backscatter, acoustics (ASW), metocean, AIS/radar/vision fusion training data, satellite MDA cueing, GNSS-denied nav references
""",
        "body": """## Overview
**Saildrone** (Alameda, CA; founded 2012 by **Richard Jenkins**) is the long-endurance autonomous USV leader spanning ocean science METOC heritage and modern **maritime defense & ocean intelligence**. With **12+ years**, **~2.5M nm** sailed, and **~65K days** at sea, it fields Explorer → Voyager → Surveyor platforms and the 2026 **Spectre** (~170-ft) ASW/strike-class USV. Aggregate equity/strategic capital exceeds **~$345M**, including a **$50M Lockheed Martin** investment (Oct 2025) and **$60M EIFO-led** Europe round (May 2025).

## Business Model
- **Fully managed service**: customer buys ocean/ISR data and mission effects via Mission Portal + API; Saildrone owns/operates fleet
- **Defense programs**: persistent MDA, ASW, mapping, and emerging kinetic effector integration for US and allied forces
- **Science/commercial residual**: hurricane METOC, fisheries, cable-route and coastal mapping
- **Moat**: unmatched open-ocean endurance dataset + Class-certified platforms + shipyard partners (Austal USA Surveyor production)

## Funding
| Round | Amount | Date | Notes |
|-------|--------|------|-------|
| Series C | $100M | 2021 | Bond lead; ~$600M post |
| Series C-1 | $75M | 2024 | ~$575M post |
| Growth | $60M | May 2025 | **EIFO** lead; Lux, Crowley, Washington Harbor, Academy, Pinegrove |
| Strategic | $50M | Oct 2025 | **Lockheed Martin** — JAGM launcher integration / 2026 live-fire |
| **Total** | **>$345M** | | |

Other investors: XN, Standard Investments, Emerson Collective, Capricorn, Social Capital, Tribe, Schmidt Family Foundation, Exor Seeds, Horizons Ventures.

## Key Technology
- Wind+solar (+engine) **extreme endurance** USVs; multi-sensor suites (radar, vision, AIS fusion, multibeam, acoustics)
- **Spectre**: silent-endurance ASW config (towed array/VDS) + stealth/effector config; designed for VLS-class mission effects
- **Surveyor**: deep-ocean mapping + undersea detection; Austal USA production
- **Voyager**: MDA workhorse; first Class-certified USV in class lineage
- **Explorer**: high-volume METOC workhorse
- AI classification + real-time C5ISR-T data delivery; GPS-denied operational experience

## Data & Measurement Needs
- **Primary data types**: Surface ISR (radar/EO/IR/AIS), acoustic ASW streams, multibeam bathymetry, sub-bottom, METOC (wind, waves, SST, pressure), satellite cueing overlays
- **Key measurements/parameters**: Contact tracks, acoustic signatures, seafloor depth/backscatter, hurricane eyewall met, GNSS-denied position error, endurance energy budgets
- **Observation platforms/programs**: Global Saildrone fleet; USCG/Navy/allied tasking; Seabed 2030-aligned mapping; hurricane reconnaissance heritage
- **Known data gaps**: Labeled multi-domain ASW datasets at scale; standardized autonomous kinetic ROE telemetry; Arctic/contested GNSS-denied basemaps
- **Interest in external data services**: Satellite MDA (SAR/RF), navy acoustic oceanography, metocean models for adaptive sampling, coalition track correlators

## Cross-Sector Connections
- **Defense ASV cluster**: Complements Saronic/Blue Water (ship-scale combatants) and Kraken Technology (high-speed modular USVs) with **sail-endurance ISR/ASW** niche; Lockheed effector path parallels defense prime integration pattern (HavocAI–Metal Shark)
- **Ocean Data & AI**: Managed data delivery competes/cooperates with Sofar (weather network) and XOCEAN (survey USVs) — Saildrone spans science METOC → defense ISR continuum
- **Marine Monitoring**: Longest open-ocean unmanned time-series moat in the tracked set
""",
        "jsonld": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Saildrone",
            "legalName": "Saildrone, Inc.",
            "url": "https://www.saildrone.com/",
            "description": "Autonomous unmanned surface vehicles for maritime defense, ocean intelligence, mapping, and METOC — fully managed persistent data and effects at sea.",
            "foundingDate": "2012",
            "founder": {"@type": "Person", "name": "Richard Jenkins", "jobTitle": "Founder & CEO"},
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Alameda",
                "addressRegion": "CA",
                "addressCountry": "US",
            },
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "USD",
                "value": 345000000,
                "description": ">$345M total incl. $60M EIFO-led (May 2025) and $50M Lockheed Martin strategic (Oct 2025)",
            },
            "sector": "Marine Monitoring & Sensors",
            "businessModel": "Fully managed autonomous USV missions delivering ocean/ISR data via Mission Portal+API; defense platform programs with effector integration path",
            "lastFundingRound": "Lockheed Martin $50M strategic (Oct 2025); prior $60M EIFO-led (May 2025)",
            "totalFunding": ">$345M",
            "investors": [
                "Bond",
                "EIFO",
                "Lockheed Martin",
                "Lux Capital",
                "Crowley",
                "XN",
                "Standard Investments",
                "Emerson Collective",
                "Capricorn Technology Impact Fund",
                "Social Capital",
                "Tribe Capital",
                "Schmidt Family Foundation",
                "Exor Seeds",
                "Washington Harbor Partners",
                "Academy Securities",
                "Pinegrove",
            ],
            "knowsAbout": [
                "Autonomous surface vehicles",
                "Maritime domain awareness",
                "Anti-submarine warfare USVs",
                "Ocean mapping",
                "METOC unmanned observations",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Surface ISR",
                    "Acoustic ASW",
                    "Multibeam bathymetry",
                    "METOC",
                    "Satellite MDA overlays",
                ],
                "keyMeasurements": [
                    "Contact tracks",
                    "Acoustic signatures",
                    "Depth/backscatter",
                    "Hurricane met",
                    "GNSS-denied navigation error",
                ],
                "observationPlatforms": [
                    "Explorer/Voyager/Surveyor/Spectre fleet",
                    "Mission Portal",
                    "Allied navy/USCG tasking",
                ],
                "knownGaps": [
                    "Labeled multi-domain ASW corpora",
                    "Autonomous kinetic ROE telemetry standards",
                ],
                "interestInExternalDataServices": "Satellite MDA, navy acoustic oceanography, metocean adaptive sampling models",
            },
        },
    },
]


def main():
    path = os.path.join(REPO, "sources", "companies.json")
    with open(path) as f:
        companies = json.load(f)
    existing = {c["name"].lower() for c in companies}
    added = []
    for c in COMPANIES:
        if c["name"].lower() in existing:
            print(f"SKIP already exists: {c['name']}")
            continue
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
    with open(path, "w") as f:
        json.dump(companies, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"companies.json: +{len(added)} → total {len(companies)}")

    for c in COMPANIES:
        slug = slugify(c["name"])
        with open(os.path.join(REPO, "raw", f"{slug}.md"), "w") as f:
            f.write(c["raw"].rstrip() + "\n")
        with open(os.path.join(REPO, "metadata", f"{slug}.jsonld"), "w") as f:
            json.dump(c["jsonld"], f, indent=2, ensure_ascii=False)
            f.write("\n")
        wiki = wiki_page(c["name"], c["url"], c["sector"], c["body"], c["description"])
        with open(os.path.join(REPO, "wiki", f"{slug}.md"), "w") as f:
            f.write(wiki.rstrip() + "\n")
        print(f"Wrote raw/metadata/wiki for {slug}")


if __name__ == "__main__":
    main()
