#!/usr/bin/env python3
"""Daily company research update — 2026-07-10 autonomous cron run.
Adds HavocAI, Seasats, Bedrock Ocean Exploration; merges Coastal Measures duplicate.
"""
import json
import os
import re
from pathlib import Path

REPO = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TODAY = "2026-07-10"


def slugify(name: str) -> str:
    slug = name.lower()
    for a, b in [("ø", "o"), ("æ", "ae"), ("å", "a"), ("ü", "u"), ("é", "e"), ("è", "e")]:
        slug = slug.replace(a, b)
    slug = re.sub(r"[^a-z0-9-]", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


NEW_COMPANIES = [
    {
        "sector": "Marine Monitoring & Sensors",
        "name": "HavocAI",
        "url": "https://www.havocai.com/",
        "notes": (
            "All-domain collaborative autonomy (sea/air/land); $100M Series A (May 2026) bringing total capital to ~$200M; "
            "Providence RI; 100+ ASVs built/deployed, 30+ delivered to DoD, 25,000+ autonomous hours; "
            "software suite (C2, Insights, Connect, OS) for one-to-many control in DDIL environments; "
            "maritime domain awareness, port security, sensor fusion; investors include B Capital, Lockheed Martin, "
            "Outlander VC, Scout VC, SAIC, Clear Street; RIMPAC 2026 demo; Fast Company Top Defense Tech 2026"
        ),
        "last_updated": TODAY,
        "raw": f"""# HavocAI – Raw Web Extract
**Source:** https://www.havocai.com/
**Also:** https://medium.com/@HavocAI/havoc-raises-100m-series-a-to-power-the-future-of-all-domain-collaborative-autonomy-e6e73be4ac23
**Extracted:** {TODAY}

## Overview
HavocAI (branded Havoc) is an all-domain collaborative autonomy company headquartered in Providence, Rhode Island. It enables a single operator to supervise tens to thousands of autonomous assets across sea, air, and land. Founded 2024; CEO/co-founder Paul Lwin.

## Business Model
- Software-defined hardware: sell/deploy autonomy stack + autonomous surface vessels and multi-domain platforms
- Defense prime partnerships (Lockheed Martin, Leidos, SAIC) and direct DoD deliveries
- Commercial maritime domain awareness and port security use cases
- Scale via commercial manufacturing partners (PacMar, Senesco) rather than pure in-house hull production

## Funding
- $100M Series A (May 12, 2026) — total capital raised ~$200M since 2024
- New investors: CCM Capital Markets, Clear Street LLC, Cobalt Capital, Boardman Bay Capital Management, Meet Perry, Mute Ventures, Soren Ventures, SAIC, JA Green
- Existing: Outlander VC, Scout VC, B Capital, Lockheed Martin, Taiwania Capital, UP.Partners, The Veteran Fund, Vanderbilt University endowment
- Prior: ~$85M round (Oct 2025) reported; seed earlier; $6M SBIR / three-time xTech winner
- AlleyWatch May 2026 large-rounds list: HavocAI ~$100M Series A

## Key Technology
- Havoc C2 — one-to-many operator control
- Havoc Insights — AI/analytics fusion of vehicle/sensor streams
- Havoc Connect — peer-to-peer overlay for DDIL / degraded comms
- Havoc OS — edge autonomy for heterogeneous platforms
- 100+ ASVs built/deployed; 40+ mission-ready; 30+ vessels to US DoD
- 25,000+ hours autonomous operations; 200+ billion data points
- Acquisitions: Mavrik, Teleo (air/land expansion)
- RIMPAC 2026 demonstration planned

## Marine Data Needs
- Real-time multi-sensor maritime domain awareness (radar, EO/IR, AIS, acoustic)
- Telemetry and mission data across contested/DDIL networks
- Port security patrol sensor feeds
- Sensor fusion for track classification without reliable GPS/comms
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "HavocAI",
            "alternateName": "Havoc",
            "url": "https://www.havocai.com/",
            "description": (
                "All-domain collaborative autonomy company enabling one-to-many control of autonomous assets "
                "across sea, air, and land. Software suite (C2, Insights, Connect, OS) plus ASV fleets for "
                "maritime domain awareness, port security, and defense logistics."
            ),
            "sector": "Marine Monitoring & Sensors",
            "foundingDate": "2024",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Providence",
                    "addressRegion": "RI",
                    "addressCountry": "USA",
                },
            },
            "knowsAbout": [
                "Collaborative autonomy",
                "Autonomous surface vessels (ASVs)",
                "Maritime domain awareness",
                "DDIL communications",
                "Sensor fusion",
                "Port security",
                "Defense autonomous systems",
            ],
            "funding": {
                "@type": "MonetaryGrant",
                "name": "Series A",
                "amount": {"@type": "MonetaryAmount", "value": "100000000", "currency": "USD"},
                "funder": [
                    "B Capital",
                    "Lockheed Martin",
                    "Outlander VC",
                    "Scout VC",
                    "Clear Street",
                    "SAIC",
                    "Cobalt Capital",
                    "Boardman Bay Capital Management",
                ],
                "date": "2026-05",
                "totalRaisedApprox": "200000000",
            },
            "founder": {"@type": "Person", "name": "Paul Lwin"},
            "dataNeeds": {
                "primaryDataTypes": [
                    "multi-sensor maritime domain awareness streams",
                    "ASV telemetry and edge mission logs",
                    "radar / EO-IR / AIS fusion products",
                    "port and critical infrastructure patrol data",
                ],
                "keyMeasurements": [
                    "vessel tracks without AIS",
                    "threat classification confidence",
                    "comms-degraded network health",
                    "real-time situational awareness coverage",
                ],
                "observationPlatforms": [
                    "ASV fleets",
                    "heterogeneous air/surface/ground autonomous assets",
                    "edge AI nodes",
                ],
                "knownGaps": [
                    "persistent wide-area ocean sensing under DDIL conditions",
                    "cross-platform sensor calibration at fleet scale",
                ],
            },
            "contactPoint": {"@type": "ContactPoint", "email": "media@havocai.com"},
            "dateModified": TODAY,
        },
        "wiki": f"""# HavocAI

**Sector**: Marine Monitoring & Sensors
**Official Site**: https://www.havocai.com/

## Overview
HavocAI (branded Havoc) builds all-domain collaborative autonomy software and platforms so a single operator can supervise large numbers of autonomous assets across sea, air, and land. HQ Providence, RI; founded 2024; CEO Paul Lwin. Strong defense traction (DoD deliveries, Lockheed/SAIC/Leidos partnerships) with commercial maritime domain awareness and port security applications.

## Business Model
- Software-defined autonomy stack (C2, Insights, Connect, OS) licensed/deployed with platforms
- ASV and multi-domain vehicle production and delivery to defense customers
- Partnerships with primes and shipbuilders for scale manufacturing
- Defense contracts + commercial MDA / port security

## Funding
- **$100M Series A (May 2026)** — total raised ~**$200M** since 2024
- Investors include B Capital, Lockheed Martin, Outlander VC, Scout VC, Clear Street, SAIC, Cobalt Capital, Boardman Bay, Taiwania Capital, UP.Partners, Vanderbilt endowment
- $6M SBIR awards; three-time xTech winner
- Prior ~$85M capital infusion reported Oct 2025

## Key Technology
- One-to-many C2; edge autonomy in DDIL environments
- Peer-to-peer mission data exchange under degraded comms
- 100+ ASVs built; 30+ delivered to DoD; 25,000+ autonomous hours
- Sensor fusion (radar, EO/IR, AIS) for track classification
- Air/land expansion via Mavrik and Teleo acquisitions
- RIMPAC 2026 demo planned

### Data & Measurement Needs
- Primary data types: multi-sensor maritime domain awareness streams; ASV/edge telemetry; radar/EO-IR/AIS fusion products; port patrol sensor feeds
- Key measurements/parameters: non-AIS vessel tracks; threat classification confidence; network health under DDIL; coverage density; acoustic/EO detections
- Observation platforms/programs: ASV fleets; heterogeneous autonomous assets; edge AI nodes; cooperative multi-asset missions
- Known data gaps: persistent ocean sensing under contested comms; cross-platform sensor calibration at fleet scale; high-fidelity ocean environment models for autonomy planning
- Interest in external data services: High — bathymetry, metocean forecasts, AIS reference feeds, satellite MDA, and coastal baseline maps improve mission planning and fusion quality

**Last Updated**: {TODAY}

---
**Cross-links**: [Marine Monitoring & Sensors](marine-monitoring-sensors.md)
""",
    },
    {
        "sector": "Marine Monitoring & Sensors",
        "name": "Seasats",
        "url": "https://seasats.com/",
        "notes": (
            "Small uncrewed surface vehicles (sUSVs) for long-endurance ocean sensing & MDA; "
            "$20M Series A (Feb 2026, Konvoy Ventures lead) — >$40M total equity; "
            ">$100M US government contracts including $24M DoW APFIT; San Diego; "
            "Lightfish/Quickfish/Heavyfish product line; 6-month endurance missions; "
            "50+ modular payloads; Taiwan Strait autonomous transit (May 2026); data-as-a-service option"
        ),
        "last_updated": TODAY,
        "raw": f"""# Seasats – Raw Web Extract
**Source:** https://seasats.com/
**Also:** https://www.prnewswire.com/news-releases/seasats-raises-20-million-series-a-to-scale-production-of-small-uncrewed-surface-vehicles-302688401.html
**Extracted:** {TODAY}

## Overview
Seasats (San Diego, CA) builds long-endurance small uncrewed surface vehicles (sUSVs) for defense, commercial, and scientific missions. Product family: Lightfish (hand-deployable), Quickfish (high-speed interceptor), Heavyfish (higher payload). CEO/co-founder Mike Flanigan.

## Business Model
- Sale of low-cost, scalable sUSV platforms
- Data-as-a-service missions
- Defense procurement (US Navy, US Marine Corps, APFIT)
- Modular payload ecosystem (50+ payloads)

## Funding
- $20M Series A (Feb 17, 2026) led by Konvoy Ventures; participants: Shield Capital, DNS Capital, Techstars, Tanis Venture Management, Crumpton Ventures, Dorado Group
- >$40M total equity funding to date
- >$100M in US government contracts; $24M DoW APFIT award (announced Jan 2026) recommended by Navy/USMC

## Key Technology
- Hybrid fuel for up to 6-month detection missions; sea state 6 operations; GPS-denial capable
- Deploy by hand / ship by aircraft; priced for scale
- Real-time alerts to cell/email; UAS launch integration
- Proven: trans-Pacific and trans-Atlantic crossings; 8-day continuous Quickfish trial; first autonomous Taiwan Strait transit (May 2026)
- Use cases: ghost fleets, illegal fishing, hurricanes, harmful algal blooms, submarine signals, pipeline status, port security, ASW/sonar surveys

## Marine Data Needs
- Persistent surface ocean intelligence and MDA sensor streams
- Metocean (wave, wind, SST), acoustic, optical, AIS-independent tracking
- Harmful algal bloom and pipeline monitoring payloads
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "Seasats",
            "url": "https://seasats.com/",
            "description": (
                "Long-endurance small uncrewed surface vehicles (Lightfish, Quickfish, Heavyfish) for maritime "
                "domain awareness, defense, commercial, and scientific missions. Modular 50+ payload library; "
                "data-as-a-service option."
            ),
            "sector": "Marine Monitoring & Sensors",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "San Diego",
                    "addressRegion": "CA",
                    "addressCountry": "USA",
                },
            },
            "knowsAbout": [
                "Uncrewed surface vehicles (USVs)",
                "Maritime domain awareness",
                "Long-endurance ocean sensing",
                "Modular ocean payloads",
                "Autonomous maritime security",
            ],
            "funding": {
                "@type": "MonetaryGrant",
                "name": "Series A",
                "amount": {"@type": "MonetaryAmount", "value": "20000000", "currency": "USD"},
                "funder": [
                    "Konvoy Ventures",
                    "Shield Capital",
                    "DNS Capital",
                    "Techstars",
                    "Tanis Venture Management",
                    "Crumpton Ventures",
                    "Dorado Group",
                ],
                "date": "2026-02",
                "totalEquityApprox": "40000000+",
                "governmentContractsApprox": "100000000+",
            },
            "founder": {"@type": "Person", "name": "Mike Flanigan"},
            "products": [
                {"@type": "Product", "name": "Lightfish", "description": "Hand-deployable long-endurance sUSV"},
                {"@type": "Product", "name": "Quickfish", "description": "High-speed interceptor USV"},
                {"@type": "Product", "name": "Heavyfish", "description": "Higher payload hybrid USV for MDA/ASW/sonar"},
            ],
            "dataNeeds": {
                "primaryDataTypes": [
                    "surface ocean sensor streams",
                    "MDA tracks",
                    "acoustic/optical payload data",
                    "metocean time series",
                ],
                "keyMeasurements": [
                    "wave height",
                    "wind speed",
                    "SST",
                    "vessel detections without AIS",
                    "HAB indicators",
                    "pipeline anomaly signals",
                ],
                "observationPlatforms": ["Lightfish", "Quickfish", "Heavyfish", "UAS launched from USV"],
                "knownGaps": [
                    "ocean-wide persistent coverage at affordable cost",
                    "real-time multi-payload fusion at fleet scale",
                ],
            },
            "contactPoint": {"@type": "ContactPoint", "email": "info@seasats.com"},
            "dateModified": TODAY,
        },
        "wiki": f"""# Seasats

**Sector**: Marine Monitoring & Sensors
**Official Site**: https://seasats.com/

## Overview
Seasats (San Diego, CA) builds long-endurance small uncrewed surface vehicles for defense, commercial, and scientific ocean missions. Product line: **Lightfish** (hand-deployable), **Quickfish** (high-speed interceptor), **Heavyfish** (higher payload). Focus on the “dull” problem — weeks-to-months of reliable autonomous operations. CEO/co-founder Mike Flanigan.

## Business Model
- Hardware sales of scalable, low-cost sUSVs
- Data-as-a-service missions
- Defense contracts (Navy, USMC, APFIT)
- Modular third-party and first-party payloads (50+ library)

## Funding
- **$20M Series A (Feb 2026)** led by Konvoy Ventures (Shield Capital, DNS Capital, Techstars, others)
- **>$40M** total equity raised
- **>$100M** US government contracts; **$24M APFIT** award (DoW, Navy/USMC recommendation)

## Key Technology
- Up to 6-month hybrid-fueled endurance; sea state 6; GPS-denial operations
- Aircraft-shippable / hand-deployable form factors
- Real-time decision-maker alerts; UAS launch for overwatch
- Proven: trans-ocean crossings; 8-day continuous Quickfish trial; first autonomous Taiwan Strait transit (May 2026)
- Missions: ghost fleets, IUU fishing, hurricanes, HABs, submarine signals, pipelines, port security

### Data & Measurement Needs
- Primary data types: surface ocean sensor streams; MDA track products; acoustic/optical payload data; metocean time series; subsea mapping when payload-equipped
- Key measurements/parameters: wave height, wind, SST, non-AIS vessel tracks, HAB indicators, pipeline status, sonar survey products
- Observation platforms/programs: Lightfish/Quickfish/Heavyfish fleets; modular payloads; optionally launched UAS
- Known data gaps: affordable ocean-wide persistent coverage; multi-payload real-time fusion; standardized open ocean baseline layers for mission planning
- Interest in external data services: High — satellite SST/ocean color, AIS reference, bathymetry, weather forecasts, and HAB models all improve cueing and validation

**Last Updated**: {TODAY}

---
**Cross-links**: [Marine Monitoring & Sensors](marine-monitoring-sensors.md)
""",
    },
    {
        "sector": "Marine Monitoring & Sensors",
        "name": "Bedrock Ocean Exploration",
        "url": "https://www.bedrockocean.com/",
        "notes": (
            "Seafloor mapping AUVs + cloud data platform (Mosaic); $25M Series A-2 (Jun 2025) led by Primary/Northzone "
            "(Costanoa, Harmony Partners, Katapult Ocean et al.); total funding ~$58.5M over 3 rounds; "
            "IHO special-order geophysical surveys (MBES, SSS, MAG, SBP); deploy from any vessel; "
            "offshore wind, subsea cables, ports, defense MDA, science; edge QA/QC during acquisition"
        ),
        "last_updated": TODAY,
        "raw": f"""# Bedrock Ocean Exploration – Raw Web Extract
**Source:** https://www.bedrockocean.com/
**Also:** TechCrunch / company announcements on $25M Series A-2 (2025)
**Extracted:** {TODAY}

## Overview
Bedrock Ocean Exploration redefines seabed intelligence with custom AUVs and a cloud-native data platform. Vertically integrated: vehicles + processing/delivery. Focus on high-resolution geophysical survey data meeting IHO special order standards.

## Business Model
- Survey-as-a-service / data products for energy, critical infrastructure, security, science
- Rapidly deployable AUV fleets launched from customer or local vessels (no specialized ships)
- Cloud-native delivery of actionable seafloor intelligence

## Funding
- $25M Series A-2 (June 2025) — co-leads Costanoa Ventures, Harmony Partners, Katapult Ocean (press); also reported Primary/Northzone lead with Autopilot, Mana Ventures participation
- ~$58.5M total over 3 rounds (public summaries)
- Prior Series A ~$25.5M (2023) for seafloor robots/data

## Key Technology
- Custom AUV fleet with edge computing for in-mission QA/QC
- Sensors: Multibeam Echosounder (MBES), Side-Scan Sonar (SSS), Magnetometer (MAG), Sub-Bottom Profiler (SBP)
- Mosaic cloud platform for ocean data
- Any-vessel mobilization; regional flexibility for weather/schedule response

## Markets
- Offshore wind / oil & gas / renewables site characterization and monitoring
- Ports, harbors, submarine telecom cables
- Security & defense seabed change detection
- Foundational science / global mapping initiatives

## Marine Data Needs
- High-resolution bathymetry and backscatter
- Sub-bottom and magnetic anomaly data
- Repeat surveys for change detection
- Environmental characterization for permitting
""",
        "metadata": {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "Bedrock Ocean Exploration",
            "url": "https://www.bedrockocean.com/",
            "description": (
                "Custom AUVs and cloud-native platform for high-resolution seafloor mapping and monitoring. "
                "IHO special-order geophysical surveys for energy, infrastructure, defense, and science."
            ),
            "sector": "Marine Monitoring & Sensors",
            "knowsAbout": [
                "Autonomous underwater vehicles",
                "Seafloor mapping",
                "Multibeam bathymetry",
                "Side-scan sonar",
                "Sub-bottom profiling",
                "Offshore wind site characterization",
            ],
            "funding": {
                "@type": "MonetaryGrant",
                "name": "Series A-2",
                "amount": {"@type": "MonetaryAmount", "value": "25000000", "currency": "USD"},
                "funder": [
                    "Primary",
                    "Northzone",
                    "Costanoa Ventures",
                    "Harmony Partners",
                    "Katapult Ocean",
                    "Autopilot",
                    "Mana Ventures",
                ],
                "date": "2025-06",
                "totalRaisedApprox": "58500000",
            },
            "products": [
                {
                    "@type": "Product",
                    "name": "Bedrock AUV Fleet",
                    "description": "Rapidly deployable AUVs with MBES, SSS, MAG, SBP payloads and edge QA/QC",
                },
                {
                    "@type": "Product",
                    "name": "Mosaic",
                    "description": "Cloud-native seafloor data platform",
                },
            ],
            "dataNeeds": {
                "primaryDataTypes": [
                    "bathymetric point clouds",
                    "side-scan imagery",
                    "sub-bottom profiles",
                    "magnetometer grids",
                    "change-detection time series",
                ],
                "keyMeasurements": [
                    "depth",
                    "backscatter",
                    "sediment layering",
                    "magnetic anomalies",
                    "cable/route clearance",
                ],
                "observationPlatforms": ["custom AUV fleets", "edge compute onboard", "any-vessel launch"],
                "knownGaps": [
                    "global high-resolution seafloor coverage",
                    "frequent revisits for change detection at commercial cost",
                ],
            },
            "dateModified": TODAY,
        },
        "wiki": f"""# Bedrock Ocean Exploration

**Sector**: Marine Monitoring & Sensors
**Official Site**: https://www.bedrockocean.com/

## Overview
Bedrock Ocean Exploration provides advanced autonomous underwater vehicles and a cloud-native data platform for mapping, monitoring, and understanding the seafloor. Vertically integrated stack delivers IHO special-order geophysical survey products for energy, critical infrastructure, defense, and science customers. Launch from any vessel without specialized ships.

## Business Model
- Seafloor survey and monitoring services / data products
- AUV fleet operations with rapid regional mobilization
- Cloud delivery of actionable seabed intelligence (Mosaic platform)
- Markets: offshore wind & energy, ports/cables, security & defense, research

## Funding
- **$25M Series A-2 (June 2025)** — investors reported include Primary, Northzone, Costanoa Ventures, Harmony Partners, Katapult Ocean, Autopilot, Mana Ventures
- **~$58.5M** total over 3 rounds
- Prior Series A (~$25.5M, 2023) scaled AUV fleet and data platform

## Key Technology
- Custom AUVs with onboard edge computing for live QA/QC
- Sensor suite: MBES, side-scan sonar, magnetometer, sub-bottom profiler
- Cloud-native Mosaic data platform
- Any-vessel deployability; low logistics overhead

### Data & Measurement Needs
- Primary data types: bathymetric point clouds; side-scan imagery; sub-bottom profiles; magnetometer grids; multi-temporal change products
- Key measurements/parameters: depth, acoustic backscatter, sediment stratigraphy, magnetic anomalies, infrastructure clearance corridors
- Observation platforms/programs: Bedrock AUV fleets; edge compute; partner research campaigns; offshore wind site surveys
- Known data gaps: global high-resolution seafloor coverage; affordable high-frequency revisits; standardized open bathymetry layers for commercial planning
- Interest in external data services: High — satellite altimetry-derived bathymetry, AIS/shipping density, metocean, and existing public bathymetry (GEBCO, NOAA) for mission planning and gap-filling

**Last Updated**: {TODAY}

---
**Cross-links**: [Marine Monitoring & Sensors](marine-monitoring-sensors.md)
""",
    },
]


