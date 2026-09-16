#!/usr/bin/env python3
"""Daily update 2026-09-16: WellFish Tech, WildTechDNA, Esox Biologics."""
import json
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "2026-09-16"
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
        "name": "WellFish Tech",
        "url": "https://wellfishtech.com/",
        "sector": "Aquaculture",
        "tag": "aquaculture",
        "notes": (
            "Blood-biomarker fish health platform + WellFish Predict 28-day mortality forecast from non-lethal clinical chemistry. "
            "Customers sample on farm; results ~24h; patents + Mattilsynet-aligned protocols. Commercial traction Norway/Iceland "
            "plus UK/Ireland/N+S America (Loch Duart case). Significantly oversubscribed interim financing (ann. 27 Aug 2026) from "
            "undisclosed VC/family office/private investors across NO/UK/EU — preparing Series A in 2027. Group FD Erik Tveteraas. "
            "Focus: predictive physiology beyond env/production telemetry; welfare, feed, harvest timing, treatment planning."
        ),
        "description": (
            "Blood-biomarker fish health + 28-day mortality forecast (WellFish Predict); oversubscribed interim round Aug 2026; Series A planned 2027."
        ),
        "raw": f"""# WellFish Tech – Raw Web Extract
**Source:** https://wellfishtech.com/
**Also:** https://wellfishtech.com/the-science/
**Also:** https://thefishsite.com/articles/wellfish-tech-draws-new-backing-as-customer-base-grows
**Extracted:** {DATE}

## Overview
WellFish Tech provides continuous, data-driven fish health monitoring using blood-based clinical chemistry biomarkers — analogous to human/veterinary bloodwork — rather than intermittent disease diagnosis. Customers (salmon producers) collect non-lethal blood samples under company protocols (training + on-site); lab analysis returns actionable insights within ~24 hours of sample receipt. Named product **WellFish Predict** delivers a **28-day mortality forecast** by detecting early physiological signs of disease and stress weeks before visible symptoms. IP: company patents + methodology aligned with Norwegian Food Safety Authority (Mattilsynet) non-lethal sampling rules. Customer proof: Loch Duart (Scotland) used biomarker insight to adjust feeding during a challenge and gain biomass.

## Business Model
- B2B aquaculture health analytics / lab-service + software decision support
- Recurring monitoring relationships with producers (Norway, Iceland, UK, Ireland, North & South America)
- Value prop: reduce preventable mortality, optimize nutrition/treatment timing, protect fillet quality, plan moves/harvests
- Expanding IP pipeline from mortality prediction into welfare and quality assessment biomarkers
- Preparing institutional Series A (2027) after oversubscribed interim bridge (Aug 2026)

## Funding
- **Significantly oversubscribed interim financing** announced **27 Aug 2026** (amount undisclosed)
- Investors: undisclosed across Norway, UK, EU — mix of VC, family office, private networks
- Purpose: commercial growth + product/IP pipeline; positions company for **Series A in 2027**
- Commercial signal cited: new agreements with leading producers in Norway and Iceland

## Key Technology
- Routine blood biomarker panels → nutrition uptake, flesh quality, gill health, liver/kidney/pancreas function
- **WellFish Predict**: 28-day forward mortality model from physiology (not only env/production sensors)
- Non-lethal sampling workflows compliant with Mattilsynet
- Decision use-cases: avoid downgrades, feed right feed at right time, treatment efficacy windows, move/harvest timing

## Marine Data & Ops Needs
- Longitudinal biomarker time series linked to cage/site IDs
- Co-registration with DO, temp, salinity, feeding, treatment, mortality, sea-lice and pathogen events
- Multi-site baselines by species/strain/life-stage; transfer learning across regions
- Integration APIs into farm OS / ERPs; welfare and retailer audit trails

## Contacts
- https://wellfishtech.com/
- Group Finance Director: Erik Tveteraas (press)
- Customer reference: Loch Duart, Scotland
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "WellFish Tech",
            "url": "https://wellfishtech.com/",
            "description": "Blood-biomarker clinical chemistry platform for continuous fish health monitoring and 28-day mortality forecasting (WellFish Predict) in aquaculture.",
            "sector": "Aquaculture",
            "businessModel": "B2B predictive fish-health analytics via non-lethal blood biomarkers + lab/service workflow; bridge-financed toward Series A 2027",
            "lastFundingRound": "Oversubscribed interim financing (ann. 27 Aug 2026); amount undisclosed; Series A planned 2027",
            "totalFunding": "Undisclosed interim round (Aug 2026)",
            "investors": [
                "Undisclosed VC / family office / private investors (Norway, UK, EU)"
            ],
            "employee": [
                {
                    "@type": "Person",
                    "name": "Erik Tveteraas",
                    "jobTitle": "Group Finance Director",
                }
            ],
            "knowsAbout": [
                "Fish blood biomarkers",
                "Mortality forecasting",
                "Salmon health welfare",
                "Non-lethal sampling",
                "Aquaculture clinical chemistry",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Blood biochemistry time series",
                    "Farm environmental telemetry",
                    "Mortality and treatment records",
                    "Feed and biomass data",
                ],
                "keyMeasurements": [
                    "Clinical chemistry biomarkers",
                    "28-day mortality risk",
                    "Gill/liver/kidney/pancreas function markers",
                    "DO temperature salinity context",
                ],
                "observationPlatforms": [
                    "On-farm non-lethal blood sampling",
                    "Central lab analysis",
                    "WellFish Predict model",
                ],
                "knownGaps": [
                    "Cross-site biomarker baseline standards",
                    "Fusion with eDNA/pathogen panels",
                    "Open APIs to multi-vendor farm OS",
                ],
                "interestInExternalDataServices": "Site metocean/WQ, pathogen outbreak networks, sea-lice counts, feed composition, genetics/strain metadata",
            },
        },
        "wiki_body": f"""# WellFish Tech

