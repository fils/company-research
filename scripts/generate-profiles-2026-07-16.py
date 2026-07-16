#!/usr/bin/env python3
"""Generate profiles for 2026-07-16 autonomous run — 5 new companies."""
import json, os, re
from datetime import date

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = "2026-07-16"

def slugify(name):
    slug = name.lower()
    slug = slug.replace('ø', 'o').replace('æ', 'ae').replace('å', 'a')
    slug = slug.replace('ü', 'u').replace('é', 'e').replace('è', 'e')
    slug = re.sub(r'[^a-z0-9-]', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')

COMPANIES = [
    {
        "name": "Biosort",
        "url": "https://biosort.no/en",
        "sector": "Aquaculture",
        "notes": "Individual-based sea lice control + FishID AI/machine vision for salmon aquaculture. NOK 100M+ (~$10.4M) venture round (Feb 2026) from Grieg Kapital, Hatch Blue, IVC, Farvatn, Futurum Ventures + existing owners. Founded 2010 by former Tomra engineers; built on Cermaq iFarm development-license project (4 production cycles). FishID identifies/tracks individual salmon; early-stage parasite removal + individual health journals (lice count, growth, welfare). Goal: continuous lice removal to suppress population growth and reduce well-boat treatments. Research partners: Nofima, IMR, NMBU, Norwegian Veterinary Institute, SINTEF Ocean, NTNU. CEO Geir Stang Hauge. Norway.",
        "raw": f"""# Biosort – Raw Web Extract
**Source:** https://biosort.no/en
**Extracted:** {TODAY}

## Overview
Biosort develops next-generation technology to protect farmed fish and provide deeper insight into growth, welfare, and health. Founded 2010 by former Tomra engineers; team includes specialists in aquaculture, software, machine vision, optics, and mechanical development. Norway-based.

## Business Model
- Hardware + AI software for individual-based sea lice control and FishID population insight
- Commercialization phase after iFarm development licenses with Cermaq
- Sell precision lice control systems + data/insight products to salmon farmers

## Funding
- **NOK 100M+ (~USD 10.4M / EUR 8.9M)** (Feb 2026) — Grieg Kapital, Hatch Blue (Blue Revolution Fund), IVC, Farvatn, Futurum Ventures + existing owners
- Capital for final development and market introduction of individual-based lice control

## Key Technology
- **FishID**: machine vision + AI to identify and track individual salmon; prevents double-counting; individual health journals
- **Early lice intervention**: remove lice at earliest attachment stage at individual level
- Built on **iFarm** core tech (Biosort + Cermaq collaboration over four production cycles): imaging, FishID, data infrastructure, individual health journals
- Advanced optics for sharpness/contrast; edge C++/ML inference roles hiring
- Research partners: Nofima, IMR (Institute of Marine Research), NMBU, Norwegian Veterinary Institute, SINTEF Ocean, NTNU

## Contacts
- CEO: Geir Stang Hauge (geir.hauge@biosort.no)
- Site: https://biosort.no/en

## Marine Data Needs
- Underwater imaging streams, individual fish IDs, lice counts, growth/welfare metrics, water quality context
""",
        "wiki": f"""# Biosort

**Sector**: Aquaculture
**Official Site**: https://biosort.no/en

## Overview
Biosort (Norway, founded 2010 by former Tomra engineers) develops individual-based sea lice control and FishID machine-vision/AI technology for farmed salmon. The company commercializes precision parasite protection and fish-level insight built on the multi-cycle iFarm development-license program with Cermaq. Sea lice remain one of the largest biological and economic challenges in salmon aquaculture; Biosort's approach targets continuous early-stage removal at the individual fish level rather than episodic pen-wide treatments.

## Business Model
- **Product**: Individual-based lice control systems + FishID insight (lice count, growth, welfare journals)
- **Market**: Salmon farmers seeking reduced well-boat treatments, lower mortality, improved welfare
- **Stage**: Commercialization after development licenses; NOK 100M+ growth capital (Feb 2026)
- **Go-to-market**: Continuous lice suppression product; data/insight as co-product of FishID

## Funding
- **NOK 100M+ (~$10.4M)** (Feb 2026) — Grieg Kapital, Hatch Blue, IVC, Farvatn, Futurum Ventures + existing owners
- Investors include aquaculture strategics (Grieg) and blue-economy tech VCs (Hatch Blue)

## Key Technology
- **FishID**: AI + machine vision uniquely identifying/tracking individual salmon across the population
- **Early parasite control**: remove lice shortly after attachment; FishID ensures population coverage
- **iFarm heritage**: imaging, data infrastructure, and individual health journals from Cermaq collaboration (4 production cycles)
- Optics + edge ML inference for real-time underwater video processing

## Team & Partners
- CEO: Geir Stang Hauge
- Research: Nofima, IMR, NMBU, Norwegian Veterinary Institute, SINTEF Ocean, NTNU
- Board includes Grieg Kapital, Hatch Blue, Credo Partners, Farvatn, IVC; Geir Molvik (former Cermaq Group CEO)

## Data & Measurement Needs
- **Primary data types**: Underwater video/optical streams, individual fish identity graphs, parasite counts, growth/welfare time series, pen-level environmental context
- **Key measurements/parameters**: Lice stage/count per fish, fish weight/condition, welfare indicators, mortality drivers, temperature, oxygen, salinity, turbidity (for imaging performance)
- **Observation platforms/programs**: In-pen optical sensor systems; edge inference; multi-cycle farm trials (iFarm); research institute validation campaigns
- **Known data gaps**: Standardized individual-level welfare baselines across sites; real-time correlation of environmental stressors with lice attachment rates; interoperable fish-ID standards across vendors
- **Interest in external data services**: Farm environmental sensor networks (DO, temp, salinity); regional sea lice pressure models; research datasets from IMR/Nofima; satellite/coastal ocean products for site risk context

## Cross-Sector Connections
- **Aquaculture AI cluster**: Complements camera/biomass players (Aquabyte, Tidal, NeuralX, Aquaticode) with individual-ID + intervention (not just monitoring)
- **Health diagnostics**: Adjacent to WellFish-style blood diagnostics and Nucleic Sensing eDNA — multi-modal health stack
- **Marine Monitoring**: In-pen optical sensing shares tech DNA with MarineSitu/Seeweed underwater imaging

*Last Updated: {TODAY}*
""",
        "jsonld": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Biosort",
            "url": "https://biosort.no/en",
            "description": "Individual-based sea lice control and FishID AI/machine vision for salmon aquaculture.",
            "foundingDate": "2010",
            "address": {"@type": "PostalAddress", "addressCountry": "NO"},
            "funding": "NOK 100M+ (Feb 2026)",
            "industry": "Aquaculture Technology",
            "sameAs": ["https://biosort.no/en"]
        }
    },
    {
        "name": "Sizable Energy",
        "url": "https://sizableenergy.com/",
        "sector": "Offshore Energy",
        "notes": "Gigawatt-scale ocean energy storage using offshore pumped hydro with brine: seabed reservoir + floating reservoir + connecting pipe + reversible pump-turbines. $8M seed (Oct 2025, Playground Global lead; Bow Capital et al.). Italian pioneer; co-founders Manuele Aufiero (CEO), Carlo Fiorina, Stefano Bernardi (founding investor). Modular/scalable, zero land use, synergistic with floating wind/PV, high RTE. Wave-basin and at-sea proof-of-concept completed; ideal sites identified in 50+ countries. Long-duration energy storage (LDES) for renewables integration.",
        "raw": f"""# Sizable Energy – Raw Web Extract
**Source:** https://sizableenergy.com/
**Extracted:** {TODAY}

## Overview
Sizable Energy redefines long-duration energy storage by taking pumped hydro offshore. Patented design: reservoir on the ocean floor, floating surface reservoir, connecting pipe, reversible pump-turbines moving saturated sea salt brine between reservoirs.

## Business Model
- Develop and deploy gigawatt-scale ocean-based pumped hydro energy storage
- Modular scalable design; couple with floating wind and PV
- Local manufacturing for supply chain resiliency

## Funding
- **$8M seed** (Oct 2025) — Playground Global lead; investors include Bow Capital
- Source: BusinessWire / NewMarketPitch ocean tech tracker

## Key Technology
- Offshore pumped hydro with brine (not freshwater land reservoirs)
- Leverages mature pumped-hydro physics with unlimited ocean deployment potential
- Advantages claimed: modular/scalable, short development times, zero land use, high RTE, competitive economics, coupling with floating wind/PV
- De-risking via wave-basin experiments and at-sea proof of concepts
- Ideal locations confirmed in 50+ countries across all continents

## Team
- Co-founder, CEO: Manuele Aufiero
- Co-founder: Carlo Fiorina
- Co-founder, founding investor: Stefano Bernardi
- VP Business Development: Simone Biondi

## Marine Data Needs
- Bathymetry, seafloor geotech, metocean (waves, currents, wind), brine density/salinity, environmental impact baselines
""",
        "wiki": f"""# Sizable Energy

**Sector**: Offshore Energy
**Official Site**: https://sizableenergy.com/

## Overview
Sizable Energy is an Italian offshore energy storage company commercializing gigawatt-scale **ocean pumped hydro**: a seabed reservoir, a floating surface reservoir, a connecting pipe, and reversible pump-turbines that move saturated sea-salt brine between the two. The design reuses the most proven long-duration storage physics (pumped hydro) while removing land and topography constraints by going offshore — unlocking co-location with floating wind and solar.

## Business Model
- **Product**: Modular offshore pumped-hydro long-duration energy storage (LDES)
- **Market**: Utilities, independent power producers, floating wind/PV developers needing multi-hour to multi-day storage
- **Stage**: Seed; technology de-risked via wave-basin and at-sea PoCs; sites identified in 50+ countries
- **Differentiation**: Zero land use, local manufacturing, high round-trip efficiency, coupling with floating renewables

## Funding
- **$8M seed** (Oct 2025) — Playground Global lead (also listed: Bow Capital et al.)
- NewMarketPitch pure-play ocean tech tracker (Aug 2025–Jul 2026 window)

## Key Technology
- Patented brine-based offshore pumped hydro architecture
- Modular/scalable reservoir and power-conversion modules
- Synergy with floating wind and floating PV for firm renewable power
- Claimed advantages: short development/deployment times, supply-chain resiliency, competitive economics, strong sustainability profile

## Team
- Manuele Aufiero (CEO, co-founder), Carlo Fiorina (co-founder), Stefano Bernardi (co-founder/founding investor)

## Data & Measurement Needs
- **Primary data types**: Bathymetry and seafloor geotechnical data, metocean time series, environmental baseline surveys, structural/motion telemetry from floating reservoirs, brine chemistry
- **Key measurements/parameters**: Water depth, seafloor slope/soil strength, significant wave height, currents, wind, salinity/density of brine, round-trip efficiency, reservoir integrity, marine mammal/benthic impact indicators
- **Observation platforms/programs**: Wave-basin tests, at-sea PoC campaigns, site characterization surveys (MBES, SBP, geotech cores), long-term environmental monitoring for permitting
- **Known data gaps**: Multi-year fatigue/corrosion data for floating brine reservoirs; regional environmental baselines for brine release scenarios; standardized LDES offshore permitting datasets
- **Interest in external data services**: Global bathymetry (GEBCO, national HO), metocean forecast/hindcast services, floating wind site databases, marine spatial planning layers

## Cross-Sector Connections
- **Offshore Energy**: Complements floating wind platforms (Principle Power, BW Ideol, Gazelle) with firming storage
- **Marine Monitoring**: Site characterization and continuous monitoring demand AUVs/USVs (Bedrock, Maritime Robotics, Seaber)
- **Climate Risk**: LDES supports grid decarbonization and climate resilience

*Last Updated: {TODAY}*
""",
        "jsonld": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Sizable Energy",
            "url": "https://sizableenergy.com/",
            "description": "Gigawatt-scale ocean-based pumped hydro energy storage using brine reservoirs.",
            "funding": "$8M seed (Oct 2025)",
            "industry": "Offshore Energy Storage",
            "sameAs": ["https://sizableenergy.com/"]
        }
    },
    {
        "name": "Clear Robotics",
        "url": "https://www.clearbot.org/",
        "sector": "Marine Monitoring & Sensors",
        "notes": "All-electric AI autonomous unmanned surface vessels (Clearbot) for solid waste recovery, hyacinth removal, bathymetric/draft survey, and waterway surveillance. $1.75M seed (Jun 2026, Katapult Ocean). Fleet of 26–27 USVs deployed across UAE, Singapore, India, Philippines and other markets. Clients/partners include ADB (Pasig River pilot), Veolia HK, JNPA Mumbai, Rajasthan municipalities, Hong Kong Highway Dept. Vessel classes: Class 3, Class 2, Alligator (hyacinth), Fetch. Business models: rental/services + distributor. Hong Kong / Singapore roots (Open Ocean Engineering / NUS Enterprise). Zero-emission autonomous waterway operations.",
        "raw": f"""# Clear Robotics – Raw Web Extract
**Source:** https://www.clearbot.org/
**Extracted:** {TODAY}

## Overview
Clear Robotics (Clearbot brand) builds all-electric, AI-powered autonomous unmanned surface vessels for waterway cleanup, survey, and surveillance. Fleet of ~26–27 vessels across UAE, Singapore, India, Philippines and other markets. Roots in Hong Kong / Open Ocean Engineering; NUS Enterprise portfolio.

## Business Model
- Rental & services (monthly)
- Distributor model
- Direct deployments with ports, municipalities, development banks
- Data on collected waste as co-product

## Funding
- **$1.75M seed** (Jun 2026) — Katapult Ocean (per NewMarketPitch / Evertiq)
- Purpose: scale zero-emission autonomous vessel fleet

## Key Technology / Products
- Vessel classes: Class 3, Class 2, Alligator (hyacinth collector), Fetch (small)
- Solar charging options; battery life up to 8 hours; speeds 2–10 knots
- Services: solid waste recovery (up to 500 kg/deployment), draft survey, bathymetric survey, hyacinth removal (~1 ton thick vegetation/deployment), under-platform surveillance (1080p live feed)
- AI navigation + data analytics

## Notable Projects
- Ilugin River, Philippines — hyacinth removal with ADB (~20,400 kg)
- Lohagarh Fort, Bharatpur — trash removal
- SENTX Landfill HK with Veolia — 260 tons hyacinth in 2 weeks
- JNPA Mumbai port trash removal
- Pasig River ADB pilot (6-month study, Jan 2026 convening)
- Hong Kong highway under-platform surveillance

## Contacts
- contact@clearbot.org
- Site: https://www.clearbot.org/
""",
        "wiki": f"""# Clear Robotics

**Sector**: Marine Monitoring & Sensors
**Official Site**: https://www.clearbot.org/

## Overview
Clear Robotics (Clearbot) develops all-electric, AI-driven autonomous unmanned surface vessels for waterway cleanup, bathymetric/draft survey, hyacinth removal, and infrastructure surveillance. With a deployed fleet of ~26–27 USVs across the UAE, Singapore, India, the Philippines and other markets, the company targets ports, municipalities, and development-bank programs seeking zero-emission, lower-cost alternatives to crewed cleanup boats. Hong Kong / Singapore roots (Open Ocean Engineering; NUS Enterprise).

## Business Model
- **Rental & services**: Monthly rental of vessels + operations
- **Distributor model**: Regional partners
- **Project services**: Waste recovery, survey, vegetation removal with waste-mass data deliverables
- **Differentiation**: Fully electric + autonomous → no fuel, less manpower, data co-product

## Funding
- **$1.75M seed** (Jun 2026) — Katapult Ocean (NewMarketPitch pure-play ocean tech tracker)
- Positioning: build one of the largest fleets of zero-emission autonomous workboats

## Key Technology
- Multi-class Clearbot USVs (Class 2/3, Alligator, Fetch) with solar charging options
- AI navigation and payload automation for waste, hyacinth, and survey missions
- Live video / recorded inspection feeds for infrastructure surveillance
- Operational metrics: up to ~500 kg trash per deployment; hyacinth ~1 ton thick vegetation; survey-capable

## Notable Deployments
- ADB-backed Pasig River / Philippines hyacinth and river cleanup pilots
- Veolia Hong Kong; JNPA Mumbai; Indian municipal projects; HK Highway Department surveillance

## Data & Measurement Needs
- **Primary data types**: USV navigation telemetry, computer-vision waste/vegetation detection, bathymetry/survey grids, waste mass/composition logs, waterway imagery
- **Key measurements/parameters**: Waste mass (kg), area cleaned (m²), hyacinth volume, draft/bathymetric depth, vessel battery state, autonomy path accuracy, turbidity/water quality co-sensors (where fitted)
- **Observation platforms/programs**: Fleet USV operations; ADB pilot studies; port authority recurring cleanups; under-structure inspection campaigns
- **Known data gaps**: Standardized waste composition taxonomies across cities; multi-city waterway pollution baselines; integration of cleanup data into municipal environmental dashboards
- **Interest in external data services**: Hydrographic charts, river discharge/tide models, satellite turbidity/plastic indicators, municipal GIS layers for priority hotspots

## Cross-Sector Connections
- **Marine Monitoring**: ASV fleet peers with Maritime Robotics, Seasats, Omission — but mission focus is urban/port environmental services
- **Coastal Risk & Infrastructure**: River and port cleanup supports coastal resilience and heritage/waterway restoration
- **Maritime Ops**: Draft survey and surveillance products overlap port operations analytics

*Last Updated: {TODAY}*
""",
        "jsonld": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Clear Robotics",
            "url": "https://www.clearbot.org/",
            "description": "All-electric AI autonomous USVs for waterway waste recovery, survey, and surveillance.",
            "funding": "$1.75M seed (Jun 2026, Katapult Ocean)",
            "industry": "Marine Robotics",
            "sameAs": ["https://www.clearbot.org/"]
        }
    },
    {
        "name": "Seaber",
        "url": "https://seaber.fr/",
        "sector": "Marine Monitoring & Sensors",
        "notes": "French micro-AUV manufacturer: YUCO (science/civil, ~10 kg, 1 m, 300 m depth, 8–10 h autonomy) and MARVEL (security/defense: MCM, ASW training, coast guard). Payloads include CTD, multi-parameter physico, side-scan, PAM acoustic recorder, 3DSS, HR camera, eDNA sampler, magnetometer, multibeam. SEAPLAN mission software. Single-person multi-modal deployment. ~$1.8–2M seed (Oct 2025; investors Sodero, Breizh Up, FNX Ventures, Défense Angels). Applications: coastal monitoring/hydrography, harbours, marine biology/aquaculture, SAR/security, mine countermeasures, beach reconnaissance. Thesis: fleets of numerous small affordable AUVs. France.",
        "raw": f"""# Seaber – Raw Web Extract
**Source:** https://seaber.fr/
**Extracted:** {TODAY}

## Overview
SEABER designs and manufactures highly reliable micro-AUVs: ~10 kg, ~1 m long, to 300 m depth, 8–10 hours autonomy. YUCO line for oceanographic research and commercial applications; MARVEL line for survey and defense (security, coast guard, MCM, ASW training). Belief: future of ocean exploration is fleets of numerous small, agile, affordable AUVs.

## Business Model
- Hardware sales of micro-AUV product lines with payload options
- SEAPLAN mission planning software
- Distributors for global reach
- Science/civil + dual-use defense markets

## Funding
- Seed ~$1.8–2M USD (Oct 2025) — Sodero, Breizh Up, FNX Ventures, Défense Angels (per Dealroom/Seedtable/NewMarketPitch)
- Public/support funding logos displayed on site

## Key Technology
- YUCO variants: CARRIER, SCAN (+SSS+DVL), CTD (RBR Legato), PHYSICO (AML multi-parameter), PAM (acoustic recorder), 3DSS, LUMEN (HR camera), eDNA sampler
- MARVEL variants: SCAN, MAGNETO, MBES, 3DSS, LUMEN (+USBL options)
- Single-person multi-modal deployment
- SEAPLAN software

## Applications
- Coastal monitoring & hydrography
- Inland waters / harbour
- Marine biology & aquaculture
- Search, rescue, security, coast guard
- Mine countermeasures; ASW training
- Beach reconnaissance (MARVEL 3DSS); oyster reef mapping (BLUE CONNECT)

## Marine Data Needs
- Navigation/positioning, payload sensor streams (CTD, acoustic, optical, magnetic, eDNA), bathymetry, mission logs
""",
        "wiki": f"""# Seaber

**Sector**: Marine Monitoring & Sensors
**Official Site**: https://seaber.fr/

## Overview
Seaber (France) manufactures micro-AUVs designed for single-person deployment: roughly 10 kg, 1 m long, 300 m depth rating, and 8–10 hours autonomy. The **YUCO** family targets scientific and commercial oceanography; the **MARVEL** family targets survey and defense (coast guard, MCM, ASW training). The company's thesis is that the future of ocean exploration belongs to fleets of numerous small, agile, affordable AUVs rather than a few large expensive platforms.

## Business Model
- **Hardware product lines** with modular payloads + SEAPLAN mission software
- **Distributor network** for global sales
- **Dual-use**: research/commercial oceanography + defense/security
- **Stage**: Seed-funded manufacturer with active product catalog and field projects

## Funding
- **~$1.8–2M seed** (Oct 2025) — Sodero, Breizh Up, FNX Ventures, Défense Angels (NewMarketPitch / Seedtable / Dealroom)
- Additional public/support program funding (logos on site)

## Key Technology
- **YUCO**: carrier + specialized payloads (side-scan/DVL, RBR CTD, AML physico, PAM, 3DSS, HR camera, eDNA sampler)
- **MARVEL**: defense/survey oriented (sonar, magnetometer, multibeam, 3DSS, camera; USBL options)
- **SEAPLAN**: mission planning software
- Micro-AUV form factor optimized for fleet economics and rapid redeployment

## Field Examples
- MARVEL 3DSS for naval beach reconnaissance
- Micro-AUV mapping of oyster reef restoration (BLUE CONNECT, North Sea)
- YUCO-SCAN missions (e.g., Australia with Grey 4 Blue Solutions)

## Data & Measurement Needs
- **Primary data types**: AUV navigation/INS logs, CTD/physico sensor streams, side-scan and multibeam sonar, passive acoustic recordings, optical imagery, magnetometry, eDNA sample metadata
- **Key measurements/parameters**: Temperature, conductivity/salinity, depth, multi-parameter water quality, acoustic backscatter, magnetic anomalies, bathymetry, species/eDNA detections, mission geofences
- **Observation platforms/programs**: Micro-AUV fleets; coastal/harbour surveys; MCM/ASW training ranges; aquaculture and restoration mapping campaigns
- **Known data gaps**: Low-cost USBL/positioning in constrained waters; standardized multi-AUV fleet coordination data models; affordable real-time acoustic communications for swarm ops
- **Interest in external data services**: Tide/current models, nautical charts, acoustic environment databases, eDNA reference libraries, defense range metadata

## Cross-Sector Connections
- **Marine Monitoring**: Complements larger AUV primes (Ulysses, Vatn, Bedrock, Sunfish) at the micro/fleet end of the cost curve
- **Aquaculture**: PHYSICO/CTD/eDNA payloads serve farm and restoration monitoring
- **Defense autonomy cluster**: MARVEL sits adjacent to Vatn/Ulysses/Saronic but at micro-AUV MCM/training niche

*Last Updated: {TODAY}*
""",
        "jsonld": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Seaber",
            "url": "https://seaber.fr/",
            "description": "French manufacturer of micro-AUVs (YUCO science/civil, MARVEL defense/survey).",
            "funding": "~$2M seed (Oct 2025)",
            "industry": "Marine Robotics",
            "address": {"@type": "PostalAddress", "addressCountry": "FR"},
            "sameAs": ["https://seaber.fr/"]
        }
    },
    {
        "name": "Voltai",
        "url": "https://www.voltai.ca/",
        "sector": "Offshore Energy",
        "notes": "Onboard wave/motion energy harvesting for ships — electrostatic generators converting wave and vibration energy into electricity without added drag. CAD $1.83M oversubscribed pre-seed (Oct 2025) co-led by Invest Nova Scotia. Modular systems scalable 25W to multi-MW. Pilots: NSCC research vessel; Net Zero Atlantic project for fishing vessels and ferries; Canadian Coast Guard Innovative Solutions Canada challenge (2 phases). Family-founded in Dartmouth, Nova Scotia (CEO Maja Maher). Positioning: emission-free energy source rivaling heavy fuel oil on cost for regulatory compliance. Supports: CDL, NRC IRAP, Ocean Startup Project, Clean Foundation, Springboard Atlantic.",
        "raw": f"""# Voltai – Raw Web Extract
**Source:** https://www.voltai.ca/
**Extracted:** {TODAY}

## Overview
Voltai (Dartmouth, Nova Scotia) develops motion-powered generators that convert wave and vibration energy into clean electricity for marine platforms. Modular energy harvesting from 25W to multi-megawatt scale for ships, fishing vessels, ferries, and buoys.

## Business Model
- Modular energy harvesting systems installable on marine platforms
- Cost-competitive emission-free power to help vessels meet emission regulations
- Path from buoy/small-vessel systems to multi-MW ship systems

## Funding
- **CAD $1.83M oversubscribed pre-seed** (Oct 2025) — Invest Nova Scotia co-lead + individual investors
- Prior: Innovative Solutions Canada (Canadian Coast Guard) 2 phases; Net Zero Atlantic research funding; NRC IRAP; Ocean Startup Project

## Key Technology
- Electrostatic / motion-to-power generators harvesting wave energy from vessel motion without added drag
- Modular scaling 25W → multi-MW
- Target: rival heavy fuel oil on cost for auxiliary/clean power

## Projects
- Pilot with NSCC research vessel
- Net Zero Atlantic: kinetic energy harvesting on fishing vessels and ferries in Nova Scotia
- Canadian Coast Guard ISC challenge PoC

## Team
- CEO: Maja Maher; COO: Ahmed Maher; CFO: Moustafa Maher (family business, 60+ years combined entrepreneurship)
- Contact: info@voltai.ca; 1 Research Dr, Dartmouth, NS B2Y 4M9

## Marine Data Needs
- Vessel motion/wave spectra, power output telemetry, fuel displacement metrics, metocean conditions
""",
        "wiki": f"""# Voltai

**Sector**: Offshore Energy
**Official Site**: https://www.voltai.ca/

## Overview
Voltai is a Nova Scotia cleantech company building modular **onboard wave/motion energy harvesters** that convert ship motion and vibration into electricity — without adding drag. Systems are designed to scale from 25 W modules to multi-megawatt installations, targeting fishing vessels, ferries, commercial ships, and buoy platforms. The company positions the technology as an emission-free energy source that can rival heavy fuel oil on cost for auxiliary power under tightening maritime emission rules.

## Business Model
- **Product**: Modular electrostatic motion-to-power generators for marine platforms
- **Market**: Commercial shipping, fishing fleets, ferries, remote marine assets needing clean auxiliary power
- **Stage**: Pre-seed; active pilots with NSCC and Net Zero Atlantic; Coast Guard ISC heritage
- **Value prop**: Regulatory compliance + fuel cost reduction without green premium

## Funding
- **CAD $1.83M oversubscribed pre-seed** (Oct 2025) — Invest Nova Scotia co-lead + angels
- Non-dilutive/public support: Innovative Solutions Canada (Canadian Coast Guard, 2 phases), Net Zero Atlantic, NRC IRAP, Ocean Startup Project, Clean Foundation, Springboard Atlantic, Creative Destruction Lab

## Key Technology
- Wave/vibration energy harvesting from vessel motion (no added drag claim)
- Modular architecture 25W → multi-MW
- Installation on existing marine platforms (retrofit-friendly path)

## Team & Location
- CEO Maja Maher; COO Ahmed Maher; CFO Moustafa Maher
- HQ: 1 Research Dr, Dartmouth, Nova Scotia

## Data & Measurement Needs
- **Primary data types**: Vessel motion/IMU time series, power generation telemetry, fuel consumption baselines, metocean conditions during voyages
- **Key measurements/parameters**: Wave height/period spectra, heave/pitch/roll energy, kWh harvested, system efficiency, corrosion/fatigue of deck-mounted units, noise/vibration impact
- **Observation platforms/programs**: NSCC research vessel pilot; fishing vessel/ferry trials (Net Zero Atlantic); Coast Guard challenge PoCs
- **Known data gaps**: Long-duration real-ocean harvested energy datasets across vessel classes; correlation of sea state to net fuel savings; fleet-scale retrofit economics under varying routes
- **Interest in external data services**: Metocean hindcasts/forecasts along fishing and ferry routes; AIS-linked vessel performance databases; emissions MRV frameworks for IMO compliance reporting

## Cross-Sector Connections
- **Offshore Energy / maritime decarbonization**: Complements Fleetzero (batteries), Kvasir (drop-in biofuel), Hullbot (drag reduction) — onboard generation is a fourth pathway
- **Panthalassa adjacency**: Both harvest ocean energy, but Voltai is vessel-mounted auxiliary power vs open-ocean wave-powered compute
- **Maritime Ops**: Direct value to fleet operators under CII/FuelEU-style rules

*Last Updated: {TODAY}*
""",
        "jsonld": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Voltai",
            "url": "https://www.voltai.ca/",
            "description": "Onboard wave/motion energy harvesting systems for marine vessels.",
            "funding": "CAD $1.83M pre-seed (Oct 2025)",
            "industry": "Marine Energy",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "1 Research Dr",
                "addressLocality": "Dartmouth",
                "addressRegion": "NS",
                "addressCountry": "CA"
            },
            "sameAs": ["https://www.voltai.ca/"]
        }
    },
]

