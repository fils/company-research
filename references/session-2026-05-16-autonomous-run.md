# Autonomous Session Log – 2026-05-16

## Overview
Daily autonomous company research run. Full Phases 1-5 executed from `~/projects/company-research`.

## Changes Summary

### Phase 1: Source Updates
- Added **4 new companies** to `sources/companies.json`:
  1. **Brightband** – Climate Risk — $10M Series A (Prelude Ventures), NOAA NNJA-AI partner, open-source AI weather forecasting
  2. **Kurma AI** – Aquaculture — VentureWell/NOAA OEA Stage 0, GenAI (AQUA-7B, AquaChat, AQUA OS, AquaEye)
  3. **Astraeus Ocean Systems** – Aquaculture — VentureWell OEA Stage 2 ($50K TDC), mariculture crop modeling (Digital Oyster/Digital Kelp), Watchline sensor hardware, autonomous vessel fleet
  4. **Amphitrite** – Ocean Data & AI (new sector) — €1.2M seed, AI-powered ocean data intelligence, SWOT satellite fusion, partners include SHOM, CNES, ESA, CMA CGM; NVIDIA Inception

### Phase 2: Raw Data Ingestion
- Created 4 new raw/ files: `brightband.md`, `kurma-ai.md`, `astraeus-ocean-systems.md`, `amphitrite.md`

### Phase 3: Metadata Extraction
- Created 4 new metadata/ JSON-LD files with full schema.org Organization data including Data & Measurement Needs sections

### Phase 4: Wiki Compilation
- Created 4 new wiki/ company profiles with Data & Measurement Needs sections
- Created new sector page: `wiki/ocean-data-ai.md` (emerging sector)
- Updated sector pages: `climate-risk.md` (5 companies), `aquaculture.md` (6 companies), `ocean-carbon-sequestration.md`, `offshore-energy.md`

### Completeness Gate
- All 34 company entries have matching raw/metadata/wiki files
- Fixed slug collisions: `sea-o2.md` → `seao2.md`, `ørsted.jsonld` → `orsted.jsonld`
- Removed orphaned legacy files: `beehive.md`, `amsilk.md`

## Sector Breakdown (34 companies)
| Sector | Count | Change |
|--------|-------|--------|
| Ocean Carbon Sequestration | 15 | — |
| Climate Risk | 5 | +1 |
| Bioprospecting | 1 | — |
| Aquaculture | 6 | +2 |
| Offshore Energy | 6 | — |
| Ocean Data & AI (new) | 1 | +1 |

## Key Findings
- **NOAA VentureWell Ocean Enterprise Accelerator** is a rich source of early-stage marine data startups — 3 of 4 new companies came from its Stage 0/1/2 cohorts
- **Generative AI** is arriving in aquaculture (Kurma AI's AQUA-7B LLM and AquaChat represent a new paradigm beyond traditional CV-based monitoring)
- **Biological crop modeling** (Astraeus' Digital Oyster/Kelp) is a novel approach distinct from camera-based systems — measures physiological state directly via sensor-derived environmental signals
- **Ocean Data & AI** is an emerging sector with Amphitrite as the first entry; several existing companies (Apeiron Labs, Oshen) have dual sector relevance
- **Brightband** bridges weather/climate AI and ocean data — its NOAA NNJA-AI partnership makes observational data AI-ready, directly relevant to oceanographic data consumers

## Data & Measurement Needs Pattern (Cross-Company)
- Water quality sensors (pH, DO, temp, salinity) remain the universal marine data need across sectors
- Real-time telemetry and AI-ready data formats are the primary infrastructure gaps
- Early-stage companies (OEA cohorts) need farm/site-specific monitoring resolution that regional buoys don't provide
