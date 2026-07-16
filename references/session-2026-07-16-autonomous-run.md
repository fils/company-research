# Autonomous Run — 2026-07-16

## Pre-run
- Working tree clean; last commit: 6d70688 (Daily update 2026-07-15)
- Completeness check: 0 errors, 0 warnings (88 companies)
- 9 sectors tracked

## Phase 1 — Sources (Discovery)
- **Primary discovery source**: NewMarketPitch.com Ocean Tech Funding Analysis (updated 13 Jul 2026) — 23 deals / $2.40B across 22 pure-play ocean tech companies (Aug 2025–Jul 2026). Cross-referenced against existing 88 companies; harvested remaining untracked high-signal names.
- Additional searches: Carbon Herald / ocean CDR funding, aquaculture AI funding, The Robot Report maritime, defense ASV, EyeROV/Seaber/Biosort/Clear Robotics/Sizable/Voltai official sites
- High-signal finds (5 new companies):
  1. **Biosort** — NOK 100M+ (~$10.4M, Feb 2026); individual-based sea lice control + FishID AI; Grieg Kapital / Hatch Blue / IVC / Farvatn; Norway; iFarm/Cermaq heritage → **Aquaculture**
  2. **Sizable Energy** — $8M seed (Oct 2025, Playground Global); gigawatt-scale ocean pumped hydro LDES with brine → **Offshore Energy**
  3. **Clear Robotics** — $1.75M seed (Jun 2026, Katapult Ocean); all-electric AI USVs for waste/hyacinth/survey; ~26–27 vessel fleet Asia/Middle East → **Marine Monitoring & Sensors**
  4. **Seaber** — ~$2M seed (Oct 2025); French micro-AUVs YUCO (science) + MARVEL (defense/MCM) → **Marine Monitoring & Sensors**
  5. **Voltai** — CAD $1.83M pre-seed (Oct 2025, Invest Nova Scotia); onboard wave/motion energy harvesting without added drag → **Offshore Energy**

### Considered but not added this run
- **Aquapulse** (India shrimp value-chain, ₹25–45 Cr Series A) — more marketplace/processing than marine data/MRV core; lower marine-data signal than AquaExchange already tracked
- **EyeROV** (India ROV/USV, ₹13 Cr) — funding figures inconsistent across sources; defer until cleaner signal
- **Maritime Fusion** ($4.5M YC) — fusion reactors for maritime; adjacent but not core marine data
- **WellFish Tech** — blood diagnostics; older rounds, incremental signal

## Phases 2–4
- Ingested homepages via web_extract for all 5 companies (+ Biosort technology & funding pages)
- Wrote raw/, metadata/ JSON-LD, wiki/ profiles with Data & Measurement Needs sections
- Updated sector wiki pages: Aquaculture 17→18, Offshore Energy 10→12, Marine Monitoring 21→23
- All wiki profiles include standardized Data & Measurement Needs sections

## Completeness
- Ran `python3 scripts/completeness-check.py` after sector count fixes
- Target: 93 companies, 0 errors

## New business model patterns discovered
1. **Individual-ID + intervention loop** (Biosort): FishID closes the loop from observation to early lice removal at the individual fish — distinct from monitoring-only CV (Aquabyte/Tidal)
2. **Ocean pumped-hydro LDES** (Sizable Energy): Brine seabed + floating reservoirs firm floating wind/PV at GW scale — storage not generation
3. **Environmental-service USV fleet** (Clear Robotics): Zero-emission cleanup/survey USVs sold as rental/services with waste-mass data co-products — distinct from defense ASV primes
4. **Micro-AUV fleet economics** (Seaber): Single-person-deploy ~10 kg AUVs with diverse science/defense payloads — fleets of many small units vs few large primes
5. **Vessel-mounted wave harvest without drag** (Voltai): Retrofit motion-to-power as fourth maritime decarbonization pathway (alongside batteries, drop-in biofuel, hull grooming)

## Cross-company marine data patterns
- **Maritime decarbonization multi-pathway now 5-deep**: Fleetzero (electrification), Kvasir (biofuel), Hullbot (drag), Voltai (onboard generation), Sizable (offshore LDES firming renewables that power ports/ships)
- **Aquaculture sensing → action stack**: Innovasea sensors → Aquabyte/Tidal/NeuralX vision → BiOceanOr forecasts → Biosort individual intervention
- **AUV cost curve stratification**: Defense primes (Vatn/Ulysses) → survey (Bedrock) → micro fleet (Seaber/Sunfish)
- **Katapult Ocean repeat investor**: Hullbot + Clear Robotics — European/APAC ocean robotics thesis

## Discovery source quality assessment
- **NewMarketPitch.com**: Still highest-yield single page; remaining untracked names from Jul 13 table fully harvested for high-signal tiers
- **The Robot Report**: No new companies beyond already-tracked defense ASV set
- **Carbon Herald**: No new pure-play ocean CDR equity rounds this cycle

## Commit
- Pending after completeness gate