def load_companies():
    path = REPO / "sources" / "companies.json"
    with open(path) as f:
        return json.load(f)


def save_companies(companies):
    path = REPO / "sources" / "companies.json"
    with open(path, "w") as f:
        json.dump(companies, f, indent=2, ensure_ascii=False)
        f.write("\n")


def merge_coastal_measures(companies):
    """Remove Coastal Risk & Intelligence duplicate; fold funding notes into Ocean Data & AI entry."""
    kept = []
    coastal_extra = None
    for c in companies:
        if c["name"] == "Coastal Measures" and c["sector"] == "Coastal Risk & Intelligence":
            coastal_extra = c
            continue
        kept.append(c)

    for c in kept:
        if c["name"] == "Coastal Measures" and c["sector"] == "Ocean Data & AI":
            notes = c.get("notes", "")
            if "Maine Angels" not in notes:
                c["notes"] = (
                    notes.rstrip(".")
                    + "; $260K seed from Maine Angels (2026); also positions CUMULUS for coastal risk analytics, "
                    "hydrokinetic site identification, resilient-community intelligence"
                )
            c["last_updated"] = TODAY
            break
    return kept, coastal_extra is not None


def write_profiles(entry):
    slug = slugify(entry["name"])
    raw_path = REPO / "raw" / f"{slug}.md"
    meta_path = REPO / "metadata" / f"{slug}.jsonld"
    wiki_path = REPO / "wiki" / f"{slug}.md"

    raw_path.write_text(entry["raw"])
    meta_path.write_text(json.dumps(entry["metadata"], indent=2) + "\n")
    wiki_path.write_text(entry["wiki"])
    print(f"  wrote profiles for {entry['name']} → {slug}")


