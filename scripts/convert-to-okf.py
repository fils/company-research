#!/usr/bin/env python3
"""
One-shot migration: company-research LLM wiki → OKF v0.1 Knowledge Bundle.

- Ensures YAML frontmatter with required `type` on every concept document
- Converts repo-root absolute links (/wiki/foo.md) and broken ../ paths to relative
- Generates wiki/index.md, wiki/concepts/index.md, optional wiki/log.md
- Adds local OKF format concept at wiki/concepts/okf-knowledge-bundle.md

Usage:
  python3 scripts/convert-to-okf.py           # apply changes
  python3 scripts/convert-to-okf.py --dry-run # report only
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
WIKI = REPO / "wiki"
SOURCES = REPO / "sources" / "companies.json"
RESERVED = {"index.md", "log.md"}

# Flat sector overview pages at wiki root (not company profiles)
SECTOR_STEMS = {
    "aquaculture",
    "bioprospecting",
    "climate-risk",
    "coastal-risk-infrastructure",
    "marine-monitoring-sensors",
    "maritime-operations-analytics",
    "ocean-carbon-sequestration",
    "ocean-data-ai",
    "offshore-energy",
}

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
MD_LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")
H1_RE = re.compile(r"^#\s+(.+)$", re.M)
SECTOR_LINE_RE = re.compile(r"(?m)^\*\*Sector\*\*:\s*(.+)$")
OFFICIAL_SITE_RE = re.compile(r"(?m)^\*\*Official Site\*\*:\s*(\S+)")
LAST_UPDATED_RE = re.compile(
    r"(?mi)(?:\*[Ll]ast updated|[Ll]ast [Uu]pdated):\s*(\d{4}-\d{2}-\d{2})"
)
URL_RE = re.compile(r"https?://[^\s\)\]\"']+")


def slugify(name: str) -> str:
    slug = name.lower()
    slug = slug.replace("ø", "o").replace("æ", "ae").replace("å", "a")
    slug = slug.replace("ü", "u").replace("é", "e").replace("è", "e")
    slug = re.sub(r"[^a-z0-9-]", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def load_company_index() -> dict[str, dict[str, Any]]:
    """stem -> company record from companies.json."""
    if not SOURCES.exists():
        return {}
    companies = json.loads(SOURCES.read_text(encoding="utf-8"))
    out: dict[str, dict[str, Any]] = {}
    for c in companies:
        out[slugify(c["name"])] = c
    return out


def load_yaml_frontmatter(text: str) -> tuple[dict[str, Any] | None, str]:
    if not text.startswith("---"):
        return None, text
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, text
    raw_fm = "".join(lines[1:end])
    body = "".join(lines[end + 1 :])
    try:
        data = yaml.safe_load(raw_fm) or {}
        if not isinstance(data, dict):
            data = {"_raw": data}
    except yaml.YAMLError:
        data = {}
    return data, body


def dump_frontmatter(data: dict[str, Any]) -> str:
    ordered: dict[str, Any] = {}
    for key in (
        "type",
        "title",
        "description",
        "resource",
        "tags",
        "timestamp",
        "date",
        "sector",
        "okf_version",
    ):
        if key in data and data[key] is not None:
            ordered[key] = data[key]
    for key, val in data.items():
        if key not in ordered and val is not None:
            ordered[key] = val
    dumped = yaml.safe_dump(
        ordered,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ).strip()
    return f"---\n{dumped}\n---\n"


def infer_type(path: Path) -> str:
    rel = path.relative_to(WIKI)
    if rel.parts[0] == "concepts":
        return "Concept"
    if path.stem in SECTOR_STEMS:
        return "Sector"
    return "Company"


def extract_title(fm: dict[str, Any], body: str, path: Path) -> str:
    if fm.get("title"):
        return str(fm["title"]).strip()
    # Legacy jupiter-style frontmatter used Company: key
    if fm.get("Company"):
        return str(fm["Company"]).strip()
    m = H1_RE.search(body)
    if m:
        return m.group(1).strip()
    return path.stem.replace("-", " ").title()


def extract_description(fm: dict[str, Any], body: str, company: dict | None) -> str | None:
    existing = fm.get("description")
    if existing:
        desc = str(existing).strip()
        if desc and "[[" not in desc and len(desc) >= 12:
            return desc

    if company and company.get("notes"):
        notes = str(company["notes"]).strip()
        if notes:
            if ". " in notes:
                notes = notes.split(". ")[0] + "."
            if len(notes) > 220:
                notes = notes[:217].rstrip() + "..."
            return notes

    # First useful prose after H1 / bold meta
    lines = body.splitlines()
    buf: list[str] = []
    started = False
    for line in lines:
        s = line.strip()
        if not s:
            if started and buf:
                break
            continue
        if s.startswith("#") or s.startswith("|") or s.startswith("!") or s == "---":
            if started and buf:
                break
            continue
        if re.match(r"^\*\*[^*]+:\*\*", s):
            continue
        if s.startswith("**") and s.endswith("**") and len(s) < 80:
            continue
        if s.startswith("http") or s.startswith("- http"):
            continue
        if s.startswith("###"):
            continue
        # Skip section-only headings like "## Overview"
        if s.startswith("##"):
            continue
        started = True
        buf.append(s)
        if len(" ".join(buf)) > 160:
            break
    if not buf:
        return None
    desc = " ".join(buf)
    if ". " in desc:
        desc = desc.split(". ")[0] + "."
    if len(desc) > 220:
        desc = desc[:217].rstrip() + "..."
    return desc


def plain_description(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_resource(
    fm: dict[str, Any], body: str, company: dict | None
) -> str | None:
    if fm.get("resource"):
        return str(fm["resource"]).strip()
    # Legacy Official Site key in jupiter frontmatter
    if fm.get("Official Site"):
        return str(fm["Official Site"]).strip()
    if company and company.get("url"):
        return str(company["url"]).strip()
    m = OFFICIAL_SITE_RE.search(body)
    if m:
        return m.group(1).strip()
    return None


def extract_sector(
    fm: dict[str, Any], body: str, path: Path, company: dict | None
) -> str | None:
    if fm.get("sector"):
        return str(fm["sector"]).strip()
    if fm.get("Sector"):
        return str(fm["Sector"]).strip()
    if company and company.get("sector"):
        return str(company["sector"]).strip()
    m = SECTOR_LINE_RE.search(body)
    if m:
        return m.group(1).strip()
    if path.stem in SECTOR_STEMS:
        # Humanize stem for sector pages
        return path.stem.replace("-", " ").title()
    return None


def extract_timestamp(
    fm: dict[str, Any], body: str, company: dict | None
) -> str | None:
    if fm.get("timestamp"):
        return str(fm["timestamp"])
    for key in ("date", "Last Updated", "last_updated"):
        if fm.get(key):
            s = str(fm[key])[:10]
            if re.match(r"\d{4}-\d{2}-\d{2}", s):
                return f"{s}T00:00:00Z"
    m = LAST_UPDATED_RE.search(body)
    if m:
        return f"{m.group(1)}T00:00:00Z"
    if company and company.get("last_updated"):
        s = str(company["last_updated"])[:10]
        if re.match(r"\d{4}-\d{2}-\d{2}", s):
            return f"{s}T00:00:00Z"
    return None


def normalize_md_links(body: str, source: Path) -> tuple[str, int]:
    """
    Rewrite absolute /wiki/... and broken ../ paths to relative links
    that resolve from the source file. Count rewrites.
    """
    rewrites = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal rewrites
        text, url = m.group(1), m.group(2).strip()
        title_part = ""
        # optional "url title"
        if " " in url and not url.startswith("<"):
            url, rest = url.split(" ", 1)
            title_part = " " + rest
        url = url.strip("<>")
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url) or url.startswith("#"):
            return m.group(0)

        new_url = url
        # Repo-root absolute style: /wiki/foo.md → relative to source
        if url.startswith("/wiki/"):
            target = WIKI / url[len("/wiki/") :]
            new_url = os.path.relpath(str(target), str(source.parent)).replace("\\", "/")
            rewrites += 1
        elif url.startswith("/"):
            # Other absolute paths under repo
            target = REPO / url.lstrip("/")
            if target.exists() or url.endswith(".md"):
                new_url = os.path.relpath(str(target), str(source.parent)).replace(
                    "\\", "/"
                )
                rewrites += 1
        elif url.startswith("../"):
            # Fix paths that incorrectly leave wiki/ when target is still in wiki
            resolved = (source.parent / url.split("#")[0]).resolve()
            try:
                resolved.relative_to(REPO.resolve())
            except ValueError:
                return m.group(0)
            # If ../ocean-carbon... was meant as sibling in wiki/
            if not resolved.exists():
                # Try stripping leading ../ segments that point outside wiki incorrectly
                stem_path = Path(url.split("#")[0])
                # ../wiki/foo.md or ../foo.md where foo is in wiki/
                candidates = [
                    WIKI / stem_path.name,
                    WIKI / Path(*stem_path.parts[1:]) if len(stem_path.parts) > 1 else None,
                ]
                for cand in candidates:
                    if cand is not None and cand.exists():
                        new_url = os.path.relpath(
                            str(cand), str(source.parent)
                        ).replace("\\", "/")
                        if "#" in url:
                            new_url += "#" + url.split("#", 1)[1]
                        rewrites += 1
                        break
            else:
                # Exists but maybe awkward; normalize to clean relative
                clean = os.path.relpath(str(resolved), str(source.parent)).replace(
                    "\\", "/"
                )
                if "#" in url:
                    clean += "#" + url.split("#", 1)[1]
                if clean != url:
                    new_url = clean
                    rewrites += 1

        if new_url == url:
            return m.group(0)
        return f"[{text}]({new_url}{title_part})"

    return MD_LINK_RE.sub(repl, body), rewrites


def convert_wikilinks(text: str) -> tuple[str, list[str]]:
    """Strip/convert residual [[wikilinks]] (rare in this repo)."""
    unresolved: list[str] = []

    def repl(m: re.Match[str]) -> str:
        raw = m.group(1).strip()
        if raw.lower() == "backlinks":
            return ""
        display = raw
        target = raw
        if "|" in raw:
            target, display = [p.strip() for p in raw.split("|", 1)]
        # Same-directory stem
        cand = WIKI / f"{target}.md"
        if cand.exists():
            return f"[{display}]({cand.name})"
        unresolved.append(raw)
        return display.replace("-", " ")

    return WIKILINK_RE.sub(repl, text), unresolved


def migrate_legacy_fm_keys(fm: dict[str, Any]) -> dict[str, Any]:
    """Map legacy producer keys into OKF fields; keep extras as extensions."""
    mapping = {
        "Company": None,  # becomes title
        "Official Site": "resource",
        "Sector": "sector",
        "Last Updated": "date",
    }
    out = dict(fm)
    for old, new in mapping.items():
        if old in out:
            val = out.pop(old)
            if new and new not in out:
                out[new] = val
    # Drop non-OKF capital keys that are pure display
    return out


def convert_concept_file(
    path: Path,
    companies: dict[str, dict[str, Any]],
    dry_run: bool,
) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    original = text
    fm, body = load_yaml_frontmatter(text)
    if fm is None:
        fm = {}
    else:
        fm = migrate_legacy_fm_keys(fm)

    company = companies.get(path.stem)
    fm["type"] = fm.get("type") or infer_type(path)
    title = extract_title(fm, body, path)
    fm["title"] = title

    new_body, link_rewrites = normalize_md_links(body, path)
    new_body, unresolved = convert_wikilinks(new_body)
    new_body = re.sub(r"[ \t]+\n", "\n", new_body)
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)

    desc = extract_description(fm, new_body, company)
    if desc:
        fm["description"] = plain_description(desc)

    resource = extract_resource(fm, new_body, company)
    if resource:
        fm["resource"] = resource

    sector = extract_sector(fm, new_body, path, company)
    if sector:
        fm["sector"] = sector
        # tags from sector slug
        if not fm.get("tags"):
            tag = re.sub(r"[^a-z0-9]+", "-", sector.lower()).strip("-")
            fm["tags"] = [tag]

    ts = extract_timestamp(fm, new_body, company)
    if ts:
        fm["timestamp"] = ts
        if not fm.get("date"):
            fm["date"] = ts[:10]

    new_text = dump_frontmatter(fm) + (
        new_body if new_body.startswith("\n") else "\n" + new_body
    )
    if not new_text.endswith("\n"):
        new_text += "\n"

    changed = new_text != original
    if changed and not dry_run:
        path.write_text(new_text, encoding="utf-8")

    return {
        "path": str(path.relative_to(REPO)),
        "changed": changed,
        "type": fm["type"],
        "link_rewrites": link_rewrites,
        "unresolved": unresolved,
    }


def read_title_desc(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    fm, body = load_yaml_frontmatter(text)
    fm = fm or {}
    title = str(fm.get("title") or "").strip() or extract_title({}, body, path)
    desc = str(fm.get("description") or "").strip()
    if not desc:
        d = extract_description({}, body, None)
        desc = d or ""
    return title, plain_description(desc)


def write_okf_concept(dry_run: bool) -> str:
    concepts = WIKI / "concepts"
    if not dry_run:
        concepts.mkdir(parents=True, exist_ok=True)
    path = concepts / "okf-knowledge-bundle.md"
    content = """---