def main():
    # Update companies.json
    path = os.path.join(REPO, "sources", "companies.json")
    with open(path) as f:
        companies = json.load(f)
    existing = {c["name"].lower() for c in companies}
    added = []
    for c in COMPANIES:
        if c["name"].lower() in existing:
            print(f"SKIP already exists: {c['name']}")
            continue
        companies.append({
            "sector": c["sector"],
            "name": c["name"],
            "url": c["url"],
            "notes": c["notes"],
            "last_updated": TODAY,
        })
        added.append(c["name"])
    with open(path, "w") as f:
        json.dump(companies, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"companies.json: +{len(added)} → total {len(companies)}")

    for c in COMPANIES:
        slug = slugify(c["name"])
        # raw
        with open(os.path.join(REPO, "raw", f"{slug}.md"), "w") as f:
            f.write(c["raw"].rstrip() + "\n")
        # metadata
        with open(os.path.join(REPO, "metadata", f"{slug}.jsonld"), "w") as f:
            json.dump(c["jsonld"], f, indent=2, ensure_ascii=False)
            f.write("\n")
        # wiki
        with open(os.path.join(REPO, "wiki", f"{slug}.md"), "w") as f:
            f.write(c["wiki"].rstrip() + "\n")
        print(f"Wrote raw/metadata/wiki for {slug}")

if __name__ == "__main__":
    main()