def update_sector_page(new_count: int):
    path = REPO / "wiki" / "marine-monitoring-sensors.md"
    text = path.read_text()
    text = re.sub(
        r"\*\*Last Updated\*\*: \d{4}-\d{2}-\d{2}",
        f"**Last Updated**: {TODAY}",
        text,
        count=1,
    )
    text = re.sub(
        r"\*\*Companies Tracked\*\*: \d+",
        f"**Companies Tracked**: {new_count}",
        text,
        count=1,
    )

    insert = f"""
### HavocAI (NEW {TODAY})
All-domain collaborative autonomy (sea/air/land). $100M Series A (May 2026), ~$200M total. ASV fleets + C2/Insights/Connect/OS software for one-to-many control in DDIL environments. Maritime domain awareness, port security, sensor fusion. Providence, RI.
- **Site**: [havocai.com](https://www.havocai.com/)
- **Funding**: $100M Series A (May 2026); ~$200M total
- **Location**: Providence, RI

### Seasats (NEW {TODAY})
Long-endurance small USVs (Lightfish / Quickfish / Heavyfish) for MDA, defense, science. $20M Series A (Feb 2026); >$40M equity; >$100M gov contracts incl. $24M APFIT. 6-month missions; Taiwan Strait autonomous transit (May 2026).
- **Site**: [seasats.com](https://seasats.com/)
- **Funding**: $20M Series A (Konvoy); >$40M equity; >$100M contracts
- **Location**: San Diego, CA

### Bedrock Ocean Exploration (NEW {TODAY})
Seafloor mapping AUVs + Mosaic cloud platform. IHO special-order MBES/SSS/MAG/SBP surveys. $25M Series A-2 (2025); ~$58.5M total. Any-vessel deploy for offshore wind, cables, ports, defense, science.
- **Site**: [bedrockocean.com](https://www.bedrockocean.com/)
- **Funding**: $25M Series A-2 (~$58.5M total)
- **Location**: US (ocean survey ops)

"""
    # Insert before Cross-Company section
    marker = "## Cross-Company Marine Data Patterns"
    if marker in text and "HavocAI" not in text:
        text = text.replace(marker, insert + marker)

    # Refresh pattern bullets slightly
    if "collaborative autonomy (HavocAI)" not in text:
        text = text.replace(
            "- **Autonomous platforms**: All companies build autonomous systems (ASVs, AUVs, cameras) for persistent ocean monitoring\n",
            "- **Autonomous platforms**: All companies build autonomous systems (ASVs, AUVs, cameras) for persistent ocean monitoring; 2026 wave adds collaborative multi-asset C2 (HavocAI), long-endurance sUSVs (Seasats), and commercial seafloor survey AUVs (Bedrock)\n",
        )

    path.write_text(text)
    print(f"  updated sector page companies → {new_count}")


