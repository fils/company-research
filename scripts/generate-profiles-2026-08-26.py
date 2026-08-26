#!/usr/bin/env python3
"""Daily update 2026-08-26: ShipIn Systems, Ocean Intelligence, AquaNab, Kuehnle AgroSystems, Vessev."""
import json, os, re
from datetime import datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "2026-08-26"
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
        "name": "ShipIn Systems",
        "url": "https://shipin.ai/",
        "sector": "Maritime Operations & Analytics",
        "tag": "maritime-operations-analytics",
        "notes": (
            "Boston AI operating system for commercial shipping — FleetVision computer vision on onboard CCTV + vessel systems/sensors. "
            "$52M financing (Aug 2026) with Proofpoint Capital, HighSage, Bling, Framework, Tokio Marine Future Fund; existing Zeev Ventures, "
            "Munich Re, Atinc, Hyperplane. Deployed on 92 shipowners / 1,300+ vessels. Modules: Safety, Bridge, Technical, Security, MARPOL, Cargo. "
            "Insurer-backed prevention model. CEO Osher Perry; board: Matt Wallach (Proofpoint Capital / Veeva co-founder)."
        ),
        "description": (
            "AI-powered FleetVision operational intelligence for commercial shipping — onboard CCTV + sensors; "
            "$52M (Aug 2026); 1,300+ vessels / 92 shipowners."
        ),
        "raw": f"""# ShipIn Systems – Raw Web Extract
**Source:** https://shipin.ai/
**Also:** https://shipin.ai/insights/52-million-financing-connected-ship
**Also:** https://smartmaritimenetwork.com/2026/08/04/shipin-raises-52m-to-expand-ai-platform/
**Also:** https://dealroom.co/news/142939-shipin-raises-52m-series-b-to-expand-maritime-ai-platform/
**Extracted:** {DATE}

## Overview
ShipIn Systems (Boston) builds the AI operating system for commercial shipping. Flagship FleetVision applies AI/computer vision to onboard CCTV and fuses vessel systems, sensors, and enterprise apps into ship-to-shore operational intelligence for safety, security, technical reliability, bridge watchkeeping, and MARPOL compliance.

## Business Model
- Hardware-enabled SaaS / platform: AI on vessel cameras + sensor/context fusion
- Sold to shipowners and fleet operators (Anglo-Eastern, Rio Tinto, Stealth, Hafnia, NYK Line, Matson, Tufton, etc.)
- Dual value: (1) crew/onboard real-time risk correction; (2) shore-side QHSE, TMSA evidence, insurance/loss-prevention alignment
- Insurer co-investment (Tokio Marine Future Fund, Munich Re) signals prevention-over-payout GTM

## Funding
- **$52M financing** (announced ~Aug 4 2026) — new: Proofpoint Capital, HighSage Ventures, Bling Ventures, Framework Venture Partners, Tokio Marine Future Fund
- Existing: Zeev Ventures, Munich Re, Atinc, Hyperplane Ventures
- Prior: Series A ~$24M with Zeev Ventures; Munich Re Ventures earlier investment
- Board: Matt Wallach (Proofpoint Capital / Veeva Systems co-founder) joins board
- Use of proceeds: international expansion, deeper AI, product (FleetVision), partnerships, IP

## Key Technology / Products
- FleetVision modules: Safety (PPE/unsafe behavior), Bridge (watchkeeping/collision risk behaviors), Technical (fire/engine-room risk), Security (unauthorized access), MARPOL (pollution equipment evidence), Cargo (coming soon)
- Continuous learning cycle across voyages — fleetwide KPI benchmarking
- Deployment scale: **92 shipowners, 1,300+ vessels** (one of largest AI deployments in commercial shipping)

## Contacts
- HQ Boston, MA; https://shipin.ai/ ; media jamess@shipin.ai (James Solada, VP Marketing)
- CEO/Founder: Osher Perry
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "ShipIn Systems",
            "url": "https://shipin.ai/",
            "description": "AI-powered operational intelligence / FleetVision platform for commercial shipping safety, security, bridge, technical, and MARPOL compliance.",
            "foundingLocation": {"@type": "Place", "name": "Boston, Massachusetts, USA"},
            "founder": [{"@type": "Person", "name": "Osher Perry", "jobTitle": "Founder & CEO"}],
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "USD",
                "value": 52000000,
                "description": "$52M financing (Aug 2026) with Proofpoint Capital and Tokio Marine Future Fund among new investors",
            },
            "sector": "Maritime Operations & Analytics",
            "businessModel": "AI computer-vision SaaS + onboard camera/sensor fusion sold to shipowners; insurer-aligned prevention platform",
            "lastFundingRound": "$52M (Aug 2026) — Proofpoint Capital, HighSage, Bling, Framework, Tokio Marine Future Fund + existing Zeev/Munich Re/Atinc/Hyperplane",
            "totalFunding": "$52M+ disclosed latest round (prior Series A ~$24M+)",
            "investors": [
                "Proofpoint Capital",
                "HighSage Ventures",
                "Bling Ventures",
                "Framework Venture Partners",
                "Tokio Marine Future Fund",
                "Zeev Ventures",
                "Munich Re",
                "Atinc",
                "Hyperplane Ventures",
            ],
            "knowsAbout": [
                "Maritime computer vision",
                "Fleet safety AI",
                "Ship-to-shore operational intelligence",
                "MARPOL compliance evidence",
                "Marine insurance loss prevention",
            ],
            "product": ["FleetVision", "Safety", "Bridge", "Technical", "Security", "MARPOL"],
            "numberOfEmployees": {"@type": "QuantitativeValue", "value": "50-200"},
            "customer": [
                "Anglo-Eastern",
                "Rio Tinto",
                "Stealth Maritime",
                "Hafnia",
                "NYK Line",
                "Matson",
                "Tufton",
            ],
        },
        "wiki_body": f"""# ShipIn Systems

