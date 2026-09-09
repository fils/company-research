#!/usr/bin/env python3
"""Daily update 2026-09-09: Bluecore Energy, Newlight Marine, Coast 4C + Oshen funding refresh."""
import json
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "2026-09-09"
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
        "name": "Bluecore Energy",
        "url": "https://www.bluecore.energy/",
        "sector": "Offshore Energy",
        "tag": "offshore-energy",
        "notes": (
            "Floating maritime nuclear SMRs on barges (~10 MWe first unit) for ports, AI data centers, coastal infrastructure. "
            "HQ inside Port of Long Beach (first nuclear co headquartered at a major port). Founder/CEO Kofi Asante (Uber alum). "
            "$10M pre-seed (Jul 2026 stealth exit) + oversubscribed $50M seed (Sep 8 2026, Silverton Partners lead; Slauson & Co., "
            "Harlem Capital, Chris Larsen/Ripple, Collab Capital, HartBeat Ventures, Tesla/Uber/Amazon/Google angels) — ~$60M total "
            "in ~2 months. Two barges launched; formal NRC + USCG design review (Aug 2026); MARAD/DOT Maritime partnership. "
            "Team DNA: SpaceX, Rivian, Toyota, US Navy nuclear. Use of proceeds: engineering, fuel, certification, hiring."
        ),
        "description": (
            "Floating barge-mounted water-cooled SMRs (~10 MWe) for ports/AI infra; $50M seed (Silverton, Sep 2026) "
            "after $10M pre-seed; ~$60M total; Port of Long Beach HQ."
        ),
        "raw": f"""# Bluecore Energy – Raw Web Extract
**Source:** https://www.bluecore.energy/
**Also:** https://techcrunch.com/2026/09/08/nuclear-startup-bluecore-energy-raises-50m-seed-round-just-two-months-after-launch/
**Also:** https://www.esgtoday.com/bluecore-energy-raises-50-million-to-build-floating-nuclear-power-plants/
**Extracted:** {DATE}

## Overview
Bluecore Energy builds compact water-cooled small modular reactors (SMRs) mounted on floating barges to deliver zero-emission power to ports, AI data centers, and coastal/critical infrastructure. First unit class ~10 MWe continuous; modular/scalable; multi-year refuel intervals. Headquartered inside the Port of Long Beach — described as the first nuclear company HQ'd at a major port. Founder & CEO Kofi Asante (ex-Uber). Team includes SpaceX, Rivian, Toyota, and former US Navy nuclear personnel.

## Business Model
- Product: barge-mounted maritime nuclear power plants (portable SMRs)
- Customers/use cases: ports (electrification/zero-emission ops), coastal AI data centers, communities lacking grid capacity, potential offshore deployment
- Go-to-market: build/certify first systems at Port of Long Beach; sell/deploy transportable clean baseload where land nuclear siting is slow
- Differentiator vs land SMR: mobility in days not years; leverages 70 years of naval nuclear ops experience commercially; co-location with maritime demand

## Funding
- **$10M pre-seed** (Jul 2026, out of stealth): Slauson & Co., Harlem Capital, Ripple co-founder Chris Larsen, others
- **$50M oversubscribed seed** (announced Sep 8 2026 / Tuesday): **Silverton Partners lead**; substantial follow-on from Slauson & Co.; new Collab Capital, Kevin Hart's HartBeat Ventures; angels from Tesla, Uber, Amazon, Google; closed in ~8 weeks
- **~ $60M total** within months of founding
- Use of proceeds: product development, regulatory/classification work, nuclear fuel purchases, manufacturing, hiring

## Key Technology / Status
- Compact water-cooled reactor on barge; defense-in-depth barriers (fuel core → cladding → vessel → steel containment → water shield)
- Two floating barges launched; first maritime nuclear energy system under development at Port of Long Beach
- Formal engagement with **US NRC** and **US Coast Guard** (Aug 2026) for commercial maritime nuclear certification path
- Partnerships/engagement: Port of Long Beach, DOT Maritime Administration, NRC, USCG
- Supply-chain strategy modeled on SpaceX/Rivian/Toyota hardware discipline; ordering fuel via national lab partner

## Marine Data & Ops Needs (implicit)
- Port energy demand curves, berth/grid interconnection, metocean for barge station-keeping, radiological/environmental baseline monitoring, maritime traffic deconfliction, emergency response modeling

## Contacts
- HQ: Port of Long Beach, California
- https://www.bluecore.energy/
- Founder/CEO: Kofi Asante
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Bluecore Energy",
            "url": "https://www.bluecore.energy/",
            "description": "Floating barge-mounted water-cooled SMR nuclear power systems (~10 MWe) for ports, AI data centers, and coastal infrastructure.",
            "foundingLocation": {"@type": "Place", "name": "Port of Long Beach, California, USA"},
            "founder": [{"@type": "Person", "name": "Kofi Asante", "jobTitle": "Founder & CEO"}],
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "USD",
                "value": 50000000,
                "description": "$50M oversubscribed seed (Sep 2026, Silverton Partners lead) after $10M pre-seed (Jul 2026); ~$60M total",
            },
            "sector": "Offshore Energy",
            "businessModel": "Transportable floating nuclear baseload power for ports and coastal AI/critical infrastructure; certification-first maritime SMR OEM",
            "lastFundingRound": "$50M seed (Sep 8 2026) — Silverton Partners lead; Slauson & Co., Collab Capital, HartBeat Ventures, Harlem Capital, Chris Larsen, strategic angels",
            "totalFunding": "~$60M ($10M pre-seed + $50M seed)",
            "investors": [
                "Silverton Partners",
                "Slauson & Co.",
                "Harlem Capital",
                "Chris Larsen",
                "Collab Capital",
                "HartBeat Ventures",
            ],
            "knowsAbout": [
                "Floating nuclear power",
                "Maritime SMR",
                "Port electrification",
                "Water-cooled reactors",
                "NRC maritime nuclear licensing",
            ],
            "product": ["10 MWe barge-mounted SMR", "Floating nuclear power plant"],
            "partner": [
                "Port of Long Beach",
                "U.S. Nuclear Regulatory Commission",
                "U.S. Coast Guard",
                "U.S. DOT Maritime Administration",
            ],
        },
        "wiki_body": f"""# Bluecore Energy