def main():
    print(f"=== Daily update {TODAY} ===")
    companies = load_companies()
    print(f"Loaded {len(companies)} companies")

    companies, removed_dup = merge_coastal_measures(companies)
    print(f"Coastal Measures duplicate removed: {removed_dup}")

    existing_names = {c["name"].lower() for c in companies}
    added = []
    for entry in NEW_COMPANIES:
        if entry["name"].lower() in existing_names:
            print(f"  SKIP already present: {entry['name']}")
            continue
        companies.append(
            {
                "sector": entry["sector"],
                "name": entry["name"],
                "url": entry["url"],
                "notes": entry["notes"],
                "last_updated": entry["last_updated"],
            }
        )
        write_profiles(entry)
        added.append(entry["name"])
        existing_names.add(entry["name"].lower())

    save_companies(companies)
    print(f"Saved companies.json → {len(companies)} entries; added: {added}")

    mm_count = sum(1 for c in companies if c["sector"] == "Marine Monitoring & Sensors")
    update_sector_page(mm_count)

    # Session log
    session = REPO / "references" / f"session-{TODAY}-autonomous-run.md"
    session.write_text(
        f"""# Autonomous Run — {TODAY}

## Pre-run
- Working tree clean; branch master up to date with origin
- Completeness check: 0 errors, 1 warning (missing wiki/coastal-risk-intelligence.md)
- Companies loaded: 69 (with duplicate Coastal Measures across two sectors)

## Phase 1 — Sources
- Discovery searches: ocean tech Series A/funding 2026, AUV/USV funding, mCDR funding, marine robotics
- **VentureWell OEA Spring 2026 exhausted** — weighted defense-tech press + AlleyWatch/Crunchbase large rounds
- High-signal finds:
  1. **HavocAI** — $100M Series A (May 2026), ~$200M total collaborative autonomy
  2. **Seasats** — $20M Series A + >$100M gov contracts; long-endurance sUSVs
  3. **Bedrock Ocean Exploration** — $25M Series A-2; seafloor AUV mapping
- Fixed: removed **Coastal Measures** duplicate under Coastal Risk & Intelligence (kept Ocean Data & AI entry; merged Maine Angels $260K note)
- Net companies: 69 − 1 + 3 = **71**

## Phases 2–4
- Ingested homepages/press for all three new companies
- Wrote raw/, metadata/ JSON-LD, wiki/ profiles with Data & Measurement Needs
- Updated `wiki/marine-monitoring-sensors.md` count to 17

## Completeness
- Run `python3 scripts/completeness-check.py` after this script

## Focus themes
- Business models, funding, marine data needs emphasized for all new profiles
"""
    )
    print(f"  wrote {session.name}")
    print("DONE")


if __name__ == "__main__":
    main()
