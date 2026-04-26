# Research Pipeline Reference

Use this reference when the user asks for well-researched academic writing with real in-text citations, references, recent studies, PDF papers, literature reviews, reports, theses, proposals, or evidence-backed sections.

## Default research assumptions

If the user does not specify constraints, use these defaults and state them briefly:

- citation style: APA 7
- recency window: last 5 years, plus older seminal sources only when clearly necessary
- source target: 6-12 high-quality sources for a short report, 12-25 for a longer literature review
- source type: peer-reviewed papers and official datasets/reports first
- access: open-access PDFs only unless the user supplies files or citations
- output: synthesized academic prose with in-text citations and a formatted reference list

## Research project folder

For substantial research tasks, create a separate project folder before downloading or parsing sources.

Recommended structure:

```text
/mnt/data/academic_research_projects/<project_slug>/
├── searches/
│   ├── boolean_queries.md
│   ├── search_log.csv
│   └── screening_decisions.csv
├── pdfs/
│   └── downloaded PDFs
├── extracted/
│   ├── full_text/
│   ├── metadata/
│   └── paper_notes/
├── synthesis/
│   ├── source_matrix.csv
│   ├── claim_evidence_map.md
│   └── literature_themes.md
├── outputs/
│   ├── report.md
│   ├── references.md
│   └── bibliography.bib when useful
└── manifest.json
```

Use `scripts/create_research_project.py` to create this structure when code execution is available.

## Boolean query design

Build several query families instead of relying on one search. Combine concepts, synonyms, methods, and source filters.

### Core Boolean pattern

```text
("concept a" OR synonym1 OR synonym2) AND ("concept b" OR synonym3) AND (method OR population OR outcome)
```

### Google-style operators

Use these where supported by the available web/search tool:

- exact phrase: `"machine learning"`
- alternatives: `(misinformation OR "fake news" OR disinformation)`
- require term: `+classifier`
- remove noise: `-blog -slides -course`
- PDF targeting: `filetype:pdf`
- source targeting: `site:arxiv.org`, `site:aclanthology.org`, `site:pmc.ncbi.nlm.nih.gov`, `site:papers.ssrn.com`, `site:openreview.net`, `site:nber.org`, `site:who.int`, `site:oecd.org`, `site:un.org`, `site:gov`
- title targeting: `intitle:review`, `intitle:"systematic review"`
- date targeting when supported: `after:2020`, `before:2026`

### Example query bank

For a topic such as misinformation detection:

```text
("misinformation" OR "fake news" OR disinformation) AND ("machine learning" OR classifier OR "deep learning") filetype:pdf after:2020
("misinformation detection" OR "fake news detection") AND (sentiment OR emotion OR engagement) filetype:pdf after:2020
("fake news detection" AND "social media") site:arxiv.org after:2020
("misinformation" AND "social media" AND "systematic review") filetype:pdf after:2020
("fake news" AND transformer AND classification) site:aclanthology.org
```

## Search and screening workflow

1. Translate the user's topic into 3-6 concept groups.
2. Generate 8-20 Boolean queries.
3. Search across general web, Google-style web search, Google Scholar when available, and discipline-specific repositories where available.
4. Prefer direct PDFs from publishers, universities, official repositories, or recognized preprint archives.
5. Create `search_log.csv` with: query, date searched, search source, result title, URL, PDF URL, year, venue, notes.
6. Screen each result using title, abstract, year, venue, methods, relevance, and availability.
7. Record exclusions in `screening_decisions.csv`; do not silently drop borderline papers.
8. Download only legally accessible/open PDFs or user-supplied PDFs.
9. Parse each PDF and create one paper note per source before writing.
10. Write from the parsed evidence, not from search snippets alone.

## Source quality hierarchy

Rank sources in this order:

1. Peer-reviewed journal articles, conference papers, systematic reviews, meta-analyses.
2. Official datasets, standards, government/regulator reports, institutional technical reports.
3. Reputable preprints from arXiv, SSRN, medRxiv/bioRxiv, OpenReview, or university repositories, clearly labeled as preprints.
4. Academic books and edited volumes.
5. High-quality industry reports only when the topic requires industry evidence.
6. News or blog material only for context, never as the main scholarly evidence unless the assignment explicitly allows it.

Do not use predatory journals, uncited essay sites, random PDFs without authorship, or AI-generated web pages as scholarly evidence.

## PDF download rules

- Download only open-access papers, official PDFs, repository PDFs, or user-provided files.
- Do not use Sci-Hub, piracy mirrors, or bypass access controls.
- If only an abstract page is available, record the source as `abstract-only` and do not claim to have parsed the full paper.
- Preserve original filenames when meaningful, but prefix with a stable source number, for example `S03_author_short_title_2023.pdf`.
- Save metadata beside the PDF when possible.

## Per-paper parsing template

Create a note for each source before synthesis:

```markdown
# S01 - [Short title]

## Bibliographic metadata
- authors:
- year:
- title:
- venue:
- doi/url:
- source type: peer-reviewed | preprint | official report | book | other
- access status: full-pdf parsed | html parsed | abstract-only | user-provided

## Research purpose
[What question or problem does the source address?]

## Data and methods
[Dataset, sample, design, model, variables, measures, analysis method.]

## Key findings
- [Finding with page/section evidence where available]
- [Finding with page/section evidence where available]

## Limitations stated by authors
- [Limitations]

## Relevance to user topic
[How this source supports, complicates, or contradicts the user's argument.]

## Safe citation claims
- Claim: [A sentence that can be cited to this source]
  Evidence: [page/section/quote/paraphrase]
```

## Synthesis workflow

After all papers are parsed:

1. Build a source matrix with rows as sources and columns as theory, method, dataset, findings, limitations, and relevance.
2. Group papers into themes based on findings and methods, not merely chronology.
3. Identify convergence, disagreement, methodological weaknesses, and research gaps.
4. Create a claim-evidence map: every major claim in the report must point to one or more parsed sources.
5. Draft sections using synthesized claims with in-text citations.
6. Produce a reference list in the requested style.
7. Run a final citation audit: every in-text citation must have a reference entry; every reference entry must be cited unless the user requests a bibliography.

## Citation audit checklist

Before final output, verify:

- all in-text citations correspond to parsed or verified sources
- no citations were invented from memory
- each reference entry contains only verified metadata
- preprints are labeled when the style or context requires it
- direct quotations include page numbers when available
- claims from abstract-only sources are limited and labeled
- old sources are used only as seminal/background sources, not as current evidence
- source limitations are reflected in the prose
