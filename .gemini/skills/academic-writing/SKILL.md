---
name: academic-writing
description: "write, research, revise, structure, critique, and polish academic work including essays, reports, theses, dissertations, journal articles, literature reviews, research proposals, peer-review responses, mathematical exposition, and reproducible methods/results writeups. use when the user asks for academic writing, real in-text citations, reference lists, literature search, recent peer-reviewed studies, pdf-based evidence gathering, google/google scholar boolean search strategy, citation-style formatting, argument refinement, or publication-quality scholarly style."
---

# Academic Writing

## Purpose

Use this skill to produce rigorous, readable, evidence-backed academic writing. Combine scholarly writing judgment with a careful research workflow: search for relevant sources when needed, parse user-provided or open-access PDFs, synthesize evidence, write with real in-text citations, and format references in the requested style.

The goal is not to make writing sound artificially complex. The goal is to make scholarly work clear, defensible, well-supported, and hard to misread.

## Non-negotiable rules

1. Never invent citations, quotations, page numbers, datasets, equations, theorem names, results, authors, journals, dates, DOIs, URLs, or consensus.
2. Cite only sources that were provided by the user, retrieved from a reliable source, or otherwise verified during the task.
3. Do not create a polished reference entry unless the required metadata has been verified. Omit unavailable fields when allowed by the style; otherwise flag the gap.
4. Prefer primary literature, peer-reviewed work, official reports, standards, and datasets over weak secondary sources.
5. Download or parse only legally accessible/open PDFs, official PDFs, repository PDFs, or user-provided files. Do not use Sci-Hub, piracy mirrors, or bypass access controls.
6. Separate facts, inferences, interpretations, and writing suggestions when the distinction matters.
7. Preserve the user's intended meaning unless explicitly asked to strengthen, challenge, or restructure it.
8. Prefer clarity over ornament. Academic writing should be precise, not inflated.
9. Do not overclaim. Use calibrated verbs such as suggests, indicates, supports, implies, contradicts, extends, or complicates.
10. In mathematical, statistical, or quantitative work, state assumptions, variables, domains, constraints, uncertainty, and edge cases explicitly.
11. If evidence is missing, mark claims with `[citation needed]`, `[evidence needed]`, or `[verify]` rather than fabricating support.
12. When editing code-adjacent academic material, preserve filenames, paths, functions, variables, equations, citations, labels, and cross-references unless there is a clear reason to change them.

## Task router

Classify the user's request before writing. Use the matching workflow.

| User need | Mode | Primary output |
|---|---|---|
| write a paper, essay, section, report | drafting | structured academic prose with evidence discipline |
| write with real citations / references | research-backed drafting | sourced prose, in-text citations, reference list |
| find recent studies / PDFs | research retrieval | Boolean query plan, source matrix, downloaded/open sources when possible |
| literature review | synthesis | themes, gaps, tensions, source matrix, research positioning |
| improve / polish / rewrite | revision | revised text plus key changes if useful |
| make it more academic | style elevation | clearer scholarly register without bloat |
| check logic / argument | argument audit | claim map, weaknesses, fixes |
| proposal / thesis plan | research design | question, contribution, method, chapter plan |
| proof / theorem / math explanation | mathematical exposition | definitions, theorem, proof, intuition, caveats |
| methods / results from code or data | reproducible writeup | method narrative, assumptions, results framing |
| respond to reviewers | peer response | respectful response matrix and revised wording |
| citation formatting / references | citation formatting | formatted citations only from provided or verified sources |

If the request spans modes, perform them in this order: diagnose, research/retrieve if required, parse sources, structure, draft or revise, audit, polish.

## Intake checklist

For complex work, infer what is obvious and ask only for genuinely missing essentials. If the user wants immediate output, proceed with reasonable assumptions and state them briefly.

Capture these fields when available:

```yaml
task_type: draft | revise | critique | outline | proof | literature_review | proposal | reviewer_response | methods_writeup | research_report
discipline: mathematics | linguistics | computer_science | social_science | humanities | natural_science | interdisciplinary | unknown
audience: undergraduate | graduate | supervisor | journal_reviewers | general_academic | policy | unknown
citation_style: apa7 | mla9 | chicago_author_date | chicago_notes | ieee | harvard | vancouver | bibtex | user_defined | unknown
source_status: provided | partial | not_provided | must_verify
research_depth: quick | standard | deep
recency_window: user_defined | last_5_years | last_10_years | seminal_plus_recent | unknown
output_format: prose | outline | latex | markdown | docx_text | table | json | yaml | code_commentary
strictness: grammar_only | light_edit | developmental_edit | rewrite | original_draft
```

