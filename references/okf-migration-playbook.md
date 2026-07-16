# OKF Migration Playbook

Reusable guidance for converting a Karpathy-style / Obsidian LLM wiki repository into an **Open Knowledge Format (OKF) v0.1** Knowledge Bundle, and for updating the agent `PLAN.md` so daily Hermes/agent runs stay format-aligned.

Based on the migration performed on the **skill-bundles** research wiki (2026-07-16).

**Authoritative OKF spec:**  
https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md

---

## 1. Copy-paste agent prompt (full migration)

Use this as the task prompt for an agent (or human) in a target repository.

```
You are migrating this repository’s LLM-maintained markdown wiki from a
Karpathy / Obsidian-style knowledge base into Open Knowledge Format (OKF) v0.1.

## Spec (authoritative)
https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md

## Goals
1. Make the knowledge tree an OKF-conformant Knowledge Bundle.
2. Preserve research content and agent daily-loop intent.
3. Use relative markdown links that work on GitHub AND are OKF-legal (§5.2).
4. Update agent workflow docs (PLAN.md / equivalent) so the agent never
   reintroduces Obsidian [[wikilinks]] or skips required frontmatter.
5. Add a lint gate the agent must run after every write day.

## Bundle root decision
- Prefer treating the existing wiki directory as the bundle root
  (e.g. wiki/, knowledge/, notes/). Do NOT require moving raw/ingestion
  folders into the bundle.
- Concept ID = path under the bundle root without .md
  (e.g. examples/foo → examples/foo.md).
- raw/, scripts/, PLAN.md, resources/ stay outside the bundle unless the
  repo already is pure knowledge-only.

## Link policy (critical)
- Convert ALL [[wikilinks]] / [[target|alias]] to standard markdown links.
- Use RELATIVE paths only, e.g. [Title](../examples/foo.md).
- Do NOT use absolute bundle-root links starting with / while the bundle
  lives as a subdirectory of a monorepo (those break GitHub navigation).
  Relative links are fully OKF-conformant (SPEC §5.2) and work on GitHub.
- Strip intentional lint markers like [[backlinks]].
- Fix known alias stems to real files when possible; otherwise leave plain text
  or external URLs (OKF consumers tolerate broken links, but clean is better).
- Path-like links into raw/ should be corrected to real relative paths from
  the source file (e.g. ../../raw/YYYY-MM-DD/file.md).

## Frontmatter policy
- Every non-reserved concept .md MUST have YAML frontmatter with required:
    type: <short descriptive string>
- Recommended: title, description, resource, tags, timestamp (ISO 8601).
- Preserve existing producer fields as extensions (sources, rating, etc.).
- Infer type from directory (customize per repo), e.g.:
    examples/ → Skill Bundle Example (or domain-specific)
    concepts/ → Concept
    papers/   → Paper
    tools/    → Tool
    daily-digests/ or digests/ → Daily Digest
    qa/ → Q&A
    root catalog → Publication
    metrics → Metrics
- If no frontmatter: create from first H1 + path inference.
- If frontmatter exists: add type; map date → timestamp when possible;
  re-derive weak/placeholder descriptions.
- Sanitize residual [[wikilinks]] inside frontmatter string fields
  (especially description).

## Reserved files (OKF §3.1)
- index.md — progressive disclosure listings; NO concept frontmatter.
  Bundle-root index.md MAY have only: okf_version: "0.1"
- log.md — optional chronological history (## YYYY-MM-DD entries, newest first).
- Do not use index.md / log.md as concept documents.

## Indexes
- Ensure bundle-root index.md exists with okf_version and sectioned catalogs.
- Generate index.md in each subdirectory listing child concepts as:
    * [Title](file.md) - short description from frontmatter
- If README.md was used as a dir listing, point it at index.md or fold it in.

## Tooling to add
1. scripts/okf-lint.py (or equivalent) that hard-fails on:
   - missing/unparseable frontmatter on concepts
   - missing non-empty `type`
   - residual [[wikilinks]] outside fenced/inline code
   Soft-check: broken relative links, missing title/description,
   absolute /links in monorepo layout.
2. Optional scripts/convert-to-okf.py one-shot migrator:
   - stem→path index for unique filenames
   - frontmatter ensure + wikilink rewrite + index/log generation
3. Deprecate Obsidian wikilink linters: make them delegate to okf-lint
   or document “do not use in daily loop.”

## Agent workflow docs (PLAN.md or equivalent) — mandatory hardening
Update the daily agent contract so format cannot drift:

1. TOP of plan: authoritative “Document format” section:
   - wiki is OKF v0.1; link SPEC
   - required type frontmatter
   - relative markdown links only; never [[wikilinks]]
   - lint command: python3 scripts/okf-lint.py only
   - ignore dated wikilink-lint-*.py scripts
   - raw/ may have any notes; do not copy wikilink style into wiki/

2. Separate “Workflow inspiration” (Karpathy daily compound loop, NORA, etc.)
   from document format. Explicitly: format is OKF, not Obsidian.

3. Remove phrases like “Obsidian-ready”, “use wikilinks heavily”,
   “proper wikilinks”, “backlink density” as format requirements.
   Prefer “cross-link density” via relative markdown.

4. Phase that writes wiki pages must require:
   - OKF frontmatter with type
   - relative markdown cross-links
   - update relevant index.md files
   - post-write: okf-lint.py

5. Secondary prompts (bundle documentation, pattern synthesis, bootstrap)
   must also include OKF frontmatter + relative link rules so they cannot
   undercut the main phase prompt.

6. Phase 3/4 “proper links” / generic “lint” → name relative MD + okf-lint.

7. Risks section: format drift, contamination (raw vs wiki).

8. Bump plan version/date.

## Local OKF reference concept (recommended)
Add a short concept doc inside the bundle, e.g.:
  <bundle>/concepts/okf-knowledge-bundle.md
covering: bundle root, types, reserved files, link policy, lint gate,
link to SPEC. Link it from root index.md.

## Out of scope (unless requested)
- Moving raw/ into the bundle
- Rewriting body content into data-catalog sections (# Schema, etc.)
- Absolute /bundle-root links (only if packaging bare bundle as publish root)
- Full citation-section rewrite of every page (optional soft hygiene)

## Verification checklist
- [ ] python3 scripts/okf-lint.py → PASS (0 hard failures)
- [ ] No residual [[wikilinks]] in wiki bodies outside code fences
- [ ] All concept files have type frontmatter
- [ ] Root index has okf_version: "0.1"
- [ ] Subdir index.md files exist and list children
- [ ] Sample relative links resolve across directories
- [ ] PLAN.md (or agent contract) has no positive instruction to use
      Obsidian/wikilink format
- [ ] Karpathy/Obsidian mentions are workflow history only, paired with
      “format is OKF”

## Delivery
Implement conversion + tooling + plan/docs updates. Do not force-push.
Summarize counts: files converted, links rewritten, unresolved aliases.
```

