# Autonomous Run: 2026-06-01

## Summary
Daily company research workflow (Phases 1-5) executed autonomously as scheduled cron job. **Three new companies added** — all major marine-autonomy / maritime-AI funding events of the past ~6 weeks. The combined disclosed capital raised by new additions is **$149M**, signaling strong investor conviction in the ocean-tech thesis. Pre-run verification and completeness gate both passed with zero issues.

## Pre-Run Verification
- `git status`: working tree clean (start of run)
- `python3 scripts/completeness-check.py`: ✅ PASSED (62 → 65 companies, 0 errors, 0 warnings)
- Sector counts updated: Marine Monitoring & Sensors 10→12, Ocean Data & AI 4→5

## New Companies Added (3)

### 1. Ulysses — Marine Monitoring & Sensors
- **Site**: https://www.theoceancompany.com/
- **Funding**: **$46M total** (seed + Series A, April 2026) led by **a16z American Dynamism** (Erin Price-Wright, Ryan McEntush)
- **Product**: Mako AUV (72hr endurance, 200 lb payload, 5,000 ft depth) + Kraken launch/recovery/recharge system
- **Key differentiator**: 50x cheaper than legacy AUVs ($50K unit cost); modular "Lego" payload design; cooperative swarms; 40x more subsea computing power
- **Customers**: US Navy, VIMS, Mote Marine Lab, Great Barrier Reef Foundation, Nature Conservancy, Government of Australia
- **Origin**: Dublin, Ireland → San Francisco, CA
- **Marine data relevance**: VERY HIGH — multiple AUV sensor platforms; high-resolution subsea imagery, acoustic, bathymetric data; cooperative swarm telemetry

### 2. Vatn Systems — Marine Monitoring & Sensors
- **Site**: https://www.vatnsystems.com/
- **Funding**: **$60M Series A** (December 2025) — one of the largest AUV defense raises to date
- **Product**: Modular AUV platform; new AUV-torpedo product line; cooperative swarms
- **Key differentiator**: "Next underwater defense prime" positioning; advanced navigation in GPS/vision/comm-denied environments; stealthy low-bandwidth inter-vehicle comms
- **State-of-the-art Rhode Island manufacturing facility**; first international contract (Singapore)
- **Marine data relevance**: HIGH — defense ISR, subsea surveillance, environmental monitoring

### 3. Quartermaster — Ocean Data & AI
- **Site**: https://www.quartermaster.us/
- **Funding**: **$43M Series A** (May 2026) co-led by **First Round Capital** (Bill Trenchard) and Quiet Capital
- **Product**: SmartMast™ distributed maritime sensing + AI analytics platform
- **Scale**: 600+ ships equipped across 25+ countries; 10M+ sq mi covered; 400K+ vessels identified without AIS; 20+ maritime rescues
- **Key differentiator**: "Pro-mariner" model — free hardware in exchange for network participation; positions as upgrade over fraud-prone AIS
- **Founder/CEO**: Neil Sobin; HQ Arlington, VA
- **Marine data relevance**: VERY HIGH — vessel tracking, HD/IR imagery, RF capture (AIS/ADS-B/VHF/radar), onboard AI classification, real-time satcom

## Updated Companies
None. The 3 new additions are net new; no existing company profiles required refreshes.

## Files Created
- `raw/ulysses.md`
- `raw/vatn-systems.md`
- `raw/quartermaster.md`
- `metadata/ulysses.jsonld`
- `metadata/vatn-systems.jsonld`
- `metadata/quartermaster.jsonld`
- `wiki/ulysses.md`
- `wiki/vatn-systems.md`
- `wiki/quartermaster.md`

## Files Updated
- `sources/companies.json` — +3 entries (62 → 65 total)
- `wiki/marine-monitoring-sensors.md` — +2 companies (10 → 12); last-updated 2026-06-01
- `wiki/ocean-data-ai.md` — +1 company (4 → 5); last-updated 2026-06-01

## Discovery Sources
- **TechCrunch / ventureburn / smartmaritimenetwork** — Quartermaster coverage
- **a16z announcement** (Erin Price-Wright, Ryan McEntush) — Ulysses investment thesis
- **Tectonic Defense / PR Newswire / Marine Technology News** — Vatn Systems coverage
- **Web searches**: "ocean AI startup 2026 funding Series A marine data", "blue economy startup Series A seed funding 2026 marine AI monitoring"

## Cross-Company Marine Data Patterns (Updated)
- **AUV/swarm signal is dominant in 2026 funding**: 3 of 3 new additions (Ulysses, Vatn) are AUV-platform companies. Combined AUV-focused raised capital in Marine Monitoring & Sensors sector now exceeds **$130M+** when including prior raises
- **Defense-driven AUV demand**: Ulysses (a16z American Dynamism) + Vatn (US Navy + Singapore) confirm that undersea domain is a primary theater of geopolitical competition
- **Distributed sensing over existing assets**: Quartermaster's "vessel-mounted" SmartMast approach contrasts with purpose-built AUVs — but both feed the same "ocean intelligence" demand curve
- **Cost-disruption thesis**: 50x cheaper AUVs (Ulysses) + attritable swarm AUVs (Vatn) + vessel-mounted sensors (Quartermaster) all attack the cost-prohibitive legacy ocean-data-acquisition market
- **Marine data demands reinforced**: every new company needs high-resolution subsea environmental data, telemetry, navigation in comm-denied environments, and AI-processed data products for downstream customers

## Verification
- Completeness check: ✅ PASSED (65 companies, 0 errors, 0 warnings)
- All new companies have full raw/ + metadata/ + wiki/ triples
- All wiki profiles include "Data & Measurement Needs" section
- Sector counts updated and consistent

## Next Steps
Continue daily monitoring. Next VentureWell OEA Fall 2026 cohorts will likely publish in Q3 2026. Funding landscape shows strong momentum in AUV + distributed sensing; expect more defense-funded marine-autonomy companies.