Default assumptions when unspecified: APA 7, last 5 years plus seminal older work, 6-12 high-quality sources for a short report, and open-access PDFs only.

## Research-backed writing workflow

Use this workflow when the user asks for real citations, recent studies, PDFs, literature reviews, research reports, or reference lists.

1. **Define the research scope.** Identify topic, discipline, research question, audience, source count, recency window, and citation style.
2. **Create a project folder.** Use `scripts/create_research_project.py` when code execution is available. Store searches, PDFs, extracted text, paper notes, synthesis files, and outputs separately.
3. **Generate Boolean query families.** Use concept groups, synonyms, methods, population, outcomes, and source filters. See `references/research-pipeline.md`.
4. **Search.** Use available web/search tools. Use Google-style Boolean operators where supported. Use Google Scholar only when an available browser/search surface permits it; otherwise approximate with web search plus academic repositories.
5. **Screen results.** Prefer peer-reviewed, recent, relevant, full-text accessible sources. Record exclusions when doing a deep task.
6. **Download PDFs where lawful and possible.** Save open-access PDFs to the project `pdfs/` folder. If only an abstract page is accessible, label it as abstract-only.
7. **Parse sources one by one.** Use `scripts/extract_pdfs.py` for local PDFs when available. For web PDFs, inspect text and use screenshot/visual inspection for tables, figures, or diagrams when the environment supports it.
8. **Create per-paper notes.** For each source, summarize purpose, methods, data/sample, key findings, limitations, relevance, and safe citeable claims.
9. **Build a source matrix and claim-evidence map.** Every major report claim must point to one or more parsed/verified sources.
10. **Draft synthesis.** Compare sources by themes, methods, evidence quality, agreement, disagreement, and gaps. Avoid one-source-per-paragraph summaries unless requested.
11. **Apply citation style.** Use in-text citations and a reference list in the requested style. See `references/citation-styles.md`.
12. **Run the final audit.** Check every in-text citation against the reference list, every reference against verified metadata, and every major claim against the evidence map.

## Search requirements

When research is required, do not rely on general memory. Search with Boolean queries and record what was searched. Good queries combine concepts, synonyms, and constraints:

```text
("concept a" OR synonym1 OR synonym2) AND ("concept b" OR synonym3) AND (method OR outcome) filetype:pdf after:2020
```

Use source filters where appropriate:

```text
site:arxiv.org
site:aclanthology.org
site:pmc.ncbi.nlm.nih.gov
site:openreview.net
site:nber.org
site:oecd.org
site:who.int
site:gov
filetype:pdf
intitle:"systematic review"
```

Do not pretend Google Scholar was searched if it was not available. Say which search surfaces were actually used.

## Evidence and citation policy

Use this hierarchy when judging evidence:

1. User-provided sources, datasets, notes, instructions, and rubric.
2. Primary literature, peer-reviewed papers, official documentation, standards, statutes, datasets, or archival material.
3. Peer-reviewed secondary scholarship, systematic reviews, meta-analyses, and academic books.
4. Reputable reports, institutional pages, and official statistics.
5. High-quality journalism or industry reports only when appropriate.
6. General background knowledge only for stable, non-controversial context.

Rules:

- Do not cite a source unless it was verified or provided.
- Do not cite search snippets as if they were full papers.
- Do not fill in DOI, volume, issue, page range, publisher, URL, or conference details from memory.
- For direct quotations, include a page, section, paragraph, or other locator when available.
- For literature reviews, synthesize relationships among sources instead of listing summaries one by one.
- For controversial topics, represent disagreement directly and do not force false consensus.
- For preprints, label them as preprints when relevant to the assignment or citation style.

## Citation style support

Support APA 7, MLA 9, Chicago author-date, Chicago notes-bibliography, IEEE, Harvard, Vancouver, and BibTeX/LaTeX. Consult `references/citation-styles.md` when formatting citations or references.

If the citation style is unknown, default to APA 7 for general academic prose and BibTeX-style keys for LaTeX or technical writing.

## Academic argument standards

A strong academic paragraph usually contains:

1. Topic sentence: one precise claim.
2. Context: why the claim matters.
3. Evidence: source, data, proof, example, or textual detail.
4. Warrant: reasoning that connects evidence to the claim.
5. Qualification: boundary, limitation, or counterpoint if needed.
6. Transition: link to the next step in the argument.

When improving arguments, look for undefined terms, missing warrants, overbroad claims, unsupported causal language, ignored counterarguments, ambiguous pronouns, and topic drift.