**Sector**: Aquaculture
**Official Site**: https://wellfishtech.com/

## Overview
**WellFish Tech** sells continuous **blood-biomarker** fish health intelligence — clinical chemistry applied routinely to farmed fish, not one-off disease workups. Flagship **WellFish Predict** turns non-lethal blood panels into a **28-day mortality forecast**, flagging physiological stress weeks before visible symptoms. Sampling protocols are trained on-farm and aligned with Norwegian **Mattilsynet** non-lethal rules; results target ~**24h** turnaround. Commercial footprint spans **Norway and Iceland** (new leading-producer agreements) plus UK/Ireland and the Americas; **Loch Duart** (Scotland) publicly cited a feeding adjustment that gained biomass from WellFish insight.

## Business Model
- **B2B health analytics + lab workflow**: producers sample; WellFish analyzes biomarkers and returns decision support
- Use cases: mortality risk, nutrition timing, treatment windows, move/harvest planning, fillet-quality protection
- **IP pipeline** expanding biomarkers from mortality into welfare and quality assessment
- Growth capital: oversubscribed **interim round (27 Aug 2026)** → **Series A planned 2027**

## Funding
- **Significantly oversubscribed interim financing** (announced **27 Aug 2026**; amount not disclosed)
- Participants: undisclosed **VC, family office, and private** investors across **Norway, UK, and EU**
- Investor thesis (per Group FD **Erik Tveteraas**): commercial value of seeing risk **28 days out** + broader physiology IP — not only env sensors

## Key Technology
- Blood biomarkers as production OS inputs (nutrition uptake, flesh quality, gill health, organ function)
- **WellFish Predict** mortality model grounded in patented physiology methods
- Non-lethal, regulator-aligned sampling vs lethal/histology-heavy workflows

## Data & Measurement Needs
- **Primary data types**: Longitudinal blood biochemistry; cage/site environmental telemetry; mortality, treatment, feed, and biomass records; welfare audit trails
- **Key measurements/parameters**: Clinical chemistry panels; 28-day mortality probability; organ/tissue function markers; contextual DO, temperature, salinity, lice/pathogen events
- **Observation platforms/programs**: On-farm non-lethal sampling networks; central lab; Predict model scoring; multi-country producer deployments
- **Known data gaps**: Harmonized cross-site biomarker baselines by strain/life-stage; tight fusion with eDNA/pathogen kits ([Nucleic Sensing Systems](nucleic-sensing-systems.md), [WildTechDNA](wildtechdna.md), [Esox Biologics](esox-biologics.md)); open APIs into heterogeneous farm OS stacks
- **Interest in external data services**: Regional outbreak networks, metocean/WQ, genetics metadata, feed formulation streams, retailer welfare score frameworks

