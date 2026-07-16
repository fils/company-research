---
type: Concept
title: OKF Knowledge Bundle — Format Rules for this Wiki
description: Local summary of Open Knowledge Format (OKF) v0.1 rules used by the company-research wiki for agents and humans.
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
tags:
- okf
- format
- conformance
- agent-workflow
timestamp: '2026-07-16 00:00:00+00:00'
date: 2026-07-16
---

# OKF Knowledge Bundle — Format Rules for this Wiki

This repository's `wiki/` directory is an **Open Knowledge Format (OKF) v0.1** Knowledge Bundle.

**Authoritative spec:** [OKF SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)

The daily research *workflow* compounds company profiles and sector overviews. The **document format** is OKF — not Obsidian, not bare `wikilink` markup.

## Bundle root

- Bundle root: `wiki/`
- Concept ID: path under `wiki/` without `.md` (e.g. `sofar-ocean`, `concepts/okf-knowledge-bundle`)
- Outside the bundle: `raw/`, `metadata/`, `sources/`, `scripts/`, `PLAN.md`, `resources/`, `references/`

## Required frontmatter (every concept)

Every non-reserved `.md` file under `wiki/` must start with YAML frontmatter including:

```yaml
---
type: Company                 # required
title: Sofar Ocean            # recommended
description: One sentence     # recommended
resource: https://...         # official homepage when known
tags: [ocean-data-ai]
timestamp: 2026-07-16T00:00:00Z
sector: Ocean Data & AI       # producer extension
date: 2026-07-16
---
```

### Types used in this bundle

| `type` | Use |
|--------|-----|
| `Company` | Individual company profiles at wiki root |
| `Sector` | Sector overview pages (e.g. `aquaculture.md`) |
| `Concept` | Format/meta notes under `concepts/` |

## Reserved filenames (OKF §3.1)

| File | Role |
|------|------|
| `index.md` | Progressive disclosure listing (no concept `type`; root may have `okf_version` only) |
| `log.md` | Chronological update history |

## Cross-linking (OKF §5)

**Use relative markdown links** so links work on GitHub and in OKF consumers:

- From `concepts/`: [Sofar Ocean](../sofar-ocean.md), [Aquaculture](../aquaculture.md)
- From a wiki-root company page: link to sibling sector files with a same-directory relative path (for example `aquaculture.md`).

**Do not use** Obsidian double-bracket wikilinks, or monorepo-absolute paths that start with `/wiki/` (those break GitHub navigation when the bundle is a subdirectory).

Absolute bundle-relative paths starting with `/` are OKF-legal when the bundle is the publish root; in this monorepo they break GitHub navigation. This project standardizes on **relative** links (§5.2).

## Company profile body conventions

Keep domain content (not OKF-required, but agent contract):

- Near top of body: `**Sector**: ...` and `**Official Site**: https://...`
- **Data & Measurement Needs** section on every company profile
- Cross-link to sector overviews and related companies via relative markdown

## Conformance gate

```bash
python3 scripts/okf-lint.py
```

Hard failures: missing frontmatter, missing `type`, residual `wikilinks`.

Also run domain checks when useful: `python3 scripts/completeness-check.py`.

## Related

- Bundle entry: [index](../index.md)
- Agent workflow contract: `PLAN.md` (repo root, outside bundle)

# Citations

[1] [Open Knowledge Format (OKF) SPEC v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
