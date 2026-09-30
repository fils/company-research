#!/usr/bin/env python3
"""Generate profiles for 2026-09-30 daily company research run."""
import json, os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "2026-09-30"
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
        "name": "Andrenam",
        "url": "https://www.andrenam.com/",
        "sector": "Marine Monitoring & Sensors",
        "notes": "LA dual-use AI-native passive sonar: PEARL networked acoustic buoys + OBSIDIAN AI track/classify/alert. $18M Series A (Jul 2026) led Upfront Ventures; Valor, Also Capital, First Round; $30M total (prior $10M seed in 36h). COCO managed sensing. 35+ PEARL units, 4500+ in-water hours; Solid Curtain 2026, Lanternfish/UUVGRU-1. CEO Matej Cernosek (ex-SpaceX), CTO Alex Chu.",
        "description": "AI-native distributed passive sonar (PEARL buoys + OBSIDIAN); $18M Series A Jul 2026; $30M total; LA dual-use undersea MDA.",
        "raw": """# Andrenam – Raw Web Extract
**Source:** https://www.andrenam.com/
**Also:** https://andrenam.com/news/andrenam-announces-18-million-series-a-to-expand-persistent-undersea-awareness
**Also:** https://www.tectonicdefense.com/exclusive-underwater-sensing-startup-andrenam-raises-18m/
**Extracted:** 2026-09-30

## Overview
Los Angeles dual-use company building AI-powered distributed maritime sensing for persistent undersea awareness from surface to seabed. Turns underwater sound into real-time tracks, classifications, and alerts usable by operators without specialized sonar training.

## Products
- **PEARL**: persistent, rapidly deployable, mass-manufacturable buoy with suspended passive sonar array; streams acoustic data via satellite. 35+ units across 3 generations; 4,500+ in-water hours (CA/WA coasts). Gen 4 designed for scale (Series A purpose).
- **OBSIDIAN**: AI signal-processing platform — detect, track, classify, display underwater vessel probabilities; plug into any C2 / common operating picture. Zero-sonar-experience operators.

## Business model
- **Contractor Owned, Contractor Operated (COCO)** managed sensing: customers buy persistent coverage and actionable intelligence rather than owning/maintaining complex sonar systems.
- Markets: defense, homeland security, port security, critical infrastructure, commercial maritime, counter-UUV, energy/offshore.

## Funding
- **$18M Series A** (announced ~Jul 23, 2026) led by **Upfront Ventures** (Mark Suster); Valor Equity Partners, Also Capital, First Round Capital. Total funding **$30M**.
- Prior **$10M seed** closed in 36 hours, led by First Round Capital.
- Investors shown on site: Upfront, Valor, First Round, Also Capital, Long Journey, Banter, 201 Ventures, Wave Function Ventures.

## Team / traction
- Co-founder/CEO Matej Cernosek (ex-SpaceX engineer)
- Co-founder/CTO Alex Chu
- Demos: Solid Curtain 2026 (US Navy fleet exercise); Lanternfish with UUVGRU-1
- Two Navy contracts pending announcement (per Tectonic interview)
- Media: andrenam@weareinvariant.com (Kevin Boland)

## Marine data angle
Core product IS undersea acoustic intelligence — wide-area passive sonar data, AI classification, C2 fusion. Extreme demand for acoustic training labels, ocean ambient noise models, bathymetry for propagation, and multi-static fusion with AIS/radar/optical (e.g. Quartermaster surface layer).
""",
        "wiki_body": """## Overview
**Andrenam** (Los Angeles) is a dual-use company building an **AI-native distributed passive sonar network** for persistent undersea domain awareness. Hardware **PEARL** buoys collect acoustic data; software **OBSIDIAN** turns it into tracks, classifications, and alerts for operators with zero sonar training — closing the gap between scarce specialist systems and the scale of undersea threats (UUVs, semi-submersibles, peer submarine fleets).

## Business Model
- **COCO managed sensing**: Contractor Owned, Contractor Operated — sell persistent coverage and intelligence, not complex systems to own
- Markets: defense MDA, homeland/port security, critical infrastructure, energy/offshore, counter-UUV, commercial maritime
- Full-stack: hardware + AI software + field operations

## Funding
- **$18M Series A** (Jul 2026) led by **Upfront Ventures**; Valor Equity Partners, Also Capital, First Round Capital
- **$30M total** (prior $10M seed in 36 hours, First Round–led)
- Additional backers: Long Journey, Banter, 201 Ventures, Wave Function Ventures

## Key Technology
- **PEARL**: mass-manufacturable networked buoy with suspended passive sonar array; satcom uplink; 35+ units, 3 gens, 4,500+ in-water hours; Gen 4 for production scale
- **OBSIDIAN**: off-board AI fusion — detect/track/classify underwater vessels; C2/COP integration
- Demos: Solid Curtain 2026; Lanternfish with Navy UUVGRU-1
- Leadership: CEO Matej Cernosek (ex-SpaceX), CTO Alex Chu

### Data & Measurement Needs
- **Primary data types:** Passive acoustic time-series; multi-buoy array geometry; satcom telemetry; AI track/classification outputs; C2 fusion feeds; ambient noise models; bathymetry for propagation
- **Key measurements/parameters:** Bearing/range estimates; source classification probabilities (sub, UUV, surface, marine mammal); SNR; array health; deployment duration; false-alarm rates
- **Observation platforms/programs:** Distributed PEARL buoy fields; Navy exercise embeds; coastal CA/WA long-duration deployments; COCO managed networks
- **Known data gaps:** Labeled undersea acoustic corpora at commercial scale; real-time multi-static fusion with surface AIS/optical/radar; shallow-water clutter models
- **Interest in external data services:** Very high — bathymetry, sound-speed profiles, AIS/RF surface truth (e.g. Quartermaster), weather/sea-state for noise, mammal call libraries

## Cross-links
[Marine Monitoring & Sensors](marine-monitoring-sensors.md) · [Ocean Data & AI](ocean-data-ai.md) · [Quartermaster](quartermaster.md) · [Maritime Robotics](maritime-robotics.md) · [Sofar Ocean](sofar-ocean.md)
""",
    },
    {
        "name": "REGENT Craft",
        "url": "https://www.regentcraft.com/",
        "sector": "Offshore Energy",
        "notes": "All-electric Seaglider wing-in-ground craft (float/foil/fly) for coastal passenger + dual-use defense. $240M Series B Aug 2026 (equity+debt) co-led Mare Liberum + AE Ventures; DCVC, Founders Fund, Caffeinated Capital, Lockheed Martin Ventures, Japan Airlines, Giant Step; Erebor Bank debt. >$340M total. First human-crewed Viceroy flight Sep 2 2026. North Kingstown RI. CEO Billy Thalheimer. Adjacent to Vessev hydrofoil thesis at larger dual-use scale.",
        "description": "All-electric Seaglider maritime craft; $240M Series B Aug 2026; >$340M total; first crewed Viceroy flight Sep 2026.",
        "raw": """# REGENT Craft – Raw Web Extract
**Source:** https://www.regentcraft.com/
**Also:** https://www.regentcraft.com/news/regent-secures-240-million-series-b-funding-to-scale-seaglider-manufacturing-and-transform-maritime-mobility
**Also:** Dealroom note Aug 2026 REGENT $240M Series B
**Extracted:** 2026-09-30

## Overview
North Kingstown, Rhode Island developer of all-electric Seaglider™ vessels — hydrofoiling wing-in-ground-effect craft that operate exclusively over water in three modes: float on hull, foil, fly in ground effect. Zero-emission coastal/regional mobility for passengers and dual-use defense (REGENT Defense).

## Product
- **Viceroy**: flagship 12-passenger Seaglider; ~160–180 nm range on current batteries; ~180 mph class speed claims on marketing
- **Squire**: autonomous drone Seaglider variant (defense/commercial)
- Modes: Float. Foil. Fly.
- Partners: ferry operators, airlines, logistics (Japan Airlines, Brittany Ferries, Alaska Air adjacency, ADNOC, NEOM, Ørsted listed among partner logos), Lockheed Martin Ventures on investor side

## Funding
- **$240M Series B** (Aug 27, 2026) — equal mix equity and debt
  - Co-led: Mare Liberum, AE Ventures
  - Equity: DCVC, Founders Fund, Caffeinated Capital, Lockheed Martin Ventures, Japan Airlines, Giant Step Capital
  - Debt: Erebor Bank
- Total funding **>$340M**
- Among largest US hardware Series B rounds (Dealroom ~98th percentile of comparable set)

## Milestones
- Sep 2, 2026: world's first human-crewed Seaglider flight (Viceroy)
- Jul 2025: REGENT Defense positioning for national security
- CEO Billy Thalheimer

## Marine data needs
Certification, route planning, and operations require high-res coastal metocean (waves, wind, sea state), AIS traffic, bathymetry/obstacles, icing/visibility, and defense MDA feeds for dual-use missions.
""",
        "wiki_body": """## Overview
**REGENT Craft** (North Kingstown, RI) builds **all-electric Seaglider™** vessels — hydrofoiling **wing-in-ground-effect** craft that **float, foil, and fly** exclusively over water. Targets zero-emission coastal passenger mobility (half aircraft ticket cost narrative) and dual-use **REGENT Defense** missions. Flagship **Viceroy** (12 pax); autonomous **Squire** variant.

## Business Model
- Manufacture and sell/lease Seagliders to ferry operators, airlines, logistics, and defense
- Scale manufacturing + certification pipeline with Series B capital
- Dual commercial + defense GTM (Japan Airlines + Lockheed Martin Ventures on cap table signals both ends)

## Funding
- **$240M Series B** (Aug 27, 2026) — ~50/50 equity/debt; co-led **Mare Liberum** + **AE Ventures**
- Participants: DCVC, Founders Fund, Caffeinated Capital, Lockheed Martin Ventures, Japan Airlines, Giant Step Capital; debt **Erebor Bank**
- **>$340M total** funding

## Key Technology
- Wing-in-ground-effect + hydrofoil multimodal craft
- 100% battery-electric propulsion
- First **human-crewed Viceroy flight** (Sep 2, 2026)
- CEO Billy Thalheimer
- Partner logos span ferries, airlines, energy (Ørsted, TotalEnergies), logistics

### Data & Measurement Needs
- **Primary data types:** Coastal metocean forecasts; high-res wave/wind/sea-state; AIS traffic density; bathymetry and obstacle databases; icing/visibility; route corridor digital twins; flight-test telemetry
- **Key measurements/parameters:** Significant wave height, period, direction; wind speed/gusts; sea surface conditions for foil/fly mode transitions; traffic separation; battery SOC vs range under real sea state
- **Observation platforms/programs:** Onboard flight-test sensors; coastal weather networks; AIS; partner airline/ferry ops data
- **Known data gaps:** Certified performance envelopes vs real coastal sea states; dual-use MDA fusion for defense variants
- **Interest in external data services:** High — Sofar-class marine weather, coastal radar, AIS analytics (Quartermaster/Orca AI adjacency)

## Cross-links
[Offshore Energy](offshore-energy.md) · [Vessev](vessev.md) · [Fleetzero](fleetzero.md) · [Maritime Operations & Analytics](maritime-operations-analytics.md) · [Sea Machines Robotics](sea-machines-robotics.md)
""",
    },
    {
        "name": "CorPower Ocean",
        "url": "https://corpowerocean.com/",
        "sector": "Offshore Energy",
        "notes": "Swedish/Portuguese wave energy pioneer; heart-inspired phase-control WEC claims ~5x energy per tonne vs prior art. C4 utility-scale generating in Atlantic (Portugal); DNV prototype certification Jul 2026 (world-first for wave). €40M EU Innovation Fund for 10MW VianaWave; €19M Horizon Europe; EIC/Algebris etc. May 2026 growth capital noted on Dealroom (~$61.6M class with EIC Fund). CorPack 10-30MW arrays. CEO Patrik Möller. Extreme metocean + environmental MRV needs.",
        "description": "Wave energy converters (heart-inspired WaveSpring); DNV-certified C4; EU €40M VianaWave 10MW farm; Atlantic grid power today.",
        "raw": """# CorPower Ocean – Raw Web Extract
**Source:** https://corpowerocean.com/
**Also:** https://corpowerocean.com/corpower-ocean-secures-world-first-dnv-certification-for-wave-energy-technology/
**Extracted:** 2026-09-30

## Overview
Wave energy company delivering point-absorber WECs inspired by the human heart's pumping (pre-tension + WaveSpring negative spring / phase control). Claims up to 5× more energy per tonne of equipment vs conventional wave devices; storm transparency up to 18.5 m waves. Utility-scale C4 generating power to grid in the Atlantic off northern Portugal.

## Technology
- Heart-inspired pneumatic pre-tension + WaveSpring phase control
- Lightweight buoy optimized for energy capture then detuned in storms
- **CorPack** modular clusters: 10–30 MW per array; path to GW-scale
- DNV Prototype Certificate (Jul 2026) — company claims world-first for wave energy technology
- HiWave-5 demonstration program; VianaWave 10 MW farm path

## Funding / public capital
- €40M EU Innovation Fund for VianaWave 10 MW wave farm (Portugal)
- €19M Horizon Europe support (Valiant / EMEC Billia Croo 5 MW path among projects)
- EIC Accelerator historical awards; May 2026 Dealroom lists growth round participation including EIC Fund, Algebris, Acario, Tokyo Gas CVC, GTT Strategic Ventures (~$61.6M class combined narrative)
- CEO Patrik Möller; Portugal Deputy Minister of Energy site visit Sep 2026

## Business model
- Sell/partner utility-scale wave farms and CorPack arrays to energy providers
- Complement wind/solar for firm clean power (case studies: reduce overbuild/storage; West Coast data-center 24/7 mix narrative)

## Marine data needs
Continuous wave spectra, currents, bathymetry, structural health, grid interconnection metocean, environmental monitoring (marine mammals, benthic), and long-duration power-performance MRV.
""",
        "wiki_body": """## Overview
**CorPower Ocean** develops **point-absorber wave energy converters** using heart-inspired **phase control** (pneumatic pre-tension + **WaveSpring**). Claims up to **5× energy per tonne** vs prior wave devices, with storm “transparency” proven in Atlantic conditions (waves to ~18.5 m). Utility-scale **C4** units are generating grid power off northern Portugal; **CorPack** clusters target 10–30 MW arrays.

## Business Model
- Utility-scale wave farms and modular CorPack deployments for energy providers and coastal nations
- Position wave as firming complement to wind/solar (lower system overbuild and storage)
- Project development with EU Innovation Fund / Horizon support (VianaWave 10 MW; EMEC paths)

## Funding & Milestones
- **€40M EU Innovation Fund** — VianaWave 10 MW farm (Portugal)
- **€19M Horizon Europe** project support
- **DNV Prototype Certificate** (Jul 2026) — claimed world-first for wave energy tech
- Growth-capital narrative (Dealroom May 2026) with EIC Fund, Algebris, Acario, Tokyo Gas CVC, GTT Strategic Ventures
- CEO **Patrik Möller**; Portuguese energy ministry visit Sep 2026

## Key Technology
- Phase-controlled point absorber; lightweight storm-survivable buoy
- Modular CorPack architecture for volume manufacturing
- Operational Atlantic generation (not lab-only)

### Data & Measurement Needs
- **Primary data types:** Wave spectra and directional seas; currents; bathymetry; structural loads/SHM; power-performance time series; environmental (PAM marine mammals, benthic, bird); grid metocean
- **Key measurements/parameters:** Hs, Tp, direction; device heave/PTO metrics; capacity factor; storm survival events; acoustic emissions; scour
- **Observation platforms/programs:** On-device SCADA; wave buoys; Portugal/EMEC demonstration sites; environmental baseline surveys
- **Known data gaps:** Multi-year array wake/interaction models; standardized wave-farm MRV for offtake contracts; coastal data-center 24/7 firming validation datasets
- **Interest in external data services:** High — Sofar/spotter-class wave networks, Copernicus marine, PAM services, offshore wind co-location metocean

## Cross-links
[Offshore Energy](offshore-energy.md) · [Panthalassa](panthalassa.md) · [Oshen](oshen.md) · [Sizable Energy](sizable-energy.md) · [Ocean Data & AI](ocean-data-ai.md)
""",
    },
    {
        "name": "Scoot Science",
        "url": "https://scootscience.com/",
        "sector": "Aquaculture",
        "notes": "Ocean intelligence software: SeaFarer (commercial fishing trip planning/catch analytics) + SeaState (aquaculture digital twin — 10-day site forecasts, HAB/hypoxia mitigation, welfare metrics). Claims 2-3× fewer major mortality events, 34% daily mortality cut, 30-44% fewer operational stressors. Customers Cermaq Canada, Grieg BC since ~2019. StartBlue OEA Scale track Sep 2026. Integrates Blue Ocean Gear Smart Buoys + Deckhand e-logbook.",
        "description": "SeaFarer + SeaState ocean intelligence for fishing and aquaculture; StartBlue Scale 2026; Cermaq/Grieg customers.",
        "raw": """# Scoot Science – Raw Web Extract
**Source:** https://scootscience.com/
**Also:** StartBlue Ocean Enterprise Accelerator Scale cohort (Sep 2026) — Ocean News
**Extracted:** 2026-09-30

## Overview
Ocean analytics software for commercial fishing and aquaculture. Products: SeaFarer (fishermen) and SeaState (fish farmers) — turn ocean and ops data into operational intelligence and welfare metrics.

## Products
- **SeaFarer**: trip planning with real-time ocean forecasts; catch logging (manual or auto sync with Blue Ocean Gear Smart Buoys and Deckhand electronic logbook); pattern analysis from own historical data
- **SeaState**: aquaculture digital twin / common operating picture; 10-day site-specific ocean forecasts for HAB, low oxygen, upwelling mitigation; semantic models map env/bio/ops data → fish welfare metrics
  - Claimed outcomes: 2–3× reduction in major mortality events; 34% reduction in daily mortality; 30–44% reduction in operational stressors

## Customers / proof
- Cermaq Canada (customer since 2019) — Brock Thomson, Innovation Director quote on centralized data decision-making
- Grieg BC — Kirstyn Hallberg, Environmental Specialist — daily sensor monitoring + forecast-driven HAB/hypoxia mitigation

## Stage
- StartBlue Ocean Enterprise Accelerator **Scale** track (UCSD/Scripps + Rady), Sep 2026 cohort — eligible up to $150K non-dilutive

## Marine data needs
Site-calibrated SST, DO, chlorophyll/HAB proxies, currents, salinity, sensor streams from farm sites, vessel/gear IoT, forecast model skill scores, welfare/mortality ground truth.
""",
        "wiki_body": """## Overview
**Scoot Science** provides **ocean intelligence software** for commercial fishing and aquaculture: **SeaFarer** (trip planning, catch analytics) and **SeaState** (aquaculture digital twin with multi-day site forecasts and fish-welfare metrics). Positioned at the ops layer between raw ocean sensors and farm/fleet decisions.

## Business Model
- SaaS ocean/ops intelligence for fishermen and fish farmers
- Integrations: Blue Ocean Gear Smart Buoys, Deckhand e-logbook
- Enterprise aquaculture accounts (Cermaq, Grieg BC)

## Funding & Stage
- **StartBlue OEA Scale** cohort (Sep 2026) — UCSD Scripps + Rady; Scale track up to $150K non-dilutive eligibility
- Commercial traction since ~2019 with major salmon producers (not pure pre-revenue)

## Key Technology
- **SeaState**: 10-day site-specific forecasts; HAB / hypoxia / upwelling early warning; semantic welfare models; claimed 2–3× fewer major mortality events, ~34% lower daily mortality, 30–44% fewer operational stressors
- **SeaFarer**: forecast-informed trip planning + catch/condition logging + historical pattern mining
- Common operating picture across multi-site farms

### Data & Measurement Needs
- **Primary data types:** In-situ farm sensors; SST/DO/chl forecasts; vessel and gear IoT; catch logs; mortality/welfare events; model ensembles
- **Key measurements/parameters:** Dissolved oxygen, temperature, salinity, chlorophyll/HAB indicators, current/upwelling indices, feed/handling stress proxies, mortality rates
- **Observation platforms/programs:** Farm sensor networks; Blue Ocean Gear buoys; e-logbooks; StartBlue/ocean-enterprise validation
- **Known data gaps:** High-resolution nearshore HAB species ID; farm-microclimate downscaling; cross-site transfer learning without sharing raw competitor data
- **Interest in external data services:** Very high — coastal ocean models, satellite SST/ocean color, eDNA/HAB labs (Lucendi-class), BiOceanOr-style biology+AI forecasts

## Cross-links
[Aquaculture](aquaculture.md) · [BiOceanOr](bioceanor.md) · [NeuralX](neuralx.md) · [Ocean Data & AI](ocean-data-ai.md) · [Sofar Ocean](sofar-ocean.md)
""",
    },
    {
        "name": "Cetocean",
        "url": "https://www.cetocean.com/",
        "sector": "Ocean Data & AI",
        "notes": "Ocean intelligence platform starting with super-resolution sea-surface temperature for aquaculture, coastal tourism, and insurance/reinsurance parametric products. Humpback tool beta Sep 2026. StartBlue Launch cohort Sep 2026. Farm-level marine heatwave exposure pricing narrative.",
        "description": "Super-resolution SST risk intelligence for aquaculture, tourism, and insurers; StartBlue Launch 2026; Humpback beta.",
        "raw": """# Cetocean – Raw Web Extract
**Source:** https://www.cetocean.com/
**Extracted:** 2026-09-30

## Overview
Ocean intelligence platform converting ocean/coastal environmental data into high-resolution risk intelligence. Starting product: super-resolution sea-surface temperature (SST) for parties that feel warming first — aquaculture, coastal tourism, and their insurers.

## Product
- Super-resolution SST / marine heatwave exposure at farm and site level
- **Humpback** tool launching in beta (Sep 1, 2026)
- Built for actuarial-grade temperature records (parametric and indemnity insurance)

## Markets
- Aquaculture: stock density, harvest timing, mortality risk tied to temperature
- Insurance & reinsurance: underwrite parametric/indemnity against transparent high-res temperature record
- Coastal tourism (adjacent)

## Stage
- Joining **StartBlue Accelerator Launch** track (Sep 1, 2026 announcement)
- Early product/beta

## Marine data needs
Multi-sensor SST inputs (satellite + in-situ), coastal downscaling training labels, farm mortality/heatwave loss histories, reanalysis fields, uncertainty quantification for actuarial use.
""",
        "wiki_body": """## Overview
**Cetocean** builds an **ocean intelligence platform** that turns coastal environmental data into **high-resolution risk products**, starting with **super-resolution sea-surface temperature (SST)** for aquaculture, coastal tourism, and insurance/reinsurance.

## Business Model
- Risk intelligence / data products for farms and insurers (parametric + indemnity)
- Farm-level marine heatwave exposure for operational and underwriting decisions
- Early-stage StartBlue Launch company expanding ocean data product line beyond SST

## Funding & Stage
- **StartBlue OEA Launch** cohort (Sep 2026) — early-stage; up to $20K non-dilutive eligibility on program completion
- **Humpback** tool beta (Sep 2026)

## Key Technology
- Super-resolution SST generation from coarser ocean/coastal inputs
- Actuarial-oriented transparent temperature records
- Roadmap: additional ocean risk data products

### Data & Measurement Needs
- **Primary data types:** Satellite SST; in-situ temperature moorings/loggers; reanalysis; farm loss/mortality labels; coastal bathymetry for downscaling
- **Key measurements/parameters:** SST at farm scale; marine heatwave intensity/duration; uncertainty bands for parametric triggers
- **Observation platforms/programs:** Public SST missions; aquaculture site sensors; StartBlue validation partners
- **Known data gaps:** Labeled coastal super-res training sets; insurer-accepted uncertainty standards; multi-hazard fusion (SST + DO + HAB)
- **Interest in external data services:** Very high — Copernicus/NOAA SST, Sofar in-situ, Scoot/BiOceanOr farm ops ground truth

## Cross-links
[Ocean Data & AI](ocean-data-ai.md) · [Climate Risk](climate-risk.md) · [Scoot Science](scoot-science.md) · [Aquaculture](aquaculture.md) · [Sofar Ocean](sofar-ocean.md)
""",
    },
]