**Sector**: Maritime Operations & Analytics
**Official Site**: https://shipin.ai/
**Last Updated**: {DATE}

**Focus**: AI operating system for commercial shipping — FleetVision turns onboard CCTV, vessel systems, and sensors into continuous operational intelligence for safety, bridge, technical, security, and MARPOL.
**Status**: $52M financing (Aug 2026); deployed across **92 shipowners / 1,300+ vessels**.
**HQ**: Boston, MA — Founder/CEO Osher Perry

## Business Model
Hardware-enabled AI SaaS sold to shipowners and fleet operators. Revenue from fleet deployments of FleetVision that close the ship-to-shore visibility gap. Differentiated GTM with marine insurers (Tokio Marine Future Fund, Munich Re) backing a **prevention-over-payout** thesis — objective operational evidence for TMSA, QHSE, and claims reduction. Customers include Anglo-Eastern, Rio Tinto, Stealth Maritime, Hafnia, NYK Line, Matson, Tufton and others.

## Funding
- **$52M financing** (Aug 2026): new investors Proofpoint Capital, HighSage Ventures, Bling Ventures, Framework Venture Partners, Tokio Marine Future Fund; existing Zeev Ventures, Munich Re, Atinc, Hyperplane Ventures
- Board addition: Matt Wallach (Proofpoint Capital; co-founder Veeva Systems)
- Prior: Series A led by Zeev Ventures (~$24M era); Munich Re Ventures strategic investment

## Key Technology
- FleetVision AI on onboard CCTV with five+ modules: Safety, Bridge, Technical, Security, MARPOL (Cargo upcoming)
- Fuses cameras + vessel systems + sensors + enterprise apps into one fleet risk dashboard
- Continuous voyage learning cycle; fleetwide KPI benchmarking and behavioral safety culture reinforcement
- Scale signal: one of the largest commercial-shipping AI deployments publicly disclosed (1,300+ vessels)

## Data & Measurement Needs
- **Primary data types**: Onboard CCTV video streams (deck, bridge, engine room, critical spaces), vessel telemetry, sensor/context feeds, enterprise SMS/QHSE records, voyage metadata
- **Key measurements/parameters**: PPE compliance events, unsafe positioning/behavior rates, watchkeeping lapses, near-miss indicators, engine-room fire/abnormal-use signals, unauthorized access events, MARPOL equipment interaction evidence, fleet risk scores/KPIs
- **Observation platforms/programs**: Ship-mounted camera networks across 1,300+ vessels; continuous ship-to-shore data pipeline; oil-major TMSA audit evidence workflows
- **Known data gaps**: Coverage depends on camera placement and vessel connectivity; limited oceanographic/metocean context natively; cargo module still emerging
- **Interest in external data services**: Weather/route risk layers, AIS traffic density, port state control histories, insurer loss databases, satellite connectivity for low-bandwidth fleets

---

**Cross-links**: [Maritime Operations & Analytics](maritime-operations-analytics.md) · [Orca AI](orca-ai.md) · [SEA.AI](sea-ai.md) · [Sea Machines Robotics](sea-machines-robotics.md)
""",
    },
    {
        "name": "Ocean Intelligence",
        "url": "https://oceanintelligence.io/",
        "sector": "Ocean Data & AI",
        "tag": "ocean-data-ai",
        "notes": (
            "NZ Cawthron Institute + Oceanum spin-out: modular SaaS unifying real-time marine environmental monitoring, forecasts, and ops data "
            "for aquaculture (HAB/water quality/harvest timing), ports/coastal ops, and councils/research. Pre-seed (Aug 2026) led by Quidnet Ventures "
            "Fund II with Andrea & Guido Neitzer; 24-month runway for product + Australia expansion. CEO Joel Bowater; Nelson, NZ. Mussel/oyster farms live."
        ),
        "description": (
            "Cawthron–Oceanum spin-out SaaS for unified marine environmental forecasting & ops intelligence (aqua, ports, coastal); "
            "pre-seed Quidnet Ventures (Aug 2026)."
        ),
        "raw": f"""# Ocean Intelligence – Raw Web Extract
