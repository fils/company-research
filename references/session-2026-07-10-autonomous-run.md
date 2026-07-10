# Autonomous Run — 2026-07-10

## Pre-run
- Working tree clean; branch master up to date with origin
- Completeness check: 0 errors, 1 warning (missing wiki/coastal-risk-intelligence.md)
- Companies loaded: 69 (with duplicate Coastal Measures across two sectors)

## Phase 1 — Sources
- Discovery searches: ocean tech Series A/funding 2026, AUV/USV funding, mCDR funding, marine robotics
- **VentureWell OEA Spring 2026 exhausted** — weighted defense-tech press + AlleyWatch/Crunchbase large rounds
- High-signal finds:
  1. **HavocAI** — $100M Series A (May 2026), ~$200M total collaborative autonomy
  2. **Seasats** — $20M Series A + >$100M gov contracts; long-endurance sUSVs
  3. **Bedrock Ocean Exploration** — $25M Series A-2; seafloor AUV mapping
- Fixed: removed **Coastal Measures** duplicate under Coastal Risk & Intelligence (kept Ocean Data & AI entry; merged Maine Angels $260K note)
- Net companies: 69 − 1 + 3 = **71**

## Phases 2–4
- Ingested homepages/press for all three new companies
- Wrote raw/, metadata/ JSON-LD, wiki/ profiles with Data & Measurement Needs
- Updated `wiki/marine-monitoring-sensors.md` count to 17

## Completeness
- Run `python3 scripts/completeness-check.py` after this script

## Focus themes
- Business models, funding, marine data needs emphasized for all new profiles