type: Concept
title: OKF Knowledge Bundle — Format Rules for this Wiki
description: Local summary of Open Knowledge Format (OKF) v0.1 rules used by the company-research wiki for agents and humans.
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
tags: [okf, format, conformance, agent-workflow]
timestamp: 2026-07-16T00:00:00Z
date: 2026-07-16
---

# OKF Knowledge Bundle — Format Rules for this Wiki

This repository's `wiki/` directory is an **Open Knowledge Format (OKF) v0.1** Knowledge Bundle.

**Authoritative spec:** [OKF SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)

The daily research *workflow* compounds company profiles and sector overviews. The **document format** is OKF — not Obsidian, not bare `[[wikilink]]` markup.

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

```markdown
[Sofar Ocean](../sofar-ocean.md)
[Aquaculture](../aquaculture.md)
```

From a flat company page (same directory):

```markdown
[Aquaculture sector overview](aquaculture.md)
```

**Do not use:**

```markdown
[[sofar-ocean]]
[/wiki/sofar-ocean.md]
```

Absolute bundle-relative paths starting with `/` are OKF-legal when the bundle is the publish root; in this monorepo they break GitHub navigation (`/wiki/...` resolves from the GitHub site root). This project standardizes on **relative** links (§5.2).

## Company profile body conventions

