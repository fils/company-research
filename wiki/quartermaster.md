# Quartermaster

**Sector**: Ocean Data & AI
**Official Site**: https://www.quartermaster.us/

**Overview**
Quartermaster is an Arlington, Virginia–based maritime-technology startup building SmartMast™, a distributed maritime sensing and AI analytics network mounted on commercial vessels. Described as a "hive mind for ships" or "continuous, distributed sensing network" that fills gaps in maritime awareness vessel-by-vessel. Positioned as a fundamental upgrade over fraud-prone AIS (Automatic Identification System), which is opt-in, self-reported, and spoofable.

**Technology**
- **SmartMast™** — vessel-mounted sensor package installed on vessels >20 GT:
  - HD optical + infrared camera array (360° rotation, 31x zoom, IP68 enclosure)
  - Dual software-defined radios (AIS, ADS-B, VHF voice, radar)
  - Onboard AI processing (vessel detection, classification, tracking)
  - Low-latency satcom (<5 sec global transmission)
  - Configurable powerpack, SATCOM, computer, cabling
- **AI analytics platform** — multimodal AI for incident detection, vessel identification, activity pattern recognition
- **Real-time dashboard** — fleet and neighbor tracking, location/heading/ID data

**Business Model**
- Sale/lease of SmartMast™ hardware to vessel operators
- Subscription AI analytics platform for maritime awareness
- Government and defense contracts (maritime domain awareness)
- Training-data sales to marine-autonomy developers
- Insurance industry data products
- "Pro-mariner" model: free hardware to mariners in exchange for network participation and goodwill — creates network-effect moat

**Recent Highlights**
- **$43M Series A** (May 2026) co-led by First Round Capital and Quiet Capital
- Bill Trenchard (First Round, led Uber seed 2010) and Quiet Capital participating
- 600+ ships equipped with SmartMast across 25+ countries
- 10 million+ square miles of ocean covered
- 400K+ vessels identified without AIS
- 20+ mariner rescues at sea (goodwill + publicity)
- Founder/CEO Neil Sobin — building maritime hardware at scale

### Data & Measurement Needs
- Primary data types: Vessel tracking data (location, heading, speed, ID); HD video and IR imagery from vessel-mounted cameras (24/7); AIS, ADS-B, VHF voice, and radar signal capture; onboard AI-processed vessel classification and pattern-of-life data; real-time satcom telemetry streams; geolocation and time-stamped records for forensic/legal use; crowdsourced maritime domain awareness feeds; training datasets for marine autonomy AI; cross-vessel network data; multi-modal fusion (video + RF + radar + AIS)
- Key measurements/parameters: Vessel position, heading, speed, course over ground; vessel classification (cargo, tanker, fishing, military, leisure); RF emissions (AIS, ADS-B, VHF voice); radar signature and bearing; visual/IR imagery (360°, 31x zoom); neighbor-vessel relative position and intent; anomaly/incident flags
- Observation platforms/programs: Vessel-mounted SmartMast sensor packages; global satcom network (sub-5s global transmission); onboard edge AI processing; centralized analytics platform (web dashboard)
- Known data gaps: Independent verification of vessel identity (AIS is opt-in, spoofable); high-resolution real-time maritime activity in 25+ countries; training data for marine computer vision
- Interest in external data services: High — network grows with each vessel joined; data is core product; external data services that augment maritime intelligence (weather, oceanographic, regulatory) are complementary

**Last Updated**: 2026-06-01

---
**Cross-links**: [Ocean Data & AI](ocean-data-ai.md), [Maritime Operations & Analytics](maritime-operations-analytics.md)