**Sector**: Offshore Energy
**Official Site**: https://www.bluecore.energy/
**Last Updated**: {DATE}

**Focus**: Floating barge-mounted water-cooled SMRs delivering portable zero-emission baseload (~10 MWe first class) to ports, AI data centers, and coastal infrastructure.
**Status**: **$50M oversubscribed seed** (Sep 8 2026, Silverton Partners lead) after **$10M pre-seed** (Jul 2026) — **~$60M total** within months of founding; two barges launched; formal NRC + USCG design review underway.
**HQ**: Port of Long Beach, CA — first nuclear company headquartered at a major port. Founder/CEO Kofi Asante (ex-Uber); team DNA SpaceX / Rivian / Toyota / US Navy nuclear.

## Business Model
Maritime nuclear power OEM: compact water-cooled reactors on floating barges that can be moved to demand (ports, coastal AI campuses, underserved coastal grids) without multi-year land siting. Differentiator vs land SMRs and vs vessel propulsion plays ([Fleetzero](fleetzero.md), [Kvasir Technologies](kvasir-technologies.md), [Newlight Marine](newlight-marine.md)): **shore-power / industrial baseload delivered from the water side**, not ship fuel. Port of Long Beach as build-and-demo beachhead under Green Port / 2050 electrification demand (hundreds of MW).