## Cross-Sector Connections
- Complements **camera CV** health ([Aquabyte](aquabyte.md), [Tidal](tidal.md), [NeuralX](neuralx.md)) with **internal physiology** signal cameras cannot see
- Pairs with **eDNA/molecular** screens ([Nucleic Sensing Systems](nucleic-sensing-systems.md), [WildTechDNA](wildtechdna.md), [Esox Biologics](esox-biologics.md)) — host state vs pathogen presence
- Informs treatment timing for **sea-lice/welfare stacks** ([Biosort](biosort.md), [Ace Aquatec](ace-aquatec.md), [AquaNab](aquanab.md))
- Sector home: [Aquaculture](aquaculture.md)

---
**Cross-links**: [Aquaculture](aquaculture.md) · [Nucleic Sensing Systems](nucleic-sensing-systems.md) · [WildTechDNA](wildtechdna.md) · [Esox Biologics](esox-biologics.md) · [Aquabyte](aquabyte.md) · [Tidal](tidal.md) · [Biosort](biosort.md)

*Last Updated: {DATE}*
""",
    },
    {
        "name": "WildTechDNA",
        "url": "https://wildtechdna.com/",
        "sector": "Aquaculture",
        "tag": "aquaculture",
        "notes": (
            "Ultra-rapid instrument-free DNA detection; ORYA multi-pathogen on-site kit for salmon & shrimp (~15 min, handheld, no lab/molecular expertise). "
            "Isothermal amplification platform; adaptable to other species/pathogens; also conservation, wildlife enforcement, food systems. "
            "ORYA aquaculture launch covered 14 Sep 2026 (The Fish Site); Responsible Seafood Innovation Awards finalist. Co-founder Keith Liddiard. "
            "Priority notifications via website; early commercial GTM for producers/distributors."
        ),
        "description": (
            "ORYA handheld multi-pathogen DNA kit (~15 min) for salmon/shrimp; instrument-free isothermal platform; Sep 2026 aquaculture launch."
        ),
        "raw": f"""# WildTechDNA – Raw Web Extract
**Source:** https://wildtechdna.com/
**Also:** https://thefishsite.com/articles/wildtechdna-launches-15-minute-multi-pathogen-test
**Extracted:** {DATE}

## Overview
WildTechDNA builds ultra-rapid, instrument-free species/pathogen DNA detection technology. In September 2026 it launched **ORYA**, a multi-pathogen screening platform aimed first at **salmon and shrimp** producers: multiple relevant pathogens in one test, results in ~**15 minutes**, handheld kit usable without lab infrastructure or specialist molecular skills. Platform uses **isothermal DNA amplification** outside conventional labs. Broader claimed markets: aquaculture, conservation, wildlife enforcement, food systems. Finalist — Responsible Seafood Innovation Awards. Co-founder **Keith Liddiard** emphasizes combination of speed + breadth + simplicity so farms can act while there is still time, including when disease is detected at nearby facilities.

## Business Model
- Hardware/consumable kits + pathogen panel configurations sold to producers and distributors
- Species-specific applications (salmon, shrimp first) with rapid retargeting of pathogen sets
- Priority notification / early-access registration on website (launch-phase GTM)
- Cross-vertical DNA detection platform (not aquaculture-only)

## Funding
- No disclosed equity round in the 14 Sep 2026 launch coverage
- Signal: product commercialization + innovation-award shortlist rather than announced VC round

## Key Technology
- Instrument-free isothermal DNA amplification
- Multi-pathogen single-test panels
- ~15-minute time-to-result on site
- Adaptable beyond salmon/shrimp to other aquaculture species and pathogen targets

## Marine Data & Ops Needs
- Ground-truth correlation of ORYA calls vs lab PCR/qPCR and farm mortality
- Regional pathogen prevalence maps; neighboring-farm outbreak feeds
- Integration of rapid molecular positives into treatment/biosecurity SOPs and farm OS
- Chain-of-custody and false-positive/negative performance by water matrix (salinity, inhibitors)