Keep domain content (not OKF-required, but agent contract):

- Near top of body: `**Sector**: ...` and `**Official Site**: https://...`
- **Data & Measurement Needs** section on every company profile
- Cross-link to sector overviews and related companies via relative markdown

## Conformance gate

```bash
python3 scripts/okf-lint.py
```

Hard failures: missing frontmatter, missing `type`, residual `[[wikilinks]]`.

Also run domain checks when useful: `python3 scripts/completeness-check.py`.

## Related

- Bundle entry: [index](../index.md)
- Agent workflow contract: `PLAN.md` (repo root, outside bundle)

# Citations

[1] [Open Knowledge Format (OKF) SPEC v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
"""
    if not dry_run:
        path.write_text(content, encoding="utf-8")
    return str(path.relative_to(REPO))


def generate_concepts_index(dry_run: bool) -> str:
    d = WIKI / "concepts"
    files = sorted(
        [f for f in d.glob("*.md") if f.name not in RESERVED and f.name != "README.md"],
        key=lambda p: p.name,
    )
    lines = [
        "# Concepts",
        "",
        "Progressive disclosure listing for format and meta concepts.",
        "",
    ]
    for f in files:
        title, desc = read_title_desc(f)
        entry = f"* [{title}]({f.name})"
        if desc:
            entry += f" - {desc}"
        lines.append(entry)
    lines.append("")
    out = d / "index.md"
    if not dry_run:
        out.write_text("\n".join(lines), encoding="utf-8")
    return str(out.relative_to(REPO))


def generate_root_index(dry_run: bool) -> str:
    companies: list[Path] = []
    sectors: list[Path] = []
    for f in sorted(WIKI.glob("*.md")):
        if f.name in RESERVED or f.name == "README.md":
            continue
        if f.stem in SECTOR_STEMS:
            sectors.append(f)
        else:
            companies.append(f)

    lines = [
        "---",
        'okf_version: "0.1"',
        "---",
        "",
        "# Company Research Knowledge Bundle",
        "",
        "Agent-maintained knowledge graph of ocean / blue-economy companies: business models, funding, technology, and data & measurement needs.",
        "",
        "## Knowledge Catalog (OKF)",
        "",
        "This directory is an [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) Knowledge Bundle.",
        "",
        f"**Format rules (read first for agents):** [OKF Knowledge Bundle — Format Rules](concepts/okf-knowledge-bundle.md)",
        "",
        "- Required: YAML frontmatter with `type` on every concept document",
        "- Cross-links: **relative markdown only** (OKF §5.2) — works on GitHub; never `[[wikilinks]]`",
        "- Conformance: `python3 scripts/okf-lint.py`",
        "- Workflow contract (outside bundle): repo-root `PLAN.md`",
        "",
        "# Bundle sections",
        "",
        "* [Concepts](concepts/) - Format rules and meta notes",
        "* [Update Log](log.md) - Chronological change history",
        "",
        f"# Sectors ({len(sectors)})",
        "",
    ]
    for f in sectors:
        title, desc = read_title_desc(f)
        entry = f"* [{title}]({f.name})"
        if desc:
            entry += f" - {desc}"
        lines.append(entry)

    lines.append("")
    lines.append(f"# Companies ({len(companies)})")
    lines.append("")
    # Group by sector when available
    by_sector: dict[str, list[Path]] = {}
    for f in companies:
        text = f.read_text(encoding="utf-8")
        fm, _ = load_yaml_frontmatter(text)
        sector = "Uncategorized"
        if fm and fm.get("sector"):
            sector = str(fm["sector"])
        by_sector.setdefault(sector, []).append(f)

    for sector in sorted(by_sector.keys()):
        lines.append(f"## {sector}")
        lines.append("")
        for f in sorted(by_sector[sector], key=lambda p: p.name):
            title, desc = read_title_desc(f)
            entry = f"* [{title}]({f.name})"
            if desc:
                entry += f" - {desc}"
            lines.append(entry)
        lines.append("")

    content = "\n".join(lines)
    if not content.endswith("\n"):
        content += "\n"
    out = WIKI / "index.md"
    if not dry_run:
        out.write_text(content, encoding="utf-8")
    return str(out.relative_to(REPO))


def generate_log(dry_run: bool) -> str:
    today = date.today().isoformat()
    content = f"""# Directory Update Log

## {today}
* **Migration**: Converted `wiki/` to OKF v0.1 Knowledge Bundle (frontmatter `type`, relative markdown links, root `index.md`, local format concept).
* **Tooling**: Added `scripts/okf-lint.py` conformance gate and `scripts/convert-to-okf.py` migrator.
* **Agent contract**: Updated `PLAN.md` so daily runs use OKF format rules (not Obsidian/wikilinks).

## 2026-05-01
* **Update**: URL enforcement for company sources, raw extracts, metadata, and wiki Official Site lines.
* **Initialization**: Company research wiki structure (sources/, raw/, wiki/, metadata/).
"""
    out = WIKI / "log.md"
    if not dry_run:
        out.write_text(content, encoding="utf-8")
    return str(out.relative_to(REPO))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not WIKI.is_dir():
        print("wiki/ not found", file=sys.stderr)
        return 1

    companies = load_company_index()
    results = []
    total_rewrites = 0
    all_unresolved: list[str] = []

    concept_files = sorted(
        f
        for f in WIKI.rglob("*.md")
        if f.name not in RESERVED and f.name != "README.md"
    )
    # Defer concepts/okf until after we write it
    for path in concept_files:
        if path.name == "okf-knowledge-bundle.md":
            continue
        r = convert_concept_file(path, companies, args.dry_run)
        results.append(r)
        total_rewrites += r["link_rewrites"]
        all_unresolved.extend(r["unresolved"])

    okf_path = write_okf_concept(args.dry_run)
    if not args.dry_run:
        # Convert the new concept through same pipeline for consistency
        r = convert_concept_file(WIKI / "concepts" / "okf-knowledge-bundle.md", {}, False)
        results.append(r)

    concepts_index = generate_concepts_index(args.dry_run)
    root_index = generate_root_index(args.dry_run)
    log_path = generate_log(args.dry_run)

    changed = sum(1 for r in results if r["changed"])
    by_type: dict[str, int] = {}
    for r in results:
        by_type[r["type"]] = by_type.get(r["type"], 0) + 1

    print(f"Concepts processed: {len(results)}")
    print(f"Files changed: {changed}")
    print(f"Link rewrites: {total_rewrites}")
    print(f"Unresolved wikilink aliases: {len(all_unresolved)}")
    if all_unresolved:
        for u in sorted(set(all_unresolved))[:20]:
            print(f"  unresolved: {u}")
    print(f"Types: {by_type}")
    print(f"Wrote: {okf_path}, {concepts_index}, {root_index}, {log_path}")
    if args.dry_run:
        print("(dry-run — no files written)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
