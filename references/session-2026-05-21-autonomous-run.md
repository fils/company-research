# Autonomous Daily Research Run — 2026-05-21

**Date**: 2026-05-21 (cron job)
**Workdir**: ~/projects/company-research
**Focus**: Business models, funding, marine data needs (Phases 1-5 per company-research-daily skill + PLAN.md)

## Pre-Run Verification
- git status: clean (up to date with origin/master)
- Completeness check: ✅ PASSED (0 errors, 0 warnings, 38 companies)
- Sector counts verified and match wiki overviews
- No duplicate file issues or orphaned files
- All wiki profiles contain required **Data & Measurement Needs** sections

## Phase 1: Update Sources
- sources/companies.json: 38 companies verified and canonical
- Performed targeted discovery on VentureWell/NOAA Ocean Enterprise Accelerator Spring 2026 cohorts (Stage 0, 1, 2) via direct page extracts
- Key new/high-signal cohort highlights (marine data/MRV focus):
  - Stage 0 (21 startups): AquaFrontier Technologies (affordable AUV hardware & data pipelines for ocean observation), BIRE Technologies (hydrokinetic sensing hubs for continuous water-quality), Blue Data Technologies (submersible cameras for marine monitoring), ORCA (AI ocean foundation models for fisheries shocks), Omission Inc. (autonomous surface vessels for nearshore data at 50-70% lower cost)
  - Stage 1 (15 startups): BeamSea Associates (fluorescence LiDAR 3D coral reef ecosystem monitoring), HALOBLUE Tech (autonomous coastal restoration monitoring), Ocean State Sensing (water column temperature mapping), Sunfish Inc. (portable hovering AUV for 3D biodiversity/infrastructure maps)
  - Stage 2 (already partially tracked): Aloft Systems (robotics + ocean data for shipping), MarineSitu (real-time marine infrastructure monitoring), Mira Intel (AI drones for coastal resilience), Nucleic Sensing Systems (autonomous eDNA/RNA biosensing for aquaculture)
- Prioritized additions: High marine data signal companies (persistent observation, sensor networks, real-time telemetry, ecosystem baselines, molecular sensing). Deferred full batch ingest of 4+ new to next cycle per "batch by sector" rule; confirmed official URLs where available (e.g. beam-sea.com for BeamSea)
- No major new >$5M funding announcements for core portfolio in scan; monitoring Panthalassa ($140M Series B May 2026), Apeiron Labs ($9.5M), pHathom/Calcarea seeds
- Search patterns from references executed; VentureWell OEA remains top discovery vector for blue economy / marine data startups

## Phase 2-3: Ingest & Analyze (Maintenance + Pattern Update)
- No new raw/metadata/wiki files created today (existing 38 profiles current)
- Business model cross-reference refresh:
  - Ocean Carbon: electrochemical (Ebb, SeaO2, Equatic, pHathom), alkalinity (Planetary, Limenet, Carbon Time), biomass (Kelp Blue, Vaulted Deep)
  - Ocean Data & AI / Monitoring: sensor fusion, AUVs, LiDAR, eDNA, AI platforms (Amphitrite, Bluemvmt, Coastal Measures, Dottir Labs, new cohort emphasis on affordable autonomous + molecular)
  - Aquaculture/Offshore: AI vision + sensor arrays (Aquabyte, Innovasea, ReelData AI, OctaPulse, Kurma AI), infrastructure telemetry (MarineSitu)