## Funding
- **$10M pre-seed** (Jul 2026, out of stealth): Slauson & Co., Harlem Capital, Ripple co-founder Chris Larsen, others
- **$50M seed** (Sep 8 2026): Silverton Partners (lead); continued Slauson & Co.; Collab Capital; Kevin Hart's HartBeat Ventures; angels from Tesla, Uber, Amazon, Google — closed in ~8 weeks after inbound demand
- **~$60M cumulative**; proceeds → engineering, regulatory/classification, nuclear fuel, manufacturing, hiring

## Key Technology
- ~10 MWe continuous first-unit class; modular scale-up path; multi-year refuel cadence
- Water-cooled architecture with multi-barrier defense-in-depth (fuel → cladding → vessel → steel containment → water shield)
- Two floating barges already launched; first system under development at Port of Long Beach
- Coordinated commercial maritime nuclear path with **NRC + US Coast Guard** (formal engagement Aug 2026) + DOT Maritime Administration
- Hardware/supply-chain discipline from aerospace/auto talent; fuel procurement via national lab partner

## Data & Measurement Needs
- **Primary data types**: Port/berth electrical load profiles, barge station-keeping metocean, radiological environmental monitoring, AIS traffic density, emergency-response/plume models, cooling-water intake/discharge chemistry, grid interconnection capacity
- **Key measurements/parameters**: Continuous MW delivery vs port demand, sea-state operating envelopes, radiological background baselines, water temperature/quality near mooring, security perimeter events, fuel burnup/refuel logistics
- **Observation platforms/programs**: Port of Long Beach pilot site instrumentation; NRC/USCG certification test campaigns; national lab fuel/partner facilities
- **Known data gaps**: Standardized commercial maritime-nuclear environmental baseline protocols; multi-port energy-demand + cold-ironing MW forecasts; long-duration barge mooring metocean for West Coast / hurricane basins
- **Interest in external data services**: High-resolution coastal metocean ([Sofar Ocean](sofar-ocean.md), [Oshen](oshen.md)), port grid capacity maps, AIS deconfliction, independent marine environmental MRV for community acceptance

---

**Cross-links**: [Offshore Energy](offshore-energy.md) · [Fleetzero](fleetzero.md) · [Kvasir Technologies](kvasir-technologies.md) · [Newlight Marine](newlight-marine.md) · [Vessev](vessev.md) · [Endurance Energy](endurance-energy.md) · [Oshen](oshen.md)
""",
    },
    {
        "name": "Newlight Marine",
        "url": "https://www.newlightmarine.com/",
        "sector": "Offshore Energy",
        "tag": "offshore-energy",
        "notes": (
            "Hydrogen-hybrid retrofit for existing marine diesel engines (Newlight Marine Technologies Inc., Alameda CA). "
            "Millisecond-level H2 injection control using exhaust temp, combustion pressure, air intake; install in ~1–2 weeks without drydock. "
            "Commercial validation: 8,500 nm Singapore→Ghana on 650-ft Lomar bulk carrier — 24% diesel cut, 28% CO2, 22% CO, 21% SO2. "
            "$9M seed (Sep 1 2026): lomarlabs, BIRD Energy (US DOE + Israel MoE), Undeterred Capital, CiRi Ventures, Fusion VC. "
            "Founders Haran Cohen Hillel (CEO) & Evyatar Cohen (Israeli Navy). RINA FAT for 2-/4-stroke mains; Vessel of the Future finalist SMM 2026. "
            "Claims LOIs for 12 vessels; live AIS map shows Oslo Trader + Lucy Borchard. Distinct from Newlight Technologies (AirCarbon biomaterials)."
        ),
        "description": (
            "Hydrogen-hybrid retrofit for marine diesels; 24% fuel / 28% CO2 cut on 8,500 nm Lomar voyage; "
            "$9M seed (lomarlabs, BIRD Energy, Fusion VC, Sep 2026); Alameda CA."
        ),
        "raw": f"""# Newlight Marine – Raw Web Extract
