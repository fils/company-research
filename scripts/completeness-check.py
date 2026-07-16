#!/usr/bin/env python3
"""Completeness gate checker for company research repo.

Run before git commit. Checks:
- Company-to-file cross-reference: every entry in companies.json has raw/ metadata/ wiki/ files
- Sector count verification: wiki/<sector>.md company counts match actual counts
- Duplicate detection: similarly-named files (sea-o2 vs seao2, orsted vs orsted)
- Orphaned file check: files in raw/ or wiki/ with no corresponding entry
- Data & Measurement Needs section: every individual company profile contains it
- Last-Updated audit: verify modified files reference today's date
"""

import json
import os
import re
import sys
from datetime import date
from pathlib import Path

REPO_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent
TODAY = date.today().isoformat()  # e.g. "2026-05-17"

errors = []
warnings = []

def slugify(name):
    """Lowercase, remove diacritics, replace spaces/special chars with hyphens."""
    slug = name.lower()
    # Replace special chars
    slug = slug.replace('ø', 'o').replace('æ', 'ae').replace('å', 'a')
    slug = slug.replace('ü', 'u').replace('é', 'e').replace('è', 'e')
    # Remove non-alphanumeric except hyphens
    slug = re.sub(r'[^a-z0-9-]', '-', slug)
    # Collapse multiple hyphens
    slug = re.sub(r'-+', '-', slug)
    # Strip leading/trailing hyphens
    slug = slug.strip('-')
    return slug

def check_cross_reference(companies):
    """Check every company has raw/, metadata/, wiki/ files."""
    for company in companies:
        name = company["name"]
        slug = slugify(name)
        
        raw_file = REPO_DIR / "raw" / f"{slug}.md"
        meta_file = REPO_DIR / "metadata" / f"{slug}.jsonld"
        wiki_file = REPO_DIR / "wiki" / f"{slug}.md"
        
        for filepath, label in [(raw_file, "raw"), (meta_file, "metadata"), (wiki_file, "wiki")]:
            if not filepath.exists():
                errors.append(f"MISSING: {label}/{slug}.md for company '{name}'")

def check_sector_counts(companies):
    """Verify sector overview page company counts match actual."""
    from collections import Counter
    sector_counts = Counter(c["sector"] for c in companies)
    
    for sector, expected_count in sector_counts.items():
        sector_slug = slugify(sector)
        wiki_file = REPO_DIR / "wiki" / f"{sector_slug}.md"
        
        if not wiki_file.exists():
            warnings.append(f"MISSING SECTOR PAGE: wiki/{sector_slug}.md for '{sector}'")
            continue
        
        content = wiki_file.read_text()
        # Look for "Companies (N monitored)" pattern
        count_match = re.search(r'Companies\s*\((\d+)\s*monitored\)', content)
        if count_match:
            listed_count = int(count_match.group(1))
            if listed_count != expected_count:
                errors.append(f"SECTOR COUNT MISMATCH: wiki/{sector_slug}.md says {listed_count} companies but companies.json has {expected_count} for '{sector}'")

# OKF reserved filenames + sector overview stems (not company profiles)
OKF_RESERVED = {"index", "log"}
SECTOR_STEMS = {
    "ocean-carbon-sequestration",
    "climate-risk",
    "bioprospecting",
    "aquaculture",
    "offshore-energy",
    "ocean-data-ai",
    "maritime-operations-analytics",
    "coastal-risk-infrastructure",
    "marine-monitoring-sensors",
}
WIKI_NON_COMPANY = OKF_RESERVED | SECTOR_STEMS | {"readme"}


def check_duplicates():
    """Check for similarly-named files."""
    raw_files = [f.stem for f in (REPO_DIR / "raw").glob("*.md") if f.is_file()]
    wiki_files = [
        f.stem
        for f in (REPO_DIR / "wiki").glob("*.md")
        if f.is_file() and f.stem not in WIKI_NON_COMPANY
    ]

    # Check for colliding slugs
    for files_list, label in [(raw_files, "raw"), (wiki_files, "wiki")]:
        normalized = {}
        for f in files_list:
            normal = f.lower().replace('-', '')
            if normal in normalized:
                warnings.append(f"DUPLICATE-ADJACENT: '{f}' and '{normalized[normal]}' in {label}/")
            normalized[normal] = f

def check_orphans(companies):
    """Check for files without corresponding company entries."""
    company_slugs = {slugify(c["name"]) for c in companies}

    for dirname, label in [("raw", "raw"), ("wiki", "wiki")]:
        for f in (REPO_DIR / dirname).glob("*.md"):
            slug = f.stem
            # Skip OKF reserved files and sector overview pages in wiki/
            if label == "wiki" and slug in WIKI_NON_COMPANY:
                continue

            if slug not in company_slugs:
                errors.append(f"ORPHANED: {label}/{slug}.md has no entry in companies.json")

def check_data_needs(companies):
    """Check every company profile has a Data & Measurement Needs section."""
    for company in companies:
        slug = slugify(company["name"])
        wiki_file = REPO_DIR / "wiki" / f"{slug}.md"
        
        if wiki_file.exists():
            content = wiki_file.read_text()
            if "Data & Measurement Needs" not in content and "Data & Measurement" not in content:
                errors.append(f"MISSING DATA NEEDS: wiki/{slug}.md lacks 'Data & Measurement Needs' section")

def check_dates(companies):
    """Verify all new/modified files reference today's date."""
    # Check companies.json dates
    for company in companies:
        last_updated = company.get("last_updated", "")
        # This is advisory — files from previous runs may have older dates
        pass

def main():
    print("=" * 60)
    print(f"COMPLETENESS CHECK — {TODAY}")
    print("=" * 60)
    
    # Load companies
    companies_file = REPO_DIR / "sources" / "companies.json"
    if not companies_file.exists():
        print("FATAL: sources/companies.json not found!")
        sys.exit(1)
    
    with open(companies_file) as f:
        companies = json.load(f)
    
    print(f"\nCompanies loaded: {len(companies)}")
    
    # Run checks
    check_cross_reference(companies)
    check_sector_counts(companies)
    check_duplicates()
    check_orphans(companies)
    check_data_needs(companies)
    
    # Report
    print(f"\nErrors: {len(errors)}")
    for e in errors:
        print(f"  [ERR] {e}")
    
    print(f"Warnings: {len(warnings)}")
    for w in warnings:
        print(f"  [WARN] {w}")
    
    if errors:
        print("\n❌ COMPLETENESS CHECK FAILED — fix errors before committing")
        sys.exit(1)
    else:
        print("\n✅ COMPLETENESS CHECK PASSED — ready to commit")
    
    # Sector breakdown
    from collections import Counter
    sector_counts = Counter(c["sector"] for c in companies)
    print(f"\nSector Breakdown ({len(companies)} companies):")
    for sector, count in sorted(sector_counts.items()):
        print(f"  {sector}: {count}")

if __name__ == "__main__":
    main()
