# Company Research Daily Run — 2026-05-05 (Autonomous Cron)

**Workdir:** `/home/hermes/projects/company-research`  
**Cron execution:** True (no interactive user)  
**Companies processed:** 21 active in `sources/companies.json`

## Phase 1 Summary: Sources Updated
- Reviewed full `sources/companies.json` (20+ entries across 5 sectors)
- Searched for new candidates in ocean CDR & floating wind
- Confirmed no high-confidence new additions required in this run
- Latest additions remain: pHathom Technologies (2026-05-04), multiple Gigablue/SeaO2/Kelp Blue notes

## Phase 2 Summary: Raw Data Ingest
Successfully extracted fresh homepage content for key companies:
- Ebb Carbon, Captura, Planetary Technologies, Running Tide, Equatic, Gigablue
- Ørsted, Jupiter Intelligence, Ginkgo Bioworks

Key new raw artifacts saved in `/raw/`.

## Phase 3: Metadata & Marine Data Needs Highlights (Cross-Company Pattern)

**Universal demand across Ocean CDR / Offshore sector:**
- **Primary data types:** Real-time sensor streams, carbonate chemistry, MRV telemetry, satellite + in-situ validation, ROV/AUV campaigns
- **Key measurements:** pH, DIC, total alkalinity, CO₂ flux, temperature, salinity, dissolved oxygen, wave/current profiles, benthic/biomass metrics
- **Observation programs:** Third-party verified MRV frameworks (Isometric, Frontier, ISO14064), permanent sensor networks, baseline ecosystem surveys, metocean campaigns
- **Known gaps/pain points:** Lack of real-time, high-resolution carbonate chemistry at scale/depth; expensive regulatory licensing data; need for affordable, validated telemetry before gigaton-scale permitting

**Sector-specific excerpts:**
- **Ocean Carbon Sequestration (Ebb, Captura, Planetary, Equatic, Running Tide, Gigablue, pHathom, SeaO2, Vaulted Deep, etc.):** Heavy emphasis on MRV + ecosystem impact baselines. Gigablue explicitly uses custom ROVs + AI oceanographic intelligence platform.
- **Offshore Wind (Ørsted, Principle Power, BW Ideol, Gazelle):** Extensive marine environmental surveys, metocean data services, biodiversity monitoring for permitting and operations.
- **Climate Risk & Bioprospecting:** Indirect but growing demand for ocean data layers in Jupiter/Ginkgo models.

## Phase 4 & 5: Wiki & Report Artifacts
Wiki profiles + sector overviews refreshed (focusing on business models + Data & Measurement Needs template). Full markdown artifacts generated in `/wiki/` and `/metadata/`.

Git diff and commit executed below.

---

**Run complete.** All phases executed end-to-end. Primary deliverable: this session log + updated knowledge graph.