**Source:** https://www.newlightmarine.com/
**Also:** https://www.newlightmarine.com/product
**Also:** https://techcrunch.com/2026/09/01/this-startup-is-fuel-injecting-hydrogen-to-make-cargo-ships-more-efficient/
**Also:** https://www.newlightmarine.com/news
**Extracted:** {DATE}
**Note:** Distinct from Newlight Technologies Inc. (AirCarbon biomaterials at newlight.com).

## Overview
Newlight Marine Technologies Inc. (Alameda, California) builds a hydrogen-hybrid propulsion retrofit for existing marine diesel engines. Compressed hydrogen is injected with millisecond-level control based on live engine state (load, RPM, exhaust temperature, combustion pressure, air intake pressure) so the engine burns less diesel while hydrogen supplies part of the energy. Typical install ~2 weeks, no drydock. Legal name on site: Newlight Marine Technologies Inc.

## Business Model
- Product: hydrogen supply conditioning + real-time hydrogen control + injection package as retrofit
- Customers: commercial shipowners/operators (bulk, container); first commercial partner Lomar Shipping / lomarlabs
- Value prop: fuel is 50–60% of OPEX; claimed >20% fuel & emissions cuts; up to ~$500k annual savings on some vessels; diesel path remains primary so vessel never depends on H2 to operate
- Safety: automatic reduce/stop H2 on out-of-range pressure/flow/temp/fire/leak; engine continues on diesel
- Pipeline: agreements claimed for 12 vessels; broader fleet rollouts planned next year
- Live installations mapped via AIS (Oslo Trader bulk carrier; Lucy Borchard container)

## Funding
- **$9M seed** (announced ~Sep 1 2026 via TechCrunch exclusive): lomarlabs (Lomar Shipping venture arm), BIRD Energy (US DOE + Israel Ministry of Energy JV), Undeterred Capital, CiRi Ventures, Fusion VC (Israeli startups in US accelerator)
- Strategic: Lomar provided test ship (investor diligence = voyage)

## Key Technology / Validation
- Hydrogen supply system: conditions onboard H2 storage to engine pressure/flow while preserving diesel path
- Hydrogen Control / System Controller: real-time adaptive maps; timed metered injection per piston event
- Sensors: pressure, mass flow, temperature, fire detectors, H2 leak atmosphere sensing, thermal probes
- **Commercial voyage**: 8,500 nm Singapore → Ghana on 650-ft Lomar bulk carrier — **24% diesel reduction, 28% lower CO2, 22% lower CO, 21% lower SO2**
- **RINA Factory Acceptance Test** (Nov 2025): 4-day class review for 2- and 4-stroke main engines
- Vessel of the Future finalist — SMM Hamburg Maritime Tech Demo Day (Aug 2026)
- Partners referenced historically: AURELIA, RINA, Lomar (Oslo Trader H2-MGO blend integration)