## Mathematical and quantitative writing standards

Use the mathematician's lens when the work includes mathematics, formal logic, statistics, algorithms, or theoretical claims.

- Define every symbol before using it unless standard for the target audience.
- State domains, quantifiers, assumptions, constraints, and boundary cases.
- Keep notation stable.
- Distinguish equality, approximation, implication, equivalence, proportionality, correlation, prediction, and causation.
- Report what was measured, how it was measured, and under what assumptions.
- Avoid saying empirical results "prove" a claim unless a formal proof exists.
- Distinguish statistical significance, practical significance, effect size, uncertainty, and model fit.

Default proof structure:

```markdown
**Definition.** [Term and conditions.]
**Assumptions.** [Domain, regularity, independence, boundary, or data assumptions.]
**Claim/Theorem.** [Precise statement.]
**Proof.** [Stepwise argument with justified transformations.]
**Intuition.** [Plain-language explanation after, not instead of, the proof.]
```

## Linguistic writing standards

Use the linguist's lens for grammar, discourse, register, and meaning.

- Prefer precise nouns and strong verbs over abstract filler.
- Reduce stacked nominalizations when they obscure agency.
- Use passive voice when the actor is unknown, irrelevant, or conventionally omitted; use active voice when agency matters.
- Keep old information before new information where possible.
- Avoid synonym-chasing for technical terms. Repetition is acceptable when it preserves precision.
- Do not make prose sound archaic, pompous, or mechanically "academic."

## File and code behavior

When code execution or local files are available:

- Inspect existing files before modifying them.
- Preserve directory structure, filenames, citation keys, LaTeX labels, equation labels, figure labels, and cross-references.
- Prefer small, reviewable edits over destructive rewrites.
- Do not modify source data, raw notes, or bibliography files unless the user asks.
- Use `scripts/create_research_project.py` to initialize research projects.
- Use `scripts/extract_pdfs.py` to extract local PDF text and create per-paper note templates.
- For LaTeX, preserve `\cite{}`, `\ref{}`, `\label{}`, `\begin{}`, and `\end{}`.
- When adding equations, define symbols immediately before or after the equation.

## Default output templates

### Research-backed report

```markdown
# [Title]

## Executive summary
[Best-supported conclusion first, with citations.]

## Background and scope
[Definitions, scope, and why the question matters.]

## Evidence synthesis
### Theme 1: [Name]
[Compare sources, methods, findings, and limitations.]

### Theme 2: [Name]
[Compare sources, methods, findings, and limitations.]

## Gaps and limitations
[What remains uncertain and why.]

## Conclusion
[Bounded conclusion, no overclaiming.]

## References
[Formatted in requested style.]
```

### Literature review synthesis

```markdown
## Synthesis

### Theme 1: [Name]
[Compare sources, not just summarize them.]

### Theme 2: [Name]
[Identify convergence, disagreement, methods, and evidence quality.]

### Gap
[State what remains unresolved and why it matters.]

### Positioning
[Explain how the user's project responds to the gap.]

## References
[Requested citation style.]
```

### Revision response

```markdown
## Revised version

[Revised text]

## Key improvements

- [Specific change and why it helps]
- [Specific change and why it helps]
- [Any remaining citation/evidence gap]
```

### Peer-review response

```markdown
| Reviewer comment | Response strategy | Manuscript change |
|---|---|---|
| [Comment] | [Accept, clarify, respectfully disagree, or partly accept] | [Exact section or proposed wording] |

**Response:** Thank you for this helpful comment. [Direct answer.] We have revised [section] to [change].
```

## Editing levels

Match the user's requested strictness.

- **Grammar-only:** fix grammar, punctuation, tense, agreement, spelling, and obvious word choice only.
- **Light academic polish:** improve flow, clarity, transitions, concision, and scholarly tone while preserving meaning.
- **Developmental edit:** reorganize argument, paragraph order, headings, and evidence placement.
- **Full rewrite:** rebuild for academic strength while preserving the intended thesis and stating assumptions.

## Final quality gate

Before finalizing, check:

```python
quality_gate = {
    "thesis_clear": True,
    "claims_supported": True,
    "scope_qualified": True,
    "terms_defined": True,
    "citations_verified": True,
    "references_match_in_text_citations": True,
    "no_fabricated_metadata": True,
    "math_logic_valid_or_flagged": True,
    "register_appropriate": True,
    "grammar_clean": True,
    "format_preserved": True,
    "user_constraints_satisfied": True,
}
```

If any item is false, either fix it or explicitly flag the issue.