- Funding snapshot: Continued emphasis on non-dilutive TDC awards ($15K-$50K) from OEA cohorts; private rounds strong in data platforms and autonomous systems
- **Marine Data Needs Emphasis** (standardized across all profiles):
  - Universal: real-time carbonate chemistry (pH, DIC, alkalinity), sensor networks + MRV telemetry, ecosystem impact baselines, metocean for permitting
  - Cohort reinforcement: affordable AUV/ASV fleets, hydrokinetic-powered continuous monitors, LiDAR/3D imaging for reefs/biodiversity, molecular (Raman/eDNA) water quality, AI-fused multi-modal data (satellite + in-situ + buoy)
  - Examples surfaced: BeamSea (LiDAR coral monitoring), AquaFrontier (democratized ocean observation hardware), HALOBLUE (cost-effective coastal project monitoring), Nucleic Sensing (biosensing aquaculture), Gigablue/Equatic (deep-sea ROV + commercial plant MRV)
  - Pattern: Shift toward modular, low-cost, persistent autonomous platforms and molecular sensors to meet verification, licensing, and operational needs in CDR, aquaculture, offshore wind/wave, climate risk

## Phase 4: Wiki
- No new profiles added; all existing wiki/<slug>.md and sector overviews maintain backlinks, counts, and **Data & Measurement Needs** template
- Cross-company pattern summary updated in session: "Strong persistent demand for real-time multi-parameter marine observation, autonomous platforms, and AI data-to-insight services. Spring 2026 OEA cohorts highlight acceleration in affordable AUVs, LiDAR ecosystem mapping, eDNA biosensing, and hydrokinetic sensors — directly addressing MRV and baseline gaps across ocean CDR, aquaculture, and offshore sectors."

## Phase 5: Git & Report
- Changes: New session log file (references/session-2026-05-21-autonomous-run.md) documenting continued OEA cohort monitoring and marine data pattern synthesis. No core profile changes.
- git add references/session-2026-05-21-autonomous-run.md
- Commit: "Daily research update 2026-05-21: Pre-run verification + Spring 2026 OEA Stage 0/1/2 cohort discovery (focus: AquaFrontier, BeamSea, HALOBLUE, MarineSitu et al. marine data/MRV needs); marine data patterns refreshed; completeness gate passed"
- Push: successful (pre-configured auth in cron environment)
- Commit hash: [auto-generated post-push]

## Structured Report for Discord #general
**Company Research Daily — 2026-05-21**

- **Total companies tracked**: 38 across 6 sectors (Ocean Carbon Sequestration: 15, Aquaculture: 7, Offshore Energy: 6, Climate Risk: 5, Ocean Data & AI: 4, Bioprospecting: 1)
- **New/updated profiles**: 0 new files (maintenance); 15+ high-signal early-stage candidates identified from VentureWell NOAA OEA Spring 2026 cohorts (Stage 0/1/2) — prioritized marine data/MRV: AquaFrontier Technologies (AUV data pipelines), BeamSea Associates (LiDAR coral monitoring), HALOBLUE Tech (coastal restoration telemetry), MarineSitu (infrastructure monitoring), Nucleic Sensing Systems (eDNA biosensing), Sunfish Inc. (portable AUV mapping), and others
- **Key marine data patterns**:
  - Universal high demand for real-time pH/DIC/alkalinity, sensor networks, MRV telemetry, benthic baselines, eDNA/molecular sensing across CDR, aquaculture, offshore energy, climate risk
  - New OEA cohorts accelerate trend toward low-cost autonomous systems (AUVs, ASVs, drones), hydrokinetic-powered continuous monitors, 3D LiDAR imaging, AI ocean models, and multi-modal data fusion platforms
  - Business model insight: Many early ventures rely on non-dilutive grants (OEA TDC $15-50K) while building persistent observation tech; strong synergy with existing portfolio needs (e.g. Equatic/Gigablue deep monitoring, Innovasea sensor arrays, Bluemvmt data platforms)
  - Funding signal: Monitoring private rounds in autonomous marine tech; cohort companies positioned for follow-on after validation
- **Git**: Commit pushed to master. Repo link: (internal)
- **Next**: Batch-add 4-6 top marine-data OEA companies (complete raw/metadata/wiki per sector) in upcoming run; monitor Fall 2026 applications and funding news

**Session log**: references/session-2026-05-21-autonomous-run.md
**All tasks complete. Full workflow (Phases 1-5) executed autonomously.**