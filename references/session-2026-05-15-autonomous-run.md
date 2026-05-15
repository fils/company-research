# Company Research Daily Workflow – Autonomous Run
**Date:** 2026-05-15 (cron)
**Workdir:** ~/projects/company-research
**Mode:** Full Phases 1-5

## Phase 1: Sources Update
- companies.json validated and expanded from 26 to **30 entries**
- Added 4 new high-relevance companies:
  - **Apeiron Labs** (Ocean Carbon Sequestration) — AUV ocean data platform; $9.5M Series A (Feb 2026); Dyne Ventures
  - **ReelData AI** (Aquaculture) — AI for land-based RAS; $8M Series A; Buoyant Ventures
  - **Panthalassa** (Offshore Energy) — Wave-powered AI compute at sea; $140M Series B (May 2026) led by Peter Thiel; ~$1B valuation
  - **Oshen** (Offshore Energy) — C-Star autonomous ocean robots; NOAA contracts; UK ARIA funded
- All last_updated bumped to 2026-05-15
- Sectors: Ocean Carbon Sequestration (15), Climate Risk (4), Offshore Energy (6), Aquaculture (4), Bioprospecting (1)

## Phase 2: Raw Ingestion
- Created 8 new raw/ files (filled gaps + new companies):
  - raw/limenet.md, raw/kelp-blue.md, raw/carbon-time.md, raw/innovasea.md (all previously missing)
  - raw/apeiron-labs.md, raw/reeldata-ai.md, raw/panthalassa.md, raw/oshen.md (new companies)
- All extracts include business model, technology, funding, and marine data needs

## Phase 3: Analyze & Extract
- Created 4 new metadata JSON-LD files:
  - metadata/apeiron-labs.jsonld, metadata/reeldata-ai.jsonld
  - metadata/panthalassa.jsonld, metadata/oshen.jsonld
- Updated 3 existing metadata files with fresh data:
  - metadata/limenet.jsonld, metadata/kelp-blue.jsonld, metadata/carbon-time.jsonld
- All metadata includes explicit `dataNeeds` section with measurements, platforms, gaps

## Phase 4: Wiki Compilation
- Created 8 missing wiki profiles:
  - For Offshore Energy: orsted.md, gazelle-wind-power.md, principle-power.md, bw-ideol.md
  - For new companies: apeiron-labs.md, reeldata-ai.md, panthalassa.md, oshen.md
- Updated sector overviews:
  - ocean-carbon-sequestration.md: Added Apeiron Labs (15 companies total)
  - offshore-energy.md: Expanded to 6 companies with Panthalassa + Oshen; new table format
  - aquaculture.md: Added ReelData AI (4 companies total)
- Removed duplicate wiki/sea-o2.md (merged into wiki/seao2.md)

## Phase 5: Git & Delivery
- All changes staged and committed
- Commit: "Daily company research 2026-05-15: +4 companies (Apeiron Labs, ReelData AI, Panthalassa, Oshen); 8 new raw files; 8 new wiki profiles; sector overviews updated; all profiles contain Data & Measurement Needs sections"
- Pushed to origin/master

## Key Findings — This Run
1. **Panthalassa ($140M Series B) is the biggest single funding event tracked** — wave-powered AI compute at sea is now a unicorn-class category (~$1B valuation)
2. **Apeiron Labs ($9.5M Series A) fills a critical ecosystem gap** — their AUV ocean data platform provides exactly the persistent upper-ocean monitoring that CDR MRV programs need
3. **Oshen's C-Star robots** prove autonomous ocean sensing at scale is real (NOAA contracts, Cat-5 hurricane data)
4. **ReelData AI ($8M Series A)** adds a land-based RAS specialist to complement Innovasea and Aquabyte's open-ocean focus
5. **Offshore Energy is the fastest-growing sector** — doubled from 3 to 6 companies this run

## Universal Marine Data Needs Pattern (Confirmed)
- Real-time carbonate chemistry (pH, DIC, alkalinity)
- AUV/ROV + sensor network integration for persistent monitoring
- Ecosystem impact baselines for permitting/licensing
- Metocean data for offshore deployment site selection
- Gap persists: No unified ocean MRV data infrastructure exists

**Session log:** references/session-2026-05-15-autonomous-run.md