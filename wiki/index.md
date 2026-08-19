---
okf_version: "0.1"
---

# Company Research Knowledge Bundle

Agent-maintained knowledge graph of ocean / blue-economy companies: business models, funding, technology, and data & measurement needs.

## Knowledge Catalog (OKF)

This directory is an [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) Knowledge Bundle.

**Format rules (read first for agents):** [OKF Knowledge Bundle — Format Rules](concepts/okf-knowledge-bundle.md)

- Required: YAML frontmatter with `type` on every concept document
- Cross-links: **relative markdown only** (OKF §5.2) — works on GitHub; never `[[wikilinks]]`
- Conformance: `python3 scripts/okf-lint.py`
- Workflow contract (outside bundle): repo-root `PLAN.md`

# Bundle sections

* [Concepts](concepts/) - Format rules and meta notes
* [Update Log](log.md) - Chronological change history

# Sectors (9)

* [Aquaculture](aquaculture.md) - Sector overview for aquaculture technology and monitoring companies.
* [Bioprospecting](bioprospecting.md) - **Official Sector Sources**: - Ginkgo Bioworks: https://www.ginkgo.bio/
* [Climate Risk](climate-risk.md) - Climate risk intelligence providers in the knowledge graph specialize in translating physical climate hazards into financial and operational impacts.
* [Coastal Risk & Infrastructure](coastal-risk-infrastructure.md) - **Last Updated**: 2026-05-25 **Companies Tracked**: 3
* [Marine Monitoring & Sensors](marine-monitoring-sensors.md) - **Last Updated**: 2026-08-19 **Companies Tracked**: 28
* [Maritime Operations & Analytics](maritime-operations-analytics.md) - **Last Updated**: 2026-07-14 **Companies Tracked**: 7
* [Ocean Carbon Sequestration](ocean-carbon-sequestration.md) - Sector overview for ocean-based carbon dioxide removal companies.
* [Ocean Data & AI](ocean-data-ai.md) - Ocean Data & AI is a rapidly growing sector in the knowledge graph covering companies whose primary business is providing AI-powered ocean data intelligence platforms and services.
* [Offshore Energy](offshore-energy.md) - **Official Sector Sources**: - Ørsted: https://orsted.com/ - Gazelle Wind Power: https://gazellewindpower.com/ - Principle Power: https://www.principlepower.com/

# Companies (106)

## Aquaculture

