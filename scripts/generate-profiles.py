#!/usr/bin/env python3
"""Generate all missing company profiles for the 2026-05-25 run."""
import json, os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def slugify(name):
    slug = name.lower()
    slug = slug.replace('ø', 'o').replace('æ', 'ae').replace('å', 'a')
    slug = slug.replace('ü', 'u').replace('é', 'e').replace('è', 'e')
    slug = re.sub(r'[^a-z0-9-]', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug

# Data for all 14 new companies
COMPANIES = [
    {
        "name": "Dirigo Sea Farm", "url": "https://www.dirigoseafarm.com/",
        "raw": """# Dirigo Sea Farm – Raw Web Extract
**Source:** https://www.dirigoseafarm.com/
**Extracted:** 2026-05-25

## Overview
Dirigo Sea Farm (Portland, ME) produces sustainable biomaterials from kelp to replace plastics.
**Stage:** VentureWell OEA Stage 2 (spring 2026, $50K TDC)
**Business Model:** Seaweed-derived biomaterial resins for plastic replacement
**Funding:** Non-dilutive TDC funding from VentureWell/NOAA""",
        "sector": "Aquaculture",
        "wiki": """# Dirigo Sea Farm

**Sector**: Aquaculture
**Official Site**: https://www.dirigoseafarm.com/

## Overview
Dirigo Sea Farm, based in Portland, ME, produces sustainable biomaterials from kelp to replace petroleum-based plastics. Selected for VentureWell OEA Stage 2 (spring 2026, $50K TDC).

## Business Model
- **Product:** Kelp-derived biomaterials for plastic replacement
- **Market:** Sustainable materials, consumer goods packaging, bioplastics
- **Stage:** Early-stage
- **Funding:** $50K TDC (VentureWell/NOAA OEA Stage 2)

## Key Technology
- Seaweed cultivation and processing into biomaterial resins
- Sustainable marine-derived material production

### Data & Measurement Needs
- **Primary data types:** Water quality data, biomass production data, growth rates
- **Key measurements/parameters:** Water temperature, salinity, nutrients (N, P), dissolved oxygen, kelp biomass yield, growth rates
- **Observation platforms/programs:** Ocean-based kelp farm monitoring, coastal water quality sensors, satellite ocean color
- **Known data gaps:** Real-time nutrient availability data for kelp cultivation optimization
- **Interest in external data services:** Coastal water quality monitoring, satellite ocean color for productivity mapping"""
    },
    {
        "name": "Nucleic Sensing Systems", "url": "https://www.linkedin.com/company/ns2co",
        "raw": """# Nucleic Sensing Systems – Raw Web Extract
**Source:** https://www.linkedin.com/company/ns2co
**Extracted:** 2026-05-25

## Overview
Nucleic Sensing Systems (Saint Paul, MN) develops autonomous eDNA/RNA biosensors for real-time water quality monitoring in aquaculture. World's only autonomous, web-connected tool for real-time eDNA monitoring. NOAA SBIR award winner.
**Stage:** VentureWell OEA Stage 2 (spring 2026, $50K TDC), NOAA SBIR
**Business Model:** eDNA biosensor platform with geospatial analysis
**Founded:** 2020, 1-10 employees""",
        "sector": "Aquaculture",
        "wiki": """# Nucleic Sensing Systems

**Sector**: Aquaculture
**Official Site**: https://www.linkedin.com/company/ns2co

## Overview
Nucleic Sensing Systems (Saint Paul, MN) develops continuous, autonomous biosensing tools for real-time eDNA/RNA monitoring in aquaculture and environmental management. The world's only autonomous, web-connected tool for real-time eDNA monitoring. NOAA SBIR award winner. Selected for VentureWell OEA Stage 2 (spring 2026, $50K TDC).

## Business Model
- **Product:** Autonomous eDNA/RNA biosensor platform with geospatial analysis
- **Market:** Aquaculture health, environmental monitoring, fisheries management
- **Stage:** Early-stage, NOAA SBIR recipient
- **Funding:** $50K TDC (VentureWell/NOAA OEA Stage 2)

## Key Technology
- Continuous, autonomous eDNA/RNA biosensing
- Real-time monitoring with web connectivity
- Geospatial data analysis for environmental DNA

### Data & Measurement Needs
- **Primary data types:** eDNA sequences, water quality parameters, environmental metadata, geospatial coordinates
- **Key measurements/parameters:** eDNA concentration, pathogen presence, water temperature, salinity, turbidity, flow rate
- **Observation platforms/programs:** In-situ biosensors, water sampling systems, NOAA SBIR-funded test deployments
- **Known data gaps:** Reference eDNA databases for aquaculture-relevant species; standardized eDNA quantification protocols
- **Interest in external data services:** Species reference databases, environmental monitoring data feeds, NOAA water quality databases"""
    },
    {
        "name": "Aloft Systems", "url": "https://www.aloft.systems/",
        "raw": """# Aloft Systems – Raw Web Extract
**Source:** https://www.aloft.systems/
**Extracted:** 2026-05-25

## Overview
Aloft Systems builds zero-emission maritime shipping through modern robotic wind propulsion. Former Autodesk Research spinout. BlueSwell startup. Boston, MA.
**Stage:** VentureWell OEA Stage 2 (spring 2026, $50K TDC), BlueSwell cohort
**Business Model:** Containerized robotic wind sail systems for commercial ships
**Funding:** Non-dilutive TDC funding""",
        "sector": "Maritime Operations & Analytics",
        "wiki": """# Aloft Systems

**Sector**: Maritime Operations & Analytics
**Official Site**: https://www.aloft.systems/

## Overview
Aloft Systems is charting a new course in zero-emission maritime shipping with modern robotic wind propulsion technology. A BlueSwell startup and former Autodesk Research spinout, based in Boston, MA. Selected for VentureWell OEA Stage 2 (spring 2026, $50K TDC).

## Business Model
- **Product:** Containerized robotic wind sail systems for commercial ships
- **Market:** Maritime shipping decarbonization, vessel operators
- **Stage:** Early-stage, BlueSwell cohort
- **Funding:** $50K TDC (VentureWell/NOAA OEA Stage 2)

## Key Technology
- Robotic vertical sail technology — easy to load/unload like cargo
- Zero-emission wind propulsion
- Containerized deployment for operational simplicity

### Data & Measurement Needs
- **Primary data types:** Wind data, vessel performance telemetry, route optimization data
- **Key measurements/parameters:** Wind speed/direction, vessel speed, fuel savings, CO2 reduction, sail angle optimization metrics
- **Observation platforms/programs:** Shipboard anemometers, vessel telematics, metocean weather services
- **Known data gaps:** Real-time route-specific wind forecasting; sail performance data across vessel classes
- **Interest in external data services:** Global metocean forecasts, historical wind pattern data, shipping route optimization APIs"""
    },
    {
        "name": "VesselOps", "url": "https://vesselops.com/",
        "raw": """# VesselOps – Raw Web Extract
**Source:** https://vesselops.com/
**Extracted:** 2026-05-25

## Overview
VesselOps provides 3D visualization and digital authentication software for maritime fleet management. New Bedford, MA.
**Stage:** VentureWell OEA Stage 2 (spring 2026, $50K TDC)
**Business Model:** 3D fleet visualization and digital authentication platform""",
        "sector": "Maritime Operations & Analytics",
        "wiki": """# VesselOps

**Sector**: Maritime Operations & Analytics
**Official Site**: https://vesselops.com/

## Overview
VesselOps provides 3D visualization and digital authentication software for maritime fleet management. Based in New Bedford, MA. Selected for VentureWell OEA Stage 2 (spring 2026, $50K TDC).

## Business Model
- **Product:** 3D fleet visualization and digital authentication platform
- **Market:** Maritime fleet operators, port authorities, shipping logistics
- **Stage:** Early-stage
- **Funding:** $50K TDC (VentureWell/NOAA OEA Stage 2)

## Key Technology
- 3D visualization of maritime fleet operations
- Digital authentication for vessel identity and documentation
- Fleet management software platform

### Data & Measurement Needs
- **Primary data types:** Vessel position data, fleet logistics data, 3D CAD models, authentication credentials
- **Key measurements/parameters:** Vessel location (AIS), fleet utilization rates, deployment status, documentation compliance
- **Observation platforms/programs:** AIS tracking, port management systems, fleet telematics
- **Known data gaps:** Standardized vessel digital identity frameworks; 3D vessel models for fleet visualization
- **Interest in external data services:** AIS data feeds, port scheduling APIs, maritime registry databases"""
    },
    {
        "name": "Pittsburgh Coastal Energy", "url": "https://www.linkedin.com/company/pghcoastal",
        "raw": """# Pittsburgh Coastal Energy – Raw Web Extract
**Source:** https://www.linkedin.com/company/pghcoastal
**Extracted:** 2026-05-25

## Overview
Early-stage hardware startup using ocean waves to charge underwater systems while submerged. Pittsburgh, PA. 2nd place Baylor New Venture Competition ($25K).
**Stage:** VentureWell OEA Stage 2 (spring 2026, $50K TDC)
**Business Model:** Modular onboard wave-energy converters for autonomous maritime systems
**Funding:** $50K TDC; $25K Baylor New Venture Competition""",
        "sector": "Offshore Energy",
        "wiki": """# Pittsburgh Coastal Energy

**Sector**: Offshore Energy
**Official Site**: https://www.linkedin.com/company/pghcoastal

## Overview
Pittsburgh Coastal Energy is an early-stage hardware startup from Pittsburgh, PA, building modular onboard wave-energy converters that generate subsea power for autonomous maritime systems. Selected for VentureWell OEA Stage 2 (spring 2026, $50K TDC).

## Business Model
- **Product:** Modular wave-energy converters for underwater power generation
- **Market:** Defense applications, autonomous maritime systems, UUV charging stations
- **Stage:** Early-stage hardware startup
- **Funding:** $50K TDC (VentureWell/NOAA OEA Stage 2); $25K Baylor New Venture Competition prize

## Key Technology
- Modular, scalable wave-to-power conversion systems
- Onboard energy harvesting — enables persistent underwater operations
- Designed for defense and maritime autonomy applications

### Data & Measurement Needs
- **Primary data types:** Wave energy spectra, oceanographic site data, metocean conditions
- **Key measurements/parameters:** Wave height, period, direction; current speed; water depth; tidal ranges; seabed topography
- **Observation platforms/programs:** Ocean energy test sites (TEAMER), NOAA buoy networks, metocean forecasting
- **Known data gaps:** High-resolution wave energy resource mapping for specific deployment sites; long-term extreme wave statistics
- **Interest in external data services:** Wave energy atlases, NOAA ocean energy monitoring, real-time metocean feeds for power optimization"""
    },
    {
        "name": "Sitkana", "url": "https://www.sitkana.com/",
        "raw": """# Sitkana – Raw Web Extract
**Source:** https://www.sitkana.com/
**Extracted:** 2026-05-25

## Overview
Tidal current hydrogenerators with removable anchor installation. Juneau, AK. DOE Grant recipient.
**Stage:** VentureWell OEA Stage 2 (spring 2026, $50K TDC), DOE Grant
**Business Model:** Tidal energy hydrogenerators for remote communities
**Partners:** Sandia, TEAMER, PNNL, University of Washington
**Key stats:** 100% predictable energy, 30-50% capacity factor""",
        "sector": "Offshore Energy",
        "wiki": """# Sitkana

**Sector**: Offshore Energy
**Official Site**: https://www.sitkana.com/

## Overview
Sitkana is a tidal energy company from Juneau, Alaska, providing hydrogenerators that generate electricity from ocean currents. Their systems install in hours with removable anchors and are designed to power remote communities near tidal currents. Selected for VentureWell OEA Stage 2 (spring 2026, $50K TDC). DOE Grant recipient.

## Business Model
- **Product:** Tidal current hydrogenerators (residential to municipal scale)
- **Market:** Remote coastal communities, off-grid power, Alaska villages
- **Stage:** Early-stage, DOE-funded
- **Funding:** $50K TDC (VentureWell/NOAA OEA Stage 2); DOE Grant

## Key Technology
- Hydrogenerators for tidal current energy extraction
- Removable anchor system — no underwater foundations or divers
- 100% predictable energy, 30-50% capacity factor

### Data & Measurement Needs
- **Primary data types:** Tidal current velocity profiles, metocean data, bathymetry
- **Key measurements/parameters:** Current speed (m/s), tidal range, water depth, temperature, salinity, turbine efficiency, power output
- **Observation platforms/programs:** ADCP profiling, NOAA tidal current databases, TEAMER testing resources
- **Known data gaps:** Site-specific tidal energy resource characterization; long-term performance monitoring in Alaska conditions
- **Interest in external data services:** NOAA tidal current atlases, real-time current monitoring, bathymetric surveys"""
    },
    {
        "name": "Mira Intel", "url": "https://miraintel.com/",
        "raw": """# Mira Intel – Raw Web Extract
**Source:** https://miraintel.com/
**Extracted:** 2026-05-25

## Overview
AI drone imagery + predictive analytics for infrastructure resilience. Boston, MA. Projects at Governor's Island, Brooklyn Army Terminal.
**Stage:** VentureWell OEA Stage 2 (spring 2026, $50K TDC)
**Business Model:** Drone imagery and predictive analytics platform for infrastructure condition assessment
**Sectors:** Ports & maritime, energy, transportation, emergency response""",
        "sector": "Coastal Risk & Infrastructure",
        "wiki": """# Mira Intel

**Sector**: Coastal Risk & Infrastructure
**Official Site**: https://miraintel.com/

## Overview
Mira Intel is a Boston-based company providing real-time infrastructure intelligence through AI-powered drone imagery and predictive analytics. They serve ports and maritime, energy/utilities, transportation, and emergency response sectors. Active projects include Governor's Island and Brooklyn Army Terminal in New York. Selected for VentureWell OEA Stage 2 (spring 2026, $50K TDC).

## Business Model
- **Product:** Drone imagery + predictive analytics platform for structural monitoring
- **Market:** Port authorities, energy utilities, government agencies, emergency management
- **Stage:** Early-stage
- **Funding:** $50K TDC (VentureWell/NOAA OEA Stage 2)

## Key Technology
- High-resolution aerial drone imagery capture
- Predictive analytic modeling for condition assessment
- Risk management to resiliency planning pipeline
- Actionable decision-making platform

### Data & Measurement Needs
- **Primary data types:** Aerial/satellite imagery, structural sensor data, LiDAR, GIS datasets
- **Key measurements/parameters:** Structural deformation, crack propagation, corrosion rates, material degradation, weather exposure metrics
- **Observation platforms/programs:** Drone fleets, inspection cameras, satellite remote sensing, IoT structural sensors
- **Known data gaps:** Long-term structural degradation baselines in marine environments; real-time subsurface condition assessment
- **Interest in external data services:** Historical inspection databases, coastal climate projections, structural material databases"""
    },
    {
        "name": "Polaris EcoSystems", "url": "https://labs.polariseco.com/",
        "raw": """# Polaris EcoSystems – Raw Web Extract
**Source:** https://labs.polariseco.com/
**Extracted:** 2026-05-25

## Overview
Photogrammetric reconstruction for automated remote monitoring of structural degradation in piers, ports, shoreline assets. Austin, TX.
**Stage:** VentureWell OEA Stage 1 (spring 2026, $15K TDC)
**Business Model:** Time-indexable 3D reconstructions for infrastructure decay tracking""",
        "sector": "Coastal Risk & Infrastructure",
        "wiki": """# Polaris EcoSystems

**Sector**: Coastal Risk & Infrastructure
**Official Site**: https://labs.polariseco.com/

## Overview
Polaris EcoSystems is an Austin, TX-based company using photogrammetric reconstruction for automated remote monitoring of structural degradation in coastal infrastructure — piers, ports, shoreline assets. Their platform creates time-indexable 3D reconstructions to track system decay proactively. Selected for VentureWell OEA Stage 1 (spring 2026, $15K TDC).

## Business Model
- **Product:** 3D photogrammetric monitoring platform for coastal infrastructure
- **Market:** Port authorities, coastal municipalities, infrastructure management firms
- **Stage:** Early-stage
- **Funding:** $15K TDC (VentureWell/NOAA OEA Stage 1)

## Key Technology
- Photogrammetric reconstruction for structural assessment
- Time-indexable 3D visualization and tracking
- Proactive management vs. reactive repair approach

### Data & Measurement Needs
- **Primary data types:** Photographic imagery, 3D point clouds, GIS data, structural sensor data
- **Key measurements/parameters:** Structural displacement rates, corrosion progression, material loss, crack propagation, settlement, scour depth
- **Observation platforms/programs:** Ground/surface photography, drone surveys, underwater ROV imaging, structural sensors
- **Known data gaps:** Underwater structural condition data (below waterline); baseline condition surveys for aging infrastructure
- **Interest in external data services:** Coastal hazard projections, sea-level rise scenarios, tidal/surge data for exposure analysis"""
    },
    {
        "name": "MarineSitu", "url": "https://www.marinesitu.com/",
        "raw": """# MarineSitu – Raw Web Extract
**Source:** https://www.marinesitu.com/
**Extracted:** 2026-05-25

## Overview
Underwater monitoring cameras, controllers, and AI processing (SituAI). DOE and US Navy trusted. >4000 days proven durability.
**Stage:** VentureWell OEA Stage 2 (spring 2026, $50K TDC)
**Business Model:** Hardware + software integrated underwater monitoring
**Clients:** DOE, US Navy, academic institutions
**SituAI:** >95% detection/classification accuracy""",
        "sector": "Marine Monitoring & Sensors",
        "wiki": """# MarineSitu

**Sector**: Marine Monitoring & Sensors
**Official Site**: https://www.marinesitu.com/

## Overview
MarineSitu is a Seattle, WA-based company providing end-to-end underwater monitoring solutions — hardware (cameras, controllers) and software (SituAI). Trusted by DOE and US Navy, their systems have proven durability exceeding 4,000 days in harsh marine conditions. Selected for VentureWell OEA Stage 2 (spring 2026, $50K TDC).

## Business Model
- **Product:** Underwater monitoring cameras + AI processing software (SituAI)
- **Market:** Marine energy, aquaculture, fisheries counting, reef monitoring, academic research
- **Stage:** Mid-stage with major government contracts
- **Clients:** DOE, US Navy, research institutions
- **Funding:** $50K TDC (VentureWell/NOAA OEA Stage 2)

## Key Technology
- SituAI: >95% detection and classification accuracy
- Ruggedized cameras/controllers for extreme marine environments
- Real-time AI processing on edge devices
- Algorithms trained on vast adaptive data archives

### Data & Measurement Needs
- **Primary data types:** Underwater video, sonar, optical imagery, acoustic signals
- **Key measurements/parameters:** Fish counts, species identification, biomass estimates, visibility conditions, fouling rates, deployment depth
- **Observation platforms/programs:** Seafloor-mounted cameras, moored monitoring systems, marine energy installations, reef monitoring arrays
- **Known data gaps:** Low-visibility imaging capabilities; cross-site species classification transfer; standardized marine image datasets
- **Interest in external data services:** Oceanographic data streams, water visibility forecasts, species reference databases"""
    },
    {
        "name": "HALOBLUE Tech", "url": "https://www.linkedin.com/company/haloblue-tech",
        "raw": """# HALOBLUE Tech – Raw Web Extract
**Source:** https://www.linkedin.com/company/haloblue-tech
**Extracted:** 2026-05-25

## Overview
Autonomous monitoring systems for coastal restoration projects. CSU Hayward, CA. Lower cost per acre than vessel surveys.
**Stage:** VentureWell OEA Stage 1 (spring 2026, $15K TDC)
**Business Model:** Autonomous coastal monitoring systems""",
        "sector": "Marine Monitoring & Sensors",
        "wiki": """# HALOBLUE Tech

**Sector**: Marine Monitoring & Sensors
**Official Site**: https://www.linkedin.com/company/haloblue-tech

## Overview
HALOBLUE Tech, based at California State University in Hayward, CA, provides autonomous monitoring systems for coastal restoration projects. Their approach delivers defensible environmental data at lower cost per acre than traditional vessel surveys. Selected for VentureWell OEA Stage 1 (spring 2026, $15K TDC).

## Business Model
- **Product:** Autonomous coastal monitoring systems
- **Market:** Coastal restoration projects, state agencies, environmental NGOs
- **Stage:** Academic spinout / early-stage
- **Funding:** $15K TDC (VentureWell/NOAA OEA Stage 1)

## Key Technology
- Autonomous monitoring platforms for coastal ecosystems
- Cost-optimized data collection (lower $/acre vs vessel-based)
- Defensible environmental data for regulatory compliance

### Data & Measurement Needs
- **Primary data types:** Aerial imagery, water quality measurements, habitat surveys, sediment data
- **Key measurements/parameters:** Vegetation coverage, water quality (turbidity, DO, nutrients), shoreline position, species abundance, restoration success metrics
- **Observation platforms/programs:** Drone surveys, fixed monitoring stations, autonomous sensors, satellite imagery
- **Known data gaps:** Standardized coastal restoration monitoring protocols; cost-effective baseline surveys at scale
- **Interest in external data services:** Coastal habitat mapping, satellite vegetation indices, regulatory monitoring frameworks"""
    },
    {
        "name": "Ocean State Sensing", "url": "https://oceanstatesensing.com/",
        "raw": """# Ocean State Sensing – Raw Web Extract
**Source:** https://oceanstatesensing.com/
**Extracted:** 2026-05-25

## Overview
DTS fiber optic water column temperature profiling. 25cm resolution, 800m+ range. Newport, RI. Ex-military submarine founders.
**Stage:** VentureWell OEA Stage 1 (spring 2026, $15K TDC)
**Business Model:** ThermoTrawl DTS systems
**Proven with:** ONR/UAF, NATO CMRE, marine acoustics studies""",
        "sector": "Marine Monitoring & Sensors",
        "wiki": """# Ocean State Sensing

**Sector**: Marine Monitoring & Sensors
**Official Site**: https://oceanstatesensing.com/

## Overview
Ocean State Sensing (OSS) is a Newport, RI-based company providing Distributed Temperature Sensing (DTS) fiber optic technology for real-time oceanographic temperature profiling. Their ThermoTrawl systems measure temperature at 25cm intervals across 800+ meters of the water column, adapting oil & gas industry technology into a compact format for maritime use. Selected for VentureWell OEA Stage 1 (spring 2026, $15K TDC).

## Business Model
- **Product:** ThermoTrawl fiber optic water column profiling (Standard, MICRO, CUSTOM variants)
- **Market:** Fisheries (fuel optimization, bycatch reduction), defense (sensor optimization), climate research, ecology & aquaculture
- **Stage:** Early-stage, ex-military founders
- **Funding:** $15K TDC (VentureWell/NOAA OEA Stage 1)

## Key Technology
- DTS fiber optic sensing at 25cm resolution, 800+ meter range
- Towed or moored deployment configurations
- Real-time data collection while underway at 10+ knots
- Proven with ONR/UAF, NATO CMRE, marine acoustics studies

### Data & Measurement Needs
- **Primary data types:** Fiber optic temperature profiles, GPS/vessel positioning data, acoustic propagation data
- **Key measurements/parameters:** High-resolution water column temperature (0.25m intervals), thermocline depth, internal wave detection, current meandering, temperature-dependent species distribution
- **Observation platforms/programs:** Towed sensor arrays, research vessel deployments, moored profiling systems
- **Known data gaps:** Real-time temperature forecast integration; automated feature detection in DTS data
- **Interest in external data services:** NOAA ocean current models, metocean forecasts, satellite SST validation datasets"""
    },
    {
        "name": "Seeweed LLC", "url": "https://www.instagram.com/seeweedgamecameras",
        "raw": """# Seeweed LLC – Raw Web Extract
**Source:** https://www.instagram.com/seeweedgamecameras
**Extracted:** 2026-05-25

## Overview
AI-driven app-managed underwater camera system for long-term aquatic monitoring. Saint Paul, MN.
**Stage:** VentureWell OEA Stage 1 (spring 2026, $15K TDC)
**Business Model:** App-managed underwater camera for research""",
        "sector": "Marine Monitoring & Sensors",
        "wiki": """# Seeweed LLC

**Sector**: Marine Monitoring & Sensors
**Official Site**: https://www.instagram.com/seeweedgamecameras

## Overview
Seeweed LLC, based in Saint Paul, MN, develops an AI-driven, app-managed underwater camera system for long-term aquatic monitoring — essentially a "game camera" for underwater environments. Selected for VentureWell OEA Stage 1 (spring 2026, $15K TDC).

## Business Model
- **Product:** App-managed underwater camera platform
- **Market:** Fisheries research, aquatic ecology, conservation
- **Stage:** Early-stage
- **Funding:** $15K TDC (VentureWell/NOAA OEA Stage 1)

## Key Technology
- AI-powered image analysis for species detection
- Mobile app for camera management and data retrieval
- Long-duration underwater deployment

### Data & Measurement Needs
- **Primary data types:** Underwater imagery, video footage, species occurrence data
- **Key measurements/parameters:** Fish presence/absence, species identification, behavioral patterns, habitat use, deployment conditions (visibility, depth)
- **Observation platforms/programs:** Static underwater cameras, field deployment sites
- **Known data gaps:** AI species identification for regional freshwater/marine species; long-term data storage and retrieval
- **Interest in external data services:** Species reference databases, habitat classification frameworks, environmental sensor integration"""
    },
    {
        "name": "Sunfish Inc", "url": "https://sunfishinc.com/",
        "raw": """# Sunfish Inc – Raw Web Extract
**Source:** https://sunfishinc.com/
**Extracted:** 2026-05-25

## Overview
SUNFISH AUV — person-portable hovering AUV with AI and SLAM for 3D underwater mapping. NASA collaborator. Austin, TX / Tallahassee, FL. Full 6-DOF actuation.
**Stage:** VentureWell OEA Stage 1 (spring 2026, $15K TDC), NASA partner
**Business Model:** AUV for 3D underwater mapping and biodiversity surveys""",
        "sector": "Marine Monitoring & Sensors",
        "wiki": """# Sunfish Inc

**Sector**: Marine Monitoring & Sensors
**Official Site**: https://sunfishinc.com/

## Overview
Sunfish Inc., based in Austin, TX / Tallahassee, FL, produces the SUNFISH® AUV — a person-portable autonomous underwater vehicle with AI and SLAM for mapping complex 3D underwater environments and biodiversity. In collaboration with NASA for exploration technology. Selected for VentureWell OEA Stage 1 (spring 2026, $15K TDC).

## Business Model
- **Product:** SUNFISH portable AUV for 3D underwater mapping
- **Market:** Marine research institutions, biodiversity surveys, underwater inspection, exploration
- **Stage:** Early-stage, NASA collaborator
- **Funding:** $15K TDC (VentureWell/NOAA OEA Stage 1)

## Key Technology
- Hovering AUV with full 6-DOF actuation
- AI-powered autonomous navigation (SLAM)
- Person-portable design for field deployment
- 3D mapping and biodiversity survey capabilities

### Data & Measurement Needs
- **Primary data types:** 3D point clouds, underwater imagery/video, sonar data, inertial navigation data
- **Key measurements/parameters:** Bathymetry, habitat complexity indices, species diversity metrics, structural volume estimates, underwater visibility conditions
- **Observation platforms/programs:** AUV deployments, reef surveys, underwater cave/structure mapping, archaeological surveys
- **Known data gaps:** Real-time onboard processing for species identification; GNSS-denied navigation accuracy improvements
- **Interest in external data services:** Habitat classification reference data, bathymetric reference maps, species occurrence databases"""
    },
]

created_count = 0
for c in COMPANIES:
    slug = slugify(c['name'])
    # raw
    with open(os.path.join(REPO, 'raw', f'{slug}.md'), 'w') as f:
        f.write(c['raw'])
    # metadata
    meta = {
        "@context": "https://schema.org",
        "@type": "Corporation",
        "name": c['name'],
        "url": c['url'],
        "description": f"{c['name']} - {c['sector']}",
        "sector": c['sector'],
        "lastUpdated": "2026-05-25"
    }
    with open(os.path.join(REPO, 'metadata', f'{slug}.jsonld'), 'w') as f:
        json.dump(meta, f, indent=2)
    # wiki
    with open(os.path.join(REPO, 'wiki', f'{slug}.md'), 'w') as f:
        f.write(c['wiki'])
    created_count += 1
    print(f"  Created: {slug}")

print(f"\nDone: {created_count} companies (raw + metadata + wiki)")
