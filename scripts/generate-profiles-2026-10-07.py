#!/usr/bin/env python3
"""Generate profiles for 2026-10-07 daily company research run."""
import json, os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "2026-10-07"
TS = f"{DATE}T00:00:00Z"

def slugify(name):
    slug = name.lower()
    for a, b in [("ø", "o"), ("æ", "ae"), ("å", "a"), ("ü", "u"), ("é", "e"), ("è", "e"), ("ö", "o"), ("ä", "a")]:
        slug = slug.replace(a, b)
    slug = re.sub(r"[^a-z0-9-]", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug

def sector_tag(sector):
    return re.sub(r"[^a-z0-9]+", "-", sector.lower()).strip("-")

COMPANIES = [
    {
        "name": "Online Oceans",
        "url": "https://onlineoceans.com/",
        "sector": "Marine Monitoring & Sensors",
        "notes": "UK dual-use solar-electric Scout USV (2.4m/80kg) + Tether browser C2 for persistent ocean data & MDA. £4M seed (Apr 30 2026) led Seraphim Space; Peter Rive (SolarCity), Quantum Systems founders (Thieser/Seibel), Koro Capital. Buy from £40k or data-as-a-service. Months on station (biofouling-limited); SS6 ops / SS8+ survive; Iridium+Starlink; BYOS payload (metocean, passive acoustics, acoustic modem harvest). Customers: ARIA, Ocean Infinity, Sofar, Royal Navy logos; first production sold out Apr 2026. Founded 2025 George Morton + Alistair Douglas. Dense low-cost fleet coverage model vs intermittent crewed ships.",
        "description": "UK Scout solar USV + Tether C2; £4M Seraphim seed Apr 2026; persistent ocean data/MDA fleets.",
        "raw": """# Online Oceans – Raw Web Extract
**Source:** https://onlineoceans.com/
**Also:** https://onlineoceans.com/scout-usv.html
**Also:** https://seraphim.vc/news/online-oceans-raises-4m-maritime-autonomy-seraphim-led/
**Also:** https://tech.eu/2026/04/30/online-oceans-raises-ps4m-to-scale-autonomous-fleets-for-maritime-security/
**Extracted:** 2026-10-07

## Overview
UK (London) dual-use ocean robotics company founded early 2025 by George Morton (CEO; maritime engineering) and Alistair Douglas (C2/fleet software). Builds low-unit-cost solar-electric USVs for dense, persistent maritime coverage — defence MDA, subsea infrastructure protection, border security, counter-drug, and commercial ocean data.

## Products
- **Scout USV**: 2.4 m, 80 kg solar-electric uncrewed surface vessel; one-person shore/boat launch; holds station or transits months; sea state 6 full ops, sea state 8+ survival, self-righting; Iridium + Starlink satcom; open payload bay (BYOS).
- Modules marketed: Scout Adapt (custom sensors), Detect (MDA/surveillance), Connect (comms/relay), Metocean, Hydrotwin (acoustics).
- Acoustic modem harvests data from subsea instruments / AUVs while surface platform streams to cloud.
- **Tether**: browser/phone cloud C2 — mission planner, live telemetry, swarm behaviours (Picket, Convoy, Cover), AIS/bathymetry/weather layers, alerts, optional manual piloting.

## Business model
- Outright purchase from **£40,000**/unit
- **Ocean data-as-a-service**: Online Oceans owns/operates Scouts, delivers QC data to customer cloud/API (no capex)
- Recurring software/data revenue thesis on top of hardware fleet scale
- Claimed ~200× cheaper than crewed ship coverage for persistent station-keeping

## Funding
- **£4M seed** (~$5.4M) announced **30 Apr 2026**, led by **Seraphim Space**
- Participants: Peter Rive (SolarCity co-founder), Frank Thieser & Florian Seibel (Quantum Systems founders), **Koro Capital**
- Use of proceeds: scale manufacturing, deployments, defence + commercial GTM

## Traction
- Initial customers across defence, MDA, ocean data; first data sales begun
- First months of production sold out ahead of commercial deliveries Apr 2026
- Homepage trust logos include ARIA, BlueOasis, Ocean Infinity, Applied Ocean Sciences, Sofar, SensorTech Canada, Sonardyne, Royal Navy, SynMax

## Marine data angle
Core product is persistent surface+subsurface metocean and acoustic sensing at fleet density. Extreme need for sensor QC, biofouling mitigation schedules, ambient noise models, bathymetry for station-keeping, and fusion with AIS/satellite MDA layers.
""",
        "wiki_body": """## Overview
**Online Oceans** (UK, founded 2025) builds **Scout** — a compact **solar-electric USV** (2.4 m / 80 kg) — and **Tether**, a browser-based fleet C2 platform. Thesis: persistent maritime coverage has been too expensive; dense low-cost fleets enable continuous monitoring of borders, subsea cables, chokepoints, and ocean data stations instead of intermittent crewed missions.

## Business Model
- Hardware sale from **£40k**/Scout **or** fully managed **data-as-a-service** (company operates fleet, delivers QC data/API)
- Dual-use GTM: defence MDA / ASW / infrastructure protection + commercial ocean observation
- Swarm software (Picket / Convoy / Cover) as recurring software/data layer
- Founders: CEO George Morton; C2 lead Alistair Douglas

## Funding
- **£4M seed** (30 Apr 2026) led by **Seraphim Space**
- Angels/strategic: Peter Rive (SolarCity), Quantum Systems founders, **Koro Capital**
- Production ramp within ~1 year of founding; early production sold out for Apr 2026 deliveries

## Key Technology
- Solar-electric endurance measured in **months** (biofouling is practical limit)
- **SS6** operations / **SS8+** survival; self-righting; van-transportable single-person launch
- Iridium + Starlink; BYOS payload (metocean, passive acoustics, custom)
- Acoustic modem bridges surface satcom to seabed instruments/AUVs
- Tether: multi-layer planner (route, bathy, AIS, weather), live hydrophone spectrograms, swarm tasking

### Data & Measurement Needs
- **Primary data types:** Metocean time-series; passive acoustic streams; satcom telemetry; swarm state; AIS fusion layers; QC ocean data products for DaaS customers
- **Key measurements/parameters:** Wave Hs/period, wind, SST, pressure, salinity; acoustic detections (vessels, mammals); station-keeping error; power/solar budget; biofouling indicators
- **Observation platforms/programs:** Scout fleets as virtual anchors or transect surveyors; defence MDA pickets; commercial ocean-data missions; subsea instrument harvest relays
- **Known data gaps:** Long-endurance sensor calibration drift; multi-Scout acoustic localization; real-time fusion with satellite RF/optical MDA
- **Interest in external data services:** Very high — bathymetry charts, global AIS, weather/tide models, sound-speed profiles, customer-owned sensor payloads

## Cross-links
[Marine Monitoring & Sensors](marine-monitoring-sensors.md) · [Ocean Data & AI](ocean-data-ai.md) · [Sofar Ocean](sofar-ocean.md) · [Maritime Robotics](maritime-robotics.md) · [Saildrone](saildrone.md) · [Seasats](seasats.md) · [Andrenam](andrenam.md)
""",
    },
    {
        "name": "Terradepth",
        "url": "https://www.terradepth.com/",
        "sector": "Ocean Data & AI",
        "notes": "Austin/Cedar Park TX Ocean Operating System™: Absolute Ocean cloud ODaaS + self-recharging AxV hybrid AUV/ASV swim-pairs (Navy SEAL-founded). ~$28–30M raised ($8M seed Seagate-led; $20M Series A Apr 2022 Giant Ventures + Nimble Ventures). 2026: Absolute Ocean placed in NIWC Atlantic RCC Hopper (direct OT up to 24 mo); 5-yr offshore-energy MSA; AWS GovCloud FedRAMP IL4/IL5. Seafloor mapping + federated multi-source ocean intelligence for defense, energy, insurance, research. Dual-use autonomy stack.",
        "description": "OceanOS Absolute Ocean + AxV AUV fleet; ~$30M raised; NIWC Atlantic Hopper 2026; dual-use seabed ODaaS.",
        "raw": """# Terradepth – Raw Web Extract
**Source:** https://www.terradepth.com/
**Also:** https://www.terradepth.com/absolute-ocean/
**Also:** https://www.terradepth.com/company/
**Also:** https://www.businesswire.com/news/home/20260409951116/en/CORRECTING-and-REPLACING-Terradepths-Absolute-Ocean-Cleared-Selection-Process-and-Placed-in-NIWC-Atlantic-RCC-Hopper
**Also:** yespress.io/terradepth (funding + 2026 MSA notes)
**Extracted:** 2026-10-07

## Overview
Cedar Park / Austin, Texas dual-use maritime tech company founded 2018 by Navy SEALs and ocean technologists. Builds the **Ocean Operating System™**: autonomous long-range subsea vehicles plus **Absolute Ocean**, a cloud-native federated ocean data platform. Mission: make high-consequence ocean/seafloor data accessible, actionable, and secure for defense, energy, insurance, government, and research.

## Products / stack
- **Absolute Ocean (AO)**: cloud-native, API-first, data-agnostic platform — storage, aggregation, visualization, analysis, multi-stakeholder collaboration. Ingests proprietary fleet + third-party AUV/ASV/sensors + public sources (NOAA, EMODnet, satellite). AWS GovCloud; FedRAMP and IL4/IL5 compliance narrative for classified ops.
- **Robotics / AxV**: hybrid autonomous surface+underwater vehicles operating as collaborative swim-pairs (one dives while partner surfaces to recharge/relay) — SEAL dive-team analogy. Survey payloads: high-res bathymetry, imagery, water-column profiling; claimed deep range (up to ~6,000 m class in marketing materials).
- Applications layer: C2/decision support, infrastructure monitoring, resource mapping, acoustic threat/anomaly detection.

## Business model
- **Ocean Data as a Service (ODaaS)** — collect + deliver decision-ready seabed/ocean intelligence
- Survey services + platform licenses + dual-use defense programs
- Five-year master services agreement with major offshore-energy operator (reported; Asia-Pacific LNG terminal start)

## Funding & traction
- Seed ~$8M (Seagate Technology among early backers; earlier seed notes also cite Kleiner/Sound Ventures in some directories)
- **$20M Series A** (Apr 2022) co-led **Giant Ventures** + **Nimble Ventures**
- Total ~**$28–30M** disclosed equity
- **2026**: Absolute Ocean selected into **NIWC Atlantic Rapid Capabilities Cell (RCC) Hopper** after Phase II CSO pitch — enables direct prototype Other Transaction agreements up to 24 months for Navy sponsors
- Sectors served: defense & national security, maritime insurance, government/regulatory, scientific research, offshore energy (O&G + renewables)

## Marine data angle
Company is both collector (AUV fleet) and integrator (federated Absolute Ocean). Extreme demand for multi-sensor bathymetry standards, ATR training labels, acoustic comms performance data, and secure multi-enclave data sharing.
""",
        "wiki_body": """## Overview
**Terradepth** (Cedar Park / Austin, TX; founded 2018 by Navy SEALs) builds the **Ocean Operating System™**: long-endurance **AxV** hybrid AUV/ASV swim-pairs plus **Absolute Ocean**, a cloud-native federated platform for high-consequence seafloor and ocean intelligence. Dual-use across defense, offshore energy, insurance, government, and research.

## Business Model
- **Ocean Data as a Service (ODaaS)** — robots collect; Absolute Ocean delivers decision-ready maps and analytics
- Survey services + platform access + defense prototype/OT pathways
- Reported **5-year offshore-energy MSA** (global operator; Asia-Pacific LNG terminal start)
- Security posture: **AWS GovCloud**, FedRAMP, **IL4/IL5** narrative

## Funding
- Seed ~**$8M** (Seagate among early strategic backers)
- **$20M Series A** (Apr 2022) co-led **Giant Ventures** + **Nimble Ventures**
- Total disclosed equity ~**$28–30M**
- **2026 milestone**: Absolute Ocean placed in **NIWC Atlantic RCC Hopper** (post Phase II CSO) — Navy sponsors can execute direct prototype OTs up to 24 months

## Key Technology
- Collaborative **swim-pair** autonomy (surface relay/recharge + submerged surveyor)
- Multibeam/imagery/water-column payloads; deep-ocean survey claims
- Absolute Ocean: API-first federation of proprietary + third-party + public ocean datasets (NOAA, EMODnet, satellite)
- Apps: C2, infrastructure monitor, resource mapping, acoustic anomaly/threat classification

### Data & Measurement Needs
- **Primary data types:** High-res bathymetry; sidescan/SAS imagery; water-column profiles; vehicle nav/state; federated multi-source ocean GIS; ATR labels; acoustic comms logs
- **Key measurements/parameters:** Depth, backscatter, feature detections, positioning accuracy, mission endurance/range, data latency shore-to-cloud
- **Observation platforms/programs:** AxV fleets; partner AUV/ASV ingest; Navy UNIT/Hopper prototypes; offshore energy survey campaigns
- **Known data gaps:** Persistent deep-ocean revisit cadence; cross-vendor payload interoperability; labeled undersea object corpora at fleet scale
- **Interest in external data services:** High — public chart/satellite baselines, third-party AUV feeds, meteorological overlays, secure multi-party data rooms

## Cross-links
[Ocean Data & AI](ocean-data-ai.md) · [Marine Monitoring & Sensors](marine-monitoring-sensors.md) · [Bedrock Ocean Exploration](bedrock-ocean-exploration.md) · [XOCEAN](xocean.md) · [Saildrone](saildrone.md) · [Orpheus Ocean](orpheus-ocean.md) · [Sofar Ocean](sofar-ocean.md)
""",
    },
    {
        "name": "MarineLabs",
        "url": "https://marinelabs.io/",
        "sector": "Ocean Data & AI",
        "notes": "Victoria BC coastal intelligence: CoastAware real-time + AI 10-day hyperlocal wind/wave/weather from North America sensor fleet; CoastInsights historical/custom reports; BerthWatch berth depth. $4.5M seed Mar 2024 (BDC Sustainability VF lead + Seaspan); $4M seed extension Oct 22 2025 (BDC + InBC). Active 4 of Canada's 5 largest ports. CEO Dr Scott Beatty (wave energy R&D background). Ports, pilots, terminals, coastal engineers, government MDA/C-UxS. Largest Canadian ocean-tech seed narrative (2024).",
        "description": "Canadian CoastAware coastal weather AI + sensor fleet; $4.5M+ $4M seed; ports/pilots hyperlocal metocean.",
        "raw": """# MarineLabs – Raw Web Extract
**Source:** https://marinelabs.io/
**Also:** https://marinelabs.io/marinelabs-closes-4-million-investment-from-bdc-and-inbc-enabling-coastal-ai-at-scale/
**Also:** https://marinelabs.io/marinelabs-raises-largest-seed-round-in-canadian-ocean-technology-history/
**Also:** https://betakit.com/marinelabs-looks-to-bring-safety-to-oceans-following-4-5-million-seed-round/
**Extracted:** 2026-10-07

## Overview
Victoria, British Columbia coastal intelligence company founded 2017 by Dr. Scott Beatty (CEO; ocean deep-tech entrepreneur with wave-energy R&D, IEC standards, DOE/Wave Energy Scotland reviewer background). Operates a North America-wide fleet of rugged cloud-connected coastal sensors delivering hyper-local wind, wave, and weather intelligence for maritime safety and climate resilience.

## Products
- **CoastAware**: subscription platform — real-time observed data + bias-corrected / ML-enabled hyper-local **10-day forecasts** + camera imagery at pilot boarding stations, channel entrances, anchorages
- **CoastInsights**: historical data and customized analytical reports for coastal modelling, flood/erosion studies, vessel wake analysis
- **BerthWatch**: real-time berth depth monitoring and reporting
- Customers: port authorities, marine pilots, terminals, ferries/tugs, coastal engineers, government (MDA / tactical ISR / C-UxS coastal narrative on site)

## Business model
- SaaS / data subscription on proprietary sensor network
- Custom historical/insight reports
- Hardware+software integrated coastal weather intelligence (not pure software)

## Funding
- **$4.5M seed** (Mar 13, 2024) led by **BDC Capital Sustainability Venture Fund** with **Seaspan Shipyards** (National Shipbuilding Strategy value-prop) — marketed as largest Canadian ocean-tech seed at the time
- **$4M seed extension** (Oct 22, 2025) led again by **BDC Sustainability VF** with **InBC Investment Corp.**
- Earlier angel/seed participants noted in directories: Audrey Capital, Bond, BoxGroup, Founder Collective, iNovia, Jump, MATH VP, Precursor, Greg Kidd, et al.
- Use of funds: expand sensor network coverage + North American GTM

## Traction
- Active in **4 of Canada's 5 largest ports**
- New HQ opened Victoria (Dec 2025 announcement)
- Robert Allan Ltd. leveraged MarineLabs data on new ship design (May 2025)
- Port of San Diego Innovation Challenge participant listing (2026)

## Marine data angle
Product is dense coastal metocean observation + AI forecast bias-correction. Needs sensor QC, camera+metocean fusion, port digital twin layers, and climate-trend historical archives for engineers.
""",
        "wiki_body": """## Overview
**MarineLabs** (Victoria, BC; founded 2017) is a **coastal intelligence** company operating a North America-wide fleet of rugged, cloud-connected sensors. Flagship **CoastAware** combines real-time observations with ML-enabled hyper-local **10-day** wind/wave/weather forecasts for ports, pilots, terminals, and coastal engineers. CEO **Dr. Scott Beatty**.

## Business Model
- Subscription coastal weather intelligence (hardware network + SaaS)
- **CoastInsights** paid historical/custom analytics
- **BerthWatch** berth-depth monitoring
- GTM: port ops, pilotage, marine construction, government coastal MDA

## Funding
- **$4.5M seed** (Mar 2024) — **BDC Capital Sustainability Venture Fund** lead + **Seaspan Shipyards**
- **$4M seed extension** (Oct 22, 2025) — BDC + **InBC**
- Network expansion and North American commercial growth

## Key Technology
- Rapidly deployable coastal sensor units + buoy cameras
- Real-time + historical wind/wave/weather at action points (pilot stations, channels, anchorages)
- Bias-corrected AI forecasting layered on proprietary observations
- Vessel wake analysis and coastal engineering support datasets

### Data & Measurement Needs
- **Primary data types:** In-situ wind/wave/weather time-series; camera imagery; berth depth; AI forecast fields; historical climate/coastal engineering archives
- **Key measurements/parameters:** Significant wave height, period, direction; wind speed/gusts; visibility proxies; water level/berth depth; wake events
- **Observation platforms/programs:** Proprietary coastal sensor fleet across North American ports; partner engineering studies
- **Known data gaps:** Ultra-local channel microclimates; multi-port standardized QC; fusion with national buoy/satellite networks
- **Interest in external data services:** High — national buoy networks, satellite altimetry/SAR, AIS for wake correlation, storm-surge models

## Cross-links
[Ocean Data & AI](ocean-data-ai.md) · [Coastal Risk & Infrastructure](coastal-risk-infrastructure.md) · [Sofar Ocean](sofar-ocean.md) · [Brightband](brightband.md) · [Cetocean](cetocean.md) · [Quartermaster](quartermaster.md)
""",
    },
    {
        "name": "Bluesonde",
        "url": "https://www.bluesonde.com/",
        "sector": "Marine Monitoring & Sensors",
        "notes": "Portland ME (Roux Institute) scalable real-time water-quality monitoring buoy: solar+battery, LTE/sat/BT, 12-inch compact, patent-pending anti-fouling. Sensors: location, temp, conductivity, DO, turbidity, pH, chlorophyll+. Markets: ports/infrastructure, water management, aquaculture, research. Continuum/NOAA Ocean Enterprise TDC awardee ($1.2M cohort share among 14 startups via Braid Theory). Building network-scale water intelligence layer.",
        "description": "Scalable real-time WQ monitoring buoys (anti-fouling); Continuum/NOAA TDC; Portland ME Roux Institute.",
        "raw": """# Bluesonde – Raw Web Extract
**Source:** https://www.bluesonde.com/
**Also:** https://www.bluesonde.com/solutions
**Also:** https://www.bluesonde.com/about
**Also:** https://www.braidtheory.com/ (TDC awardee listing)
**Also:** Continuum/NOAA Ocean Enterprise TDC $1.2M to 14 startups (Braid Theory)
**Extracted:** 2026-10-07

## Overview
Bluesonde Technologies (Portland, Maine — Roux Institute / 100 Fore St) builds compact, scalable **real-time water quality monitoring buoys** for oceans, freshwater, and industrial waterways. Positions as the water data and intelligence layer for climate resilience, ports, aquaculture, and research.

## Product
- Solar power + long-life battery
- Connectivity: LTE | Satellite | Bluetooth
- Form factor: ~12 in (30 cm) diameter compact buoy
- Sensing suite: location, temperature, conductivity, dissolved oxygen, turbidity, pH, chlorophyll, expandable
- **Patent-pending anti-fouling** to cut maintenance and keep long-duration accuracy
- Rapid deploy; swap/add sensors without full system replacement
- Cloud integration with existing data platforms

## Markets
- Ports & infrastructure (navigation safety, dredging permits, ESG)
- Water management / environmental compliance
- Aquaculture site conditions and yield optimization
- Ocean/freshwater research continuous monitoring

## Funding / programs
- Selected among **14 Continuum / NOAA Ocean Enterprise TDC awardees** sharing **$1.2M** non-dilutive commercialization funding (Braid Theory network)
- Early-stage; equity round size not clearly disclosed on homepage as of extract date
- Team messaging: decades of marine ops hardware experience; engineering-partner model

## Marine data angle
Core is multi-parameter WQ time-series at scalable buoy density. Strong anti-fouling + calibration story. Natural fit for mCDR baseline/plume monitoring, aquaculture hypoxia/HAB early warning, and port environmental compliance.
""",
        "wiki_body": """## Overview
**Bluesonde** (Portland, ME — Roux Institute) builds compact **real-time water-quality monitoring buoys** designed to scale across oceans, freshwater systems, and industrial waterways. Emphasizes durability, **anti-fouling**, rapid deployment, and integration into existing data platforms — a hardware-enabled water intelligence layer for ports, aquaculture, research, and climate resilience.

## Business Model
- Sell/deploy monitoring buoys + sensing suites
- Engineering-partner deployments (custom configs)
- Network-scale water intelligence thesis (many nodes, continuous data)
- Public program traction via **Continuum / NOAA Ocean Enterprise TDC** (one of 14 awardees in $1.2M cohort)

## Funding
- **NOAA-backed Continuum TDC** non-dilutive award (cohort total $1.2M across 14 startups; Braid Theory)
- Equity financing not prominently disclosed on site as of 2026-10-07

## Key Technology
- ~12\" solar+battery buoy; LTE / satellite / Bluetooth
- Multi-parameter suite: T, conductivity, DO, turbidity, pH, chlorophyll, location (+ expandable)
- Patent-pending **anti-fouling** for long-duration reliability
- Modular sensor swap without full system rip-and-replace

### Data & Measurement Needs
- **Primary data types:** Continuous multi-parameter WQ streams; buoy health/telemetry; geospatial deployment grids
- **Key measurements/parameters:** Temperature, salinity/conductivity, dissolved oxygen, pH, turbidity, chlorophyll-a; biofouling/maintenance indicators
- **Observation platforms/programs:** Port/harbor arrays; aquaculture farm grids; research moorings; industrial outfall monitoring
- **Known data gaps:** Cross-site calibration standards; HAB species discrimination beyond chlorophyll proxy; carbonate chemistry (TA/DIC) not in base suite
- **Interest in external data services:** High — satellite ocean color, hydrodynamic models, aquaculture farm ops data, mCDR MRV baselines

## Cross-links
[Marine Monitoring & Sensors](marine-monitoring-sensors.md) · [Aquaculture](aquaculture.md) · [Ocean Carbon Sequestration](ocean-carbon-sequestration.md) · [Dottir Labs](dottir-labs.md) · [Ocean State Sensing](ocean-state-sensing.md) · [Innovasea](innovasea.md) · [BiOceanOr](bioceanor.md)
""",
    },
    {
        "name": "Actea",
        "url": "https://actea.earth/",
        "sector": "Ocean Data & AI",
        "notes": "Public benefit corp: ML transforms sparse public/proprietary ocean data into site-specific climate, mariculture, and mCDR decision products. Lagrangian Flux Decomposition mCDR model (air-sea flux + co-benefits); ML current resolution-enhancement (Kristiansen et al. Nature Sci Rep 2026); aqua-forecast.com nearshore farm forecasts. NOAA ACLIM contributor; DFO Canada MPA work; Norwegian Miljødirektoratet coastal species climate; supports Vesta OAE air-sea flux (Duck NC). Continuum/NOAA TDC awardee. CEO Jordan Miller (ex-RealityCap/Intel, Highbridge); CTO Dr Trond Kristiansen. info@actea.earth.",
        "description": "Ocean climate/mCDR/mariculture ML analytics PBC; Continuum TDC; Vesta + NOAA ACLIM; aqua-forecast.com.",
        "raw": """# Actea – Raw Web Extract
**Source:** https://actea.earth/
**Also:** https://www.f6s.com/company/actea-inc
**Also:** https://coastalscience.noaa.gov/products/actea-ocean-climate-analytics/
**Also:** Continuum/NOAA Ocean Enterprise TDC awardee listings
**Extracted:** 2026-10-07

## Overview
Actea Inc is a **public benefit corporation** that turns sparse, biased public ocean data into decision-ready, site-specific analyses for climate adaptation, mariculture, fisheries regulation, and marine CDR. Mission: help the world mitigate and adapt to climate change through responsible ocean use.

## Leadership
- **Jordan Miller** — Cofounder/CEO (RealityCap → Intel acquisition; VP Highbridge Capital structured credit; Caltech)
- **Dr. Trond Kristiansen** — Cofounder/CTO (ocean modelling scientist)
- Advisors include Dr. Halley E. Froehlich (UCSB aquaculture/climate), Dr. Eagle Jones (SLAM/AV), Samuel Makonnen

## Products / capabilities
- **Operations**: translate open-ocean forecasts into nearshore operational meaning
- **Mariculture**: site-specific forecasts (days→years); growth/pest/mortality projections under changing T/chemistry; optimal site-shift analyses 2000s→2030s; try https://aqua-forecast.com
- **mCDR**: statistical **Lagrangian Flux Decomposition** model quantifying air-sea flux and environmental co-benefits/risks; complements dynamic models
- **ML ocean current resolution-enhancement** — Kristiansen et al. 2026 Nature Scientific Reports
- Climate projection validation — Kristiansen et al. 2024 Nature Sci Rep
- Custom ML datasets from public + proprietary inputs for regulators and operators

## Customers / collaborations
- NOAA **ACLIM** (Alaska climate-integrated modeling / Bering Sea fisheries)
- Fisheries and Oceans Canada — MPA value under climate change (FACETS paper)
- Norwegian Miljødirektoratet coastal species climate impacts
- Nunatsiavut Nation; EU FutureMARES
- **Vesta** — global air-sea flux modeling support for Duck, NC coastal enhanced weathering / OAE project
- Continuum / NOAA Ocean Enterprise **TDC** awardee (AI-powered decision-making using ocean data)

## Business model
- Contract analytics / custom dataset delivery for governments, scientists, mariculture operators, mCDR project developers
- Standard pricing available for fisheries regulators (upon request)
- PBC impact framing (stock management, farm carbon footprint, restoration siting, CDR efficiency)

## Marine data angle
Actea is pure analytics/model layer — voracious consumer of public ocean reanalyses, in-situ profiles, carbonate system fields, and proprietary farm/project observations. Bridges sparse science data to operator decisions for aqua and mCDR MRV-adjacent siting.
""",
        "wiki_body": """## Overview
**Actea** is a **public benefit corporation** that uses machine learning to transform sparse public and proprietary ocean data into **site-specific** decision products for climate adaptation, mariculture, fisheries regulation, and **marine CDR**. Cofounders: CEO **Jordan Miller**, CTO **Dr. Trond Kristiansen**.

## Business Model
- Contract custom analyses and datasets for governments, scientists, farm operators, and mCDR developers
- Nearshore **aqua-forecast** products (https://aqua-forecast.com)
- PBC mission: responsible ocean use for mitigation + adaptation
- Continuum / NOAA Ocean Enterprise **TDC** commercialization support

## Funding
- Continuum/NOAA **TDC** non-dilutive awardee (AI decision-making on ocean data)
- Equity rounds not prominently disclosed on homepage as of 2026-10-07

## Key Technology
- ML downscaling / resolution-enhancement of ocean currents (Kristiansen et al. 2026 *Nat Sci Rep*)
- Validated ocean climate projections (Kristiansen et al. 2024 *Nat Sci Rep*)
- **Lagrangian Flux Decomposition** statistical mCDR model — air-sea CO₂ flux + co-benefit/risk quantification
- Mariculture outcome models (growth, pests, mortality) under T/chemistry change; multi-decadal site-quality shift maps
- Collaborations: NOAA ACLIM, DFO Canada, Norwegian environment agency, **Vesta** Duck NC OAE flux support

### Data & Measurement Needs
- **Primary data types:** Ocean reanalyses; in-situ T/S/O₂/pH profiles; carbonate system fields; current fields; farm ops time-series; mCDR tracer/alkalinity observations
- **Key measurements/parameters:** Temperature, salinity, pH/Ω, nutrients, currents, air-sea CO₂ flux, species habitat suitability indices
- **Observation platforms/programs:** Public observing systems (Argo, gliders, coastal moorings); customer farm sensors; mCDR field pilots (e.g. Vesta)
- **Known data gaps:** Nearshore bias in global forecasts; sparse carbonate chemistry for mCDR MRV; farm-resolution pest/disease environmental drivers
- **Interest in external data services:** Very high — any dense coastal WQ/metocean (Bluesonde, MarineLabs, Innovasea), satellite SST/color, mCDR MRV partners (atdepth/Vycarb pattern)

## Cross-links
[Ocean Data & AI](ocean-data-ai.md) · [Climate Risk](climate-risk.md) · [Ocean Carbon Sequestration](ocean-carbon-sequestration.md) · [Aquaculture](aquaculture.md) · [Scoot Science](scoot-science.md) · [Cetocean](cetocean.md) · [Brightband](brightband.md) · [Vycarb](vycarb.md)
""",
    },
]

created = 0
for c in COMPANIES:
    slug = slugify(c["name"])
    tag = sector_tag(c["sector"])
    # raw
    with open(os.path.join(REPO, "raw", f"{slug}.md"), "w") as f:
        f.write(c["raw"].rstrip() + "\n")
    # metadata
    meta = {
        "@context": "https://schema.org",
        "@type": "Corporation",
        "name": c["name"],
        "url": c["url"],
        "description": c["description"],
        "sector": c["sector"],
        "lastUpdated": DATE,
    }
    with open(os.path.join(REPO, "metadata", f"{slug}.jsonld"), "w") as f:
        json.dump(meta, f, indent=2)
        f.write("\n")
    # wiki OKF
    wiki = f"""---
type: Company
title: {c['name']}
description: {c['description']}
resource: {c['url']}
tags:
- {tag}
timestamp: '{TS}'
date: '{DATE}'
sector: {c['sector']}
---

# {c['name']}

**Sector**: {c['sector']}
**Official Site**: {c['url']}

{c['wiki_body']}
"""
    with open(os.path.join(REPO, "wiki", f"{slug}.md"), "w") as f:
        f.write(wiki)
    created += 1
    print(f"Created: {slug}")

# Append to companies.json
path = os.path.join(REPO, "sources", "companies.json")
with open(path) as f:
    cos = json.load(f)

existing = {co["name"] for co in cos}
for c in COMPANIES:
    if c["name"] not in existing:
        cos.append({
            "sector": c["sector"],
            "name": c["name"],
            "url": c["url"],
            "notes": c["notes"],
            "last_updated": DATE,
        })
        print(f"JSON+: {c['name']}")

with open(path, "w") as f:
    json.dump(cos, f, indent=2)
    f.write("\n")

print(f"\nDone: {created} new profiles; companies.json now {len(cos)}")