## Contacts
- HQ: Alameda, California, USA
- https://www.newlightmarine.com/
- CEO: Haran Cohen Hillel; Co-founder: Evyatar Cohen (Israeli Navy backgrounds)
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Newlight Marine",
            "legalName": "Newlight Marine Technologies Inc.",
            "url": "https://www.newlightmarine.com/",
            "description": "Hydrogen-hybrid retrofit system for existing marine diesel engines — real-time controlled H2 injection cutting fuel use ~24% and CO2 ~28% without drydock or engine replacement.",
            "foundingLocation": {"@type": "Place", "name": "Alameda, California, USA"},
            "founder": [
                {"@type": "Person", "name": "Haran Cohen Hillel", "jobTitle": "Co-founder & CEO"},
                {"@type": "Person", "name": "Evyatar Cohen", "jobTitle": "Co-founder"},
            ],
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "USD",
                "value": 9000000,
                "description": "$9M seed (Sep 2026) — lomarlabs, BIRD Energy, Undeterred Capital, CiRi Ventures, Fusion VC",
            },
            "sector": "Offshore Energy",
            "businessModel": "Hydrogen injection retrofit hardware + controls sold/installed on existing commercial diesels; savings-share via fuel OPEX reduction; no drydock path",
            "lastFundingRound": "$9M seed (Sep 1 2026)",
            "totalFunding": "$9M disclosed seed",
            "investors": [
                "lomarlabs",
                "BIRD Energy",
                "Undeterred Capital",
                "CiRi Ventures",
                "Fusion VC",
            ],
            "knowsAbout": [
                "Marine hydrogen hybrid propulsion",
                "Diesel engine retrofit",
                "Ship fuel efficiency",
                "IMO emissions reduction",
                "Real-time engine control",
            ],
            "product": ["Hydrogen hybrid propulsion retrofit", "Hydrogen Control System", "Hydrogen supply conditioning"],
            "partner": ["Lomar Shipping", "RINA", "AURELIA"],
        },
        "wiki_body": f"""# Newlight Marine

**Sector**: Offshore Energy
**Official Site**: https://www.newlightmarine.com/
**Last Updated**: {DATE}

**Focus**: Hydrogen-hybrid retrofit for the existing marine diesel fleet — millisecond-controlled H2 injection that cuts fuel and emissions without replacing engines or drydocking.
**Status**: **$9M seed** (Sep 1 2026); first long-range commercial voyage **8,500 nm Singapore→Ghana** on Lomar bulker with **24% diesel / 28% CO₂** reduction; RINA FAT complete; LOIs claimed for 12 vessels.
**HQ**: Alameda, CA (Newlight Marine Technologies Inc.) — Co-founders Haran Cohen Hillel (CEO) & Evyatar Cohen (Israeli Navy). **Not** the AirCarbon biomaterials company (newlight.com).

## Business Model
Retrofit hardware + controls sold to commercial shipowners: onboard hydrogen supply conditioning, real-time System Controller, and metered injection into existing 2-/4-stroke mains. Install in ~1–2 weeks without drydock; diesel path remains primary so the vessel is never H2-dependent. Monetizes the fact that fuel is ~50–60% of vessel OPEX (claimed up to ~$500k/yr savings on some ships). Strategic alignment with [lomarlabs](https://www.newlightmarine.com/) / Lomar Shipping (test vessel + investor). Complements [Fleetzero](fleetzero.md) (full electrification), [Kvasir Technologies](kvasir-technologies.md) (drop-in biofuel), and [Aloft Systems](aloft-systems.md) (wind propulsion) as a **fifth** near-term decarbonization path for ships already at sea.

## Funding
- **$9M seed** (Sep 1 2026): lomarlabs, BIRD Energy (US DOE + Israel Ministry of Energy joint venture), Undeterred Capital, CiRi Ventures, Fusion VC
- Diligence signal: investor-supplied Lomar bulk carrier for the commercial ocean trial

## Key Technology
- Live engine-state sensing (load, RPM, exhaust temp, combustion pressure, intake pressure) → adaptive H2 flow every piston event
- Automatic isolate/reduce on out-of-range pressure, flow, temperature, fire, or leak; engine continues on diesel
- **Voyage results**: 24% less diesel, 28% lower CO₂, 22% lower CO, 21% lower SO₂ (Lomar 650-ft bulker)
- RINA Factory Acceptance Test (Nov 2025) for two- and four-stroke main engines; Vessel of the Future finalist (SMM 2026)
- Live AIS-tracked installations (e.g., Oslo Trader bulk carrier; Lucy Borchard container)

## Data & Measurement Needs
- **Primary data types**: High-frequency engine telemetry (load, RPM, cylinder pressure, exhaust/intake temps), hydrogen mass-flow and rail pressure, leak/fire safety channels, voyage fuel bunkering logs, AIS positions, emissions factors
- **Key measurements/parameters**: g-fuel/kWh and t-fuel/day vs baseline, CO₂/CO/SO₂ stack factors, H2 consumption per nm, injection timing maps, class-society safety KPIs, install-time and uptime
- **Observation platforms/programs**: On-vessel sensor suite during commercial voyages; RINA FAT benches; multi-vessel rollout telemetry (12-vessel LOI pipeline)
- **Known data gaps**: Multi-engine-make generalization datasets; hydrogen bunkering availability maps by port; long-duration tropical/arctic durability; independent third-party MRV for carbon-accounting buyers
- **Interest in external data services**: Port H2 bunkering infrastructure layers, weather/route optimization ([Sofar Ocean](sofar-ocean.md)), CII/IMO compliance databases, fleet fuel-price benchmarks, classification society digital twins

---

**Cross-links**: [Offshore Energy](offshore-energy.md) · [Fleetzero](fleetzero.md) · [Kvasir Technologies](kvasir-technologies.md) · [Aloft Systems](aloft-systems.md) · [Bluecore Energy](bluecore-energy.md) · [Voltai](voltai.md) · [ShipIn Systems](shipin-systems.md)
""",
    },
    {
        "name": "Coast 4C",
        "url": "https://www.coast4c.com/",
        "sector": "Aquaculture",
        "tag": "aquaculture",
        "notes": (
            "Regenerative smallholder seaweed supply platform (Philippines/SE Asia) spinning out of ZSL (2020 launch, 2022 spinout). "
            "4Cs: Community, Commerce, Conservation, Climate. GROW program: regenerative farm input packages, education, finance, insurance "
            "for seaweed farmers; buyer-side traceable eucheumatoid supply for food/feed/fertiliser/plastics. "
            "Impact: 286 farmers with GROW packages by end-2024; target 500 families by end-2025; 5,868 ha across 8 community iMPAs; "
            "1,200% YoY growth in seaweed traded (705 t dried 2024 YTD). Goal: 500,000 farming families SE Asia. "
            "$2.5M seed (Aug 2026, VentureRadar/Undercurrent) after seaweed-prize finalist signal. Founders Nick Hill (ecologist, ZSL/Imperial) "
            "& Amado \"Madz\" Blanco (Project Seahorse). Net-Works heritage with Interface."
        ),
        "description": (
            "Regenerative smallholder seaweed supply (GROW + iMPAs) across SE Asia; $2.5M seed (Aug 2026); "
            "ZSL spinout; 705 t dried traded 2024; 5,868 ha community MPAs."
        ),
        "raw": f"""# Coast 4C – Raw Web Extract
**Source:** https://www.coast4c.com/
**Also:** https://www.coast4c.com/our-story
**Also:** VentureRadar Ocean funding list (02 Aug 2026) — $2.5M seed; Undercurrent News seaweed prize finalist coverage
**Extracted:** {DATE}

## Overview
Coast 4C builds dependable supply of quality, responsibly sourced regenerative seaweed while lifting smallholder coastal communities. Brand promise: the 4Cs — Community, Commerce, Conservation, Climate. Operates primarily with eucheumatoid smallholders in the Philippines and broader SE Asia (>85% of global eucheumatoid production is small-scale fishers in PH/ID often at/below poverty line). Launched 2020; official ZSL spinout 2022. Roots in Net-Works™ (ZSL + Interface) community engagement model. Founders: Nick Hill (ecologist; ZSL / Imperial College London PhD path; 4,000+ community interviews) and Amado "Madz" Blanco (Project Seahorse Foundation marine conservation leader).

## Business Model
- **Buyers**: B2B supply of traceable regenerative seaweed for food, feed, fertiliser, plastics/materials brands — competitive price with provenance and impact claims
- **Farmers (GROW programme)**: regenerative farm input packages, education, finance, and insurance — 286 farmers by end-2024; targeting 500 families by end-2025
- **Ocean protectors**: expand community-based marine protected areas (iMPAs) with local governments/NGOs, funded/maintained via farmer model
- Scale thesis: "smallholders are the only proven route to scale" augmented with multidisciplinary agtech/finance rather than industrial monoculture alone
- Long-term ambition: develop 500,000 seaweed farming families across SE Asia

## Funding / Traction
- **$2.5M seed** (announced ~Aug 2 2026 per VentureRadar Ocean funding tracker / Undercurrent News — seaweed-focused prize finalist attractor)
- Operational traction: **1,200% YoY growth** in seaweed traded; **705 t dried seaweed** sold YTD 2024
- Conservation: **5,868 hectares** protected across **eight** community-based iMPAs

## Key Technology / Programs
- GROW regenerative input + training package for smallholders
- Supply-chain visibility: quantity, scheduling, quality, species, logistics for buyers
- Community iMPA model linking livelihoods to marine protection
- Not a sensor OEM — platform/services + market access + finance/insurance stack around seaweed aquaculture

## Marine / Data Needs
- Farm site suitability (temp, salinity, nutrients, pollution), disease/ice-ice risk, yield forecasting, traceability/MRV for regenerative claims, MPA ecological KPIs, buyer ESG reporting

## Contacts
- https://www.coast4c.com/
- Founder/CEO: Nicholas Hill; Co-founder: Amado "Madz" Blanco
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Coast 4C",
            "url": "https://www.coast4c.com/",
            "description": "Regenerative smallholder seaweed supply platform linking GROW farmer packages, buyer traceability, and community marine protected areas across Southeast Asia.",
            "foundingLocation": {"@type": "Place", "name": "Southeast Asia / Philippines (ZSL spinout)"},
            "founder": [
                {"@type": "Person", "name": "Nicholas Hill", "jobTitle": "Founder & CEO"},
                {"@type": "Person", "name": "Amado Blanco", "jobTitle": "Co-founder"},
            ],
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "USD",
                "value": 2500000,
                "description": "$2.5M seed (Aug 2026) following seaweed-prize finalist recognition",
            },
            "sector": "Aquaculture",
            "businessModel": "Two-sided regenerative seaweed marketplace + farmer GROW inputs/finance/insurance + community iMPA conservation model",
            "lastFundingRound": "$2.5M seed (Aug 2026)",
            "totalFunding": "$2.5M disclosed seed",
            "knowsAbout": [
                "Seaweed aquaculture",
                "Smallholder regenerative farming",
                "Community marine protected areas",
                "Seaweed supply chain traceability",
                "Blue economy livelihoods",
            ],
            "product": ["GROW programme", "Regenerative seaweed supply", "Community iMPAs"],
            "parentOrganization": {
                "@type": "Organization",
                "name": "Zoological Society of London",
                "description": "Spun out 2022 (launched 2020)",
            },
        },
        "wiki_body": f"""# Coast 4C

**Sector**: Aquaculture
**Official Site**: https://www.coast4c.com/
**Last Updated**: {DATE}

**Focus**: Regenerative smallholder seaweed supply at SE Asia scale — GROW farmer packages + buyer-grade traceable eucheumatoids + community marine protected areas (the 4Cs: Community, Commerce, Conservation, Climate).
**Status**: **$2.5M seed** (Aug 2026); **705 t dried** seaweed traded (2024 YTD) with **1,200% YoY** growth; **5,868 ha** across 8 community iMPAs; 286 GROW farmers (end-2024) → 500 families target (end-2025).
**HQ / roots**: Philippines & SE Asia operations; ZSL spinout (launch 2020, spinout 2022). Founders Nick Hill (ecologist; ZSL/Imperial) & Amado "Madz" Blanco (Project Seahorse). Net-Works™ heritage with Interface.

## Business Model
Two-sided regenerative seaweed platform:
1. **Buyers** — dependable, provenance-rich seaweed for food, feed, fertiliser, and materials/plastics brands at competitive price
2. **Farmers** — GROW programme delivers regenerative inputs, education, finance, and insurance so smallholders improve yield/quality and livelihoods
3. **Ocean protectors** — community iMPAs expanded with local government/NGO partners, sustained by the farmer economic model

Thesis (CEO Hill): smallholders are the only proven route to global eucheumatoid scale; the gap is meaningful investment in agtech/finance layered on local ecological knowledge — not replacing farmers with industrial monoculture. Ambition: **500,000** seaweed farming families across SE Asia. Complements cultivation genetics ([MacroBreed](macrobreed.md), [Dirigo Sea Farm](dirigo-sea-farm.md)) and full-stack farm IoT ([AquaExchange](aquaexchange.md)) by owning the **smallholder supply + conservation** layer.

## Funding
- **$2.5M seed** (Aug 2026) — reported via ocean-tech funding trackers / Undercurrent News after seaweed-prize finalist recognition
- Non-dilutive heritage: years of ZSL science + Net-Works community model before commercial spinout

## Key Technology / Programs
- GROW regenerative farm input packages + training
- Buyer supply control tower: quantity, scheduling, quality, species availability, logistics
- Community-based iMPA design and maintenance linked to farmer livelihoods
- Multidisciplinary field team many of whom come from served communities

## Data & Measurement Needs
- **Primary data types**: Farm-site oceanographic conditions, harvest volumes/quality grades, farmer livelihood KPIs, iMPA ecological indicators, chain-of-custody/traceability events, buyer ESG claim evidence
- **Key measurements/parameters**: SST, salinity, nutrients, turbidity, ice-ice disease incidence, dried-tonnage yield per family, income deltas, hectares under protection, biodiversity/ benthic metrics inside iMPAs, carbon/nutrient remediation proxies
- **Observation platforms/programs**: Field extension + farmer reporting; community MPA patrols; growing need for remote sensing of farm plots and water quality
- **Known data gaps**: Standardized regenerative-seaweed MRV accepted by global brands; high-res coastal water-quality for thousands of small plots; disease early-warning at village scale; interoperable traceability from plot to processor
- **Interest in external data services**: Satellite SST/ocean color, coastal nutrient models, eDNA/biosensors ([Nucleic Sensing Systems](nucleic-sensing-systems.md)), storm/climate risk layers, blue-carbon methodologies adjacent to [ocean carbon](ocean-carbon-sequestration.md) buyers

---

**Cross-links**: [Aquaculture](aquaculture.md) · [MacroBreed](macrobreed.md) · [Dirigo Sea Farm](dirigo-sea-farm.md) · [AquaExchange](aquaexchange.md) · [Kelp Blue](kelp-blue.md) · [Ocean Carbon Sequestration](ocean-carbon-sequestration.md)
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

    # Refresh Oshen funding notes
    for c in companies:
        if c["name"] == "Oshen":
            c["notes"] = (
                "Autonomous ocean robots (C-Stars) for persistent wide-area ocean intelligence; swarms of wind/solar USVs. "
                "Customers: US Navy, Royal Navy, Met Office. NOAA hurricane contracts; UK ARIA Forecasting Tipping Points heritage. "
                "**£3.65M / ~$5M equity (Aug 2026)** led by Lunar Ventures with AlbionVC, Twin Track, Concept Ventures + angels — "
                "to triple C-Star manufacturing (CEO Anahita Laverack: production as 'fast-food kitchen not shipyard'). "
                "Plymouth, UK; team ~30. Real-time wave height, wind, oceanographic telemetry."
            )
            c["last_updated"] = DATE
            print("Updated Oshen funding notes")
            break

    with open(sources_path, "w") as f:
        json.dump(companies, f, indent=2)
        f.write("\n")
    print(f"companies.json now has {len(companies)} entries")


if __name__ == "__main__":
    write_profiles()