## Contacts
- https://wildtechdna.com/
- Co-founder: Keith Liddiard
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "WildTechDNA",
            "url": "https://wildtechdna.com/",
            "description": "Ultra-rapid instrument-free DNA detection; ORYA multi-pathogen ~15-minute on-site screening for salmon and shrimp aquaculture.",
            "sector": "Aquaculture",
            "businessModel": "On-site multi-pathogen DNA kits/consumables for producers and distributors; platform expandable across species and non-aqua verticals",
            "lastFundingRound": "No disclosed equity round in Sep 2026 launch coverage",
            "founder": [
                {"@type": "Person", "name": "Keith Liddiard", "jobTitle": "Co-founder"}
            ],
            "knowsAbout": [
                "Isothermal DNA amplification",
                "Multi-pathogen screening",
                "Salmon and shrimp disease diagnostics",
                "Field molecular testing",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "On-site pathogen DNA assay results",
                    "Lab PCR confirmation",
                    "Farm biosecurity and mortality logs",
                    "Regional outbreak intelligence",
                ],
                "keyMeasurements": [
                    "Multi-pathogen presence/absence",
                    "Time-to-result",
                    "Sensitivity/specificity vs lab gold standards",
                    "Matrix inhibition flags",
                ],
                "observationPlatforms": [
                    "ORYA handheld kits",
                    "Producer/distributor field deployments",
                ],
                "knownGaps": [
                    "Published panel lists and LODs by species",
                    "Networked outbreak sharing standards",
                    "API hooks into farm OS and regulator reporting",
                ],
                "interestInExternalDataServices": "Neighboring-farm disease alerts, water-quality context, eDNA time series, veterinary lab networks",
            },
        },
        "wiki_body": f"""# WildTechDNA

**Sector**: Aquaculture
**Official Site**: https://wildtechdna.com/

## Overview
**WildTechDNA** commercializes **instrument-free, ultra-rapid DNA detection**. **ORYA** (aquaculture launch covered **14 Sep 2026**) is a **multi-pathogen** on-site kit for **salmon and shrimp**: several targets per test, ~**15 minutes**, no lab bench or molecular specialist required. Built on **isothermal amplification** for field use. Co-founder **Keith Liddiard** frames the product as speed **plus** breadth **plus** simplicity — enabling action when infection is still containable, including responses to nearby-farm detections. Shortlisted finalist: **Responsible Seafood Innovation Awards**. Same core platform marketed to conservation, wildlife enforcement, and food systems.

## Business Model
- Sell configurable **kits/consumables** and species pathogen panels to farms and distributors
- Launch GTM: website priority notifications / early access
- Platform strategy: retarget panels quickly beyond first salmon/shrimp SKUs
- Dual-use DNA detection across regulated non-aqua markets

## Funding
- **No public equity amount** in the Sep 2026 product launch coverage
- Commercialization and awards shortlist are the primary near-term signals; watch for seed/Series A tied to aqua panel rollout

## Key Technology
- Instrument-free isothermal DNA amplification
- Multiplex pathogen screening in one handheld workflow
- Field-operable by non-specialists; lab-free time-to-answer ~15 min

## Data & Measurement Needs
- **Primary data types**: On-site multi-pathogen DNA results; confirmatory lab PCR/qPCR; mortality and treatment logs; regional outbreak feeds
- **Key measurements/parameters**: Pathogen presence/absence (panel-specific); assay LOD/LOQ; matrix inhibition; time-to-result; concordance with gold-standard labs
- **Observation platforms/programs**: ORYA kits at farm/hatchery; distributor networks; award/demo deployments
- **Known data gaps**: Public panel compositions and performance dossiers by species/water type; standardized electronic sharing of positives across neighboring sites; integration with continuous eDNA ([Nucleic Sensing Systems](nucleic-sensing-systems.md)) and host physiology ([WellFish Tech](wellfish-tech.md))
- **Interest in external data services**: Veterinary lab networks, HABs/hypoxia context ([BiOceanOr](bioceanor.md), [ORCA](orca.md)), farm OS APIs, wildlife/customs DNA databases for dual-use panels

## Cross-Sector Connections
- **Point-of-care molecular** layer vs continuous autonomous eDNA ([Nucleic Sensing Systems](nucleic-sensing-systems.md)) and full metagenomes ([Esox Biologics](esox-biologics.md))
- Complements **host biomarker prediction** ([WellFish Tech](wellfish-tech.md)) — pathogen ID vs fish physiological state
- Informs intervention stacks ([Biosort](biosort.md), [Ace Aquatec](ace-aquatec.md), [AquaNab](aquanab.md))
- Sector: [Aquaculture](aquaculture.md)

---
**Cross-links**: [Aquaculture](aquaculture.md) · [Nucleic Sensing Systems](nucleic-sensing-systems.md) · [Esox Biologics](esox-biologics.md) · [WellFish Tech](wellfish-tech.md) · [BiOceanOr](bioceanor.md)

*Last Updated: {DATE}*
""",
    },
    {
        "name": "Esox Biologics",
        "url": "https://esoxbiologics.com/",
        "sector": "Aquaculture",
        "tag": "aquaculture",
        "notes": (
            "London metagenomics microbiome platform 'Detect' — sequences all DNA in water/swab samples to ID pathogens + beneficial microbes without prior assumptions. "
            "Stage modules: green/eyed eggs, biofilters, RAS, production, oysters. World's first full genome of sabellid worm Terebrasabella heterouncinata (ann. ~2 Sep 2026) "
            "enabling water-sample detection of worm/larvae/eggs before shell infestation on abalone farms (MD Matthew Pope). Also UK shellfish larval survival / antibiotic-alternative work (2026). "
            "Low-abundance detection claims qPCR-like sensitivity with full community view."
        ),
        "description": (
            "Metagenomic Detect platform for aquaculture microbiomes; first sabellid worm genome for water-based abalone infestation early warning (2026)."
        ),
        "raw": f"""# Esox Biologics – Raw Web Extract
**Source:** https://esoxbiologics.com/
**Also:** https://esoxbiologics.com/technology/
**Also:** https://esoxbiologics.com/news/
**Also:** https://thefishsite.com/articles/esox-biologics-sequences-sabellid-worm-genome-to-aid-abalone-farms
**Extracted:** {DATE}

## Overview
Esox Biologics (London) offers **Detect**, a metagenomics platform that sequences essentially all DNA in a farm sample to profile pathogens and beneficial microbes without targeted primers/assumptions. Positioning: one water/swab sample → whole livestock population microbial insight (vs one-fish traditional diagnostics). Solution verticals on site: green & eyed eggs (water + egg swabs), biofilters (water + biofilm), RAS water, production water + swabs, oysters. Technology pages stress bases-level sequencing, detection of bacteria/viruses/fungi/parasites/archaea including unknowns, relative abundance, and aquaculture-relevant interpretation. **News (2 Sep 2026 featured)**: first company to sequence whole genome of sabellid worm *Terebrasabella heterouncinata*, enabling sensitive detection of worm, larvae, and eggs from water — earlier than visual shell inspection on abalone farms. MD **Matthew Pope**. Other 2026 notes: metagenomics to improve larval survival in UK shellfish amid antibiotic limits; explainers on total microbiome, microbes-of-interest watchlists, low-abundance detection.

## Business Model
- Metagenomic sequencing + interpreted reports / Detect SaaS-style insights for hatcheries and farms
- Stage-specific sampling kits/protocols (eggs → grow-out → molluscs)
- Reference database expansion (e.g., sabellid genome) as product moat
- Likely B2B recurring testing programs; no public pricing in crawl

## Funding
- No disclosed funding round in Aug/Sep 2026 product-science coverage
- Signal is scientific/product milestones (genome firsts, shellfish programs) rather than announced VC

## Key Technology
- Shotgun/metagenomic sequencing of environmental/livestock-associated samples
- Pathogen + beneficial microbe joint view; novel strain detection
- Low-abundance detection positioned at qPCR-like sensitivity with full community context
- Custom "microbes of interest" monitoring over time
- Sabellid worm whole genome → water-based early warning for abalone

## Marine Data & Ops Needs
- Sample metadata standards (site, life stage, system type, recent treatments/antibiotics)
- Time-series microbiome baselines per RAS/flow-through design
- Integration with water chemistry (TAN, NO2, NO3, DO, TOC) and mortality
- Cross-lab reproducibility; turnaround time vs intervention windows
- Genome database growth for parasites of commercial molluscs/finfish

## Contacts
- https://esoxbiologics.com/
- Managing Director: Matthew Pope
- London, UK
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Esox Biologics",
            "url": "https://esoxbiologics.com/",
            "description": "London metagenomics company; Detect platform profiles full aquaculture microbiomes from water/swabs; first sabellid worm genome for abalone early detection.",
            "foundingLocation": {"@type": "Place", "name": "London, United Kingdom"},
            "sector": "Aquaculture",
            "businessModel": "B2B metagenomic testing + interpreted Detect reports/watchlists for hatchery-to-harvest aquaculture systems",
            "lastFundingRound": "No disclosed round in Aug/Sep 2026 coverage",
            "employee": [
                {
                    "@type": "Person",
                    "name": "Matthew Pope",
                    "jobTitle": "Managing Director",
                }
            ],
            "knowsAbout": [
                "Metagenomics",
                "Aquaculture microbiome",
                "Sabellid worm detection",
                "RAS biofilter microbiology",
                "Shellfish larval health",
            ],
            "marineDataNeeds": {
                "primaryDataTypes": [
                    "Metagenomic sequence data",
                    "Water and biofilm samples",
                    "Pathogen/beneficial abundance tables",
                    "Water chemistry covariates",
                ],
                "keyMeasurements": [
                    "Community composition",
                    "Pathogen presence and relative abundance",
                    "Sabellid DNA (worm/larvae/eggs)",
                    "Biofilter function microbes",
                ],
                "observationPlatforms": [
                    "Detect sampling kits by production stage",
                    "Sequencing + bioinformatics pipeline",
                    "Microbes-of-interest watchlists",
                ],
                "knownGaps": [
                    "Published turnaround SLAs",
                    "Open benchmark datasets vs qPCR panels",
                    "On-farm edge sequencing path",
                ],
                "interestInExternalDataServices": "WQ sensor streams, antibiotic-use logs, larval survival KPIs, parasite genome consortia, farm OS APIs",
            },
        },
        "wiki_body": f"""# Esox Biologics

**Sector**: Aquaculture
**Official Site**: https://esoxbiologics.com/

## Overview
**Esox Biologics** (London) runs **Detect**, a **metagenomics** service that sequences the DNA in water and swab samples to map **pathogens and beneficial microbes** without primer assumptions. One environmental sample is framed as a window on the **whole stock's** microbial world — unlike single-animal traditional diagnostics. Stage playbooks cover green/eyed eggs, biofilters, RAS water, production systems, and oysters. In **Sep 2026** the company announced the **first whole genome** of the sabellid worm ***Terebrasabella heterouncinata***, unlocking water-based detection of worms, larvae, and eggs **before** shell boring wrecks abalone value — replacing late visual inspection. MD **Matthew Pope**. Parallel 2026 work: UK shellfish larval survival programs seeking alternatives as antibiotics wane.

## Business Model
- B2B **sampling + sequencing + interpreted microbiome reports**
- Production-stage kits and recurring monitoring contracts
- Expanding reference genomes / “microbes of interest” watchlists as switching-cost moat
- Science-led GTM via genome firsts and hatchery partnerships (funding not yet public in this coverage)

## Funding
- **No disclosed equity round** in the Aug/Sep 2026 science/product announcements
- Near-term signal = database and deployment milestones; monitor for seed/Series A as Detect scales internationally

## Key Technology
- Shotgun metagenomics across bacteria, viruses, fungi, parasites, archaea
- Relative abundance + aquaculture-relevant annotation
- Low-abundance detection marketed at **qPCR-like sensitivity** with full-community context
- Sabellid whole-genome reference for abalone early warning
- Biofilter and RAS-focused modules for land-based systems

## Data & Measurement Needs
- **Primary data types**: Metagenomic reads/assemblies; stage-tagged water/biofilm/egg swab samples; pathogen and beneficial abundance tables; paired water-chemistry and husbandry logs
- **Key measurements/parameters**: Community composition; target pathogen loads; sabellid life-stage DNA; nitrification/biofilter taxa; larval pathogen pressure
- **Observation platforms/programs**: Detect kits by lifecycle stage; central sequencing/bioinformatics; longitudinal watchlists; abalone and UK shellfish deployments
- **Known data gaps**: Public turnaround SLAs vs treatment windows; open validation vs multiplex qPCR ([WildTechDNA](wildtechdna.md)); edge/on-farm sequencing economics; standardized exchange with farm OS and regulators
- **Interest in external data services**: Continuous WQ ([Innovasea](innovasea.md), [BiOceanOr](bioceanor.md)), host physiology ([WellFish Tech](wellfish-tech.md)), autonomous eDNA hardware ([Nucleic Sensing Systems](nucleic-sensing-systems.md)), parasite genome consortia

## Cross-Sector Connections
- **Full-community lab metagenomics** vs targeted rapid kits ([WildTechDNA](wildtechdna.md)) and autonomous eDNA sensors ([Nucleic Sensing Systems](nucleic-sensing-systems.md))
- Critical for **RAS** operators ([Oceanloop](oceanloop.md), [ReelData AI](reeldata-ai.md)) where biofilter failure is existential
- Mollusc/abalone focus complements finfish CV/biomarker leaders
- Sector: [Aquaculture](aquaculture.md)

---
**Cross-links**: [Aquaculture](aquaculture.md) · [WildTechDNA](wildtechdna.md) · [Nucleic Sensing Systems](nucleic-sensing-systems.md) · [WellFish Tech](wellfish-tech.md) · [Oceanloop](oceanloop.md) · [Innovasea](innovasea.md)

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