* [Ace Aquatec](ace-aquatec.md) - Welfare-first aqua AI cameras + humane stunners — £10M Stolt Ventures round (May 2025); ~$23.4M total; Dundee, Scotland.
* [Aquabyte](aquabyte.md) - AI computer vision + biomass monitoring; high marine sensor & ocean data needs
* [AquaExchange](aquaexchange.md) - Full-stack IoT/AI platform for shrimp aquaculture — farm automation, AI analytics, marketplace, embedded finance, insurance.
* [Aquaticode](aquaticode.md) - AI-powered aquaculture phenotyping; $6M Series A (Aug 2022, Nacre Capital, Innocreative Capital, Martin Halusa, Einar Wathne); SORTpro automatic high-speed salmon gender sorting (10K fish/hr, >95% accuracy); SORTvax v...
* [Astraeus Ocean Systems](astraeus-ocean-systems.md) - Mariculture crop modeling + autonomous vessel fleet for real-time ocean intelligence; Watchline hardware (temp, salinity, DO, optical sensors); Digital Oyster/Digital Kelp biological models; Almanac platform for farm...
* [BiOceanOr](bioceanor.md) - AI-powered water quality forecasting for aquaculture — combining biology & AI for environmental intelligence.
* [Biosort](biosort.md) - Individual-based sea lice control + FishID AI/machine vision for salmon aquaculture.
* [Dirigo Sea Farm](dirigo-sea-farm.md) - Seaweed-based materials to replace plastics; VentureWell OEA Stage 2 (spring 2026, $50K TDC); Portland, ME; sustainable marine biomaterials
* [Innovasea](innovasea.md) - Sustainable aquaculture tech: real-time environmental sensors (aquaMeasure), fish tracking (NexTrak acoustic telemetry), cloud communications; extensive marine sensor network needs
* [Kurma Ai](kurma-ai.md) - GenAI & computer vision for aquaculture and fisheries; AQUA-7B foundation model, AquaChat AI assistant, AQUA OS agentic platform, AquaEye fisheries compliance; VentureWell/NOAA Ocean Enterprise Accelerator Stage 0 (20...
* [MacroBreed](macrobreed.md) - Genomics + selective breeding to increase seaweed aquaculture production; mariculture crop genetics; VentureWell OEA Stage 0 (spring 2026); NY-based
* [Nearview LLC](nearview-llc.md) - Multi-object AI detection (lobster buoys, boats, aquaculture gear) from aerial/satellite imagery for marine user deconfliction; VentureWell OEA Stage 1 (spring 2026, $15K TDC); Portsmouth/Durham, NH
* [NeuralX](neuralx.md) - Decision intelligence for aquaculture from underwater video feeds; Ocean Exchange 2025 Winner ($100K) + Neptune Award; proprietary 3D Artificial Life Simulation Engine for synthetic training data (DeepFoids NeurIPS 20...
* [Nernst Electric](nernst-electric.md) - On-site ceramic OTM oxygen generators for remote fish farms; €1.7M Hatch Blue Seed (Jul 2026); Ireland.
* [Nucleic Sensing Systems](nucleic-sensing-systems.md) - Autonomous biosensing of eDNA/RNA for aquaculture health monitoring; VentureWell OEA Stage 2 (spring 2026, $50K TDC); St.
* [Oceanloop](oceanloop.md) - Software-driven land-based marine RAS + Europe's first land-based Giant Grouper; up to €38.5M (Hatch Blue, Stolt Ventures, €32M EIB); Munich/Kiel.
* [OctaPulse](octapulse.md) - AI-powered fish phenotyping & selective breeding for aquaculture; YC W26; VentureWell OEA Stage 2 (spring 2026); Carnegie Mellon, NVIDIA partners; robotics + computer vision for hatchery automation; $70K Seafood Indus...
* [ORCA](orca.md) - AI foundation modeling to predict environmental shocks to fisheries; VentureWell OEA Stage 0 (spring 2026); Oregon-based
* [ReelData AI](reeldata-ai.md) - AI-powered precision aquaculture for land-based farms; $8M Series A (2025); AI suite (ReelAppetite, ReelWeight, ReelCount) for feed optimization, biomass estimation, fish health monitoring; camera systems for behavior...
* [Tidal](tidal.md) - AI-powered underwater vision + robotics for aquaculture; Alphabet/X (moonshot factory) spinout (Aug 2024); funding from Perry Creek, Kverva-backed IVC, Futurum Ventures; Orca camera system (newest gen); 300+ cameras d...
* [Vycarb](vycarb.md) - Water-based CO2 capture & storage; $5M seed (Oct 2025, Twynam lead; Shell, Hatch Blue, Singapore govt); partnerships with Tomco Systems (industrial CO2 mgmt) & atdepth (MIT spinout ocean monitoring, Google/NASA-backed...

## Bioprospecting

* [Ginkgo Bioworks](ginkgo-bioworks.md) - Synthetic biology platform, marine microbes & enzymes

## Climate Risk

* [Brightband](brightband.md) - AI weather & climate forecasting; $10M Series A (Prelude Ventures, Starshot Capital); NOAA partner for NNJA-AI observational data archive; open-source benchmark weather datasets; ex-Google X, MIT, NSF AI2ES team
* [Climate X](climate-x.md) - AI-powered climate risk analytics and decision platforms
* [First Street Foundation](first-street-foundation.md) - Property-level climate risk data
* [Jupiter Intelligence](jupiter-intelligence.md) - Climate risk modeling & analytics
* [Kettle](kettle.md) - Climate perils insurance & underwriting data

## Coastal Risk & Infrastructure

* [Adaptora](adaptora.md) - Subsurface risk intelligence platform for coastal land subsidence; ultra-high resolution ground deformation sensors; deploying on Governors Island; VentureWell OEA Stage 1 (spring 2026, $15K TDC); Brooklyn, NY (Tensor...
* [Mira Intel](mira-intel.md) - AI drones and patented structural monitoring for coastal/marine infrastructure resilience; high-resolution aerial drone imagery, ongoing condition assessment, predictive analytic modeling; projects: Governor's Island,...
* [Polaris EcoSystems](polaris-ecosystems.md) - Photogrammetric reconstruction for automated remote monitoring of structural degradation in piers, ports, and shoreline assets; time-indexable 3D reconstructions; VentureWell OEA Stage 1 (spring 2026, $15K TDC); Austi...

## Marine Monitoring & Sensors

* [AquaFrontier Technologies](aquafrontier-technologies.md) - Biomimetic autonomous hardware + cloud data pipelines for democratizing ocean observation; real-time ocean intelligence platform; Brooklyn, NY; VentureWell OEA Stage 0 (spring 2026)
* [BeamSea Associates](beamsea-associates.md) - Automated coral reef ecosystem monitoring via fluorescence-enhanced 3D LiDAR + ML; species-level assessment at operational scales; SBIR/STTR funded (NASA, NOAA); Loxahatchee, FL; VentureWell OEA Stage 1 (spring 2026,...
* [Bedrock Ocean Exploration](bedrock-ocean-exploration.md) - Seafloor mapping AUVs + cloud data platform (Mosaic); $25M Series A-2 (Jun 2025) led by Primary/Northzone (Costanoa, Harmony Partners, Katapult Ocean et al.); total funding ~$58.5M over 3 rounds; IHO special-order geo...
* [BeeX](beex.md) - Singapore AUV fleet + SAMbal inspection software; $7.7M Series A (Monk's Hill); dual-use commercial/defense; MINDEF contract.
* [Blue Water Autonomy](blue-water-autonomy.md) - Autonomous warships for US Navy — full-size unmanned surface vessels for open-ocean endurance.
* [Boxfish Robotics](boxfish-robotics.md) - Hovering AUV and resident vehicles for marine science, environmental monitoring, coral reef ecosystem assessment, infrastructure inspection; 6DOF thrusters, NVIDIA Jetson AI, ROS2; reliable for research and conservati...
* [Clear Robotics](clear-robotics.md) - All-electric AI autonomous unmanned surface vessels (Clearbot) for solid waste recovery, hyacinth removal, bathymetric/draft survey, and waterway surveillance.
* [FishLAT (Blue Latitudes)](fishlat-blue-latitudes.md) - ML-powered rapid assessment tool predicting environmental & fisheries impact of offshore infrastructure (removal, reefing, installation); supports permitting and decommissioning decisions; cost-effective data-rich alt...
* [HALOBLUE Tech](haloblue-tech.md) - Autonomous monitoring systems for coastal restoration projects; defensible environmental data at lower cost per acre than vessel surveys; California State University based; VentureWell OEA Stage 1 (spring 2026, $15K T...
* [HavocAI](havocai.md) - All-domain collaborative autonomy (sea/air/land); $100M Series A (May 2026) bringing total capital to ~$200M; Providence RI; 100+ ASVs built/deployed, 30+ delivered to DoD, 25,000+ autonomous hours; software suite (C2...
* [Hullbot](hullbot.md) - Autonomous underwater robots for ship hull cleaning & inspection (proactive hull grooming).
* [Kraken Technology](kraken-technology.md) - UK maritime defence USV/USSV unicorn — $175M Series B at $1B (Jul 2026, DTCP); K3 SCOUT / K4 MANTA / K5; Anduril, Rheinmetall, Davie manufacturing; USSOCOM $49M OTA; Fareham, UK.
* [MarineSitu](marinesitu.md) - Hardware-enabled software for persistent underwater monitoring; SituAI detection/classification >95% accuracy; DOE and US Navy trusted; cameras/ controllers for marine energy, aquaculture, fish counting, reef monitori...
* [Maritime Robotics](maritime-robotics.md) - Norwegian USV & autonomous navigation pioneer since 2005; €28M growth investment (Jun 2026, MS+PARTNERS/Mustard Seed + Partners lead; EnvisionTech, Nysnø Climate Investment, Umoe, founders/employees participating) — o...
* [Ocean State Sensing](ocean-state-sensing.md) - Distributed Temperature Sensing (DTS) fiber optic ThermoTrawl systems; 25cm resolution, 800m+ range; real-time water column profiling; applications: fisheries, defense, climate research, aquaculture; reduce bycatch 10...
* [Oceanic Constellations](oceanic-constellations.md) - Japan USV swarm Marine Satellite Cluster — ¥2B Series B; NYK/JAFCO/Globis; 20+ swarm patents; Kamakura.
* [Omission Inc](omission-inc.md) - Portable autonomous surface vessels (ASVs) + unmanned aerial systems (UAS); reduces nearshore marine data collection cost by 50-70%; survey-grade marine data; Saco, ME; VentureWell OEA Stage 0 (spring 2026)
* [Orpheus Ocean](orpheus-ocean.md) - Deep-sea AUV for cost-effective exploration, benthic monitoring & assessment; .8M Pre-Seed; partnerships with Seabed 2030, NOAA Ocean Exploration, InnovateMass, WHOI heritage; small-footprint AUV for depths up to 11,0...
* [Saildrone](saildrone.md) - Autonomous USV leader for maritime defense & ocean intelligence — Explorer/Voyager/Surveyor/Spectre; >$345M raised; Lockheed Martin $50M strategic; 2.5M nm sailed; Alameda, CA.
* [Saronic Technologies](saronic-technologies.md) - Autonomous surface vessels (ASVs) for defense maritime autonomy; $1.75B Series D (Mar 2026) at $9.25B valuation; total funding ~$2.6B; product line: Spyglass (6'), Corsair (24', 1000+nm, 35+kt, 1000lb payload), Mirage...
* [Seaber](seaber.md) - French micro-AUV manufacturer: YUCO (science/civil, ~10 kg, 1 m, 300 m depth, 8–10 h autonomy) and MARVEL (security/defense: MCM, ASW training, coast guard).
* [Seasats](seasats.md) - Small uncrewed surface vehicles (sUSVs) for long-endurance ocean sensing & MDA; $20M Series A (Feb 2026, Konvoy Ventures lead) — >$40M total equity; >$100M US government contracts including $24M DoW APFIT; San Diego;...
* [Seeweed LLC](seeweed-llc.md) - AI-driven app-managed underwater game camera system for long-term aquatic monitoring; Saint Paul, MN; VentureWell OEA Stage 1 (spring 2026, $15K TDC); mobile app managed camera
* [Sunfish Inc](sunfish-inc.md) - SUNFISH AUV: person-portable hovering autonomous underwater vehicle with AI and SLAM for complex 3D biodiversity mapping; NASA partnership; VentureWell OEA Stage 1 (spring 2026, $15K TDC); Austin, TX / Tallahassee, FL...
* [TDSX (Tampa Deep Sea Xplorers)](tdsx-tampa-deep-sea-xplorers.md) - Barracuda AUV for cost-effective underwater exploration & data collection; sub-bottom profiling, water column characterization, ocean current/temp/salinity profiles; applications: offshore energy, oceanographic resear...
* [Ulysses](ulysses.md) - Modular autonomous underwater vehicles (Mako AUV) + Kraken launch/recovery system; $46M total (seed + Series A, April 2026) led by a16z American Dynamism (Erin Price-Wright, Ryan McEntush); 50x cheaper than legacy AUV...
* [Vatn Systems](vatn-systems.md) - Defense-tech modular AUVs operating in cooperative swarms; $60M Series A (Dec 2025) — one of largest AUV defense raises to date; founded 2023, Rhode Island-based; new AUV-torpedo product line; state-of-the-art RI manu...
* [WSense](wsense.md) - Internet of Underwater Things — underwater wireless mesh IoUT; >€25M raised; Fincantieri partner; Rome.

## Maritime Operations & Analytics

* [Aloft Systems](aloft-systems.md) - Sustainable zero-emission shipping via robotic wind propulsion / modern sails; containerized sail systems; BlueSwell startup; VentureWell OEA Stage 2 (spring 2026); Boston, MA; ex-Autodesk Research spinout
* [Nexus Ocean AI](nexus-ocean-ai.md) - Maritime AI-native service orchestration; genAI persona (SAM) + Maritime Language Model; automated 90% of maritime workflows; $400K seed (Aug 2024, Tradeworks.vc); Google Cloud partner; MPA Mint Grant; Singapore-based...
* [Orca AI](orca-ai.md) - AI-powered computer vision & situational awareness for maritime navigation safety + collision avoidance; $72.5M Series B (May 2025, Brighton Park Capital lead; Ankona Capital, Hyperlink Ventures, OCV Partners, Mizmaa...
* [SEA.AI](sea-ai.md) - Maritime machine vision for safety at sea; AI-powered camera systems detect & classify objects on water surface that escape radar/AIS (unsignalled craft, debris, persons overboard, kayaks, inflatables).
* [Sea Machines Robotics](sea-machines-robotics.md) - Autonomous control & navigation systems for commercial and defense vessels; Boston MA; products: SM300-SP (attritable compact), SM300-NG (class-approved), SELKIE (modular USV), STORMRUNNER (contested waters AUSV), AI-...
* [VesselOps](vesselops.md) - 3D visualization and digital authentication for fleet management; VentureWell OEA Stage 2 (spring 2026, $50K TDC); New Bedford, MA; maritime fleet operations software
* [Zeaclub](zeaclub.md) - AI-powered maritime collaborative workspace connecting ship owners, charterers, brokers, agents, ports in one platform; real-time collaboration replacing email chains & spreadsheets; structured data entry & validation...

## Ocean Carbon Sequestration

* [Apeiron Labs](apeiron-labs.md) - AUV-based ocean data platform; $9.5M Series A (Feb 2026); low-cost autonomous underwater vehicles for persistent ocean observation; real-time ocean intelligence; led by Dyne Ventures; MIT News May 2026 feature on ocea...
* [Calcarea](calcarea.md) - Ship-board carbon capture converting CO2 to oceanic bicarbonate; Caltech spun-out; $3.5M seed; founded by Jess Adkins
* [Captura](captura.md) - Direct Ocean Capture; $12.5M Series B (Jun 2026, Equinor Ventures lead; Aramco Ventures, EDP Ventures, Eni Next, Freeflow Ventures, Hitachi Ventures, JAL Innovation Fund, Maersk Growth, mTerra Ventures, National Grid...
* [Carbon Time](carbon-time.md) - Ocean alkalinity enhancement CDR; >20,000 yr permanence; European-based pioneer
* [CREW Carbon](crew-carbon.md) - Wastewater alkalinity CDR + process intensification — $25M Series A (May 2026); $33M+ offtakes; Yale spinout.
* [Ebb Carbon](ebb-carbon.md) - Electrochemical CDR from brine; $20M Series A (2026) — largest ocean CDR Series A to date, Carbon Herald report; landmark Microsoft CDR deal up to 350,000 tCO2 over 10 yrs (2024); Google partnership (Dec 2025); Projec...
* [Equatic](equatic.md) - Ocean-based CDI / CDR; new NA commercial plant; world's largest ocean CDR plant planned in Singapore; UCLA Institute for Carbon Management partnership; targeting <$100/t CDR; strong marine env.
* [Gigablue](gigablue.md) - Durable ocean carbon removal; deep-sea monitoring with custom ROVs; large-scale CDR credits; marine scientific research focus
* [Kelp Blue](kelp-blue.md) - Large-scale offshore giant kelp cultivation for blue carbon sequestration and ocean rewilding; biostimulants
* [Limenet](limenet.md) - Ocean alkalinity enhancement via pH-equilibrated calcium solutions; permanent carbon storage in seawater
* [pHathom Technologies](phathom-technologies.md) - Accelerated Weathering of Limestone (AWL) for biomass-sourced CO2 dissolution in seawater and limestone neutralization; durable calcium bicarbonate storage; supports marine life; $4M seed 2026 (total $12M committed).
* [Planetary Technologies](planetary-technologies.md) - Ocean alkalinity enhancement; $11.35M Series A (Oct 2024, Evok Innovations lead, BDC Capital, Amplify Capital); total funding ~$15.2M; Halifax OAE Joint Learning Opportunity with Carbon to Sea Initiative; Frontier $31...
* [Pronoe](pronoe.md) - Asset-light electrochemical alkalinity enhancement on industrial discharge streams; $3.05M Frontier/Google carbon removal pre-purchase (Frontier's first French portfolio company); automated water treatment systems co-...
* [Running Tide](running-tide.md) - Ocean-based biomass sequestration; shut down June 2024; legacy protocol for open-ocean CDR
* [Seabound](seabound.md) - Onboard carbon capture from shipping exhaust; marine CDR synergy
* [SeaO2](seao2.md) - Electrochemical Direct Ocean Capture (DOC); gigaton-scale potential; renewable-powered; preparing €12M Series A for early 2027; €2M+ seed raised; BlueInvest recognition (EU Commission, Feb 2026); GCNE accelerator sele...
* [Vaulted Deep](vaulted-deep.md) - Biomass carbon removal from waste; scalable BiCRS approach

## Ocean Data & AI

* [Amphitrite](amphitrite.md) - AI-powered ocean data intelligence platform; satellite & in-situ data fusion for maritime operations (shipping efficiency, maritime sovereignty); €1.2M seed (2024); advanced SWOT satellite technology integration; Fran...
* [Bluemvmt](bluemvmt.md) - AI-powered ocean data platform transforming unstructured IoT data (satellite, marine sensors, disparate databases) into actionable insights; Narrative Detection ML; Data Insight AI; sidecar integrations; VentureWell O...
* [Coastal Measures](coastal-measures.md) - Coastal intelligence platform (CUMULUS) powered by YSOK AI; unifies multi-modal coastal sensor data (radar, camera, buoy, satellite) into governed data fabric; automated QA/QC; NOAA, USACE, NSF, Sofar Ocean partners;...
* [Dottir Labs](dottir-labs.md) - MIT spinout (2023); real-time molecular-level water quality monitoring via patented Raman spectroscopy; reagent-free, non-destructive optical sensors; aquaculture, biotech, oil & gas, chemical manufacturing applicatio...
* [Quartermaster](quartermaster.md) - SmartMast distributed maritime sensing network mounted on commercial vessels; $43M Series A (May 2026) co-led by First Round Capital (Bill Trenchard) and Quiet Capital; 600+ ships equipped across 25+ countries; 10M+ s...
* [SeaDeep](seadeep.md) - AI platform for ocean mapping, monitoring, underwater inspection using AI for marine robotics autonomy; subsea exploration intelligence; grants $1M+; partners with Seabed 2030; focuses on AI-powered ocean data for cor...
* [Sofar Ocean](sofar-ocean.md) - Largest privately-owned ocean sensor network in the world; 2,500+ Spotter drifters deployed globally; 1.5M real-time observations/day; 25M+ hours of ocean observations; total funding ~$75-78.5M (Series B $39M led by U...
* [Ubotica](ubotica.md) - Orbital AI / cognitive Earth observation for real-time maritime intelligence from space.
* [Unseenlabs](unseenlabs.md) - Space-based RF maritime surveillance for dark vessels; €85M Series C; ~€120M total; French BRO constellation.
* [XOCEAN](xocean.md) - Turnkey ocean data via in-house USV fleet — €115M growth (Jan 2025); Ørsted/Shell/bp customers; 48.6+ GW offshore wind supported; Ireland HQ.

## Offshore Energy

* [BW Ideol](bw-ideol.md) - Floating offshore wind solutions and infrastructure
* [Endurance Energy](endurance-energy.md) - Subsea geothermal baseload power — $54M Series A (Jun 2026, Founders Fund); Adélie OOI Axial Seamount pilot; Tonga partnership; Seattle.
* [Fleetzero](fleetzero.md) - Marine energy & robotics — ultra energy-dense modular marine battery systems (Leviathan) + hybrid/electric propulsion for commercial vessels.
* [Gazelle Wind Power](gazelle-wind-power.md) - Floating wind platforms; needs oceanographic/metocean data services
* [Kvasir Technologies](kvasir-technologies.md) - Climate-neutral drop-in marine biofuel from lignocellulosic biomass (non-edible agricultural & forestry waste).
* [Ørsted](orsted.md) - Offshore wind major; extensive marine environmental surveys & monitoring
* [Oshen](oshen.md) - Autonomous ocean robots (C-Stars) for persistent wide-area ocean intelligence; NOAA contracts; funded by UK ARIA; extreme weather data collection; real-time wave height, wind speed, oceanographic data
* [Panthalassa](panthalassa.md) - Ocean wave-powered AI computing & data centers; $140M Series B (May 2026) led by Peter Thiel; ~$1B valuation; offshore compute nodes and wave energy generation; Fortune/FT/Reuters coverage May 2026; marine environment...
* [Pittsburgh Coastal Energy](pittsburgh-coastal-energy.md) - Subsea power via modular onboard wave-energy converters for autonomous maritime systems; VentureWell OEA Stage 2 (spring 2026, $50K TDC); Pittsburgh, PA; ocean wave charging for underwater systems; NOAA/defense applic...
* [Principle Power](principle-power.md) - Floating offshore wind platform technology
* [Sitkana](sitkana.md) - Ocean current energy systems powering remote communities; DOE grant; VentureWell OEA Stage 2 (spring 2026, $50K TDC); Juneau, AK; tidal stream generation for Alaska coastal communities; removable anchor installation;...
* [Sizable Energy](sizable-energy.md) - Gigawatt-scale ocean energy storage using offshore pumped hydro with brine: seabed reservoir + floating reservoir + connecting pipe + reversible pump-turbines.
* [Spoor](spoor.md) - AI bird/bat monitoring for wind farms; €8M Series A; Sky Intelligence Platform; Ørsted/RWE/Ocean Winds.
* [Voltai](voltai.md) - Onboard wave/motion energy harvesting for ships — electrostatic generators converting wave and vibration energy into electricity without added drag.
