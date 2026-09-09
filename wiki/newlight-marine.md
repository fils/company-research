---
type: Company
title: Newlight Marine
description: Hydrogen-hybrid retrofit for marine diesels; 24% fuel / 28% CO2 cut on 8,500 nm Lomar voyage; $9M seed (lomarlabs, BIRD Energy, Fusion VC, Sep 2026); Alameda CA.
resource: https://www.newlightmarine.com/
tags:
- offshore-energy
timestamp: '2026-09-09T00:00:00Z'
date: '2026-09-09'
sector: Offshore Energy
---

# Newlight Marine

**Sector**: Offshore Energy
**Official Site**: https://www.newlightmarine.com/
**Last Updated**: 2026-09-09

**Focus**: Hydrogen-hybrid retrofit for the existing marine diesel fleet — millisecond-controlled H2 injection that cuts fuel and emissions without replacing engines or drydocking.
**Status**: **$9M seed** (Sep 1 2026); first long-range commercial voyage **8,500 nm Singapore→Ghana** on Lomar bulker with **24% diesel / 28% CO₂** reduction; RINA FAT complete; LOIs claimed for 12 vessels.
**HQ**: Alameda, CA (Newlight Marine Technologies Inc.) — Co-founders Haran Cohen Hillel (CEO) & Evyatar Cohen (Israeli Navy). **Not** the AirCarbon biomaterials company (newlight.com).

## Business Model
Retrofit hardware + controls sold to commercial shipowners: onboard hydrogen supply conditioning, real-time System Controller, and metered injection into existing 2-/4-stroke mains. Install in ~1–2 weeks without drydock; diesel path remains primary so the vessel is never H2-dependent. Monetizes the fact that fuel is ~50–60% of vessel OPEX (claimed up to ~$500k/yr savings on some ships). Strategic alignment with [lomarlabs](https://www.newlightmarine.com/) / Lomar Shipping (test vessel + investor). Complements [Fleetzero](fleetzero.md) (full electrification), [Kvasir Technologies](kvasir-technologies.md) (drop-in biofuel), and [Aloft Systems](aloft-systems.md) (wind propulsion) as a **fifth** near-term decarbonization path for ships already at sea.

## Funding
- **$9M seed** (Sep 1 2026): lomarlabs, BIRD Energy (US DOE + Israel Ministry of Energy joint venture), Undeterred Capital, CiRi Ventures, Fusion VC
- Diligence signal: investor-supplied Lomar bulk carrier for the commercial ocean trial

## Key Technology
- Live engine-state sensing (load, RPM, exhaust temp, combustion pressure, intake pressure) → adaptive H2 flow every piston event
- Automatic isolate/reduce on out-of-range pressure, flow, temperature, fire, or leak; engine continues on diesel
- **Voyage results**: 24% less diesel, 28% lower CO₂, 22% lower CO, 21% lower SO₂ (Lomar 650-ft bulker)
- RINA Factory Acceptance Test (Nov 2025) for two- and four-stroke main engines; Vessel of the Future finalist (SMM 2026)
- Live AIS-tracked installations (e.g., Oslo Trader bulk carrier; Lucy Borchard container)

## Data & Measurement Needs
- **Primary data types**: High-frequency engine telemetry (load, RPM, cylinder pressure, exhaust/intake temps), hydrogen mass-flow and rail pressure, leak/fire safety channels, voyage fuel bunkering logs, AIS positions, emissions factors
- **Key measurements/parameters**: g-fuel/kWh and t-fuel/day vs baseline, CO₂/CO/SO₂ stack factors, H2 consumption per nm, injection timing maps, class-society safety KPIs, install-time and uptime
- **Observation platforms/programs**: On-vessel sensor suite during commercial voyages; RINA FAT benches; multi-vessel rollout telemetry (12-vessel LOI pipeline)
- **Known data gaps**: Multi-engine-make generalization datasets; hydrogen bunkering availability maps by port; long-duration tropical/arctic durability; independent third-party MRV for carbon-accounting buyers
- **Interest in external data services**: Port H2 bunkering infrastructure layers, weather/route optimization ([Sofar Ocean](sofar-ocean.md)), CII/IMO compliance databases, fleet fuel-price benchmarks, classification society digital twins

---

**Cross-links**: [Offshore Energy](offshore-energy.md) · [Fleetzero](fleetzero.md) · [Kvasir Technologies](kvasir-technologies.md) · [Aloft Systems](aloft-systems.md) · [Bluecore Energy](bluecore-energy.md) · [Voltai](voltai.md) · [ShipIn Systems](shipin-systems.md)
