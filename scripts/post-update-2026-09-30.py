#!/usr/bin/env python3
"""Post-process updates for Quartermaster + Maritime Robotics metadata/raw."""
from pathlib import Path
import json

REPO = Path(__file__).resolve().parents[1]

# raw quartermaster append
p = REPO / "raw" / "quartermaster.md"
t = p.read_text()
if "$140M" not in t:
    t = t.replace("**Last Updated:** 2026-06-01", "**Last Updated:** 2026-09-30")
    t += """

## Update 2026-09-30 — Series B
**Sources:** https://techcrunch.com/2026/09/28/maritime-intelligence-startup-quartermaster-raises-another-140m/
https://oceannews.com/news/milestones/quartermaster-secures-series-b-to-expand-smartmast-ocean-data-network/

- $140M total: $100M Series B (Insight Partners lead; Overmatch Ventures; First Round, Quiet Capital, Steel Atlas, TMV, BoxGroup, Operator Partners) + $40M Stifel venture debt
- 650+ vessels equipped / 800+ shipped across 25 countries; tens of GB/day per mast; fleet rollouts starting
- Hormuz jamming/spoofing + war-risk insurance narrative; pro-mariner free hardware model
- CEO Neil Sobin; manufacturing capacity doubled
"""
    p.write_text(t)
    print("raw quartermaster updated")
else:
    print("raw quartermaster already updated")

for slug, extra in [
    ("quartermaster", {"funding": "$140M Sep 2026 ($100M Series B + $40M debt)", "lastUpdated": "2026-09-30",
                       "description": "SmartMast vessel-mounted maritime sensing; $140M Sep 2026 Series B+debt; 650+ vessels"}),
    ("maritime-robotics", {"lastUpdated": "2026-09-30"}),
]:
    mp = REPO / "metadata" / f"{slug}.jsonld"
    m = json.loads(mp.read_text())
    m.update(extra)
    mp.write_text(json.dumps(m, indent=2) + "\n")
    print("meta", slug)