created = 0
for c in COMPANIES:
    slug = slugify(c["name"])
    tag = sector_tag(c["sector"])
    # raw
    with open(os.path.join(REPO, "raw", f"{slug}.md"), "w") as f:
        f.write(c["raw"])
    # metadata JSON-LD
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

# Update Quartermaster notes in-place
for co in cos:
    if co["name"] == "Quartermaster":
        co["notes"] = (
            "SmartMast distributed maritime sensing on commercial vessels (pro-mariner free hardware). "
            "$140M raise Sep 28 2026: $100M Series B led Insight Partners + Overmatch Ventures + First Round, Quiet Capital, Steel Atlas, TMV, BoxGroup, Operator Partners; $40M Stifel venture debt. "
            "Prior $43M Series A May 2026 (First Round + Quiet). 650+ vessels equipped / 800+ shipped across 25 countries; tens of GB/day per mast; fleet-scale rollouts starting. "
            "Hormuz/jamming narrative drives insurer + energy demand. CEO Neil Sobin. Arlington, VA. Ocean Data & AI."
        )
        co["last_updated"] = DATE
        print("Updated: Quartermaster")
    if co["name"] == "Maritime Robotics":
        co["notes"] = (
            "Norwegian USV pioneer (Trondheim, 2005). Growth round: Mustard Seed + Partners lead + Omnes Capital (announced Sep 28 2026) with EnvisionTech, Nysnø, Umoe, founders/employees. "
            "Prior ~€28M / $31M growth equity (Jun 2026 Dealroom). Hundreds of systems delivered; shift from pilots to fleet-level dual-use (civil survey + defense MDA). "
            "Scale production + international commercialization. CEO Vegard Evjen Hovstein."
        )
        co["last_updated"] = DATE
        print("Updated: Maritime Robotics")

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
