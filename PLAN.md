# Company Research Daily Workflow (Phases 1–5)

Run from workdir `~/projects/company-research`.

**Document format (authoritative):** `wiki/` is an **Open Knowledge Format (OKF) v0.1** Knowledge Bundle.

- Spec: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
- Local summary: `wiki/concepts/okf-knowledge-bundle.md`
- Conformance gate: `python3 scripts/okf-lint.py` (only format lint for the wiki)
- Every concept `.md` needs YAML frontmatter with required `type` (`Company`, `Sector`, or `Concept`)
- Cross-links: **relative standard markdown only** — e.g. `[Sofar Ocean](sofar-ocean.md)`, `[Aquaculture](aquaculture.md)`
- **Never** use Obsidian-style `[[wikilink]]` syntax in `wiki/`
- **Never** use repo-absolute `/wiki/...` links (they break GitHub browsing); use relative paths
- `raw/` may contain any notes; do **not** copy non-OKF link style into `wiki/`
- After every write day: run `python3 scripts/okf-lint.py` (must PASS / exit 0)

**Workflow inspiration (not document format):** compound daily agent research loop over a markdown knowledge base. The **document format is OKF**, not Obsidian.

**Plan version:** 2.0 — 2026-07-16 (OKF adoption)

---

## Phase 1: Update Sources

- `read_file('sources/companies.json')` or create if missing. Every entry MUST include:
  - `"sector"`
  - `"name"`
  - `"url"` (official homepage – **required**)
  - `"notes"`
  - `"last_updated"`
- Example:
  ```json
  {
    "sector": "Ocean Carbon Sequestration",
    "name": "Ebb Carbon",
    "url": "https://www.ebbcarbon.com/",
    "notes": "Electrochemical CDR from brine",
    "last_updated": "2026-05-01"
  }
  ```

- web searches (use web search and scraping tools along with any other appropriate tool):
   - `"ocean AI" OR "marine AI" OR "AI ocean data" OR "ocean tech AI" OR "ocean mapping AI" (startup OR company OR "AI startup" OR firm OR "ocean intelligence")`
   - `("blue economy" OR "ocean tech" OR "marine tech" OR "blue tech") AI (startup OR company OR accelerator OR "AI startup"`
   - `AI (aquaculture OR fisheries OR "illegal fishing" OR "ocean mapping" OR "underwater infrastructure" OR "marine monitoring") (startup OR company)`
   - `"ocean data intelligence" OR "AI-powered ocean" OR "AI oceanography" OR "ocean data platform" OR "AI ocean data" (company OR startup OR "data platform" OR intelligence)`
   - `(NOAA OR Copernicus OR Esri OR "public ocean data" OR "ocean data repository" OR EMODnet) AI (partner OR partnership OR startup OR company OR "AI project" OR "AI-ready")`
   - `maritime AI" OR "shipping AI" OR "vessel AI" OR "ocean AI" (startup OR company) (predictive OR analytics OR intelligence)`
   - Specific follow-ups from yesterday's gaps
   - `num_results=20` minimum; sort by recency/relevance.


## Phase 2: Ingest Raw Data

For each source in companies.json:
- Extract `url` from the JSON entry
- Run `web_extract(urls=[company.url])` → save as `raw/<company-slug>.md`
- In the generated `.md` file, **first line or a dedicated header** must contain the source URL, for example:
  ```markdown
  # Company Name – Raw Web Extract
  **Source:** https://company-url.com/
  ```
- browser_navigate if JS-heavy; snapshot/extract business model/funding/about.

## Phase 3: Analyze & Extract

For each raw/ file:
- Extract: business model, funding (amounts/rounds/investors), key tech, contacts.
- **Data, Measurements & Observations focus**:
  - Types of data the company works with or needs (sensor streams, satellite imagery, model outputs, genomic sequences, acoustic data, etc.)
  - Specific measurements/parameters of interest (pH, DIC, total alkalinity, temperature, salinity, dissolved oxygen, biomass stocks, nutrient levels, CO₂ flux, current speed, wave height, benthic community metrics, etc.)
  - Observation & monitoring programs (MRV telemetry, real-time sensor networks, baseline ecosystem surveys, satellite validation campaigns, automated underwater vehicles, fixed moorings, etc.)
- Explicitly note any gaps or pain points (e.g., “lacks real-time carbonate chemistry data at depth” or “requires high-resolution spatial coverage for licensing”).
- In the metadata JSON-LD file, **always include**:
  ```json
  "url": "https://official-homepage.com/"
  ```
- Save metadata/company-name.jsonld (schema.org Organization) with the URL field populated.

## Data Interests Template (add to every company profile in wiki/)

Every company wiki profile should contain (or link to) a structured **Data & Measurement Needs** section, for example:

### Data & Measurement Needs
- Primary data types: ...
- Key measurements/parameters: ...
- Observation platforms/programs: ...
- Known data gaps: ...
- Interest in external data services: ...

## Phase 4: Compile Wiki (OKF)

- LLM build/update `wiki/` articles: sector overviews, company profiles, concept pages.
- **OKF frontmatter (required)** on every concept file — company example:

  ```yaml
  ---
  type: Company
  title: Ebb Carbon
  description: Electrochemical CDR from brine for ocean alkalinity enhancement.
  resource: https://www.ebbcarbon.com/
  tags: [ocean-carbon-sequestration]
  timestamp: 2026-07-16T00:00:00Z
  sector: Ocean Carbon Sequestration
  date: 2026-07-16
  ---
  ```

  Sector overviews use `type: Sector`. Meta notes under `wiki/concepts/` use `type: Concept`.

- Body near the top (domain convention, keep in addition to frontmatter):
  ```
  **Sector**: ...
  **Official Site**: https://...
  ```
- Cross-links: **relative markdown only** (e.g. `[Ocean Carbon Sequestration](ocean-carbon-sequestration.md)`). Never `[[wikilinks]]` or `/wiki/...` absolute paths.
- Prefer high **cross-link density** between companies and their sector overviews.
- Update `wiki/index.md` when adding companies or sectors (keep progressive disclosure listings current).
- Health check: inconsistencies, new connections.
- **Post-write lint (mandatory):**

  ```bash
  python3 scripts/okf-lint.py
  ```

  Fix any hard failures before commit. Optional domain gate: `python3 scripts/completeness-check.py`.

## Phase 5: Report & Git

- Diff changes since last run.
- terminal('git add .; git commit -m "Daily update $(date +%Y-%m-%d)"'; git push)
- Final report: New companies? Key updates? (e.g., funding rounds). Send to Discord.

## Risks (format)

- **Format drift:** regenerating pages without OKF frontmatter or with `[[wikilinks]]` / `/wiki/` links. Always re-run `okf-lint.py`.
- **Contamination:** `raw/` notes may be free-form; do not copy that style into `wiki/`.

## Verify

```bash
cat sources/companies.json | jq '.[] | {name,url}'
ls -1 raw/ | wc -l
ls -1 wiki/*.md
python3 scripts/okf-lint.py
```
