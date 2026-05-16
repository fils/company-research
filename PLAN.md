# Company Research Daily Workflow (Phases 1-5)

Run from workdir ~/projects/company-research.

## Phase 1: Update Sources
- read_file('sources/companies.json') or create if missing. Every entry MUST include:
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

## Phase 4: Compile Wiki
- LLM build/update wiki/ articles: sector overviews, company profiles, concept pages (e.g., 'Ocean MRV').
- Every company profile `.md` file **must start with** or contain near the top:
  ```
  **Sector**: ...
  **Official Site**: https://...
  ```
- Add backlinks/summaries.
- Health check: inconsistencies, new connections.

## Phase 5: Report & Git
- Diff changes since last run.
- terminal('git add .; git commit -m "Daily update $(date +%Y-%m-%d)"'; git push)
- Final report: New companies? Key updates? (e.g., funding rounds). Send to Discord.

Verify: 
```bash
cat sources/companies.json | jq '.[] | {name,url}'
ls -1 raw/ | wc -l
ls -1 wiki/*.md
````