---

## 2. What we changed (scope checklist)

Use this as a review checklist when migrating another repo.

### A. Content / structure (wiki tree)

| Change | Why |
|--------|-----|
| Required YAML frontmatter + `type` on every concept | OKF §4.1 / §9 |
| Keep domain fields as extensions | OKF allows producer keys |
| `[[wikilinks]]` → relative `[text](path.md)` | OKF §5.2 + GitHub |
| Alias map for known broken stems | Clean graph |
| Remove `[[backlinks]]` markers | Not concepts |
| Root `index.md` + `okf_version: "0.1"` | OKF §6 / §11 |
| Subdirectory `index.md` listings | Progressive disclosure |
| Optional `log.md` from digests/history | OKF §7 |
| Optional local `concepts/okf-knowledge-bundle.md` | Agent-readable rules without fetching GitHub |

### B. Link strategy decision record

| Option | OKF | GitHub monorepo | Recommendation |
|--------|-----|-----------------|----------------|
| Relative `../examples/foo.md` | ✅ §5.2 | ✅ | **Use this** |
| Absolute `/examples/foo.md` (bundle root) | ✅ §5.1 | ❌ resolves to repo root | Avoid unless packaging bare bundle |
| Absolute `/wiki/examples/foo.md` | ❌ wrong base for OKF | ✅ | Avoid for OKF alignment |

### C. Tooling

| Artifact | Role |
|----------|------|
| `scripts/okf-lint.py` | Daily conformance gate |
| `scripts/convert-to-okf.py` | One-shot / re-run migration |
| Deprecate wikilink linters | Prevent agent regression |

Lint should strip fenced/inline code before detecting residual `[[wikilinks]]` so docs can show anti-examples.

### D. Agent contract (`PLAN.md`) hardening

| Location | Requirement |
|----------|-------------|
| Top of plan | Authoritative Document format (OKF + SPEC URL + lint) |
| Inspiration list | Karpathy = workflow only; format = OKF |
| Directory tree comment | Not “Obsidian-ready” |
| Write phase prompt | type + relative links + no wikilinks + index updates |
| Secondary prompts | Same format rules |
| Lint phases | Explicit `okf-lint.py` only |
| Metrics language | Cross-link density, not backlink density |
| Version bump | Record OKF adoption |

### E. Docs that should mention OKF

1. `PLAN.md` top + write phases  
2. Bundle root `index.md`  
3. Local concept `okf-knowledge-bundle.md`  
4. Root `README.md`  
5. `scripts/README.md`  

---

## 3. Suggested type vocabulary (customize per domain)

OKF types are **not** centrally registered. Pick descriptive strings:

```
Concept
Paper
Tool
Daily Digest
Q&A
Publication
Metrics
Reference
Playbook
# domain examples:
Skill Bundle Example
Dataset
API Endpoint
BigQuery Table
```

---

## 4. Minimal frontmatter templates

### Concept / example

```yaml
---
type: Concept
title: Human readable title
description: One sentence summary for indexes and search.
resource: https://example.com/canonical  # optional
tags: [optional, tags]
timestamp: 2026-07-16T00:00:00Z
# producer extensions below
date: 2026-07-16
sources: []
---
```

### Root index only

```yaml
---
okf_version: "0.1"
---
```

### Subdir index

No frontmatter. Body:

```markdown
# Section name

* [Title](file.md) - short description
```

---

## 5. Short re-audit prompt (after migration)

```
Audit this repo for OKF v0.1 readiness and agent format drift.

1. Run python3 scripts/okf-lint.py (or report if missing).
2. Search PLAN.md / agent docs for positive instructions to use
   Obsidian, [[wikilinks]], “Obsidian-ready”, or “use wikilinks heavily”.
3. Confirm Karpathy mentions are workflow-only, not format.
4. Confirm wiki uses relative markdown links and required type frontmatter.
5. List remaining risks and fix any that would make a daily agent
   regenerate non-OKF pages.

Spec: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
```

---

## 6. Optional: package bare bundle later

If you later publish **only** the wiki directory as a tarball/submodule:

- Absolute OKF links (`/examples/foo.md`) become attractive for move-stability.
- Until then, keep relative links for monorepo + GitHub dual use.

---

## 7. Reference implementation

This repository (`skill-bundles`) after migration:

- Bundle: `wiki/`
- Lint: `scripts/okf-lint.py`
- Migrator: `scripts/convert-to-okf.py`
- Local rules: `wiki/concepts/okf-knowledge-bundle.md`
- Agent contract: `PLAN.md` v2.0
- This playbook: `references/okf-migration-playbook.md`
