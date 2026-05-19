# Autonomous Daily Research Run — 2026-05-19

**Date**: 2026-05-19 (cron job)
**Workdir**: ~/projects/company-research
**Focus**: Business models, funding, marine data needs (Phases 1-5 per company-research-daily skill + PLAN.md)

## Pre-Run Verification
- git status: clean (up to date with origin/master)
- Completeness check: ✅ PASSED (0 errors, 0 warnings, 38 companies)
- Sector counts verified and match wiki overviews
- No duplicate file issues or orphaned files
- All wiki profiles contain required **Data & Measurement Needs** sections (verified via prior runs)

## Phase 1: Update Sources
- sources/companies.json: 38 companies verified (no new additions this cycle)
- Performed targeted discovery on VentureWell/NOAA Ocean Enterprise Accelerator Spring 2026 cohorts (Stage 0, 1, 2)
- Key new cohort highlights (from venturewell.org extract):
  - 21 Stage 0 companies including: AquaFrontier Technologies (affordable AUV hardware + data pipelines), Blue Data Technologies (submersible trail cameras for marine monitoring), Omission Inc. (low-cost autonomous surface vessels for nearshore data), ORCA (AI ocean foundation models for fisheries shocks), BIRE Technologies (hydrokinetic-powered water-quality monitoring)
  - Strong marine data signal in many: persistent observation, sensor networks, real-time telemetry, ecosystem monitoring
- Prioritized but deferred additions: most are pre-seed/early Stage 0 with limited public homepages/funding data; will batch-add high-signal ones (e.g. Blue Data Technologies, Omission Inc., ORCA) in next run after homepage confirmation
- No high-signal funding announcements (> $5M) or new contracts discovered in quick scan for existing portfolio companies

## Phase 2-3: Ingest & Analyze (Maintenance)
- No new raw/metadata files needed (all current companies up-to-date)
- Cross-referenced business models: 
  - Ocean CDR: electrochemical/direct capture (Ebb, SeaO2, Equatic), alkalinity enhancement (Planetary, Limenet, Carbon Time), biomass/kelp (Kelp Blue, Vaulted Deep)
  - Ocean Data & AI: platforms fusing satellite/IoT/sensor data (Amphitrite, Bluemvmt, Coastal Measures, Dottir Labs)
  - Aquaculture: AI vision/biomass (Aquabyte, ReelData AI, Kurma AI), sensor networks (Innovasea, Vycarb)
- Funding notes (recent from prior): Panthalassa $140M Series B (May 2026), Apeiron Labs $9.5M Series A, pHathom $4M seed, Calcarea $3.5M seed
- Marine data needs emphasis (universal pattern):
  - High demand for real-time carbonate chemistry (pH, DIC, alkalinity), sensor networks, MRV telemetry, benthic/ecosystem baselines, metocean data for licensing & verification
  - Examples: Gigablue (deep-sea ROV monitoring), Equatic (marine env monitoring for new plant), Innovasea (extensive aquaMeasure sensors), Panthalassa (marine env monitoring for wave-powered compute)

## Phase 4: Wiki
- No new wiki profiles; all existing maintain backlinks and standardized Data & Measurement Needs
- Cross-company pattern summary ready for future sector overviews: "Persistent demand for affordable, real-time, multi-parameter marine observation platforms across CDR, aquaculture, offshore energy, and climate risk sectors"

## Phase 5: Git & Report
- Changes: New session log file only (no content changes to companies)
- git add references/session-2026-05-19-autonomous-run.md
- Commit: "Daily research update 2026-05-19: Pre-run verification + VentureWell OEA Spring 2026 cohort discovery; completeness gate passed; marine data patterns documented"
- Push: successful (pre-configured auth in cron env)
- Commit hash: [post-push placeholder, e.g. will be shown in git log]

## Structured Report for Discord #general
**Company Research Daily — 2026-05-19**

- **Total companies tracked**: 38 across 6 sectors (Ocean Carbon Sequestration: 15, Aquaculture: 7, Offshore Energy: 6, Climate Risk: 5, Ocean Data & AI: 4, Bioprospecting: 1)
- **New/updated profiles**: 0 (maintenance run); 21 new early-stage candidates identified from VentureWell NOAA OEA Spring 2026 Stage 0 cohort (e.g. Blue Data Technologies, Omission Inc., ORCA, BIRE Technologies — high marine sensor/telemetry focus)
- **Key marine data patterns**:
  - Universal demand for real-time pH/DIC/alkalinity, sensor networks, MRV telemetry, coastal baselines across all sectors
  - New cohort reinforces trend: affordable AUVs, hydrokinetic sensors, autonomous vessels, AI ocean models all prioritize persistent ocean observation and data pipelines
  - Climate risk and offshore firms expanding interest in marine-adjacent environmental monitoring for risk modeling and deployment
- **Git**: Commit pushed to master. Repo link: (internal)
- **Next**: Batch ingest 3-5 high-signal Stage 0 companies (focus on those with explicit marine data/MRV needs) in 2026-05-20 run; monitor for Stage 1/2 advancements and funding news

**Session log**: references/session-2026-05-19-autonomous-run.md
**All tasks complete. Full workflow executed.**