**Source:** https://oceanintelligence.io/
**Also:** https://thefishsite.com/articles/ocean-intelligence-raises-pre-seed-funding
**Also:** https://www.finsmes.com/2026/08/ocean-intelligence-raises-pre-seed-funding.html
**Extracted:** {DATE}

## Overview
Ocean Intelligence (Nelson, New Zealand) is a marine technology spin-out founded by Cawthron Institute and Oceanum. Modular SaaS consolidates real-time marine environmental data, forecasts, and operational feeds into a single operating picture for aquaculture, port/coastal operators, and councils/research monitoring programmes.

## Business Model
- Modular SaaS / operational intelligence platform
- Beachhead: NZ mussel and oyster aquaculture (live customers); expansion to Australia aquaculture and maritime ops
- Three deployment modes: Aquaculture Intelligence, Port & Coastal Monitoring, Coastal Research & Monitoring

## Funding
- **Pre-seed** (Aug 2026, undisclosed) — led by Quidnet Ventures (first investment from Quidnet Ventures Fund II)
- Participation: Andrea Neitzer and Guido Neitzer (AIP investors)
- Provides ~24-month operating runway; use for product development, marine engineering team, Australia market entry
- CEO: Joel Bowater

## Key Technology
- Unifies monitoring sensors, forecasts, and operational data
- Early warning for harmful algal blooms (HABs), storm events, water-quality shifts, harvest timing
- Built on 20+ years Cawthron aquaculture/ocean tech research + Oceanum ocean modelling/data systems
- Production-grade data delivery for day-to-day operator decisions

## Contacts
- https://oceanintelligence.io/ ; contact form
- Nelson, New Zealand
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Ocean Intelligence",
            "url": "https://oceanintelligence.io/",
            "description": "Marine environmental forecasting and operational intelligence SaaS for aquaculture, ports, and coastal monitoring — Cawthron Institute and Oceanum spin-out.",
            "foundingLocation": {"@type": "Place", "name": "Nelson, New Zealand"},
            "founder": [
                {"@type": "Organization", "name": "Cawthron Institute"},
                {"@type": "Organization", "name": "Oceanum"},
            ],
            "employee": [{"@type": "Person", "name": "Joel Bowater", "jobTitle": "CEO"}],
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "USD",
                "description": "Pre-seed (Aug 2026) led by Quidnet Ventures Fund II with Andrea & Guido Neitzer",
            },
            "sector": "Ocean Data & AI",
            "businessModel": "Modular SaaS operational ocean intelligence for aquaculture, ports, and coastal monitoring programmes",
            "lastFundingRound": "Pre-seed Aug 2026 — Quidnet Ventures (lead), Andrea & Guido Neitzer",
            "investors": ["Quidnet Ventures", "Andrea Neitzer", "Guido Neitzer"],
            "knowsAbout": [
                "Harmful algal bloom forecasting",
                "Aquaculture environmental intelligence",
                "Port coastal ocean monitoring",
                "Marine forecast fusion",
                "Operational oceanography",
            ],
            "product": [
                "Aquaculture Intelligence",
                "Port & Coastal Monitoring",
                "Coastal Research & Monitoring",
            ],
        },
        "wiki_body": f"""# Ocean Intelligence

**Sector**: Ocean Data & AI
**Official Site**: https://oceanintelligence.io/
**Last Updated**: {DATE}

**Focus**: Modular SaaS that unifies marine monitoring, forecasts, and operational data into one operating picture for aquaculture, ports, and coastal programmes.
**Status**: Pre-seed (Aug 2026) led by Quidnet Ventures Fund II; NZ live on mussel/oyster farms; Australia expansion.
**Origin**: Spin-out of [Cawthron Institute](https://www.cawthron.org.nz/) + [Oceanum](https://oceanum.io/); CEO Joel Bowater; Nelson, NZ.

## Business Model
SaaS operational intelligence sold to marine operators drowning in disconnected data feeds. Three shaped deployments: (1) **Aquaculture Intelligence** — water quality, biosecurity triggers, harvest timing; (2) **Port & Coastal Monitoring** — local sensors + forecasts + vessel scheduling/berth windows; (3) **Coastal Research & Monitoring** — QC'd observing programmes for councils/research with public-facing delivery. Beachhead NZ shellfish aquaculture; commercial push into Australia.

## Funding
- **Pre-seed** (Aug 13–17 2026 reporting): Quidnet Ventures lead (first Fund II deal); Andrea & Guido Neitzer participate
- ~24-month runway for product, engineering team, and Australia GTM
- Amount undisclosed

## Key Technology
- Fusion of real-time environmental sensors, ocean model forecasts, and operational context
- Automated early warning for HABs, storm surge, and water-quality regime shifts
- Grounded in 20+ years Cawthron marine science + Oceanum modelling/data infrastructure
- Production-grade systems designed for day-to-day operator use (not research-only dashboards)

## Data & Measurement Needs
- **Primary data types**: In-situ water quality time series, ocean model forecast fields, local coastal sensors, vessel/ops schedules, HAB/toxin monitoring streams
- **Key measurements/parameters**: Temperature, salinity, dissolved oxygen, chlorophyll/fluorescence, turbidity, currents/waves, HAB cell counts/toxin risk indices, storm surge, berth window metocean
- **Observation platforms/programs**: Farm-site sensors, coastal moorings, model downscaling (Oceanum heritage), council coastal monitoring programmes
- **Known data gaps**: Cross-border data standards AU↔NZ; sparse real-time toxin assays vs proxy sensors; multi-farm interoperability
- **Interest in external data services**: National metocean forecasts, satellite ocean color, regional HAB bulletins, port AIS/scheduling APIs, public coastal observing networks

---

**Cross-links**: [Ocean Data & AI](ocean-data-ai.md) · [Sofar Ocean](sofar-ocean.md) · [Coastal Measures](coastal-measures.md) · [BiOceanOr](bioceanor.md) · [Aquaculture](aquaculture.md)
""",
    },
    {
        "name": "AquaNab",
        "url": "https://aquanabs.de/",
        "sector": "Aquaculture",
        "tag": "aquaculture",
        "notes": (
            "Hamburg biotech: alpaca-derived nanoantibodies (AquaNabs) delivered via fish feed for oral sea-lice treatment in Atlantic salmon — "
            "non-toxic, stress-free, residue-free alternative to chemical/mechanical delousing ($4B industry cost). Nordic Foodtech VC investment "
            "(first deal outside Nordics, Aug 2026). Co-founders Dr Ruth Tamara Montero (CEO), Dr Alejandro Rojas Fernandez (CSO), Gunnar Johildarson. "
            "Platform expandable to bacterial/viral/parasitic diseases across species. montero@aquanab.com."
        ),
        "description": (
            "Feed-delivered alpaca nanoantibodies for sea lice in salmon — Nordic Foodtech VC-backed (Aug 2026); Hamburg precision aqua health."
        ),
        "raw": f"""# AquaNab – Raw Web Extract
**Source:** https://aquanabs.de/
**Also:** https://thefishsite.com/articles/investment-backs-novel-feed-based-sea-lice-treatment
**Extracted:** {DATE}

## Overview
AquaNab (Hamburg, Germany — Altona Innovation Park) develops next-generation nanoantibody therapeutics for aquaculture. Lead programme: AquaNabs against sea lice in Atlantic salmon, delivered orally through fish feed. First-in-world application of alpaca-derived nanoantibodies via feed that cross the intestinal barrier into bloodstream. Non-toxic, stress-free, residue-free alternative to chemical and mechanical delousing.

## Business Model
- Precision immunotherapeutics platform for aquatic animal health
- Lead product: feed-based anti-sea-lice nanoantibodies for Atlantic salmon
- Platform expandable to bacterial, viral, and parasitic diseases across aquaculture species
- Collaborations with salmon producers, feed manufacturers, animal health companies
- Seeking additional investment beyond Nordic Foodtech to accelerate PoC → market

## Funding
- Investment from **Nordic Foodtech VC** (announced ~Aug 11 2026) — firm's first investment outside the Nordics
- Amount undisclosed; advancing lead programme toward finalising proof of concept
- Co-founders: Dr Ruth Tamara Montero (CEO), Dr Alejandro Rojas Fernandez (CSO; prior SARS-CoV-2 nanoAb work), Gunnar Johildarson

## Key Technology
- Alpaca immunization → specific nanoantibodies targeting salmon pathogens/parasites
- Oral delivery via feed; demonstrated intestinal barrier crossing into bloodstream
- Organic protein-based, 100% sustainable positioning vs chemical bath treatments
- Rapid on-site integration claim (minimize operational complexity vs mechanical delousing)

## Market context
- Sea lice costs industry estimated US $4B annually (treatment, lost production, mortality)
- Regulatory/retailer/welfare pressure against chemical runoff and stressful mechanical methods

## Contacts
- montero@aquanab.com
- Tech-Hub, Altona Innovation Park, Elly-See-Straße 1, 22547 Hamburg
- https://aquanabs.de/
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "AquaNab",
            "url": "https://aquanabs.de/",
            "description": "Hamburg aquaculture biotech developing feed-delivered alpaca nanoantibodies (AquaNabs) against sea lice and other pathogens.",
            "foundingLocation": {"@type": "Place", "name": "Hamburg, Germany"},
            "founder": [
                {"@type": "Person", "name": "Ruth Tamara Montero", "jobTitle": "CEO"},
                {"@type": "Person", "name": "Alejandro Rojas Fernandez", "jobTitle": "CSO"},
                {"@type": "Person", "name": "Gunnar Johildarson"},
            ],
            "email": "montero@aquanab.com",
            "funding": {
                "@type": "MonetaryAmount",
                "description": "Investment from Nordic Foodtech VC (Aug 2026); amount undisclosed",
            },
            "sector": "Aquaculture",
            "businessModel": "Precision feed-based nanoantibody therapeutics platform for aquaculture disease (lead: sea lice)",
            "lastFundingRound": "Nordic Foodtech VC investment (Aug 2026) — first NFT deal outside Nordics",
            "investors": ["Nordic Foodtech VC"],
            "knowsAbout": [
                "Nanoantibodies",
                "Sea lice control",
                "Oral aquaculture therapeutics",
                "Atlantic salmon health",
                "Feed-based drug delivery",
            ],
            "product": ["AquaNabs (anti-sea lice)"],
        },
        "wiki_body": f"""# AquaNab

**Sector**: Aquaculture
**Official Site**: https://aquanabs.de/
**Last Updated**: {DATE}

**Focus**: Feed-delivered alpaca-derived nanoantibodies (AquaNabs) for oral treatment of sea lice and a broader aquatic pathogen platform.
**Status**: Nordic Foodtech VC investment (Aug 2026); lead programme advancing to finalise proof of concept.
**HQ**: Hamburg, Germany (Altona Innovation Park) — CEO Dr Ruth Tamara Montero; CSO Dr Alejandro Rojas Fernandez.

## Business Model
Precision immunotherapeutics for aquaculture health. Differentiator vs [Biosort](biosort.md) (individual mechanical/optical intervention) and chemical/mechanical delousing: **non-toxic, stress-free, residue-free oral nanoantibodies in feed**. Platform designed to expand beyond sea lice to bacterial, viral, and parasitic diseases across species. GTM via salmon producers, feed manufacturers, and animal-health partners. Contact: montero@aquanab.com.

## Funding
- **Nordic Foodtech VC** investment (reported Aug 11 2026) — first investment outside the Nordics for the firm
- Amount undisclosed; company seeking additional capital to accelerate development and first products to market

## Key Technology
- Alpaca immunization pipeline producing pathogen-specific nanoantibodies
- Demonstrated intestinal barrier crossing into fish bloodstream after oral/feed delivery
- First-in-world feed-route nanoantibody application in aquaculture (company claim)
- Organic protein-based alternative to bath chemicals and stressful mechanical treatments

## Data & Measurement Needs
- **Primary data types**: Sea lice counts (adults/chalimus), treatment efficacy time series, fish welfare/stress biomarkers, feed intake/compliance, residue assays, pathogen load (qPCR/eDNA)
- **Key measurements/parameters**: Lice abundance per fish, FCR, mortality, cortisol/welfare scores, antibody titer/pharmacokinetics, water chemistry around pens during treatment windows
- **Observation platforms/programs**: Cage-level lice counting programmes, welfare cameras (complement [Ace Aquatec](ace-aquatec.md)/[Biosort](biosort.md)), lab PoC trials with producer partners
- **Known data gaps**: Standardised field efficacy datasets vs commercial chemical baselines; multi-site PK/PD under varying salinity/temp; resistance monitoring frameworks for biologic actives
- **Interest in external data services**: Producer lice pressure networks, environmental discharge regulations, feed mill formulation data, pathogen genomic surveillance

---

**Cross-links**: [Aquaculture](aquaculture.md) · [Biosort](biosort.md) · [Ace Aquatec](ace-aquatec.md) · [Aquaticode](aquaticode.md)
""",
    },
    {
        "name": "Kuehnle AgroSystems",
        "url": "https://www.kuehnleagro.com/",
        "sector": "Aquaculture",
        "tag": "aquaculture",
        "notes": (
            "Honolulu algal biotech: proprietary dark fermentation of non-GMO Haematococcus for natural astaxanthin oleoresin — "
            "first industrial-scale demonstration with Biorea; multi-million Series B (Jul 2026) led by Ichthus Venture Capital (IVC) with S2G, "
            "Hatch Blue, Dest EOOD. Strategic partnership with Corbion for scale-up/regulatory/GTM. Targets aquaculture feed (salmon pigmentation/health) "
            "and human nutraceuticals; claims ~90% cost reduction vs phototrophic cultivation. CEO Dr Claude Kaplan."
        ),
        "description": (
            "Dark-fermentation natural astaxanthin for aquafeed & nutraceuticals; multi-million Series B (IVC/S2G/Hatch/Dest); Corbion partner."
        ),
        "raw": f"""# Kuehnle AgroSystems (KAS) – Raw Web Extract
**Source:** https://www.kuehnleagro.com/
**Also:** https://thefishsite.com/articles/kas-secures-series-b-to-commercialise-dark-fermentation-astaxanthin
**Also:** https://www.globenewswire.com/news-release/2025/08/19/3135449/0/en/Corbion-and-Kuehnle-AgroSystems-join-forces-to-develop-natural-astaxanthin-from-algae-fermentation.html
**Extracted:** {DATE}

## Overview
Kuehnle AgroSystems (KAS, Honolulu, US) produces high-value natural microalgal products via patented dark (heterotrophic) fermentation. Lead product: affordable natural astaxanthin for aquaculture feed (salmon pigmentation + health) and human nutrition. With manufacturing partner Biorea, demonstrated world's first natural astaxanthin oleoresin via dark fermentation at industrially relevant scale. Strategic development partner: Corbion.

## Business Model
- Algal biotechnology ingredients company — sell natural astaxanthin (and protein pipeline) into aquafeed and nutraceutical channels
- Manufacturing scale via partners (Biorea demonstrated; Corbion industrial fermentation/regulatory/commercial muscle)
- Claims: production in days vs weeks; ~90% cost reduction; lower land/water/energy vs phototrophic ponds/photobioreactors
- Dual markets: aquaculture ($2B astaxanthin market growing ~15%/yr) + premium human antioxidant nutraceuticals

## Funding
- **Multi-million-dollar Series B** (reported Jul 8 2026) — led by Ichthus Venture Capital (IVC)
- Existing: S2G Investments, Hatch Blue
- New: Dest EOOD
- Board: Frode Sandmark (IVC) joins
- Use: R&D expansion, Corbion strategic programme, salmon feed product validation, global regulatory approvals, manufacturing scale-up
- CEO: Dr Claude Kaplan

## Key Technology
- Patented dark fermentation + patented natural (non-GMO) algal strains (Haematococcus heterotrophic)
- Standard fermentation equipment; esterified astaxanthin rich in bioavailable isomer
- Industrial-scale oleoresin demonstration with Biorea
- Secondary pipeline: microalgal protein

## Contacts
- https://www.kuehnleagro.com/
- Honolulu, Hawaii, USA
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Kuehnle AgroSystems",
            "alternateName": "KAS",
            "url": "https://www.kuehnleagro.com/",
            "description": "Algal biotechnology company producing natural astaxanthin via proprietary dark fermentation for aquaculture feed and human nutrition.",
            "foundingLocation": {"@type": "Place", "name": "Honolulu, Hawaii, USA"},
            "employee": [{"@type": "Person", "name": "Claude Kaplan", "jobTitle": "CEO"}],
            "funding": {
                "@type": "MonetaryAmount",
                "description": "Multi-million Series B (Jul 2026) led by Ichthus Venture Capital with S2G, Hatch Blue, Dest EOOD",
            },
            "sector": "Aquaculture",
            "businessModel": "Natural astaxanthin ingredient sales via dark fermentation manufacturing partnerships (Biorea/Corbion) into aquafeed and nutraceuticals",
            "lastFundingRound": "Series B multi-million (Jul 2026) — IVC lead; S2G, Hatch Blue, Dest EOOD",
            "investors": ["Ichthus Venture Capital", "S2G Investments", "Hatch Blue", "Dest EOOD"],
            "partner": ["Corbion", "Biorea"],
            "knowsAbout": [
                "Dark fermentation",
                "Natural astaxanthin",
                "Microalgae biotechnology",
                "Aquaculture feed ingredients",
                "Heterotrophic Haematococcus",
            ],
            "product": ["Natural astaxanthin oleoresin", "Microalgal protein"],
        },
        "wiki_body": f"""# Kuehnle AgroSystems

**Sector**: Aquaculture
**Official Site**: https://www.kuehnleagro.com/
**Last Updated**: {DATE}

**Focus**: Patented dark (heterotrophic) fermentation of non-GMO microalgae for affordable natural astaxanthin — aquafeed pigmentation/health and human nutraceuticals.
**Status**: Multi-million **Series B** (Jul 2026, IVC lead); industrial-scale oleoresin demo with Biorea; strategic scale-up with Corbion.
**HQ**: Honolulu, Hawaii — CEO Dr Claude Kaplan (also styled KAS).

## Business Model
Ingredient platform company: produce natural astaxanthin cheaper and more sustainably than phototrophic cultivation or synthetic alternatives, then sell into salmon feed and premium human nutrition. Manufacturing leverage via Biorea (demo scale) and **Corbion** (industrial fermentation, regulatory, global GTM — partnership announced Aug 2025). Claims ~90% production-cost reduction and days-not-weeks cycle times using standard fermenters. Secondary product line: microalgal protein.

## Funding
- **Series B multi-million** (Jul 2026): Ichthus Venture Capital (lead); S2G Investments; Hatch Blue; new investor Dest EOOD
- IVC's Frode Sandmark joins board
- Use of proceeds: R&D, Corbion programme, salmon feed validation, regulatory approvals, manufacturing deployment

## Key Technology
- Proprietary dark fermentation + patented natural algal strains (heterotrophic Haematococcus)
- World's first natural astaxanthin oleoresin via dark fermentation at industrially relevant scale (with Biorea)
- Esterified, bioavailable isomer focus for antioxidant performance and fat solubility
- Lower land, water, energy footprint vs pond/PBR phototrophic routes

## Data & Measurement Needs
- **Primary data types**: Fermentation process analytics (DO, pH, biomass density, sugar feed rates), carotenoid titer/isomer profiles, oleoresin quality specs, aquafeed trial performance, LCA inventories
- **Key measurements/parameters**: Astaxanthin yield (mg/g DCW), ester profile, oxidative stability, salmon flesh pigmentation scores, FCR/health markers in feeding trials, energy/water intensity per kg product
- **Observation platforms/programs**: Industrial fermenter instrumentation; partner feed trials with salmon producers; regulatory dossier stability studies
- **Known data gaps**: Long-run commercial plant variability data; multi-region regulatory residue/label datasets; head-to-head published LCAs vs synthetic and phototrophic natural benchmarks
- **Interest in external data services**: Global aquafeed demand/price series, salmon production forecasts, nutraceutical channel data, industrial fermentation capacity networks

---

**Cross-links**: [Aquaculture](aquaculture.md) · [Oceanloop](oceanloop.md) · [Nernst Electric](nernst-electric.md)
""",
    },
    {
        "name": "Vessev",
        "url": "https://www.vessev.com/",
        "sector": "Offshore Energy",
        "tag": "offshore-energy",
        "notes": (
            "Auckland electric hydrofoiling passenger vessels (VS–9 line) — America's Cup-inspired dynamic foils + electric propulsion + onboard "
            "software/telemetry. $19M Series A (Aug 2026) led by Blackbird Ventures; GD1, Rypples new; existing K1W1, Icehouse, Shasta, NZVC, angels. "
            "Commercially certified vessels in NZ service; demand across 5 continents; US expansion (NY, DC, Lake Tahoe). CEO Eric Laakmann. Team from "
            "America's Cup, Rocket Lab, Apple, Tesla, Navico. Complements Fleetzero (batteries) on maritime electrification stack."
        ),
        "description": (
            "Electric hydrofoiling passenger vessels (VS–9); $19M Series A (Blackbird, Aug 2026); NZ commercial service + US expansion."
        ),
        "raw": f"""# Vessev – Raw Web Extract
**Source:** https://www.vessev.com/
**Also:** https://www.finsmes.com/2026/08/vessev-19m-in-series-a-funding.html
**Extracted:** {DATE}

## Overview
Vessev (Auckland, New Zealand) designs and builds electric hydrofoiling marine vessels for passenger services, luxury hospitality, waterfront developments, and tourism. Platform combines electric propulsion, America's Cup-inspired dynamic foil systems, and advanced onboard software/telemetry for quiet, low-wake, high-efficiency zero-emission water transit. CEO Eric Laakmann. Team backgrounds: America's Cup, Rocket Lab, Apple, Tesla, Navico.

## Business Model
- Vessel OEM + systems: design, build, assemble in-house; sell/reserve commercial passenger hydrofoils (VS–9 line)
- Markets: passenger ferries/services, luxury hospitality, waterfront real-estate transport, tourism experiences
- Commercially certified vessels already in service in New Zealand (industry-first commercial tourism certification claim)
- Demand spanning five continents; expanding US ops (New York, Washington D.C., Lake Tahoe)
- Series A funds serial production, GTM team, onboard software/telemetry, larger vessels, US manufacturing plans

## Funding
- **$19M Series A** (Aug 21 2026 reporting) — led by Blackbird Ventures
- New: GD1, Rypples
- Existing: K1W1, Icehouse Ventures, Shasta Ventures, NZVC, angels

## Key Technology
- Electric propulsion + dynamic hydrofoils (America's Cup-derived seakeeping)
- Low wake, smooth ride, easy charging positioning
- Onboard software and telemetry platform (fleet/ops data layer)
- In-house serial production of VS–9; roadmap to larger vessels

## Contacts
- https://www.vessev.com/ ; get-a-quote / contact
- Auckland, New Zealand
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Vessev",
            "url": "https://www.vessev.com/",
            "description": "Designer and builder of electric hydrofoiling passenger vessels combining foil systems, electric propulsion, and onboard telemetry software.",
            "foundingLocation": {"@type": "Place", "name": "Auckland, New Zealand"},
            "employee": [{"@type": "Person", "name": "Eric Laakmann", "jobTitle": "CEO"}],
            "funding": {
                "@type": "MonetaryAmount",
                "currency": "USD",
                "value": 19000000,
                "description": "$19M Series A (Aug 2026) led by Blackbird Ventures",
            },
            "sector": "Offshore Energy",
            "businessModel": "Electric hydrofoil vessel OEM + onboard software/telemetry for passenger, hospitality, and tourism marine transport",
            "lastFundingRound": "$19M Series A (Aug 2026) — Blackbird lead; GD1, Rypples, K1W1, Icehouse, Shasta, NZVC",
            "totalFunding": "$19M+ Series A disclosed",
            "investors": [
                "Blackbird Ventures",
                "GD1",
                "Rypples",
                "K1W1",
                "Icehouse Ventures",
                "Shasta Ventures",
                "NZVC",
            ],
            "knowsAbout": [
                "Electric hydrofoiling",
                "Marine electrification",
                "Passenger ferry decarbonization",
                "Dynamic foil control",
                "Vessel telemetry software",
            ],
            "product": ["VS–9 electric hydrofoil vessel", "Onboard software/telemetry platform"],
        },
        "wiki_body": f"""# Vessev

**Sector**: Offshore Energy
**Official Site**: https://www.vessev.com/
**Last Updated**: {DATE}

**Focus**: Electric hydrofoiling passenger vessels — America's Cup-inspired dynamic foils + electric propulsion + onboard software/telemetry for zero-emission water transit.
**Status**: **$19M Series A** (Aug 2026, Blackbird lead); commercially certified vessels in NZ service; US expansion (NY, DC, Lake Tahoe).
**HQ**: Auckland, New Zealand — CEO Eric Laakmann.

## Business Model
Full-stack vessel OEM: design, build, and assemble electric hydrofoils in-house (VS–9 line) for passenger services, luxury hospitality, waterfront developments, and tourism. Differentiator vs [Fleetzero](fleetzero.md) (modular marine batteries/propulsion systems): **complete hydrofoiling passenger platforms** with certified commercial service already running in New Zealand. Series A funds serial production, global GTM, software/telemetry, larger vessels, and US manufacturing.

## Funding
- **$19M Series A** (Aug 2026): Blackbird Ventures (lead); new GD1, Rypples; existing K1W1, Icehouse Ventures, Shasta Ventures, NZVC, angels

## Key Technology
- Electric propulsion + dynamic foil systems adapted from America's Cup yachts
- Low-wake, high-efficiency, quiet ride enabling new routes and waterfront connections
- Onboard software and telemetry platform for ops/performance
- Team DNA: America's Cup, Rocket Lab, Apple, Tesla, Navico
- Roadmap: VS–9 serial production → larger vessel classes

## Data & Measurement Needs
- **Primary data types**: Vessel telemetry (speed, foil state, power draw, battery SOC), ride-quality/IMU seakeeping, charging-session logs, route performance, passenger load factors
- **Key measurements/parameters**: Energy kWh/nm, foil flight stability envelopes, wake energy, charging time/availability, battery degradation, weather/sea-state operating limits
- **Observation platforms/programs**: Onboard sensor/software suite across commercial fleet; route trials in NZ and planned US waterways
- **Known data gaps**: Multi-climate long-duration battery/foil durability datasets; standardized ferry operator TCO benchmarks vs diesel catamarans; cold-weather charging infrastructure maps
- **Interest in external data services**: High-resolution coastal metocean (wave/wind/current) for foil envelope prediction, port charging-grid capacity, AIS passenger-route demand, regulatory certification databases

---

**Cross-links**: [Offshore Energy](offshore-energy.md) · [Fleetzero](fleetzero.md) · [Kvasir Technologies](kvasir-technologies.md) · [Aloft Systems](aloft-systems.md)
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

        # OKF frontmatter + body
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
            print(f"  (already in companies.json)")

    with open(sources_path, "w") as f:
        json.dump(companies, f, indent=2)
        f.write("\n")
    print(f"companies.json now has {len(companies)} entries")


if __name__ == "__main__":
    write_profiles